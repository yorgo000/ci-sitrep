#!/usr/bin/env python3
"""verify.py — post-change verification for the CI SITREP report.

Run after regenerating index.html and BEFORE pushing. Checks the Markdown
source (SYNTHESIZED.md) and the generated HTML against the editorial rules
in RULES.md.

Usage:
    python3 verify.py [SYNTHESIZED.md] [index.html]
    (defaults: ~/workspace/ci-sitrep/SYNTHESIZED.md and index.html)

Exit 0: no FAILs (warnings are printed but do not block).
Exit 1: at least one FAIL — fix the cause, regenerate, re-run. Do not push
        a failing build.

FAILs are structural or factual defects (missing Source, missing rating,
broken anchor, stale date, wrong company name, literal Markdown in HTML).
WARNINGs are judgment items that need a human/worker review (rating/source
consistency, source-first pattern candidates, link-check failures — some
sites, especially Medium, block curl while loading fine in a browser).
"""

import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import date, timedelta
from pathlib import Path
from urllib.parse import urlparse

# --- Configuration -----------------------------------------------------------

CANONICAL_SECTIONS = {
    "1": "Pre-commit: CI-generated code sanitizing",
    "2": "In codebase: Sanitizing post-commit of CI-generated code",
    "3": "Agentic: CIC Design, Build, Deployment",
}
RATINGS = ["\u25cf\u25cf\u25cf\u25cf", "\u25cf\u25cf\u25cf\u25cb",
           "\u25cf\u25cf\u25cb\u25cb", "\u25cf\u25cb\u25cb\u25cb"]
# Headlines whose parenthetical legitimately carries no link.
UNLINKED_HEADLINE_EXCEPTIONS = [
    "Adoption is already majority-AI",
    "Real incidents",
]
# The one bare "Confluence" that is correct: the Atlassian product, in the
# §2.3 AWS Security Agent table row.
ALLOWED_BARE_CONFLUENCE = "GitHub/GitLab/Bitbucket + Confluence; Kiro and Claude Code plugin"
# Strings that must never appear on the public page (internal process).
# Each entry: (regex, label, case_sensitive). PENDING is case-sensitive:
# the ordinary word "pending" is legitimate prose; the matter inbox is
# always uppercase PENDING.md.
FORBIDDEN = [
    (r"\bTODO\b", "TODO", False),
    (r"\bFIXME\b", "FIXME", False),
    (r"\bBarnaby\b", "Barnaby", False),
    (r"\bcron\b", "cron", False),
    (r"\bPENDING\b", "PENDING", True),
    (r"watch-subjects", "watch-subjects", False),
    (r"Muse Spark", "Muse Spark", False),
]
# HTML markers that must be present (layout/design integrity).
HTML_MARKERS = [
    ("as-of-banner", "As-of banner"),
    ("toc-inline", "mobile inline Contents"),
    ("Confidence rating", "confidence legend heading"),
    ("Confluence<1> Corp. All rights reserved", "copyright line"),
    ("makeShareButton", "share-link buttons"),
    ("back-to-top", "back-to-top button"),
    ("situation-at-hand", "Situation at hand section"),
    ("search-box", "Search box"),
    ("search-input", "Search input"),
    ("glossary.html", "Glossary nav link"),
    ("def-tip", "Tooltip element"),
    ("How to read this", "How-to-read block"),
    ("executive-dashboard", "Executive dashboard top-level section"),
    ('id="report"', "Report top-level section"),
    ("sec-controls", "Sections control in main content"),
    ("dash-panel", "dashboard panels embedded"),
    ("bottom-line-strip", "dashboard bottom-line strip"),
]
# Primary regulator/government domains (for the rating-consistency warning).
REGULATOR_DOMAINS = [
    "occ.gov", "federalreserve.gov", "fdic.gov", "finra.org", "sec.gov",
    "cftc.gov", "mas.gov.sg", "hkma.gov.hk", "sfc.hk", "gov.uk",
    "gov.ca.gov", "eba.europa.eu", "eiopa.europa.eu", "bis.org",
    "fsb.org", "ncua.gov", "treasury.gov",
]
VENDOR_LABELS = ["[VENDOR CLAIM]", "[VENDOR RESEARCH]", "[VENDOR-COMMISSIONED]",
                 "[VENDOR STUDY]", "[VENDOR TECHNICAL POST]", "[VENDOR DATA]"]
SOURCE_FIRST_VERBS = r"(found|reported|says|said|published|announced|claims|concludes|shows)"

# --- Result collection -------------------------------------------------------

results = []  # (level, check, detail)  level in FAIL / WARN / PASS


def fail(check, detail):
    results.append(("FAIL", check, detail))


def warn(check, detail):
    results.append(("WARN", check, detail))


def ok(check, detail=""):
    results.append(("PASS", check, detail))


# --- Helpers -----------------------------------------------------------------

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def md_links(s):
    return re.findall(r"\[[^\]]*\]\((https?://[^)]+)\)", s)


def parse_ntw_date(s):
    return date.fromisoformat(s)


def parse_watch_date(s):
    """Parse 'Wed 16 Dec 2026', '1 Feb 2027', 'Dec 2027' -> (date, is_month_only)."""
    s = s.strip()
    months = {m: i + 1 for i, m in enumerate(
        ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}
    m = re.match(r"(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s+(\d{1,2})\s+([A-Za-z]{3})\s+(\d{4})", s)
    if m:
        return date(int(m.group(3)), months[m.group(2)], int(m.group(1))), False
    m = re.match(r"(\d{1,2})\s+([A-Za-z]{3})\s+(\d{4})", s)
    if m:
        return date(int(m.group(3)), months[m.group(2)], int(m.group(1))), False
    m = re.match(r"([A-Za-z]{3})\s+(\d{4})", s)
    if m:  # month-only: stale only after the month ends
        y, mo = int(m.group(2)), months[m.group(1)]
        if mo == 12:
            return date(y, 12, 31), True
        return date(y, mo + 1, 1) - timedelta(days=1), True
    return None, False


# --- Main checks -------------------------------------------------------------

def check_articles(md):
    """Every article: one Source bullet, one rating, linked parenthetical."""
    details = re.findall(r"<details>.*?<summary>(.*?)</summary>(.*?)</details>",
                         md, re.DOTALL)
    articles = [(s, b) for s, b in details if "<strong>" in s]
    n = len(articles)
    sources = len(re.findall(r"^- Source: \[", md, re.MULTILINE))
    if sources == n:
        ok("articles == Source bullets", f"{n} articles, {n} Source bullets")
    else:
        fail("articles == Source bullets", f"{n} articles but {sources} Source bullets")

    # Ratings
    dist = {r: 0 for r in RATINGS}
    unrated = []
    for summary, _ in articles:
        found = [r for r in RATINGS if r in summary]
        if len(found) == 1:
            dist[found[0]] += 1
        else:
            unrated.append(strip_tags(summary)[:80])
    if not unrated:
        ok("every article has exactly one confidence rating",
           " ●●●● %d / ●●●○ %d / ●●○○ %d / ●○○○ %d" % tuple(dist[r] for r in RATINGS))
    else:
        fail("every article has exactly one confidence rating",
             f"{len(unrated)} without exactly one rating: {unrated[:3]}")

    # Headline parenthetical links
    unlinked = []
    for summary, _ in articles:
        plain = strip_tags(summary)
        if any(e in plain for e in UNLINKED_HEADLINE_EXCEPTIONS):
            continue
        m = re.search(r"\((.*)\)", summary)
        if not m or "[" not in m.group(1):
            unlinked.append(plain[:80])
    if not unlinked:
        ok("headline parenthetical source is hyperlinked",
           f"{n - len(UNLINKED_HEADLINE_EXCEPTIONS)}/{n} linked "
           f"({len(UNLINKED_HEADLINE_EXCEPTIONS)} documented exceptions)")
    else:
        fail("headline parenthetical source is hyperlinked",
             f"{len(unlinked)} unlinked: {unlinked[:3]}")

    # Duplicate headlines
    heads = [strip_tags(s).strip() for s, _ in articles]
    dupes = sorted({h for h in heads if heads.count(h) > 1})
    if not dupes:
        ok("no duplicate article headlines", f"{n} unique")
    else:
        fail("no duplicate article headlines", f"{len(dupes)} duplicated: {dupes[:3]}")

    return articles


def check_rating_consistency(articles):
    """Warnings: rating vs source type mismatches worth a human look."""
    for summary, body in articles:
        plain = strip_tags(summary)
        m = re.search(r"- Source: \[[^\]]*\]\((https?://[^)]+)\)", body)
        url = m.group(1) if m else ""
        host = urlparse(url).netloc.lower()
        rating = next((r for r in RATINGS if r in summary), None)
        if not rating or not url:
            continue
        if "arxiv.org" in host and rating == "\u25cf\u25cf\u25cf\u25cf":
            warn("rating/source consistency",
                 f"arXiv preprint rated Established: {plain[:70]}")
        if any(host.endswith(d) for d in REGULATOR_DOMAINS) \
                and rating in ("\u25cf\u25cf\u25cb\u25cb", "\u25cf\u25cb\u25cb\u25cb") \
                and "survey" not in plain.lower():
            warn("rating/source consistency",
                 f"primary regulator source rated below Corroborated: {plain[:70]}")
        if any(v in plain for v in VENDOR_LABELS) \
                and rating in ("\u25cf\u25cf\u25cf\u25cf", "\u25cf\u25cf\u25cf\u25cb"):
            warn("rating/source consistency",
                 f"vendor-labelled article rated above Reported: {plain[:70]}")


def check_freshness(md):
    """New in the last 7 days: 7-day window, newest first. What we're watching: no past dates, soonest first."""
    today = date.today()

    ntw = re.search(r"## New in the last 7 days\n(.*?)\n## What we're watching",
                    md, re.DOTALL)
    if not ntw:
        fail("New in the last 7 days section present", "section not found")
    else:
        dates = re.findall(r"^- \*\*(\d{4}-\d{2}-\d{2}) —", ntw.group(1), re.MULTILINE)
        parsed = [parse_ntw_date(d) for d in dates]
        stale = [d for d in parsed if d < today - timedelta(days=7)]
        if not stale:
            ok("New in the last 7 days: no entry older than 7 days", f"{len(parsed)} entries")
        else:
            fail("New in the last 7 days: no entry older than 7 days",
                 f"stale: {[str(d) for d in stale]}")
        if parsed == sorted(parsed, reverse=True):
            ok("New in the last 7 days: newest first")
        else:
            fail("New in the last 7 days: newest first", "entries out of order")

    www = re.search(r"## What we're watching\n(.*?)\n## Contents", md, re.DOTALL)
    if not www:
        fail("What we're watching section present", "section not found")
    else:
        items = re.findall(r"^- \*\*(.+?)\*\* —", www.group(1), re.MULTILINE)
        dated = []
        for item in items:
            d, _ = parse_watch_date(item)
            if d:
                dated.append((item, d))
        past = [(i, d) for i, d in dated if d < today]
        if not past:
            ok("What we're watching: no past dates", f"{len(dated)} dated items")
        else:
            fail("What we're watching: no past dates",
                 f"past: {[i for i, _ in past]}")
        ds = [d for _, d in dated]
        if ds == sorted(ds):
            ok("What we're watching: soonest first")
        else:
            fail("What we're watching: soonest first", "dated items out of order")

    m = re.search(r"\*\*Last updated:\*\* (\d{4}-\d{2}-\d{2})", md)
    if not m:
        fail("Last updated line present", "line not found")
    else:
        d = parse_ntw_date(m.group(1))
        if d > today:
            fail("Last updated is not in the future", str(d))
        else:
            ok("Last updated is not in the future", str(d))
        if d < today - timedelta(days=7):
            warn("Last updated is over 7 days old",
                 f"{d} — a week with no material change; confirm the watch ran")


def check_structure(md):
    """Section names, section order, subsection order."""
    h2s = re.findall(r"^## (.+)$", md, re.MULTILINE)
    for num, name in CANONICAL_SECTIONS.items():
        want = f"{num}. {name}"
        if want in h2s:
            ok(f"section {num} name", want)
        else:
            fail(f"section {num} name",
                 f"expected '{want}'; H2s found: {[h for h in h2s if h.startswith(num + '.')]}")

    order = ["Situation at hand", "New in the last 7 days", "What we're watching", "Contents",
             "1. ", "2. ", "3. ", "Archive"]
    pos = []
    for o in order:
        i = md.find(f"## {o}")
        pos.append(i)
    if all(p >= 0 for p in pos) and pos == sorted(pos):
        ok("section order", "Situation at hand < New in the last 7 days < What we're watching < Contents < §1 < §2 < §3 < Archive")
    else:
        fail("section order", f"positions: {dict(zip(order, pos))}")

    for sec, subs in (("1", range(1, 8)), ("2", range(1, 8)), ("3", range(1, 9))):
        want = [f"{sec}.{i}" for i in subs]
        got = [h.split(" ", 1)[0] for h in
               re.findall(r"^### (.+)$", md, re.MULTILINE)
               if h.startswith(f"{sec}.")]
        if got == want:
            ok(f"§{sec} subsection order", " ".join(f"{sec}.{i}" for i in subs))
        else:
            fail(f"§{sec} subsection order", f"expected {want}, found {got}")

    h4s = [h for h in re.findall(r"^#### (.+)$", md, re.MULTILINE)
           if h.startswith("3.4.")]
    if h4s == ["3.4.1 The converged control pattern",
              "3.4.2 Regulation",
              "3.4.3 The governance gap"]:
        ok("§3.4 subsection order", "3.4.1 < 3.4.2 < 3.4.3")
    else:
        fail("§3.4 subsection order", f"found: {h4s}")


def check_top_level(html):
    """Two top-level sections, dashboard first, report second."""
    no_script = re.sub(r"<script>.*?</script>", "", html, flags=re.DOTALL)
    ed = no_script.find('id="executive-dashboard"')
    rep = no_script.find('id="report"')
    sotm = no_script.find('id="situation-at-hand"')
    if ed == -1 or rep == -1 or sotm == -1:
        fail("top-level sections present",
             f"executive-dashboard={ed}, report={rep}, situation-at-hand={sotm}")
    elif ed < rep < sotm:
        ok("top-level sections order",
           "Executive dashboard < Report < Situation at hand")
    else:
        fail("top-level sections order",
             f"positions: executive-dashboard={ed}, report={rep}, "
             f"situation-at-hand={sotm}")


def glossary_key(short):
    """Alphabetical sort key for a glossary term: lowercased, punctuation
    stripped (so CI/CD sorts as 'cicd', after CIC)."""
    return re.sub(r"[^a-z0-9]", "", short.lower())


def parse_glossary_terms(src):
    """(term, short, slug) for each **Term** — definition entry."""
    terms = []
    for block in re.split(r"\n\n+", src):
        block = block.strip()
        if not block.startswith("**"):
            continue
        m = re.match(r"\*\*(.+?)\*\*\s*—\s*(.*)", block, re.DOTALL)
        if not m:
            continue
        term = m.group(1).strip()
        short = term.split(" (")[0]
        slug = re.sub(r"[^a-z0-9]+", "-", short.lower()).strip("-")
        terms.append((term, short, slug))
    return terms


def check_glossary(md_path, html):
    """GLOSSARY.md exists, is alphabetical, has no naming slips, and every
    term is present both in the tooltip data (index.html) and as an anchored
    entry on the glossary page (glossary.html)."""
    repo = md_path.parent
    g_path = repo / "GLOSSARY.md"
    if not g_path.exists():
        fail("GLOSSARY.md exists", f"missing: {g_path} — tooltips would be empty")
        return
    ok("GLOSSARY.md exists")
    g_src = g_path.read_text()
    terms = parse_glossary_terms(g_src)
    if not terms:
        fail("glossary has entries", "no **Term** — definition blocks found")
        return
    ok("glossary has entries", f"{len(terms)} terms")
    shorts = [s for _, s, _ in terms]
    if shorts == sorted(shorts, key=glossary_key):
        ok("glossary is alphabetical")
    else:
        ordered = sorted(shorts, key=glossary_key)
        first_bad = next(i for i, (a, b) in enumerate(zip(shorts, ordered)) if a != b)
        fail("glossary is alphabetical",
             f"'{shorts[first_bad]}' should come after '{ordered[first_bad]}'")
    slugs = [s for _, _, s in terms]
    dupes = sorted({s for s in slugs if slugs.count(s) > 1})
    if not dupes:
        ok("glossary slugs unique")
    else:
        fail("glossary slugs unique", f"duplicates: {dupes}")
    if "Confluence 1" in g_src:
        fail("Glossary: no 'Confluence 1'", "found 'Confluence 1'")
    else:
        ok("Glossary: no 'Confluence 1'")
    bare = list(re.finditer(r"Confluence(?!<1>)", g_src))
    if not bare:
        ok("Glossary: no bare 'Confluence'")
    else:
        fail("Glossary: no bare 'Confluence'", f"{len(bare)} occurrences")
    # Tooltip data in index.html must carry every term.
    missing_data = [s for s in slugs if f'"slug": "{s}"' not in html]
    if not missing_data:
        ok("tooltip data carries every term", f"{len(slugs)} slugs in index.html")
    else:
        fail("tooltip data carries every term", f"missing: {missing_data[:5]}")
    # The glossary page must anchor every entry.
    g_html_path = repo / "glossary.html"
    if not g_html_path.exists():
        fail("glossary.html exists", "missing — rebuild with build_page.py")
        return
    g_html = g_html_path.read_text()
    missing_ids = [s for s in slugs if f'<p id="{s}">' not in g_html]
    if not missing_ids:
        ok("glossary page anchors every entry", f"{len(slugs)} ids in glossary.html")
    else:
        fail("glossary page anchors every entry", f"missing: {missing_ids[:5]}")


def check_naming(md, html):
    """Confluence<1> everywhere (one documented exception); no 'Confluence 1';
    the brand is all-caps 'CI SITREP' (no mixed-case 'CI Sitrep').
    NOTE: the mixed-case literal below is intentional — it is the string
    this check looks for. Do not 'fix' it in a global rename."""
    for label, text in (("Markdown", md), ("HTML", html)):
        if "Confluence 1" in text:
            fail(f"{label}: no 'Confluence 1'", "found 'Confluence 1'")
        else:
            ok(f"{label}: no 'Confluence 1'")
        if "CI Sitrep" in text:
            fail(f"{label}: brand is all-caps 'CI SITREP'",
                 "found mixed-case 'CI Sitrep'")
        else:
            ok(f"{label}: brand is all-caps 'CI SITREP'")
        bare = [(m.start(), text[max(0, m.start() - 40):m.start() + 30])
                for m in re.finditer(r"Confluence(?!<1>)", text)]
        # Remove the one allowed Atlassian mention.
        bare = [b for b in bare if ALLOWED_BARE_CONFLUENCE.split(" + ")[1].split(";")[0] not in b[1]
                or "GitHub/GitLab/Bitbucket" not in b[1]]
        if not bare:
            ok(f"{label}: no bare 'Confluence'", "only the documented Atlassian exception")
        else:
            fail(f"{label}: no bare 'Confluence'",
                 f"{len(bare)} occurrences, e.g. ...{bare[0][1]}...")


def check_hygiene(md, html):
    """No internal-process text on the public page."""
    for label, text in (("Markdown", md), ("HTML", html)):
        found = []
        for pat, name, case_sensitive in FORBIDDEN:
            flags = 0 if case_sensitive else re.IGNORECASE
            if re.search(pat, text, flags):
                found.append(name)
        if not found:
            ok(f"{label}: no internal-process strings")
        else:
            fail(f"{label}: no internal-process strings", f"found: {found}")


def check_html(html):
    """Literal Markdown links, anchors, layout markers."""
    # Strip <script> blocks first: JS string literals contain href="#..."
    # fragments (e.g. the breadcrumb builder's '<a href="#' + a.id + '">')
    # that are not real links and would false-positive the anchor check.
    no_script = re.sub(r"<script>.*?</script>", "", html, flags=re.DOTALL)
    literal = re.findall(r"\[[^\]]*\]\(https?://[^)]+\)", no_script)
    if not literal:
        ok("no literal Markdown links in HTML")
    else:
        fail("no literal Markdown links in HTML", f"{len(literal)} found, e.g. {literal[:2]}")

    ids = set(re.findall(r'id="([^"]+)"', no_script))
    # Article ids are assigned at runtime by the share JS (from the
    # headline), so they are not in the static HTML — accept the ids the
    # page will assign, computed the same way build_dashboard does.
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_dashboard
    ids |= set(build_dashboard.compute_article_ids(no_script))
    hrefs = set(re.findall(r'href="#([^"]+)"', no_script))
    missing = sorted(h for h in hrefs if h not in ids)
    if not missing:
        ok("all internal anchors resolve", f"{len(hrefs)} links, {len(ids)} ids")
    else:
        fail("all internal anchors resolve", f"missing: {missing}")

    # Markers run on the full HTML: some (makeShareButton) live in the JS.
    for marker, label in HTML_MARKERS:
        if marker in html:
            ok(f"layout marker present: {label}")
        else:
            fail(f"layout marker present: {label}", f"'{marker}' not found")


def check_source_first(md):
    """Warnings: candidate source-first segments for a human to eyeball."""
    # Exclude the Contents section (its lines are links by design).
    body = re.sub(r"## Contents\n.*?\n---", "", md, flags=re.DOTALL)
    for i, line in enumerate(body.splitlines(), 1):
        if re.match(rf"^- [A-Z][A-Za-z'’ /&.-]{{2,50}} {SOURCE_FIRST_VERBS} ", line):
            warn("possible source-first bullet (verb opener)", f"line {i}: {line[:90]}")
        elif re.match(r"^- \[", line):
            warn("bullet opens with a link (possible source-first)", f"line {i}: {line[:90]}")
        if "According to " in line and line.startswith("- "):
            warn("possible source-first bullet ('According to')", f"line {i}: {line[:90]}")


def check_link(url):
    """One URL via curl. Returns (url, status) — status is 'ok' or a detail string."""
    try:
        r = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
             "-L", "--max-time", "15",
             "-A", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/120.0 Safari/537.36",
             url],
            capture_output=True, text=True, timeout=20)
        code = r.stdout.strip()
        if code.startswith("2"):
            return url, "ok"
        return url, f"HTTP {code or 'no response'}"
    except Exception as e:
        return url, f"error: {e}"


def check_links(md):
    urls = sorted(set(md_links(md)))
    print(f"  checking {len(urls)} unique external links (parallel curl)...",
          flush=True)
    bad = []
    with ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(check_link, u): u for u in urls}
        for f in as_completed(futs):
            url, status = f.result()
            if status != "ok":
                bad.append((url, status))
    if not bad:
        ok("all external links return HTTP 200", f"{len(urls)} URLs")
    else:
        warn("external link check failures (curl)",
             f"{len(bad)}/{len(urls)} did not return 200 — browser-check each; "
             f"Medium and similar block curl but load fine: " +
             "; ".join(f"{u} [{s}]" for u, s in bad[:10]))


# --- Entry point ---------------------------------------------------------------

def main():
    md_path = Path(sys.argv[1]) if len(sys.argv) > 1 else \
        Path.home() / "workspace/ci-sitrep/SYNTHESIZED.md"
    html_path = Path(sys.argv[2]) if len(sys.argv) > 2 else \
        Path.home() / "workspace/ci-sitrep/index.html"
    md = md_path.read_text()
    html = html_path.read_text()
    # The HTML escapes < and > in text nodes, so "Confluence<1>" appears as
    # "Confluence&lt;1&gt;". Naming and marker checks run on the unescaped
    # copy; anchor and literal-link checks run on the raw HTML.
    html_unescaped = (html.replace("&lt;", "<").replace("&gt;", ">")
                          .replace("&amp;", "&"))

    print(f"Verifying {md_path} + {html_path} ({date.today()})\n")
    articles = check_articles(md)
    check_rating_consistency(articles)
    check_freshness(md)
    check_structure(md)
    check_top_level(html)
    check_naming(md, html_unescaped)
    check_hygiene(md, html)
    check_html(html_unescaped)
    check_glossary(md_path, html)
    check_source_first(md)
    check_links(md)

    # Staleness guard for the About page: site_config.VERIFY_CHECK_COUNT
    # must track the pass count, or the About numbers drift. A mismatch
    # is a WARN, not a FAIL — the report is still publishable; the
    # config needs one edit.
    try:
        from site_config import VERIFY_CHECK_COUNT
        n_pass_so_far = sum(1 for r in results if r[0] == "PASS")
        if n_pass_so_far != VERIFY_CHECK_COUNT:
            results.append(("WARN", "verify-count-config",
                            f"site_config.VERIFY_CHECK_COUNT is {VERIFY_CHECK_COUNT} "
                            f"but this run passed {n_pass_so_far} checks — update the config"))
    except ImportError:
        pass

    n_fail = sum(1 for r in results if r[0] == "FAIL")
    n_warn = sum(1 for r in results if r[0] == "WARN")
    n_pass = sum(1 for r in results if r[0] == "PASS")
    for level, check, detail in results:
        mark = {"PASS": "  PASS", "WARN": "  WARN", "FAIL": "  FAIL"}[level]
        print(f"{mark}  {check}" + (f" — {detail}" if detail else ""))
    print(f"\n{n_pass} passed, {n_warn} warnings, {n_fail} failures.")
    if n_fail:
        print("BUILD BLOCKED: fix the failures, regenerate, re-run verify.py.")
        return 1
    if n_warn:
        print("No failures. Review each warning before pushing.")
    else:
        print("Clean. Safe to push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
