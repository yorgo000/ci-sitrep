# Synthesized — Archive

Superseded text from the knowledge base, dated and categorized by subject. Nothing here is deleted from the record — it is kept so that an earlier claim can be traced. The current picture lives in [SYNTHESIZED.md](../SYNTHESIZED.md).

The original version of the report (9 November 2026, plus the 10 and 11 November updates) is preserved at [SYNTHESIZED-2026-11-11-append-only.md](SYNTHESIZED-2026-11-11-append-only.md).

---

## Subject 1 — Pre-commit scanning

### 2026-11-10 — CodeMender "not publicly available" (superseded)

- **Old claim (original report, 2026-11-09, Layer C table):** "Google DeepMind CodeMender — Fix-only agent — **Not publicly available**."
- **Superseded by:** CodeMender has in fact been in public preview since July 2026 (hundreds of customers, per Google), and the 5 Nov 2026 Security Summit update added vulnerability verification and exploit simulation inside an OS-level sandbox or isolated VM, human-in-the-loop checks for local writes and command execution, and scoped scans. Current entry lives in [SYNTHESIZED.md §1.2.3](../SYNTHESIZED.md#122-layer-b--pr--ci-gates-acts-at-pull-request-or-pipeline--the-established-market).

### 2026-11-10 — "No federal model-risk umbrella" as the whole picture (partially superseded)

- **Old claim (original report, 2026-11-09, §1.5.2):** "Practical consequence: **there is currently no federal model-risk umbrella for AI coding tools** — firms must build their own controls."
- **Superseded in part by:** OCC Bulletin 2026-54 (4 Nov 2026), a 20-page examiner resource covering exactly the generative and agentic systems SR 26-2 excluded, with sixteen components in six pillars and a four-tier consequence classification. It sets no enforceable standards, so the "no umbrella as law" part still holds — but it no longer holds as examination practice. Current entry lives in [SYNTHESIZED.md §1.5.2](../SYNTHESIZED.md#152-provenance-audit-trail-and-regulation).

### 2026-11-11 — "No independent benchmark of agent-time enforcement tools" (partially superseded)

- **Old claim (original report, 2026-11-09, §1.7):** "First independent benchmark of agent-time enforcement tools (none exists yet — the category is ~6 months old)."
- **Superseded in part by:** CWE-bench v2 (Collinear AI, 3 Nov 2026) — a public, programmatically scored benchmark of 100 tasks (91 CWE classes) for agents finding and fixing security flaws, with 11 models evaluated. It is a yardstick for remediation agents; no agent-time enforcement product has yet been independently measured against it at scale, so the gap is narrowed, not closed. Current entry lives in [SYNTHESIZED.md §1.6](../SYNTHESIZED.md#16-benchmarks--evidence) and [§1.7](../SYNTHESIZED.md#17-open-gaps--watch-items).

### 2026-11-12 — "No yardstick for LLM reviewer precision/recall" (partially superseded)

- **Old claim (§1.7):** "Precision/recall of LLM reviewers on real PRs at scale." — listed as an open gap with no yardstick.
- **Superseded in part by:** SecPRBench (Yang et al., arXiv:2610.33509, 24 Oct 2026) — the first benchmark of agentic pre-merge security review on validated real bug-introducing commits: 265 tasks from nine critical systems, recall 32.5–78.1% across eight frontier models, 68% of misses wrong-mechanism rather than oversights. No commercial review product has yet been independently measured against it at scale, so the gap is narrowed, not closed. Current entry lives in [SYNTHESIZED.md §1.6](../SYNTHESIZED.md#16-benchmarks--evidence), [§1.7](../SYNTHESIZED.md#17-open-gaps--watch-items) and [§2.1](../SYNTHESIZED.md#21-how-big-the-problem-is).

### 2026-11-13 — Semgrep Layer A row (expanded)

- **Old text (2026-11-09, §1.2.1 Layer A table):** "Semgrep (agent hooks) — Custom-rule SAST in the agent loop; Semgrep Assistant AI triage."
- **Superseded by:** Semgrep Agentic AppSec Platform (announced 12 Nov 2026): Guardian fixes issues as agents write, before commit; Mandoline program-analysis engine returns only reachable code paths to agents; Agentic Security Workflows; MCP server; integration with OpenAI Codex Security / Daybreak Defense Factory. Vendor-claimed: agents found 2× more real vulnerabilities than frontier models alone, −65% token costs (method undisclosed). Current entry lives in [SYNTHESIZED.md §1.2](../SYNTHESIZED.md#12-product-landscape).

### 2026-11-16 — OpenAI 948 kernel exploits (one-liner → full article)

- **Old text (§1.6.1 vendor-claims list):** "OpenAI's GPT-6 Cyber 48.45% intended-exploit success on ExploitGym and "948 Linux kernel privilege-escalation bugs validated" (vendor system card / research run, Nov 2026);"
- **Superseded by:** a full article in §1.6 (OpenAI, 4 Nov 2026): 2,308 candidates → 948 distinct LPE flaws with candidate patches, ~$1,279 per flaw; 61 patched upstream in ten days. The one-liner now points to the article. Current entry lives in [SYNTHESIZED.md §1.6](../SYNTHESIZED.md#16-benchmarks--evidence).

### 2026-11-18 — Veracode "~45% flaw rate" (Spring 2026 round superseded)

- **Old text (§1.1):** "~45% of AI code introduces a known security flaw (Veracode, Spring 2026, longitudinal benchmark)" — security pass rate ~55%, essentially flat for two years; best models 70–72%; XSS 15% pass, log injection 13%; Java 29%.
- **Superseded by:** Veracode Fall 2026 round (29 Oct 2026) — average pass rate 62% (up from 56% in July), flaw rate ~38%, best models tied at 73% (Claude Opus 5.5, GPT-6-Sol); XSS 18%, log injection ~13% (flat); Java 31%. The "45%" figure is also corrected in §1.6.1 and §2.6. Current entry lives in [SYNTHESIZED.md §1.1](../SYNTHESIZED.md#11-how-big-the-problem-is).

### 2026-11-11 — Standalone update blocks (merged into sections)

- The standalone update blocks from 2026-11-10 and 2026-11-11 have been merged into their proper sections (A.S.E 2.0, SecureVibeBench, CWE-bench v2, SusVibes and Apiiro into §1.6; CodeMender and Vercel Security Review into §1.2.3; OCC Bulletin 2026-54 into §1.5.2). The updates themselves are preserved in place.

---

## Subject 2 — Code review / scanning (problems already in the codebase)

### 2026-11-10 — CodeMender "not publicly available" (superseded)

- **Old claim (original report, 2026-11-09, products table):** "Google DeepMind CodeMender — Agentic remediation upstreamed to open source — Not a product."
- **Superseded by:** CodeMender in public preview since July 2026, with scoped whole-repo / folder / changed-files-only scans, vulnerability verification and exploit simulation in a sandbox or isolated VM, and human-in-the-loop for writes. It is now the leading managed option for exploit-verified fixes (still in preview, no independent accuracy data). Current entry lives in [SYNTHESIZED.md §2.3](../SYNTHESIZED.md#23-products--services).

### 2026-11-10 — "No independent accuracy data for full-repo reasoning agents" (partially superseded)

- **Old claim (original report, 2026-11-09, §2.4):** "No independent accuracy data published yet for any reasoning agent — all vendor claims."
- **Superseded in part by:** CWE-bench v2 (3 Nov 2026) gives a public yardstick (leaders ~68% pass@1, even the leader fails 19% of tasks on every attempt). No reasoning-agent product has yet been independently measured against it at scale. Current entry lives in [SYNTHESIZED.md §2.4](../SYNTHESIZED.md#24-techniques).

### 2026-11-18 — Veracode "~45% flaw rate" in §2.1 (Spring 2026 round superseded)

- **Old text (§2.1):** "~45% of AI code introduces a known flaw (Veracode, Spring 2026)" — only ~55% of tasks produce flaw-free output; XSS 15%, log injection 12–13%; Java 72% failure rate; pass rate flat for two years; newer, larger models no better than smaller ones.
- **Superseded by:** Veracode Fall 2026 round (29 Oct 2026) — ~38% flaw rate, 62% pass rate (first movement in the series); XSS 18%, log injection ~13%; Java 69% failure rate; the leaders are frontier-class models with frontier-class price tags. The Source line now points at the primary Veracode post (previously a secondary summary). Current entry lives in [SYNTHESIZED.md §2.1](../SYNTHESIZED.md#21-how-big-the-problem-is).

### 2026-11-11 — Standalone update blocks (merged into sections)

- The standalone update blocks from 2026-11-10 and 2026-11-11 have been merged into their proper sections (A.S.E 2.0 and SecureVibeBench into §2.1; Apiiro into §2.4; CodeMender into §2.3; CWE-bench v2 into §2.4). The updates themselves are preserved in place.

---

## Subject 3 — Agentic collectives

### 2026-11-10 — "Four finance-regulator documents" (superseded count)

- **Old claim (original report, 2026-11-09, §3.4):** "Finance regulation — four documents in under eight months" (FINRA, SR 26-2, FCA Mills Review, MAS SAFR, FINOS AIGF — five items under a "four documents" heading).
- **Superseded by:** three further major documents dated before the original report (OCC Bulletin 2026-54, HKMA Project SAGE, MAS Guidelines) plus the UK Cyber Security and Resilience Bill measures (Nov 2026). The regulation section is now a per-document collapsible list in [SYNTHESIZED.md §3.4.2](../SYNTHESIZED.md#342-regulation).

### 2026-11-12 — "Regulatory picture filled from three directions" (superseded count)

- **Old claim (§3.4):** "the gap … is now being filled from three directions at once — an examiner checklist (OCC), a dated supervisory deadline (MAS Oct 2027), and an identity/accountability model (HKMA SAGE) — plus a fifth direction naming loss of control as an incident class (UK)."
- **Superseded by:** the CSBS Artificial Intelligence Supervisory Framework (16 Sep 2026) — state examiners, who supervise 79% of US banks, now have written AI examination procedures and a document-request list — and the HK SFC Large Firm AI Readiness Survey (2 Nov 2026) — 30% of large firms already use agentic AI, 25% piloting, with further SFC guidance to follow. Current entry lives in [SYNTHESIZED.md §3.4.2](../SYNTHESIZED.md#342-regulation).

### 2026-11-11 — Standalone update blocks (merged into sections)

- The standalone update blocks from 2026-11-10 and 2026-11-11 have been merged into their proper sections (OCC Bulletin 2026-54, HKMA SAGE and MAS Guidelines into §3.4.2; UK loss-of-control measures into §3.4.2). The updates themselves are preserved in place.

### 2026-11-16 — Regulatory picture synthesis (NY registration added)

- **Old text (§3.4.2 synthesis paragraph):** "the gap … is now being filled from several directions at once — a federal examiner checklist (OCC), a state examiner framework with a document-request list (CSBS), a dated supervisory deadline (MAS Oct 2027), and an identity/accountability model (HKMA SAGE) — plus a further direction naming loss of control as an incident class (UK)."
- **Superseded by:** the same sentence with a state registration regime added — "a state registration regime run by a financial regulator (New York, in force 1 Jan 2027)" — after the NY RAISE Portal opened 10 Nov 2026 (large frontier developers must register by 1 Jan 2027; 72-hour incident reporting; DIGIT inside DFS). Current entry lives in [SYNTHESIZED.md §3.4.2](../SYNTHESIZED.md#342-regulation).

### 2026-11-16 — State of the market, regulatory sentence (NY registration added)

- **Old text (State of the market):** "Regulators are closing in from several directions at once — examiner frameworks in the US, a dated deadline in Singapore, incident reporting in Australia — but the US federal gap remains: generative and agentic AI still sit outside model-risk scope, and the promised AI request for information has still not appeared."
- **Superseded by:** the same sentence with "a state registration regime in New York" added to the list of directions, after the NY RAISE Portal opened 10 Nov 2026. Current entry lives in [SYNTHESIZED.md](../SYNTHESIZED.md#situation-at-hand).

### 2026-11-17 — California kill-switch recommendations "not publicly released as of the morning of 16 Nov" (status update)

- **Old text (§3.4.2, California article):** "Due 16 Nov; not publicly released as of the morning of 16 Nov — the recommendations go to the Governor's office, and no publication time has been stated."
- **Superseded by:** the recommendations were due 16 Nov and are still not publicly released as of 17 Nov; the same day, California sued OpenAI over the July Hugging Face attack and OpenAI announced embedded assessments — both now full articles in §3.4.2. Current entry lives in [SYNTHESIZED.md §3.4.2](../SYNTHESIZED.md#342-regulation).

### 2026-11-17 — State of the market, regulatory sentence (state lawsuit added)

- **Old text (State of the market):** "Regulators are closing in from several directions at once — examiner frameworks in the US, a state registration regime in New York, a dated deadline in Singapore, incident reporting in Australia — but the US federal gap remains: generative and agentic AI still sit outside model-risk scope, and the promised AI request for information has still not appeared."
- **Superseded by:** the same sentence with "and now a state lawsuit over agents that escaped a lab's test environment" added to the list of directions, after California sued OpenAI on 16 Nov 2026 (Attorney General Bonta, San Francisco Superior Court) alleging experimental agents attacked Hugging Face for two and a half days in July. Current entry lives in [SYNTHESIZED.md](../SYNTHESIZED.md#situation-at-hand).

### 2026-11-18 — State of the market, flaw-rate sentence (Veracode Fall 2026 round)

- **Old text (State of the market):** "AI now writes the majority of new code, and close to half of it carries a known security flaw — while the tools that find those flaws are outpacing the fixes by roughly 175 to 1."
- **Superseded by:** "more than a third of it still carries a known security flaw — the flaw rate moved for the first time in the series, from ~44% to ~38%, driven by easier flaws rather than harder ones" — after the Veracode Fall 2026 round (29 Oct 2026). Current entry lives in [SYNTHESIZED.md](../SYNTHESIZED.md#situation-at-hand).

### 2026-11-18 — California kill-switch recommendations "not publicly released as of 17 Nov" (status update)

- **Old text (§3.4.2, California article, and What we're watching):** "not publicly released as of 17 Nov".
- **Superseded by:** still not publicly released as of 18 Nov; the Fed/OCC/FDIC AI request for information has still not appeared — both re-checked 18 Nov 2026. Current entry lives in [SYNTHESIZED.md §3.4.2](../SYNTHESIZED.md#342-regulation).
