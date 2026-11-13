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

**Design notes (to be refined):**

- The directory should be generated from the live report files (like the rest of the audit page), not hand-maintained — the source list is already in the Markdown, in the Source and Sources lines.
- Open question: how to receive suggestions on a static site. Simplest is a mailto link to ci-sitrep@confluence1.com; a form needs a backend or a form service. A GitHub issue on the public repo is possible but exposes the repo to the public.
- Open question: whether to show per-source metadata (what we take from it, how often it's checked, when it was last cited) or just the list. Metadata makes the directory a coverage tool; the plain list is simpler and still answers "what do you follow?"

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
