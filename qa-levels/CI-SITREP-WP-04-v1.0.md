# The Structural Anatomy of Created Intelligence Adoption

<p><small>by Yorgo P. Bougás · Confluence&lt;1&gt;</small></p>

*Why Infrastructure Velocity Diverges from Enterprise Profit & Loss (P&L) Capture*

**Document ID:** CI-SITREP-WP-04
**Series:** CI SITREP Research Series
**Version:** 1.0.0 (Technical Brief & White Paper, WP-04 v1.0)
**Date:** 26 November 2026
**Author:** Yorgo P. Bougás · Confluence<1>
**Status:** Published on CI SITREP (R&D), November 2026.
**Frameworks:** Carlota Perez (2002) — Installation vs. Deployment Phases; Robert Solow (1987) — Productivity Paradox; Erik Brynjolfsson (2021) — Productivity J-Curve; Everett Rogers & Geoffrey Moore — Diffusion & Institutional Friction; Simon Wardley (2015) & Chris Dixon — Value Chain Evolution & Infra-App Cycles; NASA Technology Readiness Level (TRL) & U.S. Department of Energy Adoption Readiness Level (ARL) — Technology vs. Adoption Readiness; Daron Acemoglu (2024/2025) — The Ceiling Case (≤0.66% Total Factor Productivity over 10 years, upper bound).

### Executive Thesis

Global capital markets are currently conflating **infrastructure buildout** with **enterprise value capture**. While hyperscaler capital expenditure reached $376.1 billion in 2025, with 2026 guidance of $720–745 billion (WP-03 §II.5.1), empirical enterprise telemetry demonstrates that operational speed has detached from bottom-line margin expansion. According to the CI SITREP evidence base, **86% of United States financial firms formally use artificial intelligence, yet only 38% formally test what it produces** (ACA/NSCP 2026 AI Benchmarking Survey, November 2026, 261 firms) ●●○○, and **only 9% of organizations have redesigned workflows to safely accommodate agents** (Optro, *Authority without oversight*, October 2026, 400+ governance, risk, and compliance leaders) ●●○○.

The **CI SITREP** framework resolves this contradiction by replacing linear hype narratives with a two-part diagnostic system:
1. **The Parametric Adoption Curve:** Models the macro divergence between silicon/capital velocity and human/institutional absorption.
2. **The 6 × 5 Readiness & P&L Heatmap (the P&L Heatmap; technically, the Pure-Chromatic Telemetry Gauge):** Deconstructs Created Intelligence (CI) into 30 discrete architectural and economic states, revealing precisely where margin is currently trapped (*The Governance Tax* — the verification overhead, β, that must be paid before returns land) and where asymmetric competitive advantage lies.

In plain terms: the curve shows why the money is not landing yet; the 30-cell map shows where the margin is trapped.

---

### Part I: Theoretical Synthesis & Empirical Premises

Every General Purpose Technology (GPT)—from steam and railroads to electrification and networked computing—passes through structural phases of capital deployment and institutional friction. However, Created Intelligence differs from 19th- and 20th-century revolutions in one decisive respect: **its distribution rails already exist, while its compute rails are being built now at railroad scale — paired with unprecedented asymmetric verification costs** (WP-03, Correction 2: distribution rails exist, but compute rails are being built now — $376.1 billion of hyperscaler capital expenditure in 2025, a data-centre pipeline over $1 trillion).

This paper uses the site's stage labels — **Buildout** (α governs how much rail must be built), **Governance Tax** (β governs the trough's depth), **The Shakeout** (γ governs how concentrated the survivors are; δ governs how long the recomposition takes), and **Deployment** (projected — the dashed right half). Perez's own terms for the first and last of these are Installation and Deployment; the framework is hers, the labels are the site's.

The CI SITREP model synthesizes six validated empirical frameworks into a unified diagnostic calculus, bounded by a seventh — Acemoglu's ceiling case: at most ~0.66% Total Factor Productivity over 10 years, explicitly an upper bound (WP-03) — the fork against which the J-Curve's recovery must be read:

| Axiom ID | Framework & Thinker | Core Premise | CI SITREP Calibration Parameter |
| :--- | :--- | :--- | :--- |
| **AX-01** | **Carlota Perez (2002)** — *Buildout vs. Deployment* (Perez: Installation vs. Deployment) | Technological revolutions bifurcate into a *Buildout* (financial capital building ahead of unit economics) and a *Deployment* (production capital harvesting returns after the Shakeout). | **Rail Readiness (α):** Distribution rides existing cloud/fiber rails; compute rails are being built now. Technical installation compresses to ~6–10 years for the technical half only (historical proxies: railways ~10–14 years, dynamo ~15–30 years, automobiles ~40 years — WP-03). |
| **AX-02** | **Robert Solow (1987)** — *The Productivity Paradox* | Capital expenditure in new computing machinery appears everywhere except in aggregate productivity and corporate operating margins until workflows are redesigned. | **Macro Divergence Gap:** Total Factor Productivity +0.8% in 2025, down from +1.5% (WP-03, E2), despite $376.1 billion in 2025 hyperscaler capital expenditure. |
| **AX-03** | **Erik Brynjolfsson (2021)** — *The Productivity J-Curve* | Measured net productivity initially **dips negative** as firms divert capital and labor into intangible investments (data cleanup, security remediation, compliance) before harvesting returns. | **Verification Overhead (β — the Governance Tax):** ~38% of AI-generated code introduces a known security flaw (Veracode, Fall 2026 GenAI Code Security Update) ●●●○; monthly security findings rose ~10× (~1,000 → 10,000+) in enterprise telemetry (Apiiro via Cloud Security Alliance, April 2026) [VENDOR DATA] ●●○○ — creating net margin drag. |
| **AX-04** | **Everett Rogers & Geoffrey Moore** — *Institutional Friction* | Technical diffusion moves at network distribution speed; organizational adoption moves at the speed of legal liability, auditability, and human decision rights. | **Institutional Lag (δ):** 73% of systemically important banks permit agents in production for select use cases, yet only 8% have comprehensive agent monitoring (BCG, 13 November 2026) ●●○○; 38% of organizations authorise agents to approve or reject transactions (Optro, October 2026) ●●○○; 23% of firms with agents in production have never tested the termination capability they believe they have (Writer / Workplace Intelligence, 2026) ●●○○. |
| **AX-05** | **Simon Wardley & Chris Dixon** — *Value Chain & Infra-App Cycles* | Capabilities evolve from *Genesis → Custom → Product → Commodity*. Infra Wave 1 triggers reliability failures that require Infra Wave 2 (deterministic control planes). | **Vendor Concentration (γ):** Hyperscaler oligopoly commoditizes models while shifting value upward to semantic context and verification. |
| **AX-06** | **NASA Technology Readiness Level (TRL) & U.S. Department of Energy Adoption Readiness Level (ARL)** — *Technology vs. Adoption Readiness* | Technical viability in controlled tests is distinct from commercial and operational readiness under P&L and regulatory accountability. | **5 Sequential Payoff Gates:** Separates technical feasibility (Gate 1) from net P&L capture (Gate 5). |

---

### Part II: Architecture of the 6 × 5 Readiness & P&L Matrix

To prevent executives from making monolithic capital allocation errors ("buying AI" rather than funding specific readiness gates), the CI SITREP matrix maps **6 Architectural Stack Layers (X-Axis)** across **5 Proven Adoption & Payoff Gates (Y-Axis)**.

#### X-Axis: Value Chain Stack Layers (Bottom-Up Dependency)
1. **L1 — Compute & Cloud Infrastructure:** Silicon, data center power, and inference capacity.
2. **L2 — Foundation Models & Reasoning:** General and specialized frontier models.
3. **L3 — Data Plumbing & Semantic Context:** Enterprise extract-transform-load (ETL), unified schemas, lineage, and retrieval context.
4. **L4 — Agentic Execution & Orchestration:** Autonomous multi-step task execution, tool calling, and state management.
5. **L5 — Governance, Verification & Guardrails:** Automated code/output scanning, deterministic policy enforcement, and audit trails.
6. **L6 — Workflow Re-Architecture & P&L Capture:** Elimination of legacy human-in-the-loop friction and direct unit-margin expansion.

#### Y-Axis: Sequential Payoff Gates (Bottom-Up Progression)
* **G1 — Technical Feasibility & Cost:** Reliable functional execution at predictable unit economics.
* **G2 — Infrastructural Complementarity:** Availability of clean internal data, application programming interfaces (APIs), and plumbing required for integration.
* **G3 — Verification & Risk Containment:** Deterministic guardrails, security validation, and bounded liability ("License to Operate").
* **G4 — Organizational Absorption:** Re-engineered job roles, approval workflows, and P&L accountability.
* **G5 — Net P&L & Margin Expansion:** Positive operating cash flow *after* deducting all license, compute, scanning, and remediation costs.

#### Z-Axis: Chromatic Diagnostic States
* **EMERALD (`Mature / Deploy Now`):** Standardized utility with proven return on investment (ROI). *Mandate: Commoditize spend; deploy for competitive parity.*
* **AMBER (`Inflection Cusp`):** Technical feasibility proven; institutional and governance plumbing actively locking in. *Mandate: Invest aggressively now to establish asymmetric advantage.*
* **CRIMSON (`Governance Tax Trough` — the stage where the Governance Tax, β, is being paid):** High deployment velocity colliding with missing verification or data foundations, creating negative net margin and operational risk. *Mandate: Ring-fence spend; cap production scaling until guardrails close the gap.*
* **SLATE (`Genesis / Pre-Payoff`):** Blocked by upstream bottlenecks or structurally unproven. *Mandate: Keep strictly inside ring-fenced R&D.*

#### The Q4 2026 Matrix at a Glance

| Gate ↓ / Layer → | L1 Compute | L2 Models | L3 Data Context | L4 Agentic Exec | L5 Governance | L6 Workflow P&L |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **G5 — Net P&L** | EMERALD | AMBER | SLATE | CRIMSON | AMBER | CRIMSON |
| **G4 — Absorption** | EMERALD | EMERALD | AMBER | CRIMSON | CRIMSON | SLATE |
| **G3 — Verification** | EMERALD | AMBER | AMBER | CRIMSON | AMBER | SLATE |
| **G2 — Complementarity** | EMERALD | EMERALD | CRIMSON | AMBER | AMBER | SLATE |
| **G1 — Feasibility** | EMERALD | EMERALD | EMERALD | AMBER | AMBER | SLATE |

Tally: 9 EMERALD / 10 AMBER / 6 CRIMSON / 5 SLATE.

**A note on what EMERALD means here.** These 30 cells are architectural states — 6 stack layers × 5 payoff gates — assigned by judgment against the evidence base, not 30 measured parameters. (WP-03's separate 30-parameter tally counts measured evidence parameters; the two sets are different instruments.) An EMERALD cell at Gate 1 or Gate 2 means the technology works and the plumbing exists — it does not mean deployment-level institutional conditions are in place. The 9 EMERALD cells sit mostly at the technical gates (G1/G2), plus hyperscaler infrastructure rents at L1×G5; the gates that govern enterprise P&L capture (G4/G5) remain CRIMSON or SLATE across the agentic and workflow layers. Read the matrix gate by gate, not by its EMERALD count.

---

### Part III: Q4 2026 Baseline Telemetry Schema (Machine- & Agent-Readable)

```yaml
ci_sitrep_matrix:
  snapshot_period: "2026-Q4"
  dimensions:
    x_layers: ["L1_Compute", "L2_Models", "L3_DataContext", "L4_AgenticExec", "L5_Governance", "L6_WorkflowPnL"]
    y_gates: ["G1_Feasibility", "G2_Complementarity", "G3_Verification", "G4_Absorption", "G5_NetPnL"]
  cells:
    # Gate 5: Net P&L & Margin Expansion
    L1_G5: { state: "EMERALD", note: "Hyperscalers capturing infrastructure rents" }
    L2_G5: { state: "AMBER",   note: "Severe price compression; inference commoditizing" }
    L3_G5: { state: "SLATE",   note: "Still treated as a capex/opex cost center" }
    L4_G5: { state: "CRIMSON", note: "Pilot purgatory; no credible net return-on-investment figure published — profitability gained is a no-data gap in the evidence base" }
    L5_G5: { state: "AMBER",   note: "High-margin niche for verification & audit vendors" }
    L6_G5: { state: "CRIMSON", note: "Solow productivity lag; un-redesigned legacy workflows" }
    # Gate 4: Organizational Absorption
    L1_G4: { state: "EMERALD", note: "Cloud procurement standardized" }
    L2_G4: { state: "EMERALD", note: "API consumption culturally accepted" }
    L3_G4: { state: "AMBER",   note: "Cross-silo data ownership slowly consolidating" }
    L4_G4: { state: "CRIMSON", note: "73% of systemically important banks permit agents in production, only 8% monitor them comprehensively (BCG, Nov 2026); 38% of organizations authorise agents to approve or reject transactions (Optro, Oct 2026)" }
    L5_G4: { state: "CRIMSON", note: "Security and compliance review backlogs exploding" }
    L6_G4: { state: "SLATE",   note: "Only 9% of organizations have redesigned workflows to safely accommodate agents (Optro, Oct 2026)" }
    # Gate 3: Verification & Risk Containment
    L1_G3: { state: "EMERALD", note: "Service Organization Control 2 (SOC 2) / International Organization for Standardization (ISO) cloud security mature" }
    L2_G3: { state: "AMBER",   note: "Model-level guardrails improving but non-deterministic" }
    L3_G3: { state: "AMBER",   note: "Lineage and access controls maturing" }
    L4_G3: { state: "CRIMSON", note: "Ungoverned autonomous agents creating outage/security risk" }
    L5_G3: { state: "AMBER",   note: "Inflection cusp: automated code/output verification scaling" }
    L6_G3: { state: "SLATE",   note: "End-to-end P&L auditability unproven" }
    # Gate 2: Infrastructural Complementarity
    L1_G2: { state: "EMERALD", note: "Global fiber and cloud regions operational" }
    L2_G2: { state: "EMERALD", note: "Standardized representational state transfer (REST) / Model Context Protocol (MCP) model interfaces" }
    L3_G2: { state: "CRIMSON", note: "Fragmented silos; enterprise data remains split across disconnected systems with no unified schema or lineage" }
    L4_G2: { state: "AMBER",   note: "Tool-use protocols emerging rapidly" }
    L5_G2: { state: "AMBER",   note: "Continuous integration / continuous delivery scanning hooks actively integrating" }
    L6_G2: { state: "SLATE",   note: "Enterprise resource planning (ERP) / core system hooks remain rigid" }
    # Gate 1: Technical Feasibility & Cost
    L1_G1: { state: "EMERALD", note: "Proven at hyperscale" }
    L2_G1: { state: "EMERALD", note: "Frontier reasoning proven; token cost falling" }
    L3_G1: { state: "EMERALD", note: "Vector, graph, and lakehouse engines mature" }
    L4_G1: { state: "AMBER",   note: "Multi-step reliability improving rapidly" }
    L5_G1: { state: "AMBER",   note: "Deterministic policy & formal verification engines emerging" }
    L6_G1: { state: "SLATE",   note: "Autonomous end-to-end P&L optimization experimental" }
```

---

### Part IV: Reading the P&L Heatmap's Chromatic Field

For continuous executive monitoring, the 30-cell matrix compresses into the P&L Heatmap's chromatic field — a borderless, label-free bilinearly interpolated visual field governed directly by the underlying cell states. The chromatic field is a compression of the labeled matrix, never a substitute for it: every field reading is paired with the 6×5 grid in Part II, whose cells carry text states — the color encoding is color-blind safe by pairing.

**A worked reading — the Q4 2026 field.** Read the field from the bottom-left (L1×G1: compute, technical feasibility) to the top-right (L6×G5: workflow re-architecture, net P&L):

* **Bottom-Left Emerald Anchor:** The compute and model layers are mature at the technical gates — the technology works, and the hyperscalers are already capturing infrastructure rents (L1×G5 EMERALD). The foundation is not the problem. *What to do:* commoditize spend here; buy it, don't build it.
* **Central Crimson Fracture:** The middle of the field — agentic execution (L4) at the verification, absorption, and P&L gates, and data context (L3) at the complementarity gate — is where margin is trapped. Agents are being deployed faster than they can be verified or absorbed: 73% of systemically important banks permit agents in production while only 8% monitor them comprehensively (BCG, November 2026) ●●○○. This is the Governance Tax being paid. *What to do:* ring-fence spend on unverified autonomy; fund the verification layer (L5) and the data plumbing (L3) before scaling L4.
* **Diagonal Amber Migration:** The amber diagonal running from L2×G3 through L5×G3 to L5×G5 marks verification and data-context layers maturing — model guardrails, lineage controls, and automated code/output verification are at the inflection cusp. This diagonal is the leading indicator: as it turns emerald, the field moves from the Buildout through the Shakeout toward Deployment (projected). *What to do:* invest aggressively along the diagonal now — this is where asymmetric advantage is established.
* **Top-Right Slate:** Workflow re-architecture (L6) has not begun at any gate above feasibility — only 9% of organizations have redesigned workflows to safely accommodate agents (Optro, October 2026) ●●○○. Until L6 moves, enterprise P&L capture stays theoretical. *What to do:* keep L6 inside ring-fenced R&D until the amber diagonal reaches it.
* **Full-Field Emerald Convergence:** Indicates institutional absorption is complete and broad P&L margin expansion is underway. The Q4 2026 field is nowhere near it — and no honest reading of the evidence says otherwise.

---

### References

- Veracode. "Fall 2026 GenAI Code Security Update." Veracode, Fall 2026. [https://www.veracode.com/blog/fall-2026-genai-code-security/](https://www.veracode.com/blog/fall-2026-genai-code-security/) — ~38% of AI-generated code introduces a known security flaw (series: 45% Spring 2026 → 44% July 2026 → 38% Fall 2026) ●●●○
- Apiiro / Cloud Security Alliance. "CSA Research Note: AI-Generated Code Security (Vibe Coding)." Cloud Security Alliance, April 2026. [https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-security-vibe-coding-202/](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-security-vibe-coding-202/) — monthly security findings rose ~10× (~1,000 → 10,000+) [VENDOR DATA] ●●○○
- ACA Group / National Society of Compliance Professionals (NSCP). "2026 AI Benchmarking Survey." Business Wire, 12 November 2026 (261 firms). [https://www.businesswire.com/news/home/20261112134673/en/](https://www.businesswire.com/news/home/20261112134673/en/) — 86% of US financial firms formally use AI; 38% formally test outputs ●●○○
- Optro. "Authority without oversight." Optro, October 2026 (400+ governance, risk, and compliance leaders). [https://optro.ai/blog/one-in-three-organizations-say-they-have-acted-on-wrong-decisions-made-by-ai-agents-optro-research-finds](https://optro.ai/blog/one-in-three-organizations-say-they-have-acted-on-wrong-decisions-made-by-ai-agents-optro-research-finds) — 38% authorise agents to approve or reject transactions; only 9% have redesigned workflows ●●○○
- Boston Consulting Group (BCG). "AI Safety and Governance in Banking 2026." PR Newswire, 13 November 2026 (26 global and domestic systemically important banks). [https://www.prnewswire.com/news-releases/operationalizing-ai-governance-gives-banks-an-advantage-in-scaling-ai-302938342.html](https://www.prnewswire.com/news-releases/operationalizing-ai-governance-gives-banks-an-advantage-in-scaling-ai-302938342.html) — 73% permit agents in production for select use cases; 8% have comprehensive agent monitoring ●●○○
- Writer / Workplace Intelligence. "Enterprise AI Adoption Survey." Writer, 2026 (2,400 global employees and C-suite leaders). [https://writer.com/blog/enterprise-ai-adoption-survey-results-press-release/](https://writer.com/blog/enterprise-ai-adoption-survey-results-press-release/) — 23% of firms with agents in production have never tested the termination capability they believe they have ●●○○
- Bougás, Yorgo P. [*Diffusion Gauge — A General Purpose Technology Tracker*](tracker-whitepaper.html) (CI-SITREP-WP-03). CI SITREP Research Series, 22 November 2026 — hyperscaler capital expenditure $376.1 billion in 2025, 2026 guidance $720–745 billion (§II.5.1); Total Factor Productivity +0.8% in 2025, down from +1.5% (E2); Acemoglu ceiling ≤0.66% Total Factor Productivity over 10 years (upper bound); Correction 2 (distribution rails exist, compute rails being built now).

---

### Versioning Protocol
* `v1.0.0` (2026-11-26): Canonical baseline establishing the 6-framework axiomatic synthesis (`AX-01`–`AX-06`), the 6 × 5 matrix schema, and the P&L Heatmap specification.
* Subsequent revisions should increment minor versions (`v1.1.0`) for quarterly cell-state recalibrations and major versions (`v2.0.0`) for structural axis or parameter additions.
