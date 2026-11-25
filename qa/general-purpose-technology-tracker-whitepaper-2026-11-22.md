# The Surge Monitor — A General Purpose Technology Tracker by Yorgo P. Bougás, Confluence<1>

**Status:** v3 WHITE PAPER for Yorgo's review — 22 November 2026. Draft only. Not published, not on the site, not a finding of the report.
**Predecessor:** v2, *The Surge Monitor — A General Purpose Technology Tracker* (general-purpose-technology-tracker-2026-11-22.md) — the model document this whitepaper is drawn from. The v1 clock draft (solow-perez-clock-2026-11-22.md) is the research predecessor.
**Attribution rule (Yorgo, 22 November 2026):** the tracker is his personal work, not Confluence<1> intellectual property — it becomes the firm's only when it is useful and verified. Every byline carries his name, not the firm's. **Attribution update (Yorgo, 25 November 2026):** Confluence<1> is the affiliation on the byline — "Yorgo P. Bougás, Confluence<1>" — and nothing more. The tracker remains Yorgo P. Bougás's personal work, not Confluence<1> intellectual property; it becomes the firm's only when it is useful and verified, by his decision.
**Report base:** CI SITREP (created intelligence situation report), 122 articles (18 Established / 41 Corroborated / 57 Reported / 6 Claimed) as of 22 Nov 2026; dashboard as-of 20 Nov 2026. Report figures below carry the report's own confidence ratings.
**Acronym rule:** every acronym in this document is expanded in full on first use, per Yorgo's standing rule (22 November 2026). No unexplained acronym survives.

**How to read this whitepaper.** Part I states the thesis — the model's core claims, numbered, with no background, evidence, or justification. Part II substantiates every claim, with the evidence, the caveats, and the sources. The mapping table at the start of Part II shows where each thesis point is substantiated.

---

## Table of Contents

- [Part I: The Thesis in Brief](#part-i-the-thesis-in-brief)
- [Part II: The Expanded Version](#part-ii-the-expanded-version)
  - [Thesis-to-substantiation mapping](#thesis-to-substantiation-mapping)
  - [II.1 The Name](#ii1-the-name)
  - [II.2 The Bedrock: Solow and Perez](#ii2-the-bedrock-solow-and-perez)
    - [II.2.1 Perez: Technological Revolutions and Great Surges](#ii21-perez-technological-revolutions-and-great-surges)
    - [II.2.2 Perez: Criticisms and Limits](#ii22-perez-criticisms-and-limits)
    - [II.2.3 Solow: Growth Accounting, the Residual, and the Paradox](#ii23-solow-growth-accounting-the-residual-and-the-paradox)
    - [II.2.4 Solow: Criticisms and Limits](#ii24-solow-criticisms-and-limits)
    - [II.2.5 How Solow and Perez Combine into One Instrument](#ii25-how-solow-and-perez-combine-into-one-instrument)
  - [II.3 The Blind Spot: Why Solow and Perez Alone Are Insufficient](#ii3-the-blind-spot-why-solow-and-perez-alone-are-insufficient)
  - [II.4 The Four Complementary Frameworks](#ii4-the-four-complementary-frameworks)
    - [II.4.1 The Productivity J-Curve](#ii41-the-productivity-j-curve)
    - [II.4.2 Wardley Mapping](#ii42-wardley-mapping)
    - [II.4.3 The Infrastructure-Application Cycle](#ii43-the-infrastructure-application-cycle)
    - [II.4.4 Diffusion and Institutional Friction](#ii44-diffusion-and-institutional-friction)
  - [II.5 The Four Knobs, Operationalized](#ii5-the-four-knobs-operationalized)
    - [II.5.1 Alpha: Physical-to-Digital Rails Ratio](#ii51-alpha-physical-to-digital-rails-ratio)
    - [II.5.2 Beta: Verification-to-Generation Cost Ratio](#ii52-beta-verification-to-generation-cost-ratio)
    - [II.5.3 Gamma: Vendor Concentration and Hyperscaler Lock-In](#ii53-gamma-vendor-concentration-and-hyperscaler-lock-in)
    - [II.5.4 Delta: Institutional Absorption Half-Life](#ii54-delta-institutional-absorption-half-life)
  - [II.6 The Velocity Calibration: Two Speeds, One Cycle](#ii6-the-velocity-calibration-two-speeds-one-cycle)
    - [II.6.1 The Two Velocities](#ii61-the-two-velocities)
    - [II.6.2 The Compressed-Cycle Claim, Assessed](#ii62-the-compressed-cycle-claim-assessed)
  - [II.7 The Parameters: 30, with Heat Status](#ii7-the-parameters-30-with-heat-status)
    - [A. Finance and investment](#a-finance-and-investment--the-frenzy-markers)
    - [B. Diffusion](#b-diffusion--how-far-the-paradigm-has-spread)
    - [C. Institutional mismatch](#c-institutional-mismatch--the-adoptiongovernance-gap-the-reports-strongest-evidence)
    - [D. Regulatory recomposition](#d-regulatory-recomposition--the-turning-point-markers)
    - [E. Productivity and returns](#e-productivity-and-returns--the-solow-measurement)
    - [F. Inequality and structure](#f-inequality-and-structure)
    - [Gaps — what the tracker cannot measure (yet)](#gaps--what-the-tracker-cannot-measure-yet)
  - [II.8 Assessment: The Verdict](#ii8-assessment-the-verdict)
    - [II.8.1 The Verdict Stands](#ii81-the-verdict-stands)
    - [II.8.2 What the New Apparatus Adds](#ii82-what-the-new-apparatus-adds)
    - [II.8.3 What Would Change the Verdict](#ii83-what-would-change-the-verdict)
  - [II.9 Uncertainty: What Could Be Wrong](#ii9-uncertainty-what-could-be-wrong)
  - [II.10 Backtesting: Validating the Model on Previous Revolutions](#ii10-backtesting-validating-the-model-on-previous-revolutions)
    - [II.10.1 The Principle](#ii101-the-principle)
    - [II.10.2 The Cases](#ii102-the-cases)
    - [II.10.3 Steam and Railways](#ii103-steam-and-railways)
    - [II.10.4 The Dynamo: The Worked Case](#ii104-the-dynamo-the-worked-case)
    - [II.10.5 Oil, Automobiles, Mass Production](#ii105-oil-automobiles-mass-production)
    - [II.10.6 Information and Communications Technology and the Sub-Cases](#ii106-information-and-communications-technology-and-the-sub-cases)
    - [II.10.7 What Is Reconstructable and What Is Not](#ii107-what-is-reconstructable-and-what-is-not)
    - [II.10.8 The Validation Standard](#ii108-the-validation-standard)
    - [II.10.9 What the Backtest Changes](#ii109-what-the-backtest-changes)
  - [II.11 The Instrument: Heatmap-First](#ii11-the-instrument-heatmap-first)
    - [II.11.1 The Primary Heatmap: 30 Numbered Squares](#ii111-the-primary-heatmap-30-numbered-squares)
    - [II.11.2 The Second Panel: Wardley Stages](#ii112-the-second-panel-wardley-stages)
    - [II.11.3 The Second View: The Parametric Adoption and Margin Curve](#ii113-the-second-view-the-parametric-adoption-and-margin-curve)
    - [II.11.4 The Summary Strip: The Dial, Demoted](#ii114-the-summary-strip-the-dial-demoted)
    - [II.11.5 The Apparatus That Keeps the Instrument Honest](#ii115-the-apparatus-that-keeps-the-instrument-honest)
  - [II.12 Open Questions](#ii12-open-questions)
    - [Carried from v1 (updated)](#carried-from-v1-updated)
    - [New in v2](#new-in-v2)
    - [Restored from v1](#restored-from-v1)
  - [II.13 Sources](#ii13-sources)
    - [Frameworks and theory](#frameworks-and-theory)
    - [Productivity and macro data](#productivity-and-macro-data)
    - [Adoption and capability](#adoption-and-capability)
    - [The report's evidence base](#the-reports-evidence-base-for-group-c-and-group-d-parameters)
    - [Historical backtesting](#historical-backtesting-ii10)
    - [To check later (not used in this round)](#to-check-later-not-used-in-this-round)
  - [II.14 Conflicts and Corrections Log: The Prior Research vs the Draft](#ii14-conflicts-and-corrections-log-the-prior-research-vs-the-draft)

---

## Part I: The Thesis in Brief

The model's core claims, numbered. No background, no evidence, no justification — just the claims. Each one is substantiated in Part II; the mapping table at the start of Part II shows where.

**T1.** Artificial intelligence (AI) is not a sixth technological revolution; it is a third leap inside the Information and Communications Technology (ICT) revolution — so the cycle is read on two hands, the outer hand for the great surge and the inner hand for the artificial-intelligence sub-cycle.

**T2.** The cycle moves at two speeds: technical diffusion is compressed by an order of magnitude against physical-era baselines, while institutional absorption is not compressed at all.

**T3.** The full cycle to deployment is set by the slower half and runs 10–20+ years; the compressed 6–10 year cycle is defensible only for the technical half.

**T4.** The bottleneck of this revolution is institutional absorption — governance, liability, and trust — not deployment.

**T5.** The productivity payoff has not arrived: the economy is in the dip of the productivity J-curve, with capital and capability racing ahead while enterprise profit-and-loss capture is underwater.

**T6.** The adoption-governance mismatch is the largest ever measured: deployment is at product scale while the governance components are still custom-built or in genesis.

**T7.** The model is measurable: four adjustable parameters — the physical-to-digital rails ratio, the verification-to-generation cost ratio, vendor concentration and lock-in, and the institutional absorption half-life — are the model's quantitative form.

**T8.** The heatmap's verdict is 23 parameters lagging, 5 getting there, 0 in place, 2 unclear: nothing is in place yet.

**T9.** The inner hand stands at late frenzy, turning point beginning; the outer hand is in an extended turning point; and no deployment claim is permitted while the productivity residual is flat or falling and the institutional framework is unsettled.

**T10.** The model earns authority on the present only by describing the past: it must reconstruct previous technological revolutions before its reading of this one is worth anything.

**T11.** The instrument is heatmap-first — thirty numbered squares with a legend — with the parametric curve as the second view and the clock demoted to a summary strip.

**T12.** The instrument is called The Surge Monitor, bylined to Yorgo P. Bougás as his personal work until it is useful and verified.

---

## Part II: The Expanded Version

Part II substantiates every thesis point from Part I, with the evidence, the caveats, and the sources. Each section opens by stating which thesis point or points it substantiates. The mapping table below is the index: no thesis point is left unsubstantiated, and no substantiation is unmapped.

### Thesis-to-substantiation mapping

| Thesis point | Substantiated in |
|---|---|
| T1 — Two-hand clock | §II.2, §II.10 |
| T2 — Two velocities | §II.3, §II.4, §II.6, §II.14 |
| T3 — Full cycle 10–20+ years | §II.5, §II.6, §II.10, §II.14 |
| T4 — The bottleneck is institutional absorption | §II.3, §II.4, §II.7 |
| T5 — The productivity payoff has not arrived | §II.2, §II.4, §II.7, §II.11 |
| T6 — The mismatch is the largest ever measured | §II.4, §II.7, §II.11 |
| T7 — Four knobs | §II.5 |
| T8 — Heatmap verdict 23 / 5 / 0 / 2 | §II.7, §II.8, §II.11 |
| T9 — Late frenzy, turning point beginning | §II.8 |
| T10 — Backtesting validates the model | §II.10 |
| T11 — Heatmap-first instrument | §II.11 |
| T12 — The name and the byline | §II.1 |

§II.9 states the uncertainty bounds on all twelve thesis points. §II.12 carries the open questions on all twelve. §II.13 holds the sources behind all twelve.

---
### II.1 The Name

*Substantiates T12.*

**Recommendation: The Surge Monitor**, subtitle **"A General Purpose Technology Tracker by Yorgo P. Bougás, Confluence<1>"**.

**Reasoning.** The unit that recurs across technological revolutions is Perez's *great surge* — the 40-to-60-year process by which a revolution and its paradigm propagate across the economy. A name built on "surge" applies to the current revolution and to any future one, whether it is a new surge or (as with AI) a leap inside an existing surge; it does not tie the product to AI, to code, or to this decade. "Monitor" says what the instrument does: it watches continuously, it does not pronounce once. A clock implies a face and a needle; a monitor implies an instrument panel with readings that update — which is what the heatmap, the parametric curve, and the dated log actually are. The subtitle carries the product category (General Purpose Technology Tracker) and the author (Yorgo P. Bougás) without putting either in the name itself. **Attribution rule (Yorgo, 22 November 2026):** the tracker is his personal work, not Confluence<1> intellectual property — it becomes the firm's only when it is useful and verified. Until then, every byline, subtitle, and page carries his name, not the firm's. **Attribution update (Yorgo, 25 November 2026):** Confluence<1> is the affiliation on the byline — "Yorgo P. Bougás, Confluence<1>" — and nothing more. The tracker remains Yorgo P. Bougás's personal work, not Confluence<1> intellectual property; it becomes the firm's only when it is useful and verified, by his decision.

**Alternatives recorded:**
- **The Paradigm Tracker** — the techno-economic paradigm is the other recurring unit in Perez. Accurate, but "paradigm" is the more abstract term and the less evocative one; it also collides with the word's loose everyday use.
- **The Deployment Gauge** — names what the instrument measures (the passage from installation to deployment). Accurate, but "gauge" suggests a single reading, and the instrument's point is that no single reading suffices.

**Warning (standing).** Never shorten "General Purpose Technology" to its initials in the product name, in marketing, or in the site's navigation. Those initials now mean something else to most readers (generative pre-trained transformer models), and the collision would mislabel the product on first sight. The full words, every time.

---

### II.2 The Bedrock: Solow and Perez

*Substantiates T1 and T5.*

This section condenses v1 §2. The full framework exposition, with chapter-and-page references, remains in v1; nothing material is dropped here, and the criticisms are carried in full.

#### II.2.1 Perez: Technological Revolutions and Great Surges

**Source:** Carlota Perez, *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages* (Edward Elgar, 2002), with later papers and statements through 2025.

A **technological revolution** is "a powerful and highly visible cluster of new and dynamic technologies, products and industries, capable of bringing about an upheaval in the whole fabric of the economy" (Ch. 2, pp. 8–9). A **techno-economic paradigm** is "the main vehicle of diffusion of that set of generic 'tools' — hard, soft and ideological — which together modify the best-practice frontier for all"; once diffused it becomes the economy's "common sense". A **great surge of development** is "the process by which a technological revolution and its paradigm propagate across the economy"; each lasts "about five or six decades" (p. 15).

**The five great surges** (Perez's own approximate datings):

| # | Revolution (big-bang) | Irruption | Frenzy | Turning point | Synergy | Maturity |
|---|---|---|---|---|---|---|
| 1 | Industrial Revolution — Arkwright's Cromford mill, 1771 | 1770s–early 1780s | Late 1780s–early 1790s | 1793–97 | 1798–1812 | 1813–1829 |
| 2 | Steam and Railways — Stephenson's *Rocket*, 1829 | 1830s | 1840s | 1847 crash; 1848–50 | 1850–1857 | 1857–1873 |
| 3 | Steel, Electricity, Heavy Engineering — Carnegie Bessemer plant, 1875 | 1875–1884 | 1884–1893 | 1893–95 | 1895–1907 | 1908–1918 |
| 4 | Oil, Automobiles, Mass Production — first Model-T, 1908 | 1908–1920 | 1920–1929 | 1929–33 (Europe) / 1929–43 (United States) | 1943–1959 | 1960–1974 |
| 5 | Information and Telecommunications — Intel microprocessor, 1971 | 1971–1987 | 1987–2001 | 2001–?? (2002); 2007–??? (2010) — still open per Perez 2022–2025 | not yet reached | — |

**Two periods.** **Installation** (first 20–30 years): "the battle between the old and the new paradigm… an increasing process of decoupling between the new and the old industries"; led by financial capital; ends in a major bubble collapse. **Deployment** (second 20–30 years): the "Golden Ages" — "a steadier and more balanced prosperity, tending to spread to wider and wider portions of the population… ruled by the criteria of production capital" (Perez 2007, §1).

**Four phases.** **Irruption** ("A Time for Technology"): the big-bang amidst stagnation; new industries show "amazing growth and productivity feats". **Frenzy** ("A Time for Finance"): "Financial capital takes over; its immediate interests overrule the operation of the whole system. The paper economy decouples from the real economy"; the Gilded Age; infrastructure manias; "late Frenzy is financial bubble time". **Synergy** ("A Time for Production"): the deployment period's first half; "the closest the system ever comes to convergence"; infrastructure installed during frenzy yields "dynamic expansion and economies of scale". **Maturity** ("A Time for Questioning Complacency"): market saturation, diminishing returns, idle financial capital seeding the next revolution.

**The turning point** is "neither an event nor a phase; it is a process of contextual change. It can take any amount of time, from a few months to several years." It is "the swing of the pendulum from the extreme individualism of Frenzy to giving greater attention to collective well being, usually through the regulatory intervention of the state". The outcome is **not guaranteed**: "The resulting framework can enable a 'golden age' or only a modified, but still unstable version of the 'gilded age'." Three structural tensions make frenzy unsustainable: (1) real vs. paper wealth; (2) potential supply vs. existing demand ("premature market saturation"); (3) the socially excluded vs. the beneficiaries of the bubble (Ch. 11, pp. 115–118).

**Financial capital vs. production capital.** "Production capital is the wealth creator. It is fixed and knowledge-bound; it has a long-term bias… Financial capital is in charge of reallocating wealth; it is flexible and mobile and has a short-term bias." The bubble is functional, not accidental: financial capital "unwittingly" finances the infrastructure deployment later uses.

**Institutional mismatch** (Ch. 3, pp. 26–27): the techno-economic and socio-institutional spheres change at different rhythms, so "the first 20 or 30 years of diffusion of each technological revolution lead to an increasing mismatch between the economy and the social and regulatory systems." The mismatch resolves only by institutional recomposition at the turning point.

**Phase markers.** Perez provides almost no numeric thresholds — the one quantified marker found is the top-0.1% income share (Perez 2007, Fig. 5, via Piketty & Saez 2003): over 10% of declared income during the 1920s and 1990s bubbles, falling to ~6% in deployment.

**Perez on AI.** Her position, repeated 2017–2025: **AI is NOT a new technological revolution. It is a revolutionary technology inside the still-unfolding ICT revolution** — "a third leap" after microprocessors and the internet (*Project Syndicate*, March 2024). Her test: a revolution requires a "strongly interrelated constellation" including a new all-pervasive low-cost input and a new infrastructure — AI has neither of its own; it rides the microprocessor and the internet. On the ICT surge's status: "we seem to be stuck in the installation period or in what I call the 'turning point'… Expectations for a golden age after the NASDAQ collapse, and again after the 2008 financial crash, have been disappointed" (2022). "But we are late. This time the record in length has been broken, for both the installation and the turning point itself" (2025).

**Where others disagree:** several 2025–2026 practitioner frameworks treat AI as a sixth surge (e.g. Coatue's cycle framework, per Burnett 2026). Other scholars place the ICT surge differently: Jelassi & Enders (2008) put ICT in synergy from 2003 — directly contradicting Perez's own 2022–2025 position.

#### II.2.2 Perez: Criticisms and Limits

1. **The framework refuses to be a clock.** "Nor can predictions be made about the length or depth of the recession, or about the type of solution applied" (2002, Ch. 11, p. 115). "The length of the Turning Point is indeterminate… It can last as little as two years or as long as the whole of the 1930s plus WWII" (Perez 2007, §3). The phases are "a useful heuristic tool". The book concedes the model does not show up in aggregate statistics: "there is no expectation of neat upswings and downswings in aggregate metrics like GDP [gross domestic product]. Aggregate figures have a tendency to conceal what is really going on" — a direct problem for any Solow-style quantification.
2. **The shifting ICT turning point — the framework's live predictive failure.** Perez has moved the current phase boundary at least four times in 23 years, always extending the turning point: 2001–?? (2002); "indeterminate" (2007); double bubble 2000 + 2008 as a single turning point (2009–2010); "stuck in the installation period or… the 'turning point'" (2022); "the record in length has been broken" (2025). The ICT surge is now ~55 years old, at or beyond the top of her own 40–60-year range, with deployment not yet begun by her account.
3. **Small-n.** Perez's n is five surges — four complete. Norkus (2013) argues rigorous statistical testing of ~50-year waves requires time series of "ca. 350–500 years (including 7–10 cycles)". The Slutsky–Yule effect is the standard objection: applying moving averages and rates of change to random data can manufacture wave-like patterns.
4. **Descriptive/ex post, possibly unfalsifiable.** Big-bang dates are identifiable "only with hindsight" (Ch. 2, p. 12). No phase identification has ever been made *in advance* and then confirmed. The escape hatches are wide: phases "are not strictly separated"; the turning point's length is "indeterminate"; the outcome can be golden *or* gilded. No published statement by Perez of a falsification condition was found.
5. **Does finance cause the pattern, or merely accompany it?** The five cases are consistent with both stories. Mazzucato (*The Entrepreneurial State*, 2013) is the strongest counterweight on the *state's* role in installation. (For balance: Yerger 2024 argues Mazzucato's claims "do not survive the scrutiny of the Supply-Chain Fallacy.")
6. **Determinism / teleology.** Perez rejects the label, but the framework claims both a strong regularity (the sequence always happens) and a radical contingency (the outcome depends on politics). The tension is unresolved in her work.
7. **Generalisation limits.** All five surges are drawn from the capitalist core over ~250 years. Perez herself argues the current surge is structurally different (globalisation, mental labour, China, financialisation) — which explains the delay but concedes the historical sample may not govern the present case.
8. **Reflexivity.** A widely believed clock changes behaviour (Neumann 2015, via Merton). Predicting a crash can change the crash.
9. **Mainstream standing.** The long-wave tradition is heterodox; Perez's framework has no standing in mainstream growth theory. Roehner (2003) called the book "a big fresco, which will be refined and made more precise through subsequent studies" — programmatic, not settled.
10. **Internal inconsistencies.** Perez is not fully consistent on the Belle Époque ("a Gilded Age" in 2007; a golden age in 2010, 2013, 2025), and the 3rd surge's turning point is dated 1893–95, 1890–95, and 1890–93 in different texts. The golden/gilded split is not a clean binary in her own usage.

#### II.2.3 Solow: Growth Accounting, the Residual, and the Paradox

**Solow 1956–1957.** Robert Solow's "A Contribution to the Theory of Economic Growth" (*Quarterly Journal of Economics*, 1956) built an aggregative growth model around a constant-returns-to-scale aggregate production function. The 1957 follow-up, "Technical Change and the Aggregate Production Function" (*Review of Economics and Statistics*, 1957), turned the model into measurement: output growth decomposed into the growth of capital and labour inputs, each weighted by its share in national income, plus a term capturing Hicks-neutral shifts of the production function — Total Factor Productivity (TFP).

**The 7/8ths finding.** Solow's 1957 study of the United States (US) economy, 1909–1949, found output per man-hour approximately doubled, and concluded that about one-eighth of the increment could be attributed to increased capital per man-hour and the remaining seven-eighths to the residual (Solow 1957, p. 320). Qualifier: the 7/8ths conclusion was **atypical** — Denison (1962), adding labour quality, cut the residual's share to "a little under half".

**The Solow paradox (1987).** In "We'd better watch out," *New York Times Book Review*, 12 July 1987, p. 36: *"You can see the computer age everywhere but in the productivity statistics."* US computing capacity rose ~100-fold in the 1970s–80s while labour-productivity growth slowed from over 3% in the 1960s to roughly 1% in the 1980s.

**The productivity record** (US nonfarm business labour productivity, average annual growth): 1947–1973 ~2.8%; 1973–1995 ~1.5%; 1995–2004 ~2.8% (the information-technology resurgence); 2005–2015 1.3%; Q4 2007–Q4 2019 1.5%; 1947–present long-run average **2.2%**; Q4 2019–present 2.1% annualised (Bureau of Labor Statistics (BLS), *Productivity and Costs*, 24 Mar 2026). The historical parallel: Paul David (1989/1990) showed the electric dynamo had the same lag — ~40 years from the first power stations before electric drive covered more than half of factory power capacity.

**The J-curve** (Brynjolfsson, Rock & Syverson, "The Productivity J-Curve: How Intangibles Complement General Purpose Technologies," National Bureau of Economic Research (NBER) Working Paper 25148, September 2018; published in the *American Economic Journal: Macroeconomics*, vol. 13(1), pp. 333–372, January 2021 — see §II.14 for the two dates). General-purpose technologies require large **complementary intangible investments** — business-process redesign, co-invention of new products and business models, human capital — poorly measured in national accounts. While firms accumulate unmeasured intangible capital, measured TFP growth is **underestimated**; later, when the intangible stocks pay off, measured productivity is **overestimated**. The error follows a J-curve. The authors argue **implementation lags** have likely been the biggest contributor to the paradox. The J-curve is the strongest theoretical case that the current gap is a *lag*, not a *failure* — but it is a model, not a measurement: it cannot tell you where on the J you are.

**The mismeasurement debate.** Syverson (2017) ran four tests, all failing the hypothesis that mismeasurement explains the slowdown. The honest position: mismeasurement is real and understates digital-era welfare gains, but it is not a rescue for the productivity numbers. A 2026 International Monetary Fund (IMF) paper revives a narrower version: the wedge between task-level gains (14–56%) and macro estimates (0.2–1.3 percentage points per year over ten years) is partly a measurement problem, but it does not claim mismeasurement explains the aggregate gap.

**Forecasts of AI's productivity effect (all estimates, not measurements).** Acemoglu (2024/2025): ≤0.66% TFP over 10 years (explicitly an upper bound). Goldman Sachs (March 2023): ~7% higher annual global GDP over 10 years. Aghion & Bunel (2024): 0.68 percentage points per year additional TFP growth (6.8% cumulative). Organisation for Economic Co-operation and Development (OECD) (2024/2025): 0.2–1.3 percentage points per year. IMF (2026, patent-data paper): up to 3.8% long-term labour-productivity impact. Korinek et al. (2026): 0.7% / 3.1% / 13.4% TFP over 6 years under modest / substantial / extreme scenarios. The spread — 0.66% cumulative vs 6.8% cumulative over a decade — is driven almost entirely by two assumptions: the share of tasks AI affects, and the cost savings per task.

#### II.2.4 Solow: Criticisms and Limits

1. **Abramovitz — "a measure of our ignorance."** The residual is what we *cannot* explain, not an explanation. Standard growth accounts are "misleading" as descriptions of proximate sources, because scale effects, education, research and development, and reverse causation all get buried in the residual.
2. **The Cambridge capital controversy (aggregation).** Heterogeneous capital goods have no common natural unit; aggregating them into a single stock requires prices, which depend on the rate of profit the theory is supposed to explain. Samuelson conceded the point in 1962, retreating to treating the aggregate production function as a "parable." Every TFP number rests on an aggregate capital stock whose construction is theoretically contested.
3. **TFP is a residual, not an explanation.** It absorbs measurement error, omitted inputs (human capital, intangibles), utilisation changes, reallocation effects, market power, and increasing returns. Denison (1962) showed that adding labour quality alone cut the residual's share below half.
4. **Assumption-dependence.** Growth accounting requires perfect competition, constant returns, and Hicks-neutrality. With market power, income shares no longer equal output elasticities. With non-neutral technical change (AI is plausibly labour-augmenting in some tasks, capital-augmenting in others, and task-replacing), the single "A" is a fiction.
5. **Endogeneity — technology is not exogenous.** Endogenous growth theory (Romer 1986, 1990; Aghion & Howitt 1992) made technical change a product of profit-seeking investment, human capital, and institutions. A tracker built only on Solow can measure the residual; it cannot explain why the residual moves when it does.
6. **The general-purpose-technology lag problem.** Crafts (2019): "the impact of new general-purpose technologies on growth typically takes a long time to materialize, ICT being the notable exception." The dynamo took ~40 years; the computer took ~25 years from commercialisation to the productivity resurgence. Any tracker that reads "AI is 4 years post-ChatGPT" against those precedents should expect the productivity payoff to be years away — if it comes at all.

#### II.2.5 How Solow and Perez Combine into One Instrument

**Division of labour.** Perez supplies the instrument's *face*: the phase sequence, the markers, and the causal story (the finance/production pendulum, institutional mismatch, the turning point as recomposition). Solow supplies the instrument's *measurement*: growth accounting and TFP — the test of whether the technology is actually delivering aggregate gains. Neither alone is an instrument: Perez's framework is qualitative, retrospective, and (by its author's admission) non-predictive; Solow's apparatus measures the residual but cannot explain why it moves, and assumes away the very things a cycle theory cares about (finance, diffusion lags, institutional change).

**The bridge: the paradox is the signature of installation.** During installation, investment and diffusion run ahead of measured productivity — that is what the Solow paradox *is*. During deployment (synergy), the paradox resolves: TFP rises, gains diffuse, the paradigm's productivity potential is realised economy-wide. So the instrument reads Perez markers for *where in the sequence* and Solow measurements for *whether the payoff has arrived*. The two readings can disagree — and when they do, the disagreement is itself the information.

**The J-curve vs Acemoglu fork.** The two best explanations of the current gap are compatible, and the instrument must display both rather than choose:
- The **J-curve** (Brynjolfsson, Rock & Syverson) governs *timing*: the gap is a lag. Firms are accumulating unmeasured intangible capital; measured TFP is understated now and will be overstated later. The model cannot say where on the J we are.
- **Acemoglu's arithmetic** governs *ceiling*: only ~4.6% of gross domestic product is in tasks AI can profitably automate at current cost savings, so the gap will mostly persist even after diffusion. His ≤0.66% TFP over 10 years is explicitly an upper bound.

Both can be true at once. What would resolve the fork is time plus data: if TFP rises materially over the next 2–3 years with credible AI attribution, the J-curve reading gains; if it stays flat while adoption saturates, the ceiling reading gains.

**The two-hand decision.** Following Perez (2024), the instrument does *not* treat AI as a sixth surge: AI has no new cheap key input or infrastructure of its own — it rides microprocessors and the internet — and therefore fails Perez's own tests for a revolution. Instead: the **outer hand** is the ICT great surge (extended turning point, set by Perez's scholarship); the **inner hand** is the AI sub-cycle (irruption dated to November 2022, ChatGPT's public release — provisional, since Perez warns big-bangs are identifiable only in hindsight; frenzy from 2023). The inner hand is where CI SITREP's evidence lives, and it is the hand the tracker's parameters actually move. The sixth-surge alternative is recorded as open question Q1 (§II.12).

**The judgment rule (how the needle is set).** Perez gives no numeric thresholds, so the needle is a judgment over parameters — and the rule for that judgment must be stated, not improvised:

1. Each parameter carries a **phase reading**: the phase its current value points to (irruption / frenzy / turning point / synergy / maturity), with its source, date, and quality note.
2. The needle is the **preponderance** of phase readings, weighted by evidence quality (report-rated ●●●●/●●●○ figures and official statistics weigh more than vendor claims and single surveys).
3. **Vetoes:** (a) no deployment (synergy) call while TFP is flat or falling and the micro-macro gap is wide; (b) no turning-point-*completed* call while the institutional framework is unsettled (proposals and consultations are not law; first enforcement actions are not a settled regime); (c) a crash or funding contraction is a turning-point *confirmation*, not a requirement for the call — the turning point is a process, and its early markers (regulatory recomposition, liability crystallisation) can precede any crash.
4. The needle is a **band**, not a point. Its width reflects the spread of phase readings and the quality of the underlying evidence. The band is shown, never hidden.
5. The needle **never moves on a single parameter**. A move requires a stated reason, a dated log entry, and (for a phase change) at least two parameters moving in the same direction.

---
### II.3 The Blind Spot: Why Solow and Perez Alone Are Insufficient

*Substantiates T2 and T4.*

The prior argument, adopted with two corrections:

**The argument.** Both frameworks were calibrated on physical, heavy-capital-expenditure eras where diffusion was bottlenecked by laying track, stringing wire, and shipping hardware over 30 to 50 years. Created intelligence rides existing digital distribution rails, compressing the technical deployment timeline — while the bottleneck moves to institutional absorption, governance, and trust, which still move at human speed. A tracker built on Solow and Perez alone would therefore make two errors: it would read the cycle's *speed* off physical-era timings, and it would have no instrument for the *bottleneck*, because Perez's institutional mismatch is a qualitative observation, not a measured parameter.

**Correction 1 — Solow is not era-bound; Perez's timings are.** That argument is aimed at both frameworks equally, but it lands differently on each. Solow's apparatus is a measurement method (growth accounting), not an era-bound theory: it applies to any economy in any era, and its limits (the Cambridge controversy, the residual's opacity) are timeless, not historical. The blind spot is in *Perez*: her phase lengths (20–30 years per period) and her diffusion mechanism (physical infrastructure build-out) were calibrated on physical revolutions. What needs updating is the *clock speed* and the *unit of analysis*, not the measurement. This matters because it tells us where to add: not a new measurement apparatus, but a velocity correction (§II.6) and component-level instruments (§II.4) that Perez's economy-wide lens cannot see.

**Correction 2 — created intelligence does not simply "ride existing rails".** That phrasing collapses two different rails. *Distribution* rails exist: an application programming interface (API) call reaches the world instantly, which is why ChatGPT reached 100 million monthly active users in about two months. But *compute* rails are being built right now at railroad scale: $376.1bn of hyperscaler capital expenditure in 2025, a data-centre pipeline over $1tn, 1,360 large hyperscale data centres worldwide at the end of 2025 with almost 800 more in the pipeline (Synergy Research Group). The 2026 guided annual capital-expenditure rate alone exceeds the inflation-adjusted cost of the Interstate Highway System ($729bn, 1956–1992). So the blind-spot argument needs its own correction: the technical timeline is compressed at the *distribution* layer and *not* compressed at the *compute* layer — and the compute build-out is itself the largest frenzy marker in the parameter set (A1, A2). This is why α is two numbers, not one (§II.5.1).

**What the blind spot requires.** Four additions, each filling a named gap:
- A mechanism for the *shape* of the productivity dip (the J-curve as the Y-axis, not just a fork to display) — §II.4.1.
- A *component-level* lens, because Perez sees only the whole economy and the report's evidence is component-level (models, agents, verification, governance) — §II.4.2.
- A *cycle* mechanism explaining why capital expenditure does not stop after one wave — §II.4.3.
- A *friction* account of diffusion speed, separating the technical friction (near zero) from the institutional friction (human-speed) — §II.4.4.

---

### II.4 The Four Complementary Frameworks

*Substantiates T2, T4, T5, and T6.*

Each framework fills a named gap in Solow/Perez. Each is mapped to the report's evidence and to the existing 30 parameters. Where the report lacks the evidence, that is stated.

#### II.4.1 The Productivity J-Curve

**The gap it fills.** Perez's framework has no mechanism for the *shape* of the productivity dip during installation — it observes the mismatch qualitatively but cannot say why measured productivity falls (or stalls) while investment soars, or what determines the depth and duration of the trough. Solow's apparatus measures the residual but cannot explain its movement. The J-curve supplies the mechanism: complementary intangible investments (business-process redesign, co-invention, human capital, and — for created intelligence — verification, guardrails, and governance) consume measured inputs while producing unmeasured output, so measured Total Factor Productivity is understated during the build-out and overstated during the harvest.

**Note on provenance.** The J-curve is *not* new to this model: v1 already carried it (v1 §2.3, v1 §2.5) as one side of the J-curve vs Acemoglu fork. What v2 changes is its *role*: it is promoted from a fork to display into the Y-axis of the parametric curve (§II.11.3, Line B — Net Enterprise Profit-and-Loss Capture), and its depth is operationalized as β (§II.5.2). The citation is corrected in v2: National Bureau of Economic Research Working Paper 25148 (September 2018); *American Economic Journal: Macroeconomics*, vol. 13(1), pp. 333–372, January 2021 (see §II.14).

**Evidence mapping — the report HAS it (this is the report's home ground).**
- **The verification tax (E6):** Google's DevOps Research and Assessment (DORA) surveys — 2024: −1.5% throughput, −7.2% delivery stability per +25% AI adoption (correlational); 2026: time saved generating is re-spent auditing. GitClear: +81% duplicate code blocks; two-week churn +15%; refactoring 21% → 3.8% of changed lines (623 million code changes).
- **The review-cost anchor (β's only measured value):** a post-hoc security review lifts working-and-secure output to 47–56% at ~2.5× the cost — still leaving about half insecure (SusVibes re-run, vendor-commissioned by Checkmarx, ●●○○ Reported). See §II.5.2.
- **The return gap (E5):** the Massachusetts Institute of Technology's NANDA study ("The GenAI Divide", July 2025): 95% of organisations reported zero measurable profit-and-loss return from generative AI. Capgemini: ~50% of financial institutions cannot consistently demonstrate a return on agentic AI initiatives. Atlanta Federal Reserve Bank / Richmond Federal Reserve Bank / Duke University chief financial officer survey (~734 executives): over 80% of firms reported no impact on employment or productivity over the previous three years.
- **The generation-vs-verification gap (Agentic panel):** A.S.E 2.0 (the agentic security-evaluation benchmark): 74.0% functional pass vs 18.4% secure on the same tasks, same model. SecPRBench: the best frontier model catches 78.1% of vulnerability-introducing changes in agentic pre-merge review; the weakest catches 32.5%.
- **Parameter mapping:** E4 (micro-macro gap), E5 (firm-level returns), E6 (verification tax), E7 (forecast spread — the J-curve vs Acemoglu fork is the spread's main driver), C7 (failure counts — the cost of skipping the intangible investment).

**Evidence mapping — the report DOESN'T have it.** No hours-or-dollars net figure exists anywhere in the evidence base (the Net impact ledger's footnote states this). No verification-cost data outside the code domain. No J-curve series — the SusVibes 2.5× is a single point, and DORA's figures are correlational survey results, not cost accounts.

#### II.4.2 Wardley Mapping

**The gap it fills.** Perez sees only the whole economy: a surge, a paradigm, a phase. But the report's evidence — and an executive's decisions — are *component-level*: foundation models, agent frameworks, orchestration, verification, governance, guardrails. A single phase reading for "AI" hides the fact that its components sit at wildly different stages of evolution. Wardley Mapping supplies the component lens: every capability evolves along an axis from Genesis (novel, just invented) → Custom-Built (bespoke, hand-made) → Product (off-the-shelf, multiple vendors) → Commodity (standardised, metered, taken for granted), and components drift rightward over time. The strategic payoff is the *mismatch made visible*: a firm custom-building what is already a commodity wastes its engineering; a firm treating as a commodity what is still genesis takes risks it cannot see.

**Provenance and standing.** Created by Simon Wardley at Fotango in 2005 (the evolutionary framing dates to 2004), developed further at Canonical (United Kingdom) 2008–2010, published openly in his book *Wardley Maps* (Creative Commons, 2015 — the 2015 date is the book's, not the technique's; see §II.14). Wardley Mapping is a *practitioner* framework, not a peer-reviewed theory: it is widely used (including in United Kingdom government digital services) but has no statistical validation, and the stage placements are judgments, not measurements. The tracker uses only the evolution axis and the anchor-at-user-need discipline — not the full doctrine/gameplay apparatus — and every staging in §II.11.2 is labelled a judgment with its evidence anchor.

**Evidence mapping — the report HAS it (partially).**
- **Foundation models → Product, drifting to Commodity.** Multiple frontier labs, open-weights models, price competition. The report's evidence is thin here (subscription price lists only; no model-pricing series), so the staging rests on market structure, not price data.
- **AI coding assistants → Product.** 67% of organisations use AI-powered coding assistants (Black Duck, ●●●○ Corroborated); multiple vendors compete.
- **Agent frameworks → Product.** "By late 2026 the multi-agent field has consolidated around a handful of frameworks" — LangGraph, Microsoft Agent Framework, Strands, Google Agent Development Kit, OpenAI Agents software development kit (SDK) — report §3, prose, unrated; F2.
- **Enterprise-wide orchestration → Custom-Built.** Only 10% have achieved enterprise-wide orchestration; only 5% have institutionalised enterprise-scale agentic capability (Capgemini, ●●○○ Reported).
- **Verification / security review of AI code → Custom-Built.** Best reviewer catches 78.1%, weakest 32.5% (SecPRBench) — no standard, wide variance.
- **Agent identity / attribution → Custom-Built.** 2% have the identity tools to govern agents (SailPoint); 82% cannot reliably attribute agent actions (Whitfield).
- **Deterministic guardrails / approval gates → Genesis → Custom-Built.** The pattern is emerging, not standard: Strands Box (October 2026, open-source, operating-system containment plus policies enforced outside the agent's process); Google Semantic Governance Policies (Preview, 20 November 2026 — a large language model judge at the Agent Gateway, probabilistic verdicts); Anthropic, Pydantic, LangChain, Microsoft pre-tool-use controls (September–October 2026).
- **Kill switches / supervision → Custom-Built.** 30% have a formally deployed, documented kill switch; 23% of firms with agents in production never tested theirs (Writer / Workplace Intelligence).
- **Audit / certification of AI codebases → Genesis.** No market standard exists; the report's certification content is framework-stage (this is Confluence<1>'s own product territory).
- **Agent liability / insurance → Genesis.** Liability asserted in bank customer terms and attorney-general actions, untested in court (D3).
- **Parameter mapping:** B3 (breadth vs depth — the Wardley explanation for "broad but shallow": the easy components commoditized first), C2–C5 (the governance components are all Custom-Built or Genesis while deployment is Product-scale), F2 (consolidation — the Product stage consolidating toward oligopoly, as Perez predicts for late frenzy).

**Evidence mapping — the report DOESN'T have it.** No model-pricing series (the commodity-drift evidence for foundation models is asserted, not measured). No vendor market shares for frameworks, verification tools, or governance products. No build-vs-buy cost data. The Wardley panel is therefore the tracker's most judgment-heavy view, and it is labelled as such (open question Q14, §II.12).

#### II.4.3 The Infrastructure-Application Cycle

**The gap it fills.** Perez's framework has one infrastructure build-out per surge, financed by the frenzy bubble and then used by deployment. It has no mechanism for *repeated* infrastructure waves *within* a surge — yet the evidence shows capital expenditure not stopping after one wave. Dixon's cycle supplies it: infrastructure build-outs enable killer applications, which expose infrastructure limits, triggering a second wave of infrastructure — a mutually reinforcing feedback loop between applications and infrastructure. For created intelligence: graphics processing units and models (Infrastructure 1) → agentic applications → outages, hallucinations, and security failures → verification, deterministic guardrails, and audit layers (Infrastructure 2). The cycle explains why the capital-expenditure curve has a second hump coming, and why "Infrastructure 2" is where the next investable layer sits.

**Provenance and standing.** Practitioner framework, no single canonical publication and no peer review. The core statement is Dixon's: "The core driver of the computing movement is the mutually reinforcing feedback loop between applications and infrastructure" (cdixon.org / a16z writing, 2010s–2020s; see §II.14). The "Infrastructure 2 = verification, guardrails, audit" application to created intelligence is the prior research's — and now this model's — not Dixon's. The tracker treats the cycle as a *heuristic for where the next build-out lands*, not as a law.

**Evidence mapping — the report HAS it.**
- **Infrastructure 1 (complete, in frenzy):** A1–A2 (hyperscaler capital expenditure $376.1bn in 2025; data-centre pipeline over $1tn); A4 (NVIDIA $5tn market capitalisation, data-centre revenue $193.7bn).
- **The applications wave (under way, broad but shallow):** B1–B3 (86% of US financial firms use AI; 79% run agents in production; only 10% orchestrate enterprise-wide).
- **The limits exposed (measured, in the report's home domain):** C7 (188 production-damage cases; AI patches carry ~11× the vulnerabilities of developer patches); A.S.E 74.0% functional vs 18.4% secure; 55.6% passed every test while a working exploit succeeded.
- **Infrastructure 2 (emerging, Genesis → Custom-Built):** Strands Box, Google Semantic Governance Policies, Anthropic Managed Agents, Pydantic AI ToolCallJudge (September–November 2026); CommBank open-sourcing its CodeCheck review harness (19 November 2026); the report's own §1.2 product landscape (verification and scanning tools).
- **Parameter mapping:** A1–A2 (Infrastructure 1's scale), B3 (the applications wave's shallowness), C7 + Agentic-panel benchmarks (the exposed limits), F2 (Infrastructure 2 consolidating early around hyperscaler platforms — "cloud is becoming the governance layer", Capgemini 52%).

**Evidence mapping — the report DOESN'T have it.** No investment figures for Infrastructure 2 (no venture funding, revenue, or spending data for the verification/guardrail/audit layer — the report has no market-size data at all; see §II.7 gaps). The cycle's second hump is therefore *located* (we know what it consists of) but not *sized* (we cannot say how big it is). The tracker's Infrastructure 2 reading is qualitative until the report gains market data.

#### II.4.4 Diffusion and Institutional Friction

**The gap it fills.** Perez's diffusion is a single rhythm: the paradigm spreads, the institutions lag, the mismatch resolves at the turning point. But the report's evidence shows *two* diffusion speeds running simultaneously — technical adoption measured in months, institutional absorption measured in years — and Perez has no vocabulary for the split. Rogers (*Diffusion of Innovations*, 1962) and Moore (*Crossing the Chasm*, 1991) supply the adoption mechanics (adopter categories, the chasm between early adopters and the early majority); the friction split supplies the explanation for why the two speeds differ: **technical friction** for created intelligence is near zero (an API call is instant global deployment), while **organisational and regulatory friction** (legal liability, security audits, profit-and-loss accountability, workforce retraining) remains stubbornly human-speed.

**Provenance and standing.** Rogers (1962, 5th edition 2003) and Moore (1991) are the standard diffusion references; both are well-evidenced for the adoption-curve shape. The **friction split itself is the prior research's addition**, not Rogers' or Moore's — neither author separates technical from institutional friction in these terms (see §II.14). The tracker adopts the split as a *working distinction* because the report's evidence demands it, and operationalizes the institutional side as δ (§II.5.4). The split's status is: useful, unproven, and in need of the δ measurement to become more than a slogan.

**Evidence mapping — the report HAS it (this is the report's strongest evidence).**
- **Technical friction near zero:** ChatGPT's two-month ramp to 100 million users (see §II.6); the ACA Group / National Society of Compliance Professionals (ACA/NSCP) survey: 45% → 71% → 86% in two years (B1); ~47% of code AI-written within four years of the big-bang (B2).
- **Institutional friction at human speed — the whole of Group C:** 98% have policies, 47% bypass them (C1); 73% permit agents, 8% monitor them (C2); 79% run agents, 2% have identity tools (C3); 35% cannot confidently shut down a rogue agent (C4); 38% test outputs (C5); 79% shadow AI (C6).
- **The regulatory component of friction:** D2 (the US federal gap — generative and agentic AI expressly out of model-risk scope, the request for information still unpublished); D1 (milestone density — the recomposition is under way but every item is a proposal, consultation, or first enforcement action, not settled law).
- **Parameter mapping:** B1–B3 (technical diffusion — the fast half), C1–C7 + D1–D3 (institutional absorption — the slow half), δ (§II.5.4 — the friction split's quantitative form).

**Evidence mapping — the report DOESN'T have it.** No time series for any governance metric (every C-group figure is a single point), so the *rate* of institutional absorption is unmeasured — δ cannot yet be estimated (§II.5.4). No data on workforce retraining, organisational restructuring, or the internal change-management half of absorption.

---
### II.5 The Four Knobs, Operationalized

*Substantiates T7 and T3.*

Greek letters are not measurements. Each knob below is defined as a measurable indicator (or a stated pair of indicators), with its proposed source, its value today where determinable, its mapping onto the existing parameters, and an honest statement of what cannot yet be measured. Where a knob cannot be measured today, the document says so and states what measurement would unlock it.

#### II.5.1 Alpha: Physical-to-Digital Rails Ratio

**Definition.** α = (new physical infrastructure investment required for deployment) / (total deployment investment). It answers: how much of this revolution must be *built* in the physical world before it can diffuse?

**The correction: α is two numbers, not one.** The prior framing treats created intelligence as riding existing rails. The evidence says the distribution layer does and the compute layer does not — and the two layers have opposite implications. The tracker therefore carries α as a pair:

- **α_distribution — the share of *distribution* requiring new physical build.** For created intelligence: **≈ 0.05–0.10 (judgment, low confidence).** An application programming interface call rides the existing internet, cloud, and endpoint infrastructure; marginal distribution cost per new user is near zero. Evidence: ChatGPT's two-month ramp to 100 million monthly active users required no new consumer infrastructure (UBS / Similarweb, via Reuters, February 2023). *What would firm this up:* a defined denominator (total distribution investment) — currently no published aggregate exists; the value is a judgment anchored on the adoption-speed evidence, not a computed ratio.
- **α_compute — the share of *compute supply* requiring new physical build.** For created intelligence: **≈ 0.7–0.9 (judgment from magnitudes, medium confidence).** The compute rails are being built now, at railroad scale: $376.1bn hyperscaler capital expenditure in 2025 (A1); a data-centre pipeline over $1tn (A2); 1,360 large hyperscale data centres worldwide at end-2025 with almost 800 more in the pipeline (Synergy Research Group). The 2026 guided annual capital-expenditure rate ($720–745bn) alone exceeds the inflation-adjusted cost of the Interstate Highway System ($729bn, 1956–1992). Most of the compute spend is new physical plant: data centres, power, cooling, chips. *What would firm this up:* a published "total AI investment" denominator (no such aggregate exists — the tracker would need to construct one from capital expenditure, venture funding, and enterprise spend figures, each with its own methodology caveat).

**Baselines for comparison.** Railroads: α ≈ 0.9 (nearly everything physical — track, rolling stock, stations, telegraph). Personal computers / internet (1990s): α_distribution low (telephone lines existed), α_compute moderate (personal computers and servers had to be manufactured and shipped; the fibre build-out was the physical bottleneck). The historical α values are qualitative — no like-for-like historical series exists, and the tracker does not invent one. **Open question Q16 (§II.12):** construct a sourced historical α baseline (railroad investment as a share of gross domestic product in the 1840s–1870s; internet build-out capital expenditure 1995–2001) before the baseline curve in §II.11.3 is drawn as anything more than schematic.

**Parameter mapping.** α_distribution → B1, B2, B3 (the adoption-speed evidence). α_compute → A1, A2, A6 (the build-out's scale and its debt funding). **What α governs:** the Velocity Multiplier's technical half (§II.6) — low α_distribution is *why* technical diffusion compresses; high α_compute is *why* the frenzy's capital-expenditure signature is so large.

#### II.5.2 Beta: Verification-to-Generation Cost Ratio

**Definition.** β = (cost to verify + remediate artificial-intelligence output) / (cost to generate it). β > 1 means verification costs more than generation; β = 1 is parity; β < 1 means verification is cheaper than generation (the deployment state, where verification is automated and amortised). β governs the *depth* of the J-curve dip (Line B, §II.11.3): the higher β, the deeper and longer the profit-and-loss trough.

**Today's value — code domain: β ≈ 2.5.** Source: the SusVibes re-run — a post-hoc security review lifts working-and-secure output to 47–56% at ~2.5× the cost (●●○○ Reported). **Caveats, stated plainly:** (a) single study, vendor-commissioned (Checkmarx); (b) the denominator's construction is the study's own — "2.5× the cost" is the review's cost relative to the unreviewed generation cost on the study's terms, and the tracker has not independently verified the cost accounting; (c) the review still leaves about half of tasks insecure, so β ≈ 2.5 buys only *partial* verification — the fully-verified β (what it costs to reach ~100% secure) is higher and unmeasured; (d) code only — no β exists for agentic workflows, legal or finance outputs, or customer-facing AI.

**Corroborating proxies (not β itself, but the same phenomenon).**
- A.S.E 2.0: 74.0% functional pass vs 18.4% secure on the same tasks, same model — the gap between generation success and verified-secure success is 55.6 points.
- SecPRBench: the best frontier reviewer catches 78.1% of vulnerability-introducing changes; the weakest catches 32.5% — reviewer effectiveness varies 2.4×, so β varies by tool, not just by task.
- DORA (E6): time saved generating is re-spent auditing (2026) — the verification tax in time rather than dollars.
- GitClear (E6): +81% duplicate code blocks; refactoring 21% → 3.8% of changed lines — the cleanup cost that β must eventually include (remediation, not just review).

**What β governs and what would move it.** β falling toward 1 is the signal the J-curve dip is bottoming: verification automation (deterministic guardrails, Infrastructure 2 — §II.4.3) is the mechanism that lowers β. β *rising* would mean the verification burden is growing faster than generation is cheapening — the dip deepening. **Parameter mapping:** E6 (the verification tax — β's home), E5 (firm-level returns — β is the cost side of the return gap), E4 (the micro-macro gap — β explains part of why task-level gains do not reach the macro figures), C7 (failure counts — the cost of *not* paying β).

**What cannot be measured yet.** β outside code (no data). β over time (no series — the SusVibes figure is a single point; a β series requires the measurement to be repeated). The fully-verified β. **Proposed sources going forward:** repeat the SusVibes-style measurement annually (or find an independent replication — the vendor-commissioned status is a standing weakness); DORA's annual survey as a secondary indicator (time-based, not cost-based); the report's watch to add verification-cost figures to its evidence base as they appear. **Open question Q13 (§II.12):** is a single β meaningful across domains, or does each domain (code, agents, finance, legal) need its own β? The tracker's provisional answer: one β per domain, with code-β as the only measured one.

#### II.5.3 Gamma: Vendor Concentration and Hyperscaler Lock-In

**Definition.** γ measures how concentrated the supply of the revolution's key inputs is, and how locked-in buyers are. The prior framing treats it as one knob; the evidence says it is three sub-indicators, and they point in different directions.

**γ₁ — Accelerator concentration (Herfindahl-Hirschman Index for AI accelerator revenue).** The Herfindahl-Hirschman Index (HHI) is the standard concentration measure: the sum of squared market shares (0–10,000). United States Department of Justice / Federal Trade Commission thresholds: above 1,800 is highly concentrated (2023 guidelines); above 2,500 under the 2010 guidelines.
- **Today: HHI ≈ 5,750 (my calculation; wide band).** NVIDIA holds ~73–81% of AI accelerator revenue in 2026 (Silicon Analysts / International Data Corporation / Axis Intelligence estimates — methodology-dependent, and *no audited market-share table exists*), Google tensor processing units ~8%, Advanced Micro Devices ~7%. NVIDIA's share peaked at ~87% in 2024 and is *falling* as custom silicon grows — the concentration is easing at the top even as the market grows past $200bn. The HHI uses the midpoint (~75%): 75² + 8² + 7² + tail ≈ 5,750. On a 73% share the figure is ~5,450; on 81% it is ~6,650. **Highly concentrated by any standard.** Source for the shares: Silicon Analysts / International Data Corporation estimates via trade press (August–November 2026); NVIDIA's own filings for its revenue ($193.7bn data-centre revenue, fiscal year 2026 — A4).
- **Parameter mapping:** A4 (NVIDIA concentration and single-supplier fragility), F2 (market-structure consolidation).

**γ₂ — Cloud concentration (HHI for cloud infrastructure services).**
- **Today: HHI ≈ 1,360 (my calculation from Synergy Research Group's published shares).** Third quarter 2026: Amazon Web Services 26%, Microsoft Azure 19%, Google Cloud 16%, Oracle 4%, Alibaba Cloud 4%, long tail (~31% spread across many small providers). 26² + 19² + 16² + 4² + 4² + tail ≈ 1,361. **Below the highly-concentrated threshold on either guideline vintage** — the cloud layer is moderately concentrated, not highly. The top three hold 61% of a $168bn quarterly market, but no single firm dominates, and the leader's share is *falling* (Amazon Web Services 29% → 26% year-on-year) while the third player grows fastest (Google Cloud +103% year-on-year in the third quarter of 2026).
- **The correction:** concentration is severe at the silicon layer and moderate at the cloud layer. A single γ would hide this. The shakeout-volatility story differs by layer: the accelerator layer's risk is single-supplier fragility (A4); the cloud layer's risk is margin compression for middleware wrappers and governance lock-in, not monopoly pricing.
- **Parameter mapping:** F2 (consolidation), A1 (hyperscaler capital expenditure — the spending that *sustains* the concentration).

**γ₃ — Lock-in (qualitative; no number yet).** Switching costs, proprietary application programming interfaces, data gravity, and the governance dependency: 52% of banks and insurers name hyperscalers as their preferred partner to govern multi-agent deployments — "cloud is becoming the governance layer, not just the hosting layer" (Capgemini, ●●○○ Reported). No quantitative lock-in measure exists. **Proposed indicators:** egress-fee levels and trends; multi-cloud adoption rates; the share of enterprise AI workloads running on proprietary vs portable frameworks. **Open question Q18 (§II.12):** which lock-in indicator is measurable from public sources?

**What γ governs.** Shakeout volatility: high γ means the shakeout, when it comes, concentrates on few firms (and the failure of one is systemic); falling γ means the shakeout spreads. γ is the only knob currently moving in the de-concentrating direction (NVIDIA's share falling, cloud shares converging) — a genuine counter-signal to the frenzy reading, and the tracker records it as such rather than burying it.

#### II.5.4 Delta: Institutional Absorption Half-Life

**Definition.** δ is the time required for the adoption-governance gap to halve. Pick a gap metric G(t) — for example, the Boston Consulting Group (BCG) permission-minus-monitoring gap (73% − 8% = 65 points) or the ACA/NSCP use-minus-testing gap (86% − 38% = 48 points). δ is the time for G to fall to G/2, assuming exponential convergence. δ governs the *width* of the J-curve dip and sets the floor on the full cycle length: the cycle to deployment cannot complete faster than the institutions can absorb the technology, however fast the technical half moves.

**Today's value: cannot be estimated.** Every gap metric is a single point — no survey has yet repeated the same governance question twice. The first δ estimate becomes possible when the ACA/NSCP 2027 survey or the BCG 2027 banking survey repeats the governance questions. **This is the model's largest measurement hole, and it is stated as such rather than papered over with a guessed number.**

**What can be said without a number.**
- **Lower bound from the regulatory calendar.** The institutional framework cannot settle before ~2028 at the earliest: European Union AI Act high-risk obligations in force with enforcement (December 2027); Office of the Superintendent of Financial Institutions (Canada) Guideline E-23 effective (1 May 2027); Monetary Authority of Singapore Guidelines §§5–6 by 7 October 2028; the United States federal gap still open with no published request for information (D2). So δ ≳ 2 years from now on the regulatory component alone.
- **The behavioural component lags the regulatory component.** Firms adopt controls years after rules settle (Perez's mismatch resolves through recomposition *plus* diffusion). The report's 122 articles contain no narrowing signal for any governance gap — weak evidence, but the only evidence, that δ is long.
- **Working assumption (labelled as such, not a measurement): δ ≈ 3–5 years — revised by the backtest to the optimistic end of the range.** If δ is in this range, the full cycle to synergy is 10–20+ years (§II.6). If δ turns out to be 2 years or less, the compressed-cycle case revives — which is why measuring δ is the tracker's highest-priority research item. The backtest (§II.10.9) adds: the historical δ proxies run 10–40 years to the regulatory framework (railways ~10–14 years, dynamo ~15–30 years, automobiles ~40 years), so the 3–5 year assumption is shorter than every historical case. The working assumption stands as the optimistic end, not the centre, pending the first measured δ.
- **Parameter mapping:** C1–C7 (the gaps δ measures), D1–D3 (the regulatory component of absorption), B1–B3 (the adoption side of the gap — the numerator that δ must catch up with).

**Proposed sources going forward.** ACA/NSCP annual survey (repeat the testing question — the single most valuable repeat in the tracker's data plan); BCG annual banking survey (repeat the monitoring question); the report's own watch to track gap metrics as series (requires feature F-02's dated-value storage — the database that stores dated values, which is what makes re-measurement automatic). **Open question Q17 (§II.12):** is exponential convergence the right functional form for δ, or does absorption proceed in steps (regulation lands, then a rush of adoption)? The tracker's provisional answer: exponential is a placeholder; the first two data points will discriminate.

---

### II.6 The Velocity Calibration: Two Speeds, One Cycle

*Substantiates T2 and T3.*

The Parametric Adoption & Margin Curve normalizes time into Cycle Progress (0% to 100%), governed by a Velocity Multiplier. This section calibrates that multiplier against the evidence — and corrects the compressed-cycle claim.

#### II.6.1 The Two Velocities

The evidence supports two different velocities, not one:

| Half of the cycle | What moves | Speed | Evidence |
|---|---|---|---|
| **Technical diffusion** | Adoption, capability, usage | Compressed — order of magnitude faster than physical-era baselines | ChatGPT: 100 million monthly active users in ~2 months (UBS / Similarweb, via Reuters, February 2023); 1 million users in 5 days. TikTok took 9 months and Instagram 2.5 years to reach 100 million users (same UBS note). ACA/NSCP: 45% → 71% → 86% of US financial firms in 2 years (B1). JetBrains: ~47% of code AI-written within ~4 years of the big-bang (B2). METR (the independent model-evaluation organisation): ~7-month doubling of the 50%-reliability task horizon (B4). |
| **Institutional absorption** | Governance, liability, regulation, workforce change | Not compressed — human speed, possibly slower than the physical-era baseline | The US federal gap is still open 4 years in (D2). Every governance gap is a single point with no measured narrowing (C1–C7). Liability is asserted but untested in court (D3). δ cannot yet be estimated (§II.5.4). |

**The Velocity Multiplier, defined.** v = (time for the baseline technology to reach X% adoption) / (time for created intelligence to reach X% adoption), where X is a stated threshold in a stated population. For technical adoption with X = majority use among US financial firms: the baseline (personal computers in the enterprise, 1980s–1990s) took roughly a decade to reach majority; created intelligence took ~4 years — **v ≈ 2–3× on that comparison**. For consumer adoption with X = 100 million users: ChatGPT took ~2 months against TikTok's 9 months and Instagram's 2.5 years — **v ≈ 4–15× against the fastest previous consumer applications**, and far more against physical-era technologies. The multiplier is threshold- and population-dependent; the tracker states the comparison every time it uses a number, and never quotes a bare "v = 10×".

**The historical comparison — with its caveat.** The widely cited "years to 50 million users" figures — telephone 75 years, radio 38, television 13, personal computer 16, internet under 4 (Morgan Stanley, 1997, via European Broadcasting Union Technical Review, 2000) — illustrate the order-of-magnitude acceleration. But Hannemyr (2003) showed the figures mix United States households with worldwide users, are not like-for-like, and rest on shaky sourcing (the radio figure in particular is contested). The tracker uses them as *illustration only*, never as calibration inputs. The calibration rests on the report's own adoption series and the UBS/Similarweb ChatGPT figures, not on the folklore numbers.

**The payoff lag — the other side of the velocity story.** The dynamo took ~40 years from the first power stations to majority factory electrification (David 1989/1990). The computer took ~25 years from commercialisation to the productivity resurgence (Crafts 2019). These are the *payoff* lags, and they are the relevant baseline for Line B (Net Enterprise Profit-and-Loss Capture), not for adoption. Created intelligence is 4 years post-big-bang. Against those precedents, the productivity payoff should be expected years away — if it comes at all.

#### II.6.2 The Compressed-Cycle Claim, Assessed

**The prior claim:** a Created Intelligence compressed curve of 6–10 years, against a Railroad/Personal-Computer baseline of 30–40 years.

**The assessment, in parts:**
- **For the technical-diffusion half (adoption to majority): the claim is supported.** Majority adoption among US financial firms took ~4 years (B1); majority-AI code production took ~4 years (B2); consumer adoption took months. A 6–10 year technical cycle is, if anything, conservative for the adoption half.
- **For the full cycle (to deployment/synergy): the claim is not evidenced.** The full cycle's duration is set by the slower half — institutional absorption — and δ is unmeasured but bounded below by the observed 4+ years with no narrowing (§II.5.4). With δ ≈ 3–5 years (working assumption), the full cycle is **10–20+ years**: technical diffusion (~4–6 years) plus several half-lives of absorption. A 6–10 year full cycle would require δ ≈ 2 years or less, which nothing in the evidence supports. The backtest (§II.10.9) adds a caution in the other direction: the historical δ proxies (10–40 years to the regulatory framework) suggest even 10–20+ years may be optimistic — the working assumption is the optimistic end of the range, not the centre.
- **The Railroad/Personal-Computer baseline (30–40 years) is roughly right for the full cycle** of a physical-era surge's installation period (Perez's installation is 20–30 years; the dynamo's payoff lag was ~40 years). But the baseline conflates two different things — installation length and payoff lag — and the tracker should separate them in the curve's annotation.
- **What would change the assessment:** a measured δ (the first repeat survey round — ACA/NSCP 2027 or BCG 2027). If the governance gaps are narrowing fast, the compressed-cycle case revives. If they are flat or widening, the 10–20+ year range firms up. Until then, the compressed full cycle is a hypothesis, and the curve draws its right half dashed (§II.11.3).

**The model's central finding on velocity.** The cycle is not uniformly compressed. It is *stretched at the institutional end and compressed at the technical end* — which is precisely why the mismatch (Group C) is the largest it has ever been measured. The velocity story and the mismatch story are the same story.

---
### II.7 The Parameters: 30, with Heat Status

*Substantiates T4, T5, T6, and T8.*

Every parameter carries: what it measures, its current value, its source and date, a quality note, its **phase reading**, and its **heat status** — the status the heatmap (§II.11) shows. Report figures carry the report's own confidence ratings (●●●● Established / ●●●○ Corroborated / ●●○○ Reported / ●○○○ Claimed). External figures carry their source's own standing (official statistics > peer-reviewed research > vendor surveys > analyst estimates). Estimates are labelled as estimates. Where no data exists, the parameter says so.

**Heat-status definitions** (the mapping from phase reading to heat status is mechanical — see §II.11.1):
- **In place** (blue): the condition this parameter measures is met at a level consistent with deployment (synergy). Phase reading synergy/maturity.
- **Getting there** (amber): the condition is moving toward deployment levels but not yet met, or the precondition is met but the substance is not. Phase reading turning point / turning-point precondition.
- **Lagging** (rust): the condition is far from deployment levels, or actively points the other way. Phase reading frenzy / irruption.
- **Unclear** (grey): the parameter's reading is ambiguous, or the parameter measures disagreement rather than a state.

**Today's tally: 23 lagging, 5 getting there, 0 in place, 2 unclear.** The empty "in place" column is the heatmap's most important feature.

#### A. Finance and investment — the frenzy markers

| # | Parameter | Current value | Source (date) | Quality | Phase reading | Heat |
|---|---|---|---|---|---|---|
| A1 | Hyperscaler capital expenditure, big four (Amazon, Alphabet, Microsoft, Meta), cash property, plant and equipment | **$376.1bn in 2025** (vs ~$251bn in 2024, +66%); **guidance $720–745bn for 2026** | Securities and Exchange Commission filings via valueaddvc tracker, Platformonomics, CRE42 (2025 actuals; guidance as of Oct 2026) | Official filings via trackers; methodology varies (including finance leases: $411–416bn for 2025). Tracker uses the cash property, plant and equipment basis and states it. | **Frenzy** — infrastructure mania; the 2026 guided annual rate alone exceeds the inflation-adjusted cost of the Interstate Highway System ($729bn, 1956–1992, per CRE42) | Lagging |
| A2 | Data-centre investment pipeline (US) | Planned domestic data-centre construction **~$300bn (2024) → >$1tn in announced pipelines (2025)**; baseline annual investment **$100bn (2024) → >$880bn by end-2027, exceeding 2.0% of US gross domestic product** | Finance and Economics Discussion Series (FEDS) 2026-074, Carollo et al. (12 Nov 2026), Brandsaas et al. (2025) project-forecasting method | Federal Reserve staff working paper (authors' views, not the Board's). Path depends on assumed abandonment rates and build times. ~Half the equipment content is imported, which offsets the gross domestic product effect. | **Frenzy** — the build-out is the mania made concrete | Lagging |
| A3 | AI share of venture funding | **$243.9bn global AI venture capital in 2025, >50% of global venture capital deal value for the first time** (52.5% through Q3 on $192.7bn of $366.8bn; 62.7% of US venture capital in Q3). 2024: $131.5bn (PitchBook) | PitchBook (full-year 2025) | Provider totals vary (Crunchbase ~$100bn for 2024; BestBrokers $270.2bn for 2025). PitchBook is the primary source cited. Concentration: 24 US AI startups raised $100M+ rounds in 2025 (~$65bn, >60% of all AI funding). Meanwhile the venture-capital base is shrinking: 823 funds raised ~$80bn globally in 2025 vs 4,430 funds raising $412bn in 2022. | **Frenzy** — finance flooding the new paradigm, concentrating in fewer, larger bets | Lagging |
| A4 | Picks-and-shovels concentration (NVIDIA) | First **$5tn market capitalisation, 29 Oct 2025** (closed ~$5.03tn); fiscal year 2026 revenue **$215.9bn, +65% year-on-year**, data-centre **$193.7bn, ~90% of total**; revenue 8× in three fiscal years ($27bn fiscal year 2023 → $216bn fiscal year 2026); net income $120.1bn (55.6% margin). AI accelerator revenue share ~73–81% in 2026, down from ~87% peak in 2024 (Silicon Analysts / International Data Corporation estimates; no audited share table exists) | NVIDIA 10-K (filed 25 Feb 2026); Associated Press / CNBC (market capitalisation); Silicon Analysts / International Data Corporation (share estimates, August–November 2026) | Audited filings for revenue; market-capitalisation milestones from press. Peaked ~$5.78tn (6 Oct 2026). Share estimates are methodology-dependent (whether hyperscaler custom silicon is counted). | **Frenzy** — and a single-supplier bottleneck, which is a fragility signal | Lagging |
| A5 | Capital-expenditure-vs-revenue gap | **~$600bn/yr in end-user AI revenue** would be needed to justify the infrastructure spend (Sequoia, Jun 2024, on NVIDIA's data-centre run-rate + standard cloud economics). Against that: OpenAI + Anthropic + DeepMind lower-bound revenue **≥$107bn in 2026Q3**, ~19% of software gross output (FEDS 2026-074, via nosov.ai summary of the full text); neither lab consistently profitable; inference gross margins ~30–40% | Sequoia Capital, David Cahn, "AI's $600B Question" (20 Jun 2024); FEDS 2026-074 | Cahn's figure is a revenue requirement implied by assumptions, not a measured loss. Lab revenue figures are unaudited company statements; margins vary by calculation (Anthropic also claimed 80%). FEDS figures used via a careful secondary summary — confirm against the PDF before publication. | **Frenzy** — paper wealth ahead of real returns (Perez's tension #1) | Lagging |
| A6 | Cash-flow stress at the builders | Amazon trailing-twelve-months free cash flow **−$42.4bn**; Meta Q3 2026 free cash flow **−$2.12bn**; Oracle Q1 fiscal year 2027 free cash flow **−$5.4bn**; hyperscalers raised **$108bn in debt during 2025** | Kurums (Oct 2026, from filings); Ralph Capital Research (debt figure — second-hand, indicative) | Second-hand figures; treat as indicative. FEDS 2026-074 notes a shift by hyperscalers to debt financing and widening bond spreads at Oracle (via nosov.ai summary). | **Late frenzy** — the build-out is increasingly debt-funded | Lagging |

#### B. Diffusion — how far the paradigm has spread

| # | Parameter | Current value | Source (date) | Quality | Phase reading | Heat |
|---|---|---|---|---|---|---|
| B1 | US financial-firm AI use | **86%** formally use AI; series **45% (2024) → 71% (2025) → 86% (2026)** | ACA/NSCP 2026 AI Benchmarking Survey (12 Nov 2026), 261 firms | ●●○○ Reported. 2024/2025 values derived from the release's stated deltas. | **Turning-point precondition** — the paradigm is accepted as common sense | Getting there |
| B2 | AI-written code share | **~47%** of code written fully by AI agents (~15,000 developers); **42%** of committed code AI-generated or assisted, **65% expected by 2027** | JetBrains Developer Ecosystem Survey 2026; Sonar State of Code 2026 | ●●●○ Corroborated (both). The 65% is an expectation, not a measurement. | **Turning-point precondition** — majority-AI production | Getting there |
| B3 | Agent deployment: breadth vs depth | **79%** of enterprises run agents in production; **99%** of organisations have adopted agents (Palo Alto Networks, n=2,930) — but only **10%** have achieved enterprise-wide orchestration and only **5%** have institutionalised enterprise-scale agentic capability (Capgemini); only **2%** of United Kingdom firms allow broad autonomy (Bank of England / Financial Conduct Authority); **1 in 4** US financial firms experimenting with agentic AI (ACA/NSCP) | SailPoint (Oct 2026); Palo Alto Networks (20 May 2026); Capgemini (5 Nov 2026); Bank of England / Financial Conduct Authority (26 Oct 2026); ACA/NSCP (12 Nov 2026) | ●●○○ Reported (SailPoint, Capgemini, ACA/NSCP); ●●●○ Corroborated (Palo Alto Networks, Bank of England / Financial Conduct Authority). FEDS 2026-074: only **10%** of the surveyed US workforce uses AI daily; firm adoption estimates range from ~20% (Census Bureau Business Trends and Outlook Survey) to 58–78% in other surveys, depending on wording and sample. | **Frenzy** — broad but shallow | Lagging |
| B4 | Capability trajectory | **~7-month doubling** of the 50%-reliability task horizon (METR, the independent model-evaluation organisation); **~1.9×** capability-improvement rate since Oct 2025 vs Mar 2024–Oct 2025 (METR, 11 weeks inside Anthropic; majority ~80% attributed to AI doing research and development, "substantial uncertainty") | METR time horizons (2026); METR/Anthropic study (5 Nov 2026) | ●●●○ Corroborated (time horizons — but the public tracker is frozen as of 8 Sep 2026, and measurements above 16h flagged unreliable). The 1.9× figure is the report's §3.6 prose with no dots rating. | **Irruption/frenzy** — technology still accelerating | Lagging |

#### C. Institutional mismatch — the adoption/governance gap (the report's strongest evidence)

| # | Parameter | Current value | Source (date) | Quality | Phase reading | Heat |
|---|---|---|---|---|---|---|
| C1 | Policy vs practice | **98%** of large companies have AI governance policies; **47%** have bypassed them; **49%** of policies not updated for agentic risk | EY US AI Risk and Governance Survey 2026 (202 decision-makers, ≥$1B revenue, ±7 pts) | ●●○○ Reported | **Frenzy — mismatch** | Lagging |
| C2 | Permission vs monitoring | **73%** of systemically important banks permit agents in production for select use cases; **8%** have comprehensive agent monitoring and controls | Boston Consulting Group AI Safety and Governance in Banking 2026 (13 Nov 2026, 26 banks) | ●●○○ Reported. None permits broad production use; at 88% of banks agents are ≤10% of the AI portfolio. | **Frenzy — mismatch** | Lagging |
| C3 | Deployment vs identity tools | **79%** run agents in production; **2%** have the identity tools to govern them; **54%** at the lowest maturity tier for agent identity. Machine-to-human identity ratio **109:1** (79 of 109 are AI agents) | SailPoint Horizons of Identity Security (Oct 2026); Palo Alto Networks 2026 Identity Security Landscape (20 May 2026) | ●●○○ Reported (SailPoint); ●●●○ Corroborated (Palo Alto Networks). The 109:1 series is weak: 2 points from different samples (82:1 is CyberArk's April 2025 edition, n=2,600; 109:1 is Palo Alto Networks' 2026 edition, n=2,930). | **Frenzy — mismatch** | Lagging |
| C4 | Control: can firms stop an agent? | **35%** not confident they could shut down a rogue agent; **36%** no formal supervision plan; **30%** have a formally deployed, documented kill switch; 23% of firms with agents in production never tested their kill switch. Financial Conduct Authority-documented: AI code passed human review and caused a loss of service; kill switches insufficiently tested; no list of authorised operators | Writer / Workplace Intelligence (2026, 2,400 employees & C-suite); Financial Conduct Authority Wholesale Banks Supervision Insights 3 (2 Nov 2026) | ●●○○ Reported (Writer); **●●●● Established** (Financial Conduct Authority — supervisory findings) | **Frenzy — mismatch** | Lagging |
| C5 | Testing and oversight | Only **38%** of US financial firms have a formal program to test/validate AI outputs; no single technical control used by >36% of firms; only **18%** have an AI incident response plan; only 51% confident they could produce oversight documentation on short notice | ACA/NSCP 2026 (12 Nov 2026) | ●●○○ Reported | **Frenzy — mismatch** | Lagging |
| C6 | Shadow AI | **79%** of information-technology leaders encountered unauthorised AI deployments; **82%** discovered at least one agent information technology didn't know about in the past year; ~half of agents run without security oversight/logging; 66% of office professionals admit using AI tools they believe aren't permitted | Nutanix Enterprise Cloud Index 2026; Cloud Security Alliance / Token Security; PagerDuty 2026; Verizon Data Breach Investigations Report 2026 | ●●○○ Reported | **Frenzy — mismatch** | Lagging |
| C7 | Failure counts (the cost of the mismatch) | **188** documented cases of autonomous AI damaging production systems, no attacker involved (late 2023–mid-2026); **46%** of systemically important banks reported an AI-related issue/incident in the past 12 months; AI-code flaw rate **~38%** (series 45→44→38%, first movement); AI patches carry **~11×** the vulnerabilities of developer patches (135 vs 12, confirmed); 74 Common Vulnerabilities and Exposures traced directly to AI coding tools | Cyera analysis of 7,000+ public AI incidents; Boston Consulting Group 2026; Veracode Fall 2026; Sajadi et al. (1 Nov 2026); Georgia Tech Vibe Security Radar | ●●○○ Reported (Cyera, Boston Consulting Group, Sajadi, Georgia Tech); ●●●○ Corroborated (Veracode). **Counts have no exposure denominator** — no incident *rate* per deployment exists, and Cyera's count "almost certainly undercounts." | **Frenzy — mismatch** | Lagging |

**Group C verdict:** the most densely measured phenomenon in the report's evidence base, and the tracker's strongest parameter group. The report's own summary judgment: "Adoption has run ahead of governance on every measure that matters." That sentence *is* Perez's institutional mismatch, stated in the report's own words.

#### D. Regulatory recomposition — the turning-point markers

| # | Parameter | Current value | Source (date) | Quality | Phase reading | Heat |
|---|---|---|---|---|---|---|
| D1 | Milestone density (regulation arriving) | European Union AI Act general-purpose AI enforcement powers in force (2 Aug 2026) + first enforcement: formal information requests to OpenAI and Anthropic (14 Oct 2026; second round 6 Nov). New York Responsible AI Safety and Education (RAISE) Act registration due (1 Jan 2027). Third-party risk management (TPRM) guidance comments close (16 Dec 2026). Financial Conduct Authority Consultation Paper 26/38 comments close (24 Dec 2026). Office of the Superintendent of Financial Institutions (Canada) Guideline E-23 takes effect (1 May 2027). Monetary Authority of Singapore Guidelines §§3–4 apply (7 Oct 2027), §§5–6 by 7 Oct 2028. Hong Kong Monetary Authority Project SAGE comments due (1 Feb 2027). California kill-switch recommendations released (18 Nov 2026); legislature returns 7 Dec 2026. Office of the Comptroller of the Currency Bulletin 2026-54 examiner framework (4 Nov 2026). Conference of State Bank Supervisors AI Supervisory Framework (16 Sep 2026). | Report's dashboard deadlines + §3.4.2 articles | ●●●● Established (Conference of State Bank Supervisors, Monetary Authority of Singapore, Hong Kong Monetary Authority, Office of the Comptroller of the Currency, Financial Conduct Authority Mills Review, Financial Industry Regulatory Authority) / ●●●○ Corroborated (European Union AI Office enforcement, United Kingdom Competition and Markets Authority / Digital Regulation Cooperation Forum) — ratings vary by item; see evidence mapping. | **Turning point — process under way** | Getting there |
| D2 | The US federal gap | Supervision and Regulation Letter 26-2 (17 Apr 2026) replaces Supervision and Regulation Letter 11-7; generative and agentic AI **expressly out of model-risk scope** (Footnote 3). Federal Reserve / Office of the Comptroller of the Currency / Federal Deposit Insurance Corporation AI request for information promised Apr 2026, **still unpublished as of 21 Nov 2026**. | Federal Reserve / Office of the Comptroller of the Currency / Federal Deposit Insurance Corporation Supervision and Regulation Letter 26-2; report §1.5.2/§2.5 | **●●●● Established** (Supervision and Regulation Letter 26-2) | **Turning point — incomplete** | Lagging |
| D3 | Liability crystallising | United Kingdom Competition and Markets Authority / Digital Regulation Cooperation Forum: "an agent's autonomy does not diminish the deployer's responsibility" — fines up to 10% of worldwide turnover (30 Oct 2026). US banks writing agent liability into customer terms (Citi, PNC, Citizens, Wells Fargo effective 24 Nov 2026), **untested against Regulation E**. California Attorney General sues OpenAI (16 Nov 2026; $2,500/violation sought; allegations unproven). Arizona Attorney General opens criminal investigation (19 Nov 2026; first criminal action; no charges filed). | United Kingdom Competition and Markets Authority / Digital Regulation Cooperation Forum; report §3.4.2 articles | ●●●○ Corroborated (Competition and Markets Authority / Digital Regulation Cooperation Forum, bank terms); ●●●● Established as filed actions (California Attorney General suit, Arizona investigation) | **Turning point — early markers** | Getting there |

**Group D verdict:** turning-point markers are appearing — the recomposition process has begun — but the framework is unsettled. This is "turning point as process" (Perez: "neither an event nor a phase; it is a process of contextual change"), and the process is early.

#### E. Productivity and returns — the Solow measurement

| # | Parameter | Current value | Source (date) | Quality | Phase reading | Heat |
|---|---|---|---|---|---|---|
| E1 | Aggregate labour productivity vs trend | Bureau of Labor Statistics nonfarm business: **+3.0% (2024), +2.1% (2025)**; current cycle (Q4 2019–) **2.1%/yr** vs 1.5% previous cycle, 2.2% long-run since 1947. Q3 2026: +3.6% annualised, +2.1% year-on-year. | Bureau of Labor Statistics, *Productivity and Costs* (5 Mar 2026; revised 24 Mar 2026; United States Department of Labor release USDL 26-0558); Q3 2026 release (5 Nov 2026) | Official statistics. **Revision risk is live:** Q4 2025 was revised from +2.8% to +1.8% between the 5 Mar and 24 Mar 2026 releases; Bureau of Labor Statistics corrected 2019–2023 hours data in Apr 2024 (moving the 2023 annual figure from +1.3% to +2.3% in the current vintage). | **Ambiguous — at trend, not above it** | Unclear |
| E2 | Total factor productivity (the residual) | Bureau of Labor Statistics private nonfarm business TFP: **+1.5% (2024) → +0.8% (2025)**; 2019–2025 **+1.0%/yr**. Decomposition of 2025's 2.2% labour-productivity growth: TFP 0.8pp + capital intensity 0.9pp + labour composition 0.4pp. | Bureau of Labor Statistics TFP release (19 Mar 2026) | Official statistics. One year proves nothing either way — but the *direction* matters: the residual fell as AI investment exploded. | **Installation — the paradox persists in the residual** | Lagging |
| E3 | FEDS 2026-074 — the official verdict | "The effects of AI on aggregate productivity growth **also appear to be small so far**, and the recent pickup in productivity likely reflects factors that predated the diffusion of generative AI." Labour-market effects "small and somewhat mixed." | Carollo, Crane, Garcia Molina & Nichols, "Artificial Intelligence and the U.S. Economy: Current Evidence," FEDS 2026-074 (12 Nov 2026), abstract — **verified directly against federalreserve.gov**. Digital object identifier (DOI) 10.17016/FEDS.2026.074. Federal Reserve Vice Chair Jefferson's keynote (13 Nov 2026) explicitly invoked Solow's 1987 paradox for the generative-AI era. | Federal Reserve staff working paper — authors' views, not the Board's; analysis mostly completed June 2026. The paper's own words are "small so far" — the "negligible measurable impact" phrasing in some coverage is a secondary paraphrase, not the paper's wording. | **Installation — no aggregate payoff yet** | Lagging |
| E4 | The micro-macro gap | Task-level gains **14–56%** (IMF 2026 range) vs macro estimates **0.2–1.3pp/yr** (OECD) vs "small so far" (FEDS). Micro: Copilot randomised controlled trial (RCT) **+55.8% faster** (Peng et al. 2023, 95 freelancers, narrow greenfield task, vendor-affiliated); Cui et al. **+26.08% tasks/week** (4,867 developers, 3 RCTs, *Management Science*, 27 Feb 2026); Brynjolfsson, Li & Raymond **+14% in month 1, +25% after 3 months** (customer support); METR **19% slower with AI allowed** (16 experienced developers, 246 real issues in mature repos, Jul 2025; developers predicted 24% faster and believed afterwards they had been 20% faster); METR follow-up (Feb 2026): 4–18% point estimates, confidence intervals include zero. | IMF (2026); OECD (2024/2025); Peng et al. arXiv:2302.06590; Cui et al. (2026); Brynjolfsson et al. (2023); METR (2025, 2026) | Peer-reviewed and randomised-controlled-trial evidence, but task- and context-dependent; the METR perception-vs-measurement gap (developers believed +20% faster while measuring −19%) is itself a finding. | **Installation — the gap is the parameter** | Lagging |
| E5 | Firm-level returns | MIT NANDA: **95% of organisations reported zero measurable profit-and-loss return** from generative AI (Jul 2025). Capgemini: **~50%** of financial institutions cannot consistently demonstrate a return on agentic AI initiatives. Boston Consulting Group: **>25%** of systemically important banks say AI systems were falling behind their promised business case. Atlanta Federal Reserve Bank / Richmond Federal Reserve Bank / Duke University chief financial officer survey (~734 executives): **>80%** of firms reported no impact on employment or productivity over the previous three years; ~90% of executives say AI has not yet produced meaningful productivity gains. | MIT NANDA, "The GenAI Divide" (Jul 2025); Capgemini (5 Nov 2026); Boston Consulting Group (13 Nov 2026); Baslandze et al., Federal Reserve Bank of Atlanta Working Paper 2026-4 (Mar 2026, revised May 2026) | MIT NANDA is preliminary, non-peer-reviewed, small sample (300+ initiatives, 52 interviews, 153 surveys) — quote with the caveats; widely misquoted as "95% of pilots fail" — the figure is about measurable profit-and-loss impact, not whether software shipped. Capgemini / Boston Consulting Group ●●○○ Reported. Atlanta Federal Reserve Bank working paper is the strongest source in this row. | **Installation — returns undemonstrated at scale** | Lagging |
| E6 | The verification tax (the report's own paradox finding) | DORA: 2024 — **−1.5% throughput, −7.2% delivery stability** per +25% AI adoption (correlational survey); 2025 — adoption now correlates with higher throughput, stability still lower; 2026 — **time saved generating is re-spent auditing**. GitClear: **+81% duplicate code blocks; two-week churn +15%; refactoring 21% → 3.8% of changed lines** (623M code changes). | Google DORA, *The ROI of AI-Assisted Software Development* (2026.01; ROI = return on investment) and DORA 2024–2026; GitClear, "The Maintainability Gap" (Jan 2026) | ●●●○ Corroborated (DORA); ●●○○ Reported (GitClear). DORA's 2024 figures are correlational, not causal. | **Installation — the micro-mechanism of the paradox** | Lagging |
| E7 | Forecast spread (meta-parameter) | Acemoglu **≤0.66% TFP over 10 years** (upper bound) vs Aghion & Bunel **0.68pp/yr** (6.8% cumulative) vs Goldman Sachs **~7% higher annual global GDP over 10 years** vs OECD **0.2–1.3pp/yr**. The spread is driven almost entirely by two assumptions: the share of tasks AI affects, and the cost savings per task. | Acemoglu (2024/2025); Aghion & Bunel (2024); Goldman Sachs (Mar 2023); OECD (2024/2025) | All estimates, not measurements. The MIT Stone Center comparison tool shows the three frameworks side by side. | **Uncertainty — the disagreement width is the parameter** | Unclear |

**Group E verdict:** the paradox is intact. Labour productivity runs at trend, TFP fell in 2025, the Federal Reserve's own paper says AI's aggregate productivity effects "appear to be small so far," firm-level returns are undemonstrated at scale, and the report's own evidence shows the gains being re-spent on verification and cleanup. No deployment-period productivity signature exists.

#### F. Inequality and structure

| # | Parameter | Current value | Source (date) | Quality | Phase reading | Heat |
|---|---|---|---|---|---|---|
| F1 | Top-0.1% income share | **10.1% of all adjusted gross income**, tax year 2023 (153,076 returns; threshold $3,100,950). Perez's marker (Perez 2007, Fig. 5, via Piketty & Saez 2003): **>10%** of declared income during the 1920s and 1990s bubbles, falling to **~6%** in deployment. | Internal Revenue Service Statistics of Income, Publication 1304, Table 4.1 (March 2026), via Walnut compilation | **Indicative comparison, not the same series:** Piketty-Saez "declared income" vs Internal Revenue Service adjusted gross income share differ in construction. Latest Internal Revenue Service year published is 2023. Supporting (wealth, not income): top 1% wealth share **31.7%** in Q3 2025 (Federal Reserve data, via advisorstream) — the highest since the Second World War; top 0.1% wealth +40% in three years. | **Frenzy** — at the bubble level on Perez's only quantified marker | Lagging |
| F2 | Market structure / consolidation | Framework consolidation: "by late 2026 the multi-agent field has consolidated around a handful of frameworks" (LangGraph, Microsoft Agent Framework, Strands, Google Agent Development Kit, OpenAI Agents SDK). **52%** of banks/insurers name hyperscalers as preferred partner to govern multi-agent deployments — "cloud is becoming the governance layer." Cloud concentration: Herfindahl-Hirschman Index ≈ 1,360 (Q3 2026, Synergy Research Group shares — see §II.5.3). | Report §3 intro + §3.1 table (prose, unrated, as of 9 Nov 2026); Capgemini (5 Nov 2026); Synergy Research Group (Q3 2026) | Prose (unrated) + ●●○○ Reported (Capgemini). Thin data — the report has no market-share, revenue, or concentration figures of its own; the cloud index is computed from Synergy's published shares. | **Late frenzy / turning point** — consolidation toward oligopoly | Getting there |
| F3 | Labour-market early signals | Workers aged 22–25 in AI-exposed occupations saw a **16% relative employment decline** (Automatic Data Processing-based study cited in FEDS 2026-074), driven by reduced hiring. Software developer postings on Indeed remain **~20% below pre-pandemic**. Surveyed executives expect a **1.2% employment reduction** and a 2.3% productivity gain at their firms over three years. | FEDS 2026-074 (via nosov.ai summary of the full text) | Via secondary summary — confirm against the PDF before publication. Findings "may mix AI effects with post-pandemic overhiring and interest rates." The report itself has **no jobs data of any kind** (verified by grep). | **Frenzy** — early displacement in exposed entry-level roles | Lagging |

#### Gaps — what the tracker cannot measure (yet)

From the evidence mapping, stated plainly (carried from v1, updated):

1. **Investment flows inside the report:** the report has no venture-capital funding, capital-expenditure, data-centre/infrastructure build-out, chip supply, or energy consumption figures. Group A comes entirely from outside the report (Securities and Exchange Commission filings, PitchBook, FEDS). Methodology varies by provider (see A1/A3 caveats).
2. **Profitability / return on investment:** explicitly "Insufficient data" in the report; no credible dollar figure for money saved or lost; no hours-or-dollars net figure. The money panel's bignote: "No credible dollar figure exists yet."
3. **Employment effects:** no jobs, layoffs, headcount, hiring, or wage data of any kind in the report. F3 comes from FEDS via secondary summary.
4. **Market structure:** no market size, market share, vendor revenue, concentration ratios, or funding rounds in the report; only one spend total (Menlo Ventures $176.8B enterprise AI deployment spend by Sep 2026, up 5.4× in a year — spend, not profit) and subscription price lists. (γ's indices in §II.5.3 are computed from outside sources, not report data.)
5. **Macro productivity:** no gross domestic product, sector-productivity, or firm-level output statistics in the report — only the DORA survey correlations and the "verification tax" framing. Group E comes from the Bureau of Labor Statistics / Federal Reserve Economic Data (FRED) / FEDS.
6. **Incident rates:** incident counts (188 Cyera, 63 Gravity) are counts of *reported* cases with no exposure denominator and acknowledged undercounting; no incident *rate* per deployment exists.
7. **Longitudinal depth:** only 4 time series exist in the report; one is closed (Google), one is 2 points from different samples (Palo Alto Networks), one spans only ~7 months (Veracode). No series predates 2024 except United Kingdom AI use (2022) and the Pearce 2022 base rate.
8. **Human baselines:** CI-VS-EI.md states "No human baseline published" for nearly every quality/reliability row — so most created-intelligence-vs-human comparisons the tracker might want cannot be made from this base.
9. **Consumer/retail adoption:** adoption figures are enterprise/finance/developer only; no consumer usage or end-user demand data in the report (FEDS 2026-074: ~50% of adults use AI outside work — via secondary summary).
10. **Geography:** US/United Kingdom-centric; European Union figures are regulatory, not adoption; no China/Asia adoption data beyond Hong Kong Securities and Futures Commission and Singapore/Monetary Authority of Singapore items.
11. **Verification costs outside code:** β exists only for code (§II.5.2). No verification-cost data for agentic workflows, legal, finance, or customer-facing AI.
12. **Governance time series:** no repeat measurement of any governance metric — δ cannot yet be estimated (§II.5.4).

---
### II.8 Assessment: The Verdict

*Substantiates T8 and T9.*

#### II.8.1 The Verdict Stands

The new apparatus does not change v1's verdict. It explains *why* it is true, and makes it visible at a glance.

**The outer hand (ICT surge, 1971–): extended turning point.** The surge's turning point is extended because its third leap (created intelligence) has re-energised installation dynamics inside a surge that was already in its turning point. Evidence: the 1990s frenzy was resolved in the 2000–2002 crash and the institutional framework that followed (Sarbanes-Oxley, internet governance), but the framework never fully recomposed around the digital paradigm, and the created-intelligence leap has re-opened the mismatch at a new scale.

**The inner hand (AI sub-cycle, November 2022–): late frenzy, turning point beginning.** Evidence: the tally. **Heat tally (all 30 parameters): 23 lagging, 5 getting there, 0 in place, 2 unclear.** (v1's phase tally for the 21 parameters with a Perez-phase reading was 16 frenzy / 5 turning point / 0 synergy; the heat tally counts all 30, mapping the E-group's "installation" readings to Lagging — the payoff has not arrived — which is why the lagging count is higher.) **Both vetoes hold:** Total Factor Productivity is flat/falling (E2: +0.8% in 2025, down from +1.5%), and the institutional framework is unsettled (Group C's gaps are unmeasured for narrowing; D2's federal gap is open; D3's liability is untested). **Under the judgment rule (§II.2.5), no deployment claim is permitted.**

**The one-line verdict:** the money and the machines are in frenzy; the institutions are at the turning point's door; the productivity payoff has not arrived.

#### II.8.2 What the New Apparatus Adds

1. **The mismatch is now explained, not just observed.** The two-velocity correction (§II.6) is the mechanism behind Group C: technical diffusion compressed (α_distribution ≈ 0.05–0.1) while institutional absorption stayed at human speed (δ unmeasured, bounded below at ~2 years). The mismatch is the *largest ever measured* precisely because the velocity gap is the largest ever.
2. **The J-curve dip now has a depth and a width.** Depth: β ≈ 2.5 in code (§II.5.2). Width: governed by δ, unmeasured (§II.5.4). The dip is deep and its width is unknown — which is why the tracker draws the curve's right half dashed.
3. **The next build-out is located.** The Infrastructure–Application Cycle (§II.4.3) places Infrastructure 2 — verification, deterministic guardrails, audit layers — as the emerging layer. It is Genesis → Custom-Built (Wardley panel, §II.11.2), and it is where the next investable wave sits. The tracker watches it; it does not yet size it.
4. **The component view exposes the risk.** The Wardley panel (§II.11.2) shows the dangerous configuration: deployment at Product scale (agents, coding assistants) resting on governance components at Custom-Built or Genesis (identity, guardrails, audit, liability). That is the mismatch at component level.
5. **The concentration picture is corrected.** γ (§II.5.3) shows severe concentration at the silicon layer (Herfindahl-Hirschman Index ≈ 5,750) and moderate concentration at the cloud layer (Herfindahl-Hirschman Index ≈ 1,360) — and the only knob moving in the de-concentrating direction. A single γ would have hidden this, and the tracker records the counter-signal rather than burying it.

#### II.8.3 What Would Change the Verdict

Per the judgment rule (§II.2.5), the verdict changes when the *evidence* changes, in one of three ways:

1. **The vetoes lift.** Total Factor Productivity exceeds ~1.5% sustained for two or more years *and* the institutional framework settles (the federal gap closes, liability is tested in court, governance gaps narrow measurably). This is the deployment bar (open question Q5, §II.12).
2. **δ is measured and short.** If the first repeat survey round (ACA/NSCP 2027 or BCG 2027) shows governance gaps narrowing fast (δ ≈ 2 years or less), the compressed-cycle case revives and the turning-point reading accelerates.
3. **β falls toward 1.** If verification automation (Infrastructure 2) brings the verification-to-generation cost ratio toward parity, the J-curve dip is bottoming and Line B (Net Enterprise Profit-and-Loss Capture) is turning up.

Until one of these happens, the verdict is: **late frenzy, turning point beginning — and the heatmap's empty "In place" column is the honest headline.**

---

### II.9 Uncertainty: What Could Be Wrong

*Qualifies T1–T12: states what could be wrong with every claim in Part I.*

Carried from v1 (§7), updated with the new apparatus's own uncertainties. This section is the model's honesty apparatus: it stays in the document, and it grows as the model grows.

1. **The framework is not testable.** Perez's theory has no falsifiable predictions at the parameter level. The tracker is a structured judgment, not a measurement instrument. The two-hand reading is an interpretation, and the document says so at every level.
2. **The evidence base is the report's base.** 122 articles, skewed to code and finance, United States/United Kingdom-centric, with no macro, employment, or market data of its own. Groups A, E, and F come from outside the report. The tracker's confidence in any parameter is bounded by its source's confidence.
3. **Single points dominate.** Most parameters are single points, not series. Direction of travel is unknown for the majority. The first repeat measurements (ACA/NSCP 2027, BCG 2027) are the most valuable data the tracker can acquire.
4. **The "turning point" reading rests on process, not outcome.** Group D shows the recomposition process beginning — but processes can stall, reverse, or be captured. The D-group reading is "turning point under way," not "turning point achieved."
5. **The two-hand reading could be wrong.** If created intelligence is a sixth surge (not a third leap), the outer hand's reading changes — the ICT surge would be in maturity/decline, and the AI surge would be in its own irruption/frenzy. The two-hand clock's outer hand would then be a *different* clock. This is open question Q1 (§II.12).
6. **The Acemoglu vs J-curve fork is unresolved.** The evidence cannot yet discriminate between "the J-curve dip is temporary" and "the gains are structurally small." The tracker's verdict (late frenzy, turning point beginning) holds under either fork — but the *implications* differ sharply (a deep dip that recovers vs a shallow ceiling). The fork is the single most consequential open question in the model.
7. **The F1 series mismatch.** The top-0.1% income share (10.1% of adjusted gross income, tax year 2023) is not the same series as Piketty-Saez "declared income" that Perez cites. The comparison is indicative. A like-for-like World Inequality Database / Piketty-Saez series pull is open question Q3 (§II.12).
8. **FEDS full-text figures need PDF confirmation.** The figures used from FEDS 2026-074's full text (A2's pipeline, A5's lab revenue, F3's labour-market signals) come via a careful secondary summary (nosov.ai). The abstract was verified directly against federalreserve.gov; the full-text figures were not. Confirm against the PDF before publication (open question Q4, §II.12).
9. **β rests on a single vendor-commissioned study.** The SusVibes 2.5× is one study, commissioned by Checkmarx, rated ●●○○ Reported. An independent replication would materially raise or lower the tracker's confidence in the J-curve depth. The fully-verified β is unmeasured. (Open question Q13, §II.12.)
10. **δ cannot be estimated.** The model's most important missing number. Every statement about the full cycle's length rests on a working assumption (δ ≈ 3–5 years), not a measurement. The first δ estimate is the tracker's highest-priority research item. (Open question Q17, §II.12.)
11. **The Wardley stagings are judgments.** Every staging in §II.11.2 is a judgment with an evidence anchor, not a measurement. Contested stagings (especially foundation models' drift toward Commodity, where the price evidence is thin) should be flagged and debated, not asserted. (Open question Q14, §II.12.)
12. **The two-velocity assumption could be wrong.** Institutional absorption might accelerate — a major incident, a court decision, or a regulatory shock could compress δ dramatically (Perez's turning point is often *triggered* by a crash or crisis). The tracker watches for the trigger events (§II.11.5) and would revise δ's working assumption if one lands.
13. **α's denominators are undefined.** Neither α_distribution nor α_compute is a computed ratio — both are judgments anchored on adoption-speed and capital-expenditure evidence. A defined "total AI investment" denominator does not exist. Until one is constructed, α is a directional statement (distribution cheap, compute expensive), not a number. (Open question Q16, §II.12.)
14. **γ's share estimates are methodology-dependent.** The accelerator Herfindahl-Hirschman Index rests on estimates (Silicon Analysts / International Data Corporation) with no audited table, and the share depends on whether hyperscaler custom silicon is counted. The cloud index rests on Synergy Research Group's published shares, which are the best available but not audited.
15. **The compressed-cycle baseline conflates two things.** The Railroad/Personal-Computer baseline (30–40 years) mixes installation length with payoff lag. The tracker's curve (§II.11.3) should annotate them separately before the baseline is drawn as anything more than schematic. (Open question Q16, §II.12.)
16. **Backtesting validates the framework, not the mismatch apparatus.** The backtest (§II.10) can validate Perez's phases, the Solow measurement, and the J-curve against historical cases — but Group C (the institutional mismatch), the model's strongest signal for the present, has no historical analogue and is unvalidatable by backtesting. The aggregate Solow measurement also misses sectoral payoffs (the dynamo failure, §II.10.8). The backtest's verdict on the model is therefore partial by construction, and the document does not present it as complete.

---
### II.10 Backtesting: Validating the Model on Previous Revolutions

*Substantiates T10, T3, and T1 (the internet sub-case, §II.10.6, tests the two-hand clock).*

*Added 22 November 2026, on Yorgo's requirement: backtesting is a core requirement of the model, not an appendix.*

#### II.10.1 The Principle

The model earns its standing on the present by demonstrating it describes the past. A framework that cannot reconstruct previous revolutions has no authority on this one. Backtesting is therefore not a nice-to-have and not a marketing exercise: it is the test the model must pass before its reading of the created-intelligence cycle is worth anything.

What backtesting means, operationally: run the same apparatus — Perez phase placement, Solow measurement, the parametric curve, the four knobs, the heatmap — on historical cases, and compare the retrospective needle against the historically established phase dating. The comparison is against *independent* historical scholarship (Perez's own datings, the growth-accounting literature, the diffusion record), not against the model's own outputs. Where the apparatus reproduces the established dating, it earns confidence. Where it fails or is ambiguous, the failure is recorded (§II.10.8) — a validation section that only shows successes is not validation.

Two cautions, stated before the cases. First, **the backtest is retrospective by construction**: Perez herself warns that big-bang dates are identifiable "only with hindsight" (§II.2.2, criticism 4). A model that reconstructs the past has shown it can *describe* a completed cycle; it has not shown it can *date* a live one. The backtest validates the apparatus's descriptive power, not its predictive power — and the document does not claim otherwise. Second, **David's warning** (§II.10.4): Paul David warned repeatedly against using historical resemblance to predict the specific path of the future. The dynamo parallel illuminates the mechanism; it does not license a forecast.

#### II.10.2 The Cases

Five cases, in Perez's order (§II.2.1). The first surge (Industrial Revolution, 1771–) is excluded as a full case: no national accounts and no Total Factor Productivity (TFP) series exist before ~1800, and the diffusion record is fragmentary. Crafts' finding — that TFP growth was comparatively slow during the First Industrial Revolution — is carried as a bound, not a case.

| Case | Surge | Big-bang | Perez dating (from §II.2.1) | Backtest target |
|---|---|---|---|---|
| Steam and railways (§II.10.3) | 2nd | Stephenson's *Rocket*, 1829 | Irruption 1830s; frenzy 1840s; turning point 1847 crash, 1848–50; synergy 1850–57; maturity 1857–73 | The frenzy→turning-point sequence around the Railway Mania |
| The dynamo (§II.10.4) | 3rd (worked case) | Carnegie Bessemer plant, 1875; first central power stations, 1881–82 | Irruption 1875–84; frenzy 1884–93; turning point 1893–95; synergy 1895–1907; maturity 1908–18 | The J-curve dip and the 40-year payoff lag |
| Oil, automobiles, mass production (§II.10.5) | 4th | First Model T, 1908 | Irruption 1908–20; frenzy 1920–29; turning point 1929–33 (Europe) / 1929–43 (USA); synergy 1943–59; maturity 1960–74 | The deployment payoff (Golden Age) and the safety-regulation lag |
| Information and Communications Technology (§II.10.6) | 5th | Intel microprocessor, 1971 | Irruption 1971–87; frenzy 1987–2001; turning point 2001–?? — still open | The only case with modern data — and the most ambiguous |
| Personal computer / internet (§II.10.6) | 5th (sub-cases) | Personal computer, late 1970s; web, 1990s | Sub-cycles within the fifth surge | The closest analogue to the AI sub-cycle |

For each case, the same four applications: Perez phase placement over time; the Solow measurement (historical growth accounting and TFP where it exists); the parametric curve (capability velocity vs profit-and-loss capture, the J-curve dip); the four knobs (α, β, γ, δ) with historical values or proxies. The heatmap is shown at key dates where the parameters are reconstructable — and the gaps are marked, not filled.

#### II.10.3 Steam and Railways

**Perez phase placement over time.** Irruption in the 1830s (the Liverpool–Manchester line opened 1830; the network grew steadily). Frenzy in the 1840s — the Railway Mania: Parliament sanctioned 805 miles of new line in 1844, about 2,700 miles in 1845, and a record 4,538 miles in 1846; at the peak, 272 Railway Acts were passed and some 9,500 miles of railway were proposed. Turning point: the share-price peak in August 1845, the commercial crisis of October 1847 (the government suspended the Bank Charter Act on 25 October 1847), and the regulatory recomposition of 1848–50. Synergy 1850–57, maturity 1857–73. **The backtest target is the frenzy→turning-point sequence: the apparatus must place the needle in frenzy in 1845 and at the turning point in 1847–48.**

**Solow measurement.** No TFP series exists for the 1840s — growth accounting begins with Kendrick (1961), whose series starts in 1889. The nearest measurement is Abramovitz & David (1973): United States labour productivity grew 0.5% per year in 1800–55 and 1.1% per year in 1855–90. For Britain, Crafts' growth-accounting work shows TFP growth was slow through the early industrial period. **The Solow apparatus cannot be applied to this case at all in its TFP form** — the backtest must say so, and must not substitute a modern series for a historical one. What *is* measurable is the investment flow (Group A) and the diffusion record (Group B).

**Parametric curve.** Line A (Capital & Capability Velocity): railway capital investment reached £44 million in 1847, practically all from private sources, mostly individuals — at the mania's height, individual investors were putting twice as much money into railway infrastructure as the nation spent on the military; between 1844 and 1851, railways absorbed 20% of the total output of the engineering industry. Line B (Net Enterprise Profit-and-Loss Capture): the railway share index fell ~64–66% from its August 1845 peak to 1849–50 (Odlyzko's index: 167.9 in summer 1845 → 60.5 at end-1849; Campbell & Turner's index: 1,984 → 673 by April 1850). Odlyzko's finding is the J-curve mechanism made concrete: the mania tripled British railway mileage, the new lines cost more than expected and earned less than expected, and even well-run railways saw profits plummet — the value went to the *users* of the network, not to the investors who built it. The "collective hallucination" (Odlyzko's term): trustworthy quantitative measures existed showing demand could not support the revenues promoters promised, yet investors ignored them. **The curve's divergence — Line A soaring, Line B collapsing — is the frenzy signature, and the backtest's first pass criterion is that the apparatus shows it.**

**The four knobs.**
- **α ≈ 0.9** (qualitative, from the evidence): nearly everything physical — track, rolling stock, stations, bridges, the telegraph. The α baseline for a physical-era revolution.
- **β (proxy): the safety-and-regulation cost vs the construction cost.** No direct β exists. The proxy is the regulatory sequence: the Railway Inspectorate was established in 1840 (Board of Trade inspectors to enquire into accidents); the 1842 Railway Act strengthened safety inspection; Gladstone's Railway Regulation Act 1844 (7 & 8 Vict. c. 85) set minimum passenger standards (the "parliamentary trains" at one penny per mile, with seats and weather protection), gave the government the right to buy railways after 21 years and to take control in national emergency, and the right to fix fares. The β proxy is *qualitative*: the cost of making railways safe and governable, relative to the cost of building them. It cannot be reduced to a number from the surviving record — and the backtest says so rather than inventing one.
- **γ (concentration): high, then consolidating.** Over 100 competing companies at the mania's peak; George Hudson's empire (the "Railway King") was the era's concentration story; amalgamation followed through the rest of the century until a handful of large companies remained. No Herfindahl-Hirschman Index (HHI) is computable from the surviving data at reasonable effort — the market-share series does not exist in usable form.
- **δ (proxy): ~10–14 years.** From the first commercial line (Liverpool–Manchester, 1830) to the first safety inspectorate (1840) is 10 years; to Gladstone's comprehensive Act (1844) is 14 years. The δ proxy is *time from mass deployment to first comprehensive regulation* — not the gap's half-life, which cannot be computed without a gap metric. The proxy is stated as a proxy (open question Q21, §II.12).

**Heatmap at key dates.** At 1847 (the crash): Group A reconstructable (investment flows, share prices — all frenzy readings, rust); Group B reconstructable (miles authorised and built — frenzy, rust); Group D partially reconstructable (the 1840/1842/1844 Acts are turning-point markers — amber); Groups C, E, F not reconstructable (no mismatch surveys, no TFP series, no income-share series for the 1840s). At 1860 (deployment): Groups A and B reconstructable (synergy readings — blue, on the investment and diffusion evidence); Group D reconstructable (the regulatory framework in place — blue); Groups C, E, F still not reconstructable. **The 1847 heatmap would show 13 of 30 squares; the 1860 heatmap the same 13.** The backtest's honest finding for this case is that the apparatus works on the finance and diffusion halves and is silent on the rest.

#### II.10.4 The Dynamo: The Worked Case

The dynamo is the classic general-purpose-technology case, and the most complete backtest available. Paul David's "The Dynamo and the Computer" (*American Economic Review*, 1990) is the founding text of the productivity-paradox literature, and David & Wright (1999) supply the supporting diffusion time-series (derived from DuBoff's 1979 series).

**Perez phase placement over time.** The third surge's dating (from §II.2.1): irruption 1875–84, frenzy 1884–93, turning point 1893–95, synergy 1895–1907, maturity 1908–18. The dynamo's own timeline sits *across* these phases: first central power stations 1881–82 (Edison, New York and London); electric motors under 5% of United States factory mechanical drive in 1899; ~25% by 1910; just over 50% by 1919; nearly 80% by 1929. **The backtest's first observation is a tension: the dynamo's diffusion (1881–1929) spans the whole surge and extends well past its maturity date (1918).** The general-purpose technology's lifecycle and the surge's lifecycle are not the same thing — a finding the tracker's present-day reading should carry (the AI sub-cycle's diffusion may similarly outlast the ICT surge's phases).

**Solow measurement — the backtest's most important finding.** The manufacturing evidence shows the payoff clearly: manufacturing multifactor productivity grew 0.92% per year in 1889–1909 and 2.73% per year in 1909–1929 (Baily & Schultze 1990, from Kendrick 1961); manufacturing TFP grew only ~0.2% per year in 1909–1919, then jumped to ~5.3% per year in 1919–1929 (David & Wright 1999); trend labour-productivity growth in manufacturing jumped from 1.5% per year (1899–1914) to 5.1% per year (1919–1929); 13 of 14 major industry groups saw multifactor productivity accelerate. David estimated that about half of the 5-point acceleration was statistically accounted for by the growth in secondary electric motor capacity. **But the aggregate evidence shows no such jump:** nonfarm business multifactor productivity was 1.63% per year in 1889–1909 and 1.68% in 1909–1929 — essentially flat across the dynamo's payoff decade (Baily & Schultze 1990). **The aggregate Solow measurement misses the sectoral payoff.** A tracker reading only the aggregate residual in 1925 would have concluded the dynamo had delivered nothing — while the manufacturing data showed a 5-point acceleration. This is a *failure* of the apparatus as specified, and the backtest records it as such (§II.10.8): the fix is sector-level Solow measurement, and the fix is a consequence of the backtest, not a precondition for it.

**Parametric curve.** Line A (Capital & Capability Velocity): the electrification series above — <5% (1899) → ~25% (1910) → >50% (1919) → ~80% (1929). Line B (Net Enterprise Profit-and-Loss Capture / J-curve): manufacturing TFP flat (~0.2%/yr, 1909–19), then the 1920s surge (~5.3%/yr, 1919–29). **The J-curve dip is the 1880s–1910s — roughly four decades from the first central power station to the productivity payoff** (David's own phrase: "four decades after the first central power station opened for business" — an interpretive span anchored to specific events, not a precisely measured constant). The mechanism is the re-architecture story: early adopters retrofitted electric motors onto the existing "group drive" (central shafts and belts inherited from steam) and captured only energy savings; the large gains waited until factories were rebuilt around "unit drive" (a motor on each machine), which freed the floor plan from the geometry of the old transmission line. David also noted that electricity did not get real momentum until after 1914–17, when regulated regional utility rates came down substantially — the *institutional* precondition (rate regulation) preceded the payoff, just as the tracker's Group D logic requires. **The backtest's second pass criterion is that the curve shows the dip where the record shows one — and it does, with the mechanism attached.**

**The four knobs.**
- **α (high, qualitative):** power stations, the grid, wiring, motors — mostly new physical plant. The distribution rails (the factory building, the workforce) existed; the power rails did not. The α split (§II.5.1) applies here too: α_distribution low, α_compute high — the same structure as created intelligence, with different contents.
- **β (proxy): the re-architecture cost vs the motor cost.** The β analogue for the dynamo is the cost of tearing down and rebuilding the factory (unit drive) relative to the cost of the motors themselves. The historical record does not price this ratio directly — but David's mechanism *implies* it was large (the whole factory had to be rebuilt to release the gains) and that it *fell* as unit drive standardised. The proxy is qualitative and the backtest says so. (Open question Q21, §II.12.)
- **γ (concentration): high, regulated.** Local utility monopolies, regulated regionally; the rate regulation after 1914–17 is the γ story (concentration *managed* by regulation, not eliminated). No HHI is computable from the surviving data at reasonable effort.
- **δ (proxy): ~15–30 years to the regulatory framework; ~40 years to the payoff.** From the first central power stations (1881) to the National Electrical Code (1897) is 16 years; to state utility regulation (1907–14) is ~25–30 years; to the productivity payoff (1920s) is ~40 years. The δ proxy splits into two numbers — time-to-regulation and time-to-payoff — and the backtest keeps them separate. The time-to-payoff figure (~40 years) is the most consequential number in this section for the present-day model (§II.10.9).

**Heatmap at key dates.** At 1900: Groups A and B reconstructable (investment in power stations and motors; electrification <5% — irruption/frenzy, rust); Group E reconstructable at sector level (manufacturing TFP flat — installation, rust) but *not* at aggregate level (the aggregate series shows no signal — grey); Group D partially reconstructable (the National Electrical Code 1897 is a turning-point marker — amber); Groups C and F not reconstructable. At 1920: Groups A, B, E reconstructable (electrification >50%, manufacturing TFP surging — synergy, blue at sector level); Group D reconstructable (utility regulation in place — blue); Groups C and F still not reconstructable. **The 1900 heatmap would show ~14 of 30 squares; the 1920 heatmap the same 14, with the colours flipped on the reconstructable rows.** The flip — rust to blue on Groups B, D, and E (sector) — is the backtest's visual pass criterion, and the dynamo passes it.

#### II.10.5 Oil, Automobiles, Mass Production

**Perez phase placement over time.** Irruption 1908–20 (the Model T, the assembly line in 1913); frenzy 1920–29 (the 1920s boom, overcapacity, the stock-market bubble); turning point 1929–33 (Europe) / 1929–43 (United States) — the crash, the Depression, the New Deal, the Second World War; synergy 1943–59 (the post-war Golden Age); maturity 1960–74 (saturation, the oil shocks). **The backtest target is the deployment payoff: the apparatus must show the needle moving to synergy in the late 1940s and the Solow measurement confirming it.**

**Solow measurement.** This is the case where the aggregate measurement *works*: United States TFP growth was 2.4% per year in 1948–1966 — the strongest sustained rate in the Kendrick series (1889–1988 average: 1.6%) — and labour productivity grew 3.3% per year in the same window. The Golden Age is the deployment payoff made visible at aggregate level. The maturity signal is equally clear: TFP fell to 1.0% (1966–73) and −0.2% (1973–81); nonfarm multifactor productivity was −0.03% per year in 1973–79. **The apparatus passes here: the aggregate Solow measurement tracks the Perez phases (synergy = high TFP, maturity = falling TFP) in a way it did not for the dynamo.** The difference is that the fourth surge's paradigm (mass production, oil, the automobile) permeated the *whole* economy, while the dynamo's payoff was concentrated in manufacturing. The backtest's lesson: the aggregate measurement works when the paradigm is economy-wide, and fails when the payoff is sectoral — which is why the tracker needs both levels (§II.10.8).

**Parametric curve.** Line A (Capital & Capability Velocity): car ownership rose from 1% of United States households in 1908 to 50% by 1948 and 75% by 1960; the United States produced three-quarters of all automobiles in the world by 1950 (8.0 million of 10.6 million); the Model T sold 15 million units (1908–27) with its price falling from $600 (1912) to $290 (1925); the assembly line's first full year built 248,000 cars against 78,000 the year before. Line B (Net Enterprise Profit-and-Loss Capture): unlike railways, the automobile industry's profits were *real* — but the J-curve dip for this surge is not in firm profits, it is in the *social* cost: mass deployment from the 1920s with no safety framework until 1966. Highway fatalities rose from 36,399 in 1960 to 53,543 in 1969 (+47.1% in the decade), peaked at 54,589 in 1972 — the highest number ever recorded — and only then declined (39,250 in 1992; 32,675 in 2014), while the fatality rate fell from 5.5 deaths per 100 million vehicle-miles travelled in 1966 to 1.1 by 2014 (Federal Highway Administration / National Highway Traffic Safety Administration Fatality Analysis Reporting System). **The curve's divergence for this surge is between capability (Line A, soaring from the 1910s) and safety (the unpriced externality, rising until the 1970s).** The J-curve dip is measured in lives, not dollars — and the backtest records that the model's Line B, as specified for created intelligence (profit-and-loss capture), would need a *social-cost* line to capture this surge's dip. That is a gap in the apparatus, stated here rather than hidden.

**The four knobs.**
- **α (high, qualitative):** roads, petrol stations, factories, suburbs — mostly new physical plant. The Interstate Highway System (1956) alone is the α story: the distribution rails for automobiles had to be built.
- **β (proxy): the safety-and-regulation cost vs the production cost.** The proxy is the safety apparatus: the National Traffic and Motor Vehicle Safety Act and the Highway Safety Act (signed 9 September 1966), the United States Department of Transportation (established 15 October 1966), the National Highway Traffic Safety Administration (established 1970), and the Federal Motor Vehicle Safety Standards that followed. The National Highway Traffic Safety Administration estimates that safety technologies saved more than 600,000 lives from 1960 through 2012. The β proxy is the *cost of the safety framework* (regulation, standards, vehicle redesign) relative to the *cost of production* — qualitative, not a number, from the surviving record.
- **γ (concentration): highly concentrated — and computable.** By the end of the 1950s the smaller producers had disappeared or merged, and the industry was dominated by General Motors, Ford, and Chrysler. From 1969 production figures (General Motors 4.6 million, Ford 2.1 million, Chrysler 1.5 million, American Motors Corporation 0.26 million, of 8.2 million-plus United States passenger cars): Herfindahl-Hirschman Index ≈ 3,874 (my calculation — shares approximately 54%, 25%, 18%, 3%). Highly concentrated by any standard (United States Department of Justice / Federal Trade Commission thresholds: above 1,800 highly concentrated under the 2023 guidelines). **This is the only historical γ with a computable index in this section** — and it confirms Perez's late-frenzy consolidation prediction.
- **δ (proxy): ~40 years from mass production to the safety framework; ~18 years from majority ownership.** From mass production (1910s–20s) to the 1966 Acts is ~40–50 years; from 50% household ownership (1948) to the 1966 Acts is 18 years. The δ proxy depends on the start date, and the backtest states both. **Either way, this is the longest δ in the sample — and the most consequential for the present-day model** (§II.10.9). Note also that the fatality peak (1972) came *after* the legislation (1966): the framework was in place before the worst year, and the decline followed. The fatality-rate series (5.5 → 1.1 deaths per 100 million vehicle-miles travelled, 1966–2014) is the only historical case with a *measured narrowing series* for a safety gap — the kind of series δ needs, and the kind the created-intelligence tracker does not yet have.

**Heatmap at key dates.** At 1929 (the crash): Groups A, B, F reconstructable (investment, diffusion, and the Piketty-Saez top-share series, which begins in 1913 for the United States — the top-0.1% share above 10%, frenzy, rust); Group E reconstructable (Kendrick's series begins 1889 — TFP at trend through the 1920s, grey/amber); Groups C and D partially reconstructable (no mismatch surveys; the regulatory milestones are sparse before the New Deal). At 1960 (synergy/maturity): Groups A, B, E, F reconstructable (TFP 2.4%, diffusion at 75% household ownership, top shares falling toward deployment levels — blue); Group D partially reconstructable (the safety framework still six years away — rust on the safety parameter, amber on the broader regulatory picture); Group C not reconstructable. **The 1929 heatmap would show ~18 of 30 squares; the 1960 heatmap ~20.** The automobile case is the most reconstructable of the historical cases — and even it leaves Group C blank.

#### II.10.6 Information and Communications Technology and the Sub-Cases

**Perez phase placement over time.** Irruption 1971–87; frenzy 1987–2001; turning point 2001–?? — still open per Perez 2022–2025 ("we seem to be stuck in the installation period or in what I call the 'turning point'… the record in length has been broken, for both the installation and the turning point itself"). Synergy not yet reached. **This is the only case where the full apparatus can be applied with modern data — and the case where the model is most ambiguous.** The backtest cannot validate the turning-point judgment against a completed case, because the case is not complete. What it *can* do is test the apparatus on the surge's completed *sub-cycles*.

**Solow measurement.** The paradox (1987) → the resurgence (1995–2004, labour productivity ~2.8% per year) → the slowdown (2005–15, 1.3% per year; 1973–79 multifactor productivity −0.03% per year is the earlier slowdown's marker). The ICT case is the *exception* Crafts notes: the general-purpose-technology payoff arrived faster than the dynamo's (~25 years from commercialisation to the resurgence, vs ~40 for the dynamo). The apparatus reads this correctly — the Solow measurement shows the J-curve dip (1970s–80s), the payoff (1995–2004), and the second slowdown (2005–15). **The backtest passes on the measurement and fails on the phase dating**: the measurement shows a complete J-curve, but Perez's phase placement says deployment has not begun. The disagreement is itself the information (§II.2.5) — and it is the same disagreement the tracker faces today on created intelligence.

**The personal-computer sub-case.** David & Wright's observation: the spread of the personal computer in the 1980s looked like group drive — the new machine layered onto the old organisation (the office, the workflow) without re-architecture. The payoff came in the 1990s when organisations redesigned around networked computing. The sub-case tests the apparatus's *mechanism* (group drive → unit drive, applied to the office rather than the factory) and it passes: the mechanism generalises.

**The internet sub-case — the closest analogue to the AI sub-cycle.** A complete frenzy→turning-point→synergy sequence *within* the surge: frenzy 1995–2000 (the dot-com bubble), crash 2000–02 (the NASDAQ collapse), turning point 2001–03 (the Sarbanes-Oxley Act 2002, the regulatory recomposition), deployment from ~2003 (broadband, e-commerce, the platform economy). The internet sub-case is the backtest's most directly useful case for the AI needle: it tests whether the apparatus can date a sub-cycle's turning point *while the parent surge's turning point is still open*. The apparatus passes on the dating (the markers are clear: the crash, the legislation, the deployment that followed) — but the pass is against a sub-cycle, not a surge, and the backtest says so. **The internet sub-case is the best available evidence that the two-hand clock (§II.2.5) is a workable instrument — and the only evidence of its kind.**

**Heatmap at key dates.** At 2000 (frenzy peak): all six groups reconstructable with modern data — the only historical case where the full 30-parameter heatmap can be drawn (with the caveat that the Group C surveys did not exist in their current form; the mismatch evidence for 2000 is narrative and regulatory, not survey-based). At 2010 (turning point, ongoing): the full heatmap is reconstructable, and the Group C evidence begins to appear in measurable form (the first governance surveys). **The ICT case is the bridge between the historical backtest and the present-day tracker: it is where the apparatus goes from partial to full.**

#### II.10.7 What Is Reconstructable and What Is Not

The honest limits, stated case by case. "Reconstructable" means a sourced series or a dated milestone exists; "partial" means milestone dates or narrative evidence exists but no series; "not reconstructable" means neither exists.

| Parameter group | Railways (1840s–60s) | Dynamo (1880s–1920s) | Automobiles (1910s–70s) | ICT (1970s–) |
|---|---|---|---|---|
| A. Finance and investment | **Reconstructable** — share prices, capital raised, investment flows (Odlyzko; Campbell & Turner) | **Reconstructable** — power-station investment, utility capitalisation | **Reconstructable** — production, sales, capital expenditure | **Reconstructable** — full modern data |
| B. Diffusion | **Reconstructable** — miles authorised and built | **Reconstructable** — electrification rates (DuBoff via David & Wright) | **Reconstructable** — registrations, household ownership | **Reconstructable** — adoption series |
| C. Institutional mismatch | **Not reconstructable** — no surveys; narrative only (inspectors' complaints, Hudson's fraud) | **Not reconstructable** — no surveys; narrative only (accident reports, rate disputes) | **Partial** — no surveys, but the fatality series is a measured gap proxy | **Partial** — surveys begin in the 2010s; earlier evidence is narrative |
| D. Regulatory recomposition | **Partial** — milestone dates (1840/1842/1844 Acts); no gap metrics | **Partial** — milestone dates (National Electrical Code 1897; state utility regulation 1907–14) | **Partial** — milestone dates (1966 Acts; National Highway Traffic Safety Administration 1970) | **Reconstructable** — full milestone record |
| E. Productivity and returns | **Not reconstructable** — no TFP series before 1889; labour-productivity estimates only (Abramovitz & David) | **Reconstructable from 1889** — Kendrick's series; sector-level (manufacturing) is the informative level | **Reconstructable** — Kendrick + Bureau of Labor Statistics series | **Reconstructable** — full modern data |
| F. Inequality and structure | **Not reconstructable** — no income-share series for the 1840s | **Partial** — Piketty-Saez from 1913 (United States); market-share data thin | **Reconstructable** — Piketty-Saez + production shares (γ computable) | **Reconstructable** — full modern data |

**The honest headline.** The backtest validates the *framework* — Perez's phases, the Solow measurement, the J-curve — but it does **not** validate the mismatch apparatus (Group C), which is the model's strongest signal for the present. Group C has no historical analogue: no 19th-century equivalent of a governance-bypass survey exists, and the mismatch for earlier revolutions must be inferred from narrative evidence (the Board of Trade inspectors complaining that regulations were "constantly being ignored" is the 1840s analogue of the 47% policy-bypass figure — suggestive, not measurable). Validation that only works where data happens to exist must say so, and this section does. Group C must be validated *prospectively* — by its predictions about the present, tracked in the dated assessment log (§II.11.5) — not retrospectively.

**β needs a proxy for earlier revolutions, and the proxy is the weakest link.** For railways, the dynamo, and automobiles, β is proxied by the cost of making the technology safe, governable, or re-architected, relative to the cost of deploying it. These proxies measure *related* quantities (safety cost, re-architecture cost), not β itself (verification cost). The proxy choice is an open question (Q21, §II.12), and the backtest's β readings should be treated as directional, not numeric.

#### II.10.8 The Validation Standard

What counts as the model passing — stated before the results, so the standard cannot be moved to fit them.

**Pass criteria:**
1. **The retrospective needle matches historically established phase dating** (Perez's dating plus the historical consensus) within the band, at the target dates (§II.10.2). The band is the judgment rule's band (§II.2.5): the needle is a band, not a point, and a pass means the established dating falls inside it.
2. **The J-curve dip appears where the record shows one** — the dynamo's 1880s–1910s dip, the ICT dip of the 1970s–90s, the railway investor-return collapse of 1845–50 — with the mechanism attached (group drive → unit drive; the collective hallucination; the safety externality).
3. **The turning-point markers precede the historically dated turning points** — the railway crash (1847) precedes the 1848–50 turning point; the 1929 crash precedes the 1930s–40s recomposition; the dot-com crash (2000–02) precedes the Sarbanes-Oxley recomposition (2002–03). The markers must *lead*, not follow: a model whose markers arrive after the turning point is a description, not an instrument.

**Where the model would have FAILED or been ambiguous — recorded, not hidden:**
1. **The aggregate Solow measurement misses the dynamo's sectoral payoff** (§II.10.4). Nonfarm multifactor productivity was flat across the payoff decade (1.63% → 1.68%) while manufacturing multifactor productivity nearly tripled (0.92% → 2.73%). A tracker reading only the aggregate residual in 1925 would have concluded the dynamo had delivered nothing. **This is a failure of the apparatus as specified.** The fix — sector-level Solow measurement — is a consequence of the backtest, and the backtest records the failure first and the fix second.
2. **The third surge's turning point is genuinely ambiguous in Perez's own texts** — dated 1893–95, 1890–95, and 1890–93 in different works (§II.2.2, criticism 10), and the Belle Époque is called both a Gilded Age and a golden age. A backtest that "passes" on the third surge would be passing against a moving target. The dynamo case is therefore scored on its *mechanism* (the J-curve, the re-architecture story) rather than on its phase dating.
3. **The ICT turning point is still open** — the backtest cannot validate the model's most important current judgment (the turning point is beginning) against a completed case. The internet sub-case is the closest available test, and it is a sub-cycle, not a surge. The model's central present-day claim rests on an apparatus whose turning-point judgment has never been validated against a completed surge's turning point. That is the backtest's most serious limitation, and it is stated here.
4. **Group C has no historical analogue** (§II.10.7). The mismatch apparatus — the model's strongest signal for the present — is unvalidatable by backtesting. It must be validated prospectively, and the dated assessment log (§II.11.5) is the mechanism.
5. **Line B needs a social-cost line.** The automobile case's J-curve dip is measured in lives, not dollars (§II.10.5). The parametric curve as specified (Line B = Net Enterprise Profit-and-Loss Capture) would not have captured the automobile surge's dip. The apparatus needs a social-cost line for cases where the externality is the dip — and the created-intelligence case may be one of them (the production-damage incidents, the security failures, are social costs before they are profit-and-loss costs).

#### II.10.9 What the Backtest Changes

Backtesting is not a stamp of approval — it feeds back into the model. Four changes follow from the cases above:

1. **δ's working assumption is optimistic, and the full-cycle estimate with it.** The historical δ proxies — railways ~10–14 years to first regulation, dynamo ~15–30 years to the regulatory framework, automobiles ~40 years to the safety framework — are all measured in *decades*, not years. The tracker's working assumption (δ ≈ 3–5 years, §II.5.4) is shorter than every historical case. If the created-intelligence δ is in the historical range, the full-cycle estimate of 10–20+ years (§II.6.2) is itself optimistic and should be revised upward. The backtest does not *prove* this — the proxies measure time-to-regulation, not the gap's half-life, and created intelligence's technical velocity is genuinely unprecedented — but it shifts the burden of proof: the compressed-δ case now needs positive evidence, not just the absence of a measurement. **The δ working assumption is revised to "3–5 years (optimistic); the historical range is 10–40 years to the regulatory framework" pending the first measured δ.**
2. **Sector-level Solow measurement is added to the apparatus.** The dynamo failure (§II.10.8, item 1) requires it. The tracker carries the aggregate TFP series (E2) *and* a sector-level series for the sectors where created intelligence is concentrated (software development, financial services) as the data becomes available. Until sector-level data exists, the aggregate reading carries a standing caveat: the payoff may be arriving in a sector the aggregate cannot see.
3. **The β proxy choice is settled before the backtest runs.** The backtest cannot proceed on β until the proxy is chosen (re-architecture cost? safety cost? both, as separate proxies?). Open question Q21 (§II.12) carries this decision.
4. **Historical heatmaps carry a data-availability marker.** Every backtest heatmap marks each square as measured, inferred (from narrative or milestone evidence), or blank (no data). A reader must be able to see at a glance which squares the backtest actually tests and which it assumes. The present-day heatmap (§II.11.1) does not need this marker — every square is measured — but the historical ones do, and the distinction is part of the validation standard.

---
### II.11 The Instrument: Heatmap-First

*Substantiates T11, T8, T5, and T6 (the parametric curve visualizes the J-curve dip; the Wardley panel shows the mismatch at component level).*

**The design decision, stated plainly.** The heatmap is the primary instrument. The dial (the two-hand clock) is demoted to a summary strip. The parametric curve is the second view. The Wardley panel is the component view. This section recommends *one* structure, not a menu.

#### II.11.1 The Primary Heatmap: 30 Numbered Squares

**Layout.** Rows are the six parameter groups, in the tracker's order: A. Finance and investment (6 squares), B. Diffusion (4), C. Institutional mismatch (7), D. Regulatory recomposition (3), E. Productivity and returns (7), F. Inequality and structure (3). Each parameter is one square, numbered 1–30 in group order (A1 = 1 … A6 = 6, B1 = 7 … B4 = 10, C1 = 11 … C7 = 17, D1 = 18 … D3 = 20, E1 = 21 … E7 = 27, F1 = 28 … F3 = 30). The number is the square's identity; the colour is its status.

**Colour = status.** Four colours, matching the report's existing visual language:
- **Rust (#b3543f) — Lagging.** The condition is far from deployment levels, or actively points the other way.
- **Amber (#c98a2d, or the report's nearest amber) — Getting there.** Moving toward deployment levels, or the precondition is met but the substance is not.
- **Blue (#283060) — In place.** The condition is met at deployment levels.
- **Grey (#c9c2b0, the report's neutral) — Unclear.** The reading is ambiguous, or the parameter measures disagreement rather than a state.

**The mapping from phase reading to status is mechanical** (stated in §II.7, repeated here because it is a rule, not a judgment): frenzy/irruption → Lagging; turning point / turning-point precondition → Getting there; synergy/maturity → In place; ambiguous or meta-parameter → Unclear. The Chief Editor does not re-decide the colour per parameter — the phase reading decides it. (The phase reading itself is the judgment; the colour follows.)

**The legend.** Below (or beside) the heatmap, the legend maps each number to its parameter: number → parameter name → current value → phase reading → source. The legend is the heatmap's text: the squares are the glance, the legend is the reading. On the site, each legend row links to the evidencing article where one exists (Group C and Group D rows link to report articles; Group A/E/F rows link to the external source).

**Today's picture, at a glance.** 23 rust, 5 amber, 0 blue, 2 grey. The Group C row is solid rust (7 of 7). The Group E row is 5 rust, 2 grey. The Group D row is 2 amber, 1 rust — the only row with any amber at all, plus B1/B2 and F2. **The empty blue column is the verdict made visible.** When a square turns blue, that is a news event — and the dated assessment log (§II.11.5) records it.

**Why rows = groups, not a single 30-square grid.** The groups are the model's structure: the reader should see *where* the rust concentrates (Group C: the mismatch; Group E: the missing payoff) and *where* the amber appears (Group D: the recomposition). A single grid would show the count but hide the pattern. The group rows make the pattern the first thing the reader sees.

**Accessibility.** Colour is never the only channel: each square carries its number, and the legend carries the status word. The heatmap is readable in greyscale (number + legend) and by screen reader (the legend is a table, not an image).

#### II.11.2 The Second Panel: Wardley Stages

**Layout.** A horizontal strip with four columns — Genesis, Custom-Built, Product, Commodity — and the ten components placed in their stage (from §II.4.2). Components that are drifting (foundation models: Product → Commodity; deterministic guardrails: Genesis → Custom-Built) sit on the boundary between columns, with the direction of drift marked by an arrow.

| Genesis | Custom-Built | Product | Commodity |
|---|---|---|---|
| Audit / certification of AI codebases | Enterprise-wide orchestration | Foundation models → (drifting to Commodity) | *(empty — nothing in the created-intelligence stack has commoditized yet)* |
| Agent liability / insurance | Verification / security review of AI code | AI coding assistants | |
| *(Deterministic guardrails →)* | Agent identity / attribution | Agent frameworks / harnesses | |
| | Kill switches / supervision | | |
| | Deterministic guardrails (← from Genesis) | | |

**What the panel shows.** The dangerous configuration, at a glance: the *deployment* components (coding assistants, agent frameworks) are at Product, while the *governance* components (identity, verification, guardrails, audit, liability) are at Custom-Built or Genesis. The panel's empty Commodity column is the second honest headline: nothing in the created-intelligence stack has commoditized yet — the revolution is still young.

**Staging rules.** Each staging carries its evidence anchor (§II.4.2) and is labelled a judgment. When a component's staging changes (e.g. foundation models crossing to Commodity, or guardrails consolidating to Product), the change is logged in the dated assessment log (§II.11.5) with the evidence that moved it. Contested stagings are flagged, not hidden (open question Q14, §II.12).

#### II.11.3 The Second View: The Parametric Adoption and Margin Curve

**Layout.** X-axis: Cycle Progress, 0% (big-bang) to 100% (deployment/synergy achieved). Y-axis: two lines.
- **Line A — Capital & Capability Velocity** (steep rise). Anchored by A1 (capital expenditure), A3 (venture funding), B4 (capability trajectory). The line is *measured* for its left half (we are on it) and *projected* for its right half.
- **Line B — Net Enterprise Profit-and-Loss Capture / J-curve** (dips negative during the Governance Tax phase, crosses back above zero only after workflow re-architecture). Anchored by E5 (95% zero measurable return), E6 (the verification tax), β ≈ 2.5 (§II.5.2). The dip's *depth* is governed by β; its *width* is governed by δ.

**The divergence between Line A and Line B is the governance tax made visible.** The two lines are the model's central visual argument: capital and capability are racing ahead while enterprise profit-and-loss capture is underwater. The gap between them is the cost of the mismatch.

**The honest drawing rule.** The evidence covers only the left half of the curve (we are in the dip). **The right half — the climb out of the trough — is drawn dashed, as a projection, never as a finding.** Projecting the right half is feature F-25 (forecasting) territory, which is on hold pending Yorgo's interface write-up. The curve does not project a date for the trough's bottom or the zero-crossing until β and δ are measured as series.

**The baseline comparison.** The Railroad/Personal-Computer baseline (30–40 years) is drawn as a faint reference curve behind the created-intelligence curve — *schematic only*, annotated to separate installation length from payoff lag (§II.6.2, §II.9 item 15). The baseline's purpose is to show the compression of the technical half, not to imply a known full-cycle length for created intelligence.

#### II.11.4 The Summary Strip: The Dial, Demoted

The two-hand clock survives as a **summary strip** at the top of the tracker page: two hands (outer: ICT surge — extended turning point; inner: AI sub-cycle — late frenzy, turning point beginning) and the heat tally (23 lagging / 5 getting there / 0 in place / 2 unclear). One line of text: the verdict. The strip is the answer to "where are we?" in five seconds; the heatmap is the answer in thirty seconds; the legend and the curve are the answer in five minutes. The strip links to the heatmap; the heatmap links to the legend; the legend links to the evidence.

#### II.11.5 The Apparatus That Keeps the Instrument Honest

**The parameter panel.** The full parameter table (§II.7) is the tracker's data: every parameter, its value, its source, its quality note, its phase reading, its heat status. The heatmap is a *view* of the panel, not a replacement for it. When a parameter's value changes, the panel updates first; the heatmap follows.

**The watch-for list.** The events that would move a square (carried from v1 §5.4, updated):
- **ACA/NSCP 2027 survey** (expected November 2027): the first repeat of the testing question — the first δ data point (C5, δ).
- **BCG 2027 banking survey**: the first repeat of the monitoring question — the second δ data point (C2, δ).
- **FEDS / Federal Reserve productivity releases** (quarterly): the Total Factor Productivity series (E2) and the aggregate verdict (E3).
- **The US federal AI request for information** (promised April 2026, still unpublished): its publication closes part of D2.
- **First court test of agent liability** (any jurisdiction): moves D3 from "asserted" to "tested."
- **A SusVibes-style verification-cost replication** (any independent source): the first β confirmation or correction (E6, β).
- **A major incident or crash**: the event that could accelerate δ (§II.9 item 12) — or deepen the frenzy reading.
- **NVIDIA's accelerator share** (quarterly, via Silicon Analysts / International Data Corporation estimates): γ₁'s direction of travel.

**The dated assessment log.** Modelled on the report's Corrections page: every change to a phase reading, a heat status, a Wardley staging, or the verdict is logged with its date, its evidence, and its reasoning — and **entries are never removed**. The log is the tracker's memory: it is what makes the model auditable, and it is what prevents the heatmap from quietly rewriting its own history.

**Update cadence.**

| Cadence | What updates |
|---|---|
| Daily (the report's watch) | Groups B, C, D — new survey figures, regulatory milestones, failure counts. The watch adds the figures to the report; the tracker updates the affected parameters. |
| Quarterly | Bureau of Labor Statistics productivity (E1, E2); hyperscaler capital expenditure (A1); venture funding (A3); NVIDIA's share (γ₁); cloud shares (γ₂). |
| Annually | Total Factor Productivity (E2, annual vintage); Internal Revenue Service income shares (F1); survey series (ACA/NSCP, BCG, Capgemini, DORA). |
| As they land | Regulatory milestones (D1); major papers (FEDS, MIT NANDA follow-ups); market events (market-capitalisation milestones, funding rounds); court decisions (D3). |
| Quarterly re-assessment | The Chief Editor re-reads the needle: does any parameter's phase reading change? Does the verdict change? The re-assessment is logged (§II.11.5) whether or not anything moves. |

**Site placement (design only — no generator work in this document).** A dedicated page in Guides & Reference, alongside the CI vs EI page. A small dial (the summary strip, §II.11.4) on the executive dashboard, linking to the tracker page. The tracker page carries Yorgo P. Bougás's byline, not the firm's, until the tracker is useful and verified (§II.1). Report figures link to their evidencing articles; external parameters link to their sources. The heatmap is built from the parameter panel's data — one source of truth, not a hand-drawn image.

---

### II.12 Open Questions

*Carries the open questions on T1–T12.*

v1's twelve questions, carried forward and updated where the new apparatus reframes them, plus nine new ones (Q13–Q21) and two v1 questions restored (Q22–Q23).

#### Carried from v1 (updated)

**Q1 — Framing: follow Perez (third leap inside the ICT surge) or treat AI as a sixth surge?** The draft follows Perez's own logic (the clock is two-handed). If Yorgo prefers the sixth-surge reading, the outer hand's interpretation changes (the ICT surge would be in maturity/decline) and the heatmap's groupings would need re-examination. *The new apparatus does not settle this — it makes the stakes visible: the Wardley panel and the Infrastructure 2 analysis hold under either framing; the outer-hand reading does not.*

**Q2 — How much of the report's evidence base should the tracker re-verify?** The draft takes the report's figures and ratings as given. A deeper pass would re-check the underlying surveys (sample sizes, question wording, response rates) for the Group C figures the verdict leans on. *Unchanged.*

**Q3 — F1 series: pull a like-for-like World Inequality Database / Piketty-Saez series** for the top-0.1% income share, so the Perez comparison is apples-to-apples rather than indicative. *Unchanged.*

**Q4 — FEDS full-text figures: confirm against the PDF** (A2's pipeline, A5's lab revenue, F3's labour-market signals) before publication. The abstract is verified; the full-text figures are via a secondary summary. *Unchanged.*

**Q5 — The deployment bar.** The draft proposes: Total Factor Productivity above ~1.5% sustained for two or more years *and* the institutional framework settled (the federal gap closed, liability tested, governance gaps narrowing). *Updated by the new apparatus: the bar now has two more components — β falling toward 1 (verification cost approaching generation cost) and δ measured and shortening. The bar is therefore four conditions, not two. Yorgo's call on whether all four are required, or whether the productivity and institutional conditions suffice.*

**Q6 — How to handle the "installation" parameters in the tally.** The E-group's readings are "installation" (the payoff has not arrived), not frenzy/turning-point/synergy. v1 excluded them from the phase tally (16/5/0 over 21 parameters). *Updated: the heat tally counts all 30 (23/5/0/2), mapping installation readings to Lagging. The question is whether the phase tally should also count them — the tracker's provisional answer is no: the phase tally is a Perez-phase count, and "installation" is not a phase in Perez's sense; the heat tally is the headline count.*

**Q7 — Who moves the needle?** The Chief Editor re-assesses quarterly and logs the re-assessment — or Yorgo approves phase changes himself. *Unchanged; the dated assessment log (§II.11.5) makes either arrangement auditable.*

**Q8 — The Acemoglu vs J-curve fork: what evidence would discriminate?** The draft lists the fork but does not resolve it. The discriminating evidence would be: (a) a Total Factor Productivity upturn coinciding with the intangible-investment cycle (J-curve wins), or (b) task-level gains plateauing at low levels with no aggregate response (Acemoglu wins). *Updated: β's trajectory is the third discriminator — if β falls toward 1, the J-curve mechanism is working; if β rises, the verification burden is structural.*

**Q9 — Should the tracker cover the consumer/retail side?** The report's evidence is enterprise/finance/developer only. A consumer adoption parameter (FEDS: ~50% of adults use AI outside work) would need its own source base. *Unchanged.*

**Q10 — Geography: does the tracker need a China/Asia lens?** The report is US/United Kingdom-centric. The ICT surge's turning point is a global process; the tracker's verdict is, strictly, a US verdict with United Kingdom/European Union regulatory markers. *Unchanged.*

**Q11 — The "no credible dollar figure" gap.** The report has no money-saved-or-lost figure, and the tracker inherits that hole. Should the tracker commission or estimate one, or keep the honest "insufficient data"? *Unchanged — the tracker's provisional answer is to keep the honest gap and to treat the first credible dollar figure as a news event.*

**Q12 — How does the tracker relate to the report's daily watch?** The watch adds figures to the report; the tracker updates parameters. Who owns the parameter update — the watch worker, or a separate tracker role? *Unchanged; the update cadence table (§II.11.5) assigns the work but not the role.*

#### New in v2

**Q13 — β measurability.** Is a single β meaningful across domains, or does each domain (code, agents, finance, legal) need its own β? The tracker's provisional answer: one β per domain, with code-β as the only measured one. *What would settle it: a verification-cost study outside code.*

**Q14 — Wardley staging judgments.** Each staging in §II.11.2 is a judgment. Who stages, how are contested stagings resolved, and what evidence moves a component between stages? *The tracker's provisional answer: the Chief Editor stages, with the evidence anchor stated and the staging flagged as contested where the evidence is thin (foundation models' commodity drift is the most contested staging today).*

**Q15 — Velocity-multiplier calibration.** The multiplier is threshold- and population-dependent (§II.6.1). Should the tracker carry a *standard* comparison (e.g. "time to majority use among US financial firms" as the canonical X), or state the comparison fresh every time? *The tracker's provisional answer: state it fresh every time — a canonical X would hide the multiplier's dependence on the choice.*

**Q16 — The compressed-cycle evidence base.** What would confirm or refute a 6–10 year full cycle? The tracker's answer: a measured δ (§II.5.4). *The supporting work: construct a sourced historical α baseline (railroad investment as a share of gross domestic product; internet build-out capital expenditure 1995–2001) and separate installation length from payoff lag in the Railroad/Personal-Computer baseline curve before it is drawn as anything more than schematic.*

**Q17 — The two-velocity assumption and δ estimation.** Is exponential convergence the right functional form for δ, or does absorption proceed in steps (regulation lands, then a rush of adoption)? *The tracker's provisional answer: exponential is a placeholder; the first two data points will discriminate. The deeper question: what if institutional absorption accelerates after a trigger event (§II.9 item 12)? The tracker watches for trigger events and would revise δ's working assumption if one lands.*

**Q18 — γ lock-in measurement.** Which quantitative lock-in indicator is measurable from public sources — egress-fee levels, multi-cloud adoption rates, the share of enterprise AI workloads on proprietary vs portable frameworks? *The tracker's provisional answer: egress fees are the most publicly observable; multi-cloud rates are survey-dependent; the proprietary-vs-portable split has no published source.*

**Q19 — Historical data availability per parameter.** Which of the 30 parameters have reconstructable historical series, and for which cases? *The tracker's provisional answer is the §II.10.7 table: Groups A and B are reconstructable for all cases; Group E from 1889 (United States); Group F from 1913 (Piketty-Saez) or by case; Group D partially (milestone dates only); Group C not at all. The full audit — parameter by parameter, case by case — is the work.*

**Q20 — Which cases are fully vs partially reconstructable?** *The tracker's provisional answer: automobiles are the most complete (~20 of 30 squares at 1960); the dynamo next (~14 of 30, with the colours flipping between 1900 and 1920); railways partial (~13 of 30, no productivity series); ICT complete but unfinished (the turning point is still open); the first surge excluded (no national accounts before ~1800). No historical case reaches the full 30 — the backtest is partial by construction, and the heatmaps must carry the data-availability marker (§II.10.9).*

**Q21 — Proxy choices for β and δ in earlier revolutions.** Is the "re-architecture cost" / "safety cost" proxy for β the right one, and is "time from mass deployment to first comprehensive regulation" the right proxy for δ? *The tracker's provisional answer: for δ, yes — with the caveat that the proxy measures time-to-regulation, not the gap's half-life, and the two numbers (railways ~10–14 years, dynamo ~15–30 years, automobiles ~40 years) should be reported as a range with the start-date stated. For β, the proxy is the weakest link: the re-architecture and safety costs are related quantities, not β itself, and the backtest's β readings are directional only. The β proxy needs a dedicated design decision before the backtest runs.*

#### Restored from v1

**Q22 — The inner hand's big-bang dating.** November 2022 (ChatGPT's public release) is the provisional big-bang. Perez warns big-bangs are identifiable only in hindsight. Alternatives: the transformer paper (2017), GPT-3 (Generative Pre-trained Transformer 3, 2020), or the agentic turn (2025). The dating moves the inner hand's phase boundaries. *Recommendation: keep November 2022 as the provisional dating, labelled as such, and revisit at the first quarterly re-assessment.*

**Q23 — The "no crash yet" problem.** The turning-point call is the weakest part of the assessment (§II.9). If no crash or reckoning arrives, the tracker could sit at "late frenzy, turning point beginning" for a long time — which is honest, but risks looking like a forecast that never lands. *The defence is the watch-for list (§II.11.5) and the log: the tracker states what would confirm or refute it, and the record shows it.*

---
### II.13 Sources

*Holds the sources behind T1–T12.*

#### Frameworks and theory

- Perez, Carlota. *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages.* Edward Elgar, 2002. — The framework. (2007 abridgement of Chapter 5 in *Cambridge Journal of Economics* 31(6): 801–824 for the inequality comparison.)
- Perez, Carlota. "The double bubble at the turn of the century: technological roots and structural implications." *Cambridge Journal of Economics*, 2009. — The "double bubble" concept.
- Perez, Carlota. "The AI revolution and the next turning point." *Open Access Government*, 2025. — Perez's application to AI.
- Perez, Carlota. "Is artificial intelligence a new technological revolution or just another techno-economic paradigm?" (2025/2026, draft). — "AI is not a new revolution but a quantum leap in the ICT revolution's power and reach" (via the review cited in the draft).
- Perez, Carlota & Leach, Tom. "A Smart Green 'European Way of Life': The Path for a New Golden Age." *Transformations* (University College London (UCL) Institute for Innovation and Public Purpose), 2018.
- Solow, Robert M. "Technical Change and the Aggregate Production Function." *The Review of Economics and Statistics* 39(3): 312–320, 1957. — The 7/8ths finding.
- Solow, Robert M. "We'd better watch out." *New York Times Book Review*, 12 July 1987. — "You can see the computer age everywhere but in the productivity statistics."
- Brynjolfsson, Erik, Rock, Daniel & Syverson, Chad. "The Productivity J-Curve: How Intangibles Complement General Purpose Technologies." National Bureau of Economic Research Working Paper 25148, September 2018; *American Economic Journal: Macroeconomics* 13(1): 333–372, January 2021. Digital object identifier (DOI) 10.1257/mac.20180386. — The J-curve, with both dates (see §II.14).
- Brynjolfsson, Erik & Hitt, Lorin M. "Beyond Computation: Information Technology, Organizational Transformation and Business Performance." *Journal of Economic Perspectives* 14(4): 23–48, 2000.
- Brynjolfsson, Erik, Rock, Daniel & Syverson, Chad. "Artificial Intelligence and the Modern Productivity Paradox: A Clash of Expectations and Statistics." National Bureau of Economic Research Working Paper 24001, 2017; published 2019 in *The Economics of Artificial Intelligence* (Agrawal, Gans & Goldfarb, eds.).
- Acemoglu, Daron. "The Simple Macroeconomics of AI." *Economic Policy*, 2025. — The ≤0.66% Total Factor Productivity upper bound over 10 years.
- Aghion, Philippe & Bunel, Simon. "AI and Growth: Where Do We Stand?" (2024). — The 0.68pp/yr estimate.
- Aghion, Philippe, Jones, Benjamin F. & Jones, Charles I. "Artificial Intelligence and Economic Growth." In *The Economics of Artificial Intelligence* (2019).
- Wardley, Simon. *Wardley Maps.* Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0), 2015. — The book; the technique was created at Fotango in 2005 (see §II.14).
- Rogers, Everett M. *Diffusion of Innovations.* Free Press, 1962 (5th edition, 2003).
- Moore, Geoffrey A. *Crossing the Chasm.* HarperBusiness, 1991.
- Dixon, Chris. "The core driver of the computing movement is the mutually reinforcing feedback loop between applications and infrastructure." cdixon.org / a16z writing, 2010s–2020s. — The Infrastructure–Application Cycle; practitioner framework, no single canonical publication (see §II.14).
- David, Paul A. "The Dynamo and the Computer: An Historical Perspective on the Modern Productivity Paradox." *American Economic Review* 80(2): 355–361, 1990. — The ~40-year electrification payoff lag.
- Crafts, Nicholas. "The Productivity Slowdown: A Historical Perspective." (2019). — The ~25-year computer payoff lag.
- Hannemyr, Gisle. "The Internet as Hyperbole: A Critical Examination of Adoption Statistics." *The Information Society* 19(2): 111–121, 2003. — The critique of the "years to 50 million users" figures.

#### Productivity and macro data

- Bureau of Labor Statistics, *Productivity and Costs* (United States Department of Labor release USDL 26-0558, 5 March 2026; revised 24 March 2026); Q3 2026 release (5 November 2026).
- Bureau of Labor Statistics, Total Factor Productivity release (19 March 2026).
- Carollo, Christopher, Crane, Leland D., Garcia Molina, Mauricio & Nichols, Alexander. "Artificial Intelligence and the U.S. Economy: Current Evidence." Finance and Economics Discussion Series (FEDS) 2026-074, Federal Reserve Board, 12 November 2026. DOI 10.17016/FEDS.2026.074. — Abstract verified directly against federalreserve.gov; full-text figures via a careful secondary summary (nosov.ai) — confirm against the PDF before publication.
- Jefferson, Philip N. Keynote address, Federal Reserve Board, 13 November 2026. — Invokes Solow's 1987 paradox for the generative-AI era.
- International Monetary Fund (IMF), *World Economic Outlook* (2026). — The 14–56% task-level gain range.
- Organisation for Economic Co-operation and Development (OECD) (2024/2025). — The 0.2–1.3pp/yr macro estimates.
- Goldman Sachs (March 2023). — The ~7% higher annual global gross domestic product over 10 years estimate.
- Baslandze, Salome et al. Federal Reserve Bank of Atlanta Working Paper 2026-4 (March 2026, revised May 2026). — The chief financial officer survey (~734 executives).
- Internal Revenue Service, Statistics of Income, Publication 1304, Table 4.1 (March 2026). — The top-0.1% income share (10.1% of adjusted gross income, tax year 2023).
- Piketty, Thomas & Saez, Emmanuel. "Income Inequality in the United States, 1913–1998." *Quarterly Journal of Economics* 118(1): 1–39, 2003. — The series Perez cites.

#### Adoption and capability

- UBS / Similarweb, via Reuters (1 February 2023). — ChatGPT's 100 million monthly active users in ~2 months; 1 million users in 5 days.
- ACA/NSCP 2026 AI Benchmarking Survey (12 November 2026). — 86% of US financial firms use AI; 38% formally test outputs.
- JetBrains Developer Ecosystem Survey 2026. — ~47% of code written fully by AI agents.
- Sonar, *State of Code 2026*. — 42% of committed code AI-generated or assisted; 65% expected by 2027.
- METR (the independent model-evaluation organisation), time-horizon measurements (2026); METR/Anthropic study (5 November 2026). — The ~7-month doubling; the ~1.9× capability-improvement rate.
- Synergy Research Group (Q3 2026). — Cloud market shares (Amazon Web Services 26%, Microsoft Azure 19%, Google Cloud 16%); 1,360 large hyperscale data centres at end-2025, ~800 more in the pipeline.
- Silicon Analysts / International Data Corporation (August–November 2026). — NVIDIA's ~73–81% AI accelerator revenue share (estimates; no audited table exists).

#### The report's evidence base (for Group C and Group D parameters)

- The CI SITREP report itself: `~/workspace/your_files/watches/SYNTHESIZED.md` (122 articles, as of 22 November 2026) and `~/workspace/ci-sitrep/dashboard.json` (62 panel figures + 8 strip items). Confidence ratings are the report's own. Key surveys: EY US AI Risk and Governance Survey 2026; Boston Consulting Group AI Safety and Governance in Banking 2026 (13 November 2026); SailPoint Horizons of Identity Security (October 2026); Palo Alto Networks 2026 Identity Security Landscape (20 May 2026); Writer / Workplace Intelligence (2026); Financial Conduct Authority Wholesale Banks Supervision Insights 3 (2 November 2026); Capgemini (5 November 2026); Nutanix Enterprise Cloud Index 2026; Cloud Security Alliance / Token Security; PagerDuty 2026; Verizon Data Breach Investigations Report 2026; Cyera analysis of 7,000+ public AI incidents; Veracode Fall 2026; Sajadi et al. (1 November 2026); Georgia Tech Vibe Security Radar; Google DevOps Research and Assessment (DORA) 2024–2026; GitClear, "The Maintainability Gap" (January 2026); MIT NANDA, "The GenAI Divide" (July 2025); SusVibes re-run (2 November 2026, vendor-commissioned by Checkmarx); A.S.E 2.0 (the agentic security-evaluation benchmark); SecPRBench.

#### Historical backtesting (§II.10)

- Odlyzko, Andrew. "The Railway Mania: Fraud, disappointed expectations, and the modern economy." (Revised version, 14 August 2012.) — The Railway Mania's scale (Parliament sanctioned 805 miles in 1844, ~2,700 in 1845, 4,538 in 1846; the share index fell ~64% from summer 1845 to end-1849; the mania tripled British railway mileage); the "collective hallucination" argument; fraud as mask, not cause.
- Odlyzko, Andrew. "The collapse of the Railway Mania, the development of capital markets, and Robert Lucas Nash, a forgotten pioneer of accounting and financial analysis." (Revised version, 25 June 2011.) — The accounting revolutions the collapse produced.
- Campbell, Gareth & Turner, John D. — The railway share-price index (peak 1,984 in August 1845; 673 by April 1850), via the secondary accounts cited in §II.10.3.
- Railway Regulation Act 1840 ("Act for Regulating Railways") — Board of Trade inspectors, Railway Inspectorate established 1840. Railway Regulation Act 1844 (7 & 8 Vict. c. 85, Gladstone's Act; royal assent 9 August 1844) — parliamentary trains, government purchase option, emergency control, fare-fixing.
- David, Paul A. "The Dynamo and the Computer: An Historical Perspective on the Modern Productivity Paradox." *American Economic Review* 80(2): 355–361, 1990. — The dynamo case: electrification under 5% of factory drive in 1899; "four decades after the first central power station opened for business"; group drive vs unit drive; about half the 1920s acceleration statistically accounted for by secondary motor capacity.
- David, Paul A. & Wright, Gavin. "General Purpose Technologies and Surges in Productivity." University of Oxford Discussion Papers in Economic and Social History, no. 31, 1999. — The diffusion series (derived from DuBoff 1979): secondary-motor share just over 50% in 1919, nearly 80% in 1929; manufacturing Total Factor Productivity ~0.2% per year (1909–19) → ~5.3% per year (1919–29); labour-productivity trend 1.5% (1899–1914) → 5.1% (1919–1929).
- DuBoff, Richard B. (1979). — The underlying electrification series, via David & Wright (1999).
- Kendrick, John W. *Productivity Trends in the United States.* National Bureau of Economic Research / Princeton University Press, 1961. — The growth-accounting series from 1889 (figures from Kendrick's later summary of his series, for a consistent vintage): Total Factor Productivity 1.7% per year (1889–1919), 1.7% (1919–1948), 2.4% (1948–66), 1.0% (1966–73), −0.2% (1973–81); 1889–1988 average 1.6%.
- Abramovitz, Moses & David, Paul A. (1973). — United States labour productivity 0.5% per year (1800–55), 1.1% per year (1855–90).
- Baily, Martin Neil & Schultze, Charles L. "The Productivity of Capital in a Period of Slower Growth." *Brookings Papers on Economic Activity*, Microeconomics 1990. — Nonfarm multifactor productivity 1.63% (1889–1909) → 1.68% (1909–1929) vs manufacturing 0.92% → 2.73%: the aggregate/sectoral divergence that is the backtest's key failure finding.
- Crafts, Nicholas. "Growth Accounting in Economic History: Findings, Lessons and New Directions." *Journal of Economic Surveys* 35(3): 670–696, 2021. — Total Factor Productivity growth comparatively slow during the First Industrial Revolution; Solow's 7/8ths atypical; general-purpose-technology impact takes a long time to materialize, Information and Communications Technology the notable exception.
- Nader, Ralph. *Unsafe at Any Speed.* Grossman Publishers, 1965. — The book that drove the 1966 safety legislation.
- National Traffic and Motor Vehicle Safety Act (Pub.L. 89–563) and Highway Safety Act (Pub.L. 89–564), signed 9 September 1966; United States Department of Transportation established 15 October 1966 (Pub.L. 89–670); National Highway Traffic Safety Administration established 1970.
- Federal Highway Administration / National Highway Traffic Safety Administration, Fatality Analysis Reporting System, via *Conditions and Performance* reports (2006/2008/2010) and Bureau of Transportation Statistics, "A Half Century of Highway Safety Innovations — 1966 to 2016." — Highway fatalities: 50,894 (1966); 54,589 (1972, the highest ever recorded); 39,250 (1992); 32,675 (2014); fatality rate 5.5 → 1.1 deaths per 100 million vehicle-miles travelled (1966–2014); safety technologies saved more than 600,000 lives 1960–2012.

#### To check later (not used in this round)

- YouTube Short: "Railroads vs. the Internet vs. AI: Who Spent More?" (https://m.youtube.com/shorts/SbQTd35vXmA) — from the prior research. **Note as a source to check later via NotebookLM. Do not transcribe or summarize it from a transcript** (Yorgo's rule: video via NotebookLM, never transcript-only). This round does not need it.

---

### II.14 Conflicts and Corrections Log: The Prior Research vs the Draft

*Substantiates the corrections to T2 and T3.*

Every conflict, discrepancy, or correction between the prior research and the v1 draft, resolved or flagged. This log is part of the document, not an appendix to be dropped.

| # | Item | The prior research | The draft | Resolution |
|---|---|---|---|---|
| 1 | **J-curve date** | "Brynjolfsson's Productivity J-Curve (2021)" | Cites the 2018 working paper | **Resolved — both correct.** National Bureau of Economic Research Working Paper 25148, September 2018; *American Economic Journal: Macroeconomics*, January 2021. v2 cites both (§II.4.1, §II.13). |
| 2 | **Wardley Mapping date** | "Wardley Mapping (2015)" | (Not in the draft) | **Resolved — nuance, not error.** The technique was created by Simon Wardley at Fotango in 2005 (evolutionary framing 2004), developed at Canonical 2008–2010; the book *Wardley Maps* and the introduction post date to 2015. v2 cites "created 2005; book 2015" (§II.4.2). |
| 3 | **Dixon attribution** | "a16z / Chris Dixon's Infrastructure–Application Cycle" | (Not in the draft) | **Flagged — loose attribution.** No single canonical publication titled "Infrastructure–Application Cycle" exists. The core idea is Dixon's (from his body of writing at cdixon.org / a16z), but the framework as named is a synthesis, not a cited work — and the "Infrastructure 2 = verification/guardrails/audit" application to created intelligence is the prior research's (and now this model's), not Dixon's. v2 flags this in §II.4.3 and §II.13. |
| 4 | **Rogers/Moore "+ Institutional Friction"** | "Rogers / Moore + Institutional Friction" | (Not in the draft) | **Flagged — the prior research's addition.** Rogers (1962) and Moore (1991) do not separate technical from institutional friction in these terms. The friction split is the prior research's synthesis, adopted by v2 as a working distinction because the report's evidence demands it, and operationalized as δ (§II.4.4, §II.5.4). |
| 5 | **"Governance Tax" vs "verification tax"** | "Governance Tax" (capital/human labour diverted into intangible investments) | "Verification tax" (DORA — time saved generating re-spent auditing) | **Reconciled.** The report's term "verification tax" is the code-domain measurement (E6); The "Governance Tax" is the broader J-curve dip concept (scanning, compliance, remediation). v2 uses "verification tax" for the code-domain measurement and "governance tax" for the broader concept, and states the distinction explicitly (§II.4.1, §II.11.3). |
| 6 | **Compressed cycle: 6–10 years** | Created Intelligence compressed curve of 6–10 years vs Railroad/Personal-Computer baseline of 30–40 years | (Not in the draft — the draft's cycle is Perez's 20–30 year installation) | **Corrected.** 6–10 years is defensible only for the technical-diffusion half. The full cycle to deployment/synergy is set by the slower half (institutional absorption, δ) and is **10–20+ years** on the working assumption δ ≈ 3–5 years. A 6–10 year full cycle would require δ ≈ 2 years or less, which nothing in the evidence supports (§II.6.2). |
| 7 | **"Rides existing digital rails"** | "Software and created intelligence ride existing digital rails" | (Not in the draft — the draft's Group A shows the build-out's scale) | **Corrected.** Distribution rails exist (α_distribution ≈ 0.05–0.1), but compute rails are being built at railroad scale now (α_compute ≈ 0.7–0.9): $376.1bn hyperscaler capital expenditure in 2025, a data-centre pipeline over $1tn, 1,360 hyperscale data centres plus ~800 in the pipeline (§II.3, §II.5.1). |
| 8 | **Solow as era-bound** | "Both frameworks were derived from physical, heavy-capital-expenditure eras" — implying Solow is era-bound | (The draft presents Solow as a measurement apparatus) | **Corrected.** Solow's apparatus (the residual, the accounting identity) is era-neutral — it measures whatever the economy produces. The blind spot is in *Perez's* phase timings and unit of analysis, not in Solow (§II.3). |
| 9 | **The certainty claim** | "Certainty: High, 91%" (a self-assessment of the prior research) | (The draft carries no overall certainty score) | **Not adopted.** A self-assessed certainty is a property of the output, not of the evidence. The tracker carries no overall certainty score; each parameter carries its own source's standing (§II.7), and the uncertainty section (§II.9) states what could be wrong. |
| 10 | **YouTube Short link** | "Railroads vs. the Internet vs. AI: Who Spent More?" (link provided) | (Not in the draft) | **Noted, not used.** Recorded in §II.13 as a source to check later via NotebookLM. Not transcribed or summarized from a transcript, per Yorgo's rule. This round does not need it. |

---

*End of document. v2 (general-purpose-technology-tracker-2026-11-22.md) is the model document this whitepaper is drawn from; the v1 clock draft (solow-perez-clock-2026-11-22.md) is the research predecessor. The Surge Monitor — A General Purpose Technology Tracker, by Yorgo P. Bougás, Confluence<1>.*
