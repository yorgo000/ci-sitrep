# Future Features — CI SITREP

A running list of features to build into CI SITREP. Yorgo adds features here; we review them together and decide what to build next. Each feature carries a status: **Proposed** (on the list, not yet started), **In progress**, **Done**, or **Dropped** (decided against, with the reason recorded).

To add a feature: append a new section at the bottom with the next number, status Proposed, today's date, and the description. Do not renumber existing features.

---

## F-01 — Executive dashboard: the undeniable realities at a glance

**Status:** Done (v1, 2026-11-15)
**Proposed:** 2026-11-12
**Built:** 2026-11-15 (Yorgo's pick — "work on graphics" while he reviewed the taxonomy)

A graphic / countdown / visual dashboard that gives high-level executives making service and product decisions an immediate, at-a-glance view of the things that will affect their decisions — the pragmatic facts that get lost in the fluff of the news cycle. The kind of thing elite operators keep their eye on: the actual undeniable realities, not which way the hype is blowing.

**Live at:** https://yorgo000.github.io/ci-sitrep/#executive-dashboard — the first top-level section of the main report page. **Moved into the main page 2026-11-15** (Yorgo's restructure): it was a standalone page at dashboard.html from its build that morning until the restructure that evening; `dashboard.html` now redirects to `index.html#executive-dashboard`, so the link sent out earlier still lands on the dashboard. Linked from the "How to read this" block ("Short on time?").

**Bottom-line strip (built 2026-11-15, Yorgo's pick):** seven at-a-glance items above the countdown, each linked to its evidencing article and carrying its rating — ~47% of code written fully by AI agents (JetBrains), 86% of US financial firms formally use AI (ACA/NSCP), AI patches introduce 11× the vulnerabilities of human patches (Sajadi), verification costs 2.5× (SusVibes), 79% of enterprises run agents in production (SailPoint), 188 documented cases of autonomous AI damaging production (Cyera), and profitability gained from AI ("Insufficient data", no rating, links to the money panel; Yorgo: the absence of data is itself the most significant fact about AI use). **Charted 2026-11-15 (late evening), revised the same evening:** the cards carry graphics where the figure has one, on one colour scheme — rust (#b3543f) is the AI side, blue (#283060) the not-AI side. Pies for the three percentages, number next to the pie with a two-chip legend (~47% AI agents vs human-written; 86% using AI vs not using; 79% running agents vs not running); comparison bars for the multipliers (135 vs 12 vulnerabilities; 2.5× vs 1× review cost — the review is the human side, blue, generation alone rust); the 188 count keeps the big number (no chartable comparison in the report); the profitability item's graphic is a question mark inside a circle. Layout is 3+3+1: six cards in two rows of three, then profitability full-width last (dashed border — 2px muted gray since 2026-11-15 evening, made more pronounced at Yorgo's direction; same background as the other cards). The whole card is one link to its evidencing article (fixed 2026-11-15 evening — a browser test found only the small source name was linked, so clicking the number or chart did nothing; now the card wraps in a single `<a>`, the same pattern as the countdown cards, source name plain text). Every strip card and every countdown card carries a share button in its top-right corner (added 2026-11-15 evening, Yorgo: "very important") — hidden until hover like the article buttons, a sibling of the card's link so clicking it copies the card's URL instead of following the link; strip ids bl-<article-slug>, countdown ids cd-<deadline-slug>. The countdown strip carries a heading in the same label style ("COUNTDOWN"). Data in `dashboard.json` under `bottom_line`; rendered by `build_dashboard.py` (`render_bottom_line`, `render_pie`, `render_compare`, `render_question`), validated like the figures (rating and date optional — the profitability item has neither; chart kinds, values, labels, and bar tones checked).

**What v1 shows (5 panels, 51 figures, 4 deadline countdowns):**

- **AI code share** — bars: ~47% of code written fully by AI agents (JetBrains), 42% of committed code AI-generated or assisted (Sonar, 65% expected by 2027), 75% of new code AI-generated (Google), 97% of organisations use AI coding assistants (Black Duck); finance cut (US-led from 2026-11-15): 86% of US financial firms formally use AI, 1 in 4 experimenting with agentic AI, only 38% formally test outputs (ACA/NSCP, 261 firms); UK comparison: 80% have deployed agents (BoE/FCA).
- **The governance gap** — 13 bars (98% have policies / 47% bypassed them; 79% run agents / 2% have identity tools; 82% can't attribute actions; 88% can't roll back; 35% can't stop a rogue agent; 30% have a documented kill switch — 23% of those never tested), plus 188 documented damage cases and the 109:1 machine-to-human identity ratio; the FCA supervision finding (●●●●) as the Established anchor and the OpenAI 35-second kill switch as the counter-example.
- **Agentic right vs wrong** — SecureVibeBench stacked bar (23.8% correct-and-secure / 23.0% correct-but-exploitable / 53.3% incorrect); A.S.E 2.0 functional 74.0% vs secure 18.4%; CWE-bench ~68% pass@1; SecPRBench recall 32.5–78.1%; BugLedger 45–70% reintroduce, hint 0.35 → 0.71; ThinkingBox 67.16% pass@1 but only 241/507 on all 20 attempts; METR horizon doubles ~every 7 months.
- **Net impact: more code vs more cleanup** — a two-sided ledger (output up: Sonar 42%→65%, DORA throughput; cleanup up: GitClear duplication/churn, DORA stability, Black Duck 581 vulns +107%, Glasswing 175-to-1, Sajadi 11×, ETH Zurich 35.4-pt propagation, FCA outage). No single net number — the ledger says so honestly.
- **Money saved vs lost** — the honest panel: "No credible dollar figure exists yet" as the headline, with the cost multipliers (2.5× review cost, 3.4× vuln rate, 2.74× claimed) and the CMA 10%-of-turnover exposure context.
- **Countdown strip** — California kill-switch recommendations (Mon 16 Nov 2026), TPRM comments (Wed 16 Dec 2026), FCA CP26/38 (Thu 24 Dec 2026), OSFI E-23 (1 May 2027); days-remaining computed in the browser at load.

**Design (as built):**

- `dashboard.json` is the single source of truth (figures with value, label, source, source note, rating, date, and a link to the report article that evidences it); `_tools/build_dashboard.py` renders the section and `build_html.py` imports it, embedding the panels in `index.html` as H3s under the section's H2 ("Executive dashboard"), with the dashboard's CSS and countdown JS inserted after the template format step. Pure CSS bars and stat cards — no chart library, no backend, no cost.
- Every figure carries its confidence rating (dots + word) and links to the report article behind it — the article's runtime id, so the reader lands on the article expanded and its Source line takes them to the primary source. Six figures carry an "also" link to a second evidencing article in another subsection (SecureVibeBench, A.S.E ×3, BugLedger, CodeRabbit). The three §3.6 figures (ThinkingBox ×2, METR) still link to the section anchor: §3.6 is prose, not articles. The generator validates every figure (required fields, rating in the four levels, bar values 0–100, link anchors exist in index.html or among the computed article ids — `compute_article_ids()` replicates the share JS's slugify + uniqueId) and exits 1 on a bad entry.
- Panels start open (the template collapses every heading; the dashboard's JS re-opens them); breadcrumbs removed as noise on a one-screen page; share buttons on panel headings work as on the other pages.
- Panel order is editorial (audience-first): code share, governance gap, right vs wrong, net impact, money.

**Maintenance:** a DASHBOARD step in the daily watch cron (added 2026-11-15) — when a new article moves a headline number, update dashboard.json and regenerate index.html (which embeds and validates the dashboard); when a What-we're-watching date lands, update the deadlines list the same day. Never add a figure the report doesn't evidence; never invent a dollar figure for the money panel.

**Open questions (from the proposal, resolved):** cuts — a UK finance-sector cut exists (BoE/FCA) plus HK large firms; nothing below sector level yet. Cadence — updated with the daily watch when a headline number moves (the inventory's weekly-snapshot suggestion was superseded: the data file carries dates per figure, so either cadence works mechanically, and the daily watch already owns the numbers).

**Follow-ups (not in v1):** trend lines (the data file stores each figure with its date, so a second data round can draw the slope); verify.py dashboard checks — partly closed 2026-11-15, when the deep-link change made verify.py's anchor check accept the computed article ids, so the dashboard's links are covered by the same gate (dashboard.html is now a redirect, not a page to check); a money panel with real dollar evidence when it exists.

**Browser test (live, 2026-11-15):** 5 checks — page loads with the "As of Sunday, November 15, 2026" banner and countdown strip ("tomorrow", "in 31 days", "in 39 days", "in 167 days"); all five panels open on load with the ~47% bar, the SecureVibeBench stacked bar (23.8/23.0/53.3), and the money panel's "No credible dollar figure exists yet" statement confirmed; panel share button shows "Copied"; sidebar navigation both ways works. One defect found: a dashboard figure's source link landed on the right report section but left it collapsed — the report's anchor handler only opened ANCESTOR sections, never the target heading itself. Fixed the same day in both generators (expandForAnchor now also un-collapses the target heading itself), all 8 pages regenerated and pushed. The first re-test failed on a stale CDN copy minutes after deploy; the second re-test passed both checks (the §1.1 link opens §1.1 expanded with all six articles visible; the State-of-the-market link opens §3.4.3 expanded). Lesson: browser re-tests right after a deploy can hit a stale CDN edge — use a cache-busting query (?fresh=...) to force a fresh fetch. Note: view-source: URLs cannot be opened in the cloud browser, so a source check has to go through curl instead.

**Browser test, restructure + deep links (live, 2026-11-15 evening):** 10 checks — 9 passed first run: row layout (As-of + Sections controls, search, How-to-read right-justified), the two top-level sections in order with the countdown strip reading exactly as expected, sidebar TOC and masthead nav order, all three deep links (JetBrains → the adoption article expanded; BugLedger → its §1.6 article expanded and "also in §2.1" → the §2.1 article expanded; ThinkingBox → §3.6, the expected section-anchor exception), search returning 4 results for "TPRM", the dashboard.html redirect, and the theses page opening all-collapsed with its own Sections control working. One defect: "Collapse all" closed the two top-level sections too, leaving only two bare headings — the handler toggled every heading with no exception for the always-open ones. Fixed the same evening in both copies of build_html.py (Collapse all now skips the top-level sections, the three front-page sections, and the dashboard panels — i.e. it returns the page to its initial state; Expand all still opens everything), regenerated, verified 52/0, pushed, live-verified, and re-tested 4/4 passing.

## F-02 — Single database, filtered sitreps (the split, done right)

**Status:** In progress — first database file exists (2026-11-17); tags and the filter/query layer remain
**Proposed:** 2026-11-13

The long-term product architecture. One database of all CI news gathered each day, across all industries. Every piece of data is collected, rated, vetted, tagged, summarised, and organised **once**. Sitreps are then produced by filtering:

- **Filter by industry** → a specific industry's sitrep (finance, healthcare, manufacturing, etc.).
- **Combine filters** → intersection reports (e.g. CIC + finance, code + healthcare).
- **The same piece of information sells on multiple sitreps** — no duplication, no maintenance of parallel copies.

This resolves the split question: separate sitreps become *views* on one database, not separate products to maintain. The tagging taxonomy (subject, type, confidence, severity, jurisdiction, source-date) is the filter mechanism — it already exists in draft. **First database file (2026-11-17):** data/findings.json — structured storage for articles + ratings, generated by _tools/export_findings.py from SYNTHESIZED.md, GLOSSARY.md, and dashboard.json, refreshed by the daily watch on every publish (81 articles with ratings, source URLs, and voiceover text, plus what's-new, glossary, deadlines, and gauges). What remains: tags on the records, the filter/query layer, and per-filter rendering; the taxonomy verdict is still pending.

**Design notes (to be refined):**

- The current SYNTHESIZED.md is the single source of truth in Markdown form; the database is its structured successor.
- Intersection reports (CIC × finance) are the most commercially interesting filter — they serve the buyer who needs one slice, not the whole report.
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
- **Database schema.** What fields per item — the tagging taxonomy (subject, type, confidence, severity, jurisdiction, source-date) is the starting point, but intake may need more.
- **The production interface.** What does the operator see and choose when producing a sitrep? How are filter intersections specified?
- **Relationship to the current daily watch.** Does the daily watch cron become the radar, or is the radar something broader that the watch feeds into?

## F-05 — Situation at hand (front-page synthesis)

**Status:** Done
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)
**Built:** 2026-11-14

A short synthesis — 2–4 sentences — at the very top of the report, above "New in the last 7 days", giving a new reader the macro narrative before the granular updates: where AI code generation and agentic deployment stand, where governance lags, and where regulation is heading. The executive reader's first paragraph.

**Design notes (decided 2026-11-14):**

- Evidence-grounded in the report's own findings (the 45% flaw rate, the governance gap, the regulatory timeline) — no generic marketing lines.
- A named front-page section (H2), starting OPEN like "New in the last 7 days" and "What we're watching", sharing the tinted navy panel and the de-emphasized meta-heading style.
- Maintenance rule: the daily watch revises it when a material shift lands; it must never go stale, or it contradicts the "up to date" promise. Recorded in RULES.md and the daily watch cron.
- This is the cheap version of F-01 — the dashboard is the fuller, visual version, later.

## F-06 — Monthly summary ("This month")

**Status:** Proposed
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)

A monthly synthesis below "New in the last 7 days": the 3–4 biggest shifts of the month, so a reader checking in monthly instantly grasps the momentum without parsing individual tactical updates or digging through the Archive. Monthly, not quarterly — this field moves too fast for a quarterly cadence.

**Design notes:**

- First edition at the end of November 2026 (a strong first month: the governance gap, the TPRM extension, FCA supervision insights, the Glasswing 175-to-1 finding, the BoE/FCA survey).
- Natural raw material for the weekly newsletter (which synthesizes the week; this synthesizes the month).
- Open question: maintained by a month-end step in the daily watch cron, or a separate monthly job?

## F-07 — Plain-English tags in "New in the last 7 days"

**Status:** Done
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)
**Built:** 2026-11-14

Replace the academic "(subject 1/2/3)" parentheticals in the "New in the last 7 days" entries with plain tags — [Pre-commit], [In codebase], [Agentic]. The section names are already plain English; the parentheticals were the only place the numbered-subject language reached the public page.

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
- **Reworked 2026-11-15 (Yorgo):** the nav link is gone, replaced by a small **Contact section in the masthead** in its place (after the nav, before the confidence legend), with two mailto addresses: errors, omissions, and feature requests go to ci-sitrep@confluence1.com; working with Confluence<1> goes to hello@confluence1.com (picked for the classy, no-sales-connotation feel — sales@ was too transactional, clients@ reads as existing clients; the catch-all routes to Yorgo so the address can change in one line). The About page's Contact section lists both addresses too, in the same words.
- The real conversion engine remains the newsletter funnel (subscribe → site → value-add → Confluence<1> service), which still needs Yorgo's yes to start.

## F-10 — Business Impact & Risk module in each pillar

**Status:** Dropped
**Proposed:** 2026-11-14 (external reviewer feedback; assessed same day)

**Why dropped:** the gap the reviewer identified is real (the report is technical, not P&L-framed), but the fix is the wrong shape. A Business Impact module in each of the three pillars would be either vague or duplicative — the F-01 data inventory already found the money panel is the thinnest, with no credible dollar figure, so sourced business-impact claims barely exist yet. The business layer belongs in F-01 (the dashboard, sourced numbers only) and in the newsletter (plain language for P&L readers), both already planned. F-05 (Situation at hand) carries the macro business framing in the meantime.

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

A way for readers to ask questions and get answers grounded in the report. Assessment (2026-11-14): very doable, but a real project — days to a week for a solid v1, not an afternoon. Three pieces: (1) retrieval — finding the right passages for a question (search + ranking; F-13 is the foundation); (2) a language model to compose the answer; (3) a backend — GitHub Pages cannot run server code, so it needs a small serverless function plus an LLM API key (cost small, cents per question at this scale). The plumbing is standard; the hard part is editorial, not technical: answers must cite the report's articles, respect the confidence ratings, and say "not in the report" when the answer isn't there — otherwise it becomes a hallucination machine on top of a confidence-rated knowledge base.

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

Let readers save items to a personal reading list and come back to them later — to read, or to share from there. An executive skims the report or the dashboard, saves the three findings that matter to their P&L, and reads them properly later instead of losing them in the 60-article report.

**Storage, in two stages:**

- **V1 — browser/device-local.** The list lives in the reader's own browser (localStorage): no backend, no account, works on GitHub Pages as-is. The reader's list stays on that device.
- **V2 — user database.** Once a user DB exists (the membership/commercialization work), the list is saved in perpetuity, tied to the account, and follows the reader across devices. V1 should offer to import the local list into the account when V2 arrives.

**Design notes:**

- It builds on the share infrastructure: every article, paragraph, table, and heading already has a deterministic runtime id and a stable anchor URL that opens expanded. A list entry stores the anchor URL, the item's title, its section, its confidence rating, and the date saved.
- The "add to reading list" control sits beside the share button on each item (articles at minimum; the same control works on the other shareable units since they share the anchor machinery).
- The list itself is a view the reader returns to (own page, linked from the masthead nav): each entry links back to its anchor in the report (opens expanded) and carries its share button, so sharing from the list works exactly like sharing from the report.
- **Open questions:** the list's home — own page vs a panel; ordering (most recent first, or report order); remove/clear; what happens when a saved article is superseded and archived — its anchor may disappear from the live report, so stale entries need graceful handling (link to the Archive, or a note that the item moved); local-storage limits for heavy readers.

## F-17 — Human baselines: every CI figure compared to human performance

**Status:** In progress — baseline audit and dedicated CI vs EI page built 2026-11-17; per-figure baselines in articles and dashboard remain
**Proposed:** 2026-11-15 (Yorgo — "we need to compare all the CI-based code and agent performance to humans — it's meaningless on its own for an executive")

A benchmark score on its own tells an executive nothing: 74.0 on A.S.E, 67% on ThinkingBox, 45–70% on BugLedger — good or bad? The answer only exists against the human baseline for the same task. Every CI performance figure in the report and the dashboard should carry its human comparison next to it, wherever one exists — and where none exists, say so plainly (a gap in the evidence, not a number to guess).

**Already in the report, in scattered form (the seed of this feature):**

- CodeRabbit: CI code carries 2.74× the vulnerabilities of human-written code for equivalent tasks (§1.1, §2.1) — vendor claim, ●○○○.
- Sajadi et al. (v4, Nov 2026): on SWE-bench, a standalone LLM's patches introduced 135 manually confirmed vulnerabilities against 12 for developer patches on the same issues (§1.6) — preprint (arXiv v4), not peer-reviewed — the strongest human-comparison evidence in the report. (This entry wrongly called it peer-reviewed until 2026-11-17.)
- METR time horizons (§3.6): agent task-completion time vs human task time on the same tasks — the agent-performance equivalent.
- SusVibes re-run (§1.6): human review as the control that reduces the vulnerability share — the human as the intervention, not just the baseline.
- GitClear (§2.1): the maintainability gap, measured against human-authored code's churn patterns.

**What F-17 adds — making it systematic:**

- **A baseline audit.** Walk every performance figure in the report and the dashboard and record, per figure, whether a human baseline exists in the cited source (same task, same metric) or not. The audit itself is a finding: most benchmarks publish no human baseline at all, and that absence is worth stating.
- **Baseline next to the figure.** Where a baseline exists, it travels with the figure — in the article (a bullet: "human baseline on the same task: X"), and in the dashboard (a second value or a "vs human" line on the figure). The comparison must be same-task, same-metric; a human number from a different task is not a baseline.
- **No baseline, no guess.** Where the source publishes no human comparison, the figure carries a "no human baseline published" note rather than an invented one. Over time this becomes a pressure point: benchmarks that publish baselines are more useful to executives, and the report can say so.
- **A human-baseline view.** A dedicated view — every CI-vs-human comparison in one place. Built 2026-11-17 as the CI vs EI page (see below), ahead of the per-figure baselines: Yorgo approved the sequence audit-first-then-page on 17 Nov, promoting F-17 to the organising principle for the product (the "ATAK" view — ATAK is design analogy only; the view is named "CI vs EI").

**Built 2026-11-17 (audit + page):** the baseline audit (`~/workspace/goals/watch-subjects-synthesized-state-of-the-art/hidden_files/f17-baseline-audit.md`, working file, not public) classified all 42 performance figures in the report and dashboard: **3 complete pairs** (Sajadi 135 vs 12, Sajadi GPT-5.4 nano 3 vs 2, CodeRabbit 2.74× — all error-rate, all Development), **12 partials**, **27 gaps**; Operations has no complete pair. The audit's headline finding: the evidence base measures CI exhaustively and humans almost never, on the same task with the same metric. The page (`CI-VS-EI.md` → `ci-vs-ei.html`, via `build_page.py`) presents the pairs, partials (with their caveat), and gaps (explicitly, as gaps) in three family sections — Development, Operations, Business-composite — with every figure carrying its confidence rating and linking to its evidencing article, versioned and dated with a Changes log at the bottom. Tables use the pair-table pattern (CI column rust, EI column navy — the dashboard's colour meaning; see RULES.md §4). Linked from the masthead nav after Glossary. Glossary gained EI, EII, EIC entries (90 terms). **Still to do:** per-figure baselines in articles (a "human baseline on the same task" bullet) and in the dashboard (a second value or "vs human" line) — and a daily-watch step to maintain the page and audit when a new article publishes a human baseline.

**Open questions:** how the dashboard shows a baseline without doubling the figure count (second value, ratio, or a toggle); whether to score benchmarks partly on whether they publish a human baseline (a confidence-adjacent signal, not the confidence rating itself); which human population is the baseline for agent tasks — median developer, senior developer, specialist — since the answer changes the comparison.

---

## F-18 — Site analytics (GoatCounter)

**Status:** Done 2026-11-16
**Proposed:** 2026-11-16 (Yorgo — "is there any type of analytics I can look at for the sitrep? ... other than me, I wonder if anyone else has looked at it")

GitHub Pages has no built-in analytics, so the site has counted nothing since it went live — whatever is added starts counting from installation day and cannot look backward. GoatCounter chosen 2026-11-16 (free hosted tier, cookieless, no consent banner, ~3.5KB script; Plausible at $9/mo was the alternative). It answers the question asked: pageviews and unique visitors per page, referrers, browsers/devices, countries.

**Built 2026-11-16:** `_tools/site_config.py` holds the single `GOATCOUNTER_CODE` constant (`"ci-sitrep"`, account created by Yorgo, site domain yorgo000.github.io) and `goatcounter_snippet()`; build_html.py and build_page.py insert the snippet before `</head>` on every generated page (index + all six sub-pages; dashboard.html is a redirect and carries none). All seven pages rebuilt, verify.py passed, pushed, and confirmed live (snippet on index + about on first check). Own-visit exclusion is by IP in GoatCounter Settings → Main ("Ignore these IP addresses"); his IP is at ifconfig.me, and the dual-WAN (Spectrum + T-Mobile failover) means it can change, so both addresses may need listing. **Bug found and fixed during the build:** the archive-page rebuild command in the daily watch cron had a one-character sed error that ate the `]` of the append-only-report link, leaving raw malformed text on the live archive page; the cron command is fixed (replacement now `](archive/...` instead of `(archive/...`) and the archive page now carries a working link. **API connected 2026-11-16** (custom.goatcounter connector, Bearer key, helper `bin/goatcounter.py`): totals, per-path hits, toprefs/locations/browsers all verified working; first pull ~14:50 showed 0 visitors (counting started ~14:40, only real browser loads count). Connector doc at `~/workspace/custom-connectors/custom.goatcounter/CONNECTOR.md`.

**Notes / open questions:**
- The repo's Insights → Traffic page (repo visits + clones, last 14 days) is the only pre-analytics signal; the API token cannot read it (403), so Yorgo checks it himself in the browser.
- When rebuilding sub-pages, pass the proper title argument (build_page.py takes `[title]`; the published about.html carries "About — CI SITREP"). The GoatCounter rebuild also cleared the pre-rename `'new-this-week'` string from the sub-pages' JS (dead code there, but now consistent).

---

## F-19 — Live channel: CI SITREP on YouTube, CNBC-style

**Status:** In progress — export, scene page, and review table built 2026-11-17; OBS setup + live enablement + test streams remain
**Proposed:** 2026-11-17 (Yorgo)
**Decided 2026-11-17 (Yorgo):** channel name **CI SITREP**; **24/7**, global audience; **AI voiceover**; MVP on a **local machine (beta)** — work out the kinks and gauge response while the server version is built; **no clips** for now — ambient background footage (flowers, mountains, sailboats, cities, chip fabrication — his own photos or licensed stock), dimmed behind the tiles, so the picture isn't stiff; **one channel first**. Voice/vibe: **elite operators, brass tacks, ATAK**.

**Built 2026-11-17:** the findings export (first F-02 database file — data/findings.json, 81 articles + what's-new + glossary + deadlines + gauges, regenerated by _tools/export_findings.py on every publish), the broadcast scene page (youtube/scene.html — top band with clocks + next-deadline chip, main finding cycler at 15s with a 75s Situation at hand opener, right-rail gauges always visible, glossary scroll, what's-new ticker, voiceover hook via `ci-sitrep-slide` events), and the review table (youtube/review.html — all 81 findings, searchable, filterable, deep-linked to the report). Visually verified in a real browser the same evening (gauges measured proportional, finding block centered, rail fit fixed after a spacing pass). Remaining for the MVP: OBS setup + YouTube live enablement (24h wait) + test streams on Yorgo's machine; the AI voiceover driver (listens for the slide events) is not yet wired up.

A live YouTube channel in the CNBC style: news and the various dashboards in rotation, as an always-on broadcast of the sitrep. Sections in rotation: facts from the database; a scrolling ticker of new facts as they come in; glossary/terminology definitions; and a set of gauges showing how CI vs EI stands on the critical factors (placement TBD — top, side, or its own scene). At a later phase, clips from videos we have filtered and rated. Eventually, multiple channels specialized for particular sectors, industries, countries — the F-02 filter model applied to broadcast: one database, one channel per filter. ("Vertical" = one industry/topic slice of the same database — Code & Finance is the current one; a second channel could be e.g. CI in healthcare, CI in manufacturing, or a country slice.)

**Phases:**

- **Phase 1 — one channel, data only, local-machine MVP.** Rotating scenes rendered from data the site already has: dashboard figures (dashboard.json), the new-facts ticker ("New in the last 7 days"), glossary definitions (GLOSSARY.md), and the CI-vs-EI gauges. No video clips yet — ambient background footage only, dimmed behind the tiles. **Layout (Yorgo's spitball, 2026-11-17):** a main section cycling through all the vetted findings (every rating level, rating shown on each); a second section scrolling the applicable glossary terms; the what's-new items in a ticker; and the gauges always visible somewhere on screen. **AI voiceover** reads the main finding as it appears. The MVP runs on a local machine (OBS) in test sessions to work out the kinks and gauge response; the server version is the 24/7 production build. Ship with what we have and improve gradually — the gauges start with the real CI-vs-EI pairs we have (Sajadi 135 vs 12, CodeRabbit 2.74×, SusVibes 2.5×, METR horizons) and grow as the F-17 baseline audit fills in pairs.
- **Phase 2 — curated clips.** Clips from videos we have filtered and rated, in rotation with the data scenes. Rights policy needed before this phase: only our own content and licensed content — re-streaming other creators' videos risks Content ID claims or strikes regardless of fair-use arguments, and YouTube enforces automatically.
- **Phase 3 — multiple channels.** One channel per vertical (sector / industry / country), each a filter over the same database. Each channel needs its own stream, encoder capacity, and YouTube channel; the render pipeline is shared.

**How it works (feasibility, assessed 2026-11-17):** feasible. YouTube Live takes a standard RTMP stream; the channel is a render pipeline, not a person at a desk. Two tracks, in the order Yorgo chose: (a) **MVP — OBS Studio on a local machine**, scenes as browser sources (web pages fed by sitrep data, rotated on a timer) — fastest to build, days to ~2 weeks, run in test sessions; (b) **production — a headless pipeline** (headless Chromium + ffmpeg compositing + RTMP) on a small server — more build time (1–3 weeks), more reliable, 24/7, and the one that scales to multiple channels. Either way the site already owns the hard part: the data is structured (dashboard.json, SYNTHESIZED.md, GLOSSARY.md) and refreshed daily by the watch. Rough running cost: a VPS able to encode 720p30 is ~$20–50/mo, 1080p ~$50–100/mo; YouTube itself is free; the main cost is build time. YouTube requires a verified channel and a 24-hour wait the first time live streaming is enabled, and no live strikes. (Plain-English glosses: an **encoder** is the software that turns the picture on a screen into a video stream YouTube can broadcast — OBS includes one, so the MVP needs no separate piece; **motion design** is how things move on screen — tiles sliding in, numbers ticking, the ticker scrolling — the difference between a slideshow and a TV channel.)

**The hard parts (not the streaming):** (1) the always-on machine and monitoring — a dead stream is worse than no stream, so the encoder needs auto-reconnect and alerting (a production concern; the MVP's test sessions don't need it); (2) motion-design quality — CNBC-grade rotation is real design work, and the design-editor standard applies; (3) freshness honesty — the data refreshes daily, so the ticker repeats within a day: the channel is right-time, not a news wire, and the rotation must be designed for that (accepted 2026-11-17 — ship with what we have, improve gradually); (4) clip rights (phase 2 — see above); (5) the gauges depend on F-17/ATAK data — the CI-vs-EI pairs must exist before the gauges mean anything, so phase 1 ships with the pairs we have and grows as the baseline audit fills them in.

**Dependencies:** F-02 (single database — the channel is another renderer over it); F-17 / ATAK page (the gauges); the daily watch (freshness); the glossary (definitions feed).

**Notes / open questions:**
- ~~Channel name~~ — CI SITREP (decided 2026-11-17). ~~Broadcast hours~~ — 24/7 (decided; the local MVP runs test sessions, 24/7 comes with the server build). ~~Audio~~ — AI voiceover, reading the main finding as it appears (decided 2026-11-17).
- ~~Layout details~~ — settled 2026-11-17 in the built scene: gauges in the right rail, countdown as a top-band chip, each cycle opens with the Situation at hand summary, 15s per finding (81 findings ≈ a 20-minute cycle).
- Background footage source: his own photos (he shoots) vs licensed stock (Pexels/Coverr-style, free for commercial use). Either is rights-clean; his own photos make it unmistakably his.
- Voiceover voice and pace; whether the voice also reads the Situation at hand summary.
- Which vertical second after Code & Finance, and does each channel get its own YouTube channel (brand accounts) or one channel with playlists?
- Success metric: not views — this is a leave-it-on-the-wall credibility surface and a reason to visit the site, not a viral play.

---

## F-20 — Tagline: "the information you need to make the good calls"

**Status:** Proposed
**Proposed:** 2026-11-17 (Yorgo)

A single promise line for all CI SITREP materials — site, channel, newsletter, explainer. Draft wording (Yorgo — "or something along those lines"): "we give you the information you need to make the good calls". It states the product's job in one sentence: the reader is a person with decisions to make, and the sitrep exists so those decisions are well informed. Distinct from the descriptive tagline ("Created Intelligence in code and finance — as of today"), which says what the report covers; this one says what it does for the reader. It fits the elite-operators / brass-tacks / ATAK voice and the "Right-Time Situational Awareness Tool" framing (item 4 of the 2026-11-17 strategy discussion, pending).

**Notes / open questions:**
- Wording to settle: the draft is Yorgo's; candidates to weigh alongside it — "the information behind the good calls", "know enough to call it right". He picks the final wording.
- Placement: masthead under the existing tagline? Channel intro/outro? Newsletter header? Decide per material once the wording is settled — one line, many placements.
- Voice: the line speaks as Confluence<1> ("we give you"); check it sits comfortably next to the "by Confluence<1>" byline and the report's otherwise impersonal tone.

---

## F-21 — About: sell the making of it

**Status:** Done 2026-11-17 (About section live; LinkedIn post drafted, awaiting Yorgo's verdict)
**Proposed:** 2026-11-17 (Yorgo)

The About page needs to sell the work behind the sitrep: how many sources, how many agents, how long it takes, how much expertise goes into scouring the landscape, collecting the data, filtering it, distilling it, vetting and rating it — and then what it's used for: advising the finance industry on critical matters, building critical systems. The reader has to feel two things: (a) this takes a lot to put together, (b) it's designed to be useful to elite operators. This is the evidence behind the F-20 promise line ("the information you need to make the good calls") — the promise says what it does for the reader, this says what it costs to make.

**What it draws on (all real, all computed — nothing invented):**

- The Self-Audit page already computes the raw material: article/source/link counts, the confidence distribution, and the per-run source-review funnel (audit_log.csv — e.g. the Tuesday 2026-11-17 run reviewed 55 sources to add 5 articles). The About numbers must come from the same computed source so they can't drift from the audit.
- The pipeline: the daily watch (04:30 ET run + 08:00 catch-up), the agent team (5 CII roles: Barnaby + 3 baseline researchers + the daily watch worker; the 08:00 catch-up worker joins Nov 18, making 6), the vetting-on-the-fly rule (F-04), the 53-check verification before every push, the design-editor review.
- The expertise: decades building mission-critical systems for finance (already in About — Bernstein SMA systems, UN Situation Room, hedge funds, MGAs).
- What it's for: advising finance on critical matters, building critical systems — the Confluence<1> services the sitrep feeds.

**First application — LinkedIn launch post (Yorgo's skeleton, 2026-11-17):** "X sources, Y agents, Z years of critical systems in finance, [metric] distillation, [metric] fact-checking/confidence-rating, [metric] [something required to produce this] — so that we only need to monitor one CI SITREP — now we're letting you in on it too". Draft in chat 2026-11-17 (revised same day); Yorgo posts it himself (no LinkedIn connector). **Sources — two numbers, don't conflate them:** 212 = sources *reviewed* (opened and evaluated, per the audit-log definition) in five days of runs since tracking began 12 Nov; what we *quote* is 195 source links from 61 unique domains. **The question to expect:** "how did you decide that's all the sources to look at?" — answer: there is no fixed list; the radar runs fresh every morning across the three subjects (search + the report's existing source base), everything found is evaluated against the bar (would it change our offerings), vetting happens on the fly at intake (F-04), and reader suggestions are open (F-03). The About page must carry this methodology answer. **Agents — count every CII used to bring it to this point (Yorgo, 2026-11-17; call them "CII's (aka AI agents)"):** 5 roles — Barnaby (editor/assembler/publisher) + 3 baseline research agents (Nov 9, one per subject) + the daily watch worker (04:30 run). CORRECTION 2026-11-17: an earlier draft of this entry said a coordinator + 3 researchers built the baseline — wrong; it was three researchers assembled by Barnaby, no separate coordinator (the coordinator is a capability, not used that day). The morning catch-up worker (08:00) joins from Nov 18 → 6. Count is roles, not run-instances (each daily run is a fresh instance; counting instances would inflate meaninglessly). **Years — cumulative experience of the editing team:** 39 now (Yorgo alone: 9 Bernstein + 30 Confluence<1>, 1993–96 gap uncounted); grows with Archimedes people (partnership planned, not yet established — never claim them on the team yet) and hired recognized experts per vertical as it grows.

**Quotable inventory (verified 2026-11-17, all from the Self-Audit page / audit log / direct counts):** 212 sources reviewed in 5 days; 16.5% acceptance (35 added, 3 updated); 81 findings, every one confidence-rated (43% Established or Corroborated); 53 automated checks before every publish; 195 source links, every one verified live; 442 total external links; 163 unique URLs; 61 unique domains cited; 85 glossary terms (never removed); 53 dashboard figures; 17 superseded items dated and archived; 46 items in the 7-day what's-new window; 4 deadlines tracked; daily 04:30 ET run + 08:00 catch-up, 7 days a week.

**Notes / open questions:**
- Placement: a section in About, or a standalone "How this is made" page linked from About? About keeps it where a skeptic looks; a separate page lets the pipeline breathe.
- Which numbers: per-run (55 sources reviewed Tuesday) vs cumulative (sources reviewed since launch, articles, glossary terms)? Cumulative is the weight; per-run is the tempo. Probably both, each labeled.
- Keep it honest: every number computed from the audit log or the generators, refreshed with the daily watch — no hand-written counts, no rounded-up claims.
- Tone: brass tacks, not a brochure. The elite-operator reader respects the work when the numbers are specific and checkable.

---

## F-22 — Corrections page

**Status:** Done 2026-11-19
**Proposed:** 2026-11-19 (Yorgo)

A public Corrections page (`CORRECTIONS.md` → `corrections.html`): errors and omissions corrected in public, newest first, one line each — date, what was wrong or missing, what it is now, with a link to the corrected article where one exists. In the masthead nav after Self-Audit (both are accountability pages); linked from the About page's Contact section. The daily watch adds an entry as part of the same publish that lands a fix (RULES.md §2); entries are never removed. Launched with five entries: the Strands omission and the SailPoint/PAN 109:1 misattribution (both 19 Nov, both found by Yorgo), and the Black Duck 67%, CodeRabbit "up to 2.74×", and FCA Thu 24 Dec corrections (18 Nov).

---

## F-23 — Grouped "New in the last 7 days"

**Status:** Proposed
**Proposed:** 2026-11-20 (Yorgo — from the 2026-11-18 rethink; the section keeps growing)

"New in the last 7 days" is humongous — 71 entries as of 20 Nov 2026 (46 on 18 Nov) — and will only grow. A flat list that long stops being scannable: the reader can't see what's in it without scrolling the whole thing. Group the entries under collapsible headings that open to the article, categorized.

**Grouping scheme — Yorgo's pick (open):**

- **By type of change** — new number / new rule / incident / new tool / research / lawsuit. Reuses the taxonomy's type dimension, already on every article. (Barnaby's proposal, 2026-11-18.)
- **By report section** — Pre-commit / In codebase / Agentic. Tags already exist on every entry; zero new data. Lopsided: Agentic held 30 of 46 entries on 18 Nov.
- **By dashboard panel** — AI code share / The governance gap / Agentic right vs wrong / Net impact / Money saved vs lost. Organizes by what the news means, the most executive cut — but no article-to-panel mapping exists in the data (only the 62 dashboard figures have panel homes), so it needs editorial mapping per entry, maintained on every watch run, and some entries fit no panel or several. (Yorgo, 2026-11-20.)
- **By consequence** — act / watch / know. Most executive, most editorial.

**Structure — Yorgo's pick (open):** entries expand to the article in place (generator can do it; costs id handling + page weight) or link straight to the article anchor (lighter; entries currently link to sections, not articles).

**Notes / open questions:**

- The section is also the YouTube ticker's source (F-19) and the findings export's `whats_new` — grouping is a display change on the report page; the export keeps the flat list unless the channel wants groups too.
- Entry count keeps climbing with the daily watch — whatever the scheme, it must absorb new entries without rework.

---

## F-24 — Subset / superset choice on multi-select filters

**Status:** Proposed
**Proposed:** 2026-11-20 (Yorgo)

Today the filter panel matches AND across dimensions and union (ANY) within a dimension: an article matches if any of its values equals any selected value — and Type is the only multi-choice dimension. When a reader selects multiple values in a multi-select dimension — industries, sectors, and any other multi-select — the reader must choose the match mode: **subset** (intersection — the article must carry ALL selected values) or **superset** (union — the article carries ANY selected value, today's behaviour). No silent default: the choice is required when two or more values are selected.

**Notes / open questions:**

- Per-dimension toggle (each multi-select group gets its own subset/superset control) or one global toggle for the whole panel? Per-dimension is the natural reading; confirm at build.
- What the panel shows before the reader chooses: the multi-selection doesn't filter until a mode is picked, or the mode control appears with the second selection. Decide at build.
- Label wording: "subset" / "superset" are the spec terms; the UI may want plainer labels ("match all" / "match any") — decide at build.
- Tag caps bound intersection: set dimensions carry at most 2 values per article (pnl-impact 3), so an intersection over more values than the cap can match nothing — the UI should say so rather than show an empty result silently.
- Sector is not a filter today (removed 2026-11-18; tags kept in data) — sector multi-select arrives with the sector filter's return, under the same rule.
- Dashboard figures inherit their evidencing article's tags, so the same rule governs tiles.

---

## F-25 — Forecasting: best-fit curves and "when does it hit X"

**Status:** Proposed
**Proposed:** 2026-11-21 (Yorgo)

For every report metric that exists as a time series, fit a curve to the verified points and project it forward: not just the sparkline of where a number has been, but a fitted curve showing where it is going and by when it crosses a threshold — e.g. AI-written code share: 47% today, 80% by when. Premium-subscription material: the sparkline stays free; the fitted curve, the milestone dates, and the fit quality sit behind the premium tier (tier split to be decided — no signup or paywall exists today).

**Candidate inventory (2026-11-21):** only 4 series exist in `dashboard-history.json`; the 2026-11-18 audit found the other 55 panel figures have no verified repeated measurement. Of the 4: ACA/NSCP AI use (45→71→86%, 3 annual points, same survey — the best candidate); Google AI-code share (4 points, but the series is CLOSED — Pichai discontinued the metric Oct 2026 — and the first two points are lower bounds, so a forecast would be unverifiable); Veracode flaw rate (3 points inside 7 months — too short a span to extrapolate years); PAN identity ratio (2 points from different samples — fails any bar). The JetBrains 47% example is a single point in the report — historical points from the 2023–2025 surveys need researching before any curve exists. The held S-4/S-5/S-6 series (GitClear, Black Duck 581, VulnCheck) are further candidates once shipped.

**Method (proposed):** parametric curve fits, not ML — with 3–4 points a machine-learning model is meaningless. Logistic (S-curve) for bounded shares (0–100%), exponential or linear for unbounded ratios/counts. A projection is published only when the series clears the bar below; it renders as a dashed extension of the sparkline with an uncertainty band, labelled a projection, never a finding, and re-fits automatically as the daily watch appends points.

**Notes / open questions:**

- Minimum bar for publishing a projection — proposed: ≥4 verified points from the same source and method, spanning ≥1 year. With 3 points a 2-parameter fit is nearly interpolation and no error estimate is possible. (Demo fits 2026-11-21, illustrative only, published nowhere: ACA/NSCP logistic fit puts 90% at ~Apr 2027 and 95% at ~Mar 2028; Google's fit puts 80% at ~Aug 2026 — already past, unverifiable because the series is closed; Veracode's puts 30% at ~Sep 2027.)
- Closed series (Google): forecast with a flag, or exclude? Proposed: exclude — a projection the source itself stopped measuring can't be checked.
- Mixed-source series: never fit across sources — a JetBrains point and a Stack Overflow point are different measurements. The historical-points research must find same-survey points.
- Premium split: what stays free (sparkline + headline milestone date?) vs premium (full curve, bands, fit quality, all series)? No paywall or signup exists today — the premium tier itself is a separate decision.
- Confidence treatment: projections are not findings — they need their own rating or a fixed ●○○○ Claimed treatment, decided at build. Never a dashboard figure without the projection label.
- Depends on: the historical-points audit (new research — same-source points for the candidate metrics, starting with JetBrains) and F-02 (the database stores dated values, which is what makes re-fitting automatic).

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
