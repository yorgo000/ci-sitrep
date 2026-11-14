#!/usr/bin/env python3
"""verify.py — post-change verification for the CI Sitrep report.

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
    "3": "Agentic: CIAC Design, Build, Deployment",
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
    ("Credibility rating", "credibility legend heading"),
    ("Confluence<1> Corp. All rights reserved", "copyright line"),
    ("makeShareButton", "share-link buttons"),
    ("How to read this", "How-to-read block"),
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
        ok("every article has exactly one credibility rating",
           " ●●●● %d / ●●●○ %d / ●●○○ %d / ●○○○ %d" % tuple(dist[r] for r in RATINGS))
    else:
        fail("every article has exactly one credibility rating",
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
    """New this week: 7-day window, newest first. What we're watching: no past dates, soonest first."""
    today = date.today()

    ntw = re.search(r"## New this week\n(.*?)\n## What we're watching",
                    md, re.DOTALL)
    if not ntw:
        fail("New this week section present", "section not found")
    else:
        dates = re.findall(r"^- \*\*(\d{4}-\d{2}-\d{2}) —", ntw.group(1), re.MULTILINE)
        parsed = [parse_ntw_date(d) for d in dates]
        stale = [d for d in parsed if d < today - timedelta(days=7)]
        if not stale:
            ok("New this week: no entry older than 7 days", f"{len(parsed)} entries")
        else:
            fail("New this week: no entry older than 7 days",
                 f"stale: {[str(d) for d in stale]}")
        if parsed == sorted(parsed, reverse=True):
            ok("New this week: newest first")
        else:
            fail("New this week: newest first", "entries out of order")

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

    order = ["New this week", "What we're watching", "Contents",
             "1. ", "2. ", "3. ", "Archive"]
    pos = []
    for o in order:
        i = md.find(f"## {o}")
        pos.append(i)
    if all(p >= 0 for p in pos) and pos == sorted(pos):
        ok("section order", "New this week < What we're watching < Contents < §1 < §2 < §3 < Archive")
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


def check_naming(md, html):
    """Confluence<1> everywhere (one documented exception); no 'Confluence 1'."""
    for label, text in (("Markdown", md), ("HTML", html)):
        if "Confluence 1" in text:
            fail(f"{label}: no 'Confluence 1'", "found 'Confluence 1'")
        else:
            ok(f"{label}: no 'Confluence 1'")
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
    literal = re.findall(r"\[[^\]]*\]\(https?://[^)]+\)", html)
    if not literal:
        ok("no literal Markdown links in HTML")
    else:
        fail("no literal Markdown links in HTML", f"{len(literal)} found, e.g. {literal[:2]}")

    ids = set(re.findall(r'id="([^"]+)"', html))
    hrefs = set(re.findall(r'href="#([^"]+)"', html))
    missing = sorted(h for h in hrefs if h not in ids)
    if not missing:
        ok("all internal anchors resolve", f"{len(hrefs)} links, {len(ids)} ids")
    else:
        fail("all internal anchors resolve", f"missing: {missing}")

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
    check_naming(md, html_unescaped)
    check_hygiene(md, html)
    check_html(html_unescaped)
    check_source_first(md)
    check_links(md)

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
