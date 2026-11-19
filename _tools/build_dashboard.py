#!/usr/bin/env python3
"""Render the executive dashboard (F-01) from dashboard.json.

The dashboard lives EMBEDDED in the report page (index.html) as its first
top-level section — it is not a standalone page anymore (dashboard.html is
a redirect to index.html#executive-dashboard). build_html.py imports this
module: render_embedded() returns the section's inner HTML (as-of line,
intro, bottom-line strip, countdown, filter bar, panels), DASH_CSS /
COUNTDOWN_JS / FILTER_JS are the dashboard's own styles and scripts, and
validate() checks every figure against the generated index.html.

dashboard.json is the single source of truth for figures. Every figure
carries a tile type ("tile": pie | ratio | big-number | no-data |
sparkline | flag | note | waffle | paired) and a sentiment (positive | negative |
neutral); validate() enforces both, plus the per-type fields
(value/range/segments + pie_split for pies, chart.a/b or before/after
for ratios, history_key for sparklines, a compare chart of two counts +
caption for waffles, a figures list of exactly two pie figures for
paired). All figures render as tiles in one grid per panel — the bar
system is retired (render_bar/render_compare are gone; render_stacked's
segments now feed the segmented-pie renderer).

Tag join (filters): build_dashboard.py parses the tag lines from
SYNTHESIZED.md DIRECTLY (single source of truth — the "<!-- tags: ... -->"
comment directly above each article's <details> line). Each figure joins
to its evidencing article via the figure's link slug, and the article's
tags are emitted as data-* attributes on the tile (data-subject,
data-type, ... data-date, data-rating) — tag_attrs() builds them, and
build_html.py reuses the same function for the article <details> blocks,
so tiles and articles filter on identical attributes. A figure whose
article has no value for a filtered dimension does NOT match that
dimension (the interim untagged-visible rule retired with the backfill,
Round 4). The only exemption is figures that CANNOT be tagged — the §3.6
prose figures and the money bignote, which carry no article tags at all:
they render with the tile-untagged class and stay visible under any
filter (and keep their editorial position under any sort). No tag
fields live in dashboard.json (no second copy).

History join (sparklines): dashboard-history.json is an append-only log
of dated values, keyed by series key. A sparkline figure carries
"history_key"; the generator joins history[figure["history_key"]] to
render the sparkline. The series' last point must match the figure's
display (validate() checks) so the tile and the log cannot drift apart.

Tile ids are deterministic: tile-<panel-id>-<slug-of-label>, deduped
with -2/-3 suffixes (assign_tile_ids). The share JS in build_html.py
appends a share button to every tile; a shared tile link lands with
filters cleared (FILTER_JS) and expandForAnchor opens the panel.

Validation: every figure needs label/display (or text), source, rating,
date, and a link to the report article that evidences it — the article's
runtime id (assigned by the share JS at page load from the headline), or
a section anchor where no article exists (e.g. §3.6, which is prose, not
articles). compute_article_ids() replicates the share JS's slugify +
uniqueId so validation can check article links against the ids the page
will actually assign. A figure may also carry an "also" list of further
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
from datetime import date
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RATINGS = {
    "established": "●●●●",
    "corroborated": "●●●○",
    "reported": "●●○○",
    "claimed": "●○○○",
}
RATING_NUM = {"established": 4, "corroborated": 3, "reported": 2, "claimed": 1}
TILE_TYPES = {"pie", "ratio", "big-number", "no-data", "sparkline", "flag", "note", "waffle", "paired"}
SENTIMENTS = {"positive", "negative", "neutral"}

# Pie/strip colours (2026-11-18, Yorgo's three rules): rust is the AI
# side where the split is AI vs human; otherwise blue is the favourable
# side and rust the adverse side, grey the unclassified rest. pie_split
# names the WEDGE; the remainder follows by rule — never a boolean.
RUST = "#b3543f"
BLUE = "#283060"
GREY = "#c9c2b0"  # the unclassified rest (rule 3) / a mixed segment
PIE_SPLITS = {
    # split value -> (wedge colour, remainder colour)
    "identity": (RUST, BLUE),          # rule 1: CI vs EI / AI side vs rest
    "positive": (BLUE, RUST),          # rule 2: wedge is the good side
    "negative": (RUST, BLUE),          # rule 2: wedge is the bad side
    "positive-neutral": (BLUE, GREY),  # rule 3: good wedge, rest unclassified
    "negative-neutral": (RUST, GREY),  # rule 3: bad wedge, rest unclassified
    "none": (BLUE, GREY),              # fallback: no valence, no identity
}
SEGMENT_TONES = {"blue": BLUE, "rust": RUST, "grey": GREY}
# Chip class for a pie colour (strip legends derive their chips from
# pie_split; the grey chip reuses the muted chip class — same hex).
CHIP_CLASS = {RUST: "rust", BLUE: "blue", GREY: "muted"}


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
    How-to-read block, the mobile Contents block, the dashboard's More
    filters block, the Search/Filter/Sort panel, and "See also" blocks),
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
            if "dash-more-filters" in self._details_class:
                return
            if "search-filter-panel" in self._details_class:
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


# --- Tag join ---------------------------------------------------------------
# The tag lines live in SYNTHESIZED.md only (TAXONOMY_DRAFT.md v2).
# Format: <!-- tags: subject=1 | type=benchmark | ... --> directly above
# the article's <details> line; multi-value dimensions are comma-separated.
# The join key is the article's runtime id, computed from the headline the
# same way the share JS computes it (textContent -> slugify -> dedupe).

TAG_RE = re.compile(
    r"<!-- tags: (.*?) -->\s*\n<details>\n<summary>(.*?)</summary>", re.DOTALL
)
TAG_LINE_RE = re.compile(r"<!-- tags: ")
# Filter controls, in panel order (Yorgo's order, Round 4): the top line
# first, then the "More filters" row. Each entry is (dimension, label,
# options, kind) — kind "select" is a native <select> over the fixed
# taxonomy-v2 options; "checkbox" is a multi-choice fieldset (OR within
# the dimension); "company" is a <select> whose options are derived at
# build time from the distinct company values in the tag data (open
# vocabulary — the list is data, not taxonomy). Sector has NO control
# (Round 4): the tags stay in the data and the data-sector attribute
# stays on tiles/articles as the ready hook for the separate product.
FILTER_DIMS = [
    ("industry", "Industry", [("banking", "Banking"),
                              ("asset-management", "Asset management"),
                              ("hedge-funds", "Hedge funds"),
                              ("insurance", "Insurance"), ("mga", "MGA"),
                              ("payments", "Payments"),
                              ("capital-markets", "Capital markets"),
                              ("fintech", "Fintech"), ("software", "Software"),
                              ("cloud", "Cloud"), ("ai-labs", "AI labs"),
                              ("professional-services", "Professional services"),
                              ("cross-industry", "Cross-industry")], "select"),
    ("severity", "Severity", [("critical", "Critical"), ("material", "Material"),
                              ("directional", "Directional"),
                              ("background", "Background")], "select"),
    ("pnl-impact", "P&L impact", [("revenue", "Revenue"), ("cost", "Cost"),
                                  ("risk", "Risk"),
                                  ("compliance", "Compliance")], "select"),
    ("horizon", "Horizon", [("immediate", "Immediate"),
                            ("quarter", "This quarter"),
                            ("year", "Within 12 months"),
                            ("longer", "Longer term")], "select"),
    ("register", "Technical level", [("technical", "Technical"),
                                     ("mixed", "Mixed"),
                                     ("business", "Business")], "select"),
    ("subject", "Section", [("1", "Pre-commit"), ("2", "In codebase"),
                            ("3", "Agentic"), ("0", "Cross-cutting")], "select"),
    ("type", "Type", [("benchmark", "Benchmark"), ("study", "Study"),
                      ("product", "Product"), ("incident", "Incident"),
                      ("regulation", "Regulation"), ("guidance", "Guidance"),
                      ("survey", "Survey"), ("framework", "Framework"),
                      ("practice", "Practice"), ("verdict", "Verdict")], "checkbox"),
    ("confidence", "Confidence", [("established", "Established"),
                                  ("corroborated", "Corroborated"),
                                  ("reported", "Reported"),
                                  ("claimed", "Claimed")], "select"),
    # Jurisdiction lists the fixed taxonomy vocabulary, all nine values
    # even with zero articles today (eu, greece) — the option must
    # already exist the day the first article lands.
    ("jurisdiction", "Jurisdiction", [("global", "Global"),
                                      ("us-federal", "US federal"),
                                      ("us-state", "US state"),
                                      ("new-york", "New York"),
                                      ("uk", "UK"), ("eu", "EU"),
                                      ("hong-kong", "Hong Kong"),
                                      ("singapore", "Singapore"),
                                      ("greece", "Greece")], "select"),
    ("company", "Company", None, "company"),
]
# The top line is the first five controls; the rest live under More filters.
TOP_LINE_DIMS = FILTER_DIMS[:5]
MORE_DIMS = FILTER_DIMS[5:]
# Dimensions emitted as data-* attributes on tiles AND articles (the
# filter/sort JS reads these). Sector is in the attributes but has no
# control — see the FILTER_DIMS note above.
ATTR_DIMS = ["subject", "sector", "confidence", "severity", "type",
             "industry", "register", "pnl-impact", "horizon",
             "jurisdiction", "company"]
# Sort keys, in select order: (value, option label). The label states the
# key's default direction, so the asc/desc toggle's meaning is never a
# puzzle. Sort applies to dashboard tiles within panels ONLY — articles
# filter but do not sort. "date" reads data-date; "confidence" reads
# data-rating; every other key reads data-<key>.
SORT_KEYS = [
    ("panel", "Panel order"),
    ("date", "Date (newest first)"),
    ("confidence", "Confidence (highest first)"),
    ("severity", "Severity (highest first)"),
    ("horizon", "Horizon (soonest first)"),
    ("subject", "Section (in order)"),
    ("type", "Type (A–Z)"),
    ("industry", "Industry (A–Z)"),
    ("pnl-impact", "P&L impact (A–Z)"),
    ("register", "Technical level (technical first)"),
    ("jurisdiction", "Jurisdiction (A–Z)"),
    ("company", "Company (A–Z)"),
]


def headline_text(summary_html):
    """A <summary>'s textContent equivalent: markdown links become their
    link text, HTML tags are stripped, whitespace collapses. This is what
    the share JS slugifies at runtime, so the tag join must use it too
    (slugifying the raw Markdown would hash the link URLs into the id).
    """
    text = re.sub(r"\[([^\]]*)\]\([^)]+\)", r"\1", summary_html)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def parse_article_tags(md_path=None):
    """{article_id: {dimension: [values]}} from SYNTHESIZED.md's tag lines.

    The id is computed from the headline (slugify + document-order dedupe),
    replicating the share JS — except the JS also seeds its used-id set
    with the page's static ids, which are not knowable here. A headline
    slug colliding with a static id would join to the wrong id; validate()
    catches that (the figure's link would find no tags), and no collision
    exists today (all 85 tag lines match the computed article ids).
    """
    path = Path(md_path) if md_path else REPO / "SYNTHESIZED.md"
    if not path.exists():
        return {}
    md = path.read_text(encoding="utf-8")
    out = {}
    used = set()
    for m in TAG_RE.finditer(md):
        dims = {}
        for part in m.group(1).split(" | "):
            key, _, val = part.partition("=")
            dims[key.strip()] = [v.strip() for v in val.split(",") if v.strip()]
        base = slugify(headline_text(m.group(2))) or "item"
        ident, n = base, 2
        while ident in used:
            ident = f"{base}-{n}"
            n += 1
        used.add(ident)
        out[ident] = dims
    return out


def parse_article_sources(md_path=None):
    """{article_id: [primary-source URLs]} — the Source line(s) of each
    article, keyed by the same runtime id parse_article_tags uses. The
    two iterate TAG_RE in the same document order, so the ids line up
    (a length guard fails loudly rather than mis-joining). URLs are
    trailing-slash-normalised. An article with no Source line maps to
    [] — it simply never matches by URL. The feed join matches a feed
    entry's source URL against these."""
    path = Path(md_path) if md_path else REPO / "SYNTHESIZED.md"
    if not path.exists():
        return {}
    md = path.read_text(encoding="utf-8")
    tags = parse_article_tags(md_path)
    out = {}
    for ident, m in zip(tags.keys(), TAG_RE.finditer(md)):
        end = md.find("</details>", m.end())
        block = md[m.end():end] if end != -1 else ""
        urls = re.findall(
            r"^- Source: \[.*?]\((https?://[^)]+)\)", block, re.MULTILINE
        )
        out[ident] = [u.rstrip("/") for u in urls]
    if len(out) != len(tags):
        raise ValueError(
            f"parse_article_sources: {len(out)} blocks vs {len(tags)} "
            "tag lines — the tag-line/details alignment broke"
        )
    return out


def invert_sources(sources):
    """{source URL: [article ids]} — the reverse of
    parse_article_sources, for the feed join (one lookup per entry
    instead of a scan)."""
    out = {}
    for aid, urls in sources.items():
        for u in urls:
            out.setdefault(u, []).append(aid)
    return out


def match_feed_entry(headline, source_url, tags, url_to_ids):
    """Join one "New in the last 7 days" feed entry to its target
    article's tag dict, or None. The headline arrives with the
    YYYY-MM-DD date prefix already stripped by the caller.

    Tiers, first hit wins:
    (1) exact slug of the headline — the entry reuses the headline;
    (2) the entry's source URL appears in exactly one article's Source
        line — or in several whose tag dicts are all identical
        (mirrored pairs, same-source findings — either way the tags
        are the same, so there is nothing to disambiguate);
    (3) slug prefix, either direction, on the shorter string >= 25
        chars — the feed title is often a truncated or extended form
        of the headline (same identical-tags guard as tier 2).
    No fuzzy matching: an entry whose article cannot be identified
    exactly stays unfiltered (visible under any filter) and is
    reported at build time. That is the honest behaviour for
    structural entries (a deadline, a subsection announcement), digests
    covering several articles, table-row additions, and composite
    articles (one bullet of a multi-incident article)."""
    ident = slugify(headline_text(headline)) or "item"
    if ident in tags:
        return tags[ident]
    if source_url:
        cands = url_to_ids.get(source_url, [])
        if cands and all(tags[c] == tags[cands[0]] for c in cands):
            return tags[cands[0]]
    if len(ident) >= 25:
        cands = [aid for aid in tags
                 if min(len(ident), len(aid)) >= 25
                 and (aid.startswith(ident) or ident.startswith(aid))]
        if cands and all(tags[c] == tags[cands[0]] for c in cands):
            return tags[cands[0]]
    return None


def count_tag_lines(md_path=None):
    """Raw tag-line count, for the malformed-tag-line check in validate()."""
    path = Path(md_path) if md_path else REPO / "SYNTHESIZED.md"
    if not path.exists():
        return 0
    return len(TAG_LINE_RE.findall(path.read_text(encoding="utf-8")))


# --- History join -----------------------------------------------------------
# dashboard-history.json: {series_key: {label, unit, points: [{date,
# display, label, value}]}} — append-only, oldest first. A sparkline
# figure joins by its "history_key". Dates are YYYY-MM-DD, or YYYY-MM
# when only the month is known (the 1st of the month for placement).

def load_history(path=None):
    p = Path(path) if path else REPO / "dashboard-history.json"
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def parse_series_date(s):
    """YYYY-MM-DD or YYYY-MM -> date (month precision = the 1st)."""
    if re.fullmatch(r"\d{4}-\d{2}", s):
        return date.fromisoformat(s + "-01")
    return date.fromisoformat(s)


def build_context():
    """Everything render_embedded/validate need beyond dashboard.json."""
    return {
        "tags": parse_article_tags(),
        "history": load_history(),
    }


# --- Figure iteration -------------------------------------------------------

def iter_panel_figures(panel):
    """Every figure-like dict in a panel, in render order — including the
    stacked block and the bignote block, which are figures in themselves.
    """
    for b in panel["blocks"]:
        kind = b["kind"]
        if kind == "ledger":
            yield from b["left"]["items"]
            yield from b["right"]["items"]
        elif kind in ("bars", "stats", "notes"):
            yield from b["items"]
        elif kind in ("stacked", "bignote"):
            yield b
        else:
            raise ValueError(f"unknown block kind: {kind}")


def iter_figures(data):
    """Every figure-like dict in the file, for validation and counting."""
    for p in data["panels"]:
        yield from iter_panel_figures(p)


def assign_tile_ids(data):
    """Deterministic tile ids: tile-<panel-id>-<slug-of-label>, deduped.

    The panel prefix guarantees uniqueness across panels (several tiles
    link to the same article); the -2/-3 suffixes cover duplicate labels
    within a panel. Returns {id(figure): tile_id} — render and validate
    share this one implementation, so they can never disagree.
    """
    used = set()
    out = {}
    for p in data["panels"]:
        for f in iter_panel_figures(p):
            label = f.get("label") or f.get("text") or f.get("title", "")
            base = f"tile-{p['id']}-{slugify(label) or 'item'}"
            ident, n = base, 2
            while ident in used:
                ident = f"{base}-{n}"
                n += 1
            used.add(ident)
            out[id(f)] = ident
    return out


# --- Shared tile pieces -----------------------------------------------------

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


# Sentiment is a background TINT on the tile (Round 4 — Yorgo's ruling
# reverses the tile spec §5.2 rejection of tints). The class carries the
# colour; the visually-hidden span carries the word for screen readers
# (the tint must not be colour-only). Countdown tiles get no tint class
# and no span — a deadline has no sentiment.
SENTIMENT_WORD = {"positive": "Positive finding",
                  "negative": "Negative finding",
                  "neutral": "Neutral finding"}


def sentiment_span(sentiment):
    """The sentiment word, visually hidden, as the tile's first child."""
    return f'<span class="visually-hidden">{SENTIMENT_WORD[sentiment]}</span>'


def span_class(f, full=False):
    """The tile's unit width (Round 4 §2.1): 1-unit tiles carry no span
    class; 2-unit tiles .tile-span-2; 3-unit tiles .tile-span-3 (always
    1 / -1). The mapping is by tile TYPE, not per-figure data — the
    bignote and the strip's full-width tile span 3 by position (full),
    not by type."""
    if full:
        return " tile-span-3"
    tile = f["tile"]
    if tile in ("note", "sparkline"):
        return " tile-span-2"
    if tile == "pie" and f.get("segments"):
        return " tile-span-2"
    return ""


def tag_attrs(dims, rating_num=None):
    """Filter/sort data-* attributes from one article's parsed tag dict
    ({dimension: [values]}). Shared by tiles (via data_attrs) and by the
    article <details> blocks (build_html.py) — one implementation, so
    the two can never disagree. Multi-value dimensions are
    space-separated tokens, EXCEPT company: company values contain
    spaces ("Black Duck"), so data-company is comma-joined (a comma can
    never appear inside a value — the tag format splits on commas), and
    the filter JS splits company on ",". data-date is the article's
    source-date tag (month precision normalised to the 1st); data-rating
    is numeric, passed in by the caller when the element has a rating.
    """
    parts = []
    for dim in ATTR_DIMS:
        vals = dims.get(dim)
        if not vals:
            continue
        sep = "," if dim == "company" else " "
        parts.append(f'data-{dim}="{esc(sep.join(vals))}"')
    sd = (dims.get("source-date") or [None])[0]
    if sd:
        if re.fullmatch(r"\d{4}-\d{2}", sd):
            sd += "-01"
        parts.append(f'data-date="{esc(sd)}"')
    if rating_num is not None:
        parts.append(f'data-rating="{rating_num}"')
    return " " + " ".join(parts) if parts else ""


def data_attrs(f, tags):
    """Filter/sort data-* attributes for a panel tile, from its article's
    tags (see tag_attrs). A figure with no article tags (the §3.6 prose
    figures) gets no attributes — render_tile marks those tile-untagged,
    which is what exempts them from filtering, not the absence itself.
    """
    link = f.get("link", "")
    if not link.startswith("#"):
        return ""
    t = tags.get(link[1:])
    if not t:
        return ""
    return tag_attrs(t, RATING_NUM[f["rating"]])


def distinct_companies(tags):
    """The Company select's options: distinct company values across all
    tag lines, deduplicated, sorted case-insensitively. A newly tagged
    company appears on the next build automatically — no code change."""
    values = set()
    for dims in tags.values():
        values.update(dims.get("company") or [])
    return sorted(values, key=str.lower)


def _wedge_path(v0, v1, color, opacity=None):
    """SVG wedge path spanning v0%..v1% of the circle (0 = top, clockwise).
    A full 100% span is a circle (a 360-degree arc path does not close).
    """
    if v1 - v0 >= 100:
        op = f' fill-opacity="{opacity}"' if opacity else ""
        return f'<circle cx="50" cy="50" r="40" fill="{color}"{op}/>'
    if v1 <= v0:
        return ""
    a0 = math.radians(v0 / 100 * 360)
    a1 = math.radians(v1 / 100 * 360)
    x0, y0 = 50 + 40 * math.sin(a0), 50 - 40 * math.cos(a0)
    x1, y1 = 50 + 40 * math.sin(a1), 50 - 40 * math.cos(a1)
    large = 1 if (v1 - v0) > 50 else 0
    op = f' fill-opacity="{opacity}"' if opacity else ""
    return (
        f'<path d="M 50,50 L {x0:.1f},{y0:.1f} A 40,40 0 {large} 1 '
        f'{x1:.1f},{y1:.1f} Z" fill="{color}"{op}/>'
    )


def pie_svg(value, split, aria, range_=None, segments=None):
    """Inline SVG pie (72px). Colours follow the split (Yorgo's three
    rules): pie_split names the wedge; the remainder follows by rule.
    Segmented pies ignore split — each segment carries its own tone
    (blue = positive, rust = negative, grey = mixed). The range band
    (low to high) renders in the wedge colour at 40% opacity, compositing
    over the tile tint — so the remainder is a wedge (high to 100%), NOT
    a full circle: drawn over a navy remainder circle the band composited
    to off-palette mauve (#603E53) and the range was almost invisible.
    Wedges are drawn accurately at any value — a 2% wedge is a sliver; the
    number beside the pie carries the finding.
    """
    if segments:
        # Segmented pie: the segments ARE the whole (they sum to 100).
        paths, start = [], 0.0
        for s in segments:
            paths.append(_wedge_path(start, start + s["value"], SEGMENT_TONES[s["tone"]]))
            start += s["value"]
        body = "".join(paths)
    else:
        try:
            wedge_color, rest_color = PIE_SPLITS[split]
        except KeyError:
            raise ValueError(f"unknown pie_split: {split!r}")
        if range_ is not None:
            # Range pie: solid wedge to the low bound, a translucent band
            # from low to high in the same hue, remainder per the split
            # rule. Never a midpoint wedge — a midpoint would present a
            # guess as a measurement. The remainder is a wedge (high to
            # 100%), not a full circle, so the translucent band composites
            # over the tile tint as specified — over a full remainder
            # circle it composited to off-palette mauve.
            body = (
                _wedge_path(range_["high"], 100, rest_color)
                + _wedge_path(range_["low"], range_["high"], wedge_color, opacity="0.4")
                + _wedge_path(0, range_["low"], wedge_color)
            )
        else:
            body = (
                f'<circle cx="50" cy="50" r="40" fill="{rest_color}"/>'
                + _wedge_path(0, value, wedge_color)
            )
    return (
        '<svg class="tile-pie" viewBox="0 0 100 100" role="img" '
        f'aria-label="{esc(aria)}">{body}</svg>'
    )


def question_svg():
    """A question mark inside a circle — the graphic for the no-data tile."""
    return (
        '<svg class="tile-question" viewBox="0 0 100 100" role="img" '
        'aria-label="Unknown — no credible figure exists">'
        f'<circle cx="50" cy="50" r="40" fill="none" stroke="{BLUE}" '
        'stroke-width="6"/>'
        '<text x="50" y="68" text-anchor="middle" '
        'class="tile-question-mark">?</text>'
        "</svg>"
    )


def sparkline_svg(points, aria):
    """Inline SVG sparkline for a time series. X is time-proportional
    (points spaced by date, not evenly — a gap shows as a gap); Y scales
    to the series min/max with 10% headroom. viewBox 300x48 keeps the
    aspect ratio at typical tile widths so the point circles stay round.
    """
    dates = [parse_series_date(p["date"]) for p in points]
    values = [p["value"] for p in points]
    t0, t1 = dates[0].toordinal(), dates[-1].toordinal()
    span = max(t1 - t0, 1)
    lo, hi = min(values), max(values)
    pad = (hi - lo) * 0.1 or 1.0
    lo, hi = lo - pad, hi + pad

    def x(d):
        return 8 + 284 * (d.toordinal() - t0) / span

    def y(v):
        return 42 - 36 * (v - lo) / (hi - lo)

    coords = [(x(d), y(v)) for d, v in zip(dates, values)]
    pts_attr = " ".join(f"{cx:.1f},{cy:.1f}" for cx, cy in coords)
    circles = "".join(
        f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="3" fill="{BLUE}"/>'
        for cx, cy in coords
    )
    series = "; ".join(f"{p['label']} {p['display']}" for p in points)
    return (
        '<svg class="tile-sparkline" viewBox="0 0 300 48" role="img" '
        f'aria-label="{esc(aria)}: {esc(series)}">'
        f'<polyline points="{pts_attr}" fill="none" stroke="{BLUE}" '
        'stroke-width="2"/>'
        f"{circles}</svg>"
    )


def _tone_chip(tone):
    """A tone -> chip colour class. Two naming schemes coexist: ratio
    sides use the bar-era names (gap = rust, navy = blue); pie segments
    use the colour names (rust/blue/grey). Both name the same three chip
    colours; the grey chip reuses the muted class (same hex)."""
    return {"gap": "rust", "navy": "blue",
            "blue": "blue", "rust": "rust", "grey": "muted"}[tone]


# --- Per-type tile bodies ---------------------------------------------------
# Each returns the tile's content ABOVE the source line (graphic row,
# value, label, side rows, legend, caption). The tile shell (sentiment
# tint + visually-hidden word, source line, fig-note) is added by
# render_tile / render_bottom_line.

def render_pie_body(f, legend=False):
    if f.get("segments"):
        svg = pie_svg(None, None, f["title"], segments=f["segments"])
        # Value-first: lead with the primary (first) segment as the
        # stat value, its label + the figure title as the label — the
        # pie and the full legend sit below. Each legend segment is its
        # own block-level row: joined inline with nowrap the three
        # segments formed a ~500px unbreakable run that spilled out of
        # a ~200-330px tile (Round 3 design blocker).
        primary = f["segments"][0]
        leg = "".join(
            f'<span class="tile-legend-row">'
            f'<span class="tile-chip {_tone_chip(s["tone"])}"></span>'
            f"{esc(s['label'])} — {s['value']}%</span>"
            for s in f["segments"]
        )
        return (
            f'<p class="stat-value">{primary["value"]:g}%</p>'
            f'<p class="stat-label">{esc(primary["label"])} — '
            f'{esc(f["title"])}</p>'
            f'<div class="tile-graphic-row">{svg}</div>'
            f'<p class="tile-legend">{leg}</p>'
        )
    rng = f.get("range")
    value = f.get("value")
    if value is None and rng is None:
        value = (f.get("chart") or {}).get("value")  # strip pies
    aria = f'{f["display"]} {f["label"]}'
    svg = pie_svg(value, f.get("pie_split"), aria, range_=rng)
    body = (
        '<div class="tile-graphic-row">'
        f"{svg}"
        f'<p class="stat-value">{esc(f["display"])}</p>'
        "</div>"
        f'<p class="stat-label">{esc(f["label"])}</p>'
    )
    if legend:
        # One block-level row per segment (the same pattern as the
        # segmented-pie legend): an inline run orphaned the second
        # percentage on narrow strip tiles. No separator — rows don't
        # need one. Chip colours derive from pie_split (a-chip = wedge,
        # b-chip = remainder), never hard-coded.
        chart = f["chart"]
        wedge, rest = PIE_SPLITS[f["pie_split"]]
        body += (
            '<p class="tile-legend">'
            '<span class="tile-legend-row">'
            f'<span class="tile-chip {CHIP_CLASS[wedge]}"></span>'
            f'{esc(chart["a_label"])} {chart["value"]}%</span>'
            '<span class="tile-legend-row">'
            f'<span class="tile-chip {CHIP_CLASS[rest]}"></span>'
            f'{esc(chart["b_label"])} {100 - chart["value"]}%</span>'
            "</p>"
        )
    return body


def render_paired_body(f):
    """The paired tile (strip only): two pie figures in one 1-unit card,
    stacked as two rows in figures order (figures[0] first). Each row is
    a self-contained pie figure — small pie + value, label, and its OWN
    legend — so the two pies' colour meanings never merge (identity vs
    positive here). No "vs" connector and no gap marker between the
    rows: the two figures share a population, not a subset relationship
    (the second figure is of ALL banks, not of the first figure's
    subset); order + labels carry the story. A hairline divider
    separates the rows (CSS .tile-paired-row)."""
    rows = []
    for fig in f["figures"]:
        svg = pie_svg(fig["value"], fig["pie_split"],
                      f'{fig["display"]} {fig["label"]}')
        wedge, rest = PIE_SPLITS[fig["pie_split"]]
        rows.append(
            '<div class="tile-paired-row">'
            '<div class="tile-graphic-row">'
            f"{svg}"
            f'<p class="stat-value">{esc(fig["display"])}</p>'
            "</div>"
            f'<p class="stat-label">{esc(fig["label"])}</p>'
            '<p class="tile-legend">'
            '<span class="tile-legend-row">'
            f'<span class="tile-chip {CHIP_CLASS[wedge]}"></span>'
            f'{esc(fig["a_label"])} {fig["value"]}%</span>'
            '<span class="tile-legend-row">'
            f'<span class="tile-chip {CHIP_CLASS[rest]}"></span>'
            f'{esc(fig["b_label"])} {100 - fig["value"]}%</span>'
            "</p>"
            "</div>"
        )
    return "".join(rows)


def _side_rows(chart):
    """The two labelled side rows (chip + label + value), shared by the
    ratio and waffle tiles — both carry the exact side values in text."""
    rows = "".join(
        '<p class="tile-side">'
        f'<span class="tile-chip {_tone_chip(chart[s]["tone"])}"></span>'
        f'{esc(chart[s]["label"])} — {esc(chart[s]["display"])}</p>'
        for s in ("a", "b")
    )
    return f'<div class="tile-sides">{rows}</div>'


def render_ratio_body(f):
    if "before" in f and "after" in f:
        # Before/after variant: both sides are the same model under two
        # conditions, so the side rows carry no colour chips (there is no
        # side to encode); the derived multiple is marked approximate and
        # never replaces the two real values.
        mult = f["after"] / f["before"]
        sides = (
            '<div class="tile-sides">'
            f'<p class="tile-side">{esc(f["before_label"])} — {f["before"]:g}</p>'
            f'<p class="tile-side">{esc(f["after_label"])} — {f["after"]:g}</p>'
            f'<p class="tile-derived">≈{mult:.1f}× the secure output</p>'
            "</div>"
        )
    else:
        sides = _side_rows(f["chart"])
    return (
        f'<p class="stat-value">{esc(f["display"])}</p>'
        f'<p class="stat-label">{esc(f["label"])}</p>'
        f"{sides}"
    )


def waffle_squares(a_value, b_value):
    """The 100-square split for a waffle, computed from the counts at
    build time (never stored — a stored split could drift from the
    counts). Round the SMALLER side to the nearest whole square (halves
    up); the larger side gets the remainder (100 - smaller). Guarantees
    exactly 100 squares; maximum error 0.5 squares. Returns (a, b)
    square counts in chart order."""
    total = a_value + b_value
    if a_value <= b_value:
        a_sq = int(a_value / total * 100 + 0.5)
        return a_sq, 100 - a_sq
    b_sq = int(b_value / total * 100 + 0.5)
    return 100 - b_sq, b_sq


def render_waffle_body(f):
    """The waffle tile (Job B test): a 10x10 grid of 6px squares showing
    the share of two counts of the same thing. The multiple stays the
    headline number — the waffle is a secondary graphic, not the
    finding. Side rows are kept (they carry the exact counts the waffle
    rounds); the caption names the counted set, so the waffle never
    implies a population share the study does not establish. Fill order
    is row-major from top-left, the majority side first, so the minority
    forms the bottom-right corner. Square colours follow the sides'
    tones (AI side rust, human side blue, rule 1).
    """
    chart = f["chart"]
    a_sq, b_sq = waffle_squares(chart["a"]["value"], chart["b"]["value"])
    if a_sq >= b_sq:
        runs = [(a_sq, _tone_chip(chart["a"]["tone"])),
                (b_sq, _tone_chip(chart["b"]["tone"]))]
    else:
        runs = [(b_sq, _tone_chip(chart["b"]["tone"])),
                (a_sq, _tone_chip(chart["a"]["tone"]))]
    squares = "".join(
        f'<span class="waffle-sq {cls}" aria-hidden="true"></span>' * n
        for n, cls in runs
    )
    return (
        '<div class="tile-graphic-row">'
        '<div class="tile-waffle" role="img" '
        f'aria-label="{esc(f["aria_label"])}">'
        f'<div class="tile-waffle-grid">{squares}</div></div>'
        f'<p class="stat-value">{esc(f["display"])}</p>'
        "</div>"
        f'<p class="stat-label">{esc(f["label"])}</p>'
        f'<p class="waffle-caption">{esc(f["caption"])}</p>'
        f"{_side_rows(chart)}"
    )


def render_big_number_body(f):
    return (
        f'<p class="stat-value">{esc(f["display"])}</p>'
        f'<p class="stat-label">{esc(f["label"])}</p>'
    )


def render_no_data_body(f):
    return (
        '<div class="tile-graphic-row">'
        f"{question_svg()}"
        f'<p class="stat-value">{esc(f["display"])}</p>'
        "</div>"
        f'<p class="stat-label">{esc(f["label"])}</p>'
    )


def _short_series_label(label):
    """The caption's short date form for a history point label:
    the first token, with month names abbreviated to three letters
    ("Spring 2026" -> "Spring", "July 2026" -> "Jul")."""
    token = label.split()[0]
    months = {"January": "Jan", "February": "Feb", "March": "Mar",
              "April": "Apr", "May": "May", "June": "Jun", "July": "Jul",
              "August": "Aug", "September": "Sep", "October": "Oct",
              "November": "Nov", "December": "Dec"}
    return months.get(token, token)


def _series_year(label):
    """The 4-digit year in a history point label, or None ("Oct 2024" ->
    "2024", "2026" -> "2026", "Fall" -> None)."""
    m = re.search(r"\b\d{4}\b", label)
    return m.group(0) if m else None


def render_sparkline_body(f, history):
    series = history[f["history_key"]]
    pts = series["points"]
    # The caption lists EVERY history point, in order — first->last
    # paired non-consecutive snapshots and omitted the plotted middle
    # point (Round 3 engagement F5). The aria-label (sparkline_svg)
    # already lists all points with full labels; it stays as-is.
    # A repeated short label ("Apr" twice in the Google series) is
    # ambiguous in the caption — those points keep their full label.
    # Year rule (Round 5 F1+N1): a yearless short label sitting one line
    # above a fig-note carrying a different year can invert the trend if
    # misread ("Oct" over "Oct 2026"). A series spanning more than one
    # year keeps the FULL label on every point; a single-year series
    # carries the year once as a "YYYY: " prefix. A series with no year
    # in any label keeps the short labels, prefix-free.
    shorts = [_short_series_label(p["label"]) for p in pts]
    labels = [p["label"] if shorts.count(s) > 1 else s
              for p, s in zip(pts, shorts)]
    years = {_series_year(p["label"]) for p in pts} - {None}
    if len(years) > 1:
        labels = [p["label"] for p in pts]
        prefix = ""
    elif len(years) == 1:
        prefix = next(iter(years)) + ": "
    else:
        prefix = ""
    caption = prefix + " → ".join(
        f"{lab} {p['display']}" for lab, p in zip(labels, pts)
    )
    return (
        f'<p class="stat-value">{esc(f["display"])}</p>'
        f'<p class="stat-label">{esc(f["label"])}</p>'
        f"{sparkline_svg(pts, f['display'] + ' ' + f['label'])}"
        f'<p class="tile-caption">{esc(caption)}</p>'
    )


def render_flag_body(f):
    dot = "filled" if f["flag"] else ""
    return (
        '<div class="tile-graphic-row">'
        f'<span class="tile-flag-dot {dot}"></span>'
        f'<p class="stat-value">{esc(f["display"])}</p>'
        "</div>"
        f'<p class="stat-label">{esc(f["label"])}</p>'
    )


def render_note_body(f):
    return f'<p class="tile-text">{esc(f["text"])}</p>'


def tile_body(f, history):
    """Dispatch on tile type. Unknown types fail loudly — a tile that
    renders as nothing would silently drop a figure."""
    tile = f["tile"]
    if tile == "pie":
        return render_pie_body(f)
    if tile == "paired":
        return render_paired_body(f)
    if tile == "ratio":
        return render_ratio_body(f)
    if tile == "waffle":
        return render_waffle_body(f)
    if tile == "big-number":
        return render_big_number_body(f)
    if tile == "no-data":
        return render_no_data_body(f)
    if tile == "sparkline":
        return render_sparkline_body(f, history)
    if tile == "flag":
        return render_flag_body(f)
    if tile == "note":
        return render_note_body(f)
    raise ValueError(f"unknown tile type: {tile}")


# --- Tile shell, panels, strips ----------------------------------------------

def render_tile(f, panel_id, ctx, tile_ids):
    """One panel tile: the shared shell (sentiment tint + visually-hidden
    sentiment word, body, source line, fig-note). The share button is
    appended at runtime by the share JS (build_html.py) — top-right,
    absolute; the tile's 32px top padding clears it (the old badge row's
    job). A figure with no article tags (§3.6 prose figures) gets the
    tile-untagged class — the filter JS never hides it and no sort moves
    it (it cannot be tagged, so the retired untagged-visible rule's
    replacement does not apply to it).
    """
    tid = tile_ids[id(f)]
    attrs = data_attrs(f, ctx["tags"])
    untagged = " tile-untagged" if not attrs else ""
    note = f'<p class="fig-note">{esc(f["note"])}</p>' if f.get("note") else ""
    return (
        f'<div class="tile tile-{f["tile"]}{span_class(f)} '
        f'tile-sentiment-{f["sentiment"]}{untagged}" id="{tid}" '
        f'data-sentiment="{f["sentiment"]}"{attrs}>'
        f'{sentiment_span(f["sentiment"])}'
        f"{tile_body(f, ctx['history'])}"
        f"{source_html(f)}{note}"
        "</div>"
    )


def render_bignote_tile(b, panel_id, ctx, tile_ids):
    """The money panel's framing note: a full-width (3-unit) note tile
    with no source line (it has no source or rating — it is a panel-level
    framing statement). Still tinted, still shareable; tile-untagged like
    the §3.6 figures — it is never hidden by a filter and no sort moves
    it from the top of its panel.
    """
    tid = tile_ids[id(b)]
    return (
        f'<div class="tile tile-note tile-span-3 '
        f'tile-sentiment-{b["sentiment"]} tile-untagged" id="{tid}" '
        f'data-sentiment="{b["sentiment"]}">'
        f'{sentiment_span(b["sentiment"])}'
        f'<p class="tile-text">{esc(b["text"])}</p>'
        "</div>"
    )


def render_panel(p, ctx, tile_ids):
    """One panel: a single tile grid holding every block's tiles in
    editorial order, with block labels as full-width grid rows. One grid
    (not one per block) so the sort control can reorder within the panel;
    the ledger's two groups are labelled rows in the same grid, stacked
    vertically. The panel footnote sits below the grid.
    """
    kids = []
    footnote = ""
    for b in p["blocks"]:
        kind = b["kind"]
        if kind in ("bars", "stats", "notes"):
            if b.get("label"):
                kids.append(f'<p class="block-label">{esc(b["label"])}</p>')
            kids.extend(render_tile(f, p["id"], ctx, tile_ids) for f in b["items"])
        elif kind == "stacked":
            kids.append(render_tile(b, p["id"], ctx, tile_ids))
        elif kind == "bignote":
            kids.append(render_bignote_tile(b, p["id"], ctx, tile_ids))
        elif kind == "ledger":
            for side in ("left", "right"):
                kids.append(f'<p class="block-label">{esc(b[side]["title"])}</p>')
                kids.extend(
                    render_tile(f, p["id"], ctx, tile_ids)
                    for f in b[side]["items"]
                )
            if b.get("footnote"):
                footnote = f'<p class="ledger-foot">{esc(b["footnote"])}</p>'
        else:
            raise ValueError(f"unknown block kind: {kind}")
    grid = '<div class="tile-grid">' + "".join(kids) + "</div>"
    return (
        f'<h3 id="{esc(p["id"])}" class="dash-panel">{esc(p["title"])}</h3>'
        f'<p class="panel-lede">{esc(p["lede"])}</p>'
        f"{grid}{footnote}"
    )


def render_bottom_line(items, history):
    """The bottom-line strip (2026-11-15): seven at-a-glance tiles above
    the countdown — the WHOLE card is one link to its evidencing article
    (like the countdown cards; the source name is plain text, not a nested
    link), so the number, the chart, and the description all take the
    reader to the article. Layout is 3+3+1: six 1-unit tiles in two rows of
    three, then the profitability item full-width (3-unit by the strip
    rule — it has no figure, its display IS the finding, "Insufficient
    data", with no rating or date, linking to the money panel; its graphic
    is a question mark in a circle). The tint class sits on the tile div
    (outside the link); the visually-hidden sentiment span is the tile's
    first child, before the link. The share button stays a sibling of the
    link, as everywhere. The strip is never filtered.
    """
    cards = []
    for it in items:
        if it["tile"] == "pie":
            body = render_pie_body(it, legend=True)
        else:
            body = tile_body(it, history)
        parts = [esc(it["source"])]
        if it.get("source_note"):
            parts.append(esc(it["source_note"]))
        if it.get("date"):
            parts.append(esc(it["date"]))
        if it.get("rating"):
            parts.append(rating_html(it["rating"]))
        note = f'<p class="fig-note">{esc(it["note"])}</p>' if it.get("note") else ""
        cls = (f'tile tile-{it["tile"]}{span_class(it, full=bool(it.get("full")))} '
               f'tile-sentiment-{it["sentiment"]}')
        cards.append(
            f'<div class="{cls}" data-sentiment="{it["sentiment"]}">'
            f'{sentiment_span(it["sentiment"])}'
            f'<a href="{esc(it["link"])}">'
            f"{body}"
            '<p class="fig-source">' + " · ".join(parts) + "</p>"
            f"{note}</a></div>"
        )
    return (
        '<p class="dash-strip-label">The bottom line</p>'
        '<div class="bottom-line-strip">' + "".join(cards) + "</div>"
    )


def render_countdown(deadlines):
    """The countdown strip: four tiles of the shared shell — same card,
    same padding, same radius, share button top-right (existing
    cd-<slug> ids, assigned by the share JS). No sentiment tint and no
    visually-hidden sentiment span (a deadline has no sentiment — the
    tile stays on paper) and no rating (a deadline has no confidence
    rating — it is a calendar fact). Left border kept: 3px navy, shared
    with note tiles as the "prose/calendar card, not a stat" marker. The
    countdown is never filtered.
    """
    cards = "".join(
        '<div class="tile cd-card"><a href="#what-were-watching">'
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


def render_filter_bar(total_figures, total_articles, tags):
    """The filter/sort controls, inside the Search/Filter/Sort panel at
    the top of the page (build_html.py owns the panel wrapper; this
    function renders the controls that live inside it, below the search
    box). One set of controls filters the WHOLE page — dashboard tiles
    AND report articles (FILTER_JS); the strips never filter. Native
    <select> elements (accessible, OS picker on a phone): the top line
    is Industry, Severity, P&L impact, Horizon, Technical level + the
    sort select + the asc/desc toggle; a "More filters" <details>
    reveals Section/subject, Type (a checkbox fieldset — OR within the
    dimension, none checked = all), Confidence, Jurisdiction, Company
    (a select built from the distinct company values in the tag data).
    Clear-all sits BELOW More filters, at the bottom of the filter
    block; it resets the sort to Panel order AND collapses More filters.
    The result count is ALWAYS visible — "Showing X of <total_figures>
    figures · Y of <total_articles> articles" on fresh load and after
    clearing, not only while a filter is active.
    """
    def select(dim, label, options):
        opts = ['<option value="">All</option>'] + [
            f'<option value="{esc(v)}">{esc(text)}</option>'
            for v, text in options
        ]
        return (
            f'<label class="dash-filter">{esc(label)} '
            f'<select data-filter="{dim}">' + "".join(opts) + "</select></label>"
        )

    def control(dim, label, options, kind):
        if kind == "checkbox":
            boxes = "".join(
                f'<label><input type="checkbox" data-filter="{dim}" '
                f'value="{esc(v)}"> {esc(text)}</label>'
                for v, text in options
            )
            return (
                f'<fieldset class="dash-type"><legend>{esc(label)}</legend>'
                f'<div class="dash-type-grid">{boxes}</div></fieldset>'
            )
        if kind == "company":
            options = [(c, c) for c in distinct_companies(tags)]
            return select(dim, label, options)
        return select(dim, label, options)

    top = "".join(control(*d) for d in TOP_LINE_DIMS)
    more = "".join(control(*d) for d in MORE_DIMS)
    sort_opts = "".join(
        f'<option value="{esc(v)}">{esc(text)}</option>'
        for v, text in SORT_KEYS
    )
    sort = (
        '<label class="dash-filter dash-sort">Sort '
        f'<select id="dash-sort">{sort_opts}</select></label>'
        '<button type="button" id="dash-sort-dir" class="dash-sort-dir" '
        'aria-label="Toggle sort direction" disabled aria-disabled="true">'
        '<span class="sort-dir-label">Descending</span>'
        '<span class="sort-tri" aria-hidden="true"></span></button>'
    )
    return (
        '<div class="dash-filters" id="dash-filters">'
        f'<div class="dash-filter-row">{top}{sort}</div>'
        '<details class="dash-more-filters"><summary>More filters</summary>'
        f'<div class="dash-filter-row">{more}</div></details>'
        '<div class="dash-clear-row"><button type="button" class="dash-clear-btn" '
        'data-clear-filters>Clear all filters</button></div>'
        f'<p class="dash-count" id="dash-count">Showing {total_figures} of '
        f'{total_figures} figures · {total_articles} of {total_articles} '
        "articles</p>"
        "</div>"
    )


def render_embedded(data, ctx=None):
    """The dashboard section's inner HTML, for embedding in index.html.

    Panels render as H3s under the section's H2 ("Executive dashboard").
    The as-of line is a small muted line, not a second banner — the
    page's own As-of banner (row 1) is the page-level date.
    """
    if ctx is None:
        ctx = build_context()
    tile_ids = assign_tile_ids(data)
    # The filter/sort controls live in the Search/Filter/Sort panel at
    # the top of the page (build_html.py renders the panel and calls
    # render_filter_bar for the controls inside it) — NOT here. The
    # dashboard empty state stays here: it replaces the panels when
    # every panel is empty, so it sits directly above them (hidden
    # until then). The report has its own empty state, in build_html.py.
    parts = [
        f'<p class="dash-asof">Dashboard figures as of {esc(data["as_of_label"])}</p>',
        f'<p class="dash-intro">{esc(data["note"])}</p>',
        f'<p class="dash-intro">{esc(data["tint_note"])}</p>',
        render_bottom_line(data["bottom_line"], ctx["history"]),
        render_countdown(data["deadlines"]),
        '<p class="dash-empty" id="dash-empty" hidden>'
        "No figures match these filters. "
        '<button type="button" class="dash-clear-btn" '
        "data-clear-filters>Clear all filters</button></p>",
    ]
    parts += [render_panel(p, ctx, tile_ids) for p in data["panels"]]
    return "".join(parts)


# --- Validation ---------------------------------------------------------------

def _check_tile_fields(f, src, errors, history):
    """Per-type field checks for one figure (panel or strip)."""
    tile = f.get("tile")
    if tile not in TILE_TYPES:
        errors.append(f"{src}: bad tile type {tile!r}")
        return
    if "ai_side" in f:
        # Retired by Job A: the boolean cannot express rules 2 and 3.
        # A half-migrated figure fails loudly instead of rendering
        # half the pies under the old rule.
        errors.append(f"{src}: ai_side is retired — use pie_split")
    sentiment = f.get("sentiment")
    if sentiment not in SENTIMENTS:
        errors.append(f"{src}: bad sentiment {sentiment!r}")
    if tile == "no-data" and sentiment != "neutral":
        errors.append(f"{src}: no-data tile must be neutral, got {sentiment!r}")
    if tile == "pie":
        has_value = isinstance(f.get("value"), (int, float))
        has_range = isinstance(f.get("range"), dict)
        has_segments = isinstance(f.get("segments"), list)
        chart_value = isinstance((f.get("chart") or {}).get("value"), (int, float))
        n_forms = sum([has_value or chart_value, has_range, has_segments])
        if n_forms != 1:
            errors.append(
                f"{src}: pie needs exactly one of value/range/segments "
                f"(got value={has_value or chart_value}, range={has_range}, "
                f"segments={has_segments})"
            )
        elif has_value or chart_value:
            v = f["value"] if has_value else f["chart"]["value"]
            if not 0 <= v <= 100:
                errors.append(f"{src}: bad pie value {v!r}")
        elif has_range:
            rng = f["range"]
            lo, hi = rng.get("low"), rng.get("high")
            if not (isinstance(lo, (int, float)) and isinstance(hi, (int, float))):
                errors.append(f"{src}: bad range {rng!r}")
            elif not (0 <= lo < hi <= 100):
                errors.append(f"{src}: bad range {rng!r} (need 0 <= low < high <= 100)")
        else:
            total = sum(s["value"] for s in f["segments"])
            if not 99.5 <= total <= 100.5:
                errors.append(f"{src}: pie segments sum to {total}")
            for s in f["segments"]:
                if s.get("tone") not in ("blue", "rust", "grey"):
                    errors.append(f"{src}: bad segment tone {s.get('tone')!r}")
                if not isinstance(s.get("value"), (int, float)):
                    errors.append(f"{src}: bad segment value {s.get('value')!r}")
        if has_segments:
            # The segmented figure carries per-segment tones, not a split.
            if "pie_split" in f:
                errors.append(f"{src}: segmented pie takes per-segment tones, not pie_split")
        elif f.get("pie_split") not in PIE_SPLITS:
            errors.append(
                f"{src}: pie needs pie_split, one of {sorted(PIE_SPLITS)}"
            )
    elif tile == "paired":
        # Two pie figures in one card: each figure is a complete pie
        # (value + split + legend labels). The tile's own display/label
        # mirror figures[0] so the strip's generic display/label checks
        # keep working on the lead figure; the mirror is enforced here —
        # a drift between the tile fields and figures[0] fails loudly
        # instead of rendering one figure and validating another.
        figs = f.get("figures")
        if not isinstance(figs, list) or len(figs) != 2:
            errors.append(f"{src}: paired needs a figures list of exactly 2")
        else:
            for i, fig in enumerate(figs):
                for field in ("display", "label", "a_label", "b_label"):
                    if field not in fig:
                        errors.append(f"{src}: paired figure {i} missing {field}")
                v = fig.get("value")
                if not isinstance(v, (int, float)) or isinstance(v, bool) \
                        or not 0 <= v <= 100:
                    errors.append(f"{src}: paired figure {i} bad value {v!r}")
                if fig.get("pie_split") not in PIE_SPLITS:
                    errors.append(
                        f"{src}: paired figure {i} needs pie_split, one of "
                        f"{sorted(PIE_SPLITS)}"
                    )
            if f.get("display") != figs[0].get("display") or \
                    f.get("label") != figs[0].get("label"):
                errors.append(
                    f"{src}: paired display/label must mirror figures[0]"
                )
    elif tile == "ratio":
        has_chart = isinstance(f.get("chart"), dict) and f["chart"].get("kind") == "compare"
        has_ba = "before" in f and "after" in f
        if has_chart == has_ba:
            errors.append(
                f"{src}: ratio needs exactly one of a compare chart or "
                "before/after"
            )
        elif has_chart:
            for side in ("a", "b"):
                s = f["chart"].get(side) or {}
                for field in ("label", "value", "display", "tone"):
                    if field not in s:
                        errors.append(f"{src}: ratio {side} missing {field}")
                v = s.get("value")
                if not isinstance(v, (int, float)) or v <= 0:
                    errors.append(f"{src}: ratio {side} bad value {v!r}")
                if s.get("tone") not in ("navy", "gap"):
                    errors.append(f"{src}: ratio {side} bad tone {s.get('tone')!r}")
        else:
            for field in ("before", "after"):
                if not isinstance(f.get(field), (int, float)):
                    errors.append(f"{src}: ratio {field} must be a number")
            if isinstance(f.get("before"), (int, float)) and f["before"] == 0:
                errors.append(f"{src}: ratio before must not be 0")
            for field in ("before_label", "after_label"):
                if field not in f:
                    errors.append(f"{src}: ratio missing {field}")
    elif tile == "waffle":
        # A waffle is a share of a whole drawn as 100 squares: both sides
        # must be counts of the same thing (integers, not multipliers or
        # rates), and the minority must clear the 2% resolution floor
        # (below that it reads as a solid block). "Same thing" is an
        # editorial judgment — the check enforces the countable form;
        # the editor confirms the two counts compose one counted set.
        chart = f.get("chart") or {}
        if chart.get("kind") != "compare":
            errors.append(f"{src}: waffle needs a compare chart (two count sides)")
        else:
            vals = []
            for side in ("a", "b"):
                s = chart.get(side) or {}
                v = s.get("value")
                if not isinstance(v, int) or isinstance(v, bool) or v <= 0:
                    errors.append(
                        f"{src}: waffle {side} must be a positive integer "
                        f"count, got {v!r}"
                    )
                else:
                    vals.append(v)
                if s.get("tone") not in ("navy", "gap"):
                    errors.append(f"{src}: waffle {side} bad tone {s.get('tone')!r}")
            if len(vals) == 2:
                minority = min(vals) / sum(vals)
                if minority < 0.02:
                    errors.append(
                        f"{src}: waffle minority share {minority:.1%} is below "
                        "the 2% floor — stays a ratio tile"
                    )
        if not f.get("caption"):
            errors.append(f"{src}: waffle needs a caption naming the counted set")
        if not f.get("aria_label"):
            errors.append(
                f"{src}: waffle needs an aria_label stating the exact share "
                "and the rounding"
            )
    elif tile == "sparkline":
        key = f.get("history_key")
        if not key:
            errors.append(f"{src}: sparkline needs a history_key")
        elif key not in history:
            errors.append(f"{src}: history_key {key!r} not in dashboard-history.json")
        else:
            pts = history[key].get("points") or []
            if len(pts) < 2:
                errors.append(f"{src}: series {key!r} has fewer than 2 points")
            if pts and pts[-1].get("display") != f.get("display"):
                errors.append(
                    f"{src}: figure display {f.get('display')!r} != last history "
                    f"point {pts[-1].get('display')!r} — tile and log have drifted"
                )
    elif tile == "flag":
        if not isinstance(f.get("flag"), bool):
            errors.append(f"{src}: flag tile needs a boolean 'flag'")
    elif tile == "note":
        if "text" not in f:
            errors.append(f"{src}: note tile needs text")


def _check_history(history, errors):
    """Every series in the log is well-formed: 2+ points, ascending
    dates, numeric values, display + label on every point."""
    for key, series in history.items():
        pts = series.get("points")
        if not isinstance(pts, list) or len(pts) < 2:
            errors.append(f"history {key!r}: needs 2+ points")
            continue
        prev = None
        for i, p in enumerate(pts):
            try:
                d = parse_series_date(p["date"])
            except (KeyError, ValueError):
                errors.append(f"history {key!r} point {i}: bad date {p.get('date')!r}")
                continue
            if prev is not None and d <= prev:
                errors.append(f"history {key!r}: points not in ascending date order")
            prev = d
            if not isinstance(p.get("value"), (int, float)):
                errors.append(f"history {key!r} point {i}: bad value {p.get('value')!r}")
            if "display" not in p or "label" not in p:
                errors.append(f"history {key!r} point {i}: needs display + label")


def validate(data, index_html, ctx=None):
    errors = []
    if ctx is None:
        ctx = build_context()
    tags = ctx["tags"]
    history = ctx["history"]
    anchors = set(re.findall(r'id="([^"]+)"', index_html))
    # Article ids are assigned at runtime by the share JS, so they are
    # not in the static HTML — accept the ids the page will assign.
    article_ids = compute_article_ids(index_html)
    anchors |= set(article_ids)

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

    def check_tags(src, link, rating):
        """A figure evidencing an article joins to that article's tags;
        the figure's rating must match the article's confidence tag.
        Section anchors (§3.6 prose, #money) have no tags by design.
        """
        if not link.startswith("#"):
            return
        slug = link[1:]
        if slug not in article_ids:
            return
        t = tags.get(slug)
        if not t:
            errors.append(f"{src}: evidencing article #{slug} has no tag line")
            return
        conf = (t.get("confidence") or [None])[0]
        if rating is not None and conf is not None and rating != conf:
            errors.append(
                f"{src}: rating {rating!r} != article confidence tag {conf!r}"
            )

    # Tag-line integrity: every parsed tag line matches an article, and
    # no tag line failed to parse (a malformed line would silently drop
    # an article's tags).
    if not (REPO / "SYNTHESIZED.md").exists():
        errors.append("SYNTHESIZED.md not found — cannot join article tags")
    else:
        if count_tag_lines() != len(tags):
            errors.append(
                f"tag lines: {count_tag_lines()} in SYNTHESIZED.md but "
                f"{len(tags)} parsed — a malformed tag line is dropping tags"
            )
        for slug in tags:
            if slug not in article_ids:
                errors.append(f"tag line for #{slug} matches no article")

    _check_history(history, errors)

    for f in iter_figures(data):
        src = f.get("source", f.get("title", f.get("text", "?")[:40]))
        if f.get("kind") == "bignote":
            # The money framing note: no source/rating/date/link by
            # design — only tile/sentiment/text apply.
            _check_tile_fields(f, "money bignote", errors, history)
            continue
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
        _check_tile_fields(f, src, errors, history)
        check_tags(src, f.get("link", ""), f.get("rating"))
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
        _check_tile_fields(it, f"bottom line {src}", errors, history)
        check_tags(src, it.get("link", ""), it.get("rating"))
    # Tile ids must be unique (a duplicate id would break share links).
    tile_ids = assign_tile_ids(data)
    if len(set(tile_ids.values())) != len(tile_ids):
        seen = {}
        for tid in tile_ids.values():
            seen[tid] = seen.get(tid, 0) + 1
        dupes = sorted(t for t, n in seen.items() if n > 1)
        errors.append(f"duplicate tile ids: {dupes}")
    if "what-were-watching" not in anchors:
        errors.append("countdown link target #what-were-watching missing")
    return errors


DASH_CSS = """
  /* Executive dashboard (F-01): tile system, same palette. */
  .dash-asof { font-size: 13px; color: var(--muted); margin: 0 0 8px; }
  .dash-intro { color: var(--muted); font-size: 15px; margin: 0 0 16px; }
  .dash-strip-label { font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 0 0 10px; font-weight: 600; }
  /* Search / Filter / Sort panel: one collapsible <details> at the top
     of the page (index only), in the spot where the search box sat.
     The collapsed header is a full-width navy bar — REALLY OBVIOUS,
     chrome, not content. The chevron is a CSS border triangle (no font
     glyph); the native details marker and the generic summary chevron
     are both suppressed here. No overflow: hidden anywhere — the search
     results dropdown must not clip. */
  .search-filter-panel { margin: 0 0 16px; border: none; }
  .sfp-header { background: #283060; color: #fff; font-size: 15px; font-weight: 600; padding: 11px 14px; border-radius: 6px; cursor: pointer; display: flex; justify-content: space-between; align-items: center; gap: 12px; margin: 0; list-style: none; }
  .sfp-header::-webkit-details-marker { display: none; }
  .sfp-header::before { content: none; }
  .sfp-header:hover { background: #283060; }
  .sfp-header:focus-visible { outline: 2px solid #b3543f; outline-offset: 2px; }
  details.search-filter-panel[open] > .sfp-header { border-radius: 6px 6px 0 0; border-bottom: none; }
  .sfp-left { display: flex; flex-wrap: wrap; gap: 4px; align-items: baseline; min-width: 0; }
  .sfp-active { font-weight: 400; font-size: 14px; }
  .sfp-active:empty { display: none; }
  .sfp-chevron { flex-shrink: 0; width: 0; height: 0; border-left: 6px solid transparent; border-right: 6px solid transparent; border-top: 7px solid #fff; transition: transform 0.15s; }
  details.search-filter-panel[open] .sfp-chevron { transform: rotate(180deg); }
  .sfp-body { border: 1px solid var(--line); border-top: none; border-radius: 0 0 6px 6px; background: #fdfbf7; padding: 14px; }
  .sfp-body .search-box { margin: 0 0 14px; }
  .sfp-body .dash-filters { margin: 0; }
  /* Filter / sort controls: native selects, top line + More filters. */
  .dash-filters { margin: 0 0 20px; }
  .dash-filter-row { display: flex; flex-wrap: wrap; gap: 8px 12px; align-items: flex-end; }
  .dash-filter { font-size: 13px; color: var(--muted); display: flex; flex-direction: column; gap: 2px; }
  .dash-filter select { font: inherit; font-size: 14px; color: var(--ink); background: #fdfbf7; border: 1px solid var(--line); border-radius: 4px; padding: 4px 6px; max-width: 100%; }
  .dash-sort { margin-left: auto; }
  .dash-sort-dir { font: inherit; font-size: 13px; color: var(--ink); background: #fdfbf7; border: 1px solid var(--line); border-radius: 4px; padding: 5px 10px; cursor: pointer; display: inline-flex; align-items: center; gap: 6px; }
  .dash-sort-dir:hover { border-color: var(--accent); }
  .dash-sort-dir:disabled { color: var(--muted); cursor: default; opacity: 0.6; }
  .sort-tri { width: 0; height: 0; border-left: 5px solid transparent; border-right: 5px solid transparent; border-top: 6px solid currentColor; }
  .dash-sort-dir.asc .sort-tri { transform: rotate(180deg); }
  .dash-clear-btn { font: inherit; font-size: 13px; color: var(--muted); background: #fdfbf7; border: 1px solid var(--line); border-radius: 4px; padding: 5px 10px; cursor: pointer; }
  .dash-clear-btn:hover { color: var(--accent); border-color: var(--accent); }
  .dash-more-filters { margin: 8px 0 0; }
  .dash-more-filters summary { font-size: 13px; color: var(--muted); cursor: pointer; }
  .dash-more-filters .dash-filter-row { margin-top: 8px; }
  .dash-type { border: 1px solid var(--line); border-radius: 4px; padding: 6px 10px 8px; margin: 0; }
  .dash-type legend { font-size: 13px; color: var(--muted); padding: 0 4px; }
  .dash-type-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2px 16px; }
  .dash-type-grid label { font-size: 14px; color: var(--ink); display: flex; gap: 6px; align-items: baseline; cursor: pointer; white-space: nowrap; }
  .dash-clear-row { margin-top: 12px; }
  .dash-count { font-size: 13px; color: var(--muted); margin: 8px 0 0; }
  .dash-empty { font-size: 15px; color: var(--muted); font-style: italic; margin: 16px 0; }
  .dash-empty .dash-clear-btn { font-style: normal; margin-left: 8px; }
  /* The tile shell: one card for every figure, strip, and deadline.
     Unit sizes (Round 4 §2): the unit is WIDTH in grid columns; height
     is natural, top-aligned (align-items: start — without it the rows
     would still stretch and the unit system would be void). Fixed
     columns — 3 above 1100px, 2 at 601–1100px, 1 at ≤600px (the 1100px
     breakpoint is arithmetic: a 1-unit tile must stay ≥ ~210px for the
     pie row to fit). Dense flow backfills the holes a 2-unit tile
     leaves; the strips keep default flow (their spans cannot hole). */
  .tile-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 0 0 8px; align-items: start; grid-auto-flow: dense; }
  .tile { border: 1px solid var(--line); border-radius: 6px; padding: 32px 14px 12px; background: #fdfbf7; display: flex; flex-direction: column; min-width: 0; }
  .tile-span-2 { grid-column: span 2; }
  .tile-span-3 { grid-column: 1 / -1; }
  /* Sentiment tints (Round 4 §1): pale washes over the card colour —
     light enough not to muddy the warm paper or dull the pies. The
     encodings (saturated rust/navy/grey fills) never share the tints'
     lightness band. Countdown tiles carry no tint class (paper). */
  .tile-sentiment-positive { background-color: #E9EAEF; }
  .tile-sentiment-negative { background-color: #F6EAE5; }
  .tile-sentiment-neutral { background-color: #F0EDE5; }
  .tile-graphic-row { display: flex; align-items: center; gap: 14px; margin: 0 0 8px; }
  .tile-graphic-row .stat-value { margin: 0; }
  /* svg-qualified: .tile-pie / .tile-sparkline are also tile TYPE classes
     on the tile div — the graphic sizing must not apply to the div. */
  svg.tile-pie { width: 72px; height: 72px; flex: 0 0 auto; }
  svg.tile-question { width: 72px; height: 72px; flex: 0 0 auto; }
  .tile-question-mark { font-family: Georgia, 'Times New Roman', Times, serif; font-size: 52px; font-weight: 700; fill: #283060; }
  svg.tile-sparkline { width: 100%; height: auto; display: block; margin: 4px 0 2px; }
  .tile-caption, .waffle-caption { font-size: 12px; color: var(--muted); margin: 0 0 6px; }
  /* Waffle (Job B test): a 10x10 grid of 6px squares, 1px gaps = 69px,
     centred in the 72px graphic slot so waffle tiles align with pies.
     Scoped to the graphic row: .tile-waffle is also the tile TYPE class
     on the tile div — unscoped, this rule constrained the TILE to 72px
     (Round 5 phone review: the Sajadi tile rendered 72px wide, value
     spilling outside the tint). Same guard as the svg-qualified pie /
     sparkline rules above. */
  .tile-graphic-row .tile-waffle { width: 72px; flex: 0 0 auto; }
  .tile-waffle-grid { display: grid; grid-template-columns: repeat(10, 6px); grid-auto-rows: 6px; gap: 1px; width: 69px; height: 69px; margin: 0 auto; }
  .waffle-sq { display: block; width: 6px; height: 6px; }
  .waffle-sq.rust { background: #b3543f; }
  .waffle-sq.blue { background: #283060; }
  .waffle-sq.muted { background: #c9c2b0; }
  /* Paired tile (strip only): two pie figures stacked in one 1-unit
     card. The pies shrink to 48px — two 72px pies + labels would
     overrun the card; the value stays full-size (the number carries
     the finding). Each row carries its own legend — the two pies'
     colour meanings stay separate, never merged. A hairline divider
     marks the rows as two findings, not a comparison: no "vs"
     connector, no gap marker (the second figure is of the same
     population, not a subset of the first). */
  .tile-paired-row svg.tile-pie { width: 48px; height: 48px; }
  .tile-paired-row .tile-graphic-row { margin-bottom: 4px; }
  .tile-paired-row + .tile-paired-row { border-top: 1px solid var(--line); margin-top: 10px; padding-top: 10px; }
  .tile-flag-dot { display: inline-block; width: 14px; height: 14px; border-radius: 50%; border: 2px solid #283060; background: transparent; flex: 0 0 auto; }
  .tile-flag-dot.filled { background: #283060; }
  .tile-text { font-size: 15px; margin: 0 0 6px; }
  .tile-note { border-left: 3px solid var(--logo-navy); }
  .tile-no-data { border: 2px dashed var(--muted); }
  .tile-legend { font-size: 12px; color: var(--muted); margin: 0 0 6px; overflow-wrap: break-word; }
  /* Segmented-pie legend rows are block-level (one segment per line) —
     inline + nowrap joined them into a ~500px unbreakable run that
     spilled out of the tile. The chip reset keeps the 4px .tile-chip
     margin inside legends (the old .tile-legend > span rule overrode
     it with 12px on strip-legend chips). */
  .tile-legend-row { display: block; }
  .tile-legend .tile-chip { margin-right: 4px; }
  .tile-chip { display: inline-block; width: 10px; height: 10px; border-radius: 2px; margin-right: 4px; vertical-align: middle; }
  .tile-chip.rust { background: #b3543f; }
  .tile-chip.blue { background: #283060; }
  .tile-chip.muted { background: #c9c2b0; }
  .tile-sides { margin: 0 0 6px; }
  .tile-side { font-size: 13px; color: var(--muted); margin: 0 0 2px; }
  .tile-derived { font-size: 13px; color: var(--muted); margin: 4px 0 0; font-style: italic; }
  .stat-value { font-family: Georgia, 'Times New Roman', Times, serif; font-size: 30px; font-weight: 700; color: var(--logo-navy); line-height: 1.1; margin: 0 0 4px; overflow-wrap: break-word; }
  .stat-label { font-size: 14px; margin: 0 0 6px; line-height: 1.4; }
  .fig-source { font-size: 13px; color: var(--muted); margin: 0; padding-top: 3px; }
  .fig-source a { color: var(--muted); }
  .fig-note { font-size: 13px; color: var(--muted); margin: 2px 0 0; font-style: italic; }
  .rating { white-space: nowrap; }
  .panel-lede { color: var(--muted); font-size: 15px; margin: -4px 0 16px; }
  .block-label { grid-column: 1 / -1; font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 12px 0 0; font-weight: 600; }
  .tile-grid .block-label:first-child { margin-top: 0; }
  .ledger-foot { margin: 12px 0 0; font-size: 14px; color: var(--muted); font-style: italic; }
  /* The two strips, same shell. Whole-card links stay whole-card links. */
  .bottom-line-strip { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 0 0 20px; align-items: start; }
  .bottom-line-strip .tile a { text-decoration: none; color: inherit; display: flex; flex-direction: column; flex: 1; }
  .countdown-strip { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 0 0 8px; align-items: start; }
  .cd-card { border-left: 3px solid var(--logo-navy); }
  .cd-card a { text-decoration: none; color: inherit; display: flex; flex-direction: column; flex: 1; }
  .cd-card .cd-label { font-size: 13px; color: var(--muted); margin: 0 0 2px; }
  .cd-card .cd-date { font-weight: 700; font-size: 15px; margin: 0; }
  .cd-card .cd-days { font-size: 13px; color: var(--accent); font-weight: 600; margin: 2px 0 0; }
  @media (max-width: 1100px) { .tile-grid { grid-template-columns: repeat(2, 1fr); } .bottom-line-strip { grid-template-columns: repeat(2, 1fr); } .countdown-strip { grid-template-columns: repeat(2, 1fr); } .dash-sort { margin-left: 0; } }
  /* At one column every span becomes full-width — EXPLICITLY. A span 2
     item in a 1-column grid does not clamp: it creates an implicit
     track and the grid overflows. .tile-span-3 is 1 / -1 at all widths
     by definition, so only span-2 needs the collapse. */
  @media (max-width: 600px) { .bottom-line-strip, .countdown-strip, .tile-grid { grid-template-columns: 1fr; } .tile-span-2 { grid-column: 1 / -1; } .dash-type-grid { grid-template-columns: 1fr; } .dash-filter { flex: 1 1 100%; } .dash-filter select { width: 100%; } }
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

FILTER_JS = """
<script>
(function () {
  // Page-level filter/sort (Round 4): ONE set of controls filters the
  // whole page — dashboard tiles AND report articles. Matching is AND
  // across dimensions; within a dimension an element matches if ANY of
  // its values equals ANY selected value (Type is multi-choice, so a
  // dimension can hold several selections). An element with no value
  // for a filtered dimension does NOT match — the interim
  // untagged-visible rule retired with the tag backfill (a Company
  // selection means what it says; an untagged article is not evidence
  // about that company). The ONLY exemption is elements that cannot be
  // tagged: the §3.6 figures and the money bignote carry
  // .tile-untagged and are never hidden (and no sort moves them).
  // Filtered-out tiles/articles are hidden, not greyed out. A panel
  // with zero visible tiles hides entirely; a report subsection hides
  // when all its articles filter out, and a section hides when all its
  // subsections hide (a section with no articles — the front-page
  // sections, prose sections — never hides). The strips never filter.
  // The "New in the last 7 days" feed filters with the report: each
  // entry inherits its target article's tags at build time
  // (build_html.py) and hides when the article filters out. Entries
  // with no identifiable article (a deadline, a subsection
  // announcement, a digest covering several articles) carry no tags
  // and stay visible under any filter; the feed's empty state shows
  // only when NO entry is visible. The count line counts figures and
  // body articles only — the feed is a view onto the same articles,
  // not more of them.
  // Sorting reorders tiles WITHIN each panel only — articles filter
  // but do not sort (sorting them would scramble the report's
  // editorial structure). Block labels hide while a non-default sort
  // is active (they would no longer describe the tiles under them);
  // pinned tiles (the full-width bignote, the untaggable §3.6 figures)
  // keep their editorial positions and the sorted tiles fill the
  // remaining slots. Share links open unfiltered: filter state is
  // per-page-load only, and any in-page jump into the dashboard or the
  // report clears the filters first so the target is always visible
  // (this covers search-result clicks too).
  var bar = document.getElementById('dash-filters');
  if (!bar) return;
  var embed = document.querySelector('.dash-embed');
  if (!embed) return;
  var report = document.querySelector('.report-embed');
  var tiles = Array.prototype.slice.call(embed.querySelectorAll('.tile-grid .tile'));
  var grids = Array.prototype.slice.call(embed.querySelectorAll('.tile-grid'));
  var articles = report
    ? Array.prototype.slice.call(report.querySelectorAll('details[data-subject]'))
    : [];
  var feedList = report ? report.querySelector('.whats-new-feed') : null;
  var feedItems = feedList
    ? Array.prototype.slice.call(feedList.querySelectorAll('li[data-subject]'))
    : [];
  var feedEmptyEl = document.getElementById('feed-empty');
  var countEl = document.getElementById('dash-count');
  var emptyEl = document.getElementById('dash-empty');
  var reportEmptyEl = document.getElementById('report-empty');
  var indicatorEl = document.getElementById('sfp-active');
  var totalFigures = tiles.length;
  var totalArticles = articles.length;
  var selects = Array.prototype.slice.call(bar.querySelectorAll('select[data-filter]'));
  var typeBoxes = Array.prototype.slice.call(bar.querySelectorAll('input[type="checkbox"][data-filter]'));
  var sortSel = document.getElementById('dash-sort');
  var sortDirBtn = document.getElementById('dash-sort-dir');
  var sortDirLabel = sortDirBtn ? sortDirBtn.querySelector('.sort-dir-label') : null;
  // Indicator order: control order, top line first, then More filters.
  var DIM_ORDER = ['industry', 'severity', 'pnl-impact', 'horizon',
                   'register', 'subject', 'type', 'confidence',
                   'jurisdiction', 'company'];
  var DIM_LABEL = {industry: 'Industry', severity: 'Severity',
                   'pnl-impact': 'P&L impact', horizon: 'Horizon',
                   register: 'Technical level', subject: 'Section',
                   type: 'Type', confidence: 'Confidence',
                   jurisdiction: 'Jurisdiction', company: 'Company'};
  // Sort: per-key default direction (the option labels state it), and
  // the rank orders for dimensions with a natural (non-alphabetical)
  // order. Set dimensions sort alphabetically by first value; the
  // register is a depth scale (technical first); horizon is
  // chronological (soonest first); subject is section order with
  // Cross-cutting last (it is the residual bucket).
  var SORT_DEFAULT_DIR = {date: 'desc', confidence: 'desc',
                          severity: 'desc', horizon: 'asc', subject: 'asc',
                          type: 'asc', industry: 'asc', 'pnl-impact': 'asc',
                          register: 'asc', jurisdiction: 'asc',
                          company: 'asc'};
  var ORDER_RANK = {
    severity: {critical: 4, material: 3, directional: 2, background: 1},
    horizon: {immediate: 0, quarter: 1, year: 2, longer: 3},
    subject: {'1': 0, '2': 1, '3': 2, '0': 3},
    register: {technical: 0, mixed: 1, business: 2}
  };
  var sortDir = 'desc';
  // Remember editorial order (per grid child, labels included) so
  // "Panel order" restores the exact original sequence.
  grids.forEach(function (g) {
    Array.prototype.slice.call(g.children).forEach(function (kid, i) { kid._orig = i; });
  });
  function activeFilters() {
    var out = {};
    selects.forEach(function (s) { if (s.value) out[s.getAttribute('data-filter')] = [s.value]; });
    var checked = [];
    typeBoxes.forEach(function (b) { if (b.checked) checked.push(b.value); });
    if (checked.length) out[typeBoxes[0].getAttribute('data-filter')] = checked;
    return out;
  }
  function valuesOf(el, dim) {
    var attr = el.getAttribute('data-' + dim);
    if (!attr) return null;
    // Company values contain spaces ("Black Duck"), so data-company is
    // comma-joined; every other dimension is space-joined tokens.
    return dim === 'company' ? attr.split(',') : attr.split(' ');
  }
  function matches(el, filters) {
    for (var dim in filters) {
      var vals = valuesOf(el, dim);
      if (!vals) return false;
      var want = filters[dim];
      var hit = false;
      for (var i = 0; i < want.length; i++) {
        if (vals.indexOf(want[i]) !== -1) { hit = true; break; }
      }
      if (!hit) return false;
    }
    return true;
  }
  function tileMatches(tile, filters) {
    // Untaggable figures are never hidden by any filter.
    if (tile.classList.contains('tile-untagged')) return true;
    return matches(tile, filters);
  }
  function updateIndicator(filters) {
    if (!indicatorEl) return;
    var names = [];
    DIM_ORDER.forEach(function (dim) { if (filters[dim]) names.push(DIM_LABEL[dim]); });
    if (!names.length) { indicatorEl.textContent = ''; return; }
    var shown = names.slice(0, 3);
    var extra = names.length - shown.length;
    var text = ' \\u00b7 ' + names.length + ' filter' +
      (names.length === 1 ? '' : 's') + ' active: ' + shown.join(', ');
    if (extra) text += ' +' + extra + ' more';
    indicatorEl.textContent = text;
  }
  function updateLabels() {
    // A block label hides when every tile between it and the next label
    // (or the grid end) is hidden, and returns when any reappears. The
    // labels live inside each panel's .tile-grid, so this works with
    // the runtime DOM — the collapse JS wraps the panel content in a
    // .section-body, but the grid and its children are unchanged by it.
    // While a non-default sort is active the labels stay hidden
    // regardless: the sort has reordered the tiles, so a label no
    // longer describes the tiles under it.
    var sorted = sortSel.value !== 'panel';
    grids.forEach(function (g) {
      var kids = Array.prototype.slice.call(g.children);
      kids.forEach(function (kid, i) {
        if (!kid.classList.contains('block-label')) return;
        var anyVisible = false;
        for (var j = i + 1; j < kids.length; j++) {
          if (kids[j].classList.contains('block-label')) break;
          if (kids[j].classList.contains('tile') &&
              kids[j].style.display !== 'none') { anyVisible = true; break; }
        }
        kid.style.display = (anyVisible && !sorted) ? '' : 'none';
      });
    });
  }
  function updateSections() {
    if (!report) return;
    // Every report heading hides with its section-body when the body
    // holds articles and every one is filtered out. A body with no
    // articles (the front-page sections, prose sections) never hides —
    // the unfiltered sections stay visible by construction.
    report.querySelectorAll('h2, h3, h4').forEach(function (h) {
      var body = h.nextElementSibling;
      if (!body || !body.classList.contains('section-body')) return;
      var arts = body.querySelectorAll('details[data-subject]');
      if (!arts.length) return;
      var anyVisible = false;
      arts.forEach(function (a) { if (a.style.display !== 'none') anyVisible = true; });
      h.style.display = anyVisible ? '' : 'none';
      body.style.display = anyVisible ? '' : 'none';
    });
  }
  function applyFilters() {
    var filters = activeFilters();
    var visible = 0;
    tiles.forEach(function (t) {
      var show = tileMatches(t, filters);
      t.style.display = show ? '' : 'none';
      if (show) visible++;
    });
    var anyPanelVisible = false;
    embed.querySelectorAll('h3.dash-panel').forEach(function (h) {
      var body = h.nextElementSibling;
      if (!body || !body.classList.contains('section-body')) return;
      var vis = 0;
      body.querySelectorAll('.tile-grid .tile').forEach(function (t) {
        if (t.style.display !== 'none') vis++;
      });
      h.style.display = vis ? '' : 'none';
      body.style.display = vis ? '' : 'none';
      if (vis) anyPanelVisible = true;
    });
    var visArticles = 0;
    articles.forEach(function (a) {
      var show = matches(a, filters);
      a.style.display = show ? '' : 'none';
      if (show) visArticles++;
    });
    var visFeed = 0;
    feedItems.forEach(function (li) {
      var show = matches(li, filters);
      li.style.display = show ? '' : 'none';
      if (show) visFeed++;
    });
    // The feed's empty state shows only when NO entry is visible:
    // untagged entries are always visible, so while any remain the
    // state never appears — it matters once every entry is tagged and
    // all of them filter out. The check reads the live DOM (tagged
    // and untagged alike) rather than a precomputed count.
    if (feedEmptyEl) {
      var anyFeedVisible = visFeed > 0;
      if (!anyFeedVisible && feedList) {
        anyFeedVisible = Array.prototype.slice.call(feedList.querySelectorAll('li'))
          .some(function (li) { return li.style.display !== 'none'; });
      }
      feedEmptyEl.hidden = anyFeedVisible;
    }
    updateSections();
    if (emptyEl) emptyEl.hidden = anyPanelVisible;
    if (reportEmptyEl) reportEmptyEl.hidden = visArticles > 0;
    // The count is always shown — hiding it when unfiltered meant it
    // vanished after Clear all and never appeared on a fresh load
    // until a filter was applied.
    if (countEl) {
      countEl.hidden = false;
      countEl.textContent = 'Showing ' + visible + ' of ' + totalFigures +
        ' figures \\u00b7 ' + visArticles + ' of ' + totalArticles + ' articles';
    }
    updateLabels();
    updateIndicator(filters);
  }
  function sortValue(tile, key) {
    if (key === 'date') {
      var d = tile.getAttribute('data-date');
      return d ? Date.parse(d) : null;
    }
    if (key === 'confidence') {
      var r = tile.getAttribute('data-rating');
      return r ? +r : null;
    }
    var vals = valuesOf(tile, key);
    if (!vals) return null;
    var first = vals[0];
    if (ORDER_RANK[key]) return ORDER_RANK[key][first];
    return first.toLowerCase();
  }
  function compareTiles(a, b, key) {
    var va = sortValue(a, key), vb = sortValue(b, key);
    if (va === null && vb === null) return a._orig - b._orig;
    if (va === null) return 1;   // a missing key sorts last, either direction
    if (vb === null) return -1;
    var c = (va < vb) ? -1 : (va > vb) ? 1 : 0;
    if (sortDir === 'desc') c = -c;
    return c || (a._orig - b._orig);
  }
  function isPinned(t) {
    // Full-width tiles (the money bignote) and untaggable figures keep
    // their editorial positions under any sort.
    return t.classList.contains('tile-span-3') ||
           t.classList.contains('tile-untagged');
  }
  function applySort() {
    var key = sortSel.value;
    grids.forEach(function (g) {
      var kids = Array.prototype.slice.call(g.children);
      if (key === 'panel') {
        kids.sort(function (a, b) { return a._orig - b._orig; });
        kids.forEach(function (k) { g.appendChild(k); });
        return;
      }
      var sortable = kids.filter(function (k) {
        return k.classList.contains('tile') && !isPinned(k);
      });
      sortable.sort(function (a, b) { return compareTiles(a, b, key); });
      // Pinned tiles and block labels keep their positions; the sorted
      // tiles fill the remaining slots in order.
      var i = 0;
      kids.forEach(function (k) {
        if (k.classList.contains('tile') && !isPinned(k)) g.appendChild(sortable[i++]);
        else g.appendChild(k);
      });
    });
    updateLabels();
  }
  function setSortDir(dir) {
    sortDir = dir;
    if (sortDirLabel) sortDirLabel.textContent = dir === 'desc' ? 'Descending' : 'Ascending';
    if (sortDirBtn) sortDirBtn.classList.toggle('asc', dir === 'asc');
  }
  function syncSortDirState() {
    // Direction is meaningless for editorial order: the toggle is
    // disabled while Panel order is selected.
    if (!sortDirBtn) return;
    var panel = sortSel.value === 'panel';
    sortDirBtn.disabled = panel;
    sortDirBtn.setAttribute('aria-disabled', panel ? 'true' : 'false');
  }
  function clearFilters() {
    // Back to the default state: filters cleared (selects and Type
    // boxes), sort back to Panel order (and the tiles restored to
    // editorial order), More filters collapsed. The count line and the
    // header indicator update via applyFilters.
    selects.forEach(function (s) { s.value = ''; });
    typeBoxes.forEach(function (b) { b.checked = false; });
    sortSel.value = 'panel';
    setSortDir('desc');
    syncSortDirState();
    applySort();
    var more = bar.querySelector('.dash-more-filters');
    if (more) more.open = false;
    applyFilters();
  }
  selects.forEach(function (s) { s.addEventListener('change', applyFilters); });
  typeBoxes.forEach(function (b) { b.addEventListener('change', applyFilters); });
  sortSel.addEventListener('change', function () {
    if (sortSel.value !== 'panel') setSortDir(SORT_DEFAULT_DIR[sortSel.value] || 'asc');
    syncSortDirState();
    applySort();
  });
  if (sortDirBtn) sortDirBtn.addEventListener('click', function () {
    setSortDir(sortDir === 'desc' ? 'asc' : 'desc');
    applySort();
  });
  document.querySelectorAll('[data-clear-filters]').forEach(function (btn) {
    btn.addEventListener('click', clearFilters);
  });
  // Initialise from the DOM: the count reads "Showing 62 of 62 figures
  // · 85 of 85 articles" on fresh load (the server renders the same
  // text; this confirms it against the tiles and articles actually
  // present) and the labels start in their unfiltered state.
  syncSortDirState();
  applyFilters();
  // A shared tile/article link, a search result, or a TOC jump into the
  // dashboard or the report must land on a visible target: clear the
  // filters before the browser follows the anchor (this runs before
  // hashchange).
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href^="#"]') : null;
    if (!a) return;
    var id = a.getAttribute('href').slice(1);
    if (!id) return;
    var target = document.getElementById(id);
    if (target && (embed.contains(target) ||
                   (report && report.contains(target)))) clearFilters();
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
    from collections import Counter
    tiles = Counter(f.get("tile") for f in iter_figures(data))
    tiles.update(it.get("tile") for it in data.get("bottom_line", []))
    print(f"dashboard.json OK ({len(list(iter_figures(data)))} figures, "
          f"{len(data['panels'])} panels, "
          f"{len(data.get('bottom_line', []))} bottom-line items; "
          f"tiles: {', '.join(f'{k} {v}' for k, v in sorted(tiles.items()))})")


if __name__ == "__main__":
    main(sys.argv)
