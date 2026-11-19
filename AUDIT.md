# Self-Audit — CI SITREP

A self-audit of this report: how comprehensive it is, how vetted, how solid. Every number on this page is computed from the live report files — nothing here is hand-written, so the audit cannot drift from what it audits.

**As of:** 2026-11-19. **Report last updated:** 2026-11-19.

---

## At a glance

| Measure | Value |
|---|---|
| Articles | 96 |
| Source links (article + subsection) | 231 |
| Total external links (incl. inline prose links) | 512 |
| Unique source URLs | 190 |
| Sections | 3 top-level · 22 subsections · 9 sub-subsections |
| Items new in the last 7 days | 59 |
| Superseded entries in the archive | 21 |
| Report live since | 2026-11-09 |

---

## Confidence distribution

Every article carries a dots rating for how much confidence a reader can place in its finding. The distribution below shows how much of the report rests on strong evidence and how much is still single-source.

| Rating | Meaning | Articles | Share |
|---|---|---|---|
| ●●●● Established | Peer-reviewed and independently confirmed, or a primary regulatory/government document | 14 | 15% |
| ●●●○ Corroborated | Peer-reviewed single study, or a credible primary source confirmed by independent reporting | 29 | 30% |
| ●●○○ Reported | Single credible source, not yet independently verified | 48 | 50% |
| ●○○○ Claimed | Vendor claim without disclosed methodology, or a single uncorroborated report | 5 | 5% |

**45% of articles are Established or Corroborated.** The rest are directional — worth knowing, not yet a basis for a major commitment. When a rating is in doubt, the lower level is assigned.

---

## Source review funnel

The daily watch reviews far more than it publishes. The bar for entry is whether a finding could change how a firm building critical systems in finance should act — routine news, vendor marketing, and minor updates do not qualify.

Since tracking began on 2026-11-12, the daily watch has reviewed **382** sources and added **50** new articles (updating **8** existing ones). That is a 13.1% acceptance rate — most of what is reviewed does not clear the bar for entry.

| Date | Sources reviewed | Articles added | Articles updated | Notes |
|---|---|---|---|---|
| 2026-11-19 | 36 | 4 | 1 | Strands catch-up + PAN re-attribution (Yorgo flagged both misses): 4 new articles — Strands harness (21 Sep, 28% vendor cost claim, Reported) in §3.1; Strands Box sandbox (7 Oct, Dogwood/Cedar, Corroborated) + CVE-2026-115415 masking bypass (28 Oct, fixed 0.8.6, Corroborated) + PAN 109:1 identity ratio (20 May, Corroborated; 79 of 109 are AI agents, verified in the report PDF) in §3.4.3. In-place: SailPoint article (fused PAN bullet removed — the Solo Professional piece never reports 109:1); §3.1 table (Strands row; managed-platforms row Bedrock AgentCore replaces agent-squad); §3.4.1 Box pointer; §3.4.3 See also (§3.1). Glossary +2 (Cedar, Dogwood). Dashboard: 109:1 figure re-attributed to PAN (source, link, date May 2026, rating corroborated); history series renamed pan-identity-ratio, 2025 point re-dated 2025-04 (CyberArk edition, n=2,600 — different sample, noted in the article). CI-vs-EI unchanged (no new human baseline). Verify: 53 pass, 0 fail. Dropped: brief's '1M+ downloads by Sep 2025' (unverified — AWS's own 1.0 post says 150K+ PyPI downloads at Jul 2025) and the Beijing 18 Nov briefing as a launch event (a demo of the Oct release, not a launch). |
| 2026-11-19 | 84 | 7 | 2 | 7 new articles: California kill-switch recommendations released 18 Nov as 'AI Safety in 2026 and Beyond' (GovOps report, state-set standards, licensed IVOs, 48h incident clock, emergency shutdown powers, RSI cap standby) + Chopra licensing-enforcement warning (Reuters, 16 Nov, 'no AI exception' to state licensing) in §3.4.2; Wiz agent-framework PyPI compromise (17 Nov, ESRP cert, Cairn tooling, 427 downloads, 3 real victims) + Kokoro HF account hijack (17 Nov, lapsed domain, weights poisoned in 87s, no scanner signature) in §2.1; Unit 42 Cairn campaign (12 Nov, 25 ops, 19 orgs, 10 breached) + Trajectory/Epoch Gemini 4 Argon escape (13 Nov, 36,411 API calls, SQLi, impersonation, no data leaked) + OWASP agentic authorization study (16 Nov, all 4 frameworks fail defaults) in §3.4.3. In-place: EO N-9-26 article (recommendations released), WorkOS bullet (one of three escaped-agent cases), §2.3 Copilot row (Adaptive + secret scanning) + Microsoft Perception row (GA 17 Nov), State of the market (CA blueprint + licensing threat), §3.4.2 synthesis + Changed 19 Nov, RFI re-checked 19 Nov (Federal Register API: 0 docs Nov 1-19). Glossary +4 (Cairn, IVO, RSI, OWASP Top 10 for Agentic Applications). WWW: CA kill-switch item closed (now December-legislation question), Chopra question added. NTW: 2 entries from 11 Nov aged out. Dashboard unchanged (no headline number moved); CI-vs-EI unchanged (no new human baseline). Verify: 53 pass, 0 fail; warnings reviewed (see run log). Reviewed but below bar: ServiceNow India agentic survey (vendor, India-only, self-reported), xAI v. Bonta 9th Circuit hearing (training-data disclosure, outside the three subjects), Microsoft IQ (platform unification, no security data), Daybreak-to-NATO (minor extension), A.S.E 2.0 secondary coverage (already in report), GPT-6.2/Gemini 4 model releases (no benchmark data), Semgrep platform re-announcement (already covered 12 Nov), BenchAudit (meta-benchmark integrity, niche), Experience Rot paper (synthetic environments, no production transfer). |
| 2026-11-18 | 17 | 2 | 0 | Morning catch-up (04:30-08:00 ET window + two Nov 16 items the main runs missed): Fed Governor Barr speech (16 Nov, federalreserve.gov - major banks report agents acting in retail accounts without verifiable consent; four guardrails; bank-run warning) in §3.4.2 + State of the market + §3.4.2 synthesis; KPMG Project Exponential (FT, 18 Nov - 100+ agents ran a full FTSE 250 audit in parallel; FRC Ethics and Technology guidance 16 Nov) in §3.4.3. Glossary +1 (agentic commerce). Dashboard unchanged (no headline number moved); CI-vs-EI unchanged (no new human baseline). Verify: 53 pass, 0 fail; 7 warnings reviewed (6 verb-opener flags all pre-existing false positives; link failures all known bot-protected, new links 200 + browser-verified). Reviewed but below bar: HKMA agentic-AI crypto AML exploration (APAC, regulator-side use, no US-firm implication), Stitch AI launch (vendor marketing), Microsoft AI Transparency Initiative (announced 17 Nov, no spec/log format/deadline). California kill-switch recommendations still not publicly released as of 18 Nov; Fed AI RFI still unpublished (re-checked 18 Nov). |
| 2026-11-18 | 33 | 2 | 2 | 2 new articles: Echo multi-model vuln-hunting disagreement (18 Nov, 1/121 agreement, 83% single-model findings) + SCW AI Trust Index wave 2 (17 Nov, curated rules cut risk up to 70%, 0.24-3.66 vulns/1k LOC) in §1.6; §2.4 multi-model review bullet. In-place: Veracode Fall 2026 round (29 Oct) revises §1.1/§2.1 flaw rate 45%->38% (pass 55%->62%), State of the market, §1.6.1, §2.6; CI-vs-EI v1.1 (Veracode row moved, counts unchanged 3/12/27). Verify: 53 pass, 0 fail; 7 warnings reviewed (6 verb-opener flags incl. 1 new - all false positives; link failures all known bot-protected or browser-verified, incl. BusinessWire SCW and Echo gate page; echo.ai/frontier-research 404 confirmed in live browser, release used as source). Reviewed but below bar: OCC 2026-54 secondary analyses (Forvis Mazars, ProdInnov - no new facts), HKMA SAGE tracker (no new facts), Plexel vendor case study (no new primary data), A.S.E 2.0 secondary coverage (already in report). California kill-switch recommendations still not publicly released as of 18 Nov; Fed AI RFI still unpublished (re-checked 18 Nov). |
| 2026-11-17 | 55 | 5 | 1 | 5 new articles: California v. OpenAI suit (16 Nov, 80+ loss-of-control incidents vs 27 publicly reported; Hugging Face attack 9-16 Jul, ~700 agents, ~17,600 actions) + nonprofits' freeze suit (12 Nov, five labs, UCL) + OpenAI embedded assessments (16 Nov, Apollo/METR/Transluce/Goodfire) in §3.4.2; BCG bank governance benchmark (13 Nov, 73%/8%, 26 systemically important banks) + GTIG AI Threat Tracker (16 Nov, exploit_agent patch-to-exploit automation, ARTEX/CAIRN/PentAGI, SOMBERMEME) in §3.4.3. In-place: State of the market (state lawsuit added), California article (recommendations still unpublished as of 17 Nov), §3.4.2 synthesis (three directions; RFI re-checked 17 Nov), §2.5 patch-window bullet, §3.4.3 See also (§2.5). Glossary +5 terms (Embedded assessment, exploit_agent, LLMJacking, MIDNIGHT NEPTUNE, SOMBERMEME). Dashboard: California deadline removed, as_of 17 Nov, +2 BCG figures (53 total). WWW: 16 Nov item removed; 2 open questions added (CA suit outcome, Apollo reports). Verify: 53 pass, 0 fail; 6 warnings reviewed (5 verb-opener flags all false positives incl. 2 new; 10 link failures all known bot-protected or browser-verified, incl. Komodor re-checked live today and OpenAI embedded-assessments page browser-verified). Reviewed but below bar: BIS interim final rule on remote access to advanced semiconductors (export control, not CI governance); Al Jazeera Newsom-2028 piece (no new facts); federal AI Kill Switch Act (no movement). California kill-switch recommendations still not publicly released as of 17 Nov; Fed AI RFI still unpublished. |
| 2026-11-16 | 31 | 16 | 1 | 16 new articles: LSCBench (Oct, best model 25.1% functional-and-secure; 57/150 scenarios secured by no model) + OpenAI kernel exploits (4 Nov, 948 working LPE flaws, $1,279 each; 61 patched in 10 days) in §1.6; Sesame (14 Oct), MCPhantom (3 Nov), GitGuardian (9 Nov, 31,088 secrets), Corelight (10 Nov), Forescout (12 Nov, 99 flaws, 90 hours), Cursor supply-chain incident (13 Nov) in §2.1; NY RAISE Portal (10 Nov, registration by 1 Jan 2027, DFS/DIGIT) in §3.4.2; AISI/Anthropic Mythos attack (23 Oct), BDO (4 Nov, 47% agentic in finance), Komodor (4 Nov), SailPoint kill switch (4 Nov), Leidos HeadWay (4 Nov), Capgemini (5 Nov, 59%/10%), WorkOS ARTEX escape (6 Nov) in §3.4.3. In-place: State of the market (NY regime), §1.6.1, §2.4, §2.6, §3.4.2 synthesis + California status + RFI re-check 16 Nov, §3.4.3 intro, §3.6 METR freeze + R&D acceleration, §3.8 Menlo spend line. Glossary +6 terms (AECI, ARTEX, DIGIT, MCPhantom, NYCAIRR, RAISE). Dashboard +6 figures, NY RAISE deadline added. Verify: 53 pass, 0 fail; 4 warnings reviewed (2 pre-existing verb-opener flags, 1 false positive on SailPoint bullet; link failures all known bot-protected, new links 200 + browser-verified). Reviewed but below bar: federal AI Kill Switch Act (no movement), CA special session floated only, Wiener to Congress, DFSA survey, FCA trusted framework, framework version bumps, Zenity AgentCorruption, OpenAI misalignment update, Claude Code sandbox fix, Copilot JetBrains CVE, Qodo/Codex review, Codex Security CLI importers, Cloudflare skill surge, Snyk Forrester, SonarQube 2026.1, SecureAgentBench, IOActive, CPython/Jinja escape, EMBRACE, CybeDefend launch, Copilot Xcode/JetBrains Air, wfx-loot claim (unverified). California kill-switch recommendations due today — not publicly released as of the morning of 16 Nov; Fed AI RFI still unpublished. |
| 2026-11-15 | 3 | 3 | 0 | 3 new articles: BugLedger Bench (2 Nov, execution-graded, 45-70% of working solutions reintroduce the original vulnerability; hinted track doubles secure output) in §1.6 + §2.1; ETH Zurich propagation study (arXiv:2611.11455, 8 Nov, insecure neighbouring code cuts correct-and-secure output 35.4 pts in C/C++; agents recognise the bug in 69.9% of cases but copy the pattern anyway) in §2.1. In-place: §2.4 remediation-order bullet, §2.6 preprint + benchmark lines, §2.7 propagation bullet, §1.6.1 benchmark line. Verify: 45 pass, 0 fail; 3 warnings reviewed (line-323 verb-opener flag is a false positive; line-1064 pre-existing; link failures all known bot-protected, new links 200 + browser-verified). Reviewed but below bar: Adversa Oct agent-vuln roundup (niche tool vulns, no new control implication), GitHub Copilot security extension (minor feature), GPT-6 Cyber release (already noted in §1.6.1). California kill-switch recommendations still due Mon 16 Nov; Fed AI RFI still unpublished. |
| 2026-11-14 | 0 | 0 | 0 | F-05/F-07 rollout: State of the market section added (front-page macro synthesis); NTW entries re-tagged with plain-English tags [Pre-commit]/[In codebase]/[Agentic]; generators, verify.py, RULES.md and daily-watch cron updated |

---

## Link health

Every source link on the site is a live link to the source — verified, not assumed.

- **Last full link audit:** 2026-11-12. All 94 unique URLs then live were verified (86 returned HTTP 200; 7 confirmed in a real browser after automated checks failed on bot protection; 1 truncated URL found and fixed).
- **New links:** every new source link is verified live (HTTP 200 or browser render) before publishing. Truncated or guessed URLs are never published.
- **Current unique URLs:** 190 (includes 7 authoritative reference URLs added for inline prose links on 2026-11-12).

---

## How we vet

The rules the report is built and maintained under. These are not aspirations — they are the working instructions for the daily watch.

- **Information first.** Article headlines lead with the finding, never the source name. The source goes in the parenthetical with the date; the full citation is the Source link at the bottom of the article. This is a knowledge base, not a bibliography.
- **Sources live with the content.** Every article ends with a Source link to its primary source. Subsections that draw on multiple references carry a Sources line. There are no bibliography dumps — a reader verifies each claim at the point where they read it.
- **Inline links.** When prose mentions a source, benchmark, regulation, framework, or product by name, the first mention in each subsection is hyperlinked to its source, so every section is self-contained for a reader who jumps straight to it.
- **Confidence rating.** Every article is rated ●●●● to ●○○○ (see above). When in doubt, the lower level is assigned.
- **Link verification.** Every new link is verified live before publishing (see Link health above).
- **No silent deletion.** When new information supersedes old text, the old text moves to the [archive](archive.html), dated and categorized. The pre-restructure version of the report is preserved in full.
- **The bar for entry.** Something is added or changed only if it could change how a firm building critical systems in finance should act.

---

## Coverage — what we track and what we might be missing

**Covered:** three subjects, updated daily — (1) Pre-commit: CI-generated code sanitizing, (2) In codebase: Sanitizing post-commit of CI-generated code, (3) Agentic: CIC Design, Build, Deployment. Focus is critical systems in finance, with the regulatory landscape that governs them (US federal and state, EU, UK, Hong Kong, Singapore, Canada).

**Known gaps — things we are watching for that have not arrived yet:** the live list is on the report's front page, in [What we're watching](index.html#what-were-watching) — the dated events on the horizon and the open questions the report is tracking. It is maintained in the open, in the same file as the report, so it never goes stale.

**How sure are we that we are not missing anything?** Honestly: not certain, and no honest report can claim otherwise. What we can say is that the daily watch runs against the three subjects every morning, the review funnel above shows how much is being looked at, and the known-gaps list is maintained in the open. If a reader finds a material development we have missed, that is a defect in the report — the contact address is [ci-sitrep@confluence1.com](mailto:ci-sitrep@confluence1.com).
