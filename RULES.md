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

**Row 1** — the As-of banner and the Sections expand/collapse controls,
on one row (banner left, controls right).
**Row 2** — the search box (§4).
**Row 3** — **How to read this**, one collapsed block holding everything
before "New this week" (the intro line, the credibility legend, the
caveats). Right-justified when collapsed; full width when open. It must
not attract attention.
The mobile inline Contents sits between row 2 and row 3 (hidden on
desktop); the sidebar Contents lives in the masthead (§4).

Then the two top-level sections, both starting OPEN:

1. **EXECUTIVE DASHBOARD** — the F-01 dashboard, embedded from
   `dashboard.json`: the bottom-line strip (seven items, Yorgo's pick,
   in his order — the profitability item reads "Insufficient data" and
   links to the money panel), the countdown strip and the five panels,
   every figure linked to the report article that evidences it. (The
   standalone dashboard page is gone; `dashboard.html` redirects to
   `index.html#executive-dashboard`.)
2. **REPORT** — the report itself, in this order:
   - **State of the market** — a 2–4 sentence macro synthesis, the first
     thing a new reader actually reads. Every claim in it is grounded in
     the report's own findings and traceable via an internal link to the
     section that evidences it (the flaw rate to §1.6, the governance gap
     to §3.4.3, the regulatory picture to §3.4.2). Revise it whenever a
     material shift lands that changes the macro picture; never let it go
     stale or contradict the sections below it. No generic marketing
     claims — every sentence must be defensible from the report.
   - **New this week** — a rolling 7-day window. Entries older than 7 days
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
     (it becomes an article and a "New this week" entry instead). A past
     date or a landed item still listed is a defect.
   - **§1, §2, §3** — the three content sections, in that order.
   - **Archive** — a pointer to the archive page.

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
figure carrying its value, label, source, rating, date, and a link to
the report article that evidences it, plus a `bottom_line` list (seven
items rendered as a strip above the countdown — rating and date
optional, since the profitability item has neither) and a deadlines
list for the countdown strip. The link is the article's runtime id (assigned by the
share JS from the headline) — a section anchor is not specific enough:
the reader must land on the article itself, where its Source line
takes them to the primary source. Where a conclusion draws on a second
headline article in another subsection, the figure carries an "also"
list ({anchor, label}) rendered after the source name. The one
exception is §3.6 (Evaluation), which is prose, not articles: its
figures link to the section anchor until the content becomes articles.
It is embedded in the report page as the first
top-level section (EXECUTIVE DASHBOARD): `build_html.py` imports
`_tools/build_dashboard.py` to render it, and validates every figure
against the generated `index.html` (required fields, rating in the
four levels, bar values 0–100, link anchors exist in `index.html` or
among the computed article ids) —
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
(audience-first), not numeric.

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
Finance" sits on its own line under "CI SITREP", italic. H1 and masthead
title use a serif stack to match the Confluence<1> logo font. Body text
is sans-serif. The design is FT-inspired: upscale, quiet, paper-like.

**Masthead.** The left sidebar is a publication masthead. The heading
is identical on every page: the CI SITREP / Code & Finance wordmark +
tagline ("Created Intelligence in code and finance — as of today."),
and the "by Confluence<1>" wordmark (the "Confluence <1>" text from
the logo, cube cropped out) — the logo stays in the masthead
everywhere, all the time. On the report page the heading is followed
by the nav links, in this order: Self-Audit, Glossary, The names: CI,
CIA, CIAC, Foundational theses, Archive, About — then the credibility
rating legend (heading: "Credibility rating"), the Contents index,
and the copyright line "© 2026 Confluence<1> Corp. All rights
reserved." The nav ends with one restrained conversion link — "Work
with Confluence<1>", jumping to About's Contact section — set apart
from the content links by a separator line. It is the only conversion
element on the report page; no CTAs inside the content (see F-12,
Dropped). On the sub-pages the heading is followed by a "← Back to
the report" link and the Contents index (see Navigation).

**Section headings.** The two top-level sections (EXECUTIVE DASHBOARD,
REPORT) are the visual top of the hierarchy, their heading text in
all-caps so they read as different from their constituents (title case
until 2026-11-15, when Yorgo asked for caps); the three content
sections (§1, §2, §3) sit inside Report. The meta-section headings
("State of the market", "New this week", "What we're watching",
"Archive") are de-emphasized: smaller, lighter weight, muted color.

**Collapse behaviour.** Only the two top-level sections start OPEN;
everything inside them — the three front-page sections ("State of the
market", "New this week", "What we're watching"), the dashboard panels,
the content sections — starts collapsed, as one line each. (Before
2026-11-15 the front-page sections and dashboard panels also started
open; Yorgo reversed that — the page opens as a clean outline, and the
reader drills in.) Article headlines are native `<details>` and
start collapsed. Jumping to an anchor auto-expands its ancestors —
including the target heading itself. "Collapse all" returns the page to
its initial state: it closes everything except the two top-level
sections. "How to read this" is regular weight, italic, muted — not
attracting attention; it sits centered in row 1, between the As-of
banner and the Sections controls, and drops to a full-width line when
opened. On the content pages (About, Explainer, Theses, Archive,
Self-Audit, Glossary) everything starts collapsed, including the theses
page's Part headings (H1s other than the page title). The Sections
expand/collapse control lives in the main content — row 1 on the
report page, under the H1 on the content pages — never in the
sidebar, where it was lost.

**Mobile.** Content comes before the masthead (CSS `order`: main first,
sidebar second). A native `<details>` "Contents" line sits in the main
content between the search box (row 2) and the dashboard section;
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
  to the top. The arrow is inline SVG. On all six pages.
- **Back to the report.** On the content pages (About, Explainer,
  Theses, Archive, Self-Audit, Glossary): the sidebar opens with the
  same masthead heading as the report page (linked "CI SITREP / Code
  & Finance" wordmark + tagline + "by Confluence<1>" logo), followed
  by a "← Back to the report" link above the Contents list. On mobile
  the sidebar sits below the content, so those pages also carry a
  mobile-only back link at the top of the main content, right under
  the page title.

**Share links.** Article headlines, substantive paragraphs, tables, and
headings each carry a small link-icon button that copies a direct URL
(page + #anchor) with a "Copied" confirmation. The icon is inline SVG —
no font glyph. Buttons appear on hover on desktop and are always visible
on mobile. Ids are generated deterministically in JS from slugified text
(60-char cap, dedupe -2/-3 suffixes), so a copied link resolves
identically on any later load. Clicking an article's button never toggles
the article; a shared article link opens the article expanded. Excluded:
See also blocks, the How-to-read block, the mobile Contents block.

**Search.** A search box on the report page (row 2, under the As-of
+ controls row) — the report is reference material, and readers need
to find their way back to information they saw. It indexes the live page
at runtime on first keystroke: no build step, no index file, no
backend, no cost, and always in sync with the daily watch (it reads the
page, so it needs no cron step). Searchable units are the share-button
units (articles, headings, substantive paragraphs, tables) plus
standalone list items in a section body — the best-practice bullets and
the "New this week" / "What we're watching" entries (top-level `<li>`
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
links in the HTML; all internal anchors resolve — article ids
assigned at runtime by the share JS are accepted via the computed id
set, see §2 Dashboard), freshness (no "New this
week" entry older than 7 days; no past date in "What we're watching";
"Last updated" not in the future), order ("New this week" newest first;
"What we're watching" soonest first; section and subsection order),
naming (Confluence<1> everywhere, with the one documented Atlassian
exception; brand all-caps CI SITREP; current section names), hygiene
(no internal-process strings on the public page), and layout markers
(As-of banner, mobile Contents, credibility legend, copyright line,
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
   CI SITREP"). If ARCHIVE.md changed, rebuild archive.html too
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
