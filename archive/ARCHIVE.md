# Synthesized — Archive

Superseded text from the knowledge base, dated and categorized by subject. Nothing here is deleted from the record — it is kept so that an earlier claim can be traced. The current picture lives in [SYNTHESIZED.md](../SYNTHESIZED.md).

The pre-restructure append-only version of the file (baseline 2026-11-09 plus the 2026-11-10 and 2026-11-11 addenda) is preserved at [SYNTHESIZED-2026-11-11-append-only.md](SYNTHESIZED-2026-11-11-append-only.md).

---

## Subject 1 — Pre-commit scanning

### 2026-11-10 — CodeMender "not publicly available" (superseded)

- **Old claim (baseline 2026-11-09, Layer C table):** "Google DeepMind CodeMender — Fix-only agent — **Not publicly available**."
- **Superseded by:** CodeMender has in fact been in public preview since July 2026 (hundreds of customers, per Google), and the 5 Nov 2026 Security Summit update added vulnerability verification and exploit simulation inside an OS-level sandbox or isolated VM, human-in-the-loop checks for local writes and command execution, and scoped scans. Current entry lives in [SYNTHESIZED.md §1.2.3](../SYNTHESIZED.md#122-layer-b--pr--ci-gates-acts-at-pull-request-or-pipeline--the-established-market).

### 2026-11-10 — "No federal model-risk umbrella" as the whole picture (partially superseded)

- **Old claim (baseline 2026-11-09, §1.5.2):** "Practical consequence: **there is currently no federal model-risk umbrella for AI coding tools** — firms must build their own controls."
- **Superseded in part by:** OCC Bulletin 2026-54 (4 Nov 2026), a 20-page examiner resource covering exactly the generative and agentic systems SR 26-2 excluded, with sixteen components in six pillars and a four-tier consequence classification. It sets no enforceable standards, so the "no umbrella as law" part still holds — but it no longer holds as examination practice. Current entry lives in [SYNTHESIZED.md §1.5.2](../SYNTHESIZED.md#152-provenance-audit-trail-and-regulation).

### 2026-11-11 — "No independent benchmark of agent-time enforcement tools" (partially superseded)

- **Old claim (baseline 2026-11-09, §1.7):** "First independent benchmark of agent-time enforcement tools (none exists yet — the category is ~6 months old)."
- **Superseded in part by:** CWE-bench v2 (Collinear AI, 3 Nov 2026) — a public, programmatically scored benchmark of 100 tasks (91 CWE classes) for agents finding and fixing security flaws, with 11 models evaluated. It is a yardstick for remediation agents; no agent-time enforcement product has yet been independently measured against it at scale, so the gap is narrowed, not closed. Current entry lives in [SYNTHESIZED.md §1.6](../SYNTHESIZED.md#16-benchmarks--evidence) and [§1.7](../SYNTHESIZED.md#17-open-gaps--watch-items).

### 2026-11-11 — Standalone addendum blocks (merged into sections)

- The "Update 2026-11-10 — addendum" and "Update 2026-11-11 — addendum" blocks that sat at the end of subject 1 in the append-only version have been merged into their proper sections (A.S.E 2.0, SecureVibeBench, CWE-bench v2, SusVibes and Apiiro into §1.6; CodeMender and Vercel Security Review into §1.2.3; OCC Bulletin 2026-54 into §1.5.2). Their content is preserved in place; the addendum blocks themselves are superseded as a format.

---

## Subject 2 — Code review / scanning (problems already in the codebase)

### 2026-11-10 — CodeMender "not publicly available" (superseded)

- **Old claim (baseline 2026-11-09, products table):** "Google DeepMind CodeMender — Agentic remediation upstreamed to open source — Not a product."
- **Superseded by:** CodeMender in public preview since July 2026, with scoped whole-repo / folder / changed-files-only scans, vulnerability verification and exploit simulation in a sandbox or isolated VM, and human-in-the-loop for writes. It is now the leading managed option for exploit-verified fixes (still in preview, no independent accuracy data). Current entry lives in [SYNTHESIZED.md §2.3](../SYNTHESIZED.md#23-products--services).

### 2026-11-10 — "No independent accuracy data for full-repo reasoning agents" (partially superseded)

- **Old claim (baseline 2026-11-09, §2.4):** "No independent accuracy data published yet for any reasoning agent — all vendor claims."
- **Superseded in part by:** CWE-bench v2 (3 Nov 2026) gives a public yardstick (leaders ~68% pass@1, even the leader fails 19% of tasks on every attempt). No reasoning-agent product has yet been independently measured against it at scale. Current entry lives in [SYNTHESIZED.md §2.4](../SYNTHESIZED.md#24-techniques).

### 2026-11-11 — Standalone addendum blocks (merged into sections)

- The "Update 2026-11-10 — addendum" and "Update 2026-11-11 — addendum" blocks that sat at the end of subject 2 in the append-only version have been merged into their proper sections (A.S.E 2.0 and SecureVibeBench into §2.1; Apiiro into §2.4; CodeMender into §2.3; CWE-bench v2 into §2.4). Their content is preserved in place; the addendum blocks themselves are superseded as a format.

---

## Subject 3 — Agentic collectives

### 2026-11-10 — "Four finance-regulator documents" (superseded count)

- **Old claim (baseline 2026-11-09, §3.4):** "Finance regulation — four documents in under eight months" (FINRA, SR 26-2, FCA Mills Review, MAS SAFR, FINOS AIGF — five items under a "four documents" heading).
- **Superseded by:** three further major documents dated before the baseline (OCC Bulletin 2026-54, HKMA Project SAGE, MAS Guidelines) plus the UK Cyber Security and Resilience Bill measures (Nov 2026). The regulation section is now a per-document collapsible list in [SYNTHESIZED.md §3.4.2](../SYNTHESIZED.md#342-regulation).

### 2026-11-11 — Standalone addendum blocks (merged into sections)

- The "Update 2026-11-10 — addendum" and "Update 2026-11-11 — addendum" blocks that sat at the end of subject 3 in the append-only version have been merged into their proper sections (OCC Bulletin 2026-54, HKMA SAGE and MAS Guidelines into §3.4.2; UK loss-of-control measures into §3.4.2). Their content is preserved in place; the addendum blocks themselves are superseded as a format.
