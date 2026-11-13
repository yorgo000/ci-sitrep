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
