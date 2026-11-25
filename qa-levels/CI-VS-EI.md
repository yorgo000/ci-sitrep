# CI vs EI

**As of Wednesday, November 18, 2026 · Version 1.1**

Every CI figure in the Landscape, set against its human equivalent — [EI, evolved intelligence](glossary.html#ei) — where one exists, and marked plainly where none does. A benchmark score on its own tells an executive nothing: 74.0 on one benchmark, 25.1% on another — good or bad? The answer only exists against the human baseline for the same task.

A comparison counts only on the same task with the same metric, with the baseline population stated. A CI number from one study set against a human number from another is not a comparison. As of this edition: **3 complete pairs, 12 partial comparisons, 27 gaps**, across 42 classified items. Operations has no complete pair at all — every agent-reliability figure in the Landscape is measured against the task, never against a human doing the same task.

The strongest pair: AI patches introduce **135** confirmed vulnerabilities against **12** for developers on the same issues (Sajadi, preprint). The largest gap: no benchmark in the Landscape measures a human reviewer against the same commits the agentic reviewers were tested on — so the 32.5–78.1% recall range has nothing to be judged against.

CI figures read in rust, human figures in navy — the same colours as SITREP. Every row links to the article in the Landscape that evidences it; the article's Source line takes you to the primary source. Rows are ordered: complete pairs first, then partial comparisons, then figures with no human baseline published.

## Development

Two gaps carry a trap: SecureVibeBench and BugLedger build their tasks from cases where a human *did* introduce a vulnerability — that is how the tasks were selected, so reading them as "humans 0% secure" would be a misuse. The human rate on those tasks was never measured as a control group.

### Complete pairs

| Parameter | CI | EI (human) | Evidence |
|---|---|---|---|
| Vulnerabilities in patches | **135** manually confirmed vulnerabilities (Llama 3.3, SWE-bench train+test) | **12** in developer patches for the same issues | [Sajadi et al. §4.5](index.html#ai-generated-patches-introduce-11-the-vulnerabilities-of) · 1 Nov 2026 · preprint · ●●○○ Reported |
| Vulnerabilities in patches, newer model | **3** vulnerabilities (GPT-5.4 nano, test set) | **2** in developer patches for the same issues | [Sajadi et al. §4.5](index.html#ai-generated-patches-introduce-11-the-vulnerabilities-of) · 1 Nov 2026 · preprint · ●●○○ Reported |
| Vulnerability rate, equivalent tasks | **up to 2.74×** the vulnerabilities of human code (maximum across categories); 1.7× more major issues | **1×** baseline (human-written code, 150 of 470 PRs) | [CodeRabbit §4.1](index.html#ai-code-carries-up-to-274-the-vulnerabilities-of-human-code) · Dec 2025 · vendor's own analysis · ●○○○ Claimed |

### Partial comparisons

| Parameter | CI | EI (human) | Evidence |
|---|---|---|---|
| Commit speed | AI-assisted developers commit **3–4×** faster | Unassisted developers (implied) — method undisclosed, a rate, not same-task time | [Apiiro / CSA §3.1](index.html#volume-compounds-it-apiiro-csa-apr-2026-enterprise) · Apr 2026 · vendor telemetry · ●●○○ Reported |
| Privilege-escalation paths | **+322%** in AI-assisted repos; +153% architectural flaws | Non-AI repos in the same telemetry — populations not matched on task, size, or age | [Apiiro §3.1](index.html#322-more-privilege-escalation-paths-in-ai-assisted-repos) · 2026 · vendor study · ●●○○ Reported |
| Vulnerability trend | Mean **581** vulnerabilities per codebase, **+107%** year-on-year | 2025 codebases (~281) — a time-series, not a matched comparison; the AI attribution is the vendor's | [Black Duck OSSRA §3.1](index.html#mean-vulnerabilities-per-codebase-581-up-107-year-on-year) · 2026 · 947 codebases · ●●●○ Corroborated |
| Maintainability | Moved code **21% → 3.8%** of changed lines; duplicate blocks **+81%**; two-week churn **+15%** | 2022 commit history (human-era) vs 2023–26 (AI-era) — a time-series, not same-task | [GitClear §3.1](index.html#ai-code-has-a-maintainability-gap-gitclear-jan-2026-623m) · Jan 2026 · 623M code changes · ●●○○ Reported |
| Verification tax | Every +25% AI adoption cost **−1.5%** throughput and **−7.2%** delivery stability (2024) | Lower-adoption teams — correlational survey, compares adoption levels, not same-task performance | [Google DORA §1.2](index.html#ai-code-imposes-a-verification-tax-on-reviewers-google-dora) · 2024–2026 · ●●●○ Corroborated |
| Audit time | Embedded-stack audit: **90 hours** | **9 months** (same team's prior audit) — but not a controlled benchmark: different target sets, and the AI run rediscovered only 40% of the flaws the human audit had disclosed | [Forescout §3.1](index.html#ai-cut-an-embedded-stack-audit-from-nine-months-to-90-hours) · 12 Nov 2026 · ●●○○ Reported |
| Dose-response | Organisations at 81–100% AI-generated code ship vulnerable code at **3.4×** the rate of those at 1–20% | Organisations at 1–20% AI code — different organisations, not the same task | [SusVibes §4.5](index.html#a-post-hoc-review-lifts-working-and-secure-to-4756-at-25) · 2 Nov 2026 · vendor-commissioned · ●●○○ Reported |

### Gaps

| Parameter | CI | EI (human) | Evidence |
|---|---|---|---|
| Error rate | **~38%** of AI code introduces a known flaw (62% security pass rate; first movement in the series, from 56% in July 2026) | *No human baseline published* | [Veracode §3.1](index.html#38-of-ai-code-introduces-a-known-security-flaw-veracode) · Fall 2026 · ●●●○ Corroborated |
| Hallucinated packages | **19.7%** of package references name packages that don't exist | *No human baseline published* | [Spracklen et al. §4.1](index.html#20-of-package-references-are-hallucinated-spracklen-et-al) · USENIX Security 2025 · ●●●○ Corroborated |
| Error rate, base rates | **~40%** of Copilot programs vulnerable in high-risk scenarios; **29.5%** Python / **24.2%** JS AI-assisted snippets with weaknesses | *No human baseline published* | [Tenzai §4.1](index.html#the-failure-mode-moved-up-the-stack-tenzai-dec-2025-5-tools) · Dec 2025 · ●●○○ Reported |
| Correct-and-secure | Best agent–model pair **23.8%** correct-and-secure; **23.0%** correct but exploitable | *No human baseline published* — see the selection-trap note above | [SecureVibeBench §4.5](index.html#best-agent-238-correct-and-secure-23-correct-but) · ACL 2026 · ●●●○ Corroborated |
| Correct-and-secure | Claude Code **74.0%** functional pass, **18.4%** secure; **55.6%** passed every test while a working exploit succeeded | *No human baseline published* | [A.S.E 2.0 §4.5](index.html#556-passed-every-test-while-a-working-exploit-succeeded-ase) · 4 Nov 2026 · preprint · ●●○○ Reported |
| Correct-and-secure | Best model **25.1%** functional-and-secure on 450 tasks, 7 languages | *No human baseline published* | [LSCBench §4.5](index.html#best-agent-writes-working-and-secure-code-on-only-251-of) · Oct 2026 · preprint · ●●○○ Reported |
| Vulnerability reintroduction | **45–70%** of working agent solutions reintroduce the original vulnerability | *No human baseline published* — see the selection-trap note above | [BugLedger §4.5](index.html#4570-of-working-agent-solutions-bring-the-original) · 2 Nov 2026 · ●●○○ Reported |
| Flaw propagation | Insecure neighbouring code cuts correct-and-secure output by **35.4 points** on average in C/C++ | *No human baseline published* | [Sun et al. §3.5](index.html#agents-copy-the-flaws-already-in-a-codebase-insecure-code) · 8 Nov 2026 · preprint · ●●○○ Reported |
| Remediation accuracy | Leading remediation agents **~68%** pass@1; the leader fails 19% of tasks on every attempt | *No human baseline published* | [CWE-bench v2 §3.5](index.html#remediation-agents-now-have-a-public-yardstick-cwe-bench-v2) · 3 Nov 2026 · ●●○○ Reported |
| Review recall | Agentic pre-merge review recall **32.5–78.1%** across eight frontier models | *No human baseline published* — human reviewers are the incumbent control, and their miss rate on the same 265 commits is unpublished | [SecPRBench §4.5](index.html#best-agentic-reviewers-catch-3-in-4-vuln-introducing) · 24 Oct 2026 · preprint · ●●○○ Reported |
| Vulnerabilities per codebase | **15** confirmed vulnerabilities per AI-generated codebase, 4.3 severe | *No human baseline published* | [Secure Code Warrior §3.1](index.html#15-confirmed-vulnerabilities-per-codebase-43-severe-secure) · Jul 2026 · ●●○○ Reported |
| Flaws in AI-built apps | **2,038** critical vulnerabilities in 5,600+ publicly deployed AI-built apps | *No human baseline published* | [Escape.tech §3.1](index.html#2038-critical-vulnerabilities-in-5600-publicly-deployed-ai) · 2026 · vendor research · ●●○○ Reported |
| CVEs attributed to AI tools | **74** CVEs traced directly to AI coding tools | *No human baseline published* | [Georgia Tech §3.1](index.html#74-cves-traced-directly-to-ai-coding-tools-georgia-tech) · Sep 2026 · ●●○○ Reported |
| Patch-to-exploit speed | Working exploits generated **within a day** of disclosure (PaperCut zero-days, Aug 2026) | *No human baseline published* | [Google Threat Intelligence Group §2.6](index.html#attackers-now-turn-patches-into-working-exploits-with-no) · 16 Nov 2026 · ●●○○ Reported |
| Documentation quality | *No figure* — nothing in the Landscape measures documentation quality of CI vs EI code | *No human baseline published* | No source — no figure published |
| Test quality | *No figure* — nothing compares test quality (coverage, mutation score) of CI-written vs human-written tests | *No human baseline published* | No source — no figure published |
| Architectural foresight | *No figure* — nothing measures it | *No human baseline published* | No source — no figure published |

## Operations

### Complete pairs

No complete pair yet. Every agent-reliability figure in the Landscape is measured against the task, never against a human doing the same task.

### Partial comparisons

| Parameter | CI | EI (human) | Evidence |
|---|---|---|---|
| Task time horizon | 50%-reliability horizon doubles **~every 7 months**; the 80% horizon is far shorter; measurements above 16h flagged unreliable | Human time is the yardstick for task length (an "X-hour task" is X hours of human work) — but no human success rate on the same tasks is published as a control | [METR §2.7](index.html#27-evaluation) · 2026 · public tracker frozen (last model added 8 May) · ●●●○ Corroborated |
| R&D acceleration | Capability improving **~1.9×** the Mar 2024–Oct 2025 rate (95% CI 1.5–2.8×), ~80% of the acceleration judged attributable to AI doing R&D | The Mar 2024–Oct 2025 rate (mostly human R&D) — a time-series rate comparison; the ~80% attribution is METR's judgment, not a measurement | [METR §2.7](index.html#27-evaluation) · 5 Nov 2026 · 11 weeks inside Anthropic · ●●○○ Reported |

### Gaps

| Parameter | CI | EI (human) | Evidence |
|---|---|---|---|
| Reliability (pass^k) | ThinkingBox: Claude Opus 5.5 pass@1 **67.16%**, yet only **241 of 507** workflows pass on all 20 attempts; **67.24%** of failures terminate cleanly, then report done | *No human baseline published* | [ThinkingBox §2.7](index.html#27-evaluation) · Oct 2026 · ●●●○ Corroborated |
| Reliability (pass^k) | tau-bench: GPT-4o pass^8 **below 25%** on retail despite a much higher pass@1 | *No human baseline published* | [§2.7](index.html#27-evaluation) · prose, not an article — no rating |
| Framework failure rate | Failure rates of **41%–86.7%** across seven popular frameworks | *No human baseline published* | [MAST §2.3](index.html#23-orchestration-patterns) · reported via a Medium technical report, not independently verified |
| Self-reported completion | **Half** of self-asserted "PASS" fix claims fail independent mechanical verification | *No human baseline published* | [§2.7](index.html#27-evaluation) · 2026 digest, reported, not independently verified |
| Incident rate | **188** documented cases of autonomous AI damaging production systems, no attacker involved (late 2023–mid-2026) | *No human baseline published* | [Cyera §2.6](index.html#188-documented-cases-of-autonomous-ai-damaging-production) · 2023–mid-2026 · ●●○○ Reported |
| Incident rate | **46%** of systemically important banks reported an AI-related issue or incident in the past 12 months | *No human baseline published* | [BCG §2.6](index.html#73-of-systemically-important-banks-permit-agents-in) · 13 Nov 2026 · 26 banks · ●●○○ Reported |
| Detection time | WorkOS: a benchmark agent's bulk extraction ran **5 days** before detection | *No human baseline published* | [WorkOS §2.6](index.html#a-benchmark-agent-escaped-its-sandbox-and-pulled-customer) · 6 Nov 2026 · ●●●○ Corroborated |
| Escalation rate | *No figure* — nothing measures how often agents escalate to humans vs how often humans escalate on the same work | *No human baseline published* | No source — no figure published |
| Oversight cost per agent-hour | *No figure* — nothing prices the human oversight an agent-hour consumes | *No human baseline published* | No source — no figure published |

## Business-composite

### Complete pairs

No complete pair yet. The composite the page exists to answer — total risk-adjusted cost per outcome, both sides, same task — has no figure on either side.

### Partial comparisons

| Parameter | CI | EI (human) | Evidence |
|---|---|---|---|
| Review cost | A post-hoc security review lifts working-and-secure output to 47–56% at **~2.5×** the cost of generation alone | The human is the intervention (the review), not a baseline for generation — and the review still leaves about half of tasks insecure | [SusVibes re-run §4.5](index.html#a-post-hoc-review-lifts-working-and-secure-to-4756-at-25) · 2 Nov 2026 · vendor-commissioned · ●●○○ Reported |
| Cost per flaw found | One agent pipeline: 948 working Linux kernel exploits at **~$1,279** per flaw, $1.21M end-to-end | *No human cost per flaw published* — and the fix loop lags by an order of magnitude (61 patched in 10 days), its cost unpriced | [OpenAI §3.1](index.html#one-agent-pipeline-produced-948-working-linux-kernel-root) · 4 Nov 2026 · ●●○○ Reported |
| Cost per finding | Embedded-stack audit: 99 validated flaws for $935 in model spend, **$2.58** per finding | *No human cost per finding published* — and the $935 is the marginal cost of running a finished harness, not of building it | [Forescout §3.1](index.html#ai-cut-an-embedded-stack-audit-from-nine-months-to-90-hours) · 12 Nov 2026 · ●●○○ Reported |

### Gaps

| Parameter | CI | EI (human) | Evidence |
|---|---|---|---|
| Total risk-adjusted cost per outcome | *No figure* — SITREP's money panel states it honestly: no credible dollar figure exists yet for money saved or lost to AI code and agents | *No human baseline published* | No source — no figure published |

## Changes

- **v1.0 — 17 Nov 2026.** First edition: 3 complete pairs, 12 partial comparisons, 27 gaps, across 42 classified items. Baseline for movement.
- **v1.1 — 18 Nov 2026.** Veracode error rate moved: ~45% → ~38% of AI code introduces a known flaw (security pass rate 55% → 62%, first movement in the series); still a gap — no human baseline published. Counts unchanged: 3 pairs / 12 partials / 27 gaps.
- When a figure moves, the change is logged here with the old and new values, and the pair's row is updated.
