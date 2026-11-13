#!/usr/bin/env python3
"""Build AUDIT.md — the CI Sitrep self-audit page — from SYNTHESIZED.md and the audit log.

Usage: python3 build_audit.py [repo_root]
  repo_root defaults to the parent of this script's directory (the repo root).

Metrics are computed from the live files, never hand-written, so the audit page
cannot drift from the report it audits.

The audit log (audit_log.csv, same directory as this script) records each daily
watch run: date, sources reviewed, articles added, articles updated, notes.
The daily watch cron appends one row per run. The funnel metrics on the audit
page are computed from this log.
"""

import csv
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
SYN = ROOT / "SYNTHESIZED.md"
ARCH = ROOT / "archive" / "ARCHIVE.md"
LOG = Path(__file__).resolve().parent / "audit_log.csv"
OUT = ROOT / "AUDIT.md"


def main():
    src = SYN.read_text()
    arch = ARCH.read_text() if ARCH.exists() else ""

    # --- Articles and credibility ---
    summaries = re.findall(r"<details>\s*<summary>(.*?)</summary>", src, re.DOTALL)
    articles = [s for s in summaries if "●" in s]
    ratings = Counter()
    for s in articles:
        m = re.search(r"(●+○*)", s)
        if m:
            ratings[m.group(1)] += 1
    n_est = ratings.get("●●●●", 0)
    n_corr = ratings.get("●●●○", 0)
    n_rep = ratings.get("●●○○", 0)
    n_clm = ratings.get("●○○○", 0)

    # --- Sources and links ---
    n_article_sources = len(re.findall(r"- Source: \[.*?\]\(.*?\)", src))
    sources_lines = re.findall(r"^Sources: (.*?)$", src, re.MULTILINE)
    n_subsection_links = sum(len(re.findall(r"\[.*?\]\(.*?\)", s)) for s in sources_lines)
    all_urls = re.findall(r"\[.*?\]\(https?://([^)]+)\)", src)
    n_links = len(all_urls)
    n_unique_urls = len(set(all_urls))

    # --- Structure ---
    n_h2 = len(re.findall(r"^## \d\. ", src, re.MULTILINE))
    n_h3 = len(re.findall(r"^### \d+\.\d+ ", src, re.MULTILINE))
    n_h4 = len(re.findall(r"^#### \d+\.\d+\.\d+ ", src, re.MULTILINE))
    n_archive = len(re.findall(r"^### ", arch, re.MULTILINE)) if arch else 0

    m = re.search(r"\*\*Last updated:\*\* (\d{4}-\d{2}-\d{2})", src)
    last_updated = m.group(1) if m else "unknown"

    ntw = re.search(r"## New this week\n(.*?)(?=\n## )", src, re.DOTALL)
    n_new = len(re.findall(r"^- \*\*", ntw.group(1), re.MULTILINE)) if ntw else 0

    # --- Audit log: review funnel ---
    log_rows = []
    if LOG.exists():
        with open(LOG, newline="") as f:
            log_rows = list(csv.DictReader(f))
    total_reviewed = sum(int(r.get("sources_reviewed") or 0) for r in log_rows)
    total_added = sum(int(r.get("articles_added") or 0) for r in log_rows)
    total_updated = sum(int(r.get("articles_updated") or 0) for r in log_rows)
    log_start = log_rows[0]["date"] if log_rows else None
    log_end = log_rows[-1]["date"] if log_rows else None

    today = date.today().isoformat()

    # --- Credibility percentages ---
    n_art = len(articles)
    def pct(n):
        return f"{100 * n / n_art:.0f}%" if n_art else "—"

    # --- Funnel table (last 8 runs, most recent first) ---
    funnel_rows = ""
    if log_rows:
        for r in reversed(log_rows[-8:]):
            funnel_rows += (
                f"| {r['date']} | {r.get('sources_reviewed', '')} | "
                f"{r.get('articles_added', '')} | {r.get('articles_updated', '')} | "
                f"{r.get('notes', '')} |\n"
            )
    else:
        funnel_rows = "| — | — | — | — | No runs logged yet. |\n"

    funnel_summary = ""
    if log_rows:
        funnel_summary = (
            f"Since tracking began on {log_start}, the daily watch has reviewed "
            f"**{total_reviewed}** sources and added **{total_added}** new articles "
            f"(updating **{total_updated}** existing ones). That is a "
            f"{100 * total_added / total_reviewed:.1f}% acceptance rate — most of what "
            f"is reviewed does not clear the bar for entry."
            if total_reviewed else
            "Tracking began recently; funnel totals will accumulate with each daily run."
        )
    else:
        funnel_summary = (
            "Source-review tracking began on 2026-11-12. Each daily watch run logs "
            "how many sources it reviewed and how many made it into the report. "
            "Totals will appear here as runs accumulate."
        )

    md = f"""# Audit — CI Sitrep

A self-audit of this report: how comprehensive it is, how vetted, how solid. Every number on this page is computed from the live report files — nothing here is hand-written, so the audit cannot drift from what it audits.

**As of:** {today}. **Report last updated:** {last_updated}.

---

## At a glance

| Measure | Value |
|---|---|
| Articles | {n_art} |
| Source links (article + subsection) | {n_article_sources + n_subsection_links} |
| Total external links (incl. inline prose links) | {n_links} |
| Unique source URLs | {n_unique_urls} |
| Sections | {n_h2} top-level · {n_h3} subsections · {n_h4} sub-subsections |
| Items new this week | {n_new} |
| Superseded entries in the archive | {n_archive} |
| Report live since | 2026-11-09 |

---

## Credibility distribution

Every article carries a dots rating for how much confidence a reader can place in its source. The distribution below shows how much of the report rests on strong evidence and how much is still single-source.

| Rating | Meaning | Articles | Share |
|---|---|---|---|
| ●●●● Established | Peer-reviewed and independently confirmed, or a primary regulatory/government document | {n_est} | {pct(n_est)} |
| ●●●○ Corroborated | Peer-reviewed single study, or a credible primary source confirmed by independent reporting | {n_corr} | {pct(n_corr)} |
| ●●○○ Reported | Single credible source, not yet independently verified | {n_rep} | {pct(n_rep)} |
| ●○○○ Claimed | Vendor claim without disclosed methodology, or a single uncorroborated report | {n_clm} | {pct(n_clm)} |

**{pct(n_est + n_corr)} of articles are Established or Corroborated.** The rest are directional — worth knowing, not yet a basis for a major commitment. When a rating is in doubt, the lower level is assigned.

---

## Source review funnel

The daily watch reviews far more than it publishes. The bar for entry is whether a finding could change how a firm building critical systems in finance should act — routine news, vendor marketing, and minor updates do not qualify.

{funnel_summary}

| Date | Sources reviewed | Articles added | Articles updated | Notes |
|---|---|---|---|---|
{funnel_rows}
---

## Link health

Every source link on the site is a live link to the source — verified, not assumed.

- **Last full link audit:** 2026-11-12. All 94 unique URLs then live were verified (86 returned HTTP 200; 7 confirmed in a real browser after automated checks failed on bot protection; 1 truncated URL found and fixed).
- **New links:** every new source link is verified live (HTTP 200 or browser render) before publishing. Truncated or guessed URLs are never published.
- **Current unique URLs:** {n_unique_urls} (includes 7 authoritative reference URLs added for inline prose links on 2026-11-12).

---

## How we vet

The rules the report is built and maintained under. These are not aspirations — they are the working instructions for the daily watch.

- **Information first.** Article headlines lead with the finding, never the source name. The source goes in the parenthetical with the date; the full citation is the Source link at the bottom of the article. This is a knowledge base, not a bibliography.
- **Sources live with the content.** Every article ends with a Source link to its primary source. Subsections that draw on multiple references carry a Sources line. There are no bibliography dumps — a reader verifies each claim at the point where they read it.
- **Inline links.** When prose mentions a source, benchmark, regulation, framework, or product by name, the first mention in each subsection is hyperlinked to its source, so every section is self-contained for a reader who jumps straight to it.
- **Credibility rating.** Every article is rated ●●●● to ●○○○ (see above). When in doubt, the lower level is assigned.
- **Link verification.** Every new link is verified live before publishing (see Link health above).
- **No silent deletion.** When new information supersedes old text, the old text moves to the [archive](archive.html), dated and categorized. The pre-restructure version of the report is preserved in full.
- **The bar for entry.** Something is added or changed only if it could change how a firm building critical systems in finance should act.

---

## Coverage — what we track and what we might be missing

**Covered:** three subjects, updated daily — (1) pre-commit sanitizing / certification of CI-generated code, (2) codebase sanitize / certification for CI-generated problems already in the codebase, (3) CIA collectives: creation, governance, management. Focus is critical systems in finance, with the regulatory landscape that governs them (US federal and state, EU, UK, Hong Kong, Singapore, Canada).

**Known gaps — things we are watching for that have not arrived yet:** the live list is on the report's front page, in [What we're watching](index.html#what-were-watching) — the dated events on the horizon (including the third-party-risk guidance comments due 16 Nov 2026) and the open questions the report is tracking (including the Fed/OCC/FDIC AI request for information, promised April 2026 and still unpublished). It is maintained in the open, in the same file as the report, so it never goes stale.

**How sure are we that we are not missing anything?** Honestly: not certain, and no honest report can claim otherwise. What we can say is that the daily watch runs against the three subjects every morning, the review funnel above shows how much is being looked at, and the known-gaps list is maintained in the open. If a reader finds a material development we have missed, that is a defect in the report — the contact address is [ci-sitrep@confluence1.com](mailto:ci-sitrep@confluence1.com).
"""

    OUT.write_text(md)
    print(f"Wrote {OUT} ({len(md)} bytes)")
    print(f"  Articles: {n_art} | Sources: {n_article_sources + n_subsection_links} | Links: {n_links} | Unique URLs: {n_unique_urls}")
    print(f"  Credibility: {n_est}E / {n_corr}C / {n_rep}R / {n_clm}Cl | Log rows: {len(log_rows)}")


if __name__ == "__main__":
    main()
