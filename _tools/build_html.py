#!/usr/bin/env python3
"""Build SYNTHESIZED.html from SYNTHESIZED.md.

Reads the knowledge-base markdown, converts it to a self-contained HTML
reading surface with:
- a sidebar table of contents (jump to any section),
- collapsible sub-sections (click a heading to fold/unfold),
- collapsible article headlines (native <details>, already in the markdown),
- a "New in the last 7 days" section at the top with jump links (rolling 7-day window),
- clean typography and table styling.

Usage: build_html.py [input.md] [output.html]
Defaults: ~/workspace/your_files/watches/SYNTHESIZED.md -> SYNTHESIZED.html
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

import markdown

WATCHES = Path.home() / "workspace" / "your_files" / "watches"


def github_slugify(text, separator="-"):
    """Match GitHub's heading-anchor algorithm.

    Lowercase, drop punctuation (anything that is not a word char, a space,
    or a hyphen), replace each space with the separator (no collapsing).
    """
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return text.replace(" ", separator)


def convert_details_blocks(src):
    """Convert the markdown inside <details> blocks to HTML.

    The markdown library does not process markdown nested inside raw HTML
    blocks, so a <details> whose facts are bullet lists would otherwise
    render as raw "- ..." text. Convert each block's inner markdown to HTML
    first; the outer conversion then passes the whole <details> through.
    """
    def repl(m):
        opening = m.group(1)  # the <details ...> opening tag, attributes preserved
        inner = m.group(2)
        sm = re.match(r"(\s*<summary[^>]*>.*?</summary>)(.*)", inner, re.DOTALL)
        if not sm:
            return m.group(0)
        summary, rest = sm.group(1), sm.group(2)
        # The summary passes through untouched by the outer conversion too, so
        # Markdown inside it (e.g. a linked source name in a headline) would
        # render as literal "[text](url)". Convert the summary's inner content
        # and strip the <p> wrapper markdown adds around a single paragraph.
        sm2 = re.match(r"(\s*<summary[^>]*>)(.*?)(</summary>)", summary, re.DOTALL)
        if sm2:
            html_sum = markdown.markdown(
                sm2.group(2).strip(), extensions=["tables", "sane_lists"]
            )
            if html_sum.startswith("<p>") and html_sum.endswith("</p>"):
                html_sum = html_sum[3:-4]
            summary = sm2.group(1) + html_sum + sm2.group(3)
        html_rest = markdown.markdown(
            rest.strip(), extensions=["tables", "sane_lists"]
        )
        return opening + "\n" + summary.strip() + "\n" + html_rest + "\n</details>"

    return re.sub(r"(<details[^>]*>)(.*?)</details>", repl, src, flags=re.DOTALL)


def strip_contents_section(src):
    """Drop the markdown's own '## Contents' section.

    The sidebar TOC (generated from the headings) replaces it, so keeping
    the section would duplicate the TOC and leave a dangling #contents
    anchor. Runs from the '## Contents' heading to the next '---' or '## '.
    """
    return re.sub(
        r"^## Contents\n.*?(?=^---\s*$|^## )",
        "",
        src,
        flags=re.DOTALL | re.MULTILINE,
    )


# Terms excluded from tooltip wrapping (they stay in the glossary page): they
# are so frequent that a marker on first mention per subsection would be noise.
GLOSSARY_NO_TIP = {"agent", "agentic"}

# Match-pattern overrides: term short form -> (JS regex source, flags).
# Anything not listed gets the default: terms starting uppercase match
# case-sensitively with word boundaries; lowercase phrases match
# case-insensitively, with a space matching either a space or a hyphen.
GLOSSARY_MATCH = {
    "CI": (r"CI-generated|\bCI\b", ""),
    "PR": (r"\bPRs?\b", ""),
    "CVE": (r"\bCVEs?\b", ""),
    "pass@1 and pass^k": (r"pass@1|pass\^k", "i"),
    "human-in-the-loop / human-on-the-loop": (r"human-in-the-loop|human-on-the-loop", "i"),
    "secret": (r"secrets?", "i"),
    "consultation paper": (r"consultation paper|CP\d{2}/\d{2}", "i"),
    "Project SAGE": (r"Project SAGE|\bSAGE\b", ""),
    "four-eyes principle": (r"four-eyes", "i"),
    "frontier model": (r"frontier models?", "i"),
    "kill switch": (r"kill switches?", "i"),
    "circuit breaker": (r"circuit breakers?", "i"),
    "hallucination": (r"hallucinat\w*", "i"),
    "slopsquatting": (r"slopsquat\w*", "i"),
    "shadow AI": (r"shadow (AI|agents?)", "i"),
    "red team": (r"red[- ]team\w*", "i"),
    "pen test": (r"pen[- ]test\w*", "i"),
    "deterministic": (r"deterministic\w*", "i"),
    "dependency": (r"dependenc\w+", "i"),
    "orchestration": (r"orchestrat\w*", "i"),
    "guardrail": (r"guardrails?", "i"),
}


def glossary_slug(term):
    """Slug for a glossary entry (twin of the one in build_page.py)."""
    short = term.split(" (")[0]
    return re.sub(r"[^a-z0-9]+", "-", short.lower()).strip("-")


def _js_escape(s):
    """Escape only true regex metacharacters (spaces and hyphens stay literal)."""
    return re.sub(r"([\\^$.|?*+()\[\]{}])", r"\\\1", s)


def parse_glossary(path):
    """Parse GLOSSARY.md into tooltip entries: term, short form, plain-text
    definition, slug, JS match pattern + flags, and whether it gets a tooltip."""
    src = Path(path).read_text(encoding="utf-8")
    entries = []
    for block in re.split(r"\n\n+", src):
        block = block.strip()
        if not block.startswith("**"):
            continue
        m = re.match(r"\*\*(.+?)\*\*\s*—\s*(.*)", block, re.DOTALL)
        if not m:
            continue
        term = m.group(1).strip()
        definition = re.sub(r"\s+", " ", m.group(2)).strip()
        # Strip inline markdown so the tooltip shows plain text.
        definition = re.sub(r"\*\*(.+?)\*\*", r"\1", definition)
        definition = re.sub(r"\*(.+?)\*", r"\1", definition)
        definition = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", definition)
        short = term.split(" (")[0]
        if short in GLOSSARY_MATCH:
            pattern, flags = GLOSSARY_MATCH[short]
        elif short and short[0].isupper():
            pattern, flags = r"\b" + _js_escape(short) + r"\b", ""
        else:
            pattern = _js_escape(short).replace(" ", "[- ]")
            pattern, flags = pattern, "i"
        entries.append({
            "term": term,
            "short": short,
            "def": definition,
            "slug": glossary_slug(term),
            "pattern": pattern,
            "flags": flags,
            "tip": short not in GLOSSARY_NO_TIP,
        })
    return entries


ARTICLE_DETAILS_RE = re.compile(
    r"<details([^>]*)>\s*<summary>(.*?)</summary>", re.DOTALL
)


def add_article_data_attrs(body, tags):
    """Emit data-* attributes on every article <details> block, from the
    tag lines — the same join the dashboard tiles use
    (build_dashboard.parse_article_tags is the single parser; tag_attrs
    is the single attribute builder — nothing is duplicated here). The
    article id is the runtime id the share JS will assign (summary text
    -> slugify -> document-order dedupe), so the attributes land on the
    article whose tag line they came from. Non-article details are
    skipped: How-to-read (carries a class attribute), "See also" blocks
    (summary text), and any details whose headline has no tag line (it
    has no tags to match on, so it stays unfiltered).
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_dashboard

    used = set()

    def repl(m):
        opening_attrs, summary_html = m.group(1), m.group(2)
        if "class=" in opening_attrs:
            return m.group(0)
        text = build_dashboard.headline_text(summary_html)
        if text == "See also":
            return m.group(0)
        base = build_dashboard.slugify(text) or "item"
        ident, n = base, 2
        while ident in used:
            ident = f"{base}-{n}"
            n += 1
        used.add(ident)
        dims = tags.get(ident)
        if not dims:
            return m.group(0)
        return (
            f"<details{opening_attrs}{build_dashboard.tag_attrs(dims)}>"
            f"\n<summary>{summary_html}</summary>"
        )

    return ARTICLE_DETAILS_RE.sub(repl, body)


FEED_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}\s*[—–-]\s*")
FEED_SOURCE_RE = re.compile(
    r"<strong>.*?</strong>\s*\(<a href=\"(https?://[^\"]+)\""
)


def add_feed_data_attrs(body, tags, url_to_ids):
    """Emit data-* attributes on each "New in the last 7 days" feed
    entry, inheriting its target article's tags — the same tag parser
    and the same attribute builder as the articles
    (build_dashboard.match_feed_entry / tag_attrs), so the feed can
    never disagree with them. The feed <ul> gets the whats-new-feed
    class the filter JS selects on, and a feed-empty state is inserted
    after it (shown by the JS only when no entry is visible). Entries
    with no identifiable article keep no attributes — they stay visible
    under any filter — and are reported, so a feed title drifting away
    from its article is visible at build time instead of silently
    unfilterable.
    """
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_dashboard

    m = re.search(
        r'(<h2 id="new-in-the-last-7-days">.*?</h2>.*?)<ul>(.*?)</ul>',
        body, re.DOTALL,
    )
    if not m or m.group(1).count("<h2") != 1:
        print("WARNING: 'New in the last 7 days' feed list not found — "
              "feed entries left unfiltered")
        return body
    head, ul_inner = m.group(1), m.group(2)
    tagged, unmatched = [], []

    def repl(m):
        inner = m.group(1)
        sm = re.match(r"<strong>(.*?)</strong>", inner)
        if not sm:
            unmatched.append("(entry without a bold title)")
            return m.group(0)
        headline = FEED_DATE_RE.sub("", sm.group(1))
        um = FEED_SOURCE_RE.match(inner)
        source_url = um.group(1).rstrip("/") if um else None
        dims = build_dashboard.match_feed_entry(
            headline, source_url, tags, url_to_ids
        )
        if not dims:
            unmatched.append(headline)
            return m.group(0)
        tagged.append(headline)
        return f"<li{build_dashboard.tag_attrs(dims)}>{inner}</li>"

    new_inner = re.sub(r"<li>(.*?)</li>", repl, ul_inner, flags=re.DOTALL)
    new_feed = (
        head + '<ul class="whats-new-feed">' + new_inner + "</ul>"
        + '\n<p class="dash-empty" id="feed-empty" hidden>'
        "No new items match these filters. "
        '<button type="button" class="dash-clear-btn" '
        "data-clear-filters>Clear all filters</button></p>"
    )
    print(f"Feed: {len(tagged)} of {len(tagged) + len(unmatched)} "
          "entries tagged")
    for u in unmatched:
        print(f"WARNING: feed entry has no matching article (stays "
              f"unfiltered): {u[:100]}")
    return body[:m.start()] + new_feed + body[m.end():]


def build(input_path, output_path):
    src = Path(input_path).read_text(encoding="utf-8")
    src = strip_contents_section(src)

    # "Last updated" line, taken from the header of the markdown.
    # Extract it for the "As of" banner, then strip it from the source so it
    # does not render as visible text (the banner carries the date).
    m = re.search(r"\*\*Last updated:\*\*\s*([0-9-]+)", src)
    last_updated = m.group(1) if m else ""
    src = re.sub(r"\*\*Last updated:\*\*\s*[0-9-]+\.?\n?", "", src, count=1)
    # Human-readable "As of" date for the prominent banner (e.g. "Thursday, November 12, 2026").
    as_of = ""
    if last_updated:
        try:
            as_of = datetime.strptime(last_updated, "%Y-%m-%d").strftime("%A, %B %d, %Y")
        except ValueError:
            as_of = last_updated

    src = convert_details_blocks(src)

    md = markdown.Markdown(
        extensions=[
            "tables",
            "toc",
            "sane_lists",
        ],
        extension_configs={
            "toc": {
                "slugify": github_slugify,
                "toc_depth": "2-4",
            },
        },
    )
    body = md.convert(src)
    # External links open in a new tab, so following a source never replaces
    # the report. Internal links (anchors, .html pages, mailto) are untouched.
    body = re.sub(
        r'<a href="(https?://[^"]+)">',
        r'<a href="\1" target="_blank" rel="noopener">',
        body,
    )
    # Article data-* attributes (Round 4): every article <details> carries
    # its tags, so the page-level filter JS can hide non-matching articles.
    # Runs on the converted body, before the dashboard section and the
    # panel are assembled (neither contains article <details> blocks).
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_dashboard
    article_tags = build_dashboard.parse_article_tags(input_path)
    body = add_article_data_attrs(body, article_tags)
    # Feed data-* attributes (Round 5): each "New in the last 7 days"
    # entry inherits its target article's tags, so the page-level
    # filter covers the feed too. Same stage as the article attrs —
    # the feed <ul> is in the converted body here.
    article_sources = build_dashboard.parse_article_sources(input_path)
    url_to_ids = build_dashboard.invert_sources(article_sources)
    body = add_feed_data_attrs(body, article_tags, url_to_ids)
    toc_html = md.toc

    # Prominent timestamp banner directly under the H1, so a reader sees at a
    # glance how current the report is. Right after it, a mobile-only inline
    # table of contents: on a phone the sidebar (with the TOC) sits below the
    # content, so the reader needs navigation up top. It is a native <details>
    # (one collapsed line, "Contents") and is hidden on desktop via CSS.
    # It sits outside every section-body, so collapsing a section never hides it.
    inline_toc = (
        '<details class="toc-inline">\n'
        '<summary>PAGE CONTENTS</summary>\n'
        + toc_html +
        '\n</details>\n'
    )
    # Search box (Round 4: inside the Search/Filter/Sort panel, which sits
    # right under the "As of" banner row): the report is reference
    # material, and readers need to find their way back to something they
    # saw. It indexes the live page at runtime (see the search JS), so it
    # needs no build-time index and stays fresh with every publish. It
    # sits outside every section-body, so collapsing a section never
    # hides it.
    search_box = (
        '<div class="search-box" id="search-box">\n'
        '<div class="search-field">\n'
        '<svg class="search-icon" viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.35-4.35"/></svg>\n'
        '<input type="search" id="search-input" placeholder="Search the report\u2026" aria-label="Search the report" autocomplete="off" spellcheck="false">\n'
        '<button type="button" id="search-clear" aria-label="Clear search" hidden><svg viewBox="0 0 12 12" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M1 1l10 10M11 1L1 11"/></svg></button>\n'
        '</div>\n'
        '<div id="search-results" hidden></div>\n'
        '<p id="search-status" class="visually-hidden" aria-live="polite"></p>\n'
        '</div>\n'
    )
    # Page structure (2026-11-15 restructure; row 1 revised 2026-11-15;
    # row 2 revised 2026-11-18, Round 4; FIX 2, 2026-11-18: "How to read
    # this" moved into the masthead, above the SITREP sections nav):
    #   Row 1: As-of banner (left) + Sections expand/collapse controls
    #     (right) on desktop. The row-1 "How to read this" copy is
    #     phones-only (display: none above 900px) — on phones the
    #     masthead renders below all main content, so the row-1 copy
    #     stays where first-time readers find it. When the phone copy
    #     is opened it drops to a full-width line below the row.
    #   Row 2: the Search/Filter/Sort panel — one collapsible <details>
    #     holding the search box + the filter/sort controls (the
    #     standalone search-box row is gone; its markup moved inside).
    #   Then the two top-level sections: EXECUTIVE DASHBOARD (the F-01
    #   dashboard, embedded from dashboard.json) and REPORT (the report
    #   body). The report's headings keep their levels — the H2s stay H2s
    #   — so every anchor survives the move.
    # "How to read this" comes out of the body and is emitted twice from
    # the same extracted string (FIX 2): once into the masthead sidebar
    # (the control on desktop) and once into row 1 (phones-only).
    htr_match = re.search(r'<details class="how-to-read">.*?</details>', body, re.DOTALL)
    htr = htr_match.group(0) if htr_match else ""
    if htr_match:
        body = body[:htr_match.start()] + body[htr_match.end():]

    # Row 1: As-of banner + "How to read this" (phones-only copy) +
    # Sections controls. The copy stays in the row assembly; CSS hides
    # it above 900px (see .top-row details.how-to-read).
    sec_controls = (
        '<div class="sec-controls">Sections: '
        '<button type="button" data-act="expand">Expand all</button>'
        '<button type="button" data-act="collapse">Collapse all</button></div>'
    )
    if as_of:
        banner = f'<p class="as-of-banner">As of {as_of}</p>'
        row1 = f'<div class="top-row">\n{banner}\n{htr}\n{sec_controls}\n</div>\n'
    else:
        row1 = f'<div class="top-row">\n{htr}\n{sec_controls}\n</div>\n'

    # Split the H1 from the rest; the rest becomes the REPORT section.
    h1_part, sep, rest = body.partition("</h1>")
    h1_part += sep

    # Dashboard (F-01), embedded as the first top-level section.
    dash_path = Path(input_path).parent / "dashboard.json"
    dash_section = ""
    dash_data = None
    search_row = search_box  # no dashboard.json: the search box stands alone
    toc = toc_html
    if dash_path.exists():
        dash_data = json.loads(dash_path.read_text(encoding="utf-8"))
        dash_inner = build_dashboard.render_embedded(dash_data)
        # Search/Filter/Sort panel (Round 4): the search box + the
        # filter/sort controls in ONE collapsible panel at the top of
        # the page, in the spot where the search box sat. The panel is
        # index-only — sub-pages have no dashboard/report to filter.
        n_figures = len(list(build_dashboard.iter_figures(dash_data)))
        filter_bar = build_dashboard.render_filter_bar(
            n_figures, len(article_tags), article_tags)
        search_row = (
            '<details class="search-filter-panel">\n'
            '<summary class="sfp-header"><span class="sfp-left">'
            '<span>Search, filter &amp; sort</span>'
            '<span class="sfp-active" id="sfp-active"></span></span>'
            '<span class="sfp-chevron" aria-hidden="true"></span></summary>\n'
            '<div class="sfp-body">\n' + search_box + filter_bar + '\n</div>\n'
            '</details>\n'
        )
        dash_section = (
            '<h2 id="executive-dashboard">EXECUTIVE DASHBOARD</h2>\n'
            f'<div class="dash-embed">\n{dash_inner}\n</div>\n'
        )
        # TOC: dashboard first (with its panels), report sections nested
        # under "Report" — mirroring the page's two top-level sections.
        panel_items = "".join(
            f'<li><a href="#{build_dashboard.esc(p["id"])}">'
            f'{build_dashboard.esc(p["title"])}</a></li>'
            for p in dash_data["panels"]
        )
        ul_start = toc_html.find("<ul>")
        ul_end = toc_html.rfind("</ul>") + len("</ul>")
        report_ul = toc_html[ul_start:ul_end]
        toc = (
            '<div class="toc">\n<ul>\n'
            '<li><a href="#executive-dashboard">EXECUTIVE DASHBOARD</a>\n<ul>\n'
            + panel_items + '\n</ul>\n</li>\n'
            '<li><a href="#report">REPORT</a>\n'
            + report_ul + '\n</li>\n</ul>\n</div>\n'
        )
    else:
        print(f"WARNING: {dash_path} not found — dashboard section omitted")

    body = (
        h1_part + "\n" + row1 + search_row + "\n" + inline_toc
        + dash_section
        + '<h2 id="report">REPORT</h2>\n'
        + '<div class="report-embed">\n' + rest + '\n</div>\n'
        # Report empty state (Round 4): shows when every article filters
        # out. It sits OUTSIDE .report-embed — but inside #report's
        # section-body, which never hides — so hiding the last section
        # cannot hide the line itself.
        + '<p class="dash-empty" id="report-empty" hidden>'
        "No articles match these filters. "
        '<button type="button" class="dash-clear-btn" '
        "data-clear-filters>Clear all filters</button></p>\n"
    )

    # Glossary data for tooltips: parsed from GLOSSARY.md in the same
    # directory as the report source. The tooltip JS wraps first mentions
    # per subsection at runtime from this data, so index.html must be
    # regenerated whenever GLOSSARY.md changes.
    glossary_path = Path(input_path).parent / "GLOSSARY.md"
    if glossary_path.exists():
        glossary_data = json.dumps(parse_glossary(glossary_path)).replace("</", "<\\/")
    else:
        print(f"WARNING: {glossary_path} not found — tooltips will be empty")
        glossary_data = "[]"

    html = TEMPLATE.format(
        title="CI SITREP — Code & Finance",
        last_updated=last_updated,
        toc=toc,
        body=body,
        how_to_read=htr,
        glossary_data=glossary_data,
    )
    if dash_data is not None:
        # Dashboard CSS/JS are inserted AFTER .format() — they contain braces.
        html = html.replace("</style>", build_dashboard.DASH_CSS + "\n</style>", 1)
        html = html.replace("</body>", build_dashboard.COUNTDOWN_JS + "\n</body>", 1)
        html = html.replace("</body>", build_dashboard.FILTER_JS + "\n</body>", 1)
        # Validate the dashboard data against the final HTML.
        errors = build_dashboard.validate(dash_data, html)
        if errors:
            print("dashboard.json validation FAILED:")
            for e in errors:
                print("  -", e)
            sys.exit(1)
    # GoatCounter analytics (site_config.GOATCOUNTER_CODE; no-op when None).
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import site_config

    snippet = site_config.goatcounter_snippet()
    if snippet:
        html = html.replace("</head>", snippet + "\n</head>", 1)
    Path(output_path).write_text(html, encoding="utf-8")
    print(f"Wrote {output_path} ({len(html)} bytes)")


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{
    --ink: #1a1a1a;
    --muted: #666;
    --line: #ddd5c2;
    --accent: #283060;
    --logo-navy: #283060;
    --bg: #faf6ef;
    --side-bg: #faf6ef;
    --code-bg: #f3ede0;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--ink);
    background: var(--bg);
    line-height: 1.6;
    font-size: 16px;
  }}
  .as-of-banner {{
    display: inline-block;
    margin: 0 0 18px 0;
    padding: 6px 12px;
    background: #e9eaf1;
    border: 1px solid #c5c8dc;
    border-radius: 4px;
    color: var(--accent);
    font-size: 15px;
    font-weight: 600;
  }}
  /* Row 1: As-of banner + Sections controls, one row. (The row-3
     layout this comment used to describe was removed 2026-11-15.) */
  .top-row {{ display: flex; justify-content: space-between; align-items: center; gap: 16px; flex-wrap: wrap; margin: 0 0 16px; }}
  .top-row .as-of-banner {{ margin: 0; }}
  .sec-controls {{ font-size: 13px; color: var(--muted); white-space: nowrap; }}
  .sec-controls button {{ font-size: 12px; padding: 2px 8px; margin-left: 4px; cursor: pointer; background: #fdfbf7; border: 1px solid var(--line); border-radius: 4px; color: var(--ink); }}
  .sec-controls button:hover {{ background: #e8dfcc; }}
  /* "How to read this" in row 1 is the phones-only copy (FIX 2): the
     masthead copy is the control on desktop, so this one is hidden
     above 900px and restored in the media query below. On phones it
     sits centered between the As-of banner and the Sections controls;
     when opened it drops to a full-width line below the row (the row
     wraps). */
  .top-row details.how-to-read {{ flex: 1 1 auto; text-align: center; display: none; }}
  .top-row details.how-to-read[open] {{ flex-basis: 100%; text-align: left; }}
  details.how-to-read {{ width: fit-content; max-width: 100%; }}
  details.how-to-read[open] {{ width: 100%; }}
  .search-box {{ margin: 0 0 16px; position: relative; }}
  .search-field {{ position: relative; }}
  .search-field svg.search-icon {{ position: absolute; left: 10px; top: 50%; transform: translateY(-50%); color: var(--muted); pointer-events: none; }}
  #search-input {{ width: 100%; box-sizing: border-box; font: inherit; font-size: 15px; padding: 9px 34px 9px 34px; border: 1px solid var(--line); border-radius: 6px; background: #fff; color: var(--ink); }}
  #search-input::-webkit-search-cancel-button {{ display: none; }}
  #search-input:focus {{ outline: none; border-color: var(--logo-navy); box-shadow: 0 0 0 2px rgba(40, 48, 96, 0.15); }}
  .search-box.open #search-input {{ border-bottom-left-radius: 0; border-bottom-right-radius: 0; }}
  #search-clear {{ position: absolute; right: 6px; top: 50%; transform: translateY(-50%); border: none; background: none; color: var(--muted); cursor: pointer; padding: 4px; border-radius: 4px; line-height: 0; }}
  #search-clear:hover {{ color: var(--ink); background: #eee8d8; }}
  #search-results {{ border: 1px solid var(--line); border-top: none; border-radius: 0 0 6px 6px; background: #fff; max-height: 420px; overflow-y: auto; box-shadow: 0 8px 20px rgba(40, 48, 96, 0.12); }}
  .search-results-count {{ font-size: 12px; color: var(--muted); padding: 8px 12px 4px; }}
  .search-result {{ display: block; padding: 8px 12px; text-decoration: none; color: var(--ink); border-top: 1px solid #efe9d8; }}
  .search-result:hover, .search-result.active {{ background: #f0f1f7; }}
  .search-result-title {{ display: block; font-weight: 600; font-size: 14px; line-height: 1.4; }}
  .search-result-path {{ display: block; font-size: 12px; color: var(--muted); margin-top: 1px; }}
  .search-result-snippet {{ display: block; font-size: 13px; color: #444; margin-top: 3px; line-height: 1.45; }}
  .search-result-snippet mark {{ background: #f5e6a3; color: inherit; padding: 0 1px; border-radius: 2px; }}
  .search-no-results {{ padding: 12px; font-size: 14px; color: var(--muted); }}
  .visually-hidden {{ position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }}
  .def {{ text-decoration: underline dotted var(--muted); text-underline-offset: 2px; cursor: help; }}
  #def-tip {{ position: absolute; z-index: 1000; max-width: 320px; background: #fff; border: 1px solid var(--line); border-left: 3px solid var(--accent); border-radius: 4px; box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15); padding: 10px 12px; font-size: 14px; line-height: 1.5; color: var(--ink); }}
  #def-tip .def-tip-text {{ margin: 0; padding-right: 18px; }}
  #def-tip .def-tip-link {{ display: block; margin-top: 6px; font-size: 13px; font-weight: 600; }}
  #def-tip .def-tip-close {{ position: absolute; top: 2px; right: 6px; border: none; background: none; color: var(--muted); cursor: pointer; font-size: 18px; line-height: 1; padding: 2px 4px; }}
  #def-tip .def-tip-close:hover {{ color: var(--ink); }}
  .layout {{ display: flex; min-height: 100vh; }}
  nav.sidebar {{
    width: 300px;
    flex: 0 0 300px;
    background: var(--side-bg);
    border-right: 1px solid var(--line);
    padding: 24px 20px;
    position: sticky;
    top: 0;
    height: 100vh;
    overflow-y: auto;
  }}
  nav.sidebar h2 {{ font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 0 0 12px; }}
  .masthead {{ margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px solid var(--line); }}
  .masthead-title {{ font-family: Georgia, 'Times New Roman', Times, serif; font-size: 26px; font-weight: 700; margin: 0; line-height: 1.2; color: #283060; }}
  .masthead-vertical {{ font-family: Georgia, 'Times New Roman', Times, serif; font-size: 15px; font-weight: 600; font-style: italic; color: #283060; margin: 2px 0 6px; }}
  .masthead-tagline {{ font-size: 13px; color: var(--muted); margin: 0; line-height: 1.45; }}
  .masthead-by {{ font-size: 13px; color: var(--muted); margin: 10px 0 0; }}
  .masthead-logo {{ height: 18px; width: auto; vertical-align: middle; margin-left: 2px; }}
  .masthead-nav {{ margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px solid var(--line); }}
  .masthead-nav h3 {{ font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 0 0 10px; }}
  .masthead-nav a {{ font-weight: 600; }}
  .masthead-legend {{ margin-bottom: 18px; padding-bottom: 0; border-bottom: 1px solid var(--line); }}
  .masthead-legend[open] {{ padding-bottom: 16px; }}
  .masthead-legend summary {{ font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 0; cursor: pointer; }}
  .masthead-legend[open] summary {{ margin-bottom: 10px; }}
  .masthead-legend p {{ font-size: 13px; color: var(--muted); margin: 0 0 8px; line-height: 1.45; }}
  .masthead-legend .dots {{ color: var(--ink); font-weight: 600; letter-spacing: 1px; }}
  /* "How to read this" in the masthead (FIX 2): same treatment as the
     confidence legend — a bordered <details> box with a masthead-header
     summary. The same block also renders in row 1, hidden on desktop
     and shown on phones (see the media query below). */
  nav.sidebar details.how-to-read {{ margin-bottom: 18px; padding-bottom: 0; border-bottom: 1px solid var(--line); }}
  nav.sidebar details.how-to-read[open] {{ padding-bottom: 16px; }}
  nav.sidebar details.how-to-read > summary {{ font-size: 13px; font-style: normal; font-weight: 400; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 0; }}
  nav.sidebar details.how-to-read[open] > summary {{ margin-bottom: 10px; }}
  nav.sidebar details.how-to-read p, nav.sidebar details.how-to-read li {{ font-size: 13px; color: var(--muted); line-height: 1.45; }}
  nav.sidebar details.how-to-read p {{ margin: 0 0 8px; }}
  /* Sidebar links are block-level nav rows; the guide's links are inline,
     inside sentences — override or every link breaks its sentence. */
  nav.sidebar details.how-to-read a {{ display: inline; padding: 0; font-size: inherit; color: var(--accent); text-decoration: underline; }}
  nav.sidebar details.how-to-read a:hover {{ background: none; }}
  .masthead-contact {{ margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px solid var(--line); }}
  .masthead-contact h3 {{ font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 0 0 10px; }}
  .masthead-contact p {{ font-size: 13px; color: var(--muted); margin: 0 0 8px; line-height: 1.45; }}
  nav.sidebar ul {{ list-style: none; padding: 0; margin: 0; }}
  nav.sidebar li {{ margin: 2px 0; }}
  nav.sidebar li li {{ padding-left: 14px; }}
  nav.sidebar li li li {{ padding-left: 14px; }}
  nav.sidebar a {{ color: var(--ink); text-decoration: none; font-size: 14px; line-height: 1.45; display: block; padding: 3px 6px; border-radius: 4px; }}
  nav.sidebar a:hover {{ background: #e8dfcc; }}
  nav.sidebar .new-badge {{
    display: inline-block; font-size: 10px; font-weight: 700; color: #fff;
    background: #b3261e; border-radius: 3px; padding: 0 4px; margin-left: 4px;
    vertical-align: middle;
  }}
  nav.sidebar .toc-controls {{ margin: 0 0 10px; }}
  nav.sidebar .toc-controls button {{
    font-size: 12px; padding: 2px 8px; margin-right: 4px; cursor: pointer;
    background: #fdfbf7; border: 1px solid var(--line); border-radius: 4px; color: var(--ink);
  }}
  nav.sidebar .toc-controls button:hover {{ background: #e8dfcc; }}
  nav.sidebar .toc li.has-children > a .toc-toggle {{
    display: inline-block; cursor: pointer; width: 0; height: 0;
    border-left: 4px solid transparent; border-right: 4px solid transparent;
    border-top: 5px solid var(--muted); vertical-align: middle; margin-right: 5px;
  }}
  nav.sidebar .toc li.toc-collapsed > a .toc-toggle {{ transform: rotate(-90deg); }}
  nav.sidebar .toc li.toc-collapsed > ul {{ display: none; }}
  main {{ flex: 1; min-width: 0; padding: 32px 48px 64px; max-width: 860px; }}
  main h1 {{ font-family: Georgia, 'Times New Roman', Times, serif; font-size: 28px; margin: -32px -48px 16px; padding: 28px 48px; line-height: 1.25; color: #fff; background: var(--logo-navy); }}
  main h1 em {{ display: block; font-size: 20px; margin-top: 2px; }}
  main h2 {{ font-size: 22px; margin: 40px 0 12px; padding-top: 16px; border-top: 1px solid var(--line); line-height: 1.3; color: var(--logo-navy); }}
  /* Meta sections (front-page features + archive) sit below the three
     content sections: smaller, lighter, muted. */
  main h2#new-in-the-last-7-days, main h2#what-were-watching, main h2#state-of-the-market, main h2#archive {{ font-size: 17px; font-weight: 600; color: var(--muted); }}
  main h3 {{ font-size: 18px; margin: 28px 0 10px; line-height: 1.35; }}
  main h4 {{ font-size: 16px; margin: 20px 0 8px 16px; }}
  main h4 + .section-body {{ margin-left: 16px; }}
  h2 .toggle, h3 .toggle, h4 .toggle {{
    cursor: pointer; margin-right: 6px;
    user-select: none; display: inline-block; width: 0; height: 0;
    border-left: 5px solid transparent; border-right: 5px solid transparent;
    border-top: 6px solid var(--muted); vertical-align: middle;
  }}
  /* Content headings: the .section-body is the heading's next sibling
     (inserted by the JS below), so collapse hides the adjacent sibling,
     not a child. */
  h2.collapsed + .section-body, h3.collapsed + .section-body, h4.collapsed + .section-body {{ display: none; }}
  #state-of-the-market + .section-body, #new-in-the-last-7-days + .section-body, #what-were-watching + .section-body {{ background: #f0f1f7; border-left: 3px solid var(--logo-navy); padding: 12px 16px; border-radius: 0 6px 6px 0; }}
  /* Inline TOC: hidden on desktop (the sidebar has it); shown on mobile. */
  .toc-inline {{ display: none; }}
  .toc-inline ul {{ list-style: none; padding: 0; margin: 0; }}
  .toc-inline li {{ margin: 2px 0; }}
  .toc-inline li li {{ padding-left: 14px; }}
  .toc-inline li li li {{ padding-left: 14px; }}
  .toc-inline a {{ color: var(--ink); text-decoration: none; font-size: 14px; line-height: 1.45; display: block; padding: 3px 6px; border-radius: 4px; }}
  .toc-inline a:hover {{ background: #e8dfcc; }}
  h2.collapsed .toggle, h3.collapsed .toggle, h4.collapsed .toggle {{ transform: rotate(-90deg); }}
  /* Share link: a small link icon at the end of every section heading.
     Copies the direct URL to that section. Hidden until hover on desktop;
     always visible on mobile (no hover on touch). The icon is inline SVG,
     not a font glyph. */
  .share-link {{
    display: inline-block;
    margin-left: 8px;
    padding: 4px 6px;
    border: none;
    background: none;
    color: var(--muted);
    cursor: pointer;
    opacity: 0;
    vertical-align: middle;
    line-height: 1;
    border-radius: 4px;
  }}
  .share-link svg {{ display: block; }}
  h1:hover .share-link, h2:hover .share-link, h3:hover .share-link, h4:hover .share-link,
  .share-link:focus {{ opacity: 1; }}
  .share-link:hover {{ color: var(--accent); background: #efe9da; }}
  .share-link.copied {{ font-size: 12px; font-weight: 600; color: var(--accent); opacity: 1; }}
  p:hover .share-link, summary:hover .share-link {{ opacity: 1; }}
  .table-share {{ text-align: right; margin: 2px 0 12px; }}
  table:hover + .table-share .share-link {{ opacity: 1; }}
  /* Dashboard tiles: the share button sits in the tile's top-right
     corner (a sibling of the tile's link, never nested inside it). */
  .tile-grid .tile, .bottom-line-strip .tile, .countdown-strip .cd-card {{ position: relative; }}
  .tile-grid .tile > .share-link, .bottom-line-strip .tile > .share-link, .countdown-strip .cd-card > .share-link {{ position: absolute; top: 6px; right: 6px; margin-left: 0; }}
  .tile-grid .tile:hover > .share-link, .bottom-line-strip .tile:hover > .share-link, .countdown-strip .cd-card:hover > .share-link {{ opacity: 1; }}
  /* Breadcrumbs: a small trail at the top of every section body, back up
     to any ancestor level or the top of the page. Muted, one line. */
  .crumbs {{
    font-size: 13px;
    color: var(--muted);
    margin: 0 0 10px;
  }}
  .crumbs a {{ color: var(--muted); text-decoration: none; }}
  .crumbs a:hover {{ color: var(--accent); text-decoration: underline; }}
  .crumbs .crumb-sep {{ color: var(--line); margin: 0 3px; }}
  /* Back-to-top button: fixed, bottom-right, invisible until the reader
     has scrolled down the page. The arrow is inline SVG, not a font glyph. */
  .back-to-top {{
    position: fixed;
    right: 24px;
    bottom: 24px;
    width: 40px;
    height: 40px;
    border: none;
    border-radius: 50%;
    background: var(--logo-navy);
    color: #fff;
    cursor: pointer;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  }}
  .back-to-top.visible {{ opacity: 0.85; pointer-events: auto; }}
  .back-to-top:hover {{ opacity: 1; }}
  main p {{ margin: 8px 0; }}
  main ul, main ol {{ margin: 8px 0; padding-left: 24px; }}
  main li {{ margin: 4px 0; }}
  main li > ul, main li > ol {{ margin: 4px 0; }}
  main a {{ color: var(--accent); }}
  main table {{ border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 14px; }}
  main th, main td {{ border: 1px solid var(--line); padding: 8px 10px; text-align: left; vertical-align: top; }}
  main th {{ background: var(--side-bg); font-weight: 600; }}
  main hr {{ border: none; border-top: 1px solid var(--line); margin: 32px 0; }}
  details {{ border: 1px solid var(--line); border-radius: 6px; margin: 10px 0; padding: 0; }}
  details > summary {{
    cursor: pointer; padding: 10px 14px; font-weight: 600; list-style: none;
    border-radius: 6px;
  }}
  details > summary::-webkit-details-marker {{ display: none; }}
  details > summary::before {{
    content: ""; display: inline-block; width: 0; height: 0;
    border-left: 4px solid transparent; border-right: 4px solid transparent;
    border-top: 5px solid var(--muted); vertical-align: middle; margin-right: 6px;
  }}
  details[open] > summary::before {{ transform: rotate(0deg); }}
  details:not([open]) > summary::before {{ transform: rotate(-90deg); }}
  details > summary:hover {{ background: var(--side-bg); }}
  details.how-to-read > summary {{
    font-weight: 400; font-style: italic; color: var(--muted);
  }}
  details[open] > summary {{ border-bottom: 1px solid var(--line); border-radius: 6px 6px 0 0; }}
  details > ul, details > p {{ padding: 4px 14px 10px; margin: 0; }}
  details > ul {{ padding-left: 38px; }}
  blockquote {{ border-left: 3px solid var(--line); margin: 12px 0; padding: 4px 16px; color: var(--muted); }}
  .meta {{ color: var(--muted); font-size: 14px; margin: 0 0 24px; }}
  @media (max-width: 900px) {{
    .layout {{ flex-direction: column; }}
    /* On a phone the content comes first and the masthead/sidebar follows below it. */
    main {{ order: 1; padding: 24px 20px 48px; }}
    .share-link {{ opacity: 1; }}
    .back-to-top {{ right: 16px; bottom: 16px; }}
    #def-tip {{ max-width: calc(100vw - 32px); }}
    .toc-inline {{ display: block; }}
    /* FIX 2: the phones-only row-1 "How to read this" copy is visible
       here (hidden on desktop); the masthead copy also renders below
       the content, inside the sidebar. */
    .top-row details.how-to-read {{ display: block; }}
    nav.sidebar {{ order: 2; width: 100%; flex: none; height: auto; position: static; border-right: none; border-bottom: none; border-top: 1px solid var(--line); }}
    main h1 {{ margin: -24px -20px 16px; padding: 24px 20px; }}
  }}
</style>
</head>
<body>
<div class="layout">
  <nav class="sidebar">
    <div class="masthead">
      <p class="masthead-title">CI SITREP</p>
      <p class="masthead-vertical">Code &amp; Finance</p>
      <p class="masthead-tagline">Created Intelligence in code and finance — as of today.</p>
      <p class="masthead-by">by <img src="confluence-wordmark.png" alt="Confluence&lt;1&gt;" class="masthead-logo"></p>
    </div>
    {how_to_read}
    <div class="masthead-nav">
      <h3>SITREP sections</h3>
      <a href="audit.html">Self-Audit</a>
      <a href="corrections.html">Corrections</a>
      <a href="glossary.html">Glossary</a>
      <a href="ci-vs-ei.html">CI vs EI</a>
      <a href="explainer.html">The names: CI, CII, CIC</a>
      <a href="theses.html">Foundational theses</a>
      <a href="archive.html">Archive</a>
      <a href="about.html">About</a>
    </div>
    <h2>PAGE CONTENTS</h2>
    {toc}
    <details class="masthead-legend">
      <summary>Confidence rating scale</summary>
      <p><span class="dots">●●●●</span> Established — peer-reviewed and independently confirmed, or a primary regulatory document.</p>
      <p><span class="dots">●●●○</span> Corroborated — peer-reviewed single study, or a credible source confirmed independently.</p>
      <p><span class="dots">●●○○</span> Reported — single credible source, not yet independently verified.</p>
      <p><span class="dots">●○○○</span> Claimed — vendor claim or single uncorroborated report.</p>
    </details>
    <div class="masthead-contact">
      <h3>Contact</h3>
      <p>Errors, omissions, feature requests:<br><a href="mailto:ci-sitrep@confluence1.com">ci-sitrep@confluence1.com</a></p>
      <p>Work with Confluence&lt;1&gt;:<br><a href="mailto:hello@confluence1.com">hello@confluence1.com</a></p>
    </div>
    <p class="meta" style="margin-top: 20px;">© 2026 Confluence&lt;1&gt; Corp. All rights reserved.<br>
    Source: SYNTHESIZED.md (Markdown is the source of truth).</p>
  </nav>
  <main>
    {body}
  </main>
</div>
<button class="back-to-top" type="button" aria-label="Back to top" title="Back to top"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5"/><path d="M5 12l7-7 7 7"/></svg></button>
<script>
(function () {{
  // Sidebar TOC: make every section collapsible (drill-down / roll-up).
  // Each TOC entry with children gets a toggle arrow; Expand all /
  // Collapse all buttons sit above the TOC, and a Sections control
  // expands/collapses all content headings.
  var toc = document.querySelector('nav.sidebar .toc');
  if (toc) {{
    var controls = document.createElement('div');
    controls.className = 'toc-controls';
    controls.innerHTML = '<button type="button" data-act="expand">Expand all</button>' +
      '<button type="button" data-act="collapse">Collapse all</button>';
    toc.parentNode.insertBefore(controls, toc);
    controls.addEventListener('click', function (e) {{
      var btn = e.target.closest('button');
      if (!btn) return;
      var collapse = btn.getAttribute('data-act') === 'collapse';
      toc.querySelectorAll('li.has-children').forEach(function (li) {{
        li.classList.toggle('toc-collapsed', collapse);
      }});
    }});
    toc.querySelectorAll('li').forEach(function (li) {{
      var childUl = li.querySelector(':scope > ul');
      if (!childUl) return;
      li.classList.add('has-children');
      li.classList.add('toc-collapsed');  // TOC starts collapsed: top-level only.
      var link = li.querySelector(':scope > a');
      if (!link) return;
      var toggle = document.createElement('span');
      toggle.className = 'toc-toggle';
      // No text content: the arrow is drawn with CSS borders (see .toc-toggle),
      // so it renders identically on every system instead of depending on
      // a font carrying the U+25B8/U+25BE triangle glyphs.
      link.insertBefore(toggle, link.firstChild);
      toggle.addEventListener('click', function (e) {{
        e.preventDefault();
        e.stopPropagation();
        li.classList.toggle('toc-collapsed');
      }});
    }});
  }}
  // Sections control (in the main content, row 1): expand/collapse all
  // content headings. It used to live in the sidebar; it was lost there.
  var secControls = document.querySelector('.sec-controls');
  if (secControls) {{
    secControls.addEventListener('click', function (e) {{
      var btn = e.target.closest('button');
      if (!btn) return;
      var collapse = btn.getAttribute('data-act') === 'collapse';
      document.querySelectorAll('main h2, main h3, main h4').forEach(function (h) {{
        // Collapse all returns the page to its initial state: everything
        // closes except the two top-level sections, which stay open.
        // Expand all still opens everything.
        if (collapse && (h.id === 'executive-dashboard' || h.id === 'report')) return;
        h.classList.toggle('collapsed', collapse);
      }});
    }});
  }}
  // Make h2/h3/h4 headings collapsible: clicking the heading toggles the
  // content that follows it (up to the next heading of equal or higher level).
  // Article headlines are native <details> and already collapsible.
  // Everything starts COLLAPSED so the reader drills into one section at
  // a time; Expand all (row 1) opens the whole tree.
  var main = document.querySelector('main');
  if (!main) return;
  var headings = main.querySelectorAll('h2, h3, h4');
  headings.forEach(function (h) {{
    var level = parseInt(h.tagName.substring(1), 10);
    var toggle = document.createElement('span');
    toggle.className = 'toggle';
    h.prepend(toggle);
    h.style.cursor = 'pointer';
    // Only the two top-level sections start open; everything inside
    // them — dashboard panels, front-page sections, report sections —
    // starts collapsed, as one line each.
    if (h.id !== 'executive-dashboard' && h.id !== 'report') h.classList.add('collapsed');
    // Wrap following siblings until the next heading of equal/higher level.
    var body = document.createElement('div');
    body.className = 'section-body';
    var node = h.nextSibling;
    var collected = [];
    while (node) {{
      var next = node.nextSibling;
      if (node.nodeType === 1 && /^H[1-4]$/.test(node.tagName)) {{
        var nl = parseInt(node.tagName.substring(1), 10);
        if (nl <= level) break;
      }}
      collected.push(node);
      node = next;
    }}
    collected.forEach(function (n) {{ body.appendChild(n); }});
    h.parentNode.insertBefore(body, h.nextSibling);
    h.addEventListener('click', function (e) {{
      // Do not toggle when the click was on a link inside the heading.
      if (e.target.closest('a')) return;
      h.classList.toggle('collapsed');
    }});
    // (h4 sections were already collapsed above, like every other heading.)
  }});
  // Breadcrumbs: at the top of every section body, a small trail back up
  // to any ancestor level or the top of the page ("Top · §3 Agentic …
  // · §3.4 Governance"). A reader who drilled down jumps back without
  // scrolling. Built from the heading hierarchy, so it stays correct as
  // sections are added or renamed. Skips the three front-page sections
  // (they sit at the top of the page already), the two top-level
  // sections, the dashboard panels, and the page title.
  var crumbHeads = Array.prototype.slice.call(main.querySelectorAll('h1, h2, h3, h4'));
  var firstH1 = main.querySelector('h1');
  crumbHeads.forEach(function (h) {{
    if (h.tagName === 'H1') return;
    if (h.id === 'state-of-the-market' || h.id === 'new-in-the-last-7-days' || h.id === 'what-were-watching' || h.id === 'executive-dashboard' || h.id === 'report' || h.classList.contains('dash-panel')) return;
    var level = parseInt(h.tagName.substring(1), 10);
    var ancestors = [];
    var idx = crumbHeads.indexOf(h);
    var need = level - 1;
    for (var k = idx - 1; k >= 0 && need >= 1; k--) {{
      var cand = crumbHeads[k];
      var cl = parseInt(cand.tagName.substring(1), 10);
      if (cl === need) {{
        if (cand !== firstH1) ancestors.unshift(cand);
        need--;
      }}
    }}
    var sbody = h.nextElementSibling;
    if (!sbody || !sbody.classList.contains('section-body')) return;
    var crumbs = document.createElement('p');
    crumbs.className = 'crumbs';
    var chtml = '<a href="#" class="crumb-top" title="Back to the top of the page">↑ Top</a>';
    ancestors.forEach(function (a) {{
      chtml += ' <span class="crumb-sep">·</span> <a href="#' + a.id + '">' + a.textContent.trim() + '</a>';
    }});
    crumbs.innerHTML = chtml;
    sbody.insertBefore(crumbs, sbody.firstChild);
  }});
  // The "Top" crumb smooth-scrolls to the top (no hash change).
  main.addEventListener('click', function (e) {{
    var t = e.target.closest('a.crumb-top');
    if (!t) return;
    e.preventDefault();
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }});
  // Share links: every section heading, article headline, substantive
  // paragraph, and table gets a small link button that copies the direct
  // URL to that unit (page + #anchor). The icon is inline SVG, not a font
  // glyph, so it renders identically everywhere. On desktop the button
  // appears on hover of its unit; on touch devices it is always visible
  // (see the .share-link CSS). Clicking it never toggles its unit.
  var LINK_SVG = '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>';
  function slugify(text) {{
    var s = text.toLowerCase()
      .replace(/[^\\w\\s-]/g, '')
      .trim()
      .replace(/\\s+/g, '-')
      .replace(/-+/g, '-')
      .replace(/^-|-$/g, '');
    if (s.length > 60) {{
      s = s.slice(0, 60);
      var cut = s.lastIndexOf('-');
      if (cut > 20) s = s.slice(0, cut);
    }}
    return s;
  }}
  var usedIds = {{}};
  document.querySelectorAll('[id]').forEach(function (el) {{ usedIds[el.id] = true; }});
  function uniqueId(base) {{
    if (!base) base = 'item';
    var id = base, n = 2;
    while (usedIds[id]) {{ id = base + '-' + n; n++; }}
    usedIds[id] = true;
    return id;
  }}
  function copyUrl(id, btn) {{
    var origin = location.origin || (location.protocol + '//' + location.host);
    var path = location.pathname.replace(/\\/index\\.html$/, '/');
    var url = origin + path + '#' + id;
    function done() {{
      btn.classList.add('copied');
      btn.textContent = 'Copied';
      setTimeout(function () {{
        btn.classList.remove('copied');
        btn.innerHTML = LINK_SVG;
      }}, 1500);
    }}
    function fallbackCopy(text) {{
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try {{ document.execCommand('copy'); }} catch (err) {{}}
      document.body.removeChild(ta);
      done();
    }}
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(url).then(done, function () {{ fallbackCopy(url); }});
    }} else {{
      fallbackCopy(url);
    }}
  }}
  function makeShareButton(id, label) {{
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'share-link';
    btn.setAttribute('aria-label', label);
    btn.title = label;
    btn.innerHTML = LINK_SVG;
    btn.addEventListener('click', function (e) {{
      // Never toggle the enclosing heading or <details>: the click is
      // only for copying. preventDefault cancels the <summary> toggle,
      // stopPropagation keeps the heading collapse handler out of it.
      e.stopPropagation();
      e.preventDefault();
      copyUrl(id, btn);
    }});
    return btn;
  }}
  // Headings (all except the page title).
  var shareHeads = main.querySelectorAll('h1, h2, h3, h4');
  shareHeads.forEach(function (h, i) {{
    if (!h.id) return;
    if (i === 0 && h.tagName === 'H1') return;  // the page title is not a section
    h.appendChild(makeShareButton(h.id, 'Copy link to this section'));
  }});
  // Articles: the <details> blocks. Skips the How-to-read block, the
  // mobile Contents block, the dashboard's More filters block, the
  // Search/Filter/Sort panel, and the See-also cross-link blocks. The
  // id goes on the <details> itself; the button goes in its <summary>.
  main.querySelectorAll('details').forEach(function (d) {{
    if (d.classList.contains('how-to-read') || d.classList.contains('toc-inline') || d.classList.contains('dash-more-filters') || d.classList.contains('search-filter-panel')) return;
    var sum = d.querySelector(':scope > summary');
    if (!sum) return;
    var text = sum.textContent.trim();
    if (text === 'See also') return;
    if (!d.id) d.id = uniqueId(slugify(text));
    sum.appendChild(makeShareButton(d.id, 'Copy link to this article'));
  }});
  // Dashboard cards: the bottom-line strip, the countdown strip, and
  // the panel tiles. Each card gets a stable id and a share button in
  // its top-right corner — a sibling of the card's link, never nested
  // inside it, so clicking it copies the card's URL instead of
  // following the link. The strip id comes from the card's link target
  // (bl-<article-slug>, bl-money for the profitability card); the
  // countdown id from its label (cd-<deadline-slug>); panel tiles carry
  // their id from the generator (tile-<panel>-<slug>).
  main.querySelectorAll('.bottom-line-strip .tile').forEach(function (card) {{
    var link = card.querySelector(':scope > a');
    var base = 'bl-item';
    if (link) {{
      var href = link.getAttribute('href') || '';
      if (href.charAt(0) === '#') base = 'bl-' + href.slice(1);
    }}
    if (!card.id) card.id = uniqueId(base);
    card.appendChild(makeShareButton(card.id, 'Copy link to this figure'));
  }});
  main.querySelectorAll('.countdown-strip .cd-card').forEach(function (card) {{
    var lab = card.querySelector('.cd-label');
    var base = 'cd-' + (lab ? slugify(lab.textContent) : 'item');
    if (!card.id) card.id = uniqueId(base);
    card.appendChild(makeShareButton(card.id, 'Copy link to this deadline'));
  }});
  main.querySelectorAll('.tile-grid .tile').forEach(function (card) {{
    if (!card.id) card.id = uniqueId('tile-item');
    card.appendChild(makeShareButton(card.id, 'Copy link to this figure'));
  }});
  // Tables: id from the nearest preceding heading, button in a small
  // right-aligned row just below the table.
  var allHeads = Array.prototype.slice.call(main.querySelectorAll('h1, h2, h3, h4'));
  main.querySelectorAll('table').forEach(function (tbl) {{
    var head = null;
    for (var k = 0; k < allHeads.length; k++) {{
      if (allHeads[k].compareDocumentPosition(tbl) & Node.DOCUMENT_POSITION_FOLLOWING) head = allHeads[k];
      else break;
    }}
    var base = (head && head.id ? head.id + '-table' : 'table');
    if (!tbl.id) tbl.id = uniqueId(base);
    var row = document.createElement('div');
    row.className = 'table-share';
    row.appendChild(makeShareButton(tbl.id, 'Copy link to this table'));
    tbl.parentNode.insertBefore(row, tbl.nextSibling);
  }});
  // Substantive paragraphs: prose outside any <details>, long enough to be
  // worth sharing, not a Sources line or the As-of banner. The button goes
  // inline at the end of the paragraph.
  main.querySelectorAll('p').forEach(function (p) {{
    if (p.closest('details')) return;
    if (p.closest('.tile')) return;  // tile text is covered by the tile's own button
    if (p.classList.contains('as-of-banner')) return;
    if (p.classList.contains('crumbs')) return;
    var text = p.textContent.trim();
    if (text.length < 80) return;
    if (text.indexOf('Sources:') === 0) return;
    if (!p.id) p.id = uniqueId(slugify(text));
    p.appendChild(makeShareButton(p.id, 'Copy link to this paragraph'));
  }});

  // Search: a client-side index built from the live page the first time
  // the reader types. No build step, no index file — the page IS the
  // index, so it is always in sync with what the daily watch published.
  // Searchable units are the same units the share buttons cover
  // (articles, headings, substantive paragraphs, tables), so every
  // result links to a stable anchor that expandForAnchor opens.
  var searchInput = document.getElementById('search-input');
  var searchResults = document.getElementById('search-results');
  var searchClear = document.getElementById('search-clear');
  var searchStatus = document.getElementById('search-status');
  var searchBox = document.getElementById('search-box');
  var searchIndex = null;
  var searchActive = -1;
  var searchTimer = null;
  function cleanText(el) {{
    var c = el.cloneNode(true);
    c.querySelectorAll('button').forEach(function (b) {{ b.remove(); }});
    return c.textContent.replace(/\\s+/g, ' ').trim();
  }}
  function escapeHtml(s) {{
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }}
  function escapeRegExp(s) {{
    return s.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&');
  }}
  function buildSearchIndex() {{
    var items = [];
    var cur2 = null, cur3 = null, cur4 = null;
    function pathOf() {{
      var parts = [];
      if (cur2) parts.push(cur2);
      if (cur3) parts.push(cur3);
      if (cur4) parts.push(cur4);
      return parts.join(' · ');
    }}
    var nodes = main.querySelectorAll('h2, h3, h4, details, p, table, li');
    nodes.forEach(function (n) {{
      var tag = n.tagName;
      if (tag === 'H2' || tag === 'H3' || tag === 'H4') {{
        var label = cleanText(n);
        if (!label || !n.id) return;
        var path = '';
        if (tag === 'H3') path = cur2 || '';
        else if (tag === 'H4') path = [cur2, cur3].filter(Boolean).join(' · ');
        if (tag === 'H2') {{ cur2 = label; cur3 = null; cur4 = null; }}
        else if (tag === 'H3') {{ cur3 = label; cur4 = null; }}
        else {{ cur4 = label; }}
        items.push({{ id: n.id, title: label, text: label, path: path, kind: 'section' }});
        return;
      }}
      if (tag === 'DETAILS') {{
        if (n.classList.contains('how-to-read') || n.classList.contains('toc-inline') || n.classList.contains('dash-more-filters') || n.classList.contains('search-filter-panel')) return;
        var sum = n.querySelector(':scope > summary');
        if (!sum || !n.id) return;
        var stext = cleanText(sum);
        if (stext === 'See also') return;
        items.push({{ id: n.id, title: stext, text: cleanText(n), path: pathOf(), kind: 'article' }});
        return;
      }}
      if (tag === 'P') {{
        if (n.closest('details')) return;
        if (n.closest('#search-box')) return;
        if (n.closest('.tile')) return;  // tiles are indexed as units below
        if (n.classList.contains('as-of-banner')) return;
        if (n.classList.contains('crumbs')) return;
        var ptext = cleanText(n);
        if (ptext.length < 80) return;
        if (ptext.indexOf('Sources:') === 0) return;
        if (!n.id) return;
        var t = ptext.slice(0, 90);
        var sp = t.lastIndexOf(' ');
        if (sp > 40) t = t.slice(0, sp);
        items.push({{ id: n.id, title: t + '…', text: ptext, path: pathOf(), kind: 'paragraph' }});
        return;
      }}
      if (tag === 'TABLE') {{
        if (!n.id) return;
        items.push({{ id: n.id, title: (cur4 || cur3 || cur2 || 'Table') + ' — table', text: cleanText(n), path: pathOf(), kind: 'table' }});
        return;
      }}
      if (tag === 'LI') {{
        // Standalone list items in a section body: the best-practice
        // bullets (§1.5.2, §2.5) and the "New in the last 7 days" / "What we're
        // watching" entries live here, not in <p> or <details>. Items
        // inside a <details> are already covered by their article unit;
        // nested items are covered by their parent's text. Unlike the
        // other units these have no share-button id, so the indexer
        // assigns one with the same deterministic slugify — a
        // search-result link resolves identically on a later load.
        if (n.closest('details')) return;
        if (n.parentElement.closest('li')) return;
        var ltext = cleanText(n);
        if (ltext.length < 80) return;
        if (!n.id) n.id = uniqueId(slugify(ltext));
        var lt = ltext.slice(0, 90);
        var lsp = lt.lastIndexOf(' ');
        if (lsp > 40) lt = lt.slice(0, lsp);
        items.push({{ id: n.id, title: lt + '…', text: ltext, path: pathOf(), kind: 'list' }});
        return;
      }}
    }});
    // Dashboard tiles: each tile is a searchable figure — value + label
    // as the title, the tile's full text (minus the share button and
    // the visually-hidden sentiment word, which would otherwise make
    // every negative tile match a search for "negative") as the body,
    // its panel as the path. Hidden (filtered-out) tiles are still in
    // the DOM, so search still finds them; the filter script clears the
    // filters before following the result link.
    main.querySelectorAll('.dash-embed .tile').forEach(function (t) {{
      if (!t.id) return;
      var c = t.cloneNode(true);
      c.querySelectorAll('button, .visually-hidden').forEach(function (b) {{ b.remove(); }});
      var text = c.textContent.replace(/\s+/g, ' ').trim();
      if (text.length < 20) return;
      var val = t.querySelector('.stat-value');
      var lab = t.querySelector('.stat-label');
      var txt = t.querySelector('.tile-text');
      var title = '';
      if (val && lab) title = cleanText(val) + ' ' + cleanText(lab);
      else if (txt) title = cleanText(txt);
      else title = text;
      if (title.length > 90) {{
        var sp2 = title.slice(0, 90).lastIndexOf(' ');
        title = (sp2 > 40 ? title.slice(0, sp2) : title.slice(0, 90)) + '…';
      }}
      var path = 'Executive dashboard';
      var sbody = t.closest('.section-body');
      if (sbody) {{
        var h = sbody.previousElementSibling;
        if (h && h.tagName === 'H3') path = 'Executive dashboard · ' + cleanText(h);
      }}
      items.push({{ id: t.id, title: title, text: text, path: path, kind: 'figure' }});
    }});
    return items;
  }}
  function searchScore(item, tokens) {{
    var title = item.title.toLowerCase();
    var text = item.text.toLowerCase();
    var titleHits = 0, textHits = 0;
    tokens.forEach(function (t) {{
      if (title.indexOf(t) !== -1) titleHits++;
      if (text.indexOf(t) !== -1) textHits++;
    }});
    if (textHits === 0) return -1;
    var score = textHits * 10 + titleHits * 50;
    if (textHits === tokens.length) score += 30;
    if (titleHits === tokens.length) score += 100;
    return score;
  }}
  function searchSnippet(item, tokens) {{
    var lower = item.text.toLowerCase();
    var pos = -1;
    tokens.forEach(function (t) {{
      var i = lower.indexOf(t);
      if (i !== -1 && (pos === -1 || i < pos)) pos = i;
    }});
    if (pos === -1) return escapeHtml(item.text.slice(0, 140)) + '…';
    var start = Math.max(0, pos - 60);
    var end = Math.min(item.text.length, pos + 100);
    var s = item.text.slice(start, end);
    if (start > 0) {{ var w = s.indexOf(' '); if (w !== -1) s = s.slice(w + 1); }}
    if (end < item.text.length) {{ var w2 = s.lastIndexOf(' '); if (w2 !== -1) s = s.slice(0, w2); }}
    s = escapeHtml(s);
    tokens.forEach(function (t) {{
      if (/[&<>"]/.test(t)) return;
      s = s.replace(new RegExp('(' + escapeRegExp(t) + ')', 'gi'), '<mark>$1</mark>');
    }});
    return (start > 0 ? '…' : '') + s + (end < item.text.length ? '…' : '');
  }}
  function renderSearchResults(matches, query, total) {{
    searchResults.innerHTML = '';
    searchActive = -1;
    if (matches.length === 0) {{
      var none = document.createElement('div');
      none.className = 'search-no-results';
      none.textContent = 'No matches in the report for "' + query + '".';
      searchResults.appendChild(none);
      searchStatus.textContent = 'No matches for ' + query;
    }} else {{
      var count = document.createElement('div');
      count.className = 'search-results-count';
      count.textContent = total > matches.length
        ? ('Top ' + matches.length + ' of ' + total + ' matches — refine your search to narrow it down.')
        : (total + (total === 1 ? ' match' : ' matches'));
      searchResults.appendChild(count);
      matches.forEach(function (m) {{
        var a = document.createElement('a');
        a.href = '#' + m.item.id;
        a.className = 'search-result';
        var t = document.createElement('span');
        t.className = 'search-result-title';
        t.textContent = m.item.title;
        a.appendChild(t);
        if (m.item.path) {{
          var p = document.createElement('span');
          p.className = 'search-result-path';
          p.textContent = m.item.path;
          a.appendChild(p);
        }}
        var s = document.createElement('span');
        s.className = 'search-result-snippet';
        s.innerHTML = searchSnippet(m.item, m.tokens);
        a.appendChild(s);
        searchResults.appendChild(a);
      }});
      searchStatus.textContent = total + (total === 1 ? ' result' : ' results') + ' for ' + query;
    }}
    searchResults.hidden = false;
    searchBox.classList.add('open');
  }}
  function closeSearchResults() {{
    searchResults.hidden = true;
    searchBox.classList.remove('open');
    searchActive = -1;
  }}
  function runSearch() {{
    var q = searchInput.value.trim();
    searchClear.hidden = q.length === 0;
    if (q.length < 2) {{ closeSearchResults(); searchStatus.textContent = ''; return; }}
    if (!searchIndex) searchIndex = buildSearchIndex();
    var tokens = q.toLowerCase().split(/\\s+/).filter(Boolean);
    var scored = [];
    searchIndex.forEach(function (item) {{
      var score = searchScore(item, tokens);
      if (score >= 0) scored.push({{ item: item, score: score, tokens: tokens }});
    }});
    scored.sort(function (a, b) {{ return b.score - a.score; }});
    renderSearchResults(scored.slice(0, 10), q, scored.length);
  }}
  if (searchInput && searchResults && searchClear && searchStatus && searchBox) {{
    searchInput.addEventListener('input', function () {{
      clearTimeout(searchTimer);
      searchTimer = setTimeout(runSearch, 150);
    }});
    searchInput.addEventListener('keydown', function (e) {{
      if (e.key === 'Escape') {{ closeSearchResults(); searchInput.blur(); return; }}
      if (searchResults.hidden) return;
      var links = searchResults.querySelectorAll('a.search-result');
      if (!links.length) return;
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {{
        e.preventDefault();
        searchActive = e.key === 'ArrowDown'
          ? (searchActive + 1) % links.length
          : (searchActive - 1 + links.length) % links.length;
        links.forEach(function (l, i) {{ l.classList.toggle('active', i === searchActive); }});
        links[searchActive].scrollIntoView({{ block: 'nearest' }});
      }} else if (e.key === 'Enter') {{
        if (searchActive >= 0) {{ e.preventDefault(); links[searchActive].click(); }}
        else if (links.length) {{ e.preventDefault(); links[0].click(); }}
      }}
    }});
    searchInput.addEventListener('focus', function () {{
      if (searchInput.value.trim().length >= 2) runSearch();
    }});
    searchClear.addEventListener('click', function () {{
      searchInput.value = '';
      searchClear.hidden = true;
      closeSearchResults();
      searchStatus.textContent = '';
      searchInput.focus();
    }});
    searchResults.addEventListener('click', function (e) {{
      var a = e.target.closest('a.search-result');
      if (a) closeSearchResults();
    }});
    document.addEventListener('click', function (e) {{
      if (!searchBox.contains(e.target)) closeSearchResults();
    }});
  }}

  // Glossary tooltips: the first mention of a glossary term in each
  // subsection gets a dotted underline; hovering (desktop) or tapping
  // (mobile) shows the one-line definition with a link to the full
  // glossary entry. The data comes from GLOSSARY.md at build time (see
  // parse_glossary), so the tooltips and the glossary page can never
  // drift apart.
  var GLOSSARY = {glossary_data};
  var glossaryBySlug = {{}};
  GLOSSARY.forEach(function (e) {{ glossaryBySlug[e.slug] = e; }});
  var tipEl = null;
  var tipTrigger = null;
  var tipHideTimer = null;
  function buildTipEl() {{
    tipEl = document.createElement('div');
    tipEl.id = 'def-tip';
    tipEl.setAttribute('role', 'tooltip');
    tipEl.hidden = true;
    var closeBtn = document.createElement('button');
    closeBtn.type = 'button';
    closeBtn.className = 'def-tip-close';
    closeBtn.setAttribute('aria-label', 'Close definition');
    closeBtn.textContent = '×';
    closeBtn.addEventListener('click', hideTip);
    var text = document.createElement('p');
    text.className = 'def-tip-text';
    var link = document.createElement('a');
    link.className = 'def-tip-link';
    link.textContent = 'Glossary →';
    tipEl.appendChild(closeBtn);
    tipEl.appendChild(text);
    tipEl.appendChild(link);
    document.body.appendChild(tipEl);
  }}
  function showTip(trigger) {{
    var entry = glossaryBySlug[trigger.getAttribute('data-term')];
    if (!entry) return;
    if (!tipEl) buildTipEl();
    clearTimeout(tipHideTimer);
    tipTrigger = trigger;
    tipEl.querySelector('.def-tip-text').textContent = entry.def;
    var link = tipEl.querySelector('.def-tip-link');
    link.href = 'glossary.html#' + entry.slug;
    tipEl.hidden = false;
    trigger.setAttribute('aria-describedby', 'def-tip');
    // Position below the trigger when there is room, else above; clamp
    // horizontally so the tip never leaves the viewport.
    var r = trigger.getBoundingClientRect();
    var w = Math.min(320, window.innerWidth - 16);
    tipEl.style.width = w + 'px';
    var h = tipEl.offsetHeight;
    var top = r.bottom + window.scrollY + 6;
    if (r.bottom + h + 12 > window.innerHeight) top = r.top + window.scrollY - h - 6;
    var left = Math.max(8, Math.min(r.left + window.scrollX, window.innerWidth - w - 8));
    tipEl.style.top = Math.max(8, top) + 'px';
    tipEl.style.left = left + 'px';
  }}
  function hideTip() {{
    if (tipEl) tipEl.hidden = true;
    if (tipTrigger) tipTrigger.removeAttribute('aria-describedby');
    tipTrigger = null;
  }}
  function hideTipSoon() {{
    clearTimeout(tipHideTimer);
    tipHideTimer = setTimeout(hideTip, 250);
  }}
  function wrapGlossaryTerms() {{
    if (!GLOSSARY.length) return;
    var terms = GLOSSARY.filter(function (e) {{ return e.tip; }});
    // Longest pattern first, so a compound (CI/CD) wins over its prefix (CI).
    terms.sort(function (a, b) {{ return b.pattern.length - a.pattern.length; }});
    var scopes = document.querySelectorAll('main .section-body, main .how-to-read');
    scopes.forEach(function (scope) {{
      terms.forEach(function (entry) {{
        var re;
        try {{ re = new RegExp(entry.pattern, entry.flags); }} catch (err) {{ return; }}
        var walker = document.createTreeWalker(scope, NodeFilter.SHOW_TEXT, {{
          acceptNode: function (node) {{
            var p = node.parentElement;
            if (!p) return NodeFilter.FILTER_REJECT;
            if (p.closest('a, code, script, style, button, .def, .crumbs, .share-link, .table-share')) return NodeFilter.FILTER_REJECT;
            return NodeFilter.FILTER_ACCEPT;
          }}
        }});
        var node;
        while ((node = walker.nextNode())) {{
          var m = re.exec(node.textContent);
          if (!m) continue;
          var after = node.splitText(m.index);
          after.splitText(m[0].length);
          var span = document.createElement('span');
          span.className = 'def';
          span.setAttribute('data-term', entry.slug);
          span.setAttribute('tabindex', '0');
          span.textContent = m[0];
          after.parentNode.replaceChild(span, after);
          return;
        }}
      }});
    }});
  }}
  wrapGlossaryTerms();
  // Hover shows the definition; moving into the tip itself keeps it open
  // (so the Glossary link is clickable). Tap shows it on touch; Escape,
  // scrolling, or tapping elsewhere closes it.
  document.addEventListener('mouseover', function (e) {{
    var t = e.target.closest ? e.target.closest('.def') : null;
    if (t) {{ clearTimeout(tipHideTimer); if (tipTrigger !== t) showTip(t); }}
    else if (tipEl && !tipEl.contains(e.target)) hideTipSoon();
  }});
  document.addEventListener('click', function (e) {{
    var t = e.target.closest ? e.target.closest('.def') : null;
    if (t) {{ showTip(t); return; }}
    if (tipEl && !tipEl.contains(e.target)) hideTip();
  }});
  document.addEventListener('focusin', function (e) {{
    var t = e.target.closest ? e.target.closest('.def') : null;
    if (t) showTip(t);
  }});
  document.addEventListener('focusout', function (e) {{
    var t = e.target.closest ? e.target.closest('.def') : null;
    if (t && !(e.relatedTarget && tipEl && tipEl.contains(e.relatedTarget))) hideTip();
  }});
  document.addEventListener('keydown', function (e) {{
    if (e.key === 'Escape') hideTip();
  }});
  window.addEventListener('scroll', hideTip, {{ passive: true }});
  window.addEventListener('resize', hideTip);

  // Back-to-top button: appears once the reader has scrolled down the
  // page, smooth-scrolls back to the top. Invisible until needed.
  var toTop = document.querySelector('.back-to-top');
  if (toTop) {{
    window.addEventListener('scroll', function () {{
      toTop.classList.toggle('visible', window.scrollY > 500);
    }}, {{ passive: true }});
    toTop.addEventListener('click', function () {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }});
  }}
  // Jumping to an anchor (from the sidebar or New in the last 7 days) expands any
  // collapsed ancestor section so the target is visible.
  function expandForAnchor() {{
    var id = location.hash && location.hash.slice(1);
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    // If the anchor IS a collapsible heading, open it too: the walk
    // below only opens ancestors, so a deep link to a subsection
    // heading would otherwise land on a collapsed section.
    if (el.classList) el.classList.remove('collapsed');
    var node = el;
    while (node) {{
      if (node.classList && node.classList.contains('section-body')) {{
        var prev = node.previousElementSibling;
        if (prev) prev.classList.remove('collapsed');
      }}
      // A shared-link landing must NOT force the Search/Filter/Sort
      // panel open: landings arrive with filters cleared and the panel
      // collapsed.
      if (node.tagName === 'DETAILS' && !node.classList.contains('search-filter-panel')) node.open = true;
      node = node.parentElement;
    }}
    el.scrollIntoView();
  }}
  window.addEventListener('hashchange', expandForAnchor);
  expandForAnchor();
}})();
</script>
</body>
</html>
"""


def main(argv):
    input_path = Path(argv[1]) if len(argv) > 1 else WATCHES / "SYNTHESIZED.md"
    output_path = Path(argv[2]) if len(argv) > 2 else WATCHES / "SYNTHESIZED.html"
    build(input_path, output_path)


if __name__ == "__main__":
    main(sys.argv)
