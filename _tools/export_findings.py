#!/usr/bin/env python3
"""Export the CI SITREP report as structured JSON (F-19 / first F-02 database file).

Parses SYNTHESIZED.md (articles, State of the market, New in the last 7 days),
GLOSSARY.md (terms), and dashboard.json (deadlines, gauges) and writes:

  data/findings.json          — the database: articles, what's new, glossary,
                                deadlines, gauges, counts, warnings.
  youtube/findings-inline.js  — the same data as a JS assignment
                                (window.CI_SITREP_DATA) so the scene and review
                                pages work under file:// in OBS, where fetch()
                                of a local JSON file is blocked. Regenerated
                                in the same run, so the two can never drift.

Article ids are the site's runtime share-anchor ids: the same slugify +
uniqueId the share JS assigns at page load, seeded with the static ids in
the generated index.html. The export is validated against
build_dashboard.compute_article_ids(index.html) — a mismatch is reported
as a warning (index.html may be stale relative to SYNTHESIZED.md; the
export's own computation from the markdown is authoritative).

Usage: export_findings.py [repo-root]
Defaults to the repo root (parent of _tools). Exits 1 on a structural
failure (an article without a headline, rating, source URL, or bullets;
duplicate ids). Missing dates and gauge lookups are warnings, not failures.

Regenerate after every report change: the daily watch regenerates the
report, so this export is a step in the publish pipeline (run it after
build_html.py, before pushing).
"""

import json
import re
import sys
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_dashboard import RATINGS, compute_article_ids, slugify  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
SITE_URL = "https://yorgo000.github.io/ci-sitrep/"

RATING_BY_DOTS = {v: k for k, v in RATINGS.items()}
SECTION_NAMES = {"1": "Pre-commit", "2": "In codebase", "3": "Agentic"}

MONTHS = "Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec"
DATE_PATTERNS = [
    rf"\d{{1,2}} (?:{MONTHS}) 202\d",          # 16 Nov 2026
    rf"(?:{MONTHS})\.? 202\d",                 # Nov 2026
    r"(?:Spring|Summer|Autumn|Fall|Winter) 202\d",
    r"Q[1-4] 202\d",
    r"202\d",                                  # bare year, last resort
]


def md_to_text(md):
    """Markdown fragment -> plain text (links keep their text, URLs dropped)."""
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("**", "").replace("__", "").replace("`", "")
    s = s.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return re.sub(r"\s+", " ", s).strip()


def speakable(text):
    """Plain text -> a version an AI voiceover can read aloud.

    Expands the symbols TTS engines stumble on; the displayed text stays
    exact, this field is only for the voiceover track.
    """
    s = text
    s = s.replace("×", " times ")
    s = s.replace("~", "about ")
    s = s.replace("→", " to ")
    s = s.replace("—", ", ")
    s = s.replace("–", " to ")
    s = s.replace("%", " percent")
    s = s.replace("&", " and ")
    s = s.replace("$", " dollars ")
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def extract_date(context):
    """Best-effort date from a source-context string; None when unparseable."""
    if not context:
        return None
    for pat in DATE_PATTERNS:
        m = re.search(pat, context)
        if m:
            return m.group(0)
    return None


class _IdCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.add(d["id"])


def parse_articles(src, warnings):
    """Walk SYNTHESIZED.md; return (articles, state_of_market, whats_new)."""
    lines = src.splitlines()
    section = None
    subsection = None
    articles = []
    state_of_market = []
    whats_new_raw = []
    in_state = False
    in_new = False
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^## (\d)\. ", line)
        if m:
            section = SECTION_NAMES.get(m.group(1))
            subsection = None
            in_state = False
            in_new = False
        elif line.startswith("## State of the market"):
            in_state = True
            in_new = False
        elif line.startswith("## New in the last 7 days"):
            in_new = True
            in_state = False
        elif line.startswith("## "):
            in_state = False
            in_new = False
        elif line.startswith("### "):
            subsection = line[4:].strip()
        if in_state and line and not line.startswith("##"):
            state_of_market.append(line)
        if in_new and line.startswith("- **"):
            whats_new_raw.append(line)
        if line.strip() == "<details>":
            block = []
            i += 1
            while i < len(lines) and lines[i].strip() != "</details>":
                block.append(lines[i])
                i += 1
            art = parse_article_block(block, section, subsection, warnings)
            if art is not None:
                articles.append(art)
        i += 1
    return articles, md_to_text(" ".join(state_of_market)), whats_new_raw


def parse_article_block(block, section, subsection, warnings):
    """One <details> block -> an article record, or None (See also / other)."""
    text = "\n".join(block)
    sm = re.search(r"<summary>(.*?)</summary>", text, re.DOTALL)
    if not sm:
        return None
    summary_md = sm.group(1).strip()
    dots = re.search(r"([●○]{4})", summary_md)
    if not dots:
        return None  # "See also" and other non-article blocks
    dots = dots.group(1)
    rating = RATING_BY_DOTS.get(dots)
    if rating is None:
        warnings.append(f"Unknown dots pattern {dots!r} in: {summary_md[:80]}")
        return None
    hm = re.search(r"<strong>(.*?)</strong>", summary_md, re.DOTALL)
    if not hm:
        warnings.append(f"Article without a bold headline: {summary_md[:80]}")
        return None
    headline = md_to_text(hm.group(1))
    rest = summary_md[hm.end():]
    flag = None
    fm = re.search(r"— \[(VENDOR CLAIM|VENDOR DATA)\]", rest)
    if fm:
        flag = fm.group(1)
    # Source name: first markdown link after the headline; the Source line
    # is authoritative for the URL.
    src_link = re.search(r"\[([^\]]+)\]\(([^)]+)\)", rest)
    source_name = src_link.group(1) if src_link else None
    # Source context: the parenthetical minus the link, minus dots/flag.
    paren = re.search(r"\((.*)\)", rest, re.DOTALL)
    context = md_to_text(paren.group(1)) if paren else ""
    # The Source line: "- Source: [label](url)".
    sl = re.search(r"- Source: \[([^\]]+)\]\(([^)]+)\)", text)
    if not sl:
        warnings.append(f"Article without a Source line: {headline[:80]}")
        return None
    source_label, source_url = sl.group(1), sl.group(2)
    if source_name is None:
        source_name = source_label.split(",")[0].strip()
    date = extract_date(context) or extract_date(source_label)
    bullets = []
    for ln in block:
        if ln.startswith("- ") and not ln.startswith("- Source:"):
            bullets.append(md_to_text(ln[2:]))
    if not bullets:
        warnings.append(f"Article without fact bullets: {headline[:80]}")
        return None
    # Plain-text summary, as the share JS sees it (for the runtime id).
    summary_text = md_to_text(summary_md)
    return {
        "headline": headline,
        "section": section,
        "subsection": subsection,
        "rating": rating,
        "rating_dots": dots,
        "source": source_name,
        "source_label": source_label,
        "source_url": source_url,
        "source_context": context,
        "date": date,
        "flag": flag,
        "bullets": bullets,
        "voiceover": speakable(headline + ". " + bullets[0]),
        "_summary_text": summary_text,
    }


def assign_ids(articles, index_html_path, warnings):
    """Runtime share-anchor ids, in document order, seeded with static ids."""
    used = {}
    if index_html_path.exists():
        collector = _IdCollector()
        collector.feed(index_html_path.read_text())
        used = dict.fromkeys(collector.ids)
    else:
        warnings.append(f"{index_html_path.name} not found — ids computed "
                        "without the static-id seed; regenerate the site "
                        "and re-export before relying on them.")
    for art in articles:
        base = slugify(art["_summary_text"]) or "item"
        ident, n = base, 2
        while ident in used:
            ident = f"{base}-{n}"
            n += 1
        used[ident] = True
        art["id"] = ident
        art["url"] = SITE_URL + "#" + ident
        del art["_summary_text"]


def validate_ids(articles, index_html_path, warnings):
    """Cross-check against build_dashboard's own computation from index.html."""
    if not index_html_path.exists():
        return
    try:
        expected = compute_article_ids(index_html_path.read_text())
    except Exception as exc:  # noqa: BLE001 - validation is best-effort
        warnings.append(f"Could not validate ids against index.html: {exc}")
        return
    # compute_article_ids counts every <details> block except How-to-read,
    # the mobile Contents block, and "See also" — which includes the
    # confidence-legend block in the masthead. It is not an article.
    expected = {i: h for i, h in expected.items()
                if h != "Confidence rating scale"}
    mine = {a["id"]: a for a in articles}
    for ident, art in mine.items():
        if ident not in expected:
            warnings.append(
                f"Id {ident} not in the ids index.html would assign — "
                "index.html may be stale; regenerate the site and re-export.")
    if len(expected) != len(mine):
        warnings.append(
            f"index.html yields {len(expected)} article ids, the export has "
            f"{len(mine)} — regenerate the site and re-export.")


def parse_whats_new(raw_lines, warnings):
    """'New in the last 7 days' bullets -> structured entries."""
    out = []
    for line in raw_lines:
        m = re.match(r"- \*\*(\d{4}-\d{2}-\d{2}) — (.*?)\*\*(.*)", line)
        if not m:
            warnings.append(f"What's-new line did not parse: {line[:100]}")
            out.append({"date": None, "title": md_to_text(line[2:]),
                        "source": None, "source_url": None, "tags": [],
                        "summary": "", "sections": []})
            continue
        date, bold, rest = m.group(1), m.group(2), m.group(3)
        title = bold.rstrip(":").strip()
        tags = re.findall(r"\[(Pre-commit|In codebase|Agentic)\]", bold + rest)
        title = re.sub(r"\s*\[(Pre-commit|In codebase|Agentic)\]", "", title).strip()
        # The source lives in the LEADING parenthetical only — links inside
        # the summary body (e.g. the governance-gap roundup) are not the
        # entry's source. The parenthetical may contain a markdown link,
        # whose own parens must not end the match early.
        source = source_url = None
        body = rest
        stripped = rest.lstrip()
        if stripped.startswith("("):
            depth, i = 0, rest.index("(")
            while i < len(rest):
                if rest[i] == "(":
                    depth += 1
                elif rest[i] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                i += 1
            paren = rest[rest.index("("):i + 1]
            link = re.search(r"\[([^\]]+)\]\((https?://[^)]+)\)", paren)
            if link:
                source, source_url = link.group(1), link.group(2)
            body = rest[i + 1:]
        # Summary: after the tags, up to the " → " section pointer.
        summary_part = body.split(" → ")[0]
        summary_part = re.sub(r"\s*\[(Pre-commit|In codebase|Agentic)\]", "", summary_part)
        summary = md_to_text(summary_part).lstrip(": ").strip()
        sections = [{"label": lab, "anchor": anc}
                    for lab, anc in re.findall(r"\[([^\]]+)\]\(#([^)]+)\)", rest)]
        out.append({"date": date, "title": title, "source": source,
                    "source_url": source_url, "tags": sorted(set(tags)),
                    "summary": summary, "sections": sections})
    return out


def parse_glossary(text):
    """GLOSSARY.md -> [{term, definition}]; entries are '**Term** — def.'."""
    entries = []
    current = None
    for line in text.splitlines():
        m = re.match(r"^\*\*(.+?)\*\* — (.*)$", line)
        if m:
            current = {"term": m.group(1), "definition": m.group(2)}
            entries.append(current)
        elif current is not None and line.strip():
            current["definition"] += " " + line.strip()
    for e in entries:
        e["definition"] = re.sub(r"\s+", " ", e["definition"]).strip()
    return entries


def build_gauges(dashboard, articles, warnings):
    """The four CI-vs-EI gauges for the broadcast right rail.

    Sourced from the report's own figures — never invented. Sajadi and
    SusVibes come from the dashboard's bottom-line compare charts;
    CodeRabbit from its §1.1 article (a vendor claim — the gauge says so);
    METR from the §3.6 dashboard figure (a horizon stat, not a pair — the
    report publishes no human-side horizon, and the gauge does not invent
    one). A lookup that misses is a warning and the gauge is omitted.
    """
    gauges = []
    for item in dashboard.get("bottom_line", []):
        chart = item.get("chart") or {}
        if chart.get("kind") != "compare":
            continue
        label = item.get("label", "")
        if "vulnerabilities in AI patches" in label:
            gauges.append({
                "key": "sajadi", "kind": "pair",
                "title": "Confirmed vulnerabilities, same issues",
                "ci": {"label": chart["a"]["label"], "value": chart["a"]["value"],
                       "display": chart["a"]["display"]},
                "ei": {"label": chart["b"]["label"], "value": chart["b"]["value"],
                       "display": chart["b"]["display"]},
                "headline": item.get("display", "") + " " + label,
                "source": item.get("source"), "date": item.get("date"),
                "rating": item.get("rating"),
                "link": item.get("link"),
            })
        elif "post-hoc review" in label:
            gauges.append({
                "key": "susvibes", "kind": "pair",
                "title": "Cost of a post-hoc review vs generation alone",
                "ci": {"label": chart["b"]["label"], "value": chart["b"]["value"],
                       "display": chart["b"]["display"]},
                "ei": {"label": chart["a"]["label"], "value": chart["a"]["value"],
                       "display": chart["a"]["display"]},
                "headline": "Review lifts working-and-secure to 47–56% at "
                            + item.get("display", "") + " the cost",
                "source": item.get("source"), "date": item.get("date"),
                "rating": item.get("rating"),
                "link": item.get("link"),
            })
    for art in articles:
        if "2.74" in art["headline"]:
            gauges.append({
                "key": "coderabbit", "kind": "pair",
                "title": "Vulnerability rate, CI code vs human code",
                "ci": {"label": "CI-generated code", "value": 2.74,
                       "display": "up to 2.74×"},
                "ei": {"label": "Human-written code", "value": 1,
                       "display": "1×"},
                "headline": art["headline"],
                "source": art["source"], "date": art["date"],
                "rating": art["rating"], "link": "#" + art["id"],
                "note": "Vendor claim — CodeRabbit's own analysis.",
            })
            break
    for panel in dashboard.get("panels", []):
        for block in panel.get("blocks", []):
            for fig in block.get("items", []):
                if fig.get("source") == "METR":
                    gauges.append({
                        "key": "metr", "kind": "stat",
                        "title": "Agent time horizon (50% reliability)",
                        "display": fig.get("display"),
                        "headline": fig.get("display", "") + " "
                                    + fig.get("label", ""),
                        "source": fig.get("source"), "date": fig.get("date"),
                        "rating": fig.get("rating"),
                        "link": fig.get("link"),
                        "note": fig.get("note"),
                    })
    wanted = {"sajadi", "susvibes", "coderabbit", "metr"}
    have = {g["key"] for g in gauges}
    for missing in sorted(wanted - have):
        warnings.append(f"Gauge {missing!r} could not be sourced from the "
                        "report/dashboard — omitted from the export.")
    order = ["sajadi", "coderabbit", "susvibes", "metr"]
    return sorted(gauges, key=lambda g: order.index(g["key"]))


def main(argv):
    repo = Path(argv[1]).resolve() if len(argv) > 1 else REPO
    warnings = []
    synth = (repo / "SYNTHESIZED.md").read_text()
    dashboard = json.loads((repo / "dashboard.json").read_text())
    glossary = parse_glossary((repo / "GLOSSARY.md").read_text())

    articles, state_of_market, whats_new_raw = parse_articles(synth, warnings)
    whats_new = parse_whats_new(whats_new_raw, warnings)
    assign_ids(articles, repo / "index.html", warnings)
    validate_ids(articles, repo / "index.html", warnings)
    gauges = build_gauges(dashboard, articles, warnings)

    # Structural validation — failures, not warnings.
    errors = []
    seen = set()
    for art in articles:
        for field in ("headline", "section", "rating", "source_url", "id"):
            if not art.get(field):
                errors.append(f"{art.get('id', '?')}: missing {field}")
        if not art.get("bullets"):
            errors.append(f"{art['id']}: no bullets")
        if art["id"] in seen:
            errors.append(f"duplicate id: {art['id']}")
        seen.add(art["id"])
    nodate = [a["id"] for a in articles if not a.get("date")]
    if nodate:
        warnings.append(f"{len(nodate)} article(s) with no parseable date: "
                        + ", ".join(nodate[:8])
                        + (" …" if len(nodate) > 8 else ""))
    if errors:
        print("EXPORT FAILED:")
        for e in errors:
            print("  -", e)
        return 1

    last_updated = re.search(r"\*\*Last updated:\*\* (\d{4}-\d{2}-\d{2})", synth)
    data = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "as_of": dashboard.get("as_of_label"),
        "as_of_date": dashboard.get("as_of")
                      or (last_updated.group(1) if last_updated else None),
        "site_url": SITE_URL,
        "counts": {
            "articles": len(articles),
            "whats_new": len(whats_new),
            "glossary": len(glossary),
            "deadlines": len(dashboard.get("deadlines", [])),
            "gauges": len(gauges),
        },
        "ratings": {r: sum(1 for a in articles if a["rating"] == r)
                    for r in ("established", "corroborated", "reported", "claimed")},
        "state_of_the_market": state_of_market,
        "articles": articles,
        "whats_new": whats_new,
        "glossary": glossary,
        "deadlines": dashboard.get("deadlines", []),
        "gauges": gauges,
        "warnings": warnings,
    }

    out_dir = repo / "data"
    out_dir.mkdir(exist_ok=True)
    (out_dir / "findings.json").write_text(
        json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    yt_dir = repo / "youtube"
    yt_dir.mkdir(exist_ok=True)
    (yt_dir / "findings-inline.js").write_text(
        "// Generated by _tools/export_findings.py — do not hand-edit.\n"
        "// Same data as ../data/findings.json, as a script tag, so the scene\n"
        "// and review pages work under file:// in OBS (fetch of a local JSON\n"
        "// file is blocked by the browser). Regenerate with the export.\n"
        "window.CI_SITREP_DATA = "
        + json.dumps(data, ensure_ascii=False) + ";\n")

    print(f"Exported {len(articles)} articles, {len(whats_new)} what's-new, "
          f"{len(glossary)} glossary terms, "
          f"{len(dashboard.get('deadlines', []))} deadlines, "
          f"{len(gauges)} gauges")
    print("Ratings:", data["ratings"])
    for w in warnings:
        print("WARNING:", w)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
