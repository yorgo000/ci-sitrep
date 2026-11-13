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
