#!/usr/bin/env python3
"""Render the executive dashboard (F-01) from dashboard.json.

The dashboard lives EMBEDDED in the report page (index.html) as its first
top-level section — it is not a standalone page anymore (dashboard.html is
a redirect to index.html#executive-dashboard). build_html.py imports this
module: render_embedded() returns the section's inner HTML (as-of line,
intro, bottom-line strip, countdown, panels), DASH_CSS / COUNTDOWN_JS are the dashboard's
own styles and countdown script, and validate() checks every figure
against the generated index.html.

dashboard.json is the single source of truth. Validation: every figure
needs label/display (or text), source, rating, date, and a link to the
report article that evidences it — the article's runtime id (assigned
by the share JS at page load from the headline), or a section anchor
where no article exists (e.g. §3.6, which is prose, not articles).
compute_article_ids() replicates the share JS's slugify + uniqueId so
validation can check article links against the ids the page will
actually assign. A figure may also carry an "also" list of further
evidencing articles ({anchor, label}) when its conclusion draws on
more than one subsection. A failure exits 1 with the problem listed
— fix the data, don't weaken the check.

Usage: build_dashboard.py [dashboard.json] [index.html]
Validates dashboard.json against index.html; exits 1 on any failure.
Defaults: dashboard.json / index.html in the repo root.
"""

import html
import json
import math
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RATINGS = {
    "established": "●●●●",
    "corroborated": "●●●○",
    "reported": "●●○○",
    "claimed": "●○○○",
}


def esc(s):
    return html.escape(str(s), quote=True)


def rating_html(rating):
    return (
        f'<span class="rating">{RATINGS[rating]} {rating.capitalize()}</span>'
    )


def slugify(text):
    """Python replica of the share JS's slugify() in build_html.py.

    Lowercase, strip anything but ASCII word chars/whitespace/hyphens,
    collapse whitespace and hyphen runs, strip edge hyphens; if the
    result is over 60 chars, cut to 60 and back off to the last hyphen
    (when it is past position 20). Keep in sync with the JS — the
    dashboard's article links depend on the two agreeing.
    """
    s = text.lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.ASCII)
    s = s.strip()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"-+", "-", s)
    s = s.strip("-")
    if len(s) > 60:
        s = s[:60]
        cut = s.rfind("-")
        if cut > 20:
            s = s[:cut]
    return s


class _ArticleIdWalker(HTMLParser):
    """Walk the generated page collecting static ids and article headlines.

    Mirrors the share JS: articles are the <details> blocks (skipping the
    How-to-read block, the mobile Contents block, and "See also" blocks),
    in document order, with the id assigned from the summary's text.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.static_ids = set()
        self.headlines = []
        self._in_details = False
        self._details_class = ""
        self._in_summary = False
        self._summary_text = ""

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.static_ids.add(d["id"])
        if tag == "details":
            self._in_details = True
            self._details_class = d.get("class", "")
            self._summary_text = ""
        elif tag == "summary" and self._in_details:
            self._in_summary = True

    def handle_endtag(self, tag):
        if tag == "summary":
            self._in_summary = False
        elif tag == "details":
            self._in_details = False
            if "how-to-read" in self._details_class:
                return
            if "toc-inline" in self._details_class:
                return
            text = re.sub(r"\s+", " ", self._summary_text).strip()
            if text == "See also":
                return
            self.headlines.append(text)

    def handle_data(self, data):
        if self._in_summary:
            self._summary_text += data


def compute_article_ids(index_html):
    """The article ids the share JS will assign on this page.

    Returns {id: headline}. Replicates the JS uniqueId seeding (every
    static id in the document) and document-order assignment — articles
    run before tables and paragraphs in the share code, so nothing else
    can claim an article's id.
    """
    walker = _ArticleIdWalker()
    walker.feed(index_html)
    used = dict.fromkeys(walker.static_ids)
    out = {}
    for headline in walker.headlines:
        base = slugify(headline) or "item"
        ident, n = base, 2
        while ident in used:
            ident = f"{base}-{n}"
            n += 1
        used[ident] = True
        out[ident] = headline
    return out


def source_html(f):
    """Linked source name + date + rating, the traceability line.

    The source name links to the report article that evidences the
    figure; the article's Source line takes the reader to the primary
    source. A figure with an "also" list links its further evidencing
    articles after the source name.
    """
    parts = [f'<a href="{esc(f["link"])}">{esc(f["source"])}</a>']
    for extra in f.get("also") or []:
        parts.append(
            f'also in <a href="{esc(extra["anchor"])}">'
            f'{esc(extra["label"])}</a>'
        )
    if f.get("source_note"):
        parts.append(esc(f["source_note"]))
    parts.append(esc(f["date"]))
    parts.append(rating_html(f["rating"]))
    return '<p class="fig-source">' + " · ".join(parts) + "</p>"


def render_bar(f):
    tone = f.get("tone", "navy")
    note = f'<p class="fig-note">{esc(f["note"])}</p>' if f.get("note") else ""
    return (
        '<div class="bar-row">'
        '<div class="bar-head">'
        f'<span class="bar-label">{esc(f["label"])}</span>'
        f'<span class="bar-value">{esc(f["display"])}</span>'
        "</div>"
        '<div class="bar-track">'
        f'<div class="bar-fill {tone}" style="width: {f["value"]}%"></div>'
        "</div>"
        f"{source_html(f)}{note}"
        "</div>"
    )


def render_stat(f):
    note = f'<p class="fig-note">{esc(f["note"])}</p>' if f.get("note") else ""
    return (
        '<div class="stat-card">'
        f'<p class="stat-value">{esc(f["display"])}</p>'
        f'<p class="stat-label">{esc(f["label"])}</p>'
        f"{source_html(f)}{note}"
        "</div>"
    )


def render_text(f):
    return f'<p class="ledger-item">{esc(f["text"])}</p>' + source_html(f)


def render_note(f):
    return (
        '<div class="note-card">'
        f"<p>{esc(f['text'])}</p>"
        f"{source_html(f)}"
        "</div>"
    )


def render_stacked(b):
    segs = "".join(
        f'<div class="stacked-seg {s.get("tone", "navy")}" '
        f'style="flex: {s["value"]} 1 0%"></div>'
        for s in b["segments"]
    )
    legend = "".join(
        f'<span><span class="chip stacked-seg {s.get("tone", "navy")}">'
        f"</span>{esc(s['label'])} — {s['value']}%</span>"
        for s in b["segments"]
    )
    return (
        f'<p class="stacked-title">{esc(b["title"])}</p>'
        f'<div class="stacked-bar">{segs}</div>'
        f'<div class="stacked-legend">{legend}</div>'
        f"{source_html(b)}"
    )


def render_block(b):
    kind = b["kind"]
    label = (
        f'<p class="block-label">{esc(b["label"])}</p>' if b.get("label") else ""
    )
    if kind == "bars":
        return label + "".join(render_bar(f) for f in b["items"])
    if kind == "stats":
        cards = "".join(render_stat(f) for f in b["items"])
        return label + f'<div class="stats-grid">{cards}</div>'
    if kind == "notes":
        return label + "".join(render_note(f) for f in b["items"])
    if kind == "stacked":
        return render_stacked(b)
    if kind == "bignote":
        return f'<div class="bignote">{esc(b["text"])}</div>'
    if kind == "ledger":
        def col(side):
            items = "".join(render_text(f) for f in b[side]["items"])
            return (
                '<div class="ledger-col">'
                f'<p class="ledger-col-title">{esc(b[side]["title"])}</p>'
                f"{items}</div>"
            )

        foot = (
            f'<p class="ledger-foot">{esc(b["footnote"])}</p>'
            if b.get("footnote")
            else ""
        )
        return (
            f'<div class="ledger">{col("left")}{col("right")}</div>{foot}'
        )
    raise ValueError(f"unknown block kind: {kind}")


def render_panel(p, level=3):
    blocks = "".join(render_block(b) for b in p["blocks"])
    return (
        f'<h{level} id="{esc(p["id"])}" class="dash-panel">{esc(p["title"])}</h{level}>'
        f'<p class="panel-lede">{esc(p["lede"])}</p>'
        f"{blocks}"
    )


def render_countdown(deadlines):
    cards = "".join(
        '<div class="cd-card"><a href="#what-were-watching">'
        f'<p class="cd-label">{esc(d["label"])}</p>'
        f'<p class="cd-date">{esc(d["display"])}</p>'
        f'<p class="cd-days" data-deadline="{esc(d["date"])}"></p>'
        "</a></div>"
        for d in deadlines
    )
    return (
        '<p class="dash-strip-label">Countdown</p>'
        f'<div class="countdown-strip">{cards}</div>'
    )


# Strip chart colours (2026-11-15): rust is the AI side, blue the
# not-AI side — the same scheme on the pies and the comparison bars.
RUST = "#b3543f"
BLUE = "#283060"


def render_pie(it):
    """Inline SVG pie for a percentage figure: the rust wedge is the
    AI side, the blue remainder is the rest. The number sits NEXT TO
    the pie (in the graphic row), not inside it.
    """
    chart = it["chart"]
    v = chart["value"]
    if v <= 0:
        wedge = ""
    elif v >= 100:
        wedge = f'<circle cx="50" cy="50" r="40" fill="{RUST}"/>'
    else:
        theta = math.radians(v / 100 * 360)
        x = 50 + 40 * math.sin(theta)
        y = 50 - 40 * math.cos(theta)
        large = 1 if v > 50 else 0
        wedge = (
            f'<path d="M 50,50 L 50,10 A 40,40 0 {large} 1 '
            f'{x:.1f},{y:.1f} Z" fill="{RUST}"/>'
        )
    return (
        '<svg class="bl-pie" viewBox="0 0 100 100" role="img" '
        f'aria-label="{esc(it["label"])}">'
        f'<circle cx="50" cy="50" r="40" fill="{BLUE}"/>'
        f"{wedge}</svg>"
    )


def render_question():
    """A question mark inside a circle — the graphic for the
    profitability item, which has no data to chart.
    """
    return (
        '<svg class="bl-question" viewBox="0 0 100 100" role="img" '
        'aria-label="Unknown — no credible figure exists">'
        f'<circle cx="50" cy="50" r="40" fill="none" stroke="{BLUE}" '
        'stroke-width="6"/>'
        '<text x="50" y="68" text-anchor="middle" '
        'class="bl-question-mark">?</text>'
        "</svg>"
    )


def render_compare(chart):
    """Two horizontal bars for a head-to-head figure (Sajadi 135 vs 12
    vulnerabilities; SusVibes 2.5× vs 1× review cost). Widths are
    proportional to the values; the larger side is always 100%.
    """
    top = max(chart["a"]["value"], chart["b"]["value"])
    rows = []
    for side in ("a", "b"):
        s = chart[side]
        w = 100 * s["value"] / top
        rows.append(
            '<div class="bar-row">'
            '<div class="bar-head">'
            f'<span class="bar-label">{esc(s["label"])}</span>'
            f'<span class="bar-value">{esc(s["display"])}</span>'
            "</div>"
            '<div class="bar-track">'
            f'<div class="bar-fill {esc(s["tone"])}" '
            f'style="width: {w:.1f}%"></div>'
            "</div></div>"
        )
    return '<div class="bl-compare">' + "".join(rows) + "</div>"


def render_bottom_line(items):
    """The bottom-line strip (2026-11-15): seven at-a-glance items above
    the countdown — the WHOLE card is one link to its evidencing
    article (like the countdown cards; the source name is plain text,
    not a nested link), so the number, the chart, and the description
    all take the reader to the article. Yorgo's pick.
    Layout is 3+3+1: six cards in two rows of three, then the
    profitability item full-width (it has no figure — its display IS
    the finding, "Insufficient data", with no rating or date, linking
    to the money panel; its graphic is a question mark in a circle).
    Charts, one colour scheme throughout — rust is the AI side, blue
    the not-AI side: pies for the three percentages (number next to
    the pie, with a two-chip legend), comparison bars for the two
    multipliers (AI patches rust vs human patches blue; review cost
    blue — the review is the human side — vs generation alone rust);
    the 188 count has no chartable comparison in the report, so it
    keeps the big number.
    """
    cards = []
    for it in items:
        chart = it.get("chart")
        legend = ""
        if chart and chart["kind"] == "pie":
            visual = (
                '<div class="bl-graphic-row">'
                f"{render_pie(it)}"
                f'<p class="stat-value">{esc(it["display"])}</p>'
                "</div>"
            )
            legend = (
                '<p class="bl-legend">'
                '<span class="bl-chip rust"></span>'
                f'{esc(chart["a_label"])} {chart["value"]}% · '
                '<span class="bl-chip blue"></span>'
                f'{esc(chart["b_label"])} {100 - chart["value"]}%</p>'
            )
        elif chart and chart["kind"] == "question":
            visual = (
                '<div class="bl-graphic-row">'
                f"{render_question()}"
                f'<p class="stat-value">{esc(it["display"])}</p>'
                "</div>"
            )
        else:
            visual = f'<p class="stat-value">{esc(it["display"])}</p>'
            if chart and chart["kind"] == "compare":
                visual += render_compare(chart)
        parts = [esc(it["source"])]
        if it.get("date"):
            parts.append(esc(it["date"]))
        if it.get("rating"):
            parts.append(rating_html(it["rating"]))
        note = f'<p class="fig-note">{esc(it["note"])}</p>' if it.get("note") else ""
        cls = "stat-card bl-full" if it.get("full") else "stat-card"
        cards.append(
            f'<div class="{cls}"><a href="{esc(it["link"])}">'
            f"{visual}{legend}"
            f'<p class="stat-label">{esc(it["label"])}</p>'
            '<p class="fig-source">' + " · ".join(parts) + "</p>"
            f"{note}</a></div>"
        )
    return (
        '<p class="dash-strip-label">The bottom line</p>'
        '<div class="bottom-line-strip">' + "".join(cards) + "</div>"
    )


def render_embedded(data):
    """The dashboard section's inner HTML, for embedding in index.html.

    Panels render as H3s under the section's H2 ("Executive dashboard").
    The as-of line is a small muted line, not a second banner — the
    page's own As-of banner (row 1) is the page-level date.
    """
    parts = [
        f'<p class="dash-asof">Dashboard figures as of {esc(data["as_of_label"])}</p>',
        f'<p class="dash-intro">{esc(data["note"])}</p>',
        render_bottom_line(data["bottom_line"]),
        render_countdown(data["deadlines"]),
    ]
    parts += [render_panel(p, level=3) for p in data["panels"]]
    return "".join(parts)


def iter_figures(data):
    """Every figure-like dict in the file, for validation."""
    for p in data["panels"]:
        for b in p["blocks"]:
            if b["kind"] == "ledger":
                yield from b["left"]["items"]
                yield from b["right"]["items"]
            elif b["kind"] in ("bars", "stats", "notes"):
                yield from b["items"]
            elif b["kind"] == "stacked":
                yield b


def validate(data, index_html):
    errors = []
    anchors = set(re.findall(r'id="([^"]+)"', index_html))
    # Article ids are assigned at runtime by the share JS, so they are
    # not in the static HTML — accept the ids the page will assign.
    anchors |= set(compute_article_ids(index_html))

    def check_link(src, link):
        # Same-page anchors ("#...") or legacy "index.html#..." links.
        if link.startswith("#"):
            frag = link[1:]
        elif link.startswith("index.html#"):
            frag = link.split("#", 1)[1]
        else:
            errors.append(f"{src}: bad link {link!r}")
            return
        if frag not in anchors:
            errors.append(f"{src}: anchor missing in index.html: {link}")

    for f in iter_figures(data):
        src = f.get("source", f.get("title", "?"))
        for field in ("source", "rating", "date", "link"):
            if field not in f:
                errors.append(f"{src}: missing {field}")
        if f.get("rating") not in RATINGS:
            errors.append(f"{src}: bad rating {f.get('rating')!r}")
        check_link(src, f.get("link", ""))
        for extra in f.get("also") or []:
            if "anchor" not in extra or "label" not in extra:
                errors.append(f"{src}: malformed also entry {extra!r}")
                continue
            check_link(src, extra["anchor"])
        if f.get("kind") == "bar":
            v = f.get("value")
            if not isinstance(v, (int, float)) or not 0 <= v <= 100:
                errors.append(f"{src}: bad bar value {v!r}")
        if "kind" in f and f["kind"] == "stacked":
            total = sum(s["value"] for s in f["segments"])
            if not 99.5 <= total <= 100.5:
                errors.append(f"{src}: stacked segments sum to {total}")
    # Bottom-line strip: same link check; rating and date are optional
    # (the profitability item has neither — its display is the finding).
    for it in data.get("bottom_line", []):
        src = it.get("source", "?")
        for field in ("display", "label", "source", "link"):
            if field not in it:
                errors.append(f"bottom line {src}: missing {field}")
        if it.get("rating") is not None and it["rating"] not in RATINGS:
            errors.append(f"bottom line {src}: bad rating {it.get('rating')!r}")
        check_link(src, it.get("link", ""))
        chart = it.get("chart")
        if chart is not None:
            kind = chart.get("kind")
            if kind == "pie":
                v = chart.get("value")
                if not isinstance(v, (int, float)) or not 0 <= v <= 100:
                    errors.append(f"bottom line {src}: bad chart value {v!r}")
                for field in ("a_label", "b_label"):
                    if field not in chart:
                        errors.append(f"bottom line {src}: pie missing {field}")
            elif kind == "question":
                pass
            elif kind == "compare":
                for side in ("a", "b"):
                    s = chart.get(side) or {}
                    for field in ("label", "value", "display", "tone"):
                        if field not in s:
                            errors.append(
                                f"bottom line {src}: compare {side} missing {field}"
                            )
                    if not isinstance(s.get("value"), (int, float)) or (
                        isinstance(s.get("value"), (int, float))
                        and s["value"] <= 0
                    ):
                        errors.append(
                            f"bottom line {src}: compare {side} bad value "
                            f"{s.get('value')!r}"
                        )
                    if s.get("tone") not in ("navy", "gap"):
                        errors.append(
                            f"bottom line {src}: compare {side} bad tone "
                            f"{s.get('tone')!r}"
                        )
            else:
                errors.append(f"bottom line {src}: bad chart kind {kind!r}")
    if "what-were-watching" not in anchors:
        errors.append("countdown link target #what-were-watching missing")
    return errors


DASH_CSS = """
  /* Executive dashboard (F-01): at-a-glance figures, same palette. */
  .dash-asof { font-size: 13px; color: var(--muted); margin: 0 0 8px; }
  .dash-intro { color: var(--muted); font-size: 15px; margin: 0 0 24px; }
  .dash-strip-label { font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 0 0 10px; font-weight: 600; }
  .bottom-line-strip { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 0 0 20px; }
  .bottom-line-strip .stat-value { overflow-wrap: break-word; }
  .bottom-line-strip .stat-card a { text-decoration: none; color: inherit; display: block; }
  .stat-card.bl-full { grid-column: 1 / -1; border-style: dashed; }
  .bl-graphic-row { display: flex; align-items: center; gap: 14px; margin: 0 0 8px; }
  .bl-graphic-row .stat-value { margin: 0; }
  .bl-pie { width: 88px; height: 88px; flex: 0 0 auto; }
  .bl-question { width: 88px; height: 88px; flex: 0 0 auto; }
  .bl-question-mark { font-family: Georgia, 'Times New Roman', Times, serif; font-size: 52px; font-weight: 700; fill: #283060; }
  .bl-legend { font-size: 12px; color: var(--muted); margin: 0 0 6px; }
  .bl-chip { display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 4px; vertical-align: middle; }
  .bl-chip.rust { background: #b3543f; }
  .bl-chip.blue { background: #283060; }
  .bl-compare .bar-row { margin-bottom: 8px; }
  .countdown-strip { display: flex; flex-wrap: wrap; gap: 12px; margin: 0 0 8px; }
  .cd-card { flex: 1 1 180px; border: 1px solid var(--line); border-left: 3px solid var(--logo-navy); border-radius: 6px; padding: 10px 12px; background: #fdfbf7; }
  .cd-card a { text-decoration: none; color: inherit; display: block; }
  .cd-card .cd-label { font-size: 13px; color: var(--muted); margin: 0 0 2px; }
  .cd-card .cd-date { font-weight: 700; font-size: 15px; margin: 0; }
  .cd-card .cd-days { font-size: 13px; color: var(--accent); font-weight: 600; margin: 2px 0 0; }
  .panel-lede { color: var(--muted); font-size: 15px; margin: -4px 0 16px; }
  .block-label { font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 24px 0 10px; font-weight: 600; }
  .bar-row { margin: 0 0 14px; }
  .bar-head { display: flex; justify-content: space-between; align-items: baseline; gap: 12px; margin-bottom: 4px; }
  .bar-label { font-size: 15px; }
  .bar-value { font-weight: 700; font-size: 16px; color: var(--logo-navy); white-space: nowrap; }
  .bar-track { height: 10px; background: #ece5d3; border-radius: 5px; overflow: hidden; }
  .bar-fill { height: 100%; background: var(--logo-navy); border-radius: 5px; }
  .bar-fill.gap { background: #b3543f; }
  .fig-source { font-size: 13px; color: var(--muted); margin: 3px 0 0; }
  .fig-source a { color: var(--muted); }
  .fig-note { font-size: 13px; color: var(--muted); margin: 2px 0 0; font-style: italic; }
  .rating { white-space: nowrap; }
  .stats-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; margin: 0 0 8px; }
  .stat-card { border: 1px solid var(--line); border-radius: 6px; padding: 12px 14px; background: #fdfbf7; }
  .stat-value { font-family: Georgia, 'Times New Roman', Times, serif; font-size: 30px; font-weight: 700; color: var(--logo-navy); line-height: 1.1; margin: 0 0 4px; }
  .stat-label { font-size: 14px; margin: 0 0 6px; line-height: 1.4; }
  .stacked-title { font-weight: 600; margin: 0 0 6px; }
  .stacked-bar { display: flex; height: 26px; border-radius: 5px; overflow: hidden; }
  .stacked-seg.navy { background: var(--logo-navy); }
  .stacked-seg.gap { background: #b3543f; }
  .stacked-seg.muted { background: #c9c2b0; }
  .stacked-legend { display: flex; flex-wrap: wrap; gap: 4px 16px; margin: 8px 0 4px; font-size: 13px; color: var(--muted); }
  .stacked-legend .chip { display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 5px; vertical-align: middle; }
  .ledger { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  .ledger-col-title { font-size: 15px; font-weight: 700; color: var(--logo-navy); margin: 0 0 10px; }
  .ledger-item { margin: 0 0 4px; font-size: 15px; }
  .ledger-foot { margin: 12px 0 0; font-size: 14px; color: var(--muted); font-style: italic; }
  .note-card { border: 1px solid var(--line); border-left: 3px solid var(--logo-navy); border-radius: 6px; padding: 12px 14px; margin: 0 0 12px; background: #fdfbf7; }
  .note-card p { margin: 0; }
  .bignote { border: 1px solid var(--line); border-left: 3px solid var(--logo-navy); border-radius: 6px; padding: 16px; background: #f0f1f7; font-size: 17px; margin: 0 0 16px; }
  @media (max-width: 900px) { .ledger { grid-template-columns: 1fr; } .bottom-line-strip { grid-template-columns: repeat(2, 1fr); } }
  @media (max-width: 600px) { .bottom-line-strip { grid-template-columns: 1fr; } }
"""

COUNTDOWN_JS = """
<script>
(function () {
  // Countdown: days remaining for each dated item, computed at load.
  var today = new Date(); today.setHours(0, 0, 0, 0);
  document.querySelectorAll('[data-deadline]').forEach(function (el) {
    var d = new Date(el.getAttribute('data-deadline') + 'T00:00:00');
    var days = Math.round((d - today) / 86400000);
    if (days < 0) el.textContent = 'passed';
    else if (days === 0) el.textContent = 'today';
    else if (days === 1) el.textContent = 'tomorrow';
    else el.textContent = 'in ' + days + ' days';
  });
})();
</script>
"""


def main(argv):
    data_path = argv[1] if len(argv) > 1 else str(REPO / "dashboard.json")
    index_path = argv[2] if len(argv) > 2 else str(REPO / "index.html")
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    index_html = Path(index_path).read_text(encoding="utf-8")
    errors = validate(data, index_html)
    if errors:
        print("dashboard.json validation FAILED:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"dashboard.json OK ({len(list(iter_figures(data)))} figures, "
          f"{len(data['panels'])} panels, "
          f"{len(data.get('bottom_line', []))} bottom-line items)")


if __name__ == "__main__":
    main(sys.argv)
