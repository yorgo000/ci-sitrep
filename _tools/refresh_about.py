#!/usr/bin/env python3
"""Refresh the numbers paragraph in ABOUT.md from the computed audit data.

Usage: python3 refresh_about.py [repo_root] [--check]
  repo_root defaults to the parent of this script's directory.
  --check verifies the paragraph is current without writing (exit 1 if stale).

The "How this is made" paragraph on the About page carries numbers that go
stale every morning the watch runs (sources reviewed, findings, acceptance
rate, ...). This script regenerates the paragraph from the same computation
build_audit.py uses for the Self-Audit page, so the two can never drift
apart. The wording is Yorgo's approved text (2026-11-18) — only the numbers
change. The "61 unique domains" clause stays out: it is unverifiable from
audit data and was deliberately dropped.

Pipeline position: after build_audit.py, before build_page.py builds
about.html (RULES.md §6). Fixed values the audit data cannot supply
(check count, CII count, team years) live in site_config.py.
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import site_config
from build_audit import compute_metrics

ANCHOR = "It takes a lot to put together."

# Yorgo's approved wording (2026-11-18) — numbers are placeholders.
# Keep this byte-exact against ABOUT.md: the first run after any wording
# change must be checked by hand before the new text is trusted.
PARAGRAPH = (
    "It takes a lot to put together. Since tracking began on 12 November "
    "we have reviewed {reviewed} sources and kept {kept} of them — a "
    "{acceptance}% acceptance rate. Most of what we review doesn't clear "
    "the bar. The result is {findings} findings, every one confidence-rated "
    "({est_corr}% Established or Corroborated), drawn from {links} source "
    "links, every one verified live. Before anything publishes, it passes "
    "{checks} automated checks. The work is done by {cii} CII's (AI agents) "
    "— research, editing, publishing — working under an editing team with "
    "{years} years of cumulative experience building critical systems for "
    "finance."
)


def render_paragraph(metrics):
    """Fill the template from computed metrics + site_config fixed values."""
    if metrics["acceptance_rate"] is None:
        raise ValueError("audit log is empty — no acceptance rate to publish")
    return PARAGRAPH.format(
        reviewed=metrics["total_reviewed"],
        kept=metrics["total_added"],
        acceptance=metrics["acceptance_rate"],
        findings=metrics["n_articles"],
        est_corr=metrics["est_corr_pct"],
        links=metrics["n_source_links"],
        checks=site_config.VERIFY_CHECK_COUNT,
        cii=site_config.ABOUT_CII_COUNT,
        years=site_config.ABOUT_TEAM_YEARS,
    )


def replace_paragraph(text, paragraph):
    """Replace the numbers paragraph (the block starting with ANCHOR) with
    the regenerated single-line paragraph. Fails loudly unless exactly one
    such block exists, so a reworded About page never silently keeps stale
    numbers."""
    lines = text.split("\n")
    hits = [i for i, ln in enumerate(lines) if ln.startswith(ANCHOR)]
    if len(hits) != 1:
        raise ValueError(
            f"expected exactly 1 paragraph starting with {ANCHOR!r}, "
            f"found {len(hits)}"
        )
    start = hits[0]
    end = start
    while end < len(lines) and lines[end].strip() != "":
        end += 1
    new_lines = lines[:start] + [paragraph] + lines[end:]
    return "\n".join(new_lines)


def main(argv):
    args = [a for a in argv[1:] if a != "--check"]
    check_only = "--check" in argv[1:]
    root = Path(args[0]) if args else HERE.parent
    about_path = root / "ABOUT.md"
    metrics = compute_metrics(root)
    paragraph = render_paragraph(metrics)
    summary = (
        f"{metrics['total_reviewed']} sources, {metrics['total_added']} kept, "
        f"{metrics['acceptance_rate']}%, {metrics['n_articles']} findings, "
        f"{metrics['est_corr_pct']}% E/C, {metrics['n_source_links']} links, "
        f"{metrics['n_est']}E/{metrics['n_corr']}C"
    )
    text = about_path.read_text(encoding="utf-8")
    try:
        new_text = replace_paragraph(text, paragraph)
    except ValueError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        return 1
    if new_text == text:
        print(f"ABOUT.md numbers already current ({summary}).")
        return 0
    if check_only:
        print(f"ABOUT.md numbers are stale (computed: {summary}).", file=sys.stderr)
        return 1
    about_path.write_text(new_text, encoding="utf-8")
    print(f"Refreshed ABOUT.md ({summary}).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
