#!/usr/bin/env python3
"""Regenerate r4b-fixture.json from the built index.html (+ the FILTER_JS
extract's sibling snapshot).

The r4b harness runs the REAL filter script (r4b-filter-js.txt, the
evaluated FILTER_JS) against a fixture parsed from the REAL built page,
with scenario expectations computed INDEPENDENTLY here — replicating
FILTER_JS's matching semantics (matches/tileMatches in
build_dashboard.py), never by running the JS. Regenerate both snapshots
whenever the build or the generator changes (RULES.md §6), then re-run
`node _tools/tests/r4b-test.js` — and update that file's hard-coded
snapshot numbers (totals, Black Duck, pre-click) from the values this
script prints.

Usage: python3 _tools/tests/regen_fixture.py [index.html]
  (default: index.html in the repo root, i.e. the parent of _tools/)
Writes: _tools/tests/r4b-fixture.json
"""

import json
import sys
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

# The scenarios never change (they are the harness's test cases); only
# their EXPECTED counts move with the build.
SCENARIOS = {
    "fresh": {},
    "severity_critical": {"severity": ["critical"]},
    "type_benchmark_study": {"type": ["benchmark", "study"]},
    "company_black_duck": {"company": ["Black Duck"]},
    "company_openai": {"company": ["OpenAI"]},
    "jurisdiction_eu": {"jurisdiction": ["eu"]},
    "jurisdiction_greece": {"jurisdiction": ["greece"]},
    "severity_critical_industry_software": {
        "severity": ["critical"], "industry": ["software"]},
    "five_dims": {
        "industry": ["software"], "severity": ["critical"],
        "pnl-impact": ["risk"], "horizon": ["immediate"],
        "register": ["technical"]},
    "confidence_claimed": {"confidence": ["claimed"]},
}


def data_attrs(attrs):
    """data-* attributes with the prefix stripped (sentiment, subject,
    ..., date, rating) — exactly what the test's DOM shim reads."""
    return {k[5:]: v for k, v in attrs.items() if k.startswith("data-")}


class PageParser(HTMLParser):
    """Panels (h3.dash-panel + following .tile-grid) and the report tree
    (h2/h3/h4 after #report + <details data-subject> articles)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []  # (tag, attrs dict)
        self.panels = []
        self.panel = None
        self.in_report = False
        self.root = {"id": "report-root", "level": 1,
                     "articles": [], "children": []}
        self.heading_stack = [self.root]
        self.label_text = None

    # -- stack helpers -------------------------------------------------
    def _parent(self):
        return self.stack[-1] if self.stack else (None, {})

    def _in_grid(self):
        # Directly inside a .tile-grid (the grid is the parent element).
        tag, attrs = self._parent()
        return tag == "div" and "tile-grid" in attrs.get("class", "").split()

    # -- events --------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "h2" and d.get("id") == "report":
            self.in_report = True
        if tag == "h3" and "dash-panel" in d.get("class", "").split():
            self.panel = {"id": d["id"], "kids": []}
            self.panels.append(self.panel)
        if tag in ("h2", "h3", "h4") and self.in_report \
                and d.get("id") != "report":
            if "dash-panel" not in d.get("class", "").split():
                node = {"id": d["id"], "level": int(tag[1]),
                        "articles": [], "children": []}
                while self.heading_stack[-1]["level"] >= node["level"]:
                    self.heading_stack.pop()
                self.heading_stack[-1]["children"].append(node)
                self.heading_stack.append(node)
        if tag == "p" and self._in_grid() \
                and "block-label" in d.get("class", "").split():
            self.label_text = ""
        if tag == "div" and self._in_grid() \
                and "tile" in d.get("class", "").split():
            self.panel["kids"].append({
                "kind": "tile",
                "id": d.get("id", ""),
                "classes": d.get("class", "").split(),
                "attrs": data_attrs(d),
            })
        if tag == "details" and self.in_report and "data-subject" in d:
            self.heading_stack[-1]["articles"].append(data_attrs(d))
        self.stack.append((tag, d))

    def handle_data(self, data):
        if self.label_text is not None:
            self.label_text += data

    def handle_endtag(self, tag):
        if self.stack and self.stack[-1][0] == tag:
            _, d = self.stack.pop()
            if tag == "p" and self.label_text is not None \
                    and "block-label" in d.get("class", "").split():
                self.panel["kids"].append(
                    {"kind": "label", "text": self.label_text})
                self.label_text = None
        else:
            # Tolerate a stray close (void elements never open).
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break


# --- Independent expectation computation (FILTER_JS semantics) --------
# matches(): AND across dimensions; within a dimension ANY selected
# value must be one of the element's values; a missing attribute does
# NOT match. Company splits on ',' (values contain spaces); every
# other dimension splits on ' '. tileMatches(): tile-untagged tiles
# are never hidden.

def values_of(attrs, dim):
    v = attrs.get(dim)
    if not v:
        return None
    return v.split(",") if dim == "company" else v.split(" ")


def matches(attrs, filters):
    for dim, want in filters.items():
        vals = values_of(attrs, dim)
        if vals is None:
            return False
        if not any(w in vals for w in want):
            return False
    return True


def all_articles(node):
    out = list(node.get("articles", []))
    for c in node.get("children", []):
        out += all_articles(c)
    return out


def compute_expected(panels, report):
    tiles = [k for p in panels for k in p["kids"] if k["kind"] == "tile"]
    articles = all_articles(report)
    expected = {}
    for name, filters in SCENARIOS.items():
        vis_t = sum(
            1 for t in tiles
            if "tile-untagged" in t["classes"] or matches(t["attrs"], filters)
        )
        vis_a = sum(1 for a in articles if matches(a, filters))
        expected[name] = [vis_t, vis_a]
    return expected, len(tiles), len(articles)


def main(argv):
    index_path = Path(argv[1]) if len(argv) > 1 else REPO / "index.html"
    html = index_path.read_text(encoding="utf-8")
    parser = PageParser()
    parser.feed(html)
    expected, n_tiles, n_articles = compute_expected(
        parser.panels, parser.root)
    fixture = {
        "panels": parser.panels,
        "report": parser.root,
        "scenarios": SCENARIOS,
        "expected": expected,
    }
    out = HERE / "r4b-fixture.json"
    out.write_text(json.dumps(fixture, indent=2, ensure_ascii=False),
                   encoding="utf-8")
    untagged = [k["id"] for p in parser.panels for k in p["kids"]
                if k["kind"] == "tile" and "tile-untagged" in k["classes"]]
    print(f"wrote {out} ({n_tiles} tiles, {n_articles} articles, "
          f"{len(untagged)} untagged)")
    print("expected:", json.dumps(expected))
    print("untagged tiles:", untagged)
    print("r4b-test.js snapshot numbers to update:")
    print(f"  totals: {n_tiles} figures, {n_articles} articles")
    print(f"  severity_critical articles: {expected['severity_critical'][1]}")
    print(f"  company_black_duck: {expected['company_black_duck'][0]} figures, "
          f"{expected['company_black_duck'][1]} article(s)")


if __name__ == "__main__":
    main(sys.argv)
