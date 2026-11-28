"""Shared site configuration for the ci-sitrep generators.

Single source of truth for values every generated page needs, so the
generators cannot drift apart.
"""

# GoatCounter analytics (chosen 2026-11-16, Yorgo). The site code from
# goatcounter.com — the subdomain part of <code>.goatcounter.com.
# None = analytics disabled; no snippet is emitted.
GOATCOUNTER_CODE = "ci-sitrep"

# About page "How this is made" (refresh_about.py): fixed values the audit
# data cannot supply. One edit here updates the paragraph on the next
# publish; the computed numbers come from build_audit.compute_metrics.
ABOUT_CII_COUNT = 6       # CII roles on the team (Barnaby + 3 baseline researchers + daily watch + catch-up)
ABOUT_TEAM_YEARS = 39     # cumulative editing-team experience (9 Bernstein + 30 Confluence<1>)
VERIFY_CHECK_COUNT = 74   # verify.py pass count from the last full run; update when it changes
# Levels variant: verify_levels.py passes 92 checks (2026-11-28) — a
# different bar from the single page (different checks: per-page nav,
# collapse sets, minimap, cross-page links, research). The variant's
# About page states the variant bar; refresh_about.py uses this when
# present. Update when the variant bar changes.
VARIANT_VERIFY_CHECK_COUNT = 92

# Changed-part highlight (2026-11-23): the [new]/[updated] feed tags are
# build-only metadata (parsed for grouping + the marker check, stripped
# before rendering), and the section tags are stripped at build time
# too — the group headings and data-subject attributes carry the
# section. One label list, here — build_html.py (strip), verify.py
# (zero-visible-tags check) and export_findings.py (export strip)
# build their regexes from these, so a new label cannot leak through
# one output while another strips it.
FEED_SECTION_TAGS = ("PNL", "CIC", "Certification", "Pre-commit")
FEED_STATUS_TAGS = ("new", "updated")

# Highlight launch date (2026-11-23): feed entries dated before this
# are exempt from the [new]/[updated] tag requirement (they were
# written before tagging existed — the Nov 16-22 snapshot entries
# predate it). Entries dated on/after it that join to an article must
# carry one of the two tags (verify.py check_highlight_consistency).
# BUMP AT RELEASE: set this to the day AFTER the release date, so
# entries written up to and including release day (untagged, under
# the old cron) stay exempt — the check exempts entry_date <
# HIGHLIGHT_LAUNCH_DATE, so setting it TO the release date would
# still demand tags on release-day entries themselves. A tagged
# pre-launch entry is still validated — a tag is an assertion,
# whatever its date.
# Release round 2026-11-25: bumped 2026-11-25 → 2026-11-26. The
# release content carries five untagged feed entries dated
# 2026-11-25 (release day) that join to new articles; with the
# launch at 2026-11-25 they failed as "post-launch, neither [new]
# nor [updated]". Tagging enforcement therefore starts with
# entries dated 2026-11-26 onward; the watch must emit tags from
# then on. The two [new] entries dated 2026-11-23 (ThinkingBox /
# METR) remain accepted either way ([new] needs no markers).
HIGHLIGHT_LAUNCH_DATE = "2026-11-26"

# The rolling change window (2026-11-23, changed-dot round): "What just
# changed", the changed dot, and the article highlight all mean the same
# 7 days. ONE constant, here — no second window anywhere. The window is
# the FEED's window: the daily watch keeps "DIFF" to entries
# no older than this, and verify.py's check_freshness enforces it on the
# feed itself. The dot/highlight computation (build_html.py
# add_feed_data_attrs, via build_dashboard.match_feed_entry_ids) applies
# the same window to the feed entries it joins, with "today" taken in
# America/New_York explicitly — so the changed set is correct even if
# the build runs under another timezone. check_freshness still hardcodes
# its own 7 (it predates this constant); the two values must stay equal.
CHANGE_WINDOW_DAYS = 7

# Collapse-all semantics (Option A, decided 2026-11-23; RULES.md §4).
# Two declared sets — they deliberately DIFFER under Option A, so they
# are declared separately and checked separately by verify.py
# (check_collapse): a change to either without updating the declaration
# fails the build. No fix round adds an exemption silently: any new
# always-open element or new handler exemption is a product decision,
# recorded in RULES.md, its §7 changelog, and here.
# What starts OPEN on first load: the initial-collapse loop in
# build_html.py must skip exactly these ids and these classes.
COLLAPSE_INITIAL_OPEN_IDS = ("executive-dashboard", "report", "net-impact")
COLLAPSE_INITIAL_OPEN_CLASSES = ("dash-slice",)
# What the Collapse-all handler skips: EMPTY under Option A — the
# button closes every content heading, including the top-level H2s
# and the slices. If a future product decision re-adds an exemption,
# declare it here; the handler must match this set exactly.
# Verdicts round (2026-11-25, Yorgo): the top surface heading on each
# level page (class "surface-heading") is not collapsible — the
# handler skips it, so Collapse all leaves the surface heading open
# (it is the page's title heading, not a section to fold).
COLLAPSE_HANDLER_EXEMPT_IDS = ()
COLLAPSE_HANDLER_EXEMPT_CLASSES = ("surface-heading",)

# Levels-as-pages variant (2026-11-25): the initial-open set is
# per page — each page opens what the single-page build opens,
# restricted to the sections present on that page. The DIFF H2
# starts OPEN on diff.html (a page whose job is "what changed"
# must not open with its answer collapsed); the feed groups and
# the watchlist inside it start collapsed, as before. Landscape
# keeps only its own H2.
# HUD round (2026-11-25, Yorgo): SITREP joins the same pattern —
# the level opens as one uniform list of collapsed headings (The
# bottom line box, Situation at hand, Net impact, the four domain
# dashboards, the panels), with only the surface H2 open; the
# reader opens what they want and navigates by the HUD map. The
# former sitrep exemptions (net-impact + dash-slice open) are
# gone. verify_levels.py checks each page's built JS against its
# declared set here.
COLLAPSE_INITIAL_OPEN_BY_PAGE = {
    "sitrep": {"ids": ("executive-dashboard",),
               "classes": ()},
    "diff": {"ids": ("diff",), "classes": ()},
    "landscape": {"ids": ("report",), "classes": ()},
    # Instruments (2026-11-26): its own H2 starts open; the two
    # sections (Tool suite, Whitepapers) sit collapsed below it,
    # as on Background.
    "instruments": {"ids": ("instruments",), "classes": ()},
    # Background consolidated (round 2): its own H2 starts open; the
    # seven inlined sections sit inside its section-body, collapsed.
    "background": {"ids": ("background",), "classes": ()},
}


def goatcounter_snippet():
    """The GoatCounter <script> tag, or "" when analytics is disabled."""
    if not GOATCOUNTER_CODE:
        return ""
    return (
        f'<script data-goatcounter="https://{GOATCOUNTER_CODE}.goatcounter.com/count" '
        'async src="//gc.zgo.at/count.js"></script>'
    )


# Speed (HUD round WS5, 2026-11-25): prefetch/prerender for the
# cross-page links so the first jump into Landscape/Background is
# instant. Speculation Rules: prerender same-site .html links on
# hover (eagerness "moderate"), prefetch the four main pages
# immediately. Browsers without Speculation Rules get the plain
# <link rel="prefetch"> fallbacks for the same four pages (the
# current page's own prefetch is a no-op — already loaded).
MAIN_PAGES = ("sitrep.html", "diff.html", "landscape.html",
              "instruments.html", "background.html")


def speculation_rules_snippet():
    """The Speculation Rules <script> + prefetch fallbacks, for
    every generated page's <head>."""
    import json as _json
    rules = {
        "prerender": [{"where": {"href_matches": "/*.html"},
                       "eagerness": "moderate"}],
        "prefetch": [{"urls": list(MAIN_PAGES),
                      "eagerness": "immediate"}],
    }
    links = "".join(
        f'<link rel="prefetch" href="{p}">\n' for p in MAIN_PAGES)
    return ('<script type="speculationrules">\n'
            + _json.dumps(rules) + '\n</script>\n' + links)
