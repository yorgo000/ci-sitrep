# Future Features — CI Sitrep

A running list of features to build into CI Sitrep. Yorgo adds features here; we review them together and decide what to build next. Each feature carries a status: **Proposed** (on the list, not yet started), **In progress**, **Done**, or **Dropped** (decided against, with the reason recorded).

To add a feature: append a new section at the bottom with the next number, status Proposed, today's date, and the description. Do not renumber existing features.

---

## F-01 — Executive dashboard: the undeniable realities at a glance

**Status:** Proposed
**Proposed:** 2026-11-12

A graphic / countdown / visual dashboard that gives high-level executives making service and product decisions an immediate, at-a-glance view of the things that will affect their decisions — the pragmatic facts that get lost in the fluff of the news cycle. The kind of thing the special forces keep their eye on: the actual undeniable realities, not which way the hype is blowing.

**What it should show:**

- **AI code share:** what percentage of code is produced via AI — and how that share is trending.
- **AI code impact on development:** more code is being produced, but with bigger technical debt and more time spent cleaning it up. Net gain or net loss? Quantified where the evidence supports it.
- **Breakdowns by industry, institution, company, sector** — where the data exists to support them.
- **Agentic performance:** how much agents are getting right, how much they're getting wrong. Pass rates, failure rates, reliability over time.
- **Money:** how much companies are saving with AI/agentic tools, how much they're losing (rework, incidents, technical debt, security fixes).

**Design notes (to be refined):**

- At-a-glance: a dashboard, not a report. One screen, the numbers that matter.
- Every number traceable to a source in the report — same credibility discipline as the articles.
- Open question: which cuts (industry / institution / company / sector) have enough data to be meaningful. Start with what the report already covers; add cuts as the evidence base grows.
- Open question: update cadence — live with the daily watch, or a weekly/monthly snapshot?

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
