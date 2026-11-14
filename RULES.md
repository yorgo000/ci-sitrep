# CI Sitrep — Editorial Rules

The single source of truth for how this report is made: what gets in, how
it is written, how it looks, and how it is checked. The daily watch cron
implements these rules; when a rule changes, update this file and the cron
instructions together.

**Change control:** every rule here is a decision Yorgo made or approved.
A rule changes only on his word. Record the change in §7 (changelog) with
the date.

**Scope:** this file governs the report itself (SYNTHESIZED.md and the
generated site). The publication's future features live in FUTURE.md. The
tagging taxonomy lives in TAXONOMY_DRAFT.md (draft, awaiting approval).

---

## 1. Selection — what gets in

**The bar.** Something enters the report only if it could change how a
firm building critical systems in finance should act — its offerings, its
controls, its budget, its risk posture. Routine news, vendor marketing,
and minor updates do not qualify.

**The three subjects.**

1. Pre-commit: CI-generated code sanitizing — tools and best practices
   for addressing the problem of CI-generated code before it is committed,
   while it is being written and at the point of commit. Commercial
   products, open-source tools, and the practices that make them effective.
   Confluence<1> builds its own tools in this space as well as advising on
   and deploying others'.
2. In codebase: Sanitizing post-commit of CI-generated code — tools,
   techniques, and best practices for detecting and remediating the
   defects CI-generated code has already left in an existing codebase.
3. Agentic: CIAC Design, Build, Deployment — the creation, governance,
   and management of ci agent collectives.

**Nomenclature.** Our own framing uses CI (created intelligence), CIA (ci
agent), CIAC (cia collective) — in the title, the explainer, the theses,
the section headings, and the culture framework. The field's own words
stay as the sources say them: quoted statistics (Sonar, Google, Gartner)
keep "AI-generated" because that is what the sources say. Never rewrite a
source's wording to fit our framing.

**Agent reliability** is covered inside §3 (the §3 intro names reliability
as "the binding constraint, not capability"; §3.6 Evaluation covers
pass^k vs pass@1, METR time horizons, ThinkingBox, "never trust an
agent's self-reported PASS"). It is not a separate watch.

**Nothing is silently deleted.** Superseded text moves to
archive/ARCHIVE.md, dated and categorized by subject, with a pointer to
where the current version lives. A correction is an in-place update plus
an archive entry. The pre-restructure append-only version is preserved at
archive/SYNTHESIZED-2026-11-11-append-only.md.

**No source is lost.** If information from a source is used, it is cited
where it is used. If a source's content is superseded, its link is
archived with the superseded text.

---

## 2. Content — structure

The report is a **knowledge base**, not a log. Sections update in place;
the file is hierarchical, with a table of contents.

**Front page, in order:**

1. **How to read this** — one collapsed block holding everything before
   "New this week" (the intro line, the credibility legend, the caveats).
   It is the first thing on the page but must not attract attention.
2. **New this week** — a rolling 7-day window. Entries older than 7 days
   drop off. Every entry is dated with the date it was ADDED to the
   report, carries a finding-first title (§3), and links to the section
   where the article lives. Entries are in strict newest-first order.
3. **What we're watching** — dated upcoming events (comment deadlines,
   effective dates) and open questions the report is tracking (things
   promised but not yet published, benchmarks that don't exist yet,
   regulatory language that may harden). Dated items are in soonest-first
   order. Every item links to its section. Maintain it every run: add a
   new item when research surfaces one; remove an item the day it lands
   (it becomes an article and a "New this week" entry instead). A past
   date or a landed item still listed is a defect.
4. **Contents** — the table of contents. Anchor links must match the
   headings (GitHub-style anchors; the double hyphens are correct).
5. **§1, §2, §3** — the three content sections, in that order.
6. **Archive** — a pointer to the archive page.

**Articles.** Each article is a collapsible headline (`<details>` /
`<summary>`) with one fact per bullet inside. The headline carries the
finding, the source in a parenthetical with the date, and the credibility
rating (§3). Every article ends with a Source bullet (§3).

**See also cross-links.** One-line collapsible blocks at the end of
sub-sections, linking related sections across the three subjects. When a
new item is cross-cutting — the same evidence, control, regulation, or
watch item in two places — add a See also line in BOTH places. Link only
where the related section changes a decision, not for mere topic
similarity.

**The audit page** (Self-Audit) is generated from the live files by
`_tools/build_audit.py` — never hand-edit it. Its Coverage section links
to "What we're watching" rather than maintaining its own known-gaps list.

---

## 3. Style — how it reads

**Information first, source at the end, hyperlinked — everywhere.**

- Article headlines lead with the FINDING, never the source name. The
  source goes in the parenthetical after the finding, with the date and
  context — "…introduces a known security flaw (Veracode, Spring 2026,
  longitudinal benchmark)" — never "Veracode — …". For regulatory
  documents, lead with what the document does or says.
- The source name in the headline parenthetical is HYPERLINKED to the
  article's primary source URL (the same URL as the article's Source
  line). If the parenthetical names two distinct sources sharing one
  Source document, link both names to it. If no single source exists
  (e.g. a headline covering several surveys), leave the parenthetical
  plain — never link a name to a URL that is not its source.
- Every bullet and prose paragraph follows the same rule: the finding,
  number, or actionable fact leads; the source attribution goes at the
  END in parentheses, hyperlinked where a URL exists. NEVER open a bullet
  with a source name, study name, vendor name, or regulator name followed
  by a colon or a verb — no "SailPoint: 79% of enterprises…", no "Apiiro
  found…", no "The UK AI Security Institute reported…". Dates lead only
  for dated calendar items (the "What we're watching" list); in article
  bullets, a date goes at the end with the attribution.
- "New this week" entry titles are findings, never names — "First
  benchmark of agentic pre-merge security review (SecPRBench; subjects 1,
  2)", never "SecPRBench (subjects 1, 2): the first benchmark…". Link the
  source name in the entry to its primary source URL.
- Exceptions (the only ones): lists organized BY verification status
  (§1.6.1, §2.6, §3.8) where the source's reliability IS the point;
  tables, where the product/framework is the row subject; and bullets
  whose point is the source's reliability (e.g. "CodeRabbit's own
  analysis — treat as a vendor claim").

**Sources convention.** Every article ends with a Source bullet linking
to its primary source, in the form `- Source: [Label](URL)` as the last
bullet inside the `<details>` block. Subsections that draw on comparison
sources, background reading, or multiple references carry a
`Sources: [Label](URL) · [Label](URL)` line at the end of the subsection
(before any See also block). There are no bibliography sections — sources
live with the content they support, as hyperlinks, so the reader verifies
each claim at the point where they read it. When adding a new article,
always include its Source line with a real, verified URL (the primary
source: the paper, report, or official document — not a secondary summary
unless the primary is unavailable).

**Inline links.** When prose mentions a source, benchmark, regulation,
framework, or product by name, link the FIRST mention in each subsection
to its source (the same URL the article's Source line or the subsection's
Sources line uses, or the authoritative page for it). Do not link every
occurrence — once per subsection is enough. Inside article `<details>`
blocks: the headline parenthetical source IS linked (see above); do not
add further links inside the article body bullets (they already have
Source lines). Do not link inside Sources lines. This keeps every section
self-contained for a reader who jumps straight to it.

**Link verification.** Every source link on the site must be a LIVE link
— Yorgo uses them to start commercial conversations with the sources.
Before publishing any new Source or Sources link, verify it loads (HTTP
200 via curl, or confirm the page renders via browser.open — note that
some sites, especially Medium, block curl with 403 or time out while
still loading fine in a browser, so a curl failure alone does not prove a
link is dead; check it in the browser before concluding). Never publish a
truncated or guessed URL. If a URL returns 404, find the correct URL
(search for the article title) or use an archived copy — do not link to a
dead page.

**Credibility rating.** Every article headline carries a dots rating for
how much confidence a reader can place in its source, appended at the end
of the `<summary>` line (after the source info).

- ●●●● Established — peer-reviewed and independently confirmed, or a
  primary regulatory/government document (safe to act on).
- ●●●○ Corroborated — peer-reviewed single study, or a credible primary
  source confirmed by independent reporting (good basis for a decision).
- ●●○○ Reported — single credible source, not yet independently
  verified: preprints with transparent methodology, well-documented
  vendor research, regulator-run surveys with self-reported data
  (directional; verify before committing significant budget).
- ●○○○ Claimed — vendor claim without disclosed methodology, or a single
  uncorroborated report (treat as a lead, not a fact).

When in doubt between two levels, pick the lower one. The legend
explaining the dots lives in the report header — do not remove or alter
it. The rating will also be a structured field in the raw data for
high-paying subscribers, alongside tags and timestamps.

**Company name.** The company is **Confluence<1>** — the "<1>" is part of
the brand. Never "Confluence 1", never bare "Confluence" in new content.
The only correct bare "Confluence" on the site is the Atlassian product
in the §2.3 AWS Security Agent table row. The domain (confluence1.com)
and the email (ci-sitrep@confluence1.com) are correctly without brackets.

**No internal process detail on the public page.** The reader sees the
report, not how it is made. No mention of the watch, the cron, the
maintenance process, or Barnaby.

**Timestamps.** The Markdown carries a "Last updated" line; the
generator turns it into a prominent "As of [weekday, Month D, YYYY]"
banner directly under the H1. The "Last updated" line is stripped from
the rendered body (the date lives only in the banner).

**Numbers carry their basis.** A percentage without its sample, date, and
source is a vibe. When a figure comes from a survey, say who was surveyed
and how many. When a figure is a prediction (e.g. Gartner's 40% by 2027),
say so — never present a prediction as a measurement.

---

## 4. Design — how it looks

The standard: judge the site as an external reader on a phone. A change
is not done when it is pushed — check the live site and confirm rendering
before calling it done.

**Palette and type.** Warm paper background everywhere (#FAF6EF); logo
navy #283060 (sampled from the Confluence<1> wordmark); links logo navy.
H1 is a full-width navy masthead band with white serif text; "Code &
Finance" sits on its own line under "CI Sitrep", italic. H1 and masthead
title use a serif stack to match the Confluence<1> logo font. Body text
is sans-serif. The design is FT-inspired: upscale, quiet, paper-like.

**Masthead.** The left sidebar is a publication masthead: the CI Sitrep /
Code & Finance wordmark + tagline, the "by Confluence<1>" wordmark
(the "Confluence <1>" text from the logo, cube cropped out), nav links
(About, Explainer, Theses, Archive, Self-Audit), the credibility rating
legend (heading: "Credibility rating"), the Contents index, and the
copyright line "© 2026 Confluence<1> Corp. All rights reserved."

**Section headings.** The three content sections are the visual top of
the hierarchy. The meta-section headings ("New this week", "What we're
watching", "Archive") are de-emphasized: smaller, lighter weight, muted
color.

**Collapse behaviour.** The two front-page sections ("New this week",
"What we're watching") start OPEN; everything else starts collapsed.
Article headlines are native `<details>` and start collapsed. Jumping to
an anchor auto-expands its ancestors. "How to read this" is regular
weight, italic, muted — first on the page, not attracting attention.

**Mobile.** Content comes before the masthead (CSS `order`: main first,
sidebar second). A native `<details>` "Contents" line sits at the top of
the main content, right after the "As of" banner; it is hidden on desktop
and shown on mobile, and sits outside every section-body so collapsing a
section never hides it.

**Share links.** Article headlines, substantive paragraphs, tables, and
headings each carry a small link-icon button that copies a direct URL
(page + #anchor) with a "Copied" confirmation. The icon is inline SVG —
no font glyph. Buttons appear on hover on desktop and are always visible
on mobile. Ids are generated deterministically in JS from slugified text
(60-char cap, dedupe -2/-3 suffixes), so a copied link resolves
identically on any later load. Clicking an article's button never toggles
the article; a shared article link opens the article expanded. Excluded:
See also blocks, the How-to-read block, the mobile Contents block.

**No font-glyph dependency for UI.** Expand/collapse arrows are pure CSS
borders; icons are inline SVG. A glyph that renders as a weird character
on a reader's device is a defect, even if the behaviour works.

**External links open in new tabs** (`target="_blank" rel="noopener"`) —
following a source never replaces the sitrep. Internal links (anchors,
.html pages, mailto) stay in the same tab.

---

## 5. Verification — the daily check

Every change is verified before it is published. Two tiers:

**Tier 1 — every change (automated).** After regenerating the HTML and
before pushing, run:

```
python3 _tools/verify.py SYNTHESIZED.md index.html
```

It checks structure (every article has a Source bullet and exactly one
credibility rating; every headline parenthetical links its source, with
the documented exceptions; no duplicate headlines; no literal Markdown
links in the HTML; all internal anchors resolve), freshness (no "New this
week" entry older than 7 days; no past date in "What we're watching";
"Last updated" not in the future), order ("New this week" newest first;
"What we're watching" soonest first; section and subsection order),
naming (Confluence<1> everywhere, with the one documented Atlassian
exception; current section names), hygiene (no internal-process strings
on the public page), and layout markers (As-of banner, mobile Contents,
credibility legend, copyright line, share buttons, How-to-read block).
It also curl-checks every external link.

- A **FAIL blocks the push.** Fix the cause, regenerate, re-run until it
  passes. Do not push a failing build.
- A **WARNING needs a human review before pushing**: rating/source
  consistency flags (e.g. an arXiv preprint rated Established, a
  vendor-labelled article rated above Reported), source-first pattern
  candidates, and link-check failures. For link warnings, browser-check
  any URL that is not a known bot-protected site (Medium, OpenAI,
  BusinessWire and similar block curl but load fine in a browser).

**What automation cannot check — the worker's pre-publish re-read.**
Before publishing, re-read every new or revised segment and confirm:

1. **Necessary content is in there, and only that.** Every item from the
   day's research that passed the bar (§1) is in the report, in the right
   section; every "New this week" entry points to content that exists;
   nothing stale remains (no superseded text left in place, no entry
   promising content that isn't there).
2. **Ratings are accurate.** The rating matches the source type and
   whether it has been independently confirmed (§3). When in doubt, the
   lower level. A rating that rests on the underlying primary document
   rather than the Source URL's domain (e.g. a law-firm summary of a
   regulator's bulletin rated Established) is fine — note it if it looks
   odd.
3. **Information first.** Does the segment lead with information? Is the
   source at the end, hyperlinked? Fix any segment that doesn't.
4. **Content order.** "New this week" newest first; "What we're watching"
   soonest first; the new article sits in the right sub-section.

**Tier 2 — visual review (when the generators or the design change, or
weekly).** Open the live site in a browser, desktop and mobile, and
check it against §4: masthead and H1 band render correctly; content
before masthead on mobile; the inline Contents line is present on mobile
and absent on desktop; share buttons work (clicking one copies the link
and, for an article, does not toggle it); a shared article URL opens the
article expanded; no glyph renders as a weird character. A design change
is not done until the live site has been seen rendering correctly.

**Link health.** The daily verify run curl-checks all external links.
The Self-Audit page records the date of the last full manual link audit
(2026-11-12: all 94 unique URLs verified live).

---

## 6. Publishing

1. Edit the canonical Markdown at `~/workspace/your_files/watches/`
   (SYNTHESIZED.md, archive/ARCHIVE.md). The repo staging dir
   (`~/workspace/ci-sitrep/`) is a copy, not the source.
2. Sync the changed files into the staging repo.
3. Regenerate the HTML with the repo's generators (`build_html.py` for
   the report; `build_page.py` for the other pages; `build_audit.py`
   then `build_page.py` for the Self-Audit page, title "Self-Audit —
   CI Sitrep"). If ARCHIVE.md changed, rebuild archive.html too
   (rewrite its links to repo-root-relative form first).
4. Run the Tier 1 verification (§5). Do not push a failing build.
5. Push the changed files with the API helper
   (`~/workspace/custom-connectors/custom.github/bin/github.py put`).
   Verify each put returns status 200 or 201. (SSH push is blocked by
   the VM egress proxy — HTTPS/API only.)
6. Verify the live site reflects the change (curl the live page and
   check for the new content). GitHub Pages deployments lag — sometimes
   several minutes. If the live page is stale but the repo content is
   correct via raw.githubusercontent.com, wait and re-check rather than
   re-pushing.
7. Append one row to `_tools/audit_log.csv` per run (date, distinct
   sources actually opened and evaluated, articles added, articles
   updated, notes). On a quiet day, log 0 added and 0 updated — the
   funnel needs the denominator. The audit page numbers are computed
   from the live files — never hand-edit them.

---

## 7. Changelog of the rules

- **2026-11-09** — Report created (three subjects, append-only log).
- **2026-11-11** — Restructured into a knowledge base (in-place updates,
  archive model, "New this week"). CI/CIA/CIAC nomenclature agreed.
  See also cross-links adopted.
- **2026-11-12** — Information first adopted (headlines). Sources
  convention adopted (per-article Source bullet, subsection Sources
  lines, no bibliographies). Credibility ratings adopted. Inline links
  adopted. Link verification adopted. "As of" banner adopted. Public
  page scrubbed of internal process detail. Design refresh (warm paper,
  navy masthead band).
- **2026-11-13** — Section renames (sanitizing). "What we're watching"
  adopted. External links open in new tabs. Mobile layout fixed
  (content before masthead) + inline Contents. Share links adopted
  (articles, paragraphs, tables, headings). "Audit" renamed "Self-Audit";
  legend heading "Credibility rating". Meta-section headings
  de-emphasized.
- **2026-11-13 (evening)** — Information first STRENGTHENED to
  everywhere (bullets, prose, "New this week" titles), source
  hyperlinked at the end; headline parenthetical sources hyperlinked.
  Content-order rules adopted ("New this week" newest first; "What we're
  watching" soonest first). Verification process adopted (Tier 1
  automated checks via `_tools/verify.py`, Tier 2 visual review).
  This rulebook created.
