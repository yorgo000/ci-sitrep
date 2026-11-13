# Audit — CI Sitrep

A self-audit of this report: how comprehensive it is, how vetted, how solid. Every number on this page is computed from the live report files — nothing here is hand-written, so the audit cannot drift from what it audits.

**As of:** 2026-11-12. **Report last updated:** 2026-11-12.

---

## At a glance

| Measure | Value |
|---|---|
| Articles | 38 |
| Source links (article + subsection) | 101 |
| Total external links (incl. inline prose links) | 187 |
| Unique source URLs | 101 |
| Sections | 3 top-level · 22 subsections · 8 sub-subsections |
| Items new this week | 8 |
| Superseded entries in the archive | 11 |
| Report live since | 2026-11-09 |

---

## Credibility distribution

Every article carries a dots rating for how much confidence a reader can place in its source. The distribution below shows how much of the report rests on strong evidence and how much is still single-source.

| Rating | Meaning | Articles | Share |
|---|---|---|---|
| ●●●● Established | Peer-reviewed and independently confirmed, or a primary regulatory/government document | 9 | 24% |
| ●●●○ Corroborated | Peer-reviewed single study, or a credible primary source confirmed by independent reporting | 11 | 29% |
| ●●○○ Reported | Single credible source, not yet independently verified | 16 | 42% |
| ●○○○ Claimed | Vendor claim without disclosed methodology, or a single uncorroborated report | 2 | 5% |

**53% of articles are Established or Corroborated.** The rest are directional — worth knowing, not yet a basis for a major commitment. When a rating is in doubt, the lower level is assigned.

---

## Source review funnel

The daily watch reviews far more than it publishes. The bar for entry is whether a finding could change how a firm building critical systems in finance should act — routine news, vendor marketing, and minor updates do not qualify.

Tracking began recently; funnel totals will accumulate with each daily run.

| Date | Sources reviewed | Articles added | Articles updated | Notes |
|---|---|---|---|---|
| 2026-11-12 | 0 | 0 | 0 | Tracking begins. Baseline: 38 articles, 101 source links, 187 total external links, 101 unique URLs. Funnel counts start with the next daily run. |

---

## Link health

Every source link on the site is a live link to the source — verified, not assumed.

- **Last full link audit:** 2026-11-12. All 94 unique URLs then live were verified (86 returned HTTP 200; 7 confirmed in a real browser after automated checks failed on bot protection; 1 truncated URL found and fixed).
- **New links:** every new source link is verified live (HTTP 200 or browser render) before publishing. Truncated or guessed URLs are never published.
- **Current unique URLs:** 101 (includes 7 authoritative reference URLs added for inline prose links on 2026-11-12).

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

**Known gaps — things we are watching for that have not arrived yet:**

- The Fed/OCC/FDIC AI request for information, promised April 2026 and still unpublished.
- Replacement third-party-risk guidance (comments due 16 Nov 2026).
- The first independent benchmark of agent-time enforcement tools (the category is ~6 months old; no product has been independently measured at scale).
- Whether NYDFS advisory language hardens into examination expectations for CI-generated code testing.

**How sure are we that we are not missing anything?** Honestly: not certain, and no honest report can claim otherwise. What we can say is that the daily watch runs against the three subjects every morning, the review funnel above shows how much is being looked at, and the known-gaps list is maintained in the open. If a reader finds a material development we have missed, that is a defect in the report — the contact address is [ci-sitrep@confluence1.com](mailto:ci-sitrep@confluence1.com).
