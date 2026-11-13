# Audit — CI Sitrep

A self-audit of this report: how comprehensive it is, how vetted, how solid. Every number on this page is computed from the live report files — nothing here is hand-written, so the audit cannot drift from what it audits.

**As of:** 2026-11-13. **Report last updated:** 2026-11-13.

---

## At a glance

| Measure | Value |
|---|---|
| Articles | 50 |
| Source links (article + subsection) | 127 |
| Total external links (incl. inline prose links) | 221 |
| Unique source URLs | 121 |
| Sections | 3 top-level · 22 subsections · 9 sub-subsections |
| Items new this week | 14 |
| Superseded entries in the archive | 12 |
| Report live since | 2026-11-09 |

---

## Credibility distribution

Every article carries a dots rating for how much confidence a reader can place in its source. The distribution below shows how much of the report rests on strong evidence and how much is still single-source.

| Rating | Meaning | Articles | Share |
|---|---|---|---|
| ●●●● Established | Peer-reviewed and independently confirmed, or a primary regulatory/government document | 9 | 18% |
| ●●●○ Corroborated | Peer-reviewed single study, or a credible primary source confirmed by independent reporting | 15 | 30% |
| ●●○○ Reported | Single credible source, not yet independently verified | 24 | 48% |
| ●○○○ Claimed | Vendor claim without disclosed methodology, or a single uncorroborated report | 2 | 4% |

**48% of articles are Established or Corroborated.** The rest are directional — worth knowing, not yet a basis for a major commitment. When a rating is in doubt, the lower level is assigned.

---

## Source review funnel

The daily watch reviews far more than it publishes. The bar for entry is whether a finding could change how a firm building critical systems in finance should act — routine news, vendor marketing, and minor updates do not qualify.

Since tracking began on 2026-11-12, the daily watch has reviewed **27** sources and added **5** new articles (updating **1** existing ones). That is a 18.5% acceptance rate — most of what is reviewed does not clear the bar for entry.

| Date | Sources reviewed | Articles added | Articles updated | Notes |
|---|---|---|---|---|
| 2026-11-13 | 27 | 5 | 1 | 5 new articles: SWE-bench patches study (arXiv:2507.02976 v4), Australia mandatory AI incident reporting, UK CMA/DRCF deployer liability, California EO N-9-26 kill switch, OpenAI Control Room. Updated: Semgrep Layer A row expanded (old row archived); Daybreak + Cycode rows in §2.3; Adversa row in §1.2.1; §3.4.2 summary extended; Fed AI RFI re-checked 13 Nov — still unpublished; TPRM comments due 16 Nov. |
| 2026-11-12 | 0 | 0 | 0 | Tracking begins. Baseline: 38 articles, 101 source links, 187 total external links, 101 unique URLs. Funnel counts start with the next daily run. |

---

## Link health

Every source link on the site is a live link to the source — verified, not assumed.

- **Last full link audit:** 2026-11-12. All 94 unique URLs then live were verified (86 returned HTTP 200; 7 confirmed in a real browser after automated checks failed on bot protection; 1 truncated URL found and fixed).
- **New links:** every new source link is verified live (HTTP 200 or browser render) before publishing. Truncated or guessed URLs are never published.
- **Current unique URLs:** 121 (includes 7 authoritative reference URLs added for inline prose links on 2026-11-12).

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
