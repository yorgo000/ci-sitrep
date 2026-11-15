# Future Features — CI SITREP

A running list of features to build into CI SITREP. Yorgo adds features here; we review them together and decide what to build next. Each feature carries a status: **Proposed** (on the list, not yet started), **In progress**, **Done**, or **Dropped** (decided against, with the reason recorded).

To add a feature: append a new section at the bottom with the next number, status Proposed, today's date, and the description. Do not renumber existing features.

---

## F-01 — Executive dashboard: the undeniable realities at a glance

**Status:** Done (v1, 2026-11-15)
**Proposed:** 2026-11-12
**Built:** 2026-11-15 (Yorgo's pick — "work on graphics" while he reviewed the taxonomy)

A graphic / countdown / visual dashboard that gives high-level executives making service and product decisions an immediate, at-a-glance view of the things that will affect their decisions — the pragmatic facts that get lost in the fluff of the news cycle. The kind of thing the special forces keep their eye on: the actual undeniable realities, not which way the hype is blowing.

**Live at:** https://yorgo000.github.io/ci-sitrep/#executive-dashboard — the first top-level section of the main report page. **Moved into the main page 2026-11-15** (Yorgo's restructure): it was a standalone page at dashboard.html from its build that morning until the restructure that evening; `dashboard.html` now redirects to `index.html#executive-dashboard`, so the link sent out earlier still lands on the dashboard. Linked from the "How to read this" block ("Short on time?").

**What v1 shows (5 panels, 51 figures, 4 deadline countdowns):**

- **AI code share** — bars: ~47% of code written fully by AI agents (JetBrains), 42% of committed code AI-generated or assisted (Sonar, 65% expected by 2027), 75% of new code AI-generated (Google), 97% of organisations use AI coding assistants (Black Duck); finance cut: 86% of UK financial firms use AI, 80% deployed agents, 2% broad autonomy (BoE/FCA), 30% of large firms already use agentic AI (HK SFC).
- **The governance gap** — 13 bars (98% have policies / 47% bypassed them; 79% run agents / 2% have identity tools; 82% can't attribute actions; 88% can't roll back; 35% can't stop a rogue agent; 30% have a documented kill switch — 23% of those never tested), plus 188 documented damage cases and the 109:1 machine-to-human identity ratio; the FCA supervision finding (●●●●) as the Established anchor and the OpenAI 35-second kill switch as the counter-example.
- **Agentic right vs wrong** — SecureVibeBench stacked bar (23.8% correct-and-secure / 23.0% correct-but-exploitable / 53.3% incorrect); A.S.E 2.0 functional 74.0% vs secure 18.4%; CWE-bench ~68% pass@1; SecPRBench recall 32.5–78.1%; BugLedger 45–70% reintroduce, hint 0.35 → 0.71; ThinkingBox 67.16% pass@1 but only 241/507 on all 20 attempts; METR horizon doubles ~every 7 months.
- **Net impact: more code vs more cleanup** — a two-sided ledger (output up: Sonar 42%→65%, DORA throughput; cleanup up: GitClear duplication/churn, DORA stability, Black Duck 581 vulns +107%, Glasswing 175-to-1, Sajadi 11×, ETH Zurich 35.4-pt propagation, FCA outage). No single net number — the ledger says so honestly.
- **Money saved vs lost** — the honest panel: "No credible dollar figure exists yet" as the headline, with the cost multipliers (2.5× review cost, 3.4× vuln rate, 2.74× claimed) and the CMA 10%-of-turnover exposure context.
- **Countdown strip** — California kill-switch recommendations (Mon 16 Nov 2026), TPRM comments (Wed 16 Dec 2026), FCA CP26/38 (Wed 24 Dec 2026), OSFI E-23 (1 May 2027); days-remaining computed in the browser at load.

**Design (as built):**

- `dashboard.json` is the single source of truth (figures with value, label, source, source note, rating, date, and a link to the report article that evidences it); `_tools/build_dashboard.py` renders the section and `build_html.py` imports it, embedding the panels in `index.html` as H3s under the section's H2 ("Executive dashboard"), with the dashboard's CSS and countdown JS inserted after the template format step. Pure CSS bars and stat cards — no chart library, no backend, no cost.
- Every figure carries its credibility rating (dots + word) and links to the report article behind it — the article's runtime id, so the reader lands on the article expanded and its Source line takes them to the primary source. Six figures carry an "also" link to a second evidencing article in another subsection (SecureVibeBench, A.S.E ×3, BugLedger, CodeRabbit). The three §3.6 figures (ThinkingBox ×2, METR) still link to the section anchor: §3.6 is prose, not articles. The generator validates every figure (required fields, rating in the four levels, bar values 0–100, link anchors exist in index.html or among the computed article ids — `compute_article_ids()` replicates the share JS's slugify + uniqueId) and exits 1 on a bad entry.
- Panels start open (the template collapses every heading; the dashboard's JS re-opens them); breadcrumbs removed as noise on a one-screen page; share buttons on panel headings work as on the other pages.
- Panel order is editorial (audience-first): code share, governance gap, right vs wrong, net impact, money.

**Maintenance:** a DASHBOARD step in the daily watch cron (added 2026-11-15) — when a new article moves a headline number, update dashboard.json and regenerate index.html (which embeds and validates the dashboard); when a What-we're-watching date lands, update the deadlines list the same day. Never add a figure the report doesn't evidence; never invent a dollar figure for the money panel.

**Open questions (from the proposal, resolved):** cuts — a UK finance-sector cut exists (BoE/FCA) plus HK large firms; nothing below sector level yet. Cadence — updated with the daily watch when a headline number moves (the inventory's weekly-snapshot suggestion was superseded: the data file carries dates per figure, so either cadence works mechanically, and the daily watch already owns the numbers).

**Follow-ups (not in v1):** trend lines (the data file stores each figure with its date, so a second data round can draw the slope); verify.py dashboard checks — partly closed 2026-11-15, when the deep-link change made verify.py's anchor check accept the computed article ids, so the dashboard's links are covered by the same gate (dashboard.html is now a redirect, not a page to check); a money panel with real dollar evidence when it exists.

**Browser test (live, 2026-11-15):** 5 checks — page loads with the "As of Sunday, November 15, 2026" banner and countdown strip ("tomorrow", "in 31 days", "in 39 days", "in 167 days"); all five panels open on load with the ~47% bar, the SecureVibeBench stacked bar (23.8/23.0/53.3), and the money panel's "No credible dollar figure exists yet" statement confirmed; panel share button shows "Copied"; sidebar navigation both ways works. One defect found: a dashboard figure's source link landed on the right report section but left it collapsed — the report's anchor handler only opened ANCESTOR sections, never the target heading itself. Fixed the same day in both generators (expandForAnchor now also un-collapses the target heading itself), all 8 pages regenerated and pushed. The first re-test failed on a stale CDN copy minutes after deploy; the second re-test passed both checks (the §1.1 link opens §1.1 expanded with all six articles visible; the State-of-the-market link opens §3.4.3 expanded). Lesson: browser re-tests right after a deploy can hit a stale CDN edge — use a cache-busting query (?fresh=...) to force a fresh fetch. Note: view-source: URLs cannot be opened in the cloud browser, so a source check has to go through curl instead.

**Browser test, restructure + deep links (live, 2026-11-15 evening):** 10 checks — 9 passed first run: row layout (As-of + Sections controls, search, How-to-read right-justified), the two top-level sections in order with the countdown strip reading exactly as expected, sidebar TOC and masthead nav order, all three deep links (JetBrains → the adoption article expanded; BugLedger → its §1.6 article expanded and "also in §2.1" → the §2.1 article expanded; ThinkingBox → §3.6, the expected section-anchor exception), search returning 4 results for "TPRM", the dashboard.html redirect, and the theses page opening all-collapsed with its own Sections control working. One defect: "Collapse all" closed the two top-level sections too, leaving only two bare headings — the handler toggled every heading with no exception for the always-open ones. Fixed the same evening in both copies of build_html.py (Collapse all now skips the top-level sections, the three front-page sections, and the dashboard panels — i.e. it returns the page to its initial state; Expand all still opens everything), regenerated, verified 52/0, pushed, live-verified, and re-tested 4/4 passing.

## F-02 — Single database, filtered sitreps (the split, done right)

**Status:** Proposed
**Proposed:** 2026-11-13

The long-term product architecture. One database of all CI news gathered each day, across all industries. Every piece of data is collected, rated, vetted, tagged, summarised, and organised **once**. Sitreps are then produced by filtering:

- **Filter by industry** → a specific industry's sitrep (finance, healthcare, manufacturing, etc.).
- **Combine filters** → intersection reports (e.g. CIAC + finance, code + healthcare).
- **The same piece of information sells on multiple sitreps** — no duplication, no maintenance of parallel copies.

This resolves the split question: separate sitreps become *views* on one database, not separate products to maintain. The tagging taxonomy (subject, type, credibility, severity, jurisdiction, source-date) is the filter mechanism — it already exists in draft. What remains: the database itself (structured storage for articles + tags + ratings), the filter/query layer, and per-filter rendering.

**Design notes (to be refined):**

- The current SYNTHESIZED.md is the single source of truth in Markdown form; the database is its structured successor.
- Intersection reports (CIAC × finance) are the most commercially interesting filter — they serve the buyer who needs one slice, not the whole report.
- Open question: when does the Markdown source become a bottleneck? The filter UI on the static site (planned after the taxonomy backfill) is the first step toward filtered views without a backend.

## F-03 — Source directory + reader suggestions (in the audit section)

**Status:** Proposed
**Proposed:** 2026-11-13

In the self-audit section, keep a list of all the sources we track, follow, and get information from — the full source base behind the report, not just the per-article citations. And give readers a way to send us suggestions for more sources.

**What it should show:**

- **The source directory:** every source the watch follows — regulators, standards bodies, benchmark authors, research groups, vendor research, news outlets — organised so a reader can see at a glance what the report's coverage rests on. The audit page already computes the counts (110 unique URLs as of 13 Nov 2026); this makes the list itself visible.
- **Reader suggestions:** a way for users to propose sources we should be tracking. Every suggestion is a lead for the daily watch — and a signal about what the audience cares about.

**Design notes (decided 2026-11-13):**

- The directory is generated from the live report files (like the rest of the audit page), not hand-maintained — the source list is already in the Markdown, in the Source and Sources lines.
- **Suggestions:** a mailto link to ci-sitrep@confluence1.com. No form, no backend.
- **Metadata version, collapsible:** each source carries metadata (what we take from it, how often it's checked, when it was last cited), but behind a collapsible section — the list will grow tremendously and must stay manageable. The collapsed view is the plain list; the detail is one click away.

## F-04 — The funnel, the database, and the production backend

**Status:** Proposed
**Proposed:** 2026-11-13

The architecture for the whole operation — how information gets in, how it gets vetted, how it sits in the database, and how sitreps get produced from it. This is a design decision to make, discuss, and build; the architecture itself is the deliverable. It complements F-02 (the single-database / filtered-sitreps product model): F-02 is the data model, F-04 is the pipeline that feeds it and produces from it.

**The pipeline, as Yorgo described it:**

1. **The radar / funnel.** Goes far and wide and looks at everything, all the time (or once a day). Two streams:
   - Everything about the **development and application of CI systems** — code scanning before and after commit, agent architecting, developing, governing, deploying, etc.
   - Everything about **AI in specific verticals** — insurance, oil shipping, and every other industry we cover.
2. **Vetting on the fly (decided 2026-11-13).** We look at everything and gather everything relevant — but we only **collect** (admit to the database) what passes criteria. The vetting happens at intake, not in a separate later pass. The alternative — gather everything into the database first, vet later — was considered and rejected.
3. **The database.** All vetted information sits in one pool (see F-02). Each piece collected, rated, vetted, tagged, summarised, and organised once.
4. **The production backend (operator-side, not user-facing).** The ability to decide: produce a sitrep for any intersection of the data. Examples: all data about CI collectives × all data about the insurance industry → one sitrep; agent management and application (not development) × the oil shipping industry → another. The operator chooses the filters; the backend produces the sitrep.

**Open questions (to discuss and design):**

- **The intake criteria.** What passes the vetting bar at intake? The current report has a bar ("could change how a firm building critical systems in finance should act") — the funnel needs its own, broader criteria for what enters the database at all.
- **Radar scope and cadence.** How far and wide — which sources, which industries, which languages? Continuous or once a day?
- **Who/what vets on the fly.** Human, agent, or both? The current daily watch is agent-run with human review at the report level; intake vetting at scale may need a different split.
- **Database schema.** What fields per item — the tagging taxonomy (subject, type, credibility, severity, jurisdiction, source-date) is the starting point, but intake may need more.
- **The production interface.** What does the operator see and choose when producing a sitrep? How are filter intersections specified?
- **Relationship to the current daily watch.** Does the daily watch cron become the radar, or is the radar something broader that the watch feeds into?

## F-05 — State of the market (front-page synthesis)

**Status:** Done
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)
**Built:** 2026-11-14

A short synthesis — 2–4 sentences — at the very top of the report, above "New this week", giving a new reader the macro narrative before the granular updates: where AI code generation and agentic deployment stand, where governance lags, and where regulation is heading. The executive reader's first paragraph.

**Design notes (decided 2026-11-14):**

- Evidence-grounded in the report's own findings (the 45% flaw rate, the governance gap, the regulatory timeline) — no generic marketing lines.
- A named front-page section (H2), starting OPEN like "New this week" and "What we're watching", sharing the tinted navy panel and the de-emphasized meta-heading style.
- Maintenance rule: the daily watch revises it when a material shift lands; it must never go stale, or it contradicts the "up to date" promise. Recorded in RULES.md and the daily watch cron.
- This is the cheap version of F-01 — the dashboard is the fuller, visual version, later.

## F-06 — Monthly summary ("This month")

**Status:** Proposed
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)

A monthly synthesis below "New this week": the 3–4 biggest shifts of the month, so a reader checking in monthly instantly grasps the momentum without parsing individual tactical updates or digging through the Archive. Monthly, not quarterly — this field moves too fast for a quarterly cadence.

**Design notes:**

- First edition at the end of November 2026 (a strong first month: the governance gap, the TPRM extension, FCA supervision insights, the Glasswing 175-to-1 finding, the BoE/FCA survey).
- Natural raw material for the weekly newsletter (which synthesizes the week; this synthesizes the month).
- Open question: maintained by a month-end step in the daily watch cron, or a separate monthly job?

## F-07 — Plain-English tags in "New this week"

**Status:** Done
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)
**Built:** 2026-11-14

Replace the academic "(subject 1/2/3)" parentheticals in the "New this week" entries with plain tags — [Pre-commit], [In codebase], [Agentic]. The section names are already plain English; the parentheticals were the only place the numbered-subject language reached the public page.

**Design notes:**

- A display-label change only — it does not replace the tagging taxonomy (subject/type/severity/jurisdiction), which is the deeper tagging system and still awaits Yorgo's approval.
- The daily watch cron uses the plain tags for all new entries.

## F-08 — "What this means in practice" extended to §1

**Status:** Proposed
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day — the narrower version of the reviewer's per-link implication proposal)

The report already carries implication synthesis where it matters most: §2.7 is "What this means in practice", §3.4.2 has "What the regulatory picture means in practice", and several articles carry "What this changes in practice" bullets. §1 has no equivalent. Extend the existing pattern to §1 (and the rest of §3 where absent) — a synthesis paragraph per subsection that needs one, in the report's own voice, not a "Confluence<1> says" line under every link.

**Design notes:**

- Lower priority than F-05/F-07. Build when a §1 synthesis paragraph has something to say that the articles don't already say between them.

## F-09 — One findable contact point (the restrained conversion step)

**Status:** Done
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day — the narrower version of the reviewer's CTA proposal)
**Built:** 2026-11-14

The report page has no conversion path; the only contact point is one line on the About page ("For enquiries, write to ci-sitrep@confluence1.com"). Add exactly one restrained, findable entry point — not CTAs scattered through the text.

**Design notes:**

- Placement decided 2026-11-14 (Yorgo): a **masthead nav link** — "Work with Confluence<1>" as the last link in the report page's masthead nav, jumping to About's Contact section (about.html#contact). Set apart from the content links by a separator line. The footer-line alternative was not chosen.
- The real conversion engine remains the newsletter funnel (subscribe → site → value-add → Confluence<1> service), which still needs Yorgo's yes to start.

## F-10 — Business Impact & Risk module in each pillar

**Status:** Dropped
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)

**Why dropped:** the gap the reviewer identified is real (the report is technical, not P&L-framed), but the fix is the wrong shape. A Business Impact module in each of the three pillars would be either vague or duplicative — the F-01 data inventory already found the money panel is the thinnest, with no credible dollar figure, so sourced business-impact claims barely exist yet. The business layer belongs in F-01 (the dashboard, sourced numbers only) and in the newsletter (plain language for P&L readers), both already planned. F-05 (State of the market) carries the macro business framing in the meantime.

## F-11 — "Strategic Implication" sentence under major external links

**Status:** Dropped
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)

**Why dropped:** the proposal misreads where the report's authority comes from — it is the curation (selection, vetting, rating, organization), not per-link editorializing. A "Confluence<1> says" line under every major link would slow the daily watch, turn an evidence-based knowledge base into opinionated commentary, and duplicate what already exists (see F-08: the "in practice" synthesis pattern is already in §2.7, §3.4.2, and several articles). F-08 is the narrower version of this proposal.

## F-12 — Context-specific CTAs embedded in the text

**Status:** Dropped
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)

**Why dropped:** embedding sales CTAs at the end of sections ("Connect with Confluence<1> to architect your pre-commit gates") would spend the exact credibility the report is built on — a knowledge base that pitches reads as a sales document, and the ratings and citations are what make a P&L reader trust it. The reviewer's premise is also overstated: the intelligence is not proprietary (it is curated public sources); the moat is the ongoing curation, the ratings, and the certification framework, which a reader cannot take to a competitor. The conversion path was designed to run through the newsletter funnel, not the report page. F-09 is the restrained alternative.

## F-13 — Search the report

**Status:** Done
**Proposed:** 2026-11-14 (Yorgo — the report is reference material kept up to date; readers need to find their way back to information they saw)
**Built:** 2026-11-14

A search box at the top of the report page, right under the "As of" banner. Client-side: the page indexes its own text the first time the reader types — no build step, no index file, no backend, no cost, and always in sync with what the daily watch published. Searchable units are the same units the share buttons cover (articles, headings, substantive paragraphs, tables), so every result links to a stable anchor and clicking it opens the article expanded. Ranking: title matches above body matches, all-token matches above partial; top 10 shown with a count. Minimum 2 characters, 150ms debounce, Escape closes, arrow keys + Enter navigate, clear button, click-outside closes, aria-live result status. Icons are inline SVG (magnifier, clear ×).

**V1 scope (deliberate):** report page only. **Browser-tested live 2026-11-14 (5 checks):** box present under the banner; "kill switch" returns 10 results with highlighted matches; clicking a result jumps to the article and opens it expanded; nonsense query shows the exact "No matches" message; keyboard navigation (ArrowDown + Enter) works. The test caught one real gap: "TPRM" returned zero results — the report never used the acronym, and the standalone best-practice bullets (§1.5.2, §2.5) and "New this week" / "What we're watching" entries weren't indexed units. Fixed the same night: standalone list items are now indexed (top-level <li> outside <details>, ≥80 chars, nested items covered by their parent; ids assigned deterministically with the share slugify), and "(TPRM)" is now defined at first mention in four places (NTW entry, WWW item, §1.5.2, §2.5). Possible follow-ups: cross-page search via a generated index file; a floating search button for readers deep in the page; a small synonym/acronym map in the search JS for terms the prose doesn't spell out.

## F-14 — AI answers over the report

**Status:** Proposed
**Proposed:** 2026-11-14 (Yorgo — "the day will come when we will set up a link to have AI answer questions for the user")

A way for readers to ask questions and get answers grounded in the report. Assessment (2026-11-14): very doable, but a real project — days to a week for a solid v1, not an afternoon. Three pieces: (1) retrieval — finding the right passages for a question (search + ranking; F-13 is the foundation); (2) a language model to compose the answer; (3) a backend — GitHub Pages cannot run server code, so it needs a small serverless function plus an LLM API key (cost small, cents per question at this scale). The plumbing is standard; the hard part is editorial, not technical: answers must cite the report's articles, respect the credibility ratings, and say "not in the report" when the answer isn't there — otherwise it becomes a hallucination machine on top of a credibility-rated knowledge base.

**Notes / open questions:**
- Which backend host (serverless function); whose LLM API key pays; public vs subscriber-only — Q&A over the vetted database is a natural subscriber feature (fits the commercialization direction).
- Grounding rules in detail (citation format, rating-aware answering, refusal behaviour).
- The retrieval index rebuilds on each daily publish — automatable via the existing cron or a GitHub Action.

## F-15 — Glossary + tooltips

**Status:** Done 2026-11-14
**Proposed:** 2026-11-14 (Yorgo — the report's acronyms and jargon need a dictionary for the executive audience)

A glossary page (alphabetical, one line per term, each term linkable) built from a single Markdown source of truth, plus tooltips on the report itself: first mention of a term in each subsection gets a dotted underline; hovering (desktop) or tapping (mobile) shows the one-line definition with a link to the full glossary entry. The generator derives both from the same file, so the tooltip and the glossary can never drift apart. Draft: 71 entries mined from the report (GLOSSARY_DRAFT.md, delivered 2026-11-14). Yorgo approved the draft as-is the same evening ("better to have some of the lingo translated in a dictionary than none") and asked for it built that night, so he could send the link to executives the next morning; he will flag missing terms as he reads.

**Built 2026-11-14 (late evening):** GLOSSARY.md in the repo (71 entries, 19 letter headings) → glossary.html via build_page.py (each entry anchored by slug); tooltip data injected into index.html at build time by build_html.py (runtime wrapping, first mention per subsection; `agent`/`agentic` in the glossary but never tooltip-wrapped — too frequent); nav link "Glossary" in the report masthead; "Terms:" line in the How-to-read block. verify.py gained 10 glossary checks (45 total). **Rule (Yorgo): terms are never removed — even if the text that referred to a term drops out of the report, the entry stays; the dictionary only grows.** Recorded in RULES.md §2/§4 and in the daily watch cron (GLOSSARY step added 2026-11-14): the daily watch adds any new term or acronym introduced in the report, one line, plain language, alphabetical placement, regenerating both glossary.html and index.html.

**Browser-tested live 2026-11-14 (5/5 pass):** dotted terms present (TPRM, SAST, inference); hovering TPRM shows the tooltip with the glossary's definition verbatim; the tooltip's "Glossary →" link lands on glossary.html#tprm with the T section auto-expanded; the glossary page renders all 19 letter headings with entries (incl. the CI vs CI/CD collision note); a tooltip deep in §3.4.3 works. Two notes from the test, both non-defects: the TPRM tooltip wording differed from the test brief's paraphrase but matched the glossary entry verbatim (the brief was wrong, not the site); the "Expand all" click that seemed not to work was the sidebar's TOC control, not the "Sections: Expand all" control — the glossary TOC is flat, so there was nothing for it to expand, while individual headings and anchor auto-expand both work.

## F-16 — Reading list

**Status:** Proposed
**Proposed:** 2026-11-15 (Yorgo)

Let readers save items to a personal reading list and come back to them later — to read, or to share from there. An executive skims the report or the dashboard, saves the three findings that matter to their P&L, and reads them properly later instead of losing them in the 59-article report.

**Storage, in two stages:**

- **V1 — browser/device-local.** The list lives in the reader's own browser (localStorage): no backend, no account, works on GitHub Pages as-is. The reader's list stays on that device.
- **V2 — user database.** Once a user DB exists (the membership/commercialization work), the list is saved in perpetuity, tied to the account, and follows the reader across devices. V1 should offer to import the local list into the account when V2 arrives.

**Design notes:**

- It builds on the share infrastructure: every article, paragraph, table, and heading already has a deterministic runtime id and a stable anchor URL that opens expanded. A list entry stores the anchor URL, the item's title, its section, its credibility rating, and the date saved.
- The "add to reading list" control sits beside the share button on each item (articles at minimum; the same control works on the other shareable units since they share the anchor machinery).
- The list itself is a view the reader returns to (own page, linked from the masthead nav): each entry links back to its anchor in the report (opens expanded) and carries its share button, so sharing from the list works exactly like sharing from the report.
- **Open questions:** the list's home — own page vs a panel; ordering (most recent first, or report order); remove/clear; what happens when a saved article is superseded and archived — its anchor may disappear from the live report, so stale entries need graceful handling (link to the Archive, or a note that the item moved); local-storage limits for heavy readers.

## F-17 — Human baselines: every CI figure compared to human performance

**Status:** Proposed
**Proposed:** 2026-11-15 (Yorgo — "we need to compare all the CI-based code and agent performance to humans — it's meaningless on its own for an executive")

A benchmark score on its own tells an executive nothing: 74.0 on A.S.E, 67% on ThinkingBox, 45–70% on BugLedger — good or bad? The answer only exists against the human baseline for the same task. Every CI performance figure in the report and the dashboard should carry its human comparison next to it, wherever one exists — and where none exists, say so plainly (a gap in the evidence, not a number to guess).

**Already in the report, in scattered form (the seed of this feature):**

- CodeRabbit: CI code carries 2.74× the vulnerabilities of human-written code for equivalent tasks (§1.1, §2.1) — vendor claim, ●○○○.
- Sajadi et al. (v4, Nov 2026): on SWE-bench, a standalone LLM's patches introduced 135 manually confirmed vulnerabilities against 12 for developer patches on the same issues (§2.1) — peer-reviewed, the strongest human-comparison evidence in the report.
- METR time horizons (§3.6): agent task-completion time vs human task time on the same tasks — the agent-performance equivalent.
- SusVibes re-run (§1.6): human review as the control that reduces the vulnerability share — the human as the intervention, not just the baseline.
- GitClear (§2.1): the maintainability gap, measured against human-authored code's churn patterns.

**What F-17 adds — making it systematic:**

- **A baseline audit.** Walk every performance figure in the report and the dashboard and record, per figure, whether a human baseline exists in the cited source (same task, same metric) or not. The audit itself is a finding: most benchmarks publish no human baseline at all, and that absence is worth stating.
- **Baseline next to the figure.** Where a baseline exists, it travels with the figure — in the article (a bullet: "human baseline on the same task: X"), and in the dashboard (a second value or a "vs human" line on the figure). The comparison must be same-task, same-metric; a human number from a different task is not a baseline.
- **No baseline, no guess.** Where the source publishes no human comparison, the figure carries a "no human baseline published" note rather than an invented one. Over time this becomes a pressure point: benchmarks that publish baselines are more useful to executives, and the report can say so.
- **A human-baseline view (later).** Once baselines are structured data (a natural field for the F-02 database), a dedicated view — every CI-vs-human comparison in one place — becomes possible. That is a later step; the audit and the per-figure baselines come first.

**Open questions:** how the dashboard shows a baseline without doubling the figure count (second value, ratio, or a toggle); whether to score benchmarks partly on whether they publish a human baseline (a credibility-adjacent signal, not the credibility rating itself); which human population is the baseline for agent tasks — median developer, senior developer, specialist — since the answer changes the comparison.

---

## Template for new features

```markdown
## F-NN — Title

**Status:** Proposed
**Proposed:** YYYY-MM-DD

Description — what it is, who it's for, why it matters.

**Notes / open questions:**
- ...
```
