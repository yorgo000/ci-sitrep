# CI SITREP — Editorial Rules

The single source of truth for how this report is made: what gets in, how
it is written, how it looks, and how it is checked. The daily watch cron
implements these rules; when a rule changes, update this file and the cron
instructions together.

**Change control:** every rule here is a decision Yorgo made or approved.
A rule changes only on his word. Record the change in §7 (changelog) with
the date.

**Scope:** this file governs the report itself (SYNTHESIZED.md and the
generated site). The publication's future features live in FUTURE.md. The
tagging taxonomy lives in TAXONOMY_DRAFT.md (approved v2, 2026-11-18).

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
3. Agentic: CIC Design, Build, Deployment — the creation, governance,
   and management of cii collectives.

**Geography and audience focus (2026-11-15).** The report's focus is the
US — New York City in particular — and the firms Confluence<1> serves:
investment management, hedge funds, and managing general agents (MGAs).
Gather and prioritise US evidence: US surveys, US regulators (federal and
state), US firms. UK, EU, and APAC items enter when they bear on US firms
— EU rules that bind firms with EU operations or clients, UK supervision
as a leading indicator, APAC frameworks US firms will be measured
against — but they do not lead: the dashboard's finance cut and the
front-page synthesis lead with US figures, and non-US figures are
labelled with their jurisdiction. A missing US figure is a gap to note
and to seek, not a reason to lead with a UK one.

**Nomenclature.** Our own framing uses CI (created intelligence), CII (ci individual), CIC (cii collective) — in the title, the explainer, the theses,
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

**Row 1** — the As-of banner and the Sections expand/collapse controls,
on one row (banner left, controls right). On phones, "How to read this"
also sits centered in row 1 — a phones-only copy of the masthead
control (§4); on desktop it is hidden.
**Row 2** — the Search/Filter/Sort panel (§4): one collapsed block
holding the search box, the filters, and the sort control. Collapsed
by default.
The mobile inline PAGE CONTENTS sits between row 2 and the dashboard section
(hidden on desktop); the sidebar PAGE CONTENTS lives in the masthead (§4).

Then the two top-level sections, both starting OPEN:

1. **EXECUTIVE DASHBOARD** — the F-01 dashboard, embedded from
   `dashboard.json`: the bottom-line strip (seven items in a 3+3+1
   grid — six charted tiles occupying seven units in three rows (three
   1-unit tiles; the 2.5× tile plus the paired double tile; the 188
   tile alone, the trailing hole consolidated bottom-right), then the
   profitability item full-width, reading "Insufficient data" and
   linking to the money panel; pie tiles for the percentages, a ratio
   tile for the multiplier, a waffle tile for the count-share, a
   big-number tile for the count, a paired double tile for the two BCG
   figures; pie colours follow the split, §4;
   the WHOLE strip tile is one link
   to its evidencing article, like the countdown tiles), the countdown strip (labelled
   "COUNTDOWN") and the five panels,
   every figure linked to the report article that evidences it. (The
   standalone dashboard page is gone; `dashboard.html` redirects to
   `index.html#executive-dashboard`.)
2. **REPORT** — the report itself, in this order:
   - **Situation at hand** — a 2–4 sentence macro synthesis, the first
     thing a new reader actually reads. Every claim in it is grounded in
     the report's own findings and traceable via an internal link to the
     section that evidences it (the flaw rate to §1.6, the governance gap
     to §3.4.3, the regulatory picture to §3.4.2). Revise it whenever a
     material shift lands that changes the macro picture; never let it go
     stale or contradict the sections below it. No generic marketing
     claims — every sentence must be defensible from the report.
   - **New in the last 7 days** — a rolling 7-day window. Entries older than 7 days
     drop off. Every entry is dated with the date it was ADDED to the
     report, carries a finding-first title (§3), carries plain-English
     section tags ([Pre-commit], [In codebase], [Agentic] — one per
     section the entry touches, never the old "(subject 1/2/3)"
     parentheticals), and links to the section where the article lives.
     Entries are in strict newest-first order.
   - **What we're watching** — dated upcoming events (comment deadlines,
     effective dates) and open questions the report is tracking (things
     promised but not yet published, benchmarks that don't exist yet,
     regulatory language that may harden). Dated items are in soonest-first
     order. Every item links to its section. Maintain it every run: add a
     new item when research surfaces one; remove an item the day it lands
     (it becomes an article and a "New in the last 7 days" entry instead). A past
     date or a landed item still listed is a defect.
   - **§1, §2, §3** — the three content sections, in that order.
   - **Archive** — a pointer to the archive page.

**Articles.** Each article is a collapsible headline (`<details>` /
`<summary>`) with one fact per bullet inside. The headline carries the
finding, the source in a parenthetical with the date, and the confidence rating (§3). Every article ends with a Source bullet (§3).

**Tagging.** Every article carries one tag line — an HTML comment
directly above its headline — in the taxonomy's fixed 12-dimension
field order (subject, type, confidence, severity, jurisdiction,
source-date, sector, industry, register, pnl-impact, horizon,
company). Set dimensions are multi-value: no tie-breaks — use both
values where both fit. Level dimensions (confidence, severity,
register, horizon) are single-value; when in doubt, pick the lower /
less alarming. Multi-value fields list values in taxonomy-table
order. **Mirrored pairs:** the same finding mirrored in two sections
carries both subjects on both instances; distinct findings from the
same source stay section-pure. **Company** is the item's subject, not
its source: a named recurring benchmark, instrument, or report counts
its maker; one-off studies and surveys of third parties do not tag
their measurer or publisher. **Dates:** the headline source's date
when one exists, else the most-recent constituent. The tag join
parses SYNTHESIZED.md directly (`build_dashboard.py`'s shared parser
— one parser, never duplicated): articles and tiles carry `data-*`
attributes from their tag lines for the filter panel (§4).
`data-company` is comma-joined — company values contain spaces — all
other dimensions space-joined.

**See also cross-links.** One-line collapsible blocks at the end of
sub-sections, linking related sections across the three subjects. When a
new item is cross-cutting — the same evidence, control, regulation, or
watch item in two places — add a See also line in BOTH places. Link only
where the related section changes a decision, not for mere topic
similarity.

**The audit page** (Self-Audit) is generated from the live files by
`_tools/build_audit.py` — never hand-edit it. Its Coverage section links
to "What we're watching" rather than maintaining its own known-gaps list.

**Corrections page.** `CORRECTIONS.md` (built to `corrections.html`
via `build_page.py`) lists every correction and omission fix, newest
first, one line each: the date, what was wrong or missing, what it is
now, with a link to the corrected article where one exists. When a
correction or omission fix lands, add its entry as part of the same
publish — the daily watch owns it. Entries are never removed.

**Glossary.** `GLOSSARY.md` is the single source of truth for the
report's acronyms and jargon: one line per term, plain language,
alphabetical under letter headings. It builds to `glossary.html` via
`build_page.py` (each entry gets a stable id from its term) and feeds
the report's tooltips (§4). **Terms are never removed** — even if the
text that referred to a term drops out of the report, the entry stays,
so the dictionary only grows. The daily watch adds any new term or
acronym a new article introduces, as part of its editorial pass, in
alphabetical place under the right letter heading. Changing
`GLOSSARY.md` means regenerating BOTH `glossary.html` and `index.html`
(the tooltip data is generated from it at build time).

**Dashboard.** `dashboard.json` is the single source of truth for the
executive dashboard (F-01): five panels of at-a-glance figures, every
figure carrying its value, label, source, rating, date,
and a link to the report article that evidences it, plus a `bottom_line`
list (eight items in nine units — three full rows of three — rendered
as a strip above the countdown; rating and
date optional, since the profitability item has neither; each item
carries a tile where its figure has one — a pie tile for a percentage
(number next to the pie, block-level legend rows), a ratio tile for a
multiplier, a waffle tile for a count-share, a big-number tile for a
count, a paired tile for two figures from one finding, a question mark
in a circle for the profitability item, which
has no data — pie colours follow the split, §4; and the profitability
item is full-width, last, with `"full": true`) and a deadlines
list for the countdown strip. Tile ids derive from the figure's stable
`key`, never from its label slug — a label reword must not break a
shared tile link. (Decided 2026-11-18; migration pending — no figure
carries a `key` yet, and ids still derive from label slugs until it
lands.) Every pie-family figure carries `pie_split` (§4); the
segmented pie carries a per-segment `tone` instead. The link is the
article's runtime id (assigned by the share JS from the headline) — a
section anchor is not specific enough: the reader must land on the
article itself, where its Source line takes them to the primary
source. The link target's headline must state the tile's figure: a
reader who clicks a tile lands on an article headlined with the
finding they clicked. If the figure is a secondary finding inside an
article headlined with something else, split it into its own article
— headline the finding, same source, same rating — and point the
tile at the new article. Never point a tile at an article whose
headline is about a different finding, however good the evidence
buried in its bullets. (2026-11-19: the 3.4× strip tile linked to the
2.5× post-hoc-review article, where the 3.4× was one bullet in six;
Yorgo caught it from a QA screenshot.) Where a conclusion draws on a second headline article in
another subsection, the figure carries an "also" list ({anchor, label})
rendered after the source name. The one exception is §3.6 (Evaluation),
which is prose, not articles: its figures link to the section anchor
until the content becomes articles. The dashboard intro carries a
second paragraph, `tint_note`, stating what the tile background tint
means (§4). It is embedded in the report page as the first
top-level section (EXECUTIVE DASHBOARD): `build_html.py` imports
`_tools/build_dashboard.py` to render it, and validates every figure
against the generated `index.html` (required fields, rating in the
four levels, `pie_split` in its six values, waffle figures count-vs-count
with a minority share ≥ 2%, history join rules, link anchors exist in
`index.html` or among the computed article ids) —
a bad entry exits 1; fix the data, never weaken the check.
`compute_article_ids()` in `_tools/build_dashboard.py` replicates the
share JS's slugify + uniqueId — the two implementations must stay in
sync, or dashboard links will point at ids the page never assigns.
The standalone `dashboard.html` is a redirect to
`index.html#executive-dashboard`. **Never add a figure the report does not
evidence, and never invent a dollar figure for the money panel** — its
honest statement is "no credible dollar figure exists yet". The daily
watch updates a figure when a new article moves a headline number, and
updates the deadlines list the day a What-we're-watching date lands, so
the countdown strip never shows a passed date. Panel order is editorial
(audience-first), not numeric. `as_of_label` rolls to the release date
whenever dashboard content changes.

**Dashboard history.** `dashboard-history.json` is the append-only log
of dated values behind the sparkline tiles, keyed by figure; a figure
joins it by its `history_key`. A figure becomes a sparkline tile when
its series holds 2+ VERIFIED dated values of the same metric from the
same series (same survey/benchmark, same question/population) — a
forecast is never a point, and no point is invented or read off an
unreadable chart. Lower bounds plot at the bound value with `>` in the
display; points derived from the source's own stated deltas
(subtraction) or stated counts (division) are legitimate recomputation,
flagged in the fig-note. Validate: the key exists, 2+ points, ascending
dates, the last point's display equals the figure's display. Sparkline
captions list every point: a multi-year series keeps the full label on
every point; a single-year series carries the year once as a prefix
("2026: Spring ~45% → Jul ~44% → Fall ~38%"). One-off studies,
incidents, and counts with no repeated measurement never get a series.

**CI vs EI page.** `CI-VS-EI.md` builds to `ci-vs-ei.html` via
`build_page.py` — the dedicated always-on view of every CI figure
against its human (EI, evolved intelligence) equivalent, and the third
surface alongside the executive dashboard and the report (F-17, built
2026-11-17; "ATAK" is design analogy only — the view is named "CI vs
EI"). It presents, in three family sections (Development, Operations,
Business-composite), the complete pairs, the partial comparisons (with
their caveat), and the gaps (explicitly, as gaps — a row reading "No
human baseline published" is a finding, not a hole). A comparison
counts only on the same task with the same metric, with the baseline
population stated; a CI number from one study set against a human
number from another is not a comparison. Every figure carries its
confidence rating and links to the report article that evidences it
(the article's runtime id, as in the dashboard). The page is versioned
and dated ("As of" + version in the dateline) and carries a Changes
log at the bottom: when a figure moves, the change is logged there
with the old and new values. The working audit behind it lives at
`~/workspace/goals/watch-subjects-synthesized-state-of-the-art/hidden_files/f17-baseline-audit.md`
(not public). The daily watch maintains both: when a new article
publishes a human baseline on a task the report already measures, or a
new benchmark arrives with a human control arm, update the audit and
the page the same run — a gap that gains a baseline is a material
change, and the "New in the last 7 days" entry says so.

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
- "New in the last 7 days" entry titles are findings, never names — "First
  benchmark of agentic pre-merge security review (SecPRBench)
  [Pre-commit] [In codebase]", never "SecPRBench [Pre-commit] [In
  codebase]: the first benchmark…". Link the source name in the entry to
  its primary source URL. Tag every entry with plain-English section
  tags — [Pre-commit], [In codebase], [Agentic] — never the old
  "(subject 1/2/3)" parentheticals.
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

**Confidence rating.** Every article headline carries a dots rating for
how much confidence a reader can place in its finding, appended at the end
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
Finance" sits on its own line under "CI SITREP", italic. H1 and masthead
title use a serif stack to match the Confluence<1> logo font. Body text
is sans-serif. The design is FT-inspired: upscale, quiet, paper-like.

**Masthead.** The left sidebar is a publication masthead. The heading
is identical on every page: the CI SITREP / Code & Finance wordmark +
tagline ("Created Intelligence in code and finance — as of today."),
and the "by Confluence<1>" wordmark (the "Confluence <1>" text from
the logo, cube cropped out) — the logo stays in the masthead
everywhere, all the time. On the report page the heading is followed,
in this order: "How to read this" (a collapsed `<details>`, summary
in the masthead-header treatment — 13px, uppercase, letter-spaced,
muted, not italic — mirroring the confidence legend; body 13px muted;
its inline links need an explicit inline override, since sidebar links
are block-level nav rows); the nav, headed "SITREP sections", with
the links in this order: Self-Audit, Corrections, Glossary, CI vs
EI, The names: CI, CII, CIC, Foundational theses, Archive, About;
the page
Contents, titled "PAGE CONTENTS"; the confidence rating legend (a
collapsed `<details>`, summary "Confidence rating scale";
starts closed — the dots are also explained in "How to read this" and
carry their words in the dashboard; its padding-bottom and the
summary's margin apply only when open, so the closed line has no
blank space under it); the Contact section (heading "Contact":
errors, omissions, and feature requests to
ci-sitrep@confluence1.com; working with Confluence<1> to
hello@confluence1.com — both mailto links); and the copyright line
"© 2026 Confluence<1> Corp. All rights reserved." No CTAs inside the
content (see F-12, Dropped). On the sub-pages the heading is followed
by a "← Back to the report" link and the PAGE CONTENTS index (see
Navigation). "How to read this" also renders as a phones-only copy in
row 1 (§2) — one source, emitted twice, so the copies cannot drift;
on phones the page looks unchanged by design.

**Section headings.** The two top-level sections (EXECUTIVE DASHBOARD,
REPORT) are the visual top of the hierarchy, their heading text in
all-caps so they read as different from their constituents (title case
until 2026-11-15, when Yorgo asked for caps); the three content
sections (§1, §2, §3) sit inside Report. The meta-section headings
("Situation at hand", "New in the last 7 days", "What we're watching",
"Archive") are de-emphasized: smaller, lighter weight, muted color.

**Collapse behaviour.** Only the two top-level sections start OPEN;
everything inside them — the three front-page sections ("State of the
market", "New in the last 7 days", "What we're watching"), the dashboard panels,
the content sections — starts collapsed, as one line each. (Before
2026-11-15 the front-page sections and dashboard panels also started
open; Yorgo reversed that — the page opens as a clean outline, and the
reader drills in.) Article headlines are native `<details>` and
start collapsed. Jumping to an anchor auto-expands its ancestors —
including the target heading itself. "Collapse all" returns the page to
its initial state: it closes everything except the two top-level
sections. "How to read this" lives in the masthead (see Masthead);
its phones-only row-1 copy is regular weight, italic, muted — not
attracting attention — sits centered in row 1, between the As-of
banner and the Sections controls, and drops to a full-width line when
opened. The Search/Filter/Sort panel (§4) starts collapsed.
On the content pages (About, Explainer, Theses, Archive,
Self-Audit, Glossary) everything starts collapsed, including the theses
page's Part headings (H1s other than the page title). The Sections
expand/collapse control lives in the main content — row 1 on the
report page, under the H1 on the content pages — never in the
sidebar, where it was lost.

**Mobile.** Content comes before the masthead (CSS `order`: main first,
sidebar second). A native `<details>` "PAGE CONTENTS" line sits in the main
content between the Search/Filter/Sort panel (row 2) and the dashboard section;
it is hidden on desktop and shown on mobile, and sits outside every
section-body so collapsing a section never hides it.

**Navigation.** Three mechanisms, all unobtrusive (2026-11-14):
- **Breadcrumbs.** At the top of every section body, a small muted trail
  back up to any ancestor level or the top of the page — "↑ Top · §3
  Agentic … · §3.4 Governance". Built in JS from the heading hierarchy,
  so it stays correct as sections are added or renamed. Skipped on the
  three front-page sections (they sit at the top of the page already) and
  on the page title; the current section is not repeated (its heading is
  directly above). Breadcrumb paragraphs never get share buttons.
- **Back-to-top button.** A small round navy button, fixed bottom-right,
  invisible until the reader has scrolled 500px down, then smooth-scrolls
  to the top. The arrow is inline SVG. On every page.
- **Back to the report.** On the content pages (About, Explainer,
  Theses, Archive, Self-Audit, Glossary): the sidebar opens with the
  same masthead heading as the report page (linked "CI SITREP / Code
  & Finance" wordmark + tagline + "by Confluence<1>" logo), followed
  by a "← Back to the report" link above the PAGE CONTENTS list. On mobile
  the sidebar sits below the content, so those pages also carry a
  mobile-only back link at the top of the main content, right under
  the page title.

**Share links.** Article headlines, substantive paragraphs, tables,
headings, and every dashboard tile (panel tiles, bottom-line strip
tiles, countdown tiles) each carry a small link-icon button that copies
a direct URL (page + #anchor) with a "Copied" confirmation. The icon
is inline SVG — no font glyph. Buttons appear on hover on desktop
(Yorgo: he loves that they stay hidden until hover — keep it that
way) and are always visible on mobile. Tile buttons sit in the tile's
top-right corner, as a sibling of the tile's link, never nested
inside it, so clicking one copies the tile's URL instead of
following the link. Ids are generated deterministically in JS from
slugified text (60-char cap, dedupe -2/-3 suffixes), so a copied
link resolves identically on any later load — strip ids are
bl-<article-slug> (bl-money for the profitability tile), countdown
ids cd-<deadline-slug>, panel tile ids derive from the figure's
stable `key` (§2; migration pending — label slugs until it lands). Clicking an article's button never toggles
the article; a shared article link opens the article expanded.
Excluded: See also blocks, the How-to-read block, the mobile
PAGE CONTENTS block.

**Search.** A search box inside the Search/Filter/Sort panel (§4) — the
report is reference material, and readers need to find their way back
to information they saw. It indexes the live page
at runtime on first keystroke: no build step, no index file, no
backend, no cost, and always in sync with the daily watch (it reads the
page, so it needs no cron step). Searchable units are the share-button
units (articles, headings, substantive paragraphs, tables) plus
standalone list items in a section body — the best-practice bullets and
the "New in the last 7 days" / "What we're watching" entries (top-level `<li>`
outside `<details>`, ≥80 chars; nested items are covered by their
parent's text; items inside an article are covered by the article).
List items have no share-button id, so the indexer assigns one with the
same deterministic slugify. Results link to the same stable anchors and
open expanded. Ranking: title matches above body matches, all-token
matches above partial; top 10 shown with a count. Minimum 2 characters;
Escape closes; arrow keys + Enter navigate; clear button; click-outside
closes; aria-live result status. V1 searches the report page only.
Acronyms a reader would search for (e.g. TPRM) must be defined in the
prose at first mention — the search matches literal text, and an
acronym that never appears returns nothing. Icons are inline SVG.
Search-result clicks clear the filters first, so the target is always
visible on landing.

**Search, filter & sort panel.** One collapsed `<details>` at the top
of the page (row 2), holding the search box, the filters, and the sort
control. Collapsed by default. The header is a full-width navy bar —
"Search, filter & sort" in white, a CSS chevron (no font glyph) — with
an active-filter indicator after the label: count + dimension names,
capped at three names ("2 filters active: Severity, Industry"). One
active dimension counts once, however many values it holds; sort and
search are not counted (sort hides nothing; search has its own results
count). The panel filters the WHOLE report page — dashboard tiles AND
report articles, one model, one count line — from the tags (§2).
Sort applies to dashboard tiles within panels only: articles filter
but never sort, or the report's editorial structure scrambles. The
strips are never filtered and never counted. "New in the last 7 days",
"Situation at hand", and "What we're watching" stay unfiltered (not
tagged content). Shared links land unfiltered: a landing clears the
filters and the panel stays collapsed.
**Controls, in order.** Top line: Industry, Severity, P&L impact,
Horizon, Technical level (register), then Sort + the asc/desc toggle.
More filters: Section (subject), Type, Confidence, Jurisdiction,
Company. There is no Sector control — sector becomes a separate
product; sector tags stay in the data and `data-sector` stays on tiles
and articles as the hook. Type is a checkbox group, multiple choice:
OR within the dimension, AND across dimensions; none checked means no
constraint. Company is a select derived from the distinct company
values in the tag data at build time (open vocabulary — a newly tagged
company appears on the next build); controlled-vocabulary dimensions
list the full taxonomy vocabulary even at zero articles (EU, Greece),
so the option exists the day the first article lands. Sort offers
twelve keys — panel order, date, confidence, severity, horizon,
section, type, industry, P&L impact, tech level, jurisdiction, company
— each option labelled with its default direction; the asc/desc toggle
is a text button ("Ascending"/"Descending", CSS triangle, no glyph
characters), disabled for Panel order. Sort-key orders: severity and
confidence in their natural taxonomy order; horizon chronological;
register technical → mixed → business (depth scale); set dimensions
alphabetical by first value; ties keep editorial order (stable sort).
**Count line.** "Showing X of 62 figures · Y of 85 articles", always
visible, below Clear-all; figures are panel tiles only. When a
subsection filters out entirely it hides, heading and all; when a
section's subsections all hide, the section hides; the REPORT and
EXECUTIVE DASHBOARD headings stay visible, framing the per-area
empty-state lines ("No figures match these filters." /
"No articles match these filters.", each with its own Clear button).
Only the four untaggable tiles — the three §3.6 figures and the money
bignote — are never hidden and keep their editorial position under
sorting; the interim untagged-visible rule is retired (the backfill is
complete — an untagged article does not match a Company selection).
**Clear-all** sits below More filters, at the bottom of the filter
block; it resets the sort to Panel order and collapses More filters.
Filter selects go full-width on phones (≤600px).

**Tooltips.** The first mention of a glossary term in each subsection
gets a dotted underline; hovering (desktop) or tapping (mobile) shows
the one-line definition with a link to the full glossary entry. The
wrapping happens at runtime in the browser from the glossary data
injected at build time — it skips links, code, buttons, breadcrumbs,
and share buttons, and it never wraps the same term twice in one
subsection. Two terms are in the glossary but never tooltip-wrapped:
"agent" and "agentic" — too frequent; a marker on every first mention
would be noise. The tooltip data is generated from `GLOSSARY.md`, so
`index.html` must be regenerated whenever the glossary changes.

**No font-glyph dependency for UI.** Expand/collapse arrows are pure CSS
borders; icons are inline SVG. A glyph that renders as a weird character
on a reader's device is a defect, even if the behaviour works.

**External links open in new tabs** (`target="_blank" rel="noopener"`) —
following a source never replaces the sitrep. Internal links (anchors,
.html pages, mailto) stay in the same tab.

**Dashboard tiles.** Every dashboard figure renders as a tile, one
tile type per stat kind — nine types, no bars, no lines except
sparklines inside tiles. The value leads everywhere: the number comes
first and the label follows, so each tile reads as a sentence ("98% of
large companies have AI governance policies").
- `pie` — shares of one whole ONLY. A comparison is not a share: a-vs-b
  figures get ratio tiles, never pies.
- `ratio` — multipliers and a-vs-b comparisons; the multiple stays the
  headline number, with side rows carrying the exact side values. A
  ratio tile with a compare chart can be a DOUBLE (2 units,
  `"span": 2`): one figure in a wide card — enlarged numeral + label
  on the left, side rows on the right (the 3.4× strip tile, 2026-11-19);
  the before/after variant has no chart and keeps the stacked layout
  whatever its span.
- `big-number` — counts and single magnitudes with no denominator.
- `no-data` — the honest absence ("Insufficient data"); dashed border.
- `sparkline` — time series, 2+ dated points ONLY (§2).
- `flag` — binary facts.
- `note` — prose findings with no stat.
- `waffle` — count-shares ONLY: both sides counts of the same thing,
  minority share ≥ 2% (a 1-square minority reads as a solid block). A
  10×10 grid of 6px squares; the multiple stays the headline number;
  side rows keep the exact counts (a rounded graphic is never the only
  record); the caption names the counted set ("Share of 147
  vulnerabilities counted"). Pure multipliers and rates are not shares
  of a whole and stay ratio tiles.
- `paired` — two figures from one finding, one DOUBLE card (2 units
  wide, 280px tall): the figures sit SIDE BY SIDE (figures[0] left),
  each half carrying its own pie (standard 72px) + value, label, and
  legend, separated by a vertical hairline divider, no "vs"
  connector; the whole tile links to the evidencing article;
  sentiment judges the combined finding, not either figure alone; one
  source line below the halves. On phones the halves stack vertically
  with a horizontal hairline divider. Exactly 2 figures, each 0–100
  with a valid `pie_split`.
**Pie colours.** Every pie-family figure carries `pie_split`, naming
the wedge; the remainder follows by rule. Decision procedure, in
order: (1) CI vs EI or AI-side-vs-rest split → `identity` (rust wedge,
blue remainder); (2) wedge favourable, remainder adverse → `positive`
(blue wedge, rust remainder); (3) wedge adverse, remainder favourable
→ `negative` (rust wedge, blue remainder); (4) wedge favourable,
remainder unclassified → `positive-neutral` (blue wedge, grey
remainder); (5) wedge adverse, remainder unclassified →
`negative-neutral` (rust wedge, grey remainder); (6) none of the above
→ `none` (blue wedge, grey remainder). Identity beats valence: a CI/EI
split is `identity` even when one side is the good side. When torn
between rule 2 and rule 3, default to rule 3 — a grey remainder claims
less than a rust one. Grey is `#c9c2b0` (muted); `#ece5d3` leaves the
pie system. The segmented pie carries a per-segment `tone` (blue /
rust / grey by valence: positive → blue, negative → rust, mixed →
grey) instead of `pie_split`. The range pie draws a solid wedge to the
low bound, a band in the wedge colour at 40% opacity to the high bound,
and the remainder as a wedge path (high → 100%) — never a full circle
— so the band composites over the tile tint, not over a navy
remainder. A pie legend is one block-level row per segment, chip +
label + value, no separators, no wrapping within a row. Strip-legend
chips derive from `pie_split` (a-chip = wedge colour, b-chip =
remainder colour).
**Ratio colours.** The same decision procedure as pies, applied to
the two sides: identity first (CI vs EI → rust/blue), then valence
(favourable → blue, adverse → rust). The 2.5× SusVibes tile is the
worked example: both sides are AI generation, so identity does not
apply; the reviewed side is favourable → blue, generation alone →
rust.
**Ratio side rows name the cohorts, not the measure.** A compare
chart's two arms identify who or what is being compared — the groups,
the conditions — while the tile label states what is measured (the
rate, the cost, the share). An arm label that restates the measured
quantity reads as the measure against itself and says nothing about
what differs between the sides: "81–100% AI code vs 1–20% AI code" is
unreadable; "81–100% of code AI-generated vs 1–20% of code
AI-generated" names the two cohorts and the label supplies the rate.
(2026-11-19: the 3.4× tile's arms read "AI code vs AI code", caught
by Yorgo from a QA screenshot.)
**Sentiment is the tile's background tint** — a visual cue, never a
label (the word-pill treatment is superseded and gone). Positive =
blue tint `#E9EAEF`; negative = rust tint `#F6EAE5`; neutral = grey
tint `#F0EDE5`. The tints are pale washes (≈10% colour over paper);
the encodings are saturated fills — the two never share a lightness
band, so sentiment and the AI/not-AI encoding stay distinguishable.
Countdown tiles carry NO tint (a deadline has no sentiment); the
no-data tile takes the grey tint with its dashed border. The
`sentiment` data field stays (positive / negative / neutral); each
tinted tile also carries `data-sentiment` and a visually-hidden
sentiment word — colour is never the sole carrier, because the labels
always state the direction in words. The tint meaning is stated once,
in the dashboard intro (`tint_note`, §2) — one home per idea, no
second legend. Sentiment judges the finding as stated in the label; a
level-vs-direction conflict goes neutral.
**Unit sizes.** Tiles are standardized 1/2/3-unit cards on ONE tile
size (2026-11-19, Yorgo: same-size cards scan easiest). The unit is a
fixed card: 1 unit wide (one grid column) by 280px tall. A 2-unit tile
is two columns wide and 280px tall; a 3-unit tile spans the full width
and keeps its own (natural) height — the money bignote and the
profitability tile are framing elements, not stat cards, and are
exempt from the 280px height, as are the countdown tiles (their own
4→2→1 grid, uniform 3-line content). Height is fixed, not stretched:
every 1-unit and 2-unit tile is exactly 280px tall at every
multi-column width, so every row aligns top and bottom; the source
line is pinned to the tile's bottom (`margin-top: auto`); short tiles
vertically centre their content (the body sits centred between the top
and the source line) so a short card reads finished rather than
hollow. Content fits the unit by budget, not by truncation: labels
≤ 84 chars, legend rows ≤ 36 chars, side rows ≤ 33 chars, source lines
≤ 99 chars (1-unit) / ≤ 146 chars (2-unit), fig-notes ≤ 66 chars,
note text ≤ 190 chars, sparkline captions ≤ 79 chars, waffle captions
≤ 36 chars — and every tile's estimated height
(`build_dashboard.py`'s estimator, desktop widths) must be ≤ 280px;
the build FAILS above 290px and WARNS at 281–290px (tolerance band —
the estimator runs conservative, so band cases are decided by the live
whole-row check, not by trimming). A single tile's overflow is fixed by
trimming that tile, never by raising the unit height; the height moves
only on systematic evidence from the live whole-row check. Fixed
columns: 3 above 1100px, 2 at 601–1100px, 1 at ≤600px. On phones
(≤600px, single column) the fixed height is lifted — tiles are natural
height, since there are no row neighbours to align with and full-width
content wraps short; a double tile's content stacks (the paired tile's
halves stack vertically, each ~1 unit of content). Span collapse is
explicit (a span-2 item in a 1-column grid creates an implicit track
and overflows): span-3 is always `1 / -1`; span-2 becomes `1 / -1` at
≤600px. Mapping: pie (single/range), ratio, big-number, waffle,
no-data, flag = 1 unit; segmented pie, note, sparkline, paired = 2
units; money bignote, profitability = 3 units (full-width, natural
height). The bottom-line strip is 3+3+1 in the same system (see §2);
the countdown strip keeps its own 4→2→1 grid (four tiles do not pack
into a 3-column unit grid). `.tile-grid` uses dense flow: a later
1-unit tile backfills a hole a 2-unit tile leaves — visual order may
differ from DOM order by one slot; DOM order stays editorial. The
square variant is one aspect-ratio rule on 1-unit tiles, not adopted.
**Graphic-slot scoping.** Any CSS rule targeting a tile's inner graphic
must be scoped or qualified so it can never match the tile div:
tile-type classes are also tile-div classes — an unscoped
`.tile-waffle { width: 72px }` constrained the TILE to 72px and the
graphic overflowed it. Qualify graphic rules to the graphic row
(`.tile-graphic-row .tile-waffle`) or to the element (svg-qualified pie
and sparkline rules); audit every tile-type class for width, flex,
max/min-width, flex-basis, and grid-column rules on any class the tile
div carries.

**Pair tables (CI vs EI page).** The page's tables carry the
`pair-table` class (assigned by `build_page.py` for `CI-VS-EI.md`):
the CI column reads rust (#b3543f) and the EI column navy (#283060) —
the same colour meaning as the dashboard strip, the same two hex
values, never a third shade for the same meaning. A gap cell reads
"No human baseline published" in muted italic (Markdown emphasis —
`main em` already renders muted), so the absence is visible at a scan
without a third colour. One table shape for all rows: Parameter | CI |
EI (human) | Evidence — the Evidence cell carries the source link
(to the report article), the date, and the rating in dots + words
("●●○○ Reported"), so no legend is needed on the page. Rows are
ordered pairs first, then partials, then gaps; a section with no pairs
says so in a line ("No complete pair yet") instead of an empty table.

---

## 5. Verification — the daily check

Every change is verified before it is published. Two tiers:

**Tier 1 — every change (automated).** After regenerating the HTML and
before pushing, run:

```
python3 _tools/verify.py SYNTHESIZED.md index.html
```

It checks structure (every article has a Source bullet and exactly one
confidence rating; every headline parenthetical links its source, with
the documented exceptions; no duplicate headlines; no literal Markdown
links in the HTML; all internal anchors resolve — article ids
assigned at runtime by the share JS are accepted via the computed id
set, see §2 Dashboard), freshness (no "New this
week" entry older than 7 days; no past date in "What we're watching";
"Last updated" not in the future), order ("New in the last 7 days" newest first;
"What we're watching" soonest first; section and subsection order),
naming (Confluence<1> everywhere, with the one documented Atlassian
exception; brand all-caps CI SITREP; current section names), hygiene
(no internal-process strings on the public page), and layout markers
(As-of banner, mobile PAGE CONTENTS, confidence legend, copyright line,
share buttons, How-to-read block, the two top-level sections, the
Sections control in the main content, the embedded dashboard panels).
It also curl-checks every external link.

- A **FAIL blocks the push.** Fix the cause, regenerate, re-run until it
  passes. Do not push a failing build.
- A **WARNING needs a human review before pushing**: rating/source
  consistency flags (e.g. an arXiv preprint rated Established, a
  vendor-labelled article rated above Reported), source-first pattern
  candidates, and link-check failures. For link warnings, browser-check
  any URL that is not a known bot-protected site (Medium, OpenAI,
  BusinessWire and similar block curl but load fine in a browser).

**Proposed verify.py extensions (not implemented — record, do not
assume):** a tile-count check as a DERIVED data-vs-render check
(figures in `dashboard.json` vs tiles rendered — never a hard-coded
count, the watch adds figures); a masthead-order assertion batch
(How-to-read before SITREP sections, Contact above ©, PAGE CONTENTS
below the sections nav). The sentiment re-point is moot: verify.py
does not count pills (verified 2026-11-18) — tint counts are checked
statically instead.

**Filter JS harness.** `_tools/tests/` holds the filter/sort JS test
harness (`r4b-test.js` + `r4b-fixture.json` + `r4b-filter-js.txt`): a
Node DOM shim running the real FILTER_JS from the generator against a
fixture parsed from the built `index.html`, expectations computed
independently — 69/69 pass (2026-11-18). Re-run it (`node
_tools/tests/r4b-test.js`) after any filter or sort JS change; the
fixture and the filter-JS extract are snapshots of the 2026-11-18
build — regenerate them from the current built page and generator
when either changes.

**What automation cannot check — the worker's pre-publish re-read.**
Before publishing, re-read every new or revised segment and confirm:

1. **Necessary content is in there, and only that.** Every item from the
   day's research that passed the bar (§1) is in the report, in the right
   section; every "New in the last 7 days" entry points to content that exists;
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
4. **Content order.** "New in the last 7 days" newest first; "What we're watching"
   soonest first; the new article sits in the right sub-section.

**UX and design editor — a dedicated review on every release
(adopted 2026-11-15).** Consistency in design is what makes the report
fast to digest, so every release that touches presentation — generators,
CSS, dashboard visuals, a new component — passes a dedicated design
review before it ships. It is a separate pass from the content re-read
and the automated checks, done with fresh eyes on the built page, and
it runs after Tier 1 passes and before pushing. The editor checks:

1. **Consistency.** The same kinds of things look the same: charts of
   the same kind use the same form; labels, headings, and card
   treatments follow the established patterns; a new element reuses an
   existing style rather than inventing one.
2. **Colour meaning.** A colour means the same thing everywhere it
   appears. Pie colours follow the split (§4): rust (#b3543f) is the AI
   side where the split is AI vs human; otherwise blue (#283060) is the
   favourable side, rust the adverse side, grey (#c9c2b0) the
   unclassified rest — the same hex values everywhere, never a third
   shade for the same meaning. The sentiment tint is a separate channel
   (pale ground vs saturated mark) and never redefines a wedge colour.
3. **Hierarchy.** The most important thing reads first; visual weight
   is proportional to the information's importance.
4. **Legibility.** Every number, label, and legend is readable at a
   glance, on desktop and on a phone: no text spilling, clipping, or
   wrapping awkwardly; no element depending on a font glyph that may
   not render.
5. **Pattern completeness.** A new element follows the established
   pattern for its kind — rating dots, source links, share anchors
   where they apply.
6. **Mobile.** The layout degrades gracefully: grids wrap, cards stack,
   nothing overflows horizontally.

Findings are fixed, re-verified, and only then released. When a design
question has no established pattern, the editor proposes one, records
it in §4, and applies it consistently from then on. The editor writes
the visual checks for the Tier 2 browser test, so what was reviewed is
what gets verified live. Design findings that change a decision go in
the release note to Yorgo.

**Tier 2 — visual review (when the generators or the design change, or
weekly).** Open the live site in a browser, desktop and mobile, and
check it against §4: masthead and H1 band render correctly; content
before masthead on mobile; the inline PAGE CONTENTS line is present on mobile
and absent on desktop; share buttons work (clicking one copies the link
and, for an article, does not toggle it); a shared article URL opens the
article expanded; no glyph renders as a weird character. A design change
is not done until the live site has been seen rendering correctly.

**Link health.** The daily verify run curl-checks all external links.
The Self-Audit page records the date of the last full manual link audit
(2026-11-12: all 94 unique URLs verified live).

---

## 6. Publishing

**Pre-release checklist.** Every release — content or presentation —
passes every line before it pushes. A miss-log entry adds a line here:
the checklist is revised after every miss, and the revision is part of
closing the miss.
1. verify.py under `TZ=America/New_York`: all checks passed, 0
   failures; every warning reviewed.
2. §5 six-point design review — mandatory when the release touches
   presentation; the design editor runs it after Tier 1 passes, before
   pushing.
3. Content re-read: the day's necessary content is in and only that;
   every rating accurate; every figure's attribution verified, not
   just its value.
4. New articles tagged (§2); feed entries inherit tags; findings
   export refreshed.
5. Layout balance (added 2026-11-19 — the paired-tile miss): no
   1-unit tile more than ~1.5× its row neighbours' height;
   double/triple tiles render at their declared size (horizontal span
   on web, vertical on phone).
6. Overflow/clip check (added 2026-11-19): no clipped graphics or
   text at desktop width and at phone width (Yorgo's phone where the
   VM cannot check).
7. Browser visual checks view WHOLE ROWS and sections, never an
   isolated tile.
8. QA-first for presentation changes: land on QA, Yorgo reviews,
   Chief Editor releases. Content-only watch runs publish directly.
9. Live check after pushing: the live site byte-identical to the
   build (Pages deploys lag; a stale edge is re-checked, not
   re-pushed).
10. QA mirror re-synced to the new prod.
11. Tile links land on headlines that state the tile's figure (added
    2026-11-19 — the 3.4× miss): every dashboard figure's link
    target is an article headlined with that figure — a secondary
    finding gets its own article, never a tile pointed at another
    finding's headline; ratio side rows name the cohorts, not the
    measure.

1. Edit the canonical Markdown at `~/workspace/your_files/watches/`
   (SYNTHESIZED.md, archive/ARCHIVE.md). The repo staging dir
   (`~/workspace/ci-sitrep/`) is a copy, not the source. Tag new
   articles per §2 (one tag line above the headline) as part of the
   same edit — the daily watch cron instructions carry the tagging
   step, so new articles never arrive untagged.
2. Sync the changed files into the staging repo.
3. Regenerate the HTML with the repo's generators (`build_html.py` for
   the report; `build_page.py` for the other pages; `build_audit.py`
   then `build_page.py` for the Self-Audit page, title "Self-Audit —
   CI SITREP"). `build_html.py` is always invoked with explicit
   input/output args — with no args it writes to
   `watches/SYNTHESIZED.html` WITHOUT the dashboard or tooltips. If
   ARCHIVE.md changed, rebuild archive.html too
   (rewrite its links to repo-root-relative form first).

**About numbers refresh.** The About page's "How this is made"
paragraph carries numbers that go stale every morning the watch runs.
They are regenerated from the audit data on every publish — never
hand-edited. Pipeline position: after build_audit.py, before
build_page.py builds about.html: `python3 _tools/refresh_about.py`
regenerates the paragraph in ABOUT.md from
`build_audit.compute_metrics()` (the same computation as the Self-Audit
page) plus the fixed values in site_config.py (`VERIFY_CHECK_COUNT`,
`ABOUT_CII_COUNT`, `ABOUT_TEAM_YEARS`). The wording is Yorgo's approved
text — only the numbers change; if the paragraph is reworded, the
script fails loudly and its template must be updated by hand to match.
`refresh_about.py --check` verifies the paragraph is current without
writing (exit 1 if stale). The "61 unique domains" clause stays out: it
is unverifiable from audit data. Update site_config.py when the
verify.py pass count, the CII role count, or the team's cumulative
years change. verify.py warns when its pass count differs from
`VERIFY_CHECK_COUNT` — that warning means the config is stale.

4. Refresh the findings export — the JSON database behind the YouTube
   channel (F-02): venv python `_tools/export_findings.py` (parses
   SYNTHESIZED.md, GLOSSARY.md, dashboard.json; writes
   data/findings.json and youtube/findings-inline.js). Run it after
   build_html.py — it cross-validates article ids against index.html.
   It warns rather than failing on articles with no parseable date (4
   known as of 2026-11-17); a warning for a NEW article means the
   report genuinely carries no date for it — note it and continue.
   Push data/findings.json and youtube/findings-inline.js with the
   other changed files (their generated_at timestamp changes on every
   run, so they are always "changed"). Exporter gauge matching keys on
   stable identifiers (the source), never on display text — a label
   reword must not drop a gauge.
5. Run the Tier 1 verification (§5) and the UX and design-editor review
   (§5). Do not push a failing build. Run verify.py under
   `TZ=America/New_York` — the freshness checks are ET-relative and
   the VM clock is UTC; under UTC, feed entries on their seventh day
   fail a day early. (build_qa.py runs verify.py internally, so it
   inherits the same requirement.)
6. Push the changed files with the API helper
   (`~/workspace/custom-connectors/custom.github/bin/github.py put`).
   Verify each put returns status 200 or 201. (SSH push is blocked by
   the VM egress proxy — HTTPS/API only.)
7. Verify the live site reflects the change (curl the live page and
   check for the new content). GitHub Pages deployments lag — sometimes
   several minutes. If the live page is stale but the repo content is
   correct via raw.githubusercontent.com, wait and re-check rather than
   re-pushing.
8. Append one row to `_tools/audit_log.csv` per run (date, distinct
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
- **2026-11-14** — Navigation adopted (breadcrumbs at the top of every
  section body; floating back-to-top button on all pages; back-to-report
  masthead + top-of-sidebar link on the sub-pages, with a mobile-only
  back link at the top of the content). verify.py's anchor check now
  strips `<script>` blocks before matching (JS string literals
  false-positived it) and checks for the back-to-top button.
- **2026-11-14 (evening)** — "State of the market" adopted (front-page
  macro synthesis above "New this week", 2–4 sentences, every claim
  grounded in the report's findings and linked to its evidencing
  section; revised when a material shift lands). Three front-page
  sections now start open. "New this week" entries carry plain-English
  section tags ([Pre-commit], [In codebase], [Agentic]) instead of
  "(subject 1/2/3)" parentheticals. FUTURE.md gained F-05–F-12 from an
  external reviewer's feedback: F-05 State of the market, F-06 monthly
  summary, F-07 plain-English NTW tags, F-08 "in practice" extension to
  §1, F-09 one findable contact point; F-10 (per-pillar Business Impact
  module), F-11 (per-link Strategic Implication sentences) and F-12
  (embedded CTAs) recorded as Dropped, with reasons. F-09 built the same
  evening: a "Work with Confluence<1>" masthead nav link to About's
  Contact section, the only conversion element on the report page.
- **2026-11-14 (late evening)** — Search adopted (F-13): a search box
  under the "As of" banner indexing the live page at runtime — no build
  step, no index file, no backend; searchable units are the share-button
  units (articles, headings, paragraphs, tables); report page only in
  v1. FUTURE.md gained F-14 (AI answers over the report, Proposed).
- **2026-11-14 (late evening)** — Glossary + tooltips adopted (F-15):
  `GLOSSARY.md` as the single source of truth (one line per term,
  alphabetical, letter headings), built to `glossary.html` with stable
  per-entry ids, and tooltips on first mention per subsection (dotted
  underline; hover/tap; link to the glossary entry). Terms are never
  removed; the daily watch adds new terms as part of its editorial pass.
  verify.py now checks the glossary (existence, alphabetical order,
  unique slugs, naming, tooltip data completeness, glossary-page ids).
- **2026-11-15** — Executive dashboard adopted (F-01): `dashboard.json`
  as the single source of truth (five panels, 51 figures, four deadline
  countdowns), built to `dashboard.html` by `_tools/build_dashboard.py`
  reusing the page template; every figure carries its credibility rating
  and links to the report section that evidences it; the generator
  validates every figure and exits 1 on a bad entry. Linked from the
  report page's masthead nav and the "How to read this" block. The daily
  watch maintains it (DASHBOARD step in the cron): update a figure when
  a headline number moves, update the deadlines the day a watched date
  lands, never invent a dollar figure for the money panel.
- **2026-11-15 (restructure)** — Brand in all-caps: "CI SITREP"
  everywhere on the site (repo and email address stay lowercase
  `ci-sitrep`). Main page restructured into rows + two top-level
  sections: row 1 As-of banner + Sections controls, row 2 search,
  row 3 "How to read this" (right-justified when collapsed), then
  EXECUTIVE DASHBOARD (the F-01 dashboard embedded from
  `dashboard.json`; `dashboard.html` is now a redirect to
  `index.html#executive-dashboard`) and REPORT (State of the market,
  New this week, What we're watching, §1–§3, Archive). The report's
  headings keep their levels, so every anchor survives. Masthead nav
  reordered (Self-Audit, Glossary, The names, Foundational theses,
  Archive, About, Work with Confluence<1>); the masthead heading
  (wordmark + tagline + Confluence<1> logo) is identical on every
  page. The Sections expand/collapse control moved out of the sidebar
  into the main content (row 1 on the report page, under the H1 on
  the content pages). Content pages start all-collapsed, including
  the theses page's Part headings (H1s). verify.py now checks the
  top-level section order, the new layout markers, and the all-caps
  brand (52 checks).
- **2026-11-15 (deep links)** — Dashboard figures now link to the
  report article that evidences each figure (the article's runtime id),
  not the section top — Yorgo's correction: section links were nebulous
  and the round trip to the primary source must complete. Six figures
  carry an "also" link to a second evidencing article in another
  subsection. The three §3.6 figures keep the section anchor (§3.6 is
  prose, not articles). `build_dashboard.py` gained `compute_article_ids()`
  (a Python replica of the share JS's slugify + uniqueId) and validates
  article links against it; verify.py's anchor check accepts the same
  computed ids.
- **2026-11-15 (evening)** — Row 1 revised: "How to read this" moved
  into row 1, centered between the As-of banner and the Sections
  controls (row 3 is gone); when opened it drops to a full-width line
  below the row. First-open state reversed: only the two top-level
  sections start open — the front-page sections and dashboard panels
  now start collapsed, as one line each (they started open since
  2026-11-13/14). "Collapse all" returns the page to that initial
  state: it closes everything except the two top-level sections — this
  also fixes a real defect Yorgo found, that Collapse did nothing on
  first load (the only open headings were the ones the handler
  skipped). Geography focus adopted (§1): US, NYC, investment
  management, hedge funds, MGAs — US evidence leads; UK/EU/APAC items
  enter when they bear on US firms and are labelled with their
  jurisdiction. First application: the ACA/NSCP 2026 AI Benchmarking
  Survey article (§3.4, 60th article) and a US-led dashboard finance
  cut (86% of US firms use AI, 1 in 4 experimenting with agentic AI,
  38% formally test outputs; the UK BoE/FCA 80% deployed-agents figure
  kept as the comparison point).
- **2026-11-15 (late evening)** — Top-level headings in all-caps text
  (EXECUTIVE DASHBOARD, REPORT) on the page and in the TOC, so they
  read as different from their constituents; the anchor ids stay
  lowercase, so every link survives. Bottom-line strip built (F-01):
  seven items above the countdown, in Yorgo's order — profitability
  ("Insufficient data", no rating, links to the money panel), AI
  writes ~half the code (JetBrains ~47%), 86% of US firms use AI
  (ACA/NSCP), AI patches 11× the vulnerabilities (Sajadi), verification
  costs 2.5× (SusVibes), 79% run agents (SailPoint), 188 documented
  damage cases (Cyera) — each linked to its evidencing article, each
  carrying its rating except the profitability item. verify.py gained
  a layout marker for the strip (53 checks).
- **2026-11-15 (late evening)** — Bottom-line strip charted (F-01):
  the cards now carry graphics where the figure has one — a donut for
  the ~47% AI code share (AI 47% vs human 53%), bars for the 86% and
  79% adoption rates, comparison bars for the multipliers (Sajadi 135
  vs 12 vulnerabilities; SusVibes 2.5× vs 1× review cost); the 188
  count has no chartable comparison in the report, so it keeps the big
  number. Layout is 3+3+1: three 1-unit tiles, the 2.5× tile plus the
  paired double tile, then the 188 tile alone, then the profitability
  item full-width last (dashed border, bignote background) — which
  also fixes the "Insufficient" text spilling out of its card at the
  old width. The countdown strip got a heading in
  the same style ("COUNTDOWN"). Strip charts are inline SVG and CSS
  bars, no library; the build validates chart kinds, values, and bar
  tones.
- **2026-11-15 (late evening)** — Strip charts revised (F-01): all
  three percentages are now pie charts with the number NEXT TO the pie
  (the donut and the progress bars are gone); both comparison bars use
  one colour scheme matching the pies — rust (#b3543f) is the AI side,
  blue (#283060) the not-AI side (AI patches rust vs human patches
  blue; the review cost blue — the review is the human side — vs
  generation alone rust). The profitability card has the same
  background as the other cards now (the distinct background is gone;
  the dashed border stays) and its graphic is a question mark inside a
  circle.
- **2026-11-15 (late evening)** — UX and design editor (Yorgo's
  direction): a dedicated design review is now part of the rules-based
  pre-release review (§5) on every release that touches presentation,
  with a six-point checklist — consistency, colour meaning, hierarchy,
  legibility, pattern completeness, mobile — run after Tier 1 passes
  and before pushing; findings are fixed and re-verified before
  release, and new patterns get recorded in §4.
- **2026-11-15 (late evening)** — Masthead credibility legend is now a
  collapsed `<details>` (summary "Credibility rating", starts closed)
  instead of an always-open block — it is reference material, used
  once per reader; the dots stay explained in "How to read this" and
  carry their words in the dashboard.
- **2026-11-15 (late evening)** — Strip cards are now whole-card
  links: the browser test found clicking a strip card's number or
  chart did nothing — only the small source name linked to the
  evidencing article, which contradicted the dashboard intro's promise
  that every number links to its article. Each strip card is now one
  `<a>` to its evidencing article (source name plain text, no nested
  link), the same pattern as the countdown cards. Panel figures keep
  the source-name link (their "also" second links rule out a
  whole-card wrap).
- **2026-11-15 (late evening)** — Masthead contact section (F-09
  rework, Yorgo): the "Work with Confluence<1>" nav link is gone,
  replaced by a small Contact section in its place (after the nav,
  before the legend) with two mailto addresses — ci-sitrep@ for
  errors, omissions, and feature requests; hello@confluence1.com for
  working with Confluence<1> (picked for the classy feel; the
  catch-all routes to Yorgo, so it can change in one line). The About
  page's Contact section lists both in the same words. The legend's
  closed state was also fixed the same evening: its padding-bottom
  and the summary's margin now apply only when open, so the collapsed
  line has no blank space under it and reads as expandable.
- **2026-11-15 (late evening)** — Share buttons on dashboard cards
  (Yorgo: "very important"): every bottom-line strip card and every
  countdown card now carries a share button in its top-right corner,
  hidden until hover like the article buttons (Yorgo loves the
  hover-hidden pattern — keep it). The button is a sibling of the
  card's link, never nested inside it. Strip ids bl-<article-slug>,
  countdown ids cd-<deadline-slug>. The profitability card's dashed
  border was made more pronounced the same evening (2px, muted gray —
  it was 1px in the hairline color and Yorgo hadn't noticed it).
- **2026-11-15 (late evening)** — "New this week" renamed "New in the
  last 7 days" (Yorgo: "this week" reads as a calendar week starting
  Monday or Sunday, but the section is a rolling 7-day window — the
  name was misleading). The window itself is unchanged at 7 days (3
  would be too thin after a quiet stretch, 5 is arbitrary, a calendar
  week would be worse — one day on a Monday). The section id is now
  #new-in-the-last-7-days; the generators, verify.py, build_audit.py
  (its "Items new this week" label is now "Items new in the last 7
  days"), the cron, and these rules all use the new name. A
  user-selectable window (3 / 7 / 14 / 30 days) was assessed the same
  evening and held — it solves catching up after time away, which the
  report body already does; the rename solves the misleading part.
- **2026-11-16 (morning)** — "How to read this" guide reordered
  (Yorgo): "How to read it" and "Short on time?" now come before "New
  to the terms?" — they were buried after the terms paragraphs. The
  masthead legend was renamed "Credibility rating scale" the same
  morning (was "Credibility rating").
- **2026-11-17 (morning)** — Dashboard bar rows now lead with the
  number (Yorgo: the percentages at the end of the line were a
  less intuitive read than at the front). Value first, label after,
  in the panels and in the bottom-line strip's comparison bars —
  each row reads as a sentence, and the bar underneath still carries
  the magnitude comparison. No good reason for the old layout: it was
  a dashboard convention, and the labels were already written as
  continuations of the number. `.bar-head` is now a plain block so
  the sentence wraps naturally on narrow screens.
- **2026-11-17 (afternoon)** — Vocabulary pass (Yorgo): the rating is now
  the confidence rating (was credibility rating) — the dots rate the
  finding, not just its source, so the definition now reads "how much
  confidence you can place in its finding". CIA is now CII (ci
  individual) and CIAC is now CIC (cii collective), for symmetry with
  the human-side terms and because CIA collides with the Central
  Intelligence Agency; "special forces" is now "elite operators".
  CIA/CIAC stay in the glossary as "formerly" entries (terms are never
  removed). The taxonomy draft's credibility dimension is now
  confidence. Changelog entries above keep the terms as they were when
  written.
- **2026-11-17 (evening)** — CI vs EI page (F-17/ATAK, Yorgo): the
  baseline audit classified all 42 performance figures in the report
  and dashboard — 3 complete pairs, 12 partial comparisons, 27 gaps —
  and the dedicated CI vs EI page presents them in three family
  sections (Development, Operations, Business-composite), versioned
  and dated with a Changes log. A comparison counts only on the same
  task with the same metric; gaps read "No human baseline published".
  The page is linked from the masthead nav after Glossary. Pair-table
  pattern adopted (§4): CI column rust, EI column navy. Glossary
  gained EI, EII, EIC (90 terms). The daily watch maintains the page
  and the audit when a new article publishes a human baseline.
- **2026-11-17 (evening)** — Findings export added to the publish
  pipeline (F-19/F-02): `_tools/export_findings.py` regenerates
  data/findings.json + youtube/findings-inline.js after build_html.py
  on every publish; the export is the first F-02 database file (81
  articles, what's-new, glossary, deadlines, gauges) and feeds the
  YouTube broadcast scene (youtube/scene.html) and the review table
  (youtube/review.html).
- **2026-11-18** — Dashboard tile system recorded in these rules
  (F-01/F-02): eight tile types, one per stat kind (pie, ratio,
  big-number, no-data, sparkline, flag, note, waffle); `pie_split`
  replaces the `ai_side` boolean (six values, identity beats valence,
  grey `#c9c2b0` for the unclassified rest; range-pie remainder as a
  wedge, never a full circle); sentiment is the tile's background tint
  (blue/rust/grey), superseding the word-pill; standardized 1/2/3-unit
  cards (width units, natural height, dense flow, 1100px + 600px
  breakpoints); Search/Filter/Sort in one collapsible panel at the
  top, filtering the whole report page (sort tiles-only; sector control
  removed, tags kept in data); masthead reordered (How to read this →
  SITREP sections → PAGE CONTENTS → legend → Contact → ©) with a
  phones-only row-1 copy of How to read this; `dashboard-history.json`
  (append-only, 4 series) with the sparkline promotion and caption
  rules; tagging rules (mirrored pairs, company, composite dates, field
  order) and the tag join; stable per-figure `key` (decided; migration
  pending); filter-JS harness
  under `_tools/tests/` (69/69). verify.py extensions proposed, not
  implemented (derived tile-count check, masthead-order assertions).
  About "How this is made" numbers refresh from the audit data on
  every publish (`_tools/refresh_about.py`, option (a) — Yorgo's
  pick); verify.py warns when its pass count differs from
  `site_config.VERIFY_CHECK_COUNT`. Release 2026-11-18 (evening):
  ninth tile type `paired` (BCG strip tile replaces SailPoint 79%);
  ratio-side tones follow the same identity-first-then-valence
  procedure as pies; verify.py runs under TZ=America/New_York
  (freshness checks are ET-relative); FCA CP26/38 weekday corrected
  (Thu 24 Dec, not Wed).

- **2026-11-19:** Corrections page (`CORRECTIONS.md` →
  `corrections.html`): every correction and omission fix listed
  newest-first, one line each; the daily watch adds an entry as part
  of the same publish that lands the fix; entries never removed. Nav
  order gains Corrections after Self-Audit.
- **2026-11-19** — One tile size (Yorgo, after the paired tile
  rendered ~2× taller than its strip neighbours; the apparent row-1
  pie clip in the screenshot was his red annotation, not a rendering
  defect): every 1-unit and 2-unit tile is exactly 280px tall at
  multi-column widths, source line pinned to the bottom, short tiles
  vertically centred; content fits by budget (labels ≤ 84 chars,
  legend rows ≤ 36, source ≤ 99/146, notes ≤ 190) enforced by a
  build-time height estimator (FAIL above 290px, WARN 281–290px
  tolerance band, decided by the live whole-row check); the paired
  tile is now a double (2 units wide, figures side by side, 72px pies,
  vertical hairline divider; halves stack on phones); the strip is
  3+3+1 with the trailing hole consolidated bottom-right; on phones
  the fixed height lifts (natural height, single column). 3-unit tiles
  (money bignote, profitability) and countdown tiles keep natural
  height. Pre-release checklist added to §6 (10 lines incl. layout
  balance, overflow/clip, whole-row visual checks), revised after
  every miss.
- **2026-11-19 (evening)** — Tile-link headline rule (§2) and ratio
  side-row rule (§4): a dashboard figure's link target must be an
  article headlined with that figure — a secondary finding buried in
  another article is split into its own article (headline the
  finding) and the tile repointed; ratio compare-chart arms name the
  cohorts being compared, never the measured quantity. Prompted by
  the 3.4× tile, which linked to the 2.5× post-hoc-review article
  (the 3.4× was one bullet in six) with arms reading "AI code vs AI
  code". §6 checklist gains line 11.
- **2026-11-19 (late evening)** — Strip grows to eight items: the
  3.4× SusVibes figure promoted to a DOUBLE ratio tile (one figure in
  a 2-unit card, §4); the strip is three full rows of three units, the
  two doubles offset by one column, the vulnerability pair (3.4× +
  11× waffle) together in row 1 — Yorgo's pick. The 3.4× finding split
  into its own article (98 articles, 14E/30C/49R/5Cl). §2 strip clause
  updated to 8 items / 9 units / 3×3.
- **2026-11-20** — "State of the market" renamed "Situation at hand"
  (Yorgo's pick): the front-page macro synthesis section, its anchor
  (`#situation-at-hand`), the findings-export key, the broadcast scene
  headline + voiceover + slide id, and the watch-cron instructions all
  carry the new name. Historical changelog and archive entries keep
  the old name.
