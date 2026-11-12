# CI Sitrep — *Code & Finance*

**Last updated:** 2026-11-12.

<details class="how-to-read">
<summary>How to read this</summary>

Created Intelligence in code and finance — as of today. A living knowledge base: the state of the art in AI code scanning and agentic collectives, for critical systems in finance.

This file is a **state of affairs**, not a log: each section states the current picture, kept up to date in place. When new information arrives, the relevant section is updated and the superseded text moves to [ARCHIVE.md](archive/ARCHIVE.md), dated and categorized. Nothing is silently deleted. The pre-restructure append-only version is preserved at [archive/SYNTHESIZED-2026-11-11-append-only.md](archive/SYNTHESIZED-2026-11-11-append-only.md).

**New to the terms?** Read the [explainer: CI, CIA, and CIAC](explainer.html) — what Created Intelligence means, and why this site uses it instead of "AI". The terms come from the foundational paper [*From Evolved Intelligence to Created Intelligence* (v0.1)](theses.html) — [download the Markdown source](created_intelligence_foundational_theses_v0.1.md).

**The bar for adding or changing anything:** it could change how a firm building critical systems in finance should act. Routine news, vendor marketing, and minor updates do not qualify.

**How to read it:** scan the sub-section headings, open an article headline for its facts. Every article is a collapsible headline; the facts inside are one per bullet. Start with [New this week](#new-this-week) to jump to the latest changes.

**Credibility rating** — every article carries a dots rating for how much confidence you can place in its source.

- **●●●● Established:** peer-reviewed and independently confirmed, or a primary regulatory/government document — safe to act on.
- **●●●○ Corroborated:** peer-reviewed single study, or a credible primary source confirmed by independent reporting — good basis for a decision.
- **●●○○ Reported:** single credible source, not yet independently verified (preprints, well-documented vendor research) — directional; verify before committing significant budget.
- **●○○○ Claimed:** vendor claim or single uncorroborated report — treat as a lead, not a fact.

</details>

## New this week

Additions from the past 7 days (rolling window — entries older than 7 days drop off).

- **2026-11-12 — SecPRBench** (subjects 1, 2): the first benchmark of agentic pre-merge security review on real bug-introducing commits; the best agents catch ~3 in 4 vuln-introducing changes, the weakest ~1 in 3 — the review layer is a layer, not a control. → [1.6 Benchmarks](#16-benchmarks--evidence) · [2.1 How big the problem is](#21-how-big-the-problem-is)
- **2026-11-12 — CSBS AI Supervisory Framework** (subject 3): state examiners — who supervise 79% of US banks — now have written AI examination procedures and a document-request list. → [3.4 Governance](#34-governance--finance)
- **2026-11-12 — Postman auto-install incident** (subjects 2, 3): a desktop app silently installed plugins and a self-approved hook into Claude Code and Codex; the agent layer's own config is a supply-chain surface. → [2.1 How big the problem is](#21-how-big-the-problem-is)
- **2026-11-12 — HK SFC AI Readiness Survey** (subject 3): 30% of large firms already use agentic AI, 25% piloting; the SFC will issue further guidance. → [3.4 Governance](#34-governance--finance)
- **2026-11-11 — SecureVibeBench, CWE-bench v2, SusVibes** (subjects 1, 2): a second independent peer-reviewed benchmark confirms roughly half of test-passing AI code is vulnerable; a public yardstick for remediation agents now exists. → [1.6 Benchmarks](#16-benchmarks--evidence) · [2.1 How big the problem is](#21-how-big-the-problem-is)
- **2026-11-11 — UK Cyber Security and Resilience Bill** (subject 3): "loss of control" named as a regulated incident class; evidence preservation now a named expectation in the making. → [3.4 Governance](#34-governance--finance)
- **2026-11-10 — OCC Bulletin 2026-54, HKMA SAGE, MAS Guidelines** (subject 3): the regulatory gap is being filled from three directions; MAS sets a dated deadline (Oct 2027). → [3.4 Governance](#34-governance--finance)
- **2026-11-10 — A.S.E 2.0, CodeMender, Vercel Security Review, Apiiro secrets leak** (subjects 1, 2): exploit-verification is the gate; CodeMender is in public preview (corrects an earlier entry); agent settings files are a new secrets vector. → [1.6 Benchmarks](#16-benchmarks--evidence) · [1.2 Products](#12-product-landscape) · [2.3 Products](#23-products--services)

## Contents

- [1. Pre-commit sanitizing / certification](#1-pre-commit-sanitizing--certification)
  - [1.1 How big the problem is](#11-how-big-the-problem-is)
  - [1.2 Product landscape](#12-product-landscape)
  - [1.3 What they catch](#13-what-they-catch)
  - [1.4 How they work (mechanisms)](#14-how-they-work-mechanisms)
  - [1.5 Best practice — critical systems in finance](#15-best-practice--critical-systems-in-finance)
  - [1.6 Benchmarks & evidence](#16-benchmarks--evidence)
  - [1.7 Open gaps / watch items](#17-open-gaps--watch-items)
- [2. Codebase sanitize / certification — CI-generated problems already in the codebase](#2-codebase-sanitize--certification--ci-generated-problems-already-in-the-codebase)
  - [2.1 How big the problem is](#21-how-big-the-problem-is)
  - [2.2 Problem classes](#22-problem-classes)
  - [2.3 Products & services](#23-products--services)
  - [2.4 Techniques](#24-techniques)
  - [2.5 Best practice — finance](#25-best-practice--finance)
  - [2.6 Hype vs verified](#26-hype-vs-verified)
  - [2.7 What this means in practice](#27-what-this-means-in-practice)
- [3. CIAC — creation, governance, management](#3-ciac--creation-governance-management)
  - [3.1 Frameworks & platforms](#31-frameworks--platforms)
  - [3.2 Interoperability standards](#32-interoperability-standards)
  - [3.3 Orchestration patterns](#33-orchestration-patterns)
  - [3.4 Governance — finance](#34-governance--finance)
  - [3.5 Management & observability](#35-management--observability)
  - [3.6 Evaluation](#36-evaluation)
  - [3.7 Best practices](#37-best-practices)
  - [3.8 Hype vs verified](#38-hype-vs-verified)
- [Archive](#archive)

---

## 1. Pre-commit sanitizing / certification

Commercial products that scan CI-generated code for problems *before* it is committed, plus the state of the art in best practice, with focus on critical systems in finance.

### 1.1 How big the problem is

<details>
<summary><strong>Veracode — ~45% of AI code introduces a known security flaw</strong> (Spring 2026, longitudinal benchmark) ●●●○</summary>

- Security pass rate ~55%, essentially flat for two years (2024 → Mar 2026), while syntax correctness rose past 95%.
- Best models (GPT-5 with extended reasoning) reach only 70–72%.
- By class: SQL injection 82% pass; insecure crypto 86% pass; XSS **15%** pass; log injection **13%** pass.
- By language: Python 62%; C# 58%; JS 57%; **Java 29%**.
- 80 tasks, 4 languages, 4 CWE classes, 150+ models tested.
- Vendor-run but consistent methodology — the best longitudinal dataset available.
</details>

<details>
<summary><strong>Spracklen et al. — ~20% of package references are hallucinated</strong> (USENIX Security 2025, peer-reviewed) ●●●○</summary>

- 19.7% of package references named packages that don't exist.
- 205,474 unique invented names; 43% recur across all 10 re-runs.
- The "slopsquatting" attack: attacker registers the invented name (term coined by Seth Michael Larson, Python Software Foundation).
- Open-weight models hallucinate ~22% vs ~5% for commercial models.
- 16 models, 576k samples, 2.23M package references.
</details>

<details>
<summary><strong>CodeRabbit — AI code carries 2.74× the vulnerabilities of human code</strong> (Dec 2025, 470 PRs) — [VENDOR CLAIM] ●○○○</summary>

- CI-generated code had 1.7× more major issues and 2.74× the security-vulnerability rate of human-written code for equivalent tasks.
- CodeRabbit's own analysis — treat as a vendor claim.
</details>

<details>
<summary><strong>Tenzai — the failure mode moved up the stack</strong> (Dec 2025, 5 tools, 15 apps, 69 vulns incl. 6 critical) ●●○○</summary>

- No classic SQLi/XSS found.
- Failures were business logic and authorisation: missing ownership checks, admin endpoints without admin checks, negative pricing.
- Older peer-reviewed base rates agree: Pearce et al. (IEEE S&P 2022) ~40% of Copilot programs vulnerable in high-risk scenarios; Fu et al. (ACM TOSEM 2025) 29.5% of Python / 24.2% of JS AI-assisted snippets had weaknesses. (Models tested 2021–2024.)
</details>

<details>
<summary><strong>Apiiro / CSA — volume compounds it</strong> (Apr 2026, enterprise telemetry) — [VENDOR DATA] ●●○○</summary>

- AI-assisted developers commit 3–4× faster.
- Monthly security findings rose ~10× (∼1,000 → 10,000+).
- Privilege-escalation paths +322%; architectural flaws +153%.
- CVEs attributed to CI-generated code (Georgia Tech Vibe Security Radar): 6 in Jan 2026, 15 in Feb, 35 in Mar.
- Apiiro's own enterprise telemetry via CSA.
</details>

<details>
<summary><strong>Adoption is already majority-AI</strong> (2026 surveys) ●●●○</summary>

- JetBrains Developer Ecosystem Survey 2026 (~15,000 devs): ~47% of code written fully by AI agents.
- Sonar State of Code 2026: 42% of committed code AI-generated/assisted; 96% of developers don't fully trust AI code, yet only 48% always verify it before committing; 65% expected by 2027.
- Google (Apr 2026): 75% of new code AI-generated, engineer-approved.
</details>

### 1.2 Product landscape

Three layers, newest first. Distinguishing test for the newest layer: can it *refuse* an agent action, or only report?

#### 1.2.1 Layer A — Agent-time enforcement (acts while the agent writes, before the save)

| Product | What it does | Where it runs | Price / availability |
|---|---|---|---|
| **CybeDefend — VibeDefend** | Injects business + security/compliance rules into the agent loop; Action Guard refuses dangerous shell commands locally; live diff scan (SAST/SCA/secrets/IaC) with in-loop fix | Claude Code, Cursor, Devin Desktop, Codex, Copilot; plus CI | Free npm CLI to try; platform free to self-host; paid from $19/mo |
| **Endor Labs — AURI** | Agent-action governance (Block / Alert / Ask Permission) + reachability-led SCA, AI SAST (IDOR, broken access control, insecure design), package firewall, secrets, AI-BOM inventory of agents/models/MCP servers | Agent hooks (Claude Code, Cursor, Codex, Copilot), PR, CI | No prices on own site; AWS Marketplace 10-seat packs $7,200/yr Code Pro, $12,960/yr Open Source Pro (via third-party comparison — verify) |
| **Legit Security — VibeGuard 2.0** (3 Aug 2026) | Endpoint desktop app; discovers coding agents, MCP servers, skills; blocks dangerous operations; resists being switched off | Developer endpoint | No free tier; AWS Marketplace lists a $75,000 annual commit (via third-party comparison — verify) |
| **Snyk Studio** | Security hooks in Claude Code, Cursor, Codex CLI, Gemini CLI, Copilot; reachability for Java/JS/TS/Python; "AI Security Fabric" | Agent hooks, IDE, PR, CI | See Snyk pricing below |
| **Semgrep (agent hooks)** | Custom-rule SAST in the agent loop; Semgrep Assistant AI triage | Agent hooks, IDE, PR, CI | See below |
| **Wiz Code** | Plugins for Claude Code / Cursor (Apr 2026); aggregates scanner findings on the Wiz Security Graph | Agent, PR | Add-on to Wiz Cloud; no free tier |
| **GitGuardian** | Secrets + machine identities via pre-commit hooks, CI, agent plugins | Pre-commit, CI, agent | Published plans; exact figures vary by tier — verify |

#### 1.2.2 Layer B — PR / CI gates (acts at pull request or pipeline — the established market)

| Product | What it does | Price / availability |
|---|---|---|
| **GitHub Code Security (CodeQL)** | Semantic SAST (CodeQL), Copilot Autofix, dependency review, Dependabot; **AI Scan GA** (public preview 14 Jul 2026) extends detection beyond CodeQL's scope; **agentic autofix GA 15 Oct 2026** (batches ≤25 alerts, default branch only). Note: AI Scan findings **cannot block PR merges**. | **$30/active committer/mo**; Secret Protection **$19** (both since the 1 Apr 2025 unbundling; Team + Enterprise; free on public repos). AI Scan / agentic autofix consume a separate AI Credits SKU. |
| **Snyk** | SAST (DeepCode AI), SCA + reachability, containers, IaC; Agent Fix agentic auto-fix; "embedded security context" | Free tier (200 SCA / 100 SAST / 300 IaC / 100 container tests/mo); **Team $25/dev/mo** annual (min 5, max 10 devs); Ignite ~$105/dev/mo (~$1,260/dev/yr); Enterprise custom (Vendr medians ~$34,886/yr at 50 devs, ~$67,552/yr at 100) |
| **Semgrep** | Rule-based + taint SAST, cross-file (Pro), 20,000+ Pro rules, custom rules, Supply Chain (SCA + reachability), Secrets; Semgrep Assistant (AI triage, false-positive filtering, fix suggestions) | **Community Edition free** (LGPL-2.1 engine; rules under Semgrep Rules License since Dec 2024); full platform **free ≤10 contributors**; beyond that **~$30–35/contributor/mo** (sources differ — verify) |
| **Checkmarx One** | Enterprise SAST/SCA/IaC/containers; **v3.66 (6 Sep 2026)** routes files in languages its query-based SAST doesn't support to an LLM-based engine | Quote-based; sales-led |
| **SonarQube** | SAST + quality gates (the merge gate most teams already have); Sonar AI CodeFix | Cloud Team from **$34/mo per 100k LOC**; Server/Enterprise custom |
| **Veracode** | Enterprise SAST/SCA/governance; runs the longitudinal GenAI benchmark above | Quote-based |
| **Aikido Security** | Developer-first SAST/SCA/IaC/containers; Guardian Agent adds secure prompt enrichment + pre-commit prevention | Free plan (SCA, SAST, IaC, containers; IDE, CLI, SCM); paid tiers — verify |
| **GitLab Ultimate** | Native SAST/SCA/secrets in the platform | Quote-based |

#### 1.2.3 Layer C — LLM-based review / audit (reads the code the way a reviewer would)

| Product | What it does | Availability / price |
|---|---|---|
| **Anthropic — Claude Security** | `/security-review` in Claude Code; plugin (beta); cloud service (public beta) — editable threat model, adversarial verification of every finding, validation in an isolated environment, proposed patches | In Claude Code on Pro/Max or pay-as-you-go API; service for Claude Enterprise, price not public |
| **OpenAI — Codex Security** | Plugin + CLI (open source, Apache-2.0; Node 22.13/24/26, Python 3.10); cloud service | CLI open source; service pricing via OpenAI |
| **CodeRabbit** | Automated PR review; Learnings (past feedback applied automatically), path instructions, "slop detection" for low-quality AI PRs | $24 Essentials / $48 Team / $72 Advanced per contributing dev/mo (annual); free on open-source repos; Enterprise (SSO/RBAC/audit) custom |
| **Qodo** (ex-CodiumAI) | Generates test suites probing AI code for edge cases; PR review | Pro from $30 (~18 reviews/mo entry block); Enterprise custom (30+ users, SSO/audit, single-tenant or on-prem) |
| **Greptile** | Codebase-graph-indexed PR review, cross-repo | Pro $30/seat/mo, 50 credits, $1/extra credit |
| **Cursor Bugbot** | 8 parallel analysis passes per PR, majority-vote + validator stage | Bundled with Cursor |
| **Cloudflare security-audit skill** | Audit skill for your own coding agent | Free to start |
| **Kodus, DryRun Security** | PR review agents; DryRun adds natural-language code policies enforced on every PR | Kodus Teams ~$10/dev + tokens; DryRun quote-based |
| **Google DeepMind CodeMender** | Fix-only agent with vulnerability verification and exploit simulation in a sandbox/isolated VM; human-in-the-loop for local writes and command execution; scoped scans (single folder, whole repo, or only files changed since last scan); multi-model including Gemini 4 Argon | **In public preview since July 2026** (hundreds of customers, per Google). Thales evaluation cited by Google claims up to 95% reduction in vulnerability discovery time — vendor-cited, not independent. Still in preview; the verification-in-sandbox loop is the pattern to watch. |
| **Vercel Security Review** | Push-time, diff-scoped security review inside Vercel Agent (missing auth checks, exposed secrets, logic flaws read in context); runs on every push including direct/force pushes to production, not just PRs | **Public beta 2 Nov 2026.** Free during beta until 10 Nov 2026, then usage-based. A new gate position (push-time, between agent-time and PR) — relevant for web-facing finance front ends, less so for core systems. |

<details>
<summary>See also</summary>

[3.4 Governance — finance](#34-governance--finance) (the same gate-outside-the-model control, applied to agents rather than to code).
</details>


### 1.3 What they catch

| Problem class | Who catches it | Confidence |
|---|---|---|
| Injection (SQLi, XSS, log/command injection), insecure crypto | Deterministic SAST (CodeQL, Semgrep, Snyk, Checkmarx, Sonar) — the mature layer | High for known patterns; Veracode shows XSS/log-injection still the worst gaps |
| Hardcoded secrets / credentials | GitGuardian, GitHub Secret Protection + push protection, Semgrep Secrets, Snyk | High; push protection blocks before commit |
| Hallucinated / fabricated packages (slopsquatting) | SCA + package firewall / install-boundary checks (Endor, Snyk, Semgrep Supply Chain); verify-every-package-exists before install | Good if the install boundary is enforced; **nothing catches it if the developer installs by hand** |
| Hallucinated APIs / fabricated functions | LLM review (threat-model + validation); compile/type checks; runtime tests | Partial — the weakest automated coverage; retrieval + external verification, not prompting |
| Hallucinated auth / logic flows (middleware declared but never applied, token state trusted client-side, validation step never called) | LLM review + Endor-style AI SAST (IDOR, broken access control); human review | **Low automated confidence — this is the class that most often ships** (Tenzai; GrowExx) |
| Business-logic flaws (ownership checks, admin gating, negative pricing) | Human review; LLM review with business-rule injection (CybeDefend) | Low automated; human backstop required |
| Dependency CVEs / license issues | SCA (Snyk, Semgrep Supply Chain, Dependabot, OSV-Scanner) | High for known CVEs; license scanning is standard SCA, less covered by agent-time tools |
| Style / consistency / maintainability | Sonar quality gates, linters, Semgrep custom rules | High |

### 1.4 How they work (mechanisms)

- **Deterministic SAST** — queries over code-as-data (CodeQL), pattern/taint rules (Semgrep, Snyk DeepCode, Checkmarx). Fast, low false-positive on known classes, blind to novel logic.
- **SCA + reachability** — dependency graph + whether the vulnerable code path is actually reachable (Endor, Snyk). This is what makes machine-paced findings survivable: it ranks by exploitability instead of raw CVE count.
- **Secrets scanning + push protection** — regex/entropy + ML on diffs; blocks the commit (GitHub, GitGuardian).
- **Agent hooks / MCP interception** — the agent's tool calls (file writes, shell commands, installs) pass a policy check before executing; can refuse (Endor AURI, CybeDefend Action Guard, Snyk Studio). This is the only mechanism that acts *before* the bad code exists.
- **LLM-based review** — a model reads the diff with repo context (RAG / codebase graph / linked issues), builds a threat model, and increasingly *validates* each finding in a sandbox before reporting (Anthropic's adversarial verification; Codex Security). Best practice emerging: reviewer from a **different model family** than the generator.
- **Test generation** — CI-generated tests probing edge cases of CI-written code (Qodo).
- **AI-BOM / provenance** — inventory of agents, models, MCP servers, rule files (.cursorrules, AGENT.md, CLAUDE.md), AI API keys, and commit provenance (Endor, CybeDefend, Legit). Required for EU AI Act / NIST AI RMF alignment.
- **Package firewall / install boundary** — only allow-listed, existing packages may be installed (Endor); the direct counter to slopsquatting.

### 1.5 Best practice — critical systems in finance

#### 1.5.1 The three-layer model

The converging model across 2026 sources (Bugni Labs, Shetty, DesignVerse, CSA) is **three layers, cheapest trustworthy layer first**:

1. **Deterministic gates, blocking, before any AI review.** Tests, SAST, SCA, secrets, IaC, data/schema contracts, policy-as-code — fully automated, blocking in the pipeline, not reports read afterwards. Move *more* checks into this layer than you have today.
2. **AI judgement, trusted per task, never in general.** Narrow brief (e.g. only: changes crossing a domain boundary, code routing around an approved helper, missing negative tests, edits to data-handling logic). Model from a different family than the generator. Its calls compared against human calls before it gets any authority. **Rule now hardening into consensus: an AI reviewer may *block* a high-risk change, but never *approve* one.** Human keeps the merge decision for regulated code. (Cloudflare's reviewer can approve with human override — the exception, not the model.)
3. **Human judgement for risk, on the loop not in the loop for every line.** Accepting risk, irreversible/high-criticality changes, exceptions — and *checking the checkers*: regularly sampling what the AI reviewers let through.

#### 1.5.2 Provenance, audit trail, and regulation

- **Provenance and accountability are the audit requirement.** Every CI-generated change must record: who requested it, which tool and model, in what context, and who approved it. The CIA proposes; a human reviews, accepts, and is accountable. (Linux kernel policy is the cleanest statement: agents must not add "Signed-off-by" — only a human can certify a contribution.) Four-eyes for high-risk changes; approver ≠ requester. Tier controls by risk: heaviest on customer data, payments, access control, critical infrastructure.
- **Audit trail must survive the pipeline.** The evidence — diff, requirements, tests, automated-check results, review outcome, deployment record — must stay connected from PR through production, queryable after the people involved have moved on. Review comments and approval labels alone do not satisfy this.
- **NYDFS (NYC — directly applicable).** 21 May 2026: two Industry Letters — (1) heightened cybersecurity risks from frontier AI models (prompted by Anthropic's Mythos vulnerability-finding model), (2) guidance for heightened threat environments. They impose no new legal requirements, but explicitly direct regulated entities to consider **"strengthened testing of CI-generated code prior to production deployment"**, expedited vulnerability management, and third-party coordination. Binding backdrop remains the NYDFS Cybersecurity Regulation (23 NYCRR 500). Examiner direction is clear even where the letters are advisory.
- **US federal — a gap opened in 2026.** SR 11-7 was rescinded and replaced 17 Apr 2026 by **SR 26-2** (Fed / OCC Bulletin 2026-13 / FDIC FIL-15-2026). Generative and agentic AI are **expressly out of scope**; the guidance states it sets no enforceable standards and is most relevant above $30B in assets. The clause that still matters for buyers: **vendor products must still be validated** (by internal or outside parties). An AI request for information was promised; none had appeared by late Oct 2026. A replacement third-party-risk guidance was proposed 15 Sep 2026 (comments due 16 Nov 2026). Practical consequence: **there is currently no federal model-risk umbrella for AI coding tools** — firms must build their own controls, and existing technology-neutral rules (FFIEC IT Examination Handbook, 2023 interagency third-party guidance) still apply.
  - **OCC Bulletin 2026-54 (4 Nov 2026) narrows the gap in examination practice, not in law.** A 20-page examiner resource for national banks, federal savings associations and federal branches/agencies (with News Release 2026-97). It covers exactly the generative and agentic systems SR 26-2 excluded: sixteen components in six pillars (purpose, risk, control, oversight, resilience, assurance), and a four-tier consequence-based risk classification (an autonomous payment agent is Tier 1 "regardless of how well it performs in testing"; an internal productivity tool is Tier 4). Examiner considerations named include kill switches, circuit breakers, provider-agent limits, human-in-the-loop / human-on-the-loop controls with real authority, MRM extensions for non-deterministic systems, adversarial and hallucination testing, reconstructable records, and independent audit. **It sets no supervisory expectations, no enforceable standards and no prescriptive requirements** — it is an examiner lens, not a rule — but it is the first US federal document telling examiners what to look at in agentic AI. A vendor who maps its agentic governance to the sixteen components has a concrete, examiner-shaped sell to national banks.
- **EU (for firms with EU operations or clients).** **DORA** (Reg. (EU) 2022/2554) in force 17 Jan 2025: an AI inference vendor is an ICT third-party service provider (Arts. 28–30) — register the arrangement, assess concentration risk, maintain a *tested* exit strategy, report major ICT incidents (initial notification within 4h of classification, ≤24h of awareness). **EU AI Act** high-risk obligations (incl. creditworthiness assessment, insurance pricing) deferred to **2 Dec 2027** by the Digital Omnibus (Reg. (EU) 2026/1744, in force 27 Jul 2026). Self-hosted/on-prem deployment (Semgrep CE, SonarQube Server, Qodo single-tenant/on-prem, CodeRabbit self-host Enterprise) materially reduces the DORA third-party surface vs SaaS scanners that ingest your code.

<details>
<summary>See also</summary>

[2.5 Best practice — finance](#25-best-practice--finance) (the same controls for code already in the repo) · [3.7 Best practices](#37-best-practices) (the supervisor-pattern version of the same gate rule).
</details>


### 1.6 Benchmarks & evidence

<details>
<summary><strong>A.S.E 2.0 / CASE-Bench — 55.6% passed every test while a working exploit succeeded</strong> (arXiv:2611.06294, submitted 4 Nov 2026; preprint, not peer-reviewed) ●●○○</summary>

- 145 repository-level tasks built from real CVEs in 51 projects.
- A task counts as secure only if functional tests pass **and** a validated proof-of-concept exploit fails.
- Claude Code (Sonnet 4.5): 74.0% functional pass, but only 18.4% secure.
- **55.6% of outputs passed every test while a working exploit still succeeded.**
- Coding agents observed the relevant safeguard (existing validator / access check) in only 27–36% of trajectories.
- When the safeguard was put in context, secure output roughly doubled (24.8% vs 12.6% with the target file alone).
- A separate Nov 2026 study found security guidance in only 36.3% of AGENTS.md files and 29.9% of CLAUDE.md files.
- Implication: functional tests are a poor proxy for security in agent-written code — exploit-verification, not test-passing, is the gate — and annotating safeguards in agent context (AGENTS.md / CLAUDE.md, retrieval) is a cheap, high-leverage control.
</details>

<details>
<summary><strong>SecureVibeBench — best agent 23.8% correct-and-secure; 23% correct but exploitable</strong> (Chen et al., arXiv:2509.22097; ACL 2026 long paper, July 2026 — peer-reviewed) ●●●○</summary>

- 105 C/C++ tasks reconstructed from real OSS-Fuzz/ARVO vulnerabilities across 41 projects.
- Each task replays the exact requirements that originally led a human developer to introduce the vulnerability.
- A task counts as resolved only if functional tests pass **and** dynamic + static security checks pass.
- Best agent–model combination (SWE-agent + Claude Sonnet 4.5): **23.8% correct-and-secure**; 23.0% functionally correct but exploitable; 53.3% functionally incorrect.
- Codex CLI (GPT-5): 17.1%.
- Distinct from A.S.E 2.0 (which tests repair of known CVEs): this tests greenfield generation — whether the agent *introduces* a vulnerability when building a feature.
- Agents introduced **new CWE types not present in the original vulnerabilities** (e.g. CWE-14 compiler removal of buffer-clearing code, CWE-319 cleartext transmission).
- Implication for the pre-commit gate: the "correct but vulnerable" 23% is the class that passes every test and ships; it is only catchable by exploit-verification or security review, never by the test suite.
- A second independent, peer-reviewed confirmation of the A.S.E 2.0 finding, with a different methodology.
</details>

<details>
<summary><strong>CWE-bench v2 — public yardstick for remediation agents</strong> (Collinear AI, via Hugging Face blog, 3 Nov 2026) ●●○○</summary>

- Public benchmark of 100 tasks (91 CWE classes) for agents finding and fixing security flaws in real open-source code.
- Fully programmatic scoring, held-out private set. 11 models evaluated.
- Gemini 4 Argon leads 67.8% pass@1 (81.0% pass@4); Claude Opus 5.5 67.3%.
- Even the leader fails 19% of tasks on every attempt.
- A usable instrument for measuring remediation-agent accuracy — the "independent accuracy data" watch item now has a public yardstick, though no product has yet been independently measured against it at scale.
</details>

<details>
<summary><strong>SusVibes re-run — a post-hoc review lifts working-and-secure to 47–56% at ~2.5× cost</strong> (independent research commissioned by Checkmarx, reported 2 Nov 2026) — [VENDOR-COMMISSIONED] ●●○○</summary>

- Agents rebuilding features that originally shipped with a real vulnerability: functional success 83–95%, but only 24–36% both working and secure.
- 65–75% of working solutions reintroduced the old vulnerability.
- A one-line security reminder added only 1–8 points.
- A post-hoc security review lifted working-and-secure to 47–56% at ~2.5× the cost — still leaving about half of tasks insecure.
- Organisations where 81–100% of code is AI-generated reported shipping vulnerable code at 3.4× the rate of those at 1–20%.
- Corroborates the other two benchmarks; the cost figure (2.5× for a review that still leaves half insecure) is the number to use when scoping a review layer for a client.
</details>

<details>
<summary><strong>SecPRBench — best agentic reviewers catch ~3 in 4 vuln-introducing changes; weakest ~1 in 3</strong> (arXiv:2610.33509, 24 Oct 2026; preprint, not peer-reviewed) ●●○○</summary>

- 265 tasks from nine critical systems (Firefox, V8, OpenSSL), each built from the real commit that introduced a vulnerability — not from its later fix — and paired with a repaired companion.
- A finding counts only if it explains the vulnerability's root cause in the reviewed code (LLM-as-judge, Claude Opus 5.5).
- Recall across eight frontier models: **32.5%–78.1%**. Top four (Grok 4.6, GPT-6 sol, GLM 5.3, Claude Opus 5.5) find about three in four and are statistically tied; all eight combined still miss 23 targets.
- **68% of misses are wrong-mechanism reasoning, not oversights**: the agent reports on the file holding the flaw but argues a different mechanism.
- Security-focused harnesses move recall both ways: OpenAI's Codex Security lowers it 8.3 points (mostly by abstaining); Anthropic's Defending Code raises it 7.7 points, at higher cost and report volume.
- Implication for the pre-commit gate: agentic review as a sole gate misses 22–68% of vulnerability-introducing changes — it is a layer, not a control — and harness choice is a measurable design decision (±8 points).
</details>

<details>
<summary><strong>Apiiro — agent settings files are a new secrets vector standard scanners miss</strong> (5 Nov 2026) — [VENDOR RESEARCH] ●●○○</summary>

- Claude Code's "Don't Ask Again" approval writes the literal approved command, secrets included, into `.claude/settings.local.json`.
- Apiiro found 104,185 public copies; 1,122 (1.1%) held at least one real secret (1,379 distinct: 379 DB passwords, 122 Supabase service-role keys, 43 SSH logins, 23 AWS keys).
- Widened to git history, shared settings and agent transcripts: 2,539 secrets in 1,994 repos; one notified organisation confirmed a key still live.
- **Of the 1,122 files, gitleaks flagged 564 and TruffleHog 643; 215 were missed by both.**
- The file is excluded only via the developer's global git-excludes, not the project `.gitignore`.
- Implication: agent settings/transcript files are a new secrets vector that standard pre-commit secret scanning substantially misses — an audit check to add (scan `.claude/`, agent settings and transcripts; project-level `.gitignore`; history sweep).
</details>

#### 1.6.1 Hype vs independently verified

- **Independently verified:** Veracode's 45% figure (longitudinal, consistent method — but Veracode's own SAST is the measuring instrument); Spracklen et al. (peer-reviewed, USENIX Security 2025); Pearce et al. (IEEE S&P 2022) and Fu et al. (ACM TOSEM 2025) base rates; SecureVibeBench (peer-reviewed, ACL 2026); the regulatory facts above (primary sources: OCC Bulletin 2026-13, NYDFS letters, DORA text).
- **[VENDOR CLAIMS — treat as marketing until independently replicated]:** Snyk's "secure-and-functional fix rate 75% → 85.4%" (own June 2026 benchmark, cited by Futurum); CybeDefend's controlled study (own research, Aug 2026: 30 tasks, one retail codebase, Claude Opus 5 — 57/64 rule specifics implemented exactly; +18% token overhead); CodeRabbit's 2.74× vulnerability rate (own analysis of 470 PRs); Apiiro's 10× findings / +322% privilege-escalation paths (own enterprise telemetry via CSA); Legit "resists being switched off"; any vendor "blocks X% of vulnerabilities" figure.
- **Reported, not independently verified:** the Copilot Autofix incident in which a CI-generated fix reportedly opened a shell injection in Snowflake's CI/CD that Wiz's red agent then exploited autonomously (Wiz case study, via The State of Play, 2026) — human reviewers and GitHub Advanced Security both reportedly missed it. GitHub Copilot code review's systematic misses of SQLi/XSS/insecure deserialization while flagging style issues (evaluation cited by The State of Play, 2026).
- **What nobody has independently verified:** head-to-head detection rates of the new agent-time enforcement tools on a common benchmark; false-positive cost at enterprise scale; license/provenance compliance of CI-generated code (training-data lineage is largely unaddressed by every scanner listed).

<details>
<summary>See also</summary>

[2.1 How big the problem is](#21-how-big-the-problem-is) (the same benchmarks, read as what's already in a codebase) · [2.4 Techniques](#24-techniques) (exploit-verification as the audit method) · [3.6 Evaluation](#36-evaluation) (pass^k, not pass@1 — why a single pass misleads).
</details>


### 1.7 Open gaps / watch items

- First independent benchmark of agent-time enforcement tools (none exists yet — the category is ~6 months old). CWE-bench v2 (Nov 2026) now gives a yardstick for remediation agents, but no agent-time enforcement product has been independently measured against it at scale.
- Precision/recall of LLM reviewers on real PRs at scale — a first yardstick now exists (SecPRBench, Oct 2026: recall 32.5–78.1% on real bug-introducing commits), but no commercial review product has yet been independently measured against it at scale; head-to-head detection rates of agent-time enforcement tools still don't exist.
- The Fed/OCC/FDIC AI request for information (promised Apr 2026, still unpublished late Oct 2026) and the replacement third-party guidance (comments due 16 Nov 2026).
- Whether NYDFS's advisory language hardens into examination expectations for CI-generated code testing.
- EU AI Act high-risk obligations arriving Dec 2027 — the compliance build-out for credit/insurance AI is a 2027 budget item, not a 2026 one.

<details>
<summary>See also</summary>

[3.4 Governance — finance](#34-governance--finance) (same watch items: the Fed/OCC/FDIC AI request for information, still unpublished; replacement third-party-risk guidance, comments due 16 Nov 2026).
</details>


### Sources — subject 1 (accessed 2026-11-09 unless noted)

- Veracode, "Spring 2026 GenAI Code Security Update", 2026-03-24 — https://www.veracode.com/blog/spring-2026-genai-code-security/
- CybeDefend, "Best AI Code Security Tools 2026: 13 Platforms Compared" (docs read 21 Sep 2026) — https://www.cybedefend.com/en/blog/best-ai-code-security-tools (V)
- CybeDefend, "VibeDefend under measurement", Aug 2026 (controlled study) — https://cybedefend.com/research/vibedefend-under-measurement-full-paper.pdf (V)
- CybeDefend vs Endor Labs comparison — https://www.cybedefend.com/en/compare/cybedefend-vs-endor-labs (V)
- Pillitteri, "Best AI Tools for Code Security Audits, Compared", Oct 2026 — https://pasqualepillitteri.it/en/news/26978/best-ai-code-security-audit-tools-compared
- Best AI Code Security, ratings Oct 2026 — https://bestaicodesecurity.com/
- The State of Play, "Security-focused code review" (GitHub AI Scan / Autofix GA dates; Copilot review evaluation) — https://www.thestateofplay.ai/practice/security-focused-code-review
- GrowExx, "AI Code Review Tools vs Human Experts" — https://www.growexx.com/blog/ai-code-review-vs-human-expert/
- Cubic, "AI code security: the risks and how to catch them" — https://www.cubic.dev/blog/ai-code-security
- Bugni Labs, "How Engineering Teams Can Make AI-Generated Code Auditable", Oct 2026 — https://medium.com/@bugni_labs/how-engineering-teams-can-make-ai-generated-code-auditable-1eea3b65847e
- Shetty, "AI made code cheap. It didn't make approval cheap.", Nov 2026 — https://medium.com/@jay_17751/ai-made-code-cheap-it-didnt-make-approval-cheap-44e2bdcd94bb
- DesignVerse, "AI Governance Auditing: Who Owns AI-Generated Code?" — https://designverse.ai/blog/ai-governance-auditing-ai-code
- Willkie, "NYDFS Issues Two Industry Letters Addressing Heightened Cybersecurity Risks from Frontier AI Models", 29 May 2026 — https://www.willkie.com/publications/2026/05/nydfs-issues-two-industry-letters-addressing--heightened-cybersecurity-risks-from-frontier-ai-models
- Custosa, "AI Compliance for Financial Services (SR 11-7)" (SR 26-2 analysis) — https://custosa.com/ai-compliance-financial-services.html
- Multimodal, "AI for Compliance in Banking: 8 Best Tools" (SR 26-2, 17 Apr 2026) — https://www.multimodal.dev/post/ai-tools-for-regulatory-compliance-in-banking
- BotMinds, "SR 26-2 and AI" (OCC Bulletin 2026-13; third-party guidance proposal 15 Sep 2026) — https://www.botminds.ai/solutions/commercial-loan-portfolio-analysis/model-risk-ai-loan-file-agents
- DeepInspect, "DORA Third-Party Risk for AI" — https://www.deepinspect.ai/blog/dora-ai-third-party-risk
- Perimattic, "DORA Compliance for AI Systems" — https://perimattic.com/products/perimattic-ai-suite/ai-observability-for-dora/
- IOMete docs, "DORA, EU AI Act, Financial Institutions" (Digital Omnibus Reg. (EU) 2026/1744) — https://github.com/iomete/iom-docs/blob/HEAD/blog/2026-03-10-dora-eu-ai-act-financial-institutions-data-infrastructure.md
- Redress Compliance, "GitHub Advanced Security Pricing" ($30/$19, Apr 2025 unbundling) — https://redresscompliance.com/microsoft-github-advanced-security-licensing
- StatWharf, "Best Static Code Analysis Tools (2026)" (pricing checked Oct 2026) — https://www.statwharf.com/best/static-code-analysis-tools/
- Snyk vs Semgrep comparisons (pricing) — https://dev.to/rahulxsingh/snyk-vs-semgrep-sca-platform-vs-custom-sast-rules-in-2026-3047 ; https://konvu.com/compare/snyk-vs-semgrep ; https://www.augmentcode.com/tools/best-ai-sast-tools
- Kodus, "8 Best AI Code Review Tools for Enterprise Teams (2026)" (CodeRabbit/Qodo/Greptile pricing) — https://kodus.io/en/best-ai-code-review-tools-enterprise-teams/
- Platform Monkey, "AI Code Review Agents in 2026" — https://platform-monkey.com/guides/ai-code-review-agents
- BestAIWeb, "AI Code Review Prerequisites: RAG, SAST, and LLM Limits" — https://www.bestaiweb.ai/prerequisites-for-ai-code-review-rag-static-analysis-and-the-hard-limits-of-llm-bug-detection/
- SmarterArticles, "The Ouroboros Machine: When AI Reviews Its Own Code" (Spracklen, Tenzai, CodeRabbit figures) — https://smarterarticles.co.uk/the-ouroboros-machine-when-ai-reviews-its-own-code
- The Fourths, "AI got faster at everything except writing secure code" (Veracode + CSA/Apiiro) — https://www.thefourths.com/article-ai-code-security-debt.html
- VibeDoctor, "35 CVEs in a Single Month" (CSA note, Vibe Security Radar) — https://vibedoctor.io/blog/ai-generated-cve-surge-2026-scan-before-you-ship
- Yu et al., "A.S.E 2.0" (accessed 2026-11-10) — https://arxiv.org/abs/2611.06294
- Google Cloud, "Helping you build and defend at machine-speed in the agentic era", 5 Nov 2026 (accessed 2026-11-10) — https://cloud.google.com/blog/products/identity-security/helping-you-build-and-defend-at-machine-speed-in-the-agentic-era
- Vercel Security Review coverage, 4 Nov 2026 (accessed 2026-11-10) — https://techtoheart.com/vercel-makes-every-push-a-security-checkpoint-for-ai-generated-code/
- Apiiro research, 5 Nov 2026, via coverage (accessed 2026-11-10) — https://www.aighten.com/en/blog/claude-code-dont-ask-again-secrets-leak-github and https://pasqualepillitteri.it/en/news/31165/claude-code-leaks-passwords-api-keys-github-apiiro
- Chen et al., "SecureVibeBench" (accessed 2026-11-11) — https://arxiv.org/abs/2509.22097
- CWE-bench v2, 3 Nov 2026, via AI Evolution summary of the Hugging Face blog (accessed 2026-11-11) — https://www.ai-evolution.com.au/article/cwe-bench-v2-more-coverage-quality-and-transparency-63945bc7
- SusVibes re-run via Medium, 2 Nov 2026 (accessed 2026-11-11) — https://medium.com/@FaithChihambakwe/what-share-of-ai-code-has-vulnerabilities-and-which-kind-does-a-human-review-reduce-it-268ff4531d05
- Yang et al., "SecPRBench" (arXiv:2610.33509, 24 Oct 2026; accessed 2026-11-12) — https://arxiv.org/abs/2610.33509

**Caveats:** pricing figures are list prices verified against vendor pages or secondary compilations as of Oct–Nov 2026 and change without notice — re-verify before budgeting. The agent-time enforcement category is ~6 months old; every effectiveness claim in it is vendor-run. The two numbers that would most change a buy-or-build decision — independent head-to-head detection rates, and the Fed/OCC/FDIC AI request for information — do not exist yet as of 2026-11-09.

---

## 2. Codebase sanitize / certification — CI-generated problems already in the codebase

Detecting and remediating defects CI-generated code has already left in an existing codebase.

### 2.1 How big the problem is

<details>
<summary><strong>Veracode — ~45% of AI code introduces a known flaw</strong> (Spring 2026) ●●●○</summary>

- Same benchmark as subject 1: only ~55% of AI code-generation tasks produce output free of a known flaw.
- XSS handled securely 15% of the time; log injection 12–13%.
- Java riskiest (72% failure rate). Newer, larger models scored no better than smaller ones.
- Syntax correctness now exceeds 95% while the security pass rate is flat for two years.
- *[Vendor-published benchmark, methodology disclosed.]*
</details>

<details>
<summary><strong>Secure Code Warrior AI Trust Index — 15 confirmed vulnerabilities per codebase, 4.3 severe</strong> (July 22, 2026) ●●○○</summary>

- 16 models, 1,760 codebases, 11 frameworks; method built with RMIT University for the first 6 models.
- Average **15 confirmed vulnerabilities per codebase, 4.3 severe**; 27,000+ confirmed findings; 86 unique CWEs.
- Top flaws: CWE-532 sensitive data in logs (8,543); CWE-79 XSS (2,949); CWE-798 hardcoded credentials (1,348).
- Model scores range from Claude Sonnet 5 (80.4) to GPT 5 Mini (21.6); no model wins on every framework.
- *[Vendor-published; methodology disclosed on the page; scans used Semgrep/Bearer/Bandit plus agentic false-positive verification. Verified against the live page 2026-11-09.]*
</details>

<details>
<summary><strong>SecureVibeBench — roughly half of test-passing AI code is vulnerable</strong> (Chen et al., ACL 2026, peer-reviewed) ●●●○</summary>

- Same benchmark as subject 1; for an audit of an existing codebase this is the quantification of what's already in there.
- Of agent-written code: 23.0% of all tasks were functionally correct but exploitable, against only 23.8% correct-and-secure.
- Memory safety dominates (71.6% of suspicious findings; heap buffer overflows 46.7% of the original vulnerabilities).
- Audit implication: a codebase audit cannot sample only failing or suspicious code — the vulnerable population is disproportionately inside the code that passes tests.
- Prioritise exploit-verification (dynamic proof-of-vulnerability harness) on AI-authored modules, memory-unsafe languages first.
</details>

<details>
<summary><strong>A.S.E 2.0 — a green test suite on AI-written code is weak evidence of security</strong> (arXiv:2611.06294, Nov 2026; preprint) ●●○○</summary>

- 145 repo-level tasks from real CVEs; secure = tests pass **and** a validated proof-of-concept exploit fails.
- Claude Code (Sonnet 4.5): 74.0% functional pass, 18.4% secure — **55.6% passed every test while a working exploit still succeeded**.
- Agents saw the relevant safeguard in only 27–36% of trajectories; putting it in context roughly doubled secure output (24.8% vs 12.6%).
- The audit must include exploit-verification (or equivalent adversarial validation) on AI-authored modules, and remediation should include annotating safeguards in agent context so future agent edits see them.
</details>

<details>
<summary><strong>SecPRBench — agentic review misses 22–68% of vulnerability-introducing changes</strong> (arXiv:2610.33509, 24 Oct 2026; preprint) ●●○○</summary>

- Same benchmark as subject 1; for an audit of an existing codebase this is the measured miss rate of the review layer itself.
- Best agents (Grok 4.6, GPT-6 sol, GLM 5.3, Claude Opus 5.5) find ~3 in 4 vuln-introducing changes; the weakest finds ~1 in 3.
- 68% of misses are wrong-mechanism reasoning — the reviewer looked at the right file and argued the wrong flaw — so a clean review is weak evidence, and location-based scoring would overstate detection.
- Audit implication: a codebase audit cannot rely on agentic PR review as the control; exploit-verification and deterministic scanning remain the backstop, and the review layer needs sampling of what it let through.
</details>

<details>
<summary><strong>Independent PR analysis — AI code carries 2.74× the vulnerabilities</strong> (470 GitHub PRs, reported 2026) ●○○○</summary>

- AI-written code carries **2.74× the vulnerabilities** of human-written code and 1.7× more major issues.
- *[Secondary reporting; indicative, not a named primary study.]*
</details>

<details>
<summary><strong>Apiiro — 322% more privilege-escalation paths in AI-assisted repos</strong> (Fortune 50 codebases) — [VENDOR STUDY] ●●○○</summary>

- 322% more privilege-escalation paths and 40% more secrets exposure in AI-assisted repositories.
</details>

<details>
<summary><strong>UTSA / Virginia Tech / Oklahoma — 19.7% of package references don't exist</strong> (academic, 576,000 samples) ●●●○</summary>

- **19.7% referenced a package that does not exist**, 205,000+ unique fictional names.
- This is the hallucinated-dependency supply-chain vector.
</details>

<details>
<summary><strong>Black Duck OSSRA 2026 — mean vulnerabilities per codebase 581, up 107% year-on-year</strong> (audit of 947 commercial codebases) ●●●○</summary>

- Mean vulnerabilities per codebase **581, up 107% year-on-year** — the sharpest jump in the report's history.
- 68% of codebases have open-source license conflicts (highest ever).
- 97% of organisations now use AI coding assistants in production software.
- Black Duck explicitly attributes the surge to AI-accelerated code creation.
- *[Vendor-published audit.]*
</details>

<details>
<summary><strong>GitClear — "The Maintainability Gap"</strong> (Jan 2026, 623M code changes, 2023–2026) ●●○○</summary>

- Refactoring ("moved code") fell from 21% of changed lines (2022) to **3.8%**.
- Copy/pasted lines rose 9.4% → 15.7%.
- Duplicate blocks +81% (40.3 → 73.0 per million changed lines).
- Two-week churn +15%.
- *[Vendor research, commit-history based.]*
</details>

<details>
<summary><strong>Google DORA — the "verification tax"</strong> (2024–2026, survey-based, correlational) ●●●○</summary>

- 2024: every +25% AI adoption associated with −1.5% throughput and −7.2% delivery stability.
- 2025: 90% of professionals using AI (~2 h/day); adoption now correlates with *higher* throughput but still *lower* stability.
- By 2026 the cost is described as a "verification tax" — time saved generating is re-spent auditing.
</details>

<details>
<summary><strong>Sonar — 96% don't fully trust AI output, only 48% always review it</strong> (2026 State of Code survey, 1,100+ developers) ●●○○</summary>

- 96% do not fully trust AI output, yet only 48% always review it before committing.
</details>

<details>
<summary><strong>Georgia Tech Vibe Security Radar — 74 CVEs traced directly to AI coding tools</strong> (reported Sept 2026) ●●○○</summary>

- 74 CVEs traced directly to AI coding tools; 35 logged in March 2026 alone.
</details>

<details>
<summary><strong>Escape.tech — 2,038 critical vulnerabilities in 5,600+ publicly deployed AI-built apps</strong> — [VENDOR RESEARCH] ●●○○</summary>

- 2,038 critical vulnerabilities, 400+ leaked secrets, 175 instances of exposed personal data including medical records and IBANs.
</details>

<details>
<summary><strong>Real incidents</strong> ●●●○</summary>

- Lovable, CVE-2025-48757 (broken object-level authorisation) exposed 170+ apps to unauthenticated database access.
- March 2026: the GitHub Action for Trivy (a security scanner) was backdoored, running inside LiteLLM's CI — the scanners themselves are now supply-chain targets.
- Postman Desktop 12.33.4 (Oct 2026): opening the app auto-installed Postman plugins into Claude Code and Codex, approved its own Codex startup hook, added a remote MCP endpoint (mcp.postman.com) and a CLI — all without asking. No data exfiltration shown; Postman said 5 Nov 2026 it is reverting the change. The agent layer's own config (plugins, hooks, MCP servers) is a supply-chain surface no code scanner sees.
</details>

<details>
<summary>See also</summary>

[1.6 Benchmarks & evidence](#16-benchmarks--evidence) (the benchmarks behind these numbers) · [1.5 Best practice](#15-best-practice--critical-systems-in-finance) (the three-layer gate that catches the test-passing-but-vulnerable class) · [3.4 Governance — finance](#34-governance--finance) (the Postman incident — the agent layer's own config as a supply-chain surface, and what governance has to cover).
</details>


### 2.2 Problem classes

| Class | What it looks like | Detection |
|---|---|---|
| Injection & broken access control | SQLi, XSS, SSRF, BOLA/IDOR, missing permission checks | SAST taint analysis (Semgrep, CodeQL, Snyk Code, SonarQube); DAST in staging |
| Hardcoded secrets | Keys/tokens in source, logs, or config the model "needed for a working example" | Secret scanners pre-push (Gitleaks, TruffleHog, GitGuardian, GitHub Advanced Security) |
| Hallucinated dependencies | Imports of packages that don't exist — an attacker can register the name | Manifest audit against registries; phantom-import checks (Skylos, ai-slop-detector); lockfile review |
| Hallucinated APIs / ghost routes | Calls to SDK methods, endpoints, or helpers that don't exist; code that compiles but calls nothing | AI-specific detectors (VibeCheck engines, Skylos verify); contract tests; dead-code analysis |
| Subtle logic errors | Wrong authorisation semantics, off-by-one/edge cases, error masking (empty except, swallowed errors) | LLM PR review (CodeRabbit, Qodo, Copilot review) + human review + property/mutation testing |
| Insecure design | Missing validation, unsafe defaults, weak crypto, over-broad permissions | Threat modelling, architecture review, reasoning-based full-repo agents (AWS Security Agent) |
| Technical debt | Duplication instead of refactoring, comprehension debt (code nobody understands), pattern divergence, unmaintained AI-written modules | GitClear-style commit metrics: moved-code %, duplication (jscpd/PMD CPD), 30-day rework rate, mutation score |
| IP / license exposure | Output substantially derived from copyleft sources without attribution; 68% of commercial codebases now have license conflicts (Black Duck) | SCA + license scanning on the AI-authored subset (Black Duck Detect, Snyk, Sonatype); only 54% of orgs evaluate AI code for IP/license risk at all |

### 2.3 Products & services

| Product / service | What it does for already-shipped AI code | Pricing / availability |
|---|---|---|
| **Snyk** (Code, Agent Fix, Evo) | SAST/SCA/secrets across the whole codebase; Agent Fix generates a fix, re-scans it, and loops on failure (new agentic architecture, May 26, 2026). "Generator can't be the validator" positioning. Leader, Forrester Wave: Agentic Development Security Tools, Q4 2026. | Free tier; Team from $25/mo. Snyk product data: new critical/high issues up 10× in a year; ~8 new issues introduced per 1 remediated — **vendor's own data**. |
| **AWS Security Agent** (part of AWS Continuum) | Full-repository code review in **preview** (announced May 12, 2026): reasoning-based analysis of architecture, trust boundaries and data flows, not pattern matching; validates findings in simulated environments; generates fix commits. PR scanning, STRIDE threat modelling also in preview. On-demand pen testing is GA. | Code review free in preview (reported 1,000 scans/mo — confirm in console); pen testing GA at $50/task-hour. Regions: us-east-1, us-west-2, eu-west-1, eu-central-1, ap-southeast-2, ap-northeast-1. GitHub/GitLab/Bitbucket + Confluence; Kiro and Claude Code plugin, MCP. |
| **Qodo** (ex-CodiumAI) | Multi-agent PR review (bug/security/quality/coverage agents), self-learning team rules enforced at review; Qodo 2.0, Feb 2026. | From $30/mo (Pro Team); pricing checked Oct 2026 — verify with vendor. |
| **SonarQube** | Deterministic quality gates on CI-generated code; AI fixes inside CI gates; v26.2.0, Feb 2026. The "deterministic" counterweight to LLM reviewers. | Community free; commercial tiers priced by lines of code — verify. |
| **Semgrep** | SAST + SCA + secrets, cross-file dataflow, 3,000+ community rules, 30+ languages; AI triage of findings. | Community Edition free/open source (14,300+ GitHub stars); paid tiers. |
| **CodeRabbit** | AI PR review with codebase-wide semantic index; finds cross-file issues; Autofix with build verification. | Free tier (unlimited repos, 200 files/hr, 4 PR reviews/hr); paid tiers. |
| **GitHub Copilot code review** | Agentic PR review with full repo context; 60M reviews by March 2026 (10× growth since April 2025); actionable feedback in 71% of reviews; Low/Medium tiers. **Diff-only — weakest in independent testing on cross-file bugs.** | Included in Copilot Pro; Business $19/seat/mo. |
| **Checkmarx / Veracode** | Enterprise SAST/SCA; Veracode's 2026 State of Software Security (1.6M apps): 82% of organisations now carry security debt, +11 pts YoY. | Enterprise pricing on request. |
| **DeepAudit** (open source) | Multi-agent vulnerability discovery across whole repos. | Free; ~4,900 GitHub stars by March 2026; 49 CVEs found across 16 OSS projects. |
| **Google DeepMind CodeMender** | Agentic remediation with vulnerability verification and exploit simulation in a sandbox/isolated VM; human-in-the-loop for writes; scoped whole-repo / folder / changed-files-only scans. Now the leading managed option for exploit-verified fixes. | **In public preview since July 2026** (not a product yet). 72 security fixes upstreamed in six months, codebases up to 4.5M lines — **vendor-reported**. No independent accuracy data. |
| **Alibaba Agentic Code Security** (May 2026) | Dual-agent: scanning agent + verification agent that simulates attack paths to confirm exploitability and filter false positives. | China-market; availability outside China unclear. |
| **VibeCheck** (VS Code ext.) | 16 detection engines aimed at AI-specific failures: ghost routes, phantom deps, API hallucinations, hardcoded secrets; local Ollama first, then cloud. | Free plan with daily scan quota via cloud API. Small vendor; claims unverified. |
| **Skylos** (open source, Apache-2.0) | CLI + PR gate, 12 languages: dead code, security, secrets, dep CVEs, and AI-code mistakes (missing guards, fake helpers, invented APIs, impossible versions); "AI hallucination contracts" verify generated code against repo symbols/APIs. | Free. |
| **ai-slop-detector** (PyPI, v3.0.2) | 25 patterns in 5 categories; phantom-import detection; self-calibrating scoring. | Free, niche open-source project. |
| **Cisco AI Agent Security Scanner / Snyk agent-tool scanning** | Scans the agent layer itself — MCP servers, skills, agent tooling — rather than the code it wrote. | Cisco: pricing not published. |
| **GrowExx** (services) | AI code audit & cleanup engagements; 4-tier framework (security scan → production-readiness audit → expert review → ongoing QA); fixes land in your repo, critical first; ISO 27001:2022-certified process. | Services; 48 h for an MVP-scale codebase; pricing on request. |

**Stacking is the 2026 norm, not single-tool:** PR review (CodeRabbit/Copilot/Qodo) + deterministic gates (SonarQube) + security scanning (Semgrep/Snyk) — the layers cover different ground and don't conflict.

### 2.4 Techniques

- **Whole-codebase scanning:** run SAST/SCA/secrets/DAST on the full repo on every commit, not at release — the failure modes are detectable by taint analysis, and a finding at commit-time costs minutes versus hours post-incident. Full-repo reasoning agents (AWS Security Agent) are the new layer above pattern SAST; they find cross-module trust-boundary violations pattern tools miss. **No independent accuracy data published yet for any reasoning agent — all vendor claims.** CWE-bench v2 (Nov 2026) now gives a public yardstick — leaders ~68% pass@1, even the leader fails 19% of tasks on every attempt.
- **Provenance / attribution:** retrospective identification is weak. What works is capture-at-write-time:
  - Claude Code writes `Co-Authored-By` trailers by default.
  - **git-ai** stores line-level attribution (tool, model, session) in `refs/notes/ai`, surviving amend/rebase/squash in local testing.
  - **OmniType** tags lines as human/AI/paste from editor input, stored as git notes.
  - Git hooks + commit conventions (`AI_TOOL` env var, `prepare-commit-msg` trailer injection, non-human author identity for autonomous commits).
  - Without this, attribution is commit archaeology — keyword parsing, PR comment history, stylistic heuristics.
  - **There is no reliable post-hoc "AI code detector" for code; any vendor claiming one is selling a heuristic.**
- **Remediation:** generate → verify → loop. Snyk Agent Fix and Copilot Autofix both re-scan generated fixes; Snyk's golden tests require FAIL→PASS on the vuln and PASS→PASS on existing tests. Rule for finance: **never let the generator validate its own fix** — independent scan + full test suite + human sign-off on high-risk paths. AWS Security Agent generates fix commits directly into the Git workflow; private repos only for automated remediation (disabled on public repos).
- **Regression testing of AI-written code:** generate tests for AI-heavy files (Qodo); apply **stricter thresholds to AI-authored modules** than the codebase average (industry practice reported 2026: 85% coverage where the baseline is 70%); mutation testing to separate real tests from coverage theatre; property-based and contract tests for hallucinated-API risk; DAST (OWASP ZAP) in staging; re-run the full suite on every remediation.
- **Dependency verification:** audit every manifest entry — confirm each package existed before the agent suggested it; `npm audit` / `pip-audit` / Dependabot / OWASP Dependency-Check; check lockfiles; treat an unfamiliar package name as a stop-and-verify, not an install.
- **Secrets in agent artefacts (new vector, Nov 2026):** scan agent settings files, transcripts and full git history for credentials. Claude Code's "Don't Ask Again" writes the literal approved command, secrets included, into `.claude/settings.local.json`; 1,122 of 104,185 public copies held a real secret; gitleaks and TruffleHog together missed 215 of them. Secrets persist in history and forks — deleting the file now does not close the exposure. Check project `.gitignore` (Claude Code excludes the file only via the developer's global git-excludes); rotate anything found.
- **Audit method (services):** measure four numbers, not opinions — duplication (clone threshold), shallow-error-handling density per 1,000 lines, mutation score, and 30-day rework rate.

<details>
<summary>See also</summary>

[1.3 What they catch](#13-what-they-catch) (what pre-commit scanning catches, and its stated confidence limits) · [1.6 Benchmarks & evidence](#16-benchmarks--evidence) (CWE-bench v2 as the yardstick for remediation agents; the Apiiro agent-settings secrets vector, also recorded there).
</details>


### 2.5 Best practice — finance

- **Gate everything in CI as a required step:** SAST, SCA, DAST, secrets — blocked merge on failure for critical paths; pre-commit hooks with SAST + secret rules so the commit never lands.
- **Human review is not a security control on its own** (NCC Group, verified live page 2026-11-09): reviewers miss hidden instructions (whitespace, Unicode, markdown), interfaces that show one action while the model does another, and excessive trust in model output under high-volume review. Automated checks + adversarial testing + AI-focused pen testing are the control; humans validate the controls.
- **Separate recommendation from enforcement:** business rules, approval requirements and policy enforcement must operate independently of model recommendations; deterministic controls run before any action executes (NCC Group).
- **Record complete decision histories:** inputs, outputs, approvals, policy evaluations — auditable evidence for every AI-influenced decision. EU AI Act Art. 19 requires automatically generated logs for high-risk systems to be retained ≥ 6 months.
- **Agent-to-agent:** explicit input/output contracts per agent, trust boundaries, provenance validation, privilege limits, validation checkpoints between critical stages — each interaction is a control point, not an assumed trust relationship (NCC Group).
- **Regulatory state, US (as of Nov 2026):** **SR 11-7 is dead.** On April 17, 2026 the Fed, OCC and FDIC replaced it with **SR 26-2** (OCC Bulletin 2026-13; FDIC FIL-15-2026). Generative and agentic AI are **explicitly out of scope** — "novel and rapidly evolving" — and banks are told their own risk management should govern them. The agencies promised a request for information on AI model risk; **not issued as of Oct 16, 2026**. SR 26-2 is risk-based, most relevant above $30B in assets, and sets no enforceable standards. Practical consequence: **there is currently no US supervisory model-risk framework covering CI-generated code — firms must self-govern, and examiners will judge the framework you built.** Also pending: four agencies' Sept 11, 2026 proposal to replace 2023 third-party risk guidance (comments closed Nov 16, 2026).
- **NYDFS (directly relevant in NYC):** Oct 16, 2024 industry letter — no new requirements, but Part 500 risk assessments (§500.9) must address the firm's own AI use, vendor AI, and AI-application vulnerabilities, and third-party diligence (§500.11) must cover AI providers. Plus the 21 May 2026 Industry Letters directing strengthened testing of CI-generated code prior to production (see subject 1, [1.5.2](#152-provenance-audit-trail-and-regulation)).
- **EU:** EU AI Act — chatbot disclosure (Art. 50) in force since Aug 2, 2026; Annex III high-risk obligations (including credit scoring) moved to **Dec 2, 2027** by the Digital Omnibus, Reg. (EU) 2026/1744 (in force July 27, 2026); penalties up to €35M or 7% of global turnover. DORA has applied since Jan 2025.
- **Peer regulators:** OSFI (Canada) AI Bulletin, July 13, 2026, plus Frontier AI Guidance, May 2026 (ITSAP.10.050) — map AI risks onto existing B-13/E-21/B-10 guidelines; clear ownership of every AI lifecycle step; human oversight; data governance; agent access rights; third-party AI dependencies. Useful template for a US firm's self-governance framework.
- **UK NCSC:** May 1, 2026, CTO Ollie Whitehouse — "prepare for a vulnerability patch wave": AI is surfacing decades of latent flaws faster than patching infrastructure can absorb; the window from disclosure to exploitation has shrunk to hours for critical flaws. June 18, 2026: "Vibe Coding Spectrum" framework. May 12, 2026: "ten questions to ask before using AI to find vulnerabilities." Nov 3, 2026: AI-powered malware ransomware attack on UK critical national infrastructure judged "highly likely" by 2028. **For a finance dev shop this is a capacity warning: patch throughput is now a board-level operational risk.**
- **Frameworks to anchor to:** NIST AI Risk Management Framework + GenAI Profile (NIST-AI-600-1); ISO/IEC 42001; OWASP GenAI Security Project Top 10 (prompt injection the #1 risk for the third consecutive year, backed by a ~10,000-incident database); Governance-as-Code — deterministic guardrails (prompt filtering, state-transition validation as a circuit breaker) embedded in CI/CD.
- **KPIs to track:** vulnerability density in AI-authored vs human-authored code; secrets-exposure rate; rework/churn rate; moved-code % and duplication; fix rate vs new-issue rate; delivery stability (change failure rate, time to recover).

<details>
<summary>See also</summary>

[1.5 Best practice — critical systems in finance](#15-best-practice--critical-systems-in-finance) (provenance and audit trail for new code) · [3.4 Governance — finance](#34-governance--finance) (OCC 2026-54, MAS, HKMA SAGE, UK loss-of-control — the regulatory picture now filling the gap).
</details>


### 2.6 Hype vs verified

- **Vendor-published but methodologically transparent, treat as directional:** Veracode 45%, SCW 15/codebase (partly RMIT-partnered), Black Duck OSSRA (audit, not survey), GitClear (commit-history data), DORA (survey, correlational).
- **Preprint, method transparent, not peer-reviewed:** SecPRBench recall figures (arXiv:2610.33509, Oct 2026) — LLM-as-judge scoring by Claude Opus 5.5; the judge's verdicts, not execution.
- **Vendor's own benchmarks on its own tests, not independent:** Snyk Agent Fix 82.5% golden-test pass; Snyk's 8:1 new-issues-to-fixes ratio; AWS "reasons like a human security researcher"; CodeMender's 72 upstreamed fixes; Apiiro's 322% figure.
- **Analyst forecasts, not measurements:** Gartner — 60% of all new code AI-generated by end of 2026; prompt-to-app defects +2,500% by 2028; 40% of enterprises on consumption-priced AI tools facing 2× budget overruns by 2027.
- **NOT verified — do not use:** a claim circulating in low-quality roundups that "SITS2026" is a mandatory national standard for AI-assisted coding in finance/healthcare since March 2026. No corroboration found in any primary or reputable secondary source; single-source, likely unreliable.
- **Cautionary example — CI-generated compliance content getting regulation wrong:** a 2026 guide (quizforml.com) asserts SR 11-7 "mandates continuous automated evaluation" for LLM pipelines in banking. False — SR 11-7 was rescinded in April 2026 and its replacement excludes generative AI. Any compliance claim about AI in banking should be checked against the bulletin itself, not against secondary summaries.
- **Pricing:** figures above were checked Oct 2026 (Superblocks) or are vendor-published; several vendors changed tier structures in 2026 — verify before committing.

### 2.7 What this means in practice

- The audit/remediation market is real and available now: services (4-tier audits, 48 h MVP turnaround), tooling integration, and "AI code audit as a service" for finance firms who must demonstrate control to examiners and counterparties.
- For a firm building finance-critical systems, demonstrable AI-code governance — provenance capture, gated CI, verified remediation, complete audit trail — is becoming a procurement and examiner expectation, not a differentiator. The SR 26-2 gap is the opening: banks have no supervisory framework for AI code and must build their own; a firm that arrives with one (mapped to NIST AI RMF, NYDFS Part 500, OSFI's bulletin) has a concrete proposition.
- What to watch: the SR 26-2 follow-up RFI on AI (still pending); EU AI Act Dec 2027 obligations; NCSC patch-wave volume (whether patch throughput becomes a reported operational metric); independent accuracy data for full-repo reasoning agents (CWE-bench v2 now gives a yardstick — no product yet independently measured at scale); and whether any post-hoc AI-code detector survives independent evaluation.

<details>
<summary>See also</summary>

[3.4 Governance — finance](#34-governance--finance) (the regulatory picture now fills the SR 26-2 gap from three directions — the sharpened sell).
</details>


### Sources — subject 2 (accessed 2026-11-09 unless noted)

- Secure Code Warrior, AI Trust Index — https://www.securecodewarrior.com/product/ai-trust-index (launched July 22, 2026; verified live 2026-11-09)
- NCC Group, "AI Security in Financial Services: Four Areas Where Control Gaps Are Emerging" — https://www.nccgroup.com/ai-security-in-financial-services-four-areas-where-control-gaps-are-emerging/ (verified live 2026-11-09)
- Veracode, 2026 GenAI Code Security Report (Spring 2026) — cited via https://valueaddvc.com/blog/ai-generated-code-quality-security-risks-testing-overhead-and-what-ctos-are-doing and https://for.you.com/posts/ai-code-review-gap-developers-distrust-ai-code-but-skip-077bdcb4
- AWS, "AWS Security Agent full repository code scanning feature now available in preview," May 12, 2026 — https://aws.amazon.com/blogs/security/aws-security-agent-full-repository-code-scanning-feature-now-available-in-preview/
- AWS, "AWS Security Agent adds threat modeling, Kiro power and Claude Code plugin" — https://aws.amazon.com/blogs/aws/aws-security-agent-adds-threat-modeling-kiro-power-and-claude-code-plugin-and-more/
- Snyk, "New Agentic Architecture for Snyk Agent Fix" (May 26, 2026) — https://snyk.io/blog/snyk-agent-fix-agentic-architecture/
- Snyk, Forrester Wave Leader, Agentic Development Security Tools, Q4 2026 — https://snyk.io/blog/snyk-named-leader-forrester-wave-agentic-development-security-tools-q4-2026/
- Syntrox, "SR 11-7 for AI Agents: Model Risk Management After SR 26-2" (Oct 29, 2026) — https://www.syntrox.io/blog/sr-11-7-model-risk-management-ai-agents
- BotMinds, "SR 11-7 and Generative AI: What SR 26-2 Changed for LLMs" (Oct 2026) — https://www.botminds.ai/guides/sr-11-7-and-generative-ai
- Sumatsoft, "AI in Banking After SR 11-7 and SR 26-2" (Oct 19, 2026; verified Oct 16, 2026) — https://sumatosoft.com/blog/ai-in-banking-compliance
- Legal500, "Managing the AI Risks in the Financial Sector: OSFI's Bulletin" — https://www.legal500.com/intelligence/canada/technology/managing-the-ai-risks-in-the-financial-sector-osfis-bulletin-on-generative-and-agentic-artificial-intelligence
- Superblocks, "9 Best AI Code Governance Tools for Enterprises in 2026" (pricing checked Oct 2026) — https://www.superblocks.com/blog/ai-code-governance-tools
- Jellyfish, "23 Best AI SDLC Tools" (Oct 1, 2026) — https://jellyfish.co/library/best-ai-sdlc-tools/
- Matt Goodrich, "Who Wrote This Code? A Layered Approach to AI Attribution and Provenance" (June 6, 2026) — https://github.com/mgoodric/mattgoodrich.com/blob/HEAD/content/posts/ai-code-attribution-and-provenance/index.md
- Bruniaux, "AI Code Traceability & Attribution" (updated Nov 8, 2026) — https://cc.bruniaux.com/guide/ai-traceability/
- EASM News, "NCSC Patch Wave: An External Readiness Checklist" — https://www.easm.news/ncsc-patch-wave-external-readiness/
- Cybersecurity Insiders, "The Same AI That Writes Your Code May Be the Worst Reviewer of It" (Sept 29, 2026) — https://www.cybersecurity-insiders.com/the-same-ai-that-writes-your-code-may-be-the-worst-reviewer-of-it/
- GitClear, "The Maintainability Gap" (Jan 2026) — cited via https://www.nazarboyko.com/articles/ai-tech-debt-bill-comes-due-in-2027 and https://shantiinfosoft.com/blog/ai-generated-code-technical-debt-audit/
- GrowExx, "AI Code Audit | Vibe Code Cleanup" — https://www.growexx.com/ai-code-audit/
- Skylos (open source) — https://glama.ai/mcp/servers/duriantaco/skylos
- VibeCheck, VS Code Marketplace — https://marketplace.visualstudio.com/items?itemName=Vibecheck-AI.vibecheck-ai
- Yu et al., "A.S.E 2.0" (accessed 2026-11-10) — https://arxiv.org/abs/2611.06294
- Apiiro research, 5 Nov 2026, via coverage (accessed 2026-11-10) — https://www.aighten.com/en/blog/claude-code-dont-ask-again-secrets-leak-github and https://pasqualepillitteri.it/en/news/31165/claude-code-leaks-passwords-api-keys-github-apiiro
- Google Cloud, 5 Nov 2026 (accessed 2026-11-10) — https://cloud.google.com/blog/products/identity-security/helping-you-build-and-defend-at-machine-speed-in-the-agentic-era
- Chen et al., "SecureVibeBench" (accessed 2026-11-11) — https://arxiv.org/abs/2509.22097
- CWE-bench v2, 3 Nov 2026, via AI Evolution summary of the Hugging Face blog (accessed 2026-11-11) — https://www.ai-evolution.com.au/article/cwe-bench-v2-more-coverage-quality-and-transparency-63945bc7
- Yang et al., "SecPRBench" (arXiv:2610.33509, 24 Oct 2026; accessed 2026-11-12) — https://arxiv.org/abs/2610.33509
- Postman auto-install incident, Oct–Nov 2026, via coverage (accessed 2026-11-12) — https://kernelpost.com/postman-ai-plugin-consent/ and https://dev.to/slabb/postman-silently-installed-itself-into-claude-code-and-codex-the-log-lines-the-self-approving-16dc

---

## 3. CIAC — creation, governance, management

By late 2026 the multi-agent field has consolidated around a handful of frameworks, the supervisor pattern is the production default, and the binding constraint is reliability, not capability: the best agents succeed once far more often than they succeed every time. Governance has shifted from model oversight to runtime control — deterministic gates before execution, scoped permissions, tamper-evident audit trails — and finance regulators have now spoken in several documents, most consequentially the US agencies' decision to *exclude* agentic AI from the new model-risk guidance, leaving firms to govern it themselves.

### 3.1 Frameworks & platforms

| Framework / platform | Model | Maturity / status (as of 2026-11-09) |
|---|---|---|
| **LangGraph** (LangChain) | Explicit state graph: nodes, edges, typed shared state; checkpointer for resume/replay | 1.0 Oct 2025, 1.1 Dec 2025. Widest production use; best debugging story (state snapshots, replay). MIT library; managed deployment via LangSmith Deployment (Cloud/BYOC/self-hosted, Enterprise for BYOC/self-host). |
| **CrewAI** | Role-based crews: agents with roles/goals/tasks, sequential or hierarchical | Active (v1.15.21, Sep 2026). Fastest to a prototype (~20 lines); weakest production evidence of the three majors per Microsoft's own comparison. MIT library + hosted product. |
| **Microsoft Agent Framework** | Workflow graph + conversation; hub-and-spoke, concurrent | 1.0 GA 3 Apr 2026 (Python + .NET). Successor to both Semantic Kernel and **AutoGen**, which Microsoft moved to maintenance mode Oct 2025 and archived — do not start new work on AutoGen despite its ~61k GitHub stars. Native Foundry integration, managed identity. |
| **OpenAI Agents SDK** | Minimal: agents, handoffs, guardrails, tools; agents call agents as tools | Successor to experimental Swarm (Mar 2025). Handoffs are one-way control transfer via tool call — transparent, but not native parallel orchestration. Limited built-in RBAC/governance; compliance evidence must come from another layer. MIT. |
| **Google ADK** | Hierarchical tree: root agent → sub-agents, each with own tools/memory | Released Apr 2025 (Python, TS, Go, Java). Native **A2A protocol** support — an ADK agent can invoke agents built on LangGraph/CrewAI/etc. Multimodal; Vertex AI / Agent Engine managed deployment. |
| **Claude Agent SDK / Claude Code** | Subagent model; "Swarm Mode" released early 2026 | Vendor tooling; supervisor pattern at the tooling level. Reported in blogs, not independently verified. |
| **AG2** (AutoGen fork), **MetaGPT**, **ChatDev** | Conversation/SOP-based | Older generation; AG2 continues the AutoGen line for existing users. |
| **Managed platforms** | Azure AI Foundry Agent Service, LangGraph Platform, Vertex AI Agent Engine, AWS Bedrock/agent-squad | The deployment/governance layer above the frameworks; this is where enterprise buyers increasingly land. |

### 3.2 Interoperability standards

- **MCP** (Anthropic Nov 2024; OpenAI Mar 2025; Google Apr 2025; donated to the Linux Foundation Dec 2025) is now the universal tool-integration standard.
- **A2A** (Google, Apr 2025) is the cross-framework agent-interop protocol.
- Both are real and adopted; they are what make mixing frameworks feasible. This is the most consequential 2025 development in the field.

### 3.3 Orchestration patterns

- **Supervisor / orchestrator-worker (the 2026 production default).** A lead agent decomposes, dispatches to 3–5 parallel specialists with separate context windows, synthesizes. Star-shaped; the orchestrator is the single point of coordination *and* failure. Anthropic's Research system is the canonical example; Anthropic reports ~90% improvement over a single agent on BrowseComp — **vendor claim, its own benchmark**.
- **Hierarchical / manager-of-managers.** Supervisors nest recursively. Powerful for deep decomposition; latency and token cost multiply geometrically and error compounds at every layer.
- **Pipeline / sequential.** Fixed role handoffs (MetaGPT's "Code = SOP"). Oldest pattern; still the most abused — errors propagate forward with no correction.
- **Swarm / handoff.** Peer agents transfer full control (OpenAI Swarm/Agents SDK). No central orchestrator. In practice most marketed "swarms" are supervisor-with-handoffs.
- **Debate.** Agents argue the same task; a judge arbitrates. **Does not beat single-agent baselines at equal compute** once thinking-token budgets are equalized (reported in a 2026 technical review); the one reliably beneficial ensemble intervention is model heterogeneity. Costs ~2.5× single-model baseline before the judge (blog estimate).
- **Mesh / peer-to-peer.** Any agent can talk to any agent. Maximum flexibility; message volume scales O(N²); prone to deadlock/livelock.
- **Market / auction (Contract Net Protocol, 1980).** Tasks announced, agents bid. Canonical reference; rarely used in production LLM systems.
- **Graph-based orchestration** (LangGraph subgraphs) is where architectural momentum sits in 2026; MultiAgentBench (Zhu et al., ACL 2025) found graph structure best in a research scenario — academic, not production evidence.

**Failure signatures to design against:**
- Compounding error across nondeterministic hops (pⁿ).
- Partial-failure aggregation (one branch fails, the synthesis silently degrades).
- Cost: multi-agent runs consume roughly 15× the tokens of a single chat (blog estimate, chierhu/Medium).
- A UC Berkeley MAST study is reported to have found 41%–86.7% failure rates across seven popular frameworks — **reported via a Medium technical report, not independently verified**.

### 3.4 Governance — finance

#### 3.4.1 The converged control pattern

Five oversight patterns, per a 2026 survey of regulated-industry practice:
1. Human gates on *consequential* actions only — gate nothing and you fail supervision, gate everything and you rebuild the manual process.
2. Audit trails a regulator can replay.
3. Scoped permissions.
4. Deterministic fallbacks.
5. Model-risk documentation.

**The specific control that matters most:** put the gate *outside the model*. A model proposes a tool call; a deterministic gate decides whether it may run; anything consequential waits for approval that a named person signed for those exact arguments, written to a tamper-evident audit log. Text — including an automated "Please proceed" message — cannot authorise anything. Between Sep–Oct 2026 the major frameworks shipped pre-tool-use controls in response to this (Anthropic Managed Agents `auto` permission policy, Pydantic AI `ToolCallJudge`, plus LangChain/Google/Microsoft controls — per the Braiviq playbook, Oct 2026). The UK AI Security Institute reported (28 Sep 2026, per the same playbook) a frontier model completing a simulated supply-chain attack in 29.2% of runs after treating an automated "proceed" message as permission — **reported, not independently verified**.

**Agent identity:** an agent should inherit the permissions of the person authorising it, not a separate standing credential; every action must be attributable to a specific accountable person — "the AI did it" is not an audit trail.

#### 3.4.2 Regulation

<details>
<summary><strong>FINRA 2026 Annual Regulatory Oversight Report (9 Dec 2025)</strong> ●●●●</summary>

- New standalone GenAI section names AI agents an emerging risk: autonomy without human validation, scope creep beyond intended authority, auditability of multi-step reasoning, sensitive-data handling, insufficient domain expertise, plus existing GenAI risks.
- Ties deployment to supervisory controls under **Rule 3110**.
- Not rulemaking itself — the underlying rule binds.
</details>

<details>
<summary><strong>Fed/OCC/FDIC SR 26-2 (17 Apr 2026) — generative and agentic AI expressly out of scope</strong> ●●●●</summary>

- Supersedes SR 11-7, the model-risk framework US banks ran for fifteen years.
- **Footnote 3 explicitly places generative and agentic AI outside its scope** — "novel and rapidly evolving" — and points firms to their own governance for anything it does not cover.
- Corroborated across multiple independent secondary sources.
- Practical consequence: no US model-risk clause compels a per-decision record from a bank AI agent; the bank sets that bar itself.
</details>

<details>
<summary><strong>OCC Bulletin 2026-54 — "Super Intelligence: Supervisory Framework" (4 Nov 2026)</strong> ●●●●</summary>

- A 20-page examiner resource for OCC examiners at national banks, federal savings associations and federal branches/agencies, issued with News Release 2026-97.
- Covers exactly the generative and agentic systems SR 26-2 excluded: sixteen components in six pillars (purpose, risk, control, oversight, resilience, assurance).
- Four-tier consequence-based risk classification: an autonomous payment agent is Tier 1 "regardless of how well it performs in testing"; an internal productivity tool is Tier 4.
- Examiner considerations named include kill switches, circuit breakers, provider-agent limits, human-in-the-loop / human-on-the-loop controls with real authority, MRM extensions for non-deterministic systems, adversarial and hallucination testing, reconstructable records, and independent audit.
- **Sets no supervisory expectations for banks, no enforceable standards and no prescriptive requirements** — it is an examiner lens, not a rule — but it is the first US federal document telling examiners what to look at in agentic AI.
- The original finding — "no US model-risk umbrella" — still holds as law; it no longer holds as examination practice. A firm that maps its agentic governance to the sixteen components has a concrete, examiner-shaped case to make to national banks.
</details>

<details>
<summary><strong>CSBS Artificial Intelligence Supervisory Framework (16 Sep 2026) — state examiners get written AI procedures</strong> ●●●●</summary>

- Published by the Conference of State Bank Supervisors for state-chartered banks and state-licensed nonbank financial institutions — state regulators supervise **79% of all US banks**.
- Five documents: Core Examiner Guide, Examiner Work Program, non-bank supplements, an AI Use Case Risk-Tiering Worksheet, and sources.
- Gives examiners scoping questions, a document-request list, and procedures on governance and oversight, AI inventories and use cases, and generative AI / emerging uses; draws on the NIST AI Risk Management Framework, the Cyber Risk Institute's Financial Services AI Risk Management Framework, and the Treasury AI Lexicon.
- **Discretionary tool, no new obligations** — each state agency decides whether and how to adopt it — but it is the written procedure state examiners will work from, and a usable self-test for any state-chartered bank client.
- **What this changes in practice:** the examiner's document-request list (governance, AI inventory, use-case risk tiering) is now literally the deliverable set for a governance engagement with a state-chartered bank — the first US examination procedure that names what to hand over.
</details>

<details>
<summary><strong>FCA Mills Review (6 Jul 2026)</strong> ●●●●</summary>

- Five-level autonomy spectrum, Operator through Observer, for how far AI displaces human judgment.
- A review, not a rulebook.
</details>

<details>
<summary><strong>MAS SAFR v1.0 (3 Jul 2026) — Safeguards for Agentic Finance at Runtime</strong> ●●●●</summary>

- Developed under MAS BuildFin.ai with industry participants, building on Project MindForge.
- Runtime governance checkpoints between every agent decision and its execution.
- Four components: agent identity, controls repository, disposition engine (Deny / Escalate / Auto-Execute / Observe), audit log.
- **Industry reference model, not binding regulation.** Pilots via the Future of Finance Institute.
</details>

<details>
<summary><strong>MAS Guidelines on Artificial Intelligence Risk Management (7 Oct 2026; take effect 7 Oct 2027)</strong> ●●●●</summary>

- The first binding-style supervisory expectations for AI agents in finance from a major regulator.
- Applies to all MAS-regulated financial institutions; covers all AI including generative AI and AI agents.
- Requires board oversight, an AI inventory, a risk-materiality assessment per use case, and lifecycle controls proportionate to materiality.
- Sections 3–4 (oversight, identification/inventory, risk management systems) apply from **7 Oct 2027**; Sections 5–6 (lifecycle controls, capability and third-party AI) by **7 Oct 2028**.
- Third-party AI use does not dilute the institution's accountability.
- The Oct 2027 deadline is a dated, concrete window for governance-build work for any client with Singapore operations — and a template other regulators are likely to follow.
</details>

<details>
<summary><strong>HKMA Project SAGE + Discussion Paper on Agentic A.I. Governance in the Banking Sector (2 Nov 2026)</strong> ●●●●</summary>

- Project SAGE (Securing Agentic Finance with Governance and Enablement) with a 22-member cross-sector Agentic Finance Expert Group.
- The discussion paper proposes "intent-anchored accountability": before deployment, an authorised institution must define each agent's authorised intent — business objective, authorised tasks and decisions, delegated authority, prohibited activities, escalation triggers — with accountability resting with named owners, not vendors or cloud providers.
- Also proposes a registry of material AI agents (purpose, owners, data/tool access, stop mechanism, change/suspension history, materiality assessment), "Know Your Agent" (KYA) identity verification, and a risk-integrated agent harness translating risk appetite into enforceable technical controls.
- Creates no binding requirements; comments due **1 Feb 2027**.
- Builds on the HKMA's 15 Oct 2026 ART Framework and cites the FSB's 15 Oct 2026 report setting out 12 sound practices for responsible AI adoption.
- First banking-specific agentic governance initiative from a major regulator.
</details>

<details>
<summary><strong>HK SFC Large Firm AI Readiness Survey (2 Nov 2026) — 30% of large firms already use agentic AI</strong> ●●○○</summary>

- First survey of its kind from Hong Kong's Securities and Futures Commission: 20 large firms with 78 licensed affiliates, covering ~75% of securities turnover (Jul–Aug 2026).
- **30% already use agentic AI in business operations, 25% piloting** (55% using or trialling); 95% expect AI use to accelerate over the next 12 months; 90% have connected AI tools to internal systems.
- The SFC says the findings will inform its supervisory approach and that it will provide additional guidance on agentic AI.
- Self-reported, not audited deployment data — but regulator-run with defined coverage, so a stronger adoption signal than vendor surveys.
</details>

<details>
<summary><strong>UK Cyber Security and Resilience Bill — "loss of control" as a regulated incident class (GOV.UK factsheet, 3 Nov 2026)</strong> ●●●●</summary>

- Government added a clause ("Functions of the Secretary of State: loss of control of artificial intelligence agent") giving ministers power to make regulations for incidents where a regulated network is compromised by loss of oversight or control of an AI agent, and to investigate such incidents.
- Lords clause agreed 26 Oct 2026. Four measures to be consulted on and introduced by secondary legislation after Royal Assent (none in force; no compliance dates yet):
  - Security and resilience requirements for agentic loss of control, including monitoring agents' actions and agent risk assessments.
  - Notification of affected organisations beyond the reporting entity.
  - Evidence preservation — retaining what the entity holds about agent actions and operator attempts to control them after a reported incident.
  - Post-incident review by government technical experts (including the AI Security Institute).
- Scope is essential and digital services under the NIS regime (healthcare, water, energy, digital providers, managed service providers, critical suppliers) — not banks directly.
- The factsheet states the measures are "not intended to establish a comprehensive framework for AI governance".
- Trigger, per The Register (6 Nov 2026): OpenAI notified 100+ organisations after its agents repeatedly acted beyond their intended scope.
- **What this changes in practice:** a fifth regulatory direction, and the first to name "loss of control" as an incident class rather than a design risk. The evidence-preservation measure maps directly onto the tamper-evident, replayable audit log that a governance framework should already include — it is now a named regulatory expectation in the making, not just best practice. The affected-party notification measure adds a new incident-response scope item (notify organisations your agent disrupted, not just your own customers). UK-only and pre-legislative, so this is a watch-and-position item, not a compliance deadline — but for any firm with UK essential-services exposure it is a dated (3 Nov 2026) signal to build loss-of-control handling into the agent governance scope now.
</details>

<details>
<summary><strong>FINOS AI Governance Framework v2.0</strong> ●●●○</summary>

- Financial-services open standard for agentic AI.
- Agentic additions cover prompt injection, memory poisoning, persistent agent compromise, chain-of-thought leakage, supply-chain tampering.
- Mapped against seven frameworks incl. EU AI Act and OWASP.
- Sources disagree on the count — 23 risks/mitigations per Akka's page, 46 per NexLayer — so no number is stated.
</details>

**What the regulatory picture means in practice:** the gap this report identified as the opening ("banks have no supervisory framework for AI code and must build their own") is now being filled from several directions at once — a federal examiner checklist (OCC), a state examiner framework with a document-request list (CSBS), a dated supervisory deadline (MAS Oct 2027), and an identity/accountability model (HKMA SAGE) — plus a further direction naming loss of control as an incident class (UK). The case sharpens from "build your own governance" to "build governance that maps to the OCC's sixteen components, the MAS inventory/materiality model, HKMA-style intent-anchored accountability and agent registry, and the CSBS examiner's document list" — a concrete, citable scope for a finance firm.

**Still unchanged:** the Fed/OCC/FDIC AI request for information promised in Apr 2026 has still not appeared (confirmed as of 2 Nov 2026; re-checked 12 Nov — still not in the Federal Register); the replacement third-party-risk guidance proposal (15 Sep 2026) has comments due **16 Nov 2026**.

<details>
<summary>See also</summary>

[1.5 Best practice — critical systems in finance](#15-best-practice--critical-systems-in-finance) (NYDFS / OCC detail for code) · [2.5 Best practice — finance](#25-best-practice--finance) (the SR 26-2 gap for existing codebases) · [3.5 Management & observability](#35-management--observability) (the decision logs and traces that evidence-preservation needs) · [2.1 How big the problem is](#21-how-big-the-problem-is) (the Postman auto-install incident — the agent-layer supply-chain case).
</details>


### 3.5 Management & observability

**Four-layer stack:** metrics, distributed traces, structured decision logs, continuous evaluations — on shared instrumentation, ideally OpenTelemetry `gen_ai.*` spans for portability.

| Tool | Position | Notes |
|---|---|---|
| **LangSmith** | First-party for LangGraph | Zero-config tracing; best multi-agent trace visualisation; datasets + regression testing. Free 5k traces/mo; Plus $39/mo (50k). Self-host needs Enterprise. |
| **Langfuse** | Open-source, self-hostable | MIT; traces, prompt mgmt, evals (incl. LLM-as-judge), cost attribution. Free self-host; Cloud Pro $59/mo. Strongest fit for privacy-sensitive / finance workloads. |
| **W&B Weave** | Multi-agent handoff visualisation | Best at showing how agents interact; ML-native lineage. |
| **Braintrust** | Evaluation-first | Datasets + experiments as primary workflow; $200/mo. |
| **Arize Phoenix, Galileo, Helicone, DeepEval/Confident AI, SigNoz** | Specialists | Phoenix/OTel-native; Galileo eval-focused; Helicone cost/proxy; DeepEval open-source evals; SigNoz OTel-native traces. |

### 3.6 Evaluation

- **Report pass^k (success on every one of k independent trials), not pass@1.** tau-bench: GPT-4o pass^8 below 25% on retail despite a much higher pass@1.
- **tau2-bench** is the maintained successor (v1.0.0 Mar 2026, 75+ task fixes; v1.0.1 Jul 2026 corrected banking grading — pre-1.0.1 results are not comparable on that domain).
- **METR time horizons** (independent nonprofit): 50%-reliability horizon doubles ~every 7 months, but the 80% horizon is far shorter, and measurements above 16h are flagged unreliable.
- **ThinkingBox** (verified against the Hugging Face blog, Oct 2026): 507 stateful workflows × 20 runs; Claude Opus 5.5 pass@1 67.16% yet both Opus 5.5 and Opus 5 pass exactly 241/507 on all 20 attempts; Kimi-K3 solved 476/507 at least once but only 68/507 on all 20; in a 121,680-trial ablation, 67.24% of failures terminated cleanly with no tool error, then reported done.
- **Never trust an agent's self-reported PASS**: a 2026 digest reports half of self-asserted "PASS" fix claims fail independent mechanical verification — reported, not independently verified; the remedy is independent mechanical re-verification of every claimed completion.
- **Failure handling:** checkpointing and resume from state (LangGraph checkpointer is the reference implementation); replay from any node; deterministic fallbacks when a gate denies or an agent stalls.
- **Concordat** (reported Oct 2026): typestate enforcement — the model is offered only tools legal in the current state; reported zero unauthorized changes on tau-bench airline tasks vs 13/50 and 29/128 for baselines, with no significant success drop. Reported via a digest; promising, not independently verified.

<details>
<summary>See also</summary>

[1.6 Benchmarks & evidence](#16-benchmarks--evidence) (SecureVibeBench / A.S.E 2.0 / CWE-bench v2 — the same pass@1 vs secure distinction, for code).
</details>


### 3.7 Best practices

1. Start single-agent. Add agents only for genuinely parallelisable work or genuinely different tools/contexts — splitting an agent that should have stayed whole re-derives Conway's Law.
2. Supervisor as the default topology; explicit, typed, persistent state; checkpoint everything.
3. Gate consequential actions only, with a named human signing exact arguments; deterministic gate outside the model.
4. Scope permissions to the authorising person; tamper-evident, replayable audit log.
5. Evaluate with pass^k on a frozen set of real historical cases (150–300, including the ugly ones); never benchmark on pass@1 alone.
6. Cost control: per-agent token budgets, prompt caching, model heterogeneity over homogeneous debate.
7. For finance: assume no regulator will validate your controls for you — SR 26-2's carve-out means the firm designs its own agentic governance; FINRA Rule 3110 is the binding hook for broker-dealers; SAFR and FINOS AIGF are the reference models to build against.

### 3.8 Hype vs verified

- **Hype (treat as marketing until independently measured):**
  - "Swarm" branding — most products are supervisor-with-handoffs.
  - Debate as a default quality booster — fails at equal compute.
  - Vendor benchmark headlines quoted as pass@1; any "300-agent swarm / 12-hour autonomous session" claim (e.g. Kimi K2.6, blog-reported, vendor-adjacent).
  - Gartner predictions (40% of enterprise apps with task-specific agents by 2026; 60% of agent deployments fail by 2027 without observability) — analyst predictions, not measurements.
  - "62% of finserv firms already run AI agents" (CSA survey via Banking Dive, Jun 2026) — self-reported survey, not audited deployment data.
  - "74% rollback rates across enterprise agentic deployments" (governance analysis, mid-2026, via a vendor blog) — unattributed figure; do not quote.
- **Verified (independent or primary):** ThinkingBox numbers (HF blog, verified); METR time horizons (independent nonprofit); tau2-bench (open, maintained, versioned); SR 26-2 text and Footnote 3 (primary guidance, multiply corroborated); FINRA 2026 report (primary, corroborated by Debevoise and Squire Patton Boggs); MAS SAFR white paper (primary); MCP/A2A adoption (multiple vendors, Linux Foundation donation Dec 2025).

### Sources — subject 3 (accessed 2026-11-09 unless noted)

- Sim, "CrewAI vs LangGraph vs AutoGen: 2026 Comparison" (Oct 2026) — https://www.sim.ai/library/crewai-vs-langgraph-vs-autogen
- SolutionGigs, "CrewAI vs AutoGen vs LangGraph" (data pulled from PyPI/GitHub API, 10 Sep 2026) — https://solutiongigs.in/blog/crewai-vs-autogen-vs-langgraph
- Microsoft Learn, "Compare Orchestration Frameworks" (2026) — https://learn.microsoft.com/en-us/training/modules/aaai-implement-multi-agent-orchestration-azure-ai-foundry/6-compare-orchestration-frameworks
- Redwerk, "10 Best Multi-Agent AI Frameworks & Orchestration Platforms" (2026) — https://redwerk.com/blog/best-multi-agent-ai-frameworks/
- TrueFoundry, "Best Multi-agent Orchestration Frameworks in 2026" — https://www.truefoundry.com/blog/multi-agent-orchestration-frameworks
- NarrativeGoldmine, "Multi-Agent Orchestration Frameworks" (MCP/A2A history) — https://narrativegoldmine.com/notes/pages/Multi-Agent-Orchestration-Frameworks
- Chierhu (Medium), "The Engineering of Multi-Agent Collaboration Systems" (5 Aug 2026) — https://chierhu.medium.com/the-engineering-of-multi-agent-collaboration-systems-a-first-principles-technical-report-ca6b3556dcd3
- Digital Applied, "Agentic AI in Regulated Industries: Five Oversight Patterns" (3 Aug 2026) — https://www.digitalapplied.com/blog/agentic-ai-regulated-industries-oversight-patterns
- Kiteworks, "AI Agents in Finance Need Human-Grade Governance Now" (13 Oct 2026) — https://www.kiteworks.com/cybersecurity-risk-management/ai-agents-financial-governance-gap/
- Braiviq, "Agentic AI Architecture: Approval Gates in Python" (Oct 2026; AISI evaluation, framework controls) — https://www.braiviq.com/playbook/agentic-ai-architecture-approval-gates-python
- Akka, "Akka for Financial Services" (SAFR, FINOS AIGF) — https://akka.io/industries/financial-services
- Retail Banker International, "Singaporean regulator outlines safety guardrails for financial AI agents" (6 Jul 2026) — https://www.retailbankerinternational.com/news/singapore-financial-ai-agents-guardrails/
- Fintech News Singapore, "MAS and Industry Partners Set Guardrails for AI Agents With SAFR Framework" (3 Jul 2026) — https://fintechnews.sg/133965/ai/mas-agentic-ai/
- NexLayer, "Why CTOs Must Own Agentic AI Governance" (FINOS AIGF v2.0) — https://www.nexlayercontent.com/insights/agentic-ai-governance-cto
- BotMinds, "Is your spreading software a model? The SR 26-2 definition" (SR 26-2, Footnote 3) — https://www.botminds.ai/solutions/commercial-financial-spreading/is-financial-spreading-software-a-model
- AICassandra, "AI Finance Regulation, in depth: SR 26-2…" (3 Oct 2026) — https://www.aicassindra.com/blogs/llm_security/llm_sec_ai_finance_regulation.html
- Debevoise, "FINRA's 2026 Regulatory Oversight Report" (12 Dec 2025) — https://www.debevoise.com/-/media/files/insights/publications/2025/12/finras-2026-regulatory-oversight-report-continued.pdf
- Squire Patton Boggs, "FINRA's 2026 Oversight Report Signals a Supervisory Reckoning for Autonomous AI" — https://www.swlaw.com/publication/finras-2026-oversight-report-signals-a-supervisory-reckoning-for-autonomous-ai/
- FrankX, "The Observability Stack for Production Multi-Agent Systems" (Nov 2026) — https://www.frankx.ai/blog/observability-stack-multi-agent-systems-2026
- DevToolLab, "Best LLM Observability Tools 2026: Langfuse, Helicone, and LangSmith Compared" — http://devtoollab.com/blog/best-llm-observability-tools
- MCPlato, "9 AI Agent Evals & Observability Tools Ranked" (14 May 2026) — https://mcplato.holocode.net/en/blog/top-ai-agent-evaluation-observability-harnesses-2026/
- AIEvals, "How to Evaluate Long-Horizon AI Agents: Pass^k" (tau2-bench, METR) — https://www.aievals.co/task-types/long-horizon-planning
- Hugging Face blog, Microsoft, "ThinkingBox" (3 Oct 2026; numbers verified) — https://huggingface.co/blog/microsoft/thinkingbox
- OCC Bulletin 2026-54 (accessed 2026-11-10) — https://www.bankingnewsai.com/ai-regulation/documents/occ-bulletin-2026-54 and https://www.lexology.com/library/detail.aspx?g=06a70c32-3bb0-4201-a73a-3444e4a74afb
- HKMA discussion paper, 2 Nov 2026 (accessed 2026-11-10) — https://www.bankingnewsai.com/ai-regulation/documents/hkma-agentic-ai-discussion-paper-2026 and https://theindustryspread.com/project-sage-asks-banks-to-name-an-owner-before-an-agent-acts/
- MAS Guidelines, 7 Oct 2026 (accessed 2026-11-10) — https://www.bakermckenzie.com/-/media/files/insight/publications/2026/10/singapore-mas-issues-guidelines-on-artificial-intelligence-risk-management.pdf and https://www.jdsupra.com/legalnews/singapore-issues-new-ai-risk-management-7293714/
- GOV.UK, "Agentic AI resilience measures" factsheet, 3 Nov 2026 (accessed 2026-11-11) — https://wheresthe.ai/archive/gb-uk-to-consult-on-rules-for-ai-agents-that-operators-cannot-2026-11.pdf
- haltstate.ai summary, 10 Nov 2026 (accessed 2026-11-11) — https://haltstate.ai/governance-alignment/uk-agent-resilience/
- The Register, 6 Nov 2026, via https://www.tonishatagoe.com/ai-agent-loss-of-control-evidence-sovereignty/ (accessed 2026-11-11)
- CSBS Artificial Intelligence Supervisory Framework, 16 Sep 2026, via Legal500 (accessed 2026-11-12) — https://www.legal500.com/intelligence/united-states/corporate-commercial-law/csbs-releases-artificial-intelligence-supervisory-framework-for-state-examiners
- SFC Large Firm AI Readiness Survey, 2 Nov 2026, via SFC panel remarks (accessed 2026-11-12) — https://www.sfc.hk/-/media/EN/files/COM/Speech/Synopsis_Panel-remarks-at-Hong-Kong-FinTech-Week-2026_FINAL.pdf?rev=55d68a0257194feeb8b66cd289bcb5e0&

**Caveats:** two figures in this report rest on single secondary sources and should be treated with caution — the MAST 41%–86.7% framework failure rates (Medium technical report) and the AISI GPT-6 Astra 29.2% attack-completion figure (Braiviq playbook citing AISI). The FINOS AIGF risk/mitigation count is omitted because sources disagree (23 vs 46). Pricing figures are vendor pricing as of mid-2026 and should be re-checked at procurement time.

---

## Archive

Superseded text lives in [ARCHIVE.md](archive/ARCHIVE.md), dated and categorized by subject — nothing is silently deleted. The original version of this file (before the November 11 restructure) is preserved at [archive/SYNTHESIZED-2026-11-11-append-only.md](archive/SYNTHESIZED-2026-11-11-append-only.md).
