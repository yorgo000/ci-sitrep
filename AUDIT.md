# Self-Audit — CI Sitrep

A self-audit of this report: how comprehensive it is, how vetted, how solid. Every number on this page is computed from the live report files — nothing here is hand-written, so the audit cannot drift from what it audits.

**As of:** 2026-11-14. **Report last updated:** 2026-11-14.

---

## At a glance

| Measure | Value |
|---|---|
| Articles | 56 |
| Source links (article + subsection) | 144 |
| Total external links (incl. inline prose links) | 330 |
| Unique source URLs | 134 |
| Sections | 3 top-level · 22 subsections · 9 sub-subsections |
| Items new this week | 21 |
| Superseded entries in the archive | 12 |
| Report live since | 2026-11-09 |

---

## Credibility distribution

Every article carries a dots rating for how much confidence a reader can place in its source. The distribution below shows how much of the report rests on strong evidence and how much is still single-source.

| Rating | Meaning | Articles | Share |
|---|---|---|---|
| ●●●● Established | Peer-reviewed and independently confirmed, or a primary regulatory/government document | 11 | 20% |
| ●●●○ Corroborated | Peer-reviewed single study, or a credible primary source confirmed by independent reporting | 16 | 29% |
| ●●○○ Reported | Single credible source, not yet independently verified | 27 | 48% |
| ●○○○ Claimed | Vendor claim without disclosed methodology, or a single uncorroborated report | 2 | 4% |

**48% of articles are Established or Corroborated.** The rest are directional — worth knowing, not yet a basis for a major commitment. When a rating is in doubt, the lower level is assigned.

---

## Source review funnel

The daily watch reviews far more than it publishes. The bar for entry is whether a finding could change how a firm building critical systems in finance should act — routine news, vendor marketing, and minor updates do not qualify.

Since tracking began on 2026-11-12, the daily watch has reviewed **123** sources and added **11** new articles (updating **1** existing ones). That is a 8.9% acceptance rate — most of what is reviewed does not clear the bar for entry.

| Date | Sources reviewed | Articles added | Articles updated | Notes |
|---|---|---|---|---|
| 2026-11-14 | 91 | 6 | 0 | 6 new articles: CrowdStrike AI Kill Switch (3 Nov, gateway-first stop; Fiddler/Dreadnode acquisitions), VulnCheck Glasswing audit (9 Nov, 37966 findings vs 217 fixed), FCA Wholesale Banks Supervision Insights 3 (2 Nov, AI code passed human review, untested kill switches), Canadian banks block third-party agents (28 Oct, RBC/TD/BMO/CIBC/Scotiabank), FCA CP26/38 Financial Crime Guide (23 Oct, comments due 24 Dec), BoE/FCA 2026 AI survey (26 Oct, 86% use AI, 80% agents, 2% broad autonomy). In-place: OSFI E-23 effective 1 May 2027 (WWW + §2.5), FCA agentic-finance framework open question (WWW), §2.5 human-review + §2.7 Glasswing bullets, §1.6.1 Anthropic TP-rate line, §3.4.2 synthesis sentence, §3.8 BoE/FCA verified line. Verify: 31 pass, 0 fail; 2 warnings reviewed (source-first flag is a false positive; link failures all known bot-protected or browser-verified, incl. FII 403). Reviewed but below bar: Cohere AISLE/cubic acquisitions (no product yet), KPMG AI Threat Management (services launch), OpenAI Codex Security CLI importers (minor), Multimodal-SEA preprint (consumer-fraud angle), CWE-bench arXiv paper (0.8pp version noise vs existing article), Reuters banks-AI-questions story (second-hand, Oct). California kill-switch recommendations still due Mon 16 Nov; Fed AI RFI still unpublished. |
| 2026-11-13 | 2 | 0 | 0 | Evening verification pass: verify.py built and first-run (31 checks pass, 0 failures); content-order fixes (New this week now strict newest-first, Australia/UK entry re-dated 2026-11-10 -> 2026-11-13 as added that day; What we're watching now soonest-first); Kiteworks headline linked to LobeHub (figures confirmed in the article); 12 curl-blocked links browser-checked, all live. |
| 2026-11-13 | 1 | 0 | 0 | Evening editorial pass: information-first rewrite of 55 source-first segments (bullets, prose, New-this-week titles) + source hyperlinked in 48 of 50 article headlines; Google 75% figure now linked to Pichai Cloud Next 2026 post (verified 200). |
| 2026-11-13 | 2 | 0 | 0 | Evening update: TPRM comment period extended to 16 Dec 2026 (OCC News Release 2026-100; OCC Bulletin 2026-57) - 6 date mentions corrected, New-this-week entry added. California kill-switch recommendations still due 16 Nov (not extended). |
| 2026-11-13 | 27 | 5 | 1 | 5 new articles: SWE-bench patches study (arXiv:2507.02976 v4), Australia mandatory AI incident reporting, UK CMA/DRCF deployer liability, California EO N-9-26 kill switch, OpenAI Control Room. Updated: Semgrep Layer A row expanded (old row archived); Daybreak + Cycode rows in §2.3; Adversa row in §1.2.1; §3.4.2 summary extended; Fed AI RFI re-checked 13 Nov — still unpublished; TPRM comments due 16 Nov. |
| 2026-11-12 | 0 | 0 | 0 | Tracking begins. Baseline: 38 articles, 101 source links, 187 total external links, 101 unique URLs. Funnel counts start with the next daily run. |

---

## Link health

Every source link on the site is a live link to the source — verified, not assumed.

- **Last full link audit:** 2026-11-12. All 94 unique URLs then live were verified (86 returned HTTP 200; 7 confirmed in a real browser after automated checks failed on bot protection; 1 truncated URL found and fixed).
- **New links:** every new source link is verified live (HTTP 200 or browser render) before publishing. Truncated or guessed URLs are never published.
- **Current unique URLs:** 134 (includes 7 authoritative reference URLs added for inline prose links on 2026-11-12).

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

**Covered:** three subjects, updated daily — (1) Pre-commit: CI-generated code sanitizing, (2) In codebase: Sanitizing post-commit of CI-generated code, (3) Agentic: CIAC Design, Build, Deployment. Focus is critical systems in finance, with the regulatory landscape that governs them (US federal and state, EU, UK, Hong Kong, Singapore, Canada).

**Known gaps — things we are watching for that have not arrived yet:** the live list is on the report's front page, in [What we're watching](index.html#what-were-watching) — the dated events on the horizon and the open questions the report is tracking. It is maintained in the open, in the same file as the report, so it never goes stale.

**How sure are we that we are not missing anything?** Honestly: not certain, and no honest report can claim otherwise. What we can say is that the daily watch runs against the three subjects every morning, the review funnel above shows how much is being looked at, and the known-gaps list is maintained in the open. If a reader finds a material development we have missed, that is a defect in the report — the contact address is [ci-sitrep@confluence1.com](mailto:ci-sitrep@confluence1.com).
