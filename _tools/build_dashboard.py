#!/usr/bin/env python3
"""Build the executive dashboard page (dashboard.html) from dashboard.json.

F-01: at-a-glance numbers for executives, every figure traceable to the
report. dashboard.json is the single source of truth; this generator
renders it into the site's page shell by reusing build_page.py's TEMPLATE,
so the dashboard always matches the site's design. The dashboard's own
CSS and JS are inserted after TEMPLATE.format() (they contain braces, so
they must not pass through .format()).

Validation: every figure needs label/display (or text), source, rating,
date, and a link whose #anchor exists in index.html. A failure exits 1
with the problem listed — fix the data, don't weaken the check.

Usage: build_dashboard.py [dashboard.json] [dashboard.html]
Defaults: dashboard.json / dashboard.html in the repo root.
"""

import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_page  # noqa: E402  (TEMPLATE only — the shell and base CSS)

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


def source_html(f):
    """Linked source name + date + rating, the traceability line."""
    parts = [f'<a href="{esc(f["link"])}">{esc(f["source"])}</a>']
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


def render_panel(p):
    blocks = "".join(render_block(b) for b in p["blocks"])
    return (
        f'<h2 id="{esc(p["id"])}" class="dash-panel">{esc(p["title"])}</h2>'
        f'<p class="panel-lede">{esc(p["lede"])}</p>'
        f"{blocks}"
    )


def render_countdown(deadlines):
    cards = "".join(
        '<div class="cd-card"><a href="index.html#what-were-watching">'
        f'<p class="cd-label">{esc(d["label"])}</p>'
        f'<p class="cd-date">{esc(d["display"])}</p>'
        f'<p class="cd-days" data-deadline="{esc(d["date"])}"></p>'
        "</a></div>"
        for d in deadlines
    )
    return f'<div class="countdown-strip">{cards}</div>'


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
    for f in iter_figures(data):
        src = f.get("source", f.get("title", "?"))
        for field in ("source", "rating", "date", "link"):
            if field not in f:
                errors.append(f"{src}: missing {field}")
        if f.get("rating") not in RATINGS:
            errors.append(f"{src}: bad rating {f.get('rating')!r}")
        link = f.get("link", "")
        if not link.startswith("index.html#"):
            errors.append(f"{src}: bad link {link!r}")
        elif link.split("#", 1)[1] not in anchors:
            errors.append(f"{src}: anchor missing in index.html: {link}")
        if f.get("kind") == "bar":
            v = f.get("value")
            if not isinstance(v, (int, float)) or not 0 <= v <= 100:
                errors.append(f"{src}: bad bar value {v!r}")
        if "kind" in f and f["kind"] == "stacked":
            total = sum(s["value"] for s in f["segments"])
            if not 99.5 <= total <= 100.5:
                errors.append(f"{src}: stacked segments sum to {total}")
    if "what-were-watching" not in anchors:
        errors.append("countdown link target #what-were-watching missing")
    return errors


def build(data_path, output_path):
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    index_html = (REPO / "index.html").read_text(encoding="utf-8")
    errors = validate(data, index_html)
    if errors:
        print("dashboard.json validation FAILED:")
        for e in errors:
            print("  -", e)
        sys.exit(1)

    toc_items = "".join(
        f'<li><a href="#{esc(p["id"])}">{esc(p["title"])}</a></li>'
        for p in data["panels"]
    )
    toc = f'<div class="toc"><ul>{toc_items}</ul></div>'

    body = (
        "<h1>Executive dashboard"
        "<em>CI Sitrep — Code &amp; Finance</em></h1>"
        '<p class="back-inline"><a href="index.html">&larr; Back to the report</a></p>'
        '<div class="as-of-banner">As of <strong>'
        f"{esc(data['as_of_label'])}</strong></div>"
        f'<p class="dash-intro">{esc(data["note"])}</p>'
        f"{render_countdown(data['deadlines'])}"
        + "".join(render_panel(p) for p in data["panels"])
    )

    html_out = build_page.TEMPLATE.format(
        title="Executive dashboard — CI Sitrep",
        toc=toc,
        body=body,
    )
    # Dashboard CSS/JS are inserted AFTER .format() — they contain braces.
    html_out = html_out.replace("</style>", DASH_CSS + "\n</style>", 1)
    html_out = html_out.replace("</body>", DASH_JS + "\n</body>", 1)
    Path(output_path).write_text(html_out, encoding="utf-8")
    print(f"Wrote {output_path} ({len(html_out)} bytes)")


DASH_CSS = """
  /* Executive dashboard (F-01): at-a-glance figures, same palette. */
  .as-of-banner { background: #E9EAF1; border: 1px solid #C5C8DC; border-radius: 6px; padding: 10px 14px; margin: 0 0 16px; font-size: 15px; }
  .as-of-banner strong { color: var(--logo-navy); }
  .dash-intro { color: var(--muted); font-size: 15px; margin: 0 0 24px; }
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
  @media (max-width: 900px) { .ledger { grid-template-columns: 1fr; } }
"""

DASH_JS = """
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
  // Dashboard panels start open (the page template collapses every
  // heading); the reader can still collapse one by clicking its heading.
  document.querySelectorAll('main h2.dash-panel').forEach(function (h) {
    h.classList.remove('collapsed');
  });
  // Breadcrumbs are noise on a one-screen dashboard.
  document.querySelectorAll('main .crumbs').forEach(function (el) {
    el.remove();
  });
})();
</script>
"""

if __name__ == "__main__":
    data_path = sys.argv[1] if len(sys.argv) > 1 else str(REPO / "dashboard.json")
    output_path = (
        sys.argv[2] if len(sys.argv) > 2 else str(REPO / "dashboard.html")
    )
    build(data_path, output_path)
