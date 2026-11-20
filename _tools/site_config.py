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
VERIFY_CHECK_COUNT = 54   # verify.py pass count from the last full run; update when it changes


def goatcounter_snippet():
    """The GoatCounter <script> tag, or "" when analytics is disabled."""
    if not GOATCOUNTER_CODE:
        return ""
    return (
        f'<script data-goatcounter="https://{GOATCOUNTER_CODE}.goatcounter.com/count" '
        'async src="//gc.zgo.at/count.js"></script>'
    )
