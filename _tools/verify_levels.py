#!/usr/bin/env python3
"""verify_levels.py — variant verify for the levels-as-pages build.

Reuses verify.py's page-agnostic checks where they hold across the
four-page split, and adds variant checks for what only exists in the
split: per-page order, nav-as-page-links, per-page collapse sets,
cross-page bullet deep links, the minimap, the countdown/modal
placement, cross-page anchor resolution, per-page TOCs, and the
current-page marking.

Bar: PASS/FAIL/WARN counts are printed at the end, exactly like
verify.py's main(). The expected bar is stated in
_review/levels-tech-build.md — the variant bar is its own number,
NOT site_config.VERIFY_CHECK_COUNT (which tracks the single-page
verify.py run).

Reuse rules, established by testing on the built variant (2026-11-25):
- check_changed_dots / check_changed_markers /
  check_highlight_consistency take the COMBINED four-page HTML: the
  feed lists appear once (diff), the article highlights once
  (landscape), the SOTM once (sitrep); the minimap's duplicated leaf
  dots are sets, so the dot checks are unaffected.
- check_html / check_naming take the UNESCAPED combined HTML, exactly
  as verify.py's main() does (the footer escapes <1> as &lt;1&gt;).
- check_bullet_deep_links is NOT reusable as-is: its rendered-href
  regex only matches bare `#slug-bN`, and article_bullets() picks up
  the four minimap-group <details> as pseudo-articles (keys sitrep /
  diff / landscape / background). The variant version below drops
  those four keys and normalises the `landscape.html#` prefix.
- check_top_level / check_diff_hoist / check_collapse /
  check_nav are single-page checks; their variant equivalents are
  check_page_order / check_collapse_levels / check_nav_levels below.
- check_glossary's tooltip check runs on the combined HTML (the
  glossary data lives on every page); the glossary.html anchor check
  reads from the repo root, unchanged.
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
import verify as V
import build_dashboard as bd
from minimap import MINIMAP_JS
from site_config import COLLAPSE_INITIAL_OPEN_BY_PAGE

ok, fail, warn = V.ok, V.fail, V.warn
results = V.results

ROOT = Path(__file__).resolve().parent.parent  # ~/workspace/ci-sitrep-levels
MAIN_PAGES = ["sitrep", "diff", "landscape", "background"]
SUB_PAGES = ["audit", "glossary", "corrections", "ci-vs-ei",
             "explainer", "theses", "archive", "about",
             "tracker-whitepaper"]
# tracker.html is the tool page in the standard container
# (2026-11-25, Yorgo: masthead header + sidebar condensed to the
# siderail; same tab). It carries the chrome but is NOT a nav
# page: no SWAP_JS (full loads both ways — the tool's Tailwind
# CDN script is a src script the swap re-run skips, and the
# tool's JS state does not survive a body swap), no slim bar.
# Its chrome + the no-new-tab rule are checked in
# check_research_levels.
NAV_PAGES = MAIN_PAGES + SUB_PAGES
ALL_PAGES = NAV_PAGES + ["dashboard", "tracker"]

# The minimap-group <details> used to be picked up by
# build_dashboard's article walkers as pseudo-articles (keys sitrep /
# diff / landscape / background); the walkers now skip minimap-group
# (the minimap lives outside <main>, like the runtime share JS).
# The filter below is retained as a defensive no-op.
MINIMAP_PSEUDO_IDS = ("sitrep", "diff", "landscape", "background")


def strip_scripts(html):
    return re.sub(r"<script>.*?</script>", "", html, flags=re.DOTALL)


def page_ids(html):
    """Every id a link may target on one page: static ids + the
    runtime article ids + the runtime -bN bullet ids (the same rule
    verify.py's check_html uses)."""
    no_script = strip_scripts(html)
    ids = set(re.findall(r'id="([^"]+)"', no_script))
    ids |= set(bd.compute_article_ids(no_script))
    bullets = bd.article_bullets(no_script)
    for k in MINIMAP_PSEUDO_IDS:
        bullets.pop(k, None)
    for aid, blist in bullets.items():
        ids.update(f"{aid}-b{n}" for n in range(1, len(blist) + 1))
    return ids


def hud_sections_tree(page):
    """The HUD's Sections tree (the masthead's one navigation
    surface since the HUD round, 2026-11-25): the first
    <nav class="minimap-tree"> block. The internal minimap-*
    identifiers are kept as code names."""
    m = re.search(r'<nav class="minimap-tree" id="minimap-tree">(.*?)</nav>',
                  page, re.DOTALL)
    return m.group(1) if m else None


def hud_group_body(tree, group):
    """Body of the HUD group <details> for `group`, with balanced
    <details> counting (the BACKGROUND group's nested R&D group
    defeats a non-greedy match). The summary is excluded, so its
    link is not counted among the children."""
    m = re.search(r'<details class="minimap-group"[^>]*'
                  r'data-minimap-group="' + group + r'"[^>]*>', tree)
    if not m:
        return None
    start, depth, pos = m.end(), 1, m.end()
    while depth:
        nxt_open = tree.find("<details", pos)
        nxt_close = tree.find("</details>", pos)
        if nxt_close == -1:
            return None
        if nxt_open != -1 and nxt_open < nxt_close:
            depth += 1
            pos = nxt_open + len("<details")
        else:
            depth -= 1
            if depth == 0:
                return tree[start:nxt_close]
            pos = nxt_close + len("</details>")
    return None


def hud_group_children(tree, group):
    """The child hrefs of a HUD group (summary link excluded)."""
    body = hud_group_body(tree, group)
    if body is None:
        return None
    sm = re.search(r'<summary[^>]*>.*?</summary>', body, re.DOTALL)
    rest = body[sm.end():] if sm else body
    return re.findall(r'href="([^"]+)"', rest)


# --- Variant checks -------------------------------------------------------

def check_census(md_path, pages, data):
    """Census preserved: 136 articles / 64 feed / 62 figures / 8 strip /
    4 countdowns, plus the live domain-heading counts (panel figures per
    domain: PNL 13, CIC 24, Cert 5, San 10 — after the 2026-11-25
    redistribution the panel-home counts equal the by-content counts:
    the one Cert-subject figure that used to sit in the governance-gap
    panel (the FCA supervisors note) now sits in the Cert panel, so
    CIC 25→24 and Cert 4→5; PNL 13 and San 10 unchanged. A naive
    count of `items` lists only would read PNL 12 / San 9 — it misses
    the money bignote and the right-vs-wrong stacked block, which are
    figures in themselves per iter_panel_figures; see the build note).
    Release round 2026-11-25: articles 117→131 and feed 46→63 (2026-11-26 watch: 131→135; 2026-11-26 catch-up: 135→136, feed 63→64) on the
    new release content (direct-counted: 136 <details data-subject= in
    landscape.html, 63 <li> across the four whats-new-feed lists in
    diff.html); figures/strip/countdowns unchanged (dashboard.json
    untouched)."""
    problems = []
    land = pages["landscape"]
    diff = pages["diff"]
    sit = pages["sitrep"]
    n_art = len(re.findall(r"<details data-subject=", land))
    if n_art != 136:
        problems.append(f"articles: {n_art} (expected 136)")
    n_feed = sum(len(re.findall(r"<li[^>]*>", ul))
                 for ul in re.findall(r'<ul class="whats-new-feed">(.*?)</ul>',
                                      diff, re.DOTALL))
    if n_feed != 64:
        problems.append(f"feed entries: {n_feed} (expected 64)")
    n_fig = len(list(bd.iter_figures(data)))
    if n_fig != 62:
        problems.append(f"figures: {n_fig} (expected 62)")
    n_strip = len(data.get("bottom_line", []))
    if n_strip != 8:
        problems.append(f"strip tiles: {n_strip} (expected 8)")
    n_cd = len(data.get("deadlines", []))
    if n_cd != 4:
        problems.append(f"countdowns: {n_cd} (expected 4)")
    n_tiles = len(re.findall(r'class="tile ', sit))
    if n_tiles != 70:
        problems.append(f"sitrep tiles: {n_tiles} (expected 70 = 62 + 8)")
    # Countdown cards carry class="tile cd-card" (cd-card second).
    n_cd_cards = len(re.findall(r'class="[^"]*\bcd-card\b', diff))
    if n_cd_cards != 4:
        problems.append(f"countdown cards on diff: {n_cd_cards} (expected 4)")
    # Domain headings split label and count across a <span>:
    # `PNL dashboard <span class="section-count">— 13 figures</span>`.
    for label, count in (("PNL dashboard", 13),
                         ("CIC (Agentic Staff) dashboard", 24),
                         ("Codebase Certification dashboard", 5),
                         ("Code Sanitizing Pre-commit dashboard", 10)):
        if not re.search(re.escape(label)
                         + r'\s*<span class="section-count">— '
                         + str(count) + r' figures</span>', sit):
            problems.append(f'domain heading "{label} — {count} figures" missing')
    if problems:
        fail("variant census preserved", "; ".join(problems))
    else:
        ok("variant census preserved",
           "136 articles / 64 feed / 62 figures / 8 strip / 4 countdowns; "
           "70 sitrep tiles; domain headings PNL 13 / CIC 24 / Cert 5 / San 10")


def check_page_order(pages):
    """Per-page section order + exclusivity: each page carries only its
    own sections, in the single-page order restricted to that page."""
    # SITREP: dashboard (surface H2) < The bottom line (abstract
    # box) < What this is < Situation at hand (strip block) <
    # net-impact < domains; no DIFF, no Landscape, no countdown, no
    # modal-less page. (Grid rename 2026-11-25: the box id is
    # bottom-line, the strip id is situation-at-hand — names
    # swapped, order unchanged. Fix round 2026-11-25, Yorgo:
    # EVERYTHING goes under the SITREP title — the H2 moved before
    # the box, so dash now leads.)
    sit = strip_scripts(pages["sitrep"])
    pos = {k: sit.find(v) for k, v in (
        ("sotm", 'id="bottom-line"'),
        ("dash", 'id="executive-dashboard"'),
        ("whatis", 'class="dash-what-is"'),
        ("bl", 'id="situation-at-hand"'),
        ("ni", 'id="net-impact"'),
        ("pnl", 'id="slice-pnl"'))}
    absent = [k for k in ('id="diff"', 'id="report"', 'id="countdown"')
              if k in sit]
    if all(v != -1 for v in pos.values()) and \
            pos["dash"] < pos["sotm"] < pos["whatis"] < pos["bl"] < \
            pos["ni"] < pos["pnl"] and not absent:
        ok("sitrep page order",
           "SITREP < The bottom line < What this is < Situation at hand < "
           "net-impact < domains; no DIFF / Landscape / countdown")
    else:
        fail("sitrep page order",
             f"positions {pos}; unexpected sections: {absent}")

    # DIFF: DIFF H2 < feed groups < feed-empty < countdown <
    # watchlist < Coming up; no SITREP, no Landscape. (Verdicts
    # round, 2026-11-25: Countdown is a peer H3 before What we're
    # watching.)
    dif = strip_scripts(pages["diff"])
    dpos = {k: dif.find(v) for k, v in (
        ("diff", 'id="diff"'),
        ("pnl", 'id="diff-pnl"'), ("cic", 'id="diff-cic"'),
        ("cert", 'id="diff-cert"'), ("san", 'id="diff-san"'),
        ("empty", 'id="feed-empty"'),
        ("cd", 'id="countdown"'),
        ("www", 'id="what-were-watching"'),
        ("coming", "Coming up:"))}
    dabsent = [k for k in ('id="executive-dashboard"', 'id="report"')
               if k in dif]
    if all(v != -1 for v in dpos.values()) and \
            dpos["diff"] < dpos["pnl"] < dpos["cic"] < dpos["cert"] < \
            dpos["san"] < dpos["empty"] < dpos["cd"] < dpos["www"] < \
            dpos["coming"] and not dabsent:
        ok("diff page order",
           "DIFF < feed groups < feed-empty < countdown < watchlist < Coming up; "
           "no SITREP / Landscape")
    else:
        fail("diff page order",
             f"positions {dpos}; unexpected sections: {dabsent}")

    # Landscape: Landscape H2 < report-embed < 136 articles; no SITREP,
    # no DIFF, no Archive section (round 2 — Archive moved to BACKGROUND).
    land = strip_scripts(pages["landscape"])
    lpos = {k: land.find(v) for k, v in (
        ("rep", 'id="report"'),
        ("embed", '<div class="report-embed">'))}
    labsent = [k for k in ('id="executive-dashboard"', 'id="diff"')
               if k in land]
    n_art = len(re.findall(r"<details data-subject=", land))
    if all(v != -1 for v in lpos.values()) and lpos["rep"] < lpos["embed"] \
            and not labsent and n_art == 136 and 'id="archive"' not in land:
        ok("landscape page order",
           "Landscape < report-embed < 136 articles; no SITREP / DIFF / Archive")
    else:
        fail("landscape page order",
             f"positions {lpos}; articles {n_art}; unexpected: {labsent}; "
             f"archive present: {'id=\"archive\"' in land}")

    # BACKGROUND (round 2): consolidated page — seven H2 sections in
    # BACKGROUND order (About, Self-Audit, The names, Glossary,
    # Research, Archive), Research with its four H3 children in order.
    # Scoped to <main> from the BACKGROUND H2: the drawer TOC, the
    # sidebar nav and the minimap repeat the same hrefs, so a
    # whole-page findall would count them too.
    bg = strip_scripts(pages["background"])
    main = bg[bg.find('<h2 id="background"'):bg.find("</main>")]
    h2s = re.findall(r'<h2 id="([^"]+)"', main)
    research_sec = main[main.find('<h2 id="research">'):
                        main.find('<h2 id="archive">')]
    h3s = re.findall(r'<h3 id="([^"]+)"', research_sec)
    g_lo = main.find('<h2 id="glossary">')
    g_hi = main.find('<h2 id="research">')
    gloss_sec = main[g_lo:g_hi] if 0 <= g_lo < g_hi else ""
    # id="diff" is also the Glossary anchor for the DIFF term (a <p>,
    # not the DIFF level) — test its absence outside the Glossary.
    bg_nogloss = bg.replace(gloss_sec, "", 1) if gloss_sec else bg
    babsent = [k for k in ('id="executive-dashboard"', 'id="diff"',
                          'id="report"', 'id="dash-sort"',
                          'class="search-filter-panel"')
               if k in (bg_nogloss if k == 'id="diff"' else bg)]
    if h2s == ["background", "about", "self-audit", "the-names",
               "glossary", "research", "archive"] and h3s == [
            "technology-tracker", "the-surge-monitor", "ci-vs-ei",
            "theses"] and not babsent:
        ok("background page order",
           "BACKGROUND + seven H2 sections in order (About, Self-Audit, "
           "The names, Glossary, R&D, Archive) + R&D H3s "
           "(Technology Tracker, Diffusion Gauge, CI vs EI, "
           "Foundational theses)")
    else:
        fail("background page order",
             f"h2s={h2s}, research h3s={h3s}, unexpected: {babsent}")


def _nav_group_body(nav, summary):
    """Body of the nav-group <details> whose summary matches, with
    balanced <details> counting — the BACKGROUND group's nested
    Research <details> defeats a non-greedy `.*?</details>` match.
    The summary itself is excluded, so its link is not counted."""
    m = re.search(r'<details class="nav-group"[^>]*>\s*' + summary,
                  nav, re.DOTALL)
    if not m:
        return None
    start, depth, pos = m.end(), 1, m.end()
    while depth:
        nxt_open = nav.find("<details", pos)
        nxt_close = nav.find("</details>", pos)
        if nxt_close == -1:
            return None
        if nxt_open != -1 and nxt_open < nxt_close:
            depth += 1
            pos = nxt_open + len("<details")
        else:
            depth -= 1
            if depth == 0:
                return nav[start:nxt_close]
            pos = nxt_close + len("</details>")
    return None


def _open_group_body(page):
    """Balanced body of the first open HUD minimap-group <details>
    on the page — the non-greedy `.*?</details>` stops at the
    nested R&D group's close, which is before the Archive row."""
    start = page.find('<details class="minimap-group" open')
    if start == -1:
        return None
    body_start = page.find(">", start) + 1
    pos, depth = body_start, 1
    while depth:
        nxt_open = page.find("<details", pos)
        nxt_close = page.find("</details>", pos)
        if nxt_close == -1:
            return None
        if nxt_open != -1 and nxt_open < nxt_close:
            depth += 1
            pos = nxt_open + len("<details")
        else:
            depth -= 1
            if depth == 0:
                return page[body_start:nxt_close]
            pos = nxt_close + len("</details>")
    return None


def check_nav_levels(pages):
    """HUD navigation on all 13 nav pages (HUD round, 2026-11-25):
    the masthead's one navigation surface — the Sections tree with
    four groups in order (SITREP / DIFF / Landscape / BACKGROUND),
    each group's children as page links; no index.html and no bare
    section anchors in the tree. Landscape's children are the four
    sections + 29 subsections + 136 articles (169 rows); the other
    groups' child lists are exact."""
    sitrep_group = ["sitrep.html#bottom-line",
                    "sitrep.html#situation-at-hand",
                    "sitrep.html#net-impact",
                    "sitrep.html#slice-pnl",
                    "sitrep.html#pnl-adoption",
                    "sitrep.html#money",
                    "sitrep.html#slice-cic",
                    "sitrep.html#governance-gap",
                    "sitrep.html#cic-evaluation",
                    "sitrep.html#slice-cert",
                    "sitrep.html#cert",
                    "sitrep.html#slice-san",
                    "sitrep.html#right-vs-wrong",
                    "corrections.html"]
    diff_group = ["diff.html#diff-pnl", "diff.html#diff-cic",
                  "diff.html#diff-cert", "diff.html#diff-san",
                  "diff.html#countdown",
                  "diff.html#what-were-watching"]
    bg_group = ["background.html#about", "background.html#self-audit",
                "background.html#the-names", "background.html#glossary",
                "tracker.html", "tracker-whitepaper.html",
                "background.html#ci-vs-ei", "background.html#theses",
                "background.html#archive"]
    land_sections = ["landscape.html#1-pnl-money-adoption-liability",
                     "landscape.html#2-cic-agentic-staff-the-agent-workforce",
                     "landscape.html#3-codebase-certification-attesting-what-is-already-there",
                     "landscape.html#4-code-sanitizing-pre-commit-stopping-bad-code-getting-in"]
    bad_order, bad_page, bad_anchor = [], [], []
    for name, page in pages.items():
        tree = hud_sections_tree(page)
        if tree is None or page.count('id="minimap-tree"') != 1:
            bad_order.append(f"{name}: no single HUD tree")
            continue
        pos = [tree.find(f'data-minimap-group="{g}"')
               for g in ("sitrep", "diff", "landscape", "background")]
        if any(p == -1 for p in pos) or pos != sorted(pos):
            bad_order.append(f"{name}: group order {pos}")
        if "index.html" in tree:
            bad_page.append(f"{name}: index.html in HUD tree")
        for bare in ('href="#executive-dashboard"',
                     'href="#diff"', 'href="#report"'):
            if bare in tree:
                bad_anchor.append(f"{name}: bare {bare} in HUD tree")
    if not bad_order:
        ok("nav: four sections in order on every page",
           "SITREP < DIFF < Landscape < BACKGROUND, 13 pages")
    else:
        fail("nav: four sections in order on every page", "; ".join(bad_order))
    if bad_page or bad_anchor:
        fail("nav: page links only (no index.html, no bare anchors)",
             "; ".join(bad_page + bad_anchor))
    else:
        ok("nav: page links only (no index.html, no bare anchors)",
           "13 pages")
    # Group children, in tree order (full hrefs).
    for label, group, want in (
            ("SITREP", "sitrep", sitrep_group),
            ("BACKGROUND", "background", bg_group),
            ("DIFF", "diff", diff_group)):
        bad = []
        for name, page in pages.items():
            tree = hud_sections_tree(page)
            if tree is None:
                bad.append(f"{name}: no HUD tree")
                continue
            got = hud_group_children(tree, group)
            if got != want:
                bad.append(f"{name}: {label} links {got}")
        if not bad:
            ok(f"nav: {label} group links on every page", " · ".join(want))
        else:
            fail(f"nav: {label} group links on every page", "; ".join(bad))
    # Landscape: the four sections in order among 169 rows
    # (4 sections + 29 subsections + 136 articles).
    bad = []
    for name, page in pages.items():
        tree = hud_sections_tree(page)
        if tree is None:
            bad.append(f"{name}: no HUD tree")
            continue
        got = hud_group_children(tree, "landscape")
        if got is None or len(got) != 169:
            bad.append(f"{name}: Landscape has {len(got) if got else 0} rows (expected 169)")
            continue
        pos = [got.index(h) if h in got else -1 for h in land_sections]
        if any(p == -1 for p in pos) or pos != sorted(pos):
            bad.append(f"{name}: Landscape section order {pos}")
    if not bad:
        ok("nav: Landscape group links on every page",
           "4 sections in order among 169 rows (sections + subsections + 136 articles)")
    else:
        fail("nav: Landscape group links on every page", "; ".join(bad))


def check_collapse_levels(pages):
    """Per-page collapse sets: the Sections handler skips exactly
    COLLAPSE_HANDLER_EXEMPT (empty), and each page's initial-collapse
    loop skips exactly COLLAPSE_INITIAL_OPEN_BY_PAGE[page]. Same
    marker-scoped parse as verify.py's check_collapse, per page."""
    try:
        import site_config
        want_h_ids = set(site_config.COLLAPSE_HANDLER_EXEMPT_IDS)
        want_h_classes = set(site_config.COLLAPSE_HANDLER_EXEMPT_CLASSES)
    except (ImportError, AttributeError) as e:
        fail("collapse: handler + initial-open sets match site_config",
             f"cannot import the declared sets: {e}")
        return
    problems = []
    for name, html in pages.items():
        if name not in MAIN_PAGES:
            continue
        want_i = COLLAPSE_INITIAL_OPEN_BY_PAGE[name]
        want_i_ids, want_i_classes = set(want_i["ids"]), set(want_i["classes"])
        sec_start = html.find("// Sections control (on the surface title line; row 1 on the single-page build)")
        head_start = html.find("// Make h2/h3/h4/h5/h6 headings collapsible")
        crumb_start = html.find("// Breadcrumbs: at the top of every section body")
        if sec_start == -1 or head_start == -1 or crumb_start == -1 \
                or not (sec_start < head_start < crumb_start):
            problems.append(f"{name}: cannot locate the Sections/initial-collapse/Breadcrumbs markers")
            continue
        handler = html[sec_start:head_start]
        init = html[head_start:crumb_start]
        skips = re.findall(r"if \(collapse && (.*?)\) return;", handler, re.DOTALL)
        if len(skips) > 1:
            problems.append(f"{name}: handler has {len(skips)} skip statements")
            got_h_ids, got_h_classes = set(), set()
        else:
            cond = skips[0] if skips else ""
            got_h_ids = set(re.findall(r"h\.id === '([^']+)'", cond))
            got_h_classes = set(re.findall(r"classList\.contains\('([^']+)'", cond))
        if got_h_ids != want_h_ids or got_h_classes != want_h_classes:
            problems.append(f"{name}: handler skips ids={sorted(got_h_ids)} "
                            f"classes={sorted(got_h_classes)}")
        adds = re.findall(r"if \((.*?)\) h\.classList\.add\('collapsed'\)",
                          init, re.DOTALL)
        if len(adds) != 1:
            problems.append(f"{name}: initial-collapse loop found {len(adds)} times")
        else:
            got_i_ids = set(re.findall(r"h\.id !== '([^']+)'", adds[0]))
            got_i_classes = set(re.findall(r"!h\.classList\.contains\('([^']+)'\)",
                                           adds[0]))
            if got_i_ids != want_i_ids or got_i_classes != want_i_classes:
                problems.append(f"{name}: initial-open ids={sorted(got_i_ids)} "
                                f"classes={sorted(got_i_classes)}, declared "
                                f"ids={sorted(want_i_ids)} "
                                f"classes={sorted(want_i_classes)}")
        if 'class="sec-controls"' not in html:
            problems.append(f"{name}: no .sec-controls element")
        if "secControls.addEventListener" not in html:
            problems.append(f"{name}: handler not wired")
    if problems:
        fail("collapse: handler + initial-open sets match site_config",
             "; ".join(problems))
    else:
        ok("collapse: handler + initial-open sets match site_config",
           "handler skips nothing; per-page initial-open sets "
           "(sitrep ids executive-dashboard+net-impact + dash-slice, "
           "diff ids diff, landscape ids report, background ids background)")


def check_bullet_deep_links_levels(md_path, pages):
    """Variant of verify.py's check_bullet_deep_links: the mapped
    figures are checked against landscape.html's bullets, and the
    rendered -bN hrefs are collected from sitrep + diff with the
    `landscape.html#` prefix normalised to bare `#`. The four
    minimap-group pseudo-articles are dropped from the bullet map."""
    dash_path = Path(md_path).parent / "dashboard.json"
    if not dash_path.exists():
        fail("bullet deep links land on the right bullet",
             "dashboard.json missing")
        return
    data = json.loads(dash_path.read_text())
    land = pages["landscape"]
    try:
        bullets = bd.article_bullets(land)
    except AssertionError as e:
        fail("bullet deep links land on the right bullet", str(e))
        return
    for k in MINIMAP_PSEUDO_IDS:
        bullets.pop(k, None)
    problems = []
    mapped_hrefs = set()
    n_mapped = 0
    n_tokens = 0

    def figures():
        for f in bd.iter_figures(data):
            yield f, f.get("source", f.get("title", f.get("text", "?")[:40]))
        for it in data.get("bottom_line", []):
            yield it, "bottom line " + it.get("source", "?")
        for dl in data.get("deadlines", []):
            yield dl, "deadline " + dl.get("label", "?")

    for f, src in figures():
        if "bullet" not in f:
            continue
        n_mapped += 1
        mapped_hrefs.add(bd.figure_href(f))
        link = f.get("link", "")
        if not link.startswith("#"):
            problems.append(f"{src}: bullet {f['bullet']} but no article link")
            continue
        aid = link[1:]
        if aid not in bullets:
            problems.append(f"{src}: evidencing article #{aid} not in the built page")
            continue
        n = f["bullet"]
        if not isinstance(n, int) or isinstance(n, bool) or not 1 <= n <= len(bullets[aid]):
            problems.append(f"{src}: bullet {n} out of range "
                            f"(#{aid} has {len(bullets[aid])} bullets)")
            continue
        token = bd.bullet_token_for(f)
        if token is None:
            problems.append(f"{src}: bullet {n} but no token — add '\"bullet_token\"'")
            continue
        n_tokens += 1
        if token.lower() not in bullets[aid][n - 1].lower():
            problems.append(f"{src}: bullet {n} of #{aid} does not contain {token!r}")
    rendered = set()
    for name in ("sitrep", "diff"):
        no_script = strip_scripts(pages[name])
        for h in re.findall(r'href="(?:landscape\.html)?(#[^"]+)"', no_script):
            if re.search(r"-b\d+$", h):
                rendered.add(h)
    for href in sorted(rendered):
        m = re.match(r"^#(.*)-b(\d+)$", href)
        aid, n = m.group(1), int(m.group(2))
        if aid not in bullets or not 1 <= n <= len(bullets[aid]):
            problems.append(f"rendered {href} matches no bullet")
    stray = sorted(rendered - mapped_hrefs)
    if stray:
        problems.append(f"rendered deep links with no mapped figure: {stray[:5]}"
                        + (f" (+{len(stray) - 5} more)" if len(stray) > 5 else ""))
    missing = sorted(mapped_hrefs - rendered)
    if missing:
        problems.append(f"mapped deep links not rendered: {missing[:5]}"
                        + (f" (+{len(missing) - 5} more)" if len(missing) > 5 else ""))
    if problems:
        fail("bullet deep links land on the right bullet", "; ".join(problems))
    else:
        ok("bullet deep links land on the right bullet",
           f"{n_mapped} figures mapped ({n_tokens} tokens checked); "
           f"{len(rendered)} distinct deep links rendered across sitrep + diff; "
           "all land on a bullet containing the token")


def minimap_trees(page):
    """The minimap's two trees: <nav class="minimap-tree"> (Sections)
    and <nav class="minimap-tree minimap-all"> (All articles). The
    panel itself is <div id="minimap">, the scrim
    <div id="minimap-scrim"> — neither is a <nav>, and the tree
    regex is the only way to scope checks to the minimap's rows."""
    return re.findall(r'<nav class="minimap-tree[^>]*>(.*?)</nav>',
                      page, re.DOTALL)


def check_minimap_levels(pages, md_path):
    """Minimap present + correct on all nav pages: floating toggle,
    panel, scrim, float-close; five groups (SITREP/DIFF/Landscape/
    BACKGROUND + nested Research); BACKGROUND children in order with
    background.html as the group landing; no standalone Self-Audit;
    domain rows named 'X dashboard' without doubling."""
    problems = []
    for name, page in pages.items():
        if name not in NAV_PAGES:
            continue
        for marker, label in (
                ('id="minimap-toggle"', "toggle"),
                ('id="minimap"', "panel"),
                ('id="minimap-scrim"', "scrim"),
                ('id="minimap-close"', "float-close")):
            if marker not in page:
                problems.append(f"{name}: no minimap {label}")
        trees = minimap_trees(page)
        if not trees:
            problems.append(f"{name}: no minimap trees")
            continue
        body = "".join(trees)
        for grp in ("sitrep", "diff", "landscape", "background"):
            if f'data-minimap-group="{grp}"' not in body:
                problems.append(f"{name}: minimap missing {grp} group")
        if "minimap-self-audit" in body:
            problems.append(f"{name}: stale standalone Self-Audit in minimap")
        if "dashboard — dashboard" in body:
            problems.append(f"{name}: doubled 'dashboard' in a domain label")
        if 'href="background.html"' not in body:
            problems.append(f"{name}: minimap BACKGROUND group has no background.html landing")
        # Minimap design pass (2026-11-25): explicit-level indent,
        # the row-end mark slot, group article lists for the
        # summary marks, and the new legend wording must all be
        # present; the old read-mark span must be gone.
        for marker, label in (
                ('data-level="1"', "L1 indent"),
                ('data-level="2"', "L2 indent"),
                ('data-level="3"', "L3 indent"),
                ('class="minimap-mark"', "mark slot"),
                ('data-minimap-articles="', "group article lists")):
            if marker not in body:
                problems.append(f"{name}: minimap missing {label}")
        if 'class="minimap-read"' in body:
            problems.append(f"{name}: stale minimap-read span in minimap")
        if "new — changed in the last 7 days, not yet read" not in page \
                or " started" not in page:
            problems.append(f"{name}: minimap legend wording stale")
        # Research nested in BACKGROUND, last after Glossary, four
        # children in order (round 2: Tracker, Diffusion Gauge, CI vs EI,
        # Foundational theses), Archive last after Research. Positions
        # of the bare hrefs — the row anchors carry class/data-title
        # attributes, so the match is on the href value, not the full
        # tag. SITREP must carry no archive.html row (Archive moved).
        if 'data-minimap-group="research"' not in body:
            problems.append(f"{name}: minimap missing R&D subgroup")
        else:
            gloss = body.find('href="background.html#glossary"')
            res = body.find('data-minimap-group="research"')
            tr = body.find('href="tracker.html"')
            wp = body.find('href="tracker-whitepaper.html"')
            ci = body.find('href="background.html#ci-vs-ei"')
            th = body.find('href="background.html#theses"')
            arch = body.find('href="background.html#archive"')
            if gloss == -1 or res == -1 or tr == -1 or wp == -1 \
                    or ci == -1 or th == -1 or arch == -1 \
                    or not (gloss < res < tr < wp < ci < th < arch):
                problems.append(f"{name}: minimap R&D not after Glossary / children out of order")
        if 'href="archive.html"' in body:
            problems.append(f"{name}: stale archive.html row in minimap")
    if problems:
        fail("minimap present on every page", "; ".join(problems))
    else:
        ok("minimap present on every page",
           "toggle + panel + scrim + float-close on every nav page; five groups; "
           "BACKGROUND lands on background.html; R&D after Glossary; "
           "Archive last in BACKGROUND; design-pass levels + mark slots + legend")

    # Workstream 5 (Yorgo, 2026-11-25): opening the minimap must NOT
    # move focus into the search box — on a phone it pops the keyboard
    # over half the screen. No .focus() call may sit inside openPanel
    # (up to closePanel); the toggle-focus on close and the
    # clear-button refocus stay.
    op_start = MINIMAP_JS.find("function openPanel()")
    op_end = MINIMAP_JS.find("function closePanel()", op_start)
    op_body = MINIMAP_JS[op_start:op_end] if op_start != -1 and op_end != -1 else ""
    if op_start == -1 or op_end == -1:
        fail("minimap: no autofocus on open",
             "cannot locate openPanel/closePanel in MINIMAP_JS")
    elif ".focus()" in op_body:
        fail("minimap: no autofocus on open",
             "a .focus() call sits inside openPanel")
    elif MINIMAP_JS.count("searchInput.focus()") != 1 \
            or "toggle.focus()" not in MINIMAP_JS:
        fail("minimap: no autofocus on open",
             "expected exactly one searchInput.focus() (clear handler) "
             "and toggle.focus() on close")
    else:
        ok("minimap: no autofocus on open",
           "openPanel moves no focus; toggle.focus() on close; "
           "searchInput.focus() only in the clear handler")

    # One-click switch (fix round, 2026-11-25): the two toggles must
    # stay clickable while the other panel is open, or a tap lands on
    # the open panel's scrim (990) and only closes it — the switch
    # then costs a second tap. The Contents toggle (z 500) lifts
    # above the Tools scrim + drawer while the drawer is open, and
    # the Tools button lifts above the minimap scrim + panel while
    # the minimap is open; both lifts drop the moment the other
    # panel closes (the body classes are removed synchronously).
    combined_css = "".join(pages[n] for n in NAV_PAGES if n in pages)
    switch_problems = []
    if "body.tools-open #minimap-toggle { z-index: 1005; }" not in combined_css:
        switch_problems.append("no body.tools-open toggle lift")
    if "body.minimap-open main h1 .tools-btn { position: relative; z-index: 1005; }" not in combined_css:
        switch_problems.append("no body.minimap-open Tools-button lift")
    if switch_problems:
        fail("minimap/tools one-click switch", "; ".join(switch_problems))
    else:
        ok("minimap/tools one-click switch",
           "both toggles lift above the other panel's scrim (z 1005) "
           "while it is open, so one tap closes the other panel and "
           "opens its own")

    # Leaf dots: the minimap's changed-article rows must be exactly the
    # feed's changed set (44), in both tabs, on every page — and the
    # row titles must carry no raw markdown or URLs (the 2026-11-25
    # Veracode defect: tree titles with raw [text](url) never matched
    # the runtime ids, so two articles linked nowhere).
    today = datetime.now(ZoneInfo("America/New_York")).date()
    from site_config import CHANGE_WINDOW_DAYS
    from datetime import timedelta
    window_start = (today - timedelta(days=CHANGE_WINDOW_DAYS)).isoformat()
    try:
        tags = bd.parse_article_tags(md_path)
        sources = bd.parse_article_sources(md_path)
    except (ValueError, FileNotFoundError) as e:
        fail("minimap leaf dots match the feed", f"cannot parse tags/sources: {e}")
        return
    url_to_ids = bd.invert_sources(sources)
    combined = "".join(pages[n] for n in MAIN_PAGES)
    expected = V.feed_changed_set(strip_scripts(combined), tags,
                                  url_to_ids, window_start)
    problems = []
    for name, page in pages.items():
        if name not in NAV_PAGES:
            continue
        trees = minimap_trees(page)
        if not trees:
            problems.append(f"{name}: no minimap trees")
            continue
        body = "".join(trees)
        # Row titles must carry no raw markdown links or URLs (the
        # 2026-11-25 Veracode defect). Bare "[" is NOT tested: article
        # headlines legitimately carry bracketed tags ([VENDOR CLAIM],
        # [VENDOR RESEARCH], ...).
        if "https://" in body or re.search(r"\[[^\]]*\]\(https?://", body):
            problems.append(f"{name}: raw markdown/URL in minimap row titles")
        # Leaf dots are the <span class="changed-dot" data-article>
        # elements — one per changed article per tab. (The row <a>
        # carries the same data-article/data-changed attributes, so a
        # bare data-article count would double-count.)
        dots = re.findall(
            r'<span class="changed-dot"[^>]*data-article="([^"]+)"', body)
        if len(dots) != 2 * len(expected):
            problems.append(f"{name}: {len(dots)} minimap leaf dots "
                            f"(expected {2 * len(expected)} = 44 x 2 tabs)")
        if set(dots) != set(expected):
            problems.append(f"{name}: minimap dot set != feed changed set "
                            f"({len(set(dots))} distinct)")
    if problems:
        fail("minimap leaf dots match the feed", "; ".join(problems))
    else:
        ok("minimap leaf dots match the feed",
           f"{len(expected)} changed articles x 2 tabs on every page; "
           "no raw markdown in row titles")


def check_research_levels(pages):
    """R&D subsection (2026-11-25, spec item 33 — variant form of
    verify.py's check_research; renamed from "Research" 2026-11-25
    on Yorgo's word — the id/href anchors keep the name
    "research"): a nested <details> inside the
    BACKGROUND group, after Glossary, with four children in order
    (round 2: tracker tool, white paper, CI vs EI, Foundational
    theses); Archive follows R&D as the last BACKGROUND row.
    Both tool/paper pages exist, the tool carries Yorgo's byline + a
    return link to the variant landing page (sitrep.html, F2 — not
    index.html), the white paper carries his byline. Three results.
    The R&D <details> may carry `open` (on the white-paper,
    CI-vs-EI or theses page) and the white-paper link may carry
    aria-current, so the match allows both."""
    # HUD round (2026-11-25): the R&D subgroup lives in the HUD
    # tree's BACKGROUND group (data-minimap-group="research"), its
    # rows are minimap-rows; the white-paper row may carry the
    # current marking, so the row match allows attributes.
    research_re = re.compile(
        r'<li><details class="minimap-group"( open)? '
        r'data-minimap-group="research"[^>]*>\s*'
        r'<summary[^>]*>R&amp;D.*?</summary>\s*'
        r'<ul>\s*'
        r'<li><a[^>]*href="tracker\.html"[^>]*>'
        r'<span class="minimap-row-title">Technology Tracker</span>'
        r'<span class="minimap-mark">(<span class="changed-dot"[^>]*></span>)?</span></a></li>\s*'
        r'<li><a[^>]*href="tracker-whitepaper\.html"[^>]*>'
        r'<span class="minimap-row-title">Diffusion Gauge</span>'
        r'<span class="minimap-mark">(<span class="changed-dot"[^>]*></span>)?</span></a></li>\s*'
        r'<li><a[^>]*href="background\.html#ci-vs-ei"[^>]*>'
        r'<span class="minimap-row-title">CI vs EI</span>'
        r'<span class="minimap-mark">(<span class="changed-dot"[^>]*></span>)?</span></a></li>\s*'
        r'<li><a[^>]*href="background\.html#theses"[^>]*>'
        r'<span class="minimap-row-title">Foundational theses</span>'
        r'<span class="minimap-mark">(<span class="changed-dot"[^>]*></span>)?</span></a></li>\s*'
        r'</ul>\s*</details></li>', re.DOTALL)
    # 1. R&D nested in BACKGROUND, after Glossary, four children
    # in order, Archive last after R&D, on every nav page.
    bad = []
    for name, page in pages.items():
        if name not in NAV_PAGES:
            continue
        tree = hud_sections_tree(page)
        if tree is None:
            bad.append(f"{name}: no HUD tree")
            continue
        m = research_re.search(tree)
        if not m:
            bad.append(f"{name}: no R&D subsection")
            continue
        gloss = tree.find('href="background.html#glossary"')
        if gloss == -1 or gloss > m.start():
            bad.append(f"{name}: R&D not after Glossary")
        bg = tree.find('data-minimap-group="background"')
        if bg == -1 or bg > m.start():
            bad.append(f"{name}: R&D not inside BACKGROUND")
        tail = tree[m.end():]
        arch_re = re.compile(
            r'\s*<li><a[^>]*href="background\.html#archive"[^>]*>'
            r'<span class="minimap-row-title">Archive</span>'
            r'<span class="minimap-mark">(<span class="changed-dot"[^>]*></span>)?</span></a></li>\s*'
            r'</ul>\s*</details>', re.DOTALL)
        if not arch_re.match(tail):
            bad.append(f"{name}: Archive does not follow R&D as the last BACKGROUND row")
    if not bad:
        ok("r&d: subsection in BACKGROUND on every page",
           "after Glossary; Tracker + white paper + CI vs EI + theses; "
           "Archive last")
    else:
        fail("r&d: subsection in BACKGROUND on every page",
             "; ".join(bad))

    # 2. The tracker tool page: served, bylined, in the standard
    # container (2026-11-25, Yorgo: header + siderail, same tab):
    # masthead + siderail + condensed default + phone trigger,
    # NO swap JS (full loads both ways), and no page may open it
    # in a new tab.
    tool = ROOT / "tracker.html"
    problems = []
    if not tool.is_file():
        problems.append("tracker.html missing")
    else:
        text = tool.read_text()
        if "by Yorgo P. Bougás · Confluence&lt;1&gt;" not in text:
            problems.append("no byline (Yorgo P. Bougás · Confluence<1>)")
        if 'href="sitrep.html"' not in text:
            problems.append("no return link to sitrep.html")
        if 'id="cycleCanvas"' not in text:
            problems.append("no chart canvas")
        if 'class="masthead-title"' not in text:
            problems.append("no site masthead (container chrome)")
        if 'class="hud-rail"' not in text:
            problems.append("no siderail (container chrome)")
        if 'hud-condensed' not in text.split("<body", 1)[-1].split(">", 1)[0]:
            problems.append("body does not default to the siderail "
                            "(hud-condensed)")
        if 'id="minimap-toggle"' not in text:
            problems.append("no phone HUD trigger (container chrome)")
        if "__ciSwap" in text:
            problems.append("carries SWAP_JS — the tool page must "
                            "stay a full load")
    for name, page in pages.items():
        if re.search(r'href="tracker\.html"[^>]*target="_blank"',
                     page):
            problems.append(f"{name}: tracker.html opens in a new "
                            "tab (same tab since 2026-11-25)")
    if not problems:
        ok("r&d: tracker tool page served",
           "byline + return link + canvas + container chrome "
           "(masthead, siderail default, phone trigger), no swap "
           "JS, same-tab links site-wide")
    else:
        fail("r&d: tracker tool page served", "; ".join(problems))

    # 3. The white-paper page: served, with Yorgo's byline.
    paper = ROOT / "tracker-whitepaper.html"
    problems = []
    if not paper.is_file():
        problems.append("tracker-whitepaper.html missing")
    else:
        text = paper.read_text()
        if "Yorgo P. Bougás" not in text:
            problems.append("no byline")
        if "Diffusion Gauge" not in text:
            problems.append("no title")
    if not problems:
        ok("r&d: white-paper page + byline",
           "Diffusion Gauge, bylined Yorgo P. Bougás")
    else:
        fail("r&d: white-paper page + byline", "; ".join(problems))


def check_countdown_modal_levels(pages):
    """Countdowns on DIFF only (4 cards under their own peer H3,
    before What we're watching; FCA/NY RAISE link to landscape
    bullets, TPRM/OSFI stay same-page) and the how-to modal on
    every main page. Modal rule (Yorgo, 2026-11-25 17:43 EST):
    auto-opens on EVERY fresh page load — no per-page auto-open
    marking; the only suppression is the "Don't ever show me
    again" checkbox (localStorage ci-sitrep-howto-never) — the
    pre-rename ci-sitrep-howto-dismissed key is NOT honoured
    (Yorgo, 2026-11-25 18:21 EST) and must not appear in the
    shipped JS; the sidebar button opens it on demand from any
    page."""
    problems = []
    sit, dif = pages["sitrep"], pages["diff"]
    if 'id="countdown"' in sit:
        problems.append("countdown strip still on sitrep")
    if 'id="countdown"' not in dif:
        problems.append("no countdown strip on diff")
    for label, link in (
            ("FCA", "landscape.html#firms-stay-accountable-for-ai-in-financial-crime-controls-b4"),
            ("NY RAISE", "landscape.html#new-york-opens-frontier-ai-registration-a-financial-b1")):
        if f'href="{link}"' not in dif:
            problems.append(f"countdown {label} link missing: {link}")
    if dif.count('href="#what-were-watching"') < 2:
        problems.append("TPRM/OSFI countdown links should stay #what-were-watching")
    for name in ("sitrep", "diff", "landscape", "background"):
        if 'id="howto-modal"' not in pages[name]:
            problems.append(f"no howto modal on {name}")
        if 'id="howto-open"' not in pages[name]:
            problems.append(f"no howto open button on {name}")
        if 'data-auto-open' in pages[name]:
            problems.append(
                f"howto modal carries per-page auto-open gating on {name}")
        if 'ci-sitrep-howto-never' not in pages[name]:
            problems.append(f"howto never-flag key missing on {name}")
        if 'ci-sitrep-howto-dismissed' in pages[name]:
            problems.append(
                f"legacy howto dismissed-flag still honoured on {name}")
        if "Don't ever show me again" not in pages[name]:
            problems.append(f"howto dismiss checkbox label missing on {name}")
    if problems:
        fail("countdown on DIFF, modal auto-opens every arrival",
             "; ".join(problems))
    else:
        ok("countdown on DIFF, modal auto-opens every arrival",
           "4 countdown cards on diff (FCA/NY RAISE -> landscape bullets); "
           "modal + sidebar open button on all four main pages; "
           "never-flag opt-out on every page, no per-page gating")


def check_xlinks_levels(pages):
    """Every cross-page href resolves: `page.html#fragment` must exist
    on the target page (static id, runtime article id, or -bN bullet
    id); every bare `#fragment` must exist on its own page; every
    `.md` file link must exist under the levels root (a `../` target
    escapes the variant — the archive page's `../SYNTHESIZED.md`
    links are rebased at build time). Fragments on `.md` targets are
    not verifiable (raw markdown) and are skipped. Covers the
    431/360/286/288 landscape.html# links the page split created."""
    ids_by_page = {name: page_ids(html) for name, html in pages.items()}
    problems = []
    for name, html in pages.items():
        no_script = strip_scripts(html)
        for href in sorted(set(re.findall(r'href="([^"]+)"', no_script))):
            if "://" in href or href.startswith(("mailto:", "tel:", "data:")):
                continue
            if "#" not in href and not href.endswith((".md", ".png")):
                continue
            target, _, frag = href.partition("#")
            if not target:
                if frag and frag not in ids_by_page[name]:
                    problems.append(f"{name}.html: bare #{frag} resolves nowhere on the page")
                continue
            if target.endswith(".md"):
                # File link: must exist under the levels root.
                if target.startswith("../") or not (ROOT / target).is_file():
                    problems.append(f"{name}.html: {href} — file not in the variant")
                continue
            if target.endswith(".png"):
                if target.startswith("../") or not (ROOT / target).is_file():
                    problems.append(f"{name}.html: {href} — file not in the variant")
                continue
            if not frag:
                continue
            tname = target[:-5] if target.endswith(".html") else target
            if tname not in ids_by_page:
                problems.append(f"{name}.html: link to unknown page {target}")
            elif frag not in ids_by_page[tname]:
                problems.append(f"{name}.html: {href} — #{frag} not on {target}")
    if problems:
        fail("cross-page anchors resolve",
             "; ".join(problems[:10])
             + (f" (+{len(problems) - 10} more)" if len(problems) > 10 else ""))
    else:
        ok("cross-page anchors resolve",
           f"{len(ids_by_page)} pages, all page.html#fragment and bare #fragment links resolve")


def check_toc_levels(pages):
    """HUD tree page-contents (HUD round, 2026-11-25): each main
    page's own group in the masthead HUD carries its page contents
    as rows (the former page-top TOCs): sitrep 14 (2 + 12), diff
    5 (4 domains + watchlist), landscape 169 (4 sections + 29
    subsections + 136 articles), background 9 (9 sections — the
    page-H2 landing row was removed in the TOC cleanup,
    2026-11-25). DIFF's group carries the watchlist row;
    BACKGROUND's carries the R&D sub-group."""
    expected = {"sitrep": 14, "diff": 6, "landscape": 169,
                "background": 9}
    problems = []
    for name, want in expected.items():
        tree = hud_sections_tree(pages[name])
        n = len(hud_group_children(tree, name))
        if n != want:
            problems.append(f"{name}: HUD page contents {n} rows (expected {want})")
    if 'href="diff.html#what-were-watching"' not in pages["diff"]:
        problems.append("diff HUD group has no watchlist row")
    if 'data-minimap-group="research"' not in pages["background"]:
        problems.append("background HUD group has no R&D sub-group")
    if problems:
        fail("per-page TOCs", "; ".join(problems))
    else:
        ok("per-page TOCs",
           "in the HUD tree: sitrep 14 / diff 6 (incl. countdown + watchlist) / landscape 169 / background 9 (incl. R&D)")


def check_current_levels(pages):
    """The HUD marks the current page at build time (HUD round,
    2026-11-25): the page's group(s) open in the static markup,
    exactly one row carries aria-current="page", and the marked
    row is the page's own — the surface summary link on main
    pages, the sub-page's row on sub-pages — inside the open
    group(s). The white paper, CI vs EI and theses sit in the
    nested R&D group, so they open TWO groups (BACKGROUND + R&D)."""
    want = {"sitrep": "sitrep.html",
            "diff": "diff.html",
            "landscape": "landscape.html",
            "background": "background.html",
            "audit": "background.html#self-audit",
            "glossary": "background.html#glossary",
            "corrections": "corrections.html",
            "ci-vs-ei": "background.html#ci-vs-ei",
            "explainer": "background.html#the-names",
            "theses": "background.html#theses",
            "archive": "background.html#archive",
            "about": "background.html#about",
            "tracker-whitepaper": "tracker-whitepaper.html"}
    problems = []
    for name, page in pages.items():
        if name not in NAV_PAGES:
            continue
        tree = hud_sections_tree(page)
        n_open = tree.count('<details class="minimap-group" open')
        want_open = 2 if name in ("tracker-whitepaper", "ci-vs-ei",
                                  "theses") else 1
        if n_open != want_open:
            problems.append(f"{name}: {n_open} open HUD groups (expected {want_open})")
            continue
        cur = re.findall(r'aria-current="page"[^>]*href="([^"]+)"',
                         tree) + re.findall(r'href="([^"]+)"[^>]*aria-current="page"',
                                            tree)
        if len(cur) != 1:
            problems.append(f"{name}: {len(cur)} aria-current rows (expected 1)")
        elif cur[0] != want[name]:
            problems.append(f"{name}: aria-current is {cur[0]} (expected {want[name]})")
        else:
            # The aria-current row must sit inside the open group.
            gm_body = _open_group_body(page)
            if gm_body is None or f'href="{want[name]}"' not in gm_body:
                problems.append(f"{name}: aria-current row is not inside the open group")
    if problems:
        fail("current page marked in nav", "; ".join(problems))
    else:
        ok("current page marked in nav",
           "one open HUD group + one aria-current row on each of 13 pages "
           "(white paper, CI vs EI and theses open BACKGROUND + R&D)")


# --- Entry point -----------------------------------------------------------

def check_hierarchy_levels(pages):
    """WS6a (2026-11-25): the SITREP heading ladder, revised after
    Yorgo's phone screenshots showed the levels reading as one jumble.
    Every rung differs in size AND colour/weight/rule, not size alone:
    SITREP H2 22px/700 navy (base main-h2 rule, asserted in
    check_page_order's shape, not repeated here) > bottom-line heading
    19px/700 dark rust-brown #8a3f2e, with a 1px hairline above the
    block > domain H3 17px/700 navy + bottom hairline > panel H3 15px/
    600 navy. "What this is" 14px/400 muted sits a full step below
    the panel headings it used to tie with; the SOTM summary stays
    the 13px uppercase label rung. Asserted on the built sitrep.html
    CSS (the rules are inlined in the page)."""
    problems = []
    sit = pages["sitrep"]
    rules = (
        (r"\.dash-bottom-line \{ margin: 0 0 8px; "
         r"border-top: 1px solid var\(--line\); padding-top: 12px; \}",
         "bottom-line block top hairline"),
        (r"\.dash-bottom-line-heading \{ font-size: 19px; "
         r"font-weight: 700; color: #8a3f2e;",
         "bottom-line heading 19px/700 rust-brown"),
        (r"h3\.dash-slice \{ font-size: 17px; color: #8a3f2e; "
         r"border-bottom: 1px solid var\(--line\);",
         "domain H3 17px rust-brown + hairline"),
        (r"h3\.dash-panel \{ font-size: 15px; font-weight: 600; "
         r"color: #283060;",
         "panel H3 15px/600 navy"),
        (r"main h3 \{ font-size: 18px; margin: 28px 0 10px; "
         r"line-height: 1\.35; color: #283060; \}",
         "base H3 18px navy"),
        (r"h3\.feed-group \{ font-size: 17px; font-weight: 700; "
         r"color: #8a3f2e; \}",
         "DIFF feed-group H3 17px/700 rust-brown"),
        (r"main h2#about, main h2#self-audit, main h2#the-names, "
         r"main h2#glossary, main h2#research \{ font-size: 20px; "
         r"color: #8a3f2e; \}",
         "BACKGROUND section H2s 20px rust-brown"),
        (r"\.dash-what-is > summary \{ font-weight: 400; "
         r"color: var\(--muted\); font-size: 14px; \}",
         "\"What this is\" 14px/400 muted"),
        (r"\.sotm-box summary \{ font-size: 13px; "
         r"text-transform: uppercase;",
         "SOTM summary 13px uppercase label"),
    )
    for pat, label in rules:
        if not re.search(pat, sit):
            problems.append(f"{label} rule missing")
    # The old rungs must be gone, not merely superseded: a stale
    # duplicate rule later in the cascade would win silently.
    stale = (
        (r"\.dash-bottom-line-heading \{ font-size: 20px;",
         "bottom-line heading still 20px"),
        (r"h3\.dash-slice \{ font-size: 18px;",
         "domain H3 still 18px"),
        (r"h3\.dash-panel \{ font-size: 16px;",
         "panel H3 still 16px"),
        (r"\.dash-what-is > summary \{[^}]*font-size: 15px;",
         "\"What this is\" still 15px"),
    )
    for pat, label in stale:
        if re.search(pat, sit):
            problems.append(label)
    if problems:
        fail("SITREP hierarchy ladder (WS6a)", "; ".join(problems))
    else:
        ok("SITREP hierarchy ladder (WS6a)",
           "H2 22 navy > bottom line 19 rust-brown + hairline > "
           "domain 17 rust-brown + hairline > panel 15/600 navy; "
           "base H3 18 navy; feed-group 17 rust-brown; "
           "BACKGROUND sections 20 rust-brown; "
           "What-this-is 14 muted; SOTM 13 uppercase")


def check_dashboard_sync_levels(pages, data):
    """WS6b (2026-11-25): the variant's dashboard is the reslice copy
    — domain counts, panel title, strip kickers, and countdown label
    must all match the re-synced data. Expected counts are computed
    from dashboard.json via iter_panel_figures (the same formula the
    renderers use), never hard-coded, so this check fails if the data
    and the render disagree for any reason. H3 + TOC + minimap domain
    rows must all carry the same counts."""
    problems = []
    sit = pages["sitrep"]
    diff = pages["diff"]
    expected = {}
    for s in data.get("slices", []):
        sp = [p for p in data["panels"] if p.get("slice") == s["id"]]
        expected[s["title"]] = sum(
            len(list(bd.iter_panel_figures(p))) for p in sp)
    for label, n in expected.items():
        # H3: `PNL dashboard <span class="section-count">— 13 figures</span>`
        if not re.search(re.escape(label)
                         + r'\s*<span class="section-count">— '
                         + str(n) + r' figures</span>', sit):
            problems.append(f'H3 "{label} — {n} figures" missing')
        # HUD tree row: the same label + count in the row title
        # (the aggregate changed dot now follows the title, inside
        # the row-end mark slot — minimap design pass 2026-11-25).
        if not re.search(r'href="sitrep\.html#slice-[^"]*"[^>]*>'
                         r'<span class="minimap-row-title">'
                         + re.escape(label)
                         + r' — ' + str(n) + r' figures</span>', sit):
            problems.append(f'HUD "{label} — {n} figures" missing')
    # Cert panel title rename. ("The state of the codebase" is ALSO
    # the report §3.1 subsection title, so the stale check must be
    # scoped to the panel heading and its TOC entry, not a bare
    # substring — the section keeps its name.)
    if "Flaws in the codebase — and the fix loop" not in sit:
        problems.append("Cert panel title rename missing")
    if re.search(r'<h3 id="cert" class="dash-panel">'
                 r'The state of the codebase', sit):
        problems.append("old Cert panel heading still present")
    if re.search(r'href="sitrep\.html#cert"[^>]*>'
                 r'<span class="minimap-row-title">'
                 r'The state of the codebase', sit):
        problems.append("old Cert panel title still in HUD tree")
    # Net-impact lede carries the redistribution counts.
    if ("output up — PNL 2; cleanup up — Cert 5 · San 2 · PNL 1"
            not in sit):
        problems.append("net-impact lede redistribution counts missing")
    # The domain kicker is internal bookkeeping only (Yorgo,
    # 2026-11-25 flag n): no strip-kicker span may render. The
    # strip's slice order is guarded by the data-subject check
    # below.
    strip = re.search(r'<div class="bottom-line-strip">(.*?)</div>\s*'
                      r'<h3 id="net-impact"',
                      sit, re.DOTALL)
    if not strip:
        problems.append("bottom-line strip not found")
    else:
        if "strip-kicker" in strip.group(1):
            problems.append(
                "strip kicker rendered — internal bookkeeping "
                "must not reach the reader")
        got_subjects = re.findall(
            r'<div class="tile [^"]*" data-sentiment="[^"]*" '
            r'data-subject="([^"]*)"', strip.group(1))
        expected_subjects = [it["subject"]
                             for it in data.get("bottom_line", [])]
        if got_subjects != expected_subjects:
            problems.append(
                f"strip data-subject {got_subjects} != "
                f"{expected_subjects}")
    # Countdown label (ported from the reslice render; verdicts
    # round, 2026-11-25: the label is the peer H3 now, with the
    # "(PNL §1.4)" qualifier in a section-count span).
    if ('<h3 id="countdown" class="feed-group">Countdown — regulation '
            'deadlines <span class="section-count">(PNL §1.4)</span></h3>'
            not in diff):
        problems.append("countdown label missing on diff")
    if re.search(r'<p class="dash-strip-label">Countdown</p>', diff):
        problems.append("old bare countdown label still present")
    if problems:
        fail("dashboard re-sync (WS6b)", "; ".join(problems))
    else:
        ok("dashboard re-sync (WS6b)",
           "H3/HUD " + " / ".join(
               f"{k.split()[0]} {v}" for k, v in expected.items())
           + "; no strip kickers (internal bookkeeping)"
           + "; Cert title renamed; countdown labelled")


def check_buttons_levels(pages):
    """WS7 + HUD round (2026-11-25): the HUD trigger lives
    bottom-LEFT on phones (the slide-out panel's opener); on
    desktop the HUD is always visible in the sidebar, so the
    trigger is hidden. The back-to-top arrow stays bottom-right
    in rust — opposite corners, different colours, never stacked.
    The old floating minimap close is GONE (the HUD panel closes
    from its head). Mutual exclusion: on phones, opening one
    panel closes the other (OBS-2 fix). Level-switch swap
    (2026-11-25, Yorgo): every page carries SWAP_JS (guard +
    predicate) and the loading-bar CSS, and the modal JS carries
    the swap suppression — asserted on all 13 nav pages. Slim
    sticky bar (2026-11-25, Yorgo: "slim bar"): markup + JS + CSS
    on all 13; the View Manager button only on the three pages
    with a drawer."""
    problems = []
    for name in NAV_PAGES:
        page = pages[name]
        if "@media (min-width: 901px) { #minimap-toggle { display: none; }" not in page:
            problems.append(f"{name}: HUD trigger not hidden on desktop")
        if "#minimap-toggle { left: 16px; bottom: 16px; }" not in page:
            problems.append(f"{name}: HUD trigger not bottom-left (phone)")
        if "bottom: 80px" in page or "bottom: 72px" in page:
            problems.append(f"{name}: stale toggle-above-arrow geometry")
        btt = re.search(r"\.back-to-top \{[^}]*background: ([^;]+);",
                        page)
        if not btt or btt.group(1).strip() != "#b3543f":
            problems.append(f"{name}: back-to-top not rust")
        if "minimap-float-close" in page:
            problems.append(f"{name}: floating minimap close still present")
        if "window.__ciSwap" not in page:
            problems.append(f"{name}: swap JS guard missing")
        if "__ciSwapTarget" not in page:
            problems.append(f"{name}: swap predicate missing")
        if "#ci-swap-bar" not in page:
            problems.append(f"{name}: swap loading-bar CSS missing")
        if "__ciSwapNav" not in page:
            problems.append(f"{name}: modal swap-suppression missing")
        # Slim sticky bar (2026-11-25, Yorgo: "slim bar"): every
        # nav page carries the markup + JS + CSS; the View Manager
        # button rides only where a drawer exists (the three
        # dashboard pages).
        if 'id="slim-bar"' not in page:
            problems.append(f"{name}: slim bar markup missing")
        if "__ciSlimBar" not in page:
            problems.append(f"{name}: slim bar JS missing")
        if ".slim-bar { position: fixed" not in page:
            problems.append(f"{name}: slim bar CSS missing")
        has_slim_btn = 'id="slim-tools-btn"' in page
        if name in ("sitrep", "diff", "landscape") and not has_slim_btn:
            problems.append(f"{name}: slim bar View Manager button "
                            "missing")
        if name not in ("sitrep", "diff", "landscape") and has_slim_btn:
            problems.append(f"{name}: slim bar View Manager button "
                            "without a drawer")
    # Mutual exclusion lives in the JS: openPanel closes the drawer,
    # openTools closes the HUD panel — both through the other panel's
    # public close button (separate IIFEs, so DOM, not a call).
    sit = pages["sitrep"]
    if ("tools-drawer-close" not in sit
            or "document.getElementById('tools-drawer-close')"
            not in sit):
        problems.append("openPanel does not close the Tools drawer")
    if ("document.getElementById('minimap-close')" not in sit):
        problems.append("openTools does not close the HUD panel")
    if problems:
        fail("floating buttons (WS7)", "; ".join(problems))
    else:
        ok("floating buttons (WS7)",
           "HUD trigger phone-only bottom-left + back-to-top rust on "
           "13 pages; float-close gone; mutual exclusion wired both ways; "
           "swap JS + loading bar + modal suppression on all 13; "
           "slim bar on all 13 (View Manager button on the 3 "
           "dashboard pages)")


def main():
    md_path = ROOT / "SYNTHESIZED.md"
    md = md_path.read_text()
    pages = {name: (ROOT / f"{name}.html").read_text()
             for name in ALL_PAGES}
    combined = "".join(pages[n] for n in MAIN_PAGES)
    combined_unescaped = (combined.replace("&lt;", "<")
                          .replace("&gt;", ">").replace("&amp;", "&"))
    data = json.loads((ROOT / "dashboard.json").read_text())

    print(f"Verifying levels variant {md_path} + 4 main pages "
          f"({datetime.now(ZoneInfo('America/New_York')).date()})\n")
    articles = V.check_articles(md)
    V.check_rating_consistency(articles)
    V.check_freshness(md)
    V.check_structure(md)
    check_census(md_path, pages, data)
    check_hierarchy_levels(pages)
    check_dashboard_sync_levels(pages, data)
    check_buttons_levels(pages)
    check_page_order(pages)
    check_nav_levels({n: pages[n] for n in NAV_PAGES})
    check_research_levels(pages)
    check_collapse_levels(pages)
    V.check_changed_dots(md_path, combined)
    V.check_changed_markers(md, md_path, combined)
    V.check_highlight_consistency(md, md_path, combined)
    check_bullet_deep_links_levels(md_path, pages)
    V.check_naming(md, combined_unescaped)
    V.check_hygiene(md, combined)
    V.check_html(combined_unescaped, ROOT)
    V.check_howto_modal(pages["sitrep"])
    check_countdown_modal_levels(pages)
    check_minimap_levels({n: pages[n] for n in NAV_PAGES}, md_path)
    check_xlinks_levels(pages)
    check_toc_levels(pages)
    check_current_levels(pages)
    V.check_glossary(md_path, combined)
    V.check_source_first(md)
    V.check_links(md)

    # Staleness guard for the About page (mirrors verify.py's guard
    # for the single page): site_config.VARIANT_VERIFY_CHECK_COUNT
    # must track this run's pass count, or the About numbers drift
    # (refresh_about.py renders the constant into ABOUT.md). A
    # mismatch is a WARN, not a FAIL — the report is still
    # publishable; the config needs one edit.
    try:
        from site_config import VARIANT_VERIFY_CHECK_COUNT
        n_pass_so_far = sum(1 for r in results if r[0] == "PASS")
        if n_pass_so_far != VARIANT_VERIFY_CHECK_COUNT:
            results.append(("WARN", "verify-count-config",
                            f"site_config.VARIANT_VERIFY_CHECK_COUNT is "
                            f"{VARIANT_VERIFY_CHECK_COUNT} but this run "
                            f"passed {n_pass_so_far} checks — update the "
                            f"config"))
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
        print("BUILD BLOCKED: fix the failures, regenerate, re-run verify_levels.py.")
        return 1
    if n_warn:
        print("No failures. Review each warning before pushing.")
    else:
        print("Clean. Safe to push.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
