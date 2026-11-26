# CI SITREP — Editorial Rules

The single source of truth for how this report is made: what gets in, how
it is written, how it looks, and how it is checked. The daily watch cron
implements these rules; when a rule changes, update this file and the cron
instructions together.

**Change control:** every rule here is a decision Yorgo made or approved.
A rule changes only on his word. Record the change in §7 (changelog) with
the date.

**Scope:** this file governs the report itself (SYNTHESIZED.md and the
generated website). The publication's future features live in FUTURE.md. The
tagging taxonomy lives in TAXONOMY_DRAFT.md (approved v3, 2026-11-25).

---

## 1. Selection — what gets in

**The bar.** Something enters the report only if it could change how a
firm building critical systems in finance should act — its offerings, its
controls, its budget, its risk posture. Routine news, vendor marketing,
and minor updates do not qualify.

**The grid — how the report names what it covers (2026-11-25).** The
governing principle: name what the user is GETTING (descriptors of what
is analyzed), never the tool's structure; a good tool goes unnoticed.
All information sits in a three-dimensional grid: **Levels** (zoom
levels — from Evidence at the base through Analysis, Dashboards,
Situation at hand, The bottom line, to The heatmap at the top),
**Domains** (the areas of concern regarding the surge itself), and
**Verticals** (the business end of the reader's life — Finance now;
Health, Defense, Public Sector later). The internal word "slice" is
never reader-facing; the reader word is "domain". **The bottom line**
is the most distilled takeaway (the prose abstract — you can't get
more distilled than the bottom line); **Situation at hand** is the
more comprehensive situational picture (the strip, the countdowns, the
ledger). The two names were inverted on 2026-11-25 to match what they
describe; anchors follow their labels. The site is a **website**, not
a "file".

**The four domains** (in this order on every surface):

1. **PNL (profit and loss)** — money, adoption, liability: what AI
   costs, what it returns, how fast it is spreading, and who pays when
   it goes wrong. The reader's question is "what does this do to my
   numbers?" An article is PNL-primary when its headline finding is a
   dollar figure or ratio of dollars, a quantified business outcome, an
   adoption or scale figure, a liability or exposure ruling, or a dated
   obligation with a cost consequence. **The boundary:** "everything
   has P&L implications" is NOT the test — the finding itself must be
   stated in business terms (money, share, outcome, liability), not
   have a business consequence derived from it. A rate ratio of
   vulnerabilities is not PNL; a ratio of costs is. **Regulation lives
   in PNL (§1.4 Regulation & enforcement), not CIC** (Option B,
   Yorgo's verdict 2026-11-23): CIC keeps the governance firms build
   themselves; PNL holds the governance regulators impose. The seven
   frontier-lab regulation articles moved with the cluster.
2. **CIC (Agentic Staff)** — the agent workforce: how agents are
   designed, built, deployed, governed, managed, and evaluated, and
   what happens when they act, fail, or are attacked. The reader's
   question is "how do I run this workforce, and what is it doing?"
   Incidents where the agent is the actor — or the exploited party —
   are CIC, even when the damage lands on code. **Boundary with
   Certification:** an incident about a *poisoned artifact* (a bad
   skill, a backdoored package, a CVE in shipped code) is
   Certification; an incident about *agent behaviour* (an agent
   installing from memory, an agent exploited through its instructions,
   an agent escaping its sandbox) is CIC. When both are true, the
   primary follows the finding's lead.
3. **Codebase Certification** — attesting what is already there:
   measuring, attesting, and verifying the state of code already
   written, shipped, or deployed, and the fix loop that changes that
   state (measure → attest → fix → re-verify → re-attest). The
   reader's question is "what is the state of my codebase, and can I
   prove it?" The line against Pre-commit is *when* the code is judged:
   already in the codebase (Certification) vs at generation
   (Pre-commit).
4. **Code Sanitizing Pre-commit** — stopping bad code getting in:
   cleaning CI-generated code before it enters the codebase — while the
   agent writes it and at the point of commit (agent-time enforcement,
   PR/CI gates, LLM review). The reader's question is "how do I stop
   bad code getting in?" Confluence<1> builds its own tools in this
   space as well as advising on and deploying others'.

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
source's wording to fit our framing. CIC always appears as "CIC
(Agentic Staff)" in full on first use per page. The product is always
"CI SITREP"; bare "SITREP" is the dashboard surface only.

**Agent reliability** is covered inside the CIC domain (the CIC intro
names reliability as "the binding constraint, not capability"; the
Evaluation subsection covers pass^k vs pass@1, METR time horizons,
ThinkingBox, "never trust an agent's self-reported PASS"). It is not a
separate watch.

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

**The site structure — levels as pages (2026-11-25).** The levels
variant is THE site structure: four level pages — SITREP, DIFF,
Landscape, BACKGROUND — plus the BACKGROUND sub-pages. Articles do not
have separate pages; they all live on the Landscape page. (The
single-page build is retained for the record; its verify bar is 81 —
the release bar is the variant's 85, §5.)

**SITREP page, in order:** the H1 banner (with the as-of date, §4);
**The bottom line** — the prose abstract, a standalone expandable box
first below the header, starting collapsed (§4); the dashboard
(F-01, embedded from `dashboard.json`): the "What this is" explainer
(collapsed by default — the reader needs to know what the surface IS
before any content), then **Situation at hand** — the comprehensive
situational picture in figures: the bottom-line strip (eight items in
nine units, three full rows of three, in domain order PNL 4 / CIC 2 /
Certification 1 / Pre-commit 1; the WHOLE strip tile is one link to
its evidencing article) and the net-impact ledger last; then the four
**domain dashboards** (PNL dashboard, CIC (Agentic Staff) dashboard,
Codebase Certification dashboard, Code Sanitizing Pre-commit
dashboard) in that order, every figure linked to the article that
evidences it (§4 tile→bullet deep link). The SITREP level opens as a
standard collapsed view: only the surface H2 starts open; The bottom
line, Situation at hand, Net impact, the four domain dashboards and
their panels all start collapsed (§4).

**The bottom line (the abstract).** The markdown source keeps
`## Situation at hand` as four paragraphs, one per domain in domain
order; only the render moves it into the box labelled "The bottom
line" (the names were inverted 2026-11-25 — §1). Every claim in it is
grounded in the report's own findings and traceable via an internal
link to the section that evidences it. Revise it whenever a material
shift lands that changes the macro picture; never let it go stale or
contradict the sections below it. No generic marketing claims — every
sentence must be defensible from the report. A fixed fifth paragraph
follows the four domain paragraphs — "**Researcher, scientist, deep
diver?** BACKGROUND holds the research and development this is derived
from." — generator-appended after the four abstract paragraphs; the
watch owns only the four domain paragraphs and cannot touch it.

**DIFF page — "what happened and what's coming".** DIFF is the changes
surface: the feed (what happened) + the watchlist (what's coming),
one surface with one toggle; the watchlist is an H3 inside the DIFF
body (never a peer H2 — §6 DOM-vs-rendered lesson). The heading
carries its tagline in the heading itself: "DIFF — What changed and
what's coming (N entries)". The feed is a rolling 7-day window;
entries older than 7 days drop off. Every entry is dated with the date
it was ADDED to the report, carries a finding-first title (§3), and
links to where the article lives. Entries are in strict newest-first
order in the markdown (flat); grouping happens at render time: a
**Today (N)** group first (entries dated today, America/New_York —
moved out of their domain groups, not duplicated; the heading gains
"· N new today" only when N>0), then the four domain groups in domain
order, then the Countdown block, then **What we're watching**. Feed
tags (`[PNL]` / `[CIC]` / `[Certification]` / `[Pre-commit]` and
`[new]` / `[updated]`) are internal bookkeeping only — stripped at
build time, never rendered (§4). **What we're watching** — dated
upcoming events (comment deadlines, effective dates) and open
questions the report is tracking. Dated items are in soonest-first
order. Every item links to its section. Maintain it every run: add a
new item when research surfaces one; remove an item the day it lands
(it becomes an article and a DIFF feed entry instead). A past date or
a landed item still listed is a defect. The watch keeps writing
`## What we're watching` in the markdown as before; the build places
it inside DIFF. The regulation countdown tiles live in the watchlist
(first block under the Countdown heading); countdowns are undotted
(§4).

**Landscape page** — the full knowledge base of findings ("Landscape —
the complete picture"): the four domains (§1 PNL, §2 CIC, §3
Codebase Certification, §4 Code Sanitizing Pre-commit) with all
articles in their subsections. Section headings and article-bearing
subsection headings carry build-time counts ("PNL (36 articles)") —
in the body and in the masthead map. Generator-only — the markdown
stays clean. Heading counts never leak into breadcrumbs or
search-index titles/paths (`cleanText` strips `.section-count`).
Feed-group headings and domain-dashboard headings carry counts the
same way. One-line definitional intros per domain; the PNL heading
carries the honesty note ("The money evidence is thin and growing —
this section leads because the question matters most, not because the
evidence is thickest.").

**BACKGROUND page** — the consolidated reference page: About,
Self-Audit, The names, Glossary, R&D, Archive in that order (anchor-first
nav; each standalone page carries an "In BACKGROUND →" return link).
R&D is a BACKGROUND subsection holding the research: the Diffusion
Gauge tool (tracker.html) and The Surge Monitor white paper
(tracker-whitepaper.html), plus CI vs EI and the Foundational
theses. Self-Audit sits in BACKGROUND, second after About — never
buried under SITREP.

**How to use the SITREP** (the five lines, navigation only): (1) the
map (SITREP numbers / Landscape evidence, same four domains); (2)
first time (the bottom line, or the whole Landscape); (3) short on
time or back for the day (the bottom line, then DIFF, or follow the
red dots); (4) pick-and-open; (5) terms + keep-opening. Plus the
pointer line to Self-Audit and the Confidence rating scale. The bar
lives on Self-Audit; the rating definitions live in the masthead
legend (the fullest wording + action guidance). The block renders as
the entry modal (§4) and as the sidebar reference copy — one source,
emitted twice, so the copies cannot drift.

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
order. **Subject (taxonomy v3, 2026-11-25):** values are the four
domain words `pnl`, `cic`, `cert`, `san`, **primary-first** — the
first value is the article's home (the generator uses it for
placement; both values are used for filtering). `0` (cross-cutting)
is dropped. Feed tags are `[PNL]` / `[CIC]` / `[Certification]` /
`[Pre-commit]` (internal only — §4). **Mirrored pairs:** the same
finding mirrored in two domains carries both subjects on both
instances; distinct findings from the same source stay domain-pure.
**Company** is the item's subject, not its source: a named recurring
benchmark, instrument, or report counts its maker; one-off studies
and surveys of third parties do not tag their measurer or publisher.
**Dates:** the headline source's date when one exists, else the
most-recent constituent. The tag join parses SYNTHESIZED.md directly
(`build_dashboard.py`'s shared parser — one parser, never
duplicated): articles and tiles carry `data-*` attributes from their
tag lines for the filter panel (§4). `data-company` is comma-joined
— company values contain spaces — all other dimensions space-joined.

**Changed-part marking (2026-11-23).** When the watch changes an
article because of news, it marks the changed part at edit time; the
build renders the highlight (§4) and enforces the marking. Three
marker forms: `<!-- changed YYYY-MM-DD -->` appended to a bullet line
(the whole bullet is the part); `<span data-changed="YYYY-MM-DD">…</span>`
for prose or a partial bullet (exactly the wrapped text); `"changed":
"YYYY-MM-DD"` on a dashboard figure (the numeral only). Mark
**substantive** changes only (new fact, corrected number, changed
conclusion) — cosmetic fixes (grammar, clarity, a fixed link) are not
marked; only the editor can make that call. **New articles: dot only**
(the whole article being new is what the dot says); **updated
articles: dot + per-part highlight**. Feed entries carry `[new]` or
`[updated]` after the domain tags (build-only — §4): an `[updated]`
entry whose article has no live marker (and no figure with a live
`changed` date) FAILS the build; a post-launch entry with neither tag
also FAILS. The watch runs `clean_changed_markers.py` at run start
(strips expired markers; expiry is render-time, so a skipped cleanup
costs source clutter, never a wrong render). A weekly git-diff audit
(Monday ~07:00 ET) diffs the week's SYNTHESIZED.md versions after
stripping markers from both, flags content changes with no marker,
and reports to Barnaby — it never writes to SYNTHESIZED.md. The
highlight lives and dies with the dot: same 7-day window
(`CHANGE_WINDOW_DAYS = 7`, America/New_York), same consumption (§4).

**See also cross-links.** One-line collapsible blocks at the end of
sub-sections, linking related sections across the four domains. When a
new item is cross-cutting — the same evidence, control, regulation, or
watch item in two places — add a See also line in BOTH places. Link only
where the related section changes a decision, not for mere topic
similarity.

**The audit page** (Self-Audit) is generated from the live files by
`_tools/build_audit.py` — never hand-edit it. Its Coverage section links
to "What we're watching" rather than maintaining its own known-gaps list.
Self-Audit sits in BACKGROUND, second after About (§2 above).

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
`GLOSSARY.md` means regenerating `glossary.html` and every page that
inlines the tooltip data (the tooltip data is generated from it at
build time).

**Dashboard.** `dashboard.json` is the single source of truth for the
SITREP dashboard (F-01): the Situation at hand strip + net-impact
ledger, then the four domain dashboards of at-a-glance figures, every
figure carrying its value, label, source, rating, date,
and a link to the report article that evidences it, plus a `bottom_line`
list (eight items in nine units — three full rows of three, in domain
order; rating and
date optional, since the profitability item has neither; each item
carries a tile where its figure has one — a pie tile for a percentage
(number next to the pie, block-level legend rows), a ratio tile for a
multiplier, a waffle tile for a count-share, a big-number tile for a
count, a paired tile for two figures from one finding, a question mark
in a circle for the profitability item, which
has no data — pie colours follow the split, §4; and the profitability
item is full-width, last, with `"full": true`) and a deadlines
list for the countdown tiles (rendered in DIFF, §2 above). Tile ids derive from the figure's stable
`key`, never from its label slug — a label reword must not break a
shared tile link. (Decided 2026-11-18; migration pending — no figure
carries a `key` yet, and ids still derive from label slugs until it
lands.) Every pie-family figure carries `pie_split` (§4); the
segmented pie carries a per-segment `tone` instead. The link is the
article's runtime id (assigned by the share JS from the headline) — a
section anchor is not specific enough: the reader must land on the
article itself, where its Source line takes them to the primary
source. The link target's headline must state the tile's figure — but
only for figures rated ●○○○ (Claimed): a reader who clicks a
one-dot tile lands on an article headlined with the finding they
clicked. A figure rated ●●○○ (Reported) or better may link to an
article that does not headline its figure (Yorgo, 2026-11-21) — the
confidence carries it, and the split rule below does not apply to
it. If a Claimed figure is a secondary finding inside an article
headlined with something else, split it into its own article
— headline the finding, same source, same rating — and point the
tile at the new article. Never point a one-dot tile at an article
whose headline is about a different finding, however good the
evidence buried in its bullets. (2026-11-19: the 3.4× strip tile
linked to the 2.5× post-hoc-review article, where the 3.4× was one
bullet in six; Yorgo caught it from a QA screenshot.) Since
2026-11-20 the rule is enforced mechanically:
`build_dashboard.validate()` fails the build when a Claimed
figure's display numerals are absent from its target headline,
except figures listed in `HEADLINE_KNOWN_MISMATCHES` (which warn)
and theme-headlined articles (which warn); a `headline_match`
word-form in data (e.g. "four in five") also passes. `verify.py`
also checks that every relative file link resolves to a file in
the repo (D3). Numbered figures render as
visual tiles, never bare notes (§4). Where a conclusion draws on a
second headline article in another subsection, the figure carries an
"also" list ({anchor, label})
rendered after the source name. The dashboard intro carries a
second paragraph, `tint_note`, stating what the tile background tint
means (§4). It renders on the SITREP page: `build_html.py` imports
`_tools/build_dashboard.py` to render it, and validates every figure
against the generated pages (required fields, rating in the
four levels, `pie_split` in its six values, waffle figures count-vs-count
with a minority share ≥ 2%, history join rules, link anchors exist
among the computed article ids) —
a bad entry exits 1; fix the data, never weaken the check.
`compute_article_ids()` in `_tools/build_dashboard.py` replicates the
share JS's slugify + uniqueId — the two implementations must stay in
sync, or dashboard links will point at ids the page never assigns.
**Never add a figure the report does not
evidence, and never invent a dollar figure for the money panel** — its
honest statement is "no credible dollar figure exists yet". The daily
watch updates a figure when a new article moves a headline number, and
updates the deadlines list the day a What-we're-watching date lands, so
the countdown tiles never show a passed date. Panel order is editorial
(audience-first), not numeric. `as_of_label` rolls to the release date
whenever dashboard content changes.

**Figure-section rule (2026-11-22).** Every dashboard figure carries
its own `subject` (pnl/cic/cert/san) — the domain its content belongs
to, which may diverge from its evidencing article's primary subject.
Tiles filter by figure subject; articles filter by article subject.
A figure whose evidencing article lives in another domain than the
figure's dashboard carries `article_section` ("§x.y"), rendered as
`in §x.y` on the fig-source line, so the cross-domain landing is
signposted, not silent. Known behavior (not a bug): a tile carries
only its single figure subject, so under a filter for its article's
secondary domain the tile hides while the article shows.

**Panel-placement rule (2026-11-22).** Multi-domain panels dissolve
into the domain dashboards; single-domain panels stay whole;
net-impact is the one cross-domain panel (inside Situation at hand,
last — splitting it would kill the ledger framing, which is the
panel's whole point). The Situation at hand strip stays unsliced (a
recorded exception: an at-a-glance layer whose job is temporal, not
domainal). The countdown tiles live in DIFF (the deadlines carry
`subject: pnl`; the figure-section rule governs filtering, not
render position, for the countdown).

**Domain-alignment check (2026-11-25).** `check_dashboard_domain_alignment`
(in `build_dashboard.py`, called by `validate()` at build time and by
verify.py) enforces: figure subject = panel domain (net-impact
exempt); panel domain ∈ the evidencing article's tag-subject set or
a registry entry; panel domain = the article's primary domain or a
correct `article_section` / registry entry; strip-tile subject =
panel-twin subject; every countdown has a link and all share one
declared domain; net-impact subjects in article tag sets and the
ledger spans ≥2 domains. The `divergences` registry (figure, reason,
`article_section`) and `panel_homes` (the subsections each panel
legitimately draws from) live in `dashboard.json` — a divergence not
in the registry FAILS the build. The **domain kicker** on strip
tiles is internal bookkeeping only — never rendered (removed from
rendering 2026-11-25; the reader must never see it).

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
against its human (EI, evolved intelligence) equivalent, a companion
view alongside SITREP and Landscape (F-17, built
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
change, and the DIFF feed entry says so.

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
- DIFF feed entry titles are findings, never names — "First
  benchmark of agentic pre-merge security review (SecPRBench)", never
  "SecPRBench: the first benchmark…". Link the source name in the entry to
  its primary source URL. Tag every entry in the markdown with the
  domain tags — [PNL], [CIC], [Certification], [Pre-commit] — plus
  `[new]` / `[updated]` (§2); all tags are internal bookkeeping only,
  stripped at build time, never rendered (§4). Never the old
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
unless the primary is unavailable). When an article draws on more than
one source, the Source bullet lists every source, separated by ·,
primary first — the Source line is the article's complete source list,
not just its primary. (Added 2026-11-23 — the JetBrains miss: the
Adoption article's Source line named Sonar only while its bullets drew
on JetBrains and Google too.)

**Inline links — bullet attributions hyperlinked everywhere
(2026-11-25).** Every bullet attribution is hyperlinked to the
attributed source's own page wherever a URL exists, in every article —
not only multi-source ones. Hyperlink the source name inside the
existing end-of-bullet parenthetical; where the link text names source
X, the URL target must belong to X (compare the URL TARGET, never the
link text — an aggregator URL under a publisher's name FAILS). The
Source line is the article-level bibliography, not a substitute for
bullet-level links — it still lists every source the article draws on,
primary first (the 2026-11-23 JetBrains rule). In prose, link the
FIRST mention of a source, benchmark, regulation, framework, or
product in each subsection to its source; once per subsection is
enough. Inside article `<details>` blocks the headline parenthetical
source IS linked (above). `verify.py`'s `check_bullet_citations`
enforces the bullet rule: every bullet's named source must be in the
article's own-source set (the publishers named in its Source line)
and hyperlinked in that bullet to that source's own page, or be in
the adjudicated leave set (people-statements, letters, cross-references
to the report's own articles, bare dates, CVE IDs, model names, bill
numbers). An attribution gap with no verifiable URL stays unlinked —
never invent a link; it warns on every run until the URL is supplied.
Do not link inside Sources lines. This keeps every section
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
in the AWS Security Agent table row. The domain (confluence1.com)
and the email (ci-sitrep@confluence1.com) are correctly without brackets.

**Tools are proprietary (2026-11-25).** Never name or attribute the
tools used to produce the work in anything reader-facing. What is
produced with tools can have versions and names; the tools themselves
are not disclosed.

**No internal process detail on the public page.** The reader sees the
report, not how it is made. No mention of the watch, the cron, the
maintenance process, or Barnaby.

**Timestamps.** The Markdown carries a "Last updated" line; the
generator turns it into the as-of date inside the H1 banner (§4). The
"Last updated" line is stripped from the rendered body (the date
lives only in the banner).

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
The as-of date lives inside the H1 banner, right-justified, floating
right on the title line ("As of {date}", single line, zero added
height — the date span must precede the subtitle `<em>` or the float
cannot rise to the title line); the date + View Manager button form
one right-hand unit pinned to the banner's corners (date top-right,
button bottom-right) so they never crowd each other. The banner is
identical on every level page.

**Masthead — the HUD (2026-11-25).** One navigation surface: the left
sidebar is the masthead HUD. The heading is identical on every page:
the CI SITREP / Code & Finance wordmark + tagline ("Created
Intelligence in code and finance — as of today.") — the masthead title
is a home link to sitrep.html — and the "by Confluence<1>" wordmark
(the "Confluence <1>" text from the logo, cube cropped out) — the
logo stays in the masthead everywhere, all the time. Below the
heading, the sidebar carries the minimap tree statically (site map +
page contents + changed dots + read state + search + Sections / All
articles tabs) — the sidebar tree IS the map, rendered compactly
(flex rows, the dot inline at the row start, 600-weight rows; read
rows 400 grey). The four surface groups are SITREP / Diff /
Landscape / Background (masthead capitalisation; page headings keep
their own caps), each a link-in-summary group (the name navigates,
the triangle expands): SITREP's children are its apparatus
(Corrections); DIFF's children are the four feed groups + Countdown +
What we're watching; Landscape's children are the four domains;
Background's children are About, Self-Audit, The names, Glossary,
R&D (Technology Tracker, The Surge Monitor, CI vs EI, Foundational
theses), Archive. The current page's group starts open and marked;
the current-position marker (wash #EFE9D8 + 3px navy bar + bold
title) updates on scroll AND immediately when a section is opened;
the sidebar keeps the current row in view without scrolling the
page; HUD row clicks open the target section + collapsed ancestors.
Expand/Collapse all live in the HUD (one home, every page). Condense
mode: a 64px desktop icon rail (home + 4 surfaces + View Manager +
expand), persisted in `ci-sitrep-hud-condensed`. On phones the
sidebar itself is the slide-out panel (same DOM node) behind a
floating HUD button bottom-left; mutual exclusion with the View
Manager drawer is preserved on phones (one tap switches panels).
Opening the map never moves focus into the search box (no autofocus —
the keyboard must not pop; tapping the search box still focuses it).
The confidence rating legend (collapsed `<details>`, summary
"Confidence rating scale", fullest wording + action guidance), the
Contact section (errors, omissions, and feature requests to
ci-sitrep@confluence1.com; working with Confluence<1> to
hello@confluence1.com — both mailto links), the "How to use the
SITREP" sidebar reference copy, and the copyright line "© 2026
Confluence<1> Corp. All rights reserved." complete the sidebar. No
CTAs inside the content (see F-12, Dropped).

**View Manager (2026-11-25).** The Filters + Sort drawer (the
"Tools" hamburger, renamed): a button in the H1 banner (and in the
HUD) opens a slide-over drawer holding Filters (+ Match any/all,
Clear all) with the count line, and Sort (SITREP only). The button
badge reads "View Manager · N filters active" when filters are
active. The drawer is Filters + Sort only — search lives in the HUD
tree. Background has no drawer. The slim sticky bar (title + date +
View Manager button, mirroring the H1 banner) appears once the H1
banner scrolls away; same-site level switches hold the current page
with a loading indicator rather than blanking (the swap).

**Section headings + hierarchy scale.** Every level is smaller and
less prominent than the one above, with a relative indent of ~8px
per level. The heading colour ladder, one system every level:
surface H2 navy #283060 22px/700 (SITREP, DIFF, Landscape,
BACKGROUND); domain/section headings dark rust-brown #8a3f2e
(Landscape report H2s 20px, BACKGROUND sections 20px, Situation at
hand 19px, DIFF feed groups + SITREP domain dashboards 17px);
panel/subsection headings navy (base H3 18px, SITREP panels
15px/600); tile content 13–15px. The rust-brown (not plain rust
#b3543f) keeps the changed-dot visible as a brighter spot on those
same headings. Feed-group H3s sit under 17px muted meta H2s, so they
step down to 16px/600. The four surface H2s are NOT collapsible
(`surface-heading` class; the collapse JS gives them no toggle).
"Archive" and "What we're watching" keep their muted de-emphasis.
SITREP heading ladder: 22 / 19 / 17 / 15 — SITREP H2 22px/700 navy →
"Situation at hand" 19px/700 dark rust-brown with a hairline above →
domain dashboard H3 17px/700 navy → panel H3 15px/600 navy.

**Collapse behaviour.** The SITREP level opens as a standard
collapsed view: only the surface H2 starts open; The bottom line
box, Situation at hand, Net impact, the four domain dashboards and
their panels all start collapsed — one uniform list of collapsed
headings. DIFF, Landscape, and BACKGROUND match the pattern (surface
H2 open, everything below collapsed). Article headlines are native
`<details>` and start collapsed. Jumping to an anchor auto-expands
its ancestors — including the target heading itself.
**Collapse-all / Expand-all semantics (Option A, 2026-11-23):**
Collapse all closes every content heading (main h2/h3/h4) — the four
surface H2s are the one exemption (declared in
`site_config.COLLAPSE_HANDLER_EXEMPT_CLASSES`) — and every
`<details>` in main (the bottom-line box, articles, filter/sort
panels); Expand all opens every content heading. The two buttons
are true inverses. TOC tree groups (the sidebar map) STAY open —
navigation chrome whose state the map JS manages; folding the map
would hide where the reader is. The initial-open set is separate:
what starts open on a fresh page is declared in site_config.py as
COLLAPSE_INITIAL_OPEN_* and is the initial-collapse loop's business
only; the handler's skip set is declared as
COLLAPSE_HANDLER_EXEMPT_* . The two sets deliberately differ — do
not "fix" them into agreement. No fix round adds an exemption
silently: any new always-open element or new handler exemption is a
product decision, recorded here, in the §7 changelog, and in the
declared set. The Expand/Collapse controls live on the page title
lines (surface H2s / sub-page H1s, right-justified) and in the HUD.
On the content pages everything starts collapsed, including the
theses page's Part headings (H1s other than the page title).

**Mobile.** Content comes before the masthead (CSS `order`: main first,
sidebar second). On phones the sidebar is the slide-out HUD panel
behind the floating HUD button bottom-left; the back-to-top button
stays bottom-right (rust #b3543f). One tap switches between the HUD
panel and the View Manager drawer (mutual exclusion).

**Navigation.** Three mechanisms, all unobtrusive (2026-11-14):
- **Breadcrumbs.** At the top of every section body, a small muted trail
  back up to any ancestor level or the top of the page — "↑ Top · §2
  CIC (Agentic Staff) … · §2.5 The governance gap". Built in JS from the
  heading hierarchy, so it stays correct as sections are added or
  renamed. Skipped on the top-level sections (they sit at the top of
  the page already) and on the page title; the current section is not
  repeated (its heading is directly above). Breadcrumb paragraphs
  never get share buttons.
- **Back-to-top button.** A small round rust button, fixed bottom-right,
  invisible until the reader has scrolled 500px down, then smooth-scrolls
  to the top. The arrow is inline SVG. On every page.
- **Back to the report.** On the content pages (About, Explainer,
  Theses, Archive, Self-Audit, Glossary): the sidebar opens with the
  same masthead heading as the level pages (linked "CI SITREP / Code
  & Finance" wordmark + tagline + "by Confluence<1>" logo — the title
  is the home link to sitrep.html), followed by the HUD map. On mobile
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
Excluded: See also blocks, the How-to block, the map tree.

**Search.** Search lives in the HUD tree (headings/articles across
all pages) — the report is reference material, and readers need to
find their way back to information they saw. It indexes the live page
at runtime on first keystroke: no build step, no index file, no
backend, no cost, and always in sync with the daily watch (it reads the
page, so it needs no cron step). Searchable units are the share-button
units (articles, headings, substantive paragraphs, tables) plus
standalone list items in a section body — the best-practice bullets and
the DIFF feed / "What we're watching" entries (top-level `<li>`
outside `<details>`, ≥80 chars; nested items are covered by their
parent's text; items inside an article are covered by the article).
List items have no share-button id, so the indexer assigns one with the
same deterministic slugify. Results link to the same stable anchors and
open expanded. Ranking: title matches above body matches, all-token
matches above partial; top 10 shown with a count. Minimum 2 characters;
Escape closes; arrow keys + Enter navigate; clear button; click-outside
closes; aria-live result status. Opening the map never autofocuses the
search box (§4 Masthead). Acronyms a reader would search for (e.g.
TPRM) must be defined in the prose at first mention — the search
matches literal text, and an acronym that never appears returns
nothing. Icons are inline SVG. Jumps never touch the filters (§4
filter persistence).

**Search, filter & sort (the View Manager drawer).** Search stays in
the HUD. Filters and Sort live in the View Manager drawer (above):
the **Filters** section (open by default) holds every filter control
— the Match any / Match all toggle first, then the controls in two
rows, then Clear all filters; the **Sort** section (SITREP only,
closed by default) holds the sort select + direction toggle + its
own Clear sort button (resets the sort alone). The count line
("Showing N of N figures · N of N articles") sits inside Filters and
surfaces as the badge on the View Manager button. One active
dimension counts once, however many values it holds; sort and search
are not counted (sort hides nothing; search has its own results
count). Filters are per-page by content type with SHARED localStorage
keys (`ci-sitrep-filters`, `ci-sitrep-sort`, `ci-sitrep-match-mode`)
— the reader's filters carry across pages: SITREP filters tiles,
DIFF filters feed entries, Landscape filters articles; no Sort on
tile-less pages. Sort applies to dashboard tiles within panels only:
articles filter but never sort, or the report's editorial structure
scrambles. The strips are never filtered and never counted. The DIFF
feed, The bottom line, Situation at hand, and "What we're watching"
stay unfiltered (not tagged content) — except DIFF feed entries,
which filter by their domain tags. **Filters + sort persist; nothing
clears them automatically (2026-11-24):** only the reader's own Clear
all / Clear sort changes them; tile/article/TOC/search jumps never
touch them; the state is cached per browser and restored on return
(including the cleared state). A jump to a target the reader's
filter hides lands on a hidden element — the filter doing its job,
not a defect; Clear all is the way out.

**Multi-select (F-24, implemented 2026-11-22 as ONE global toggle).**
Five dimensions are multi-select checkbox fieldsets: Domain
(Section), Industry, P&L impact, Jurisdiction, Type. The four
ordered levels (Confidence, Severity, Horizon, Technical level) and
Company stay single-select. The toggle governs how multiple values
within a dimension combine: **Match any** (default) or **Match all**
(the element must carry every selected value). The reader's choice
persists in localStorage (`ci-sitrep-match-mode`), per browser. With
Match all and more values selected than the tag cap allows (2 per
dimension, 3 for P&L impact), the cap note says the intersection is
empty by construction — never a silent empty result. The header
indicator appends "· Match all" when the mode changes the result.
Clear all filters resets the filters AND the sort and returns the
panels to their defaults — it does NOT reset the match mode.
**Controls, in order.** The Match any / Match all toggle first, then
the controls in two rows (Industry, Severity, P&L impact, Horizon,
Technical level (register), Domain (Section), Type, Confidence,
Jurisdiction, Company), then Clear all filters; Sort holds the sort
select + the asc/desc toggle + Clear sort. There is no Sector
control — sector becomes a separate product; sector tags stay in the
data and `data-sector` stays on tiles and articles as the hook.
Within a dimension, values combine per the match mode (above); AND
across dimensions; none checked means no constraint. Company is a
select derived from the distinct company values in the tag data at
build time (open vocabulary — a newly tagged company appears on the
next build); controlled-vocabulary dimensions list the full taxonomy
vocabulary even at zero articles (EU, Greece), so the option exists
the day the first article lands. Sort offers twelve keys — panel
order, date, confidence, severity, horizon, domain, type, industry,
P&L impact, tech level, jurisdiction, company — each option labelled
with its default direction; the asc/desc toggle is a text button
("Ascending"/"Descending", CSS triangle, no glyph characters),
disabled for Panel order. Sort-key orders: severity and confidence
in their natural taxonomy order; horizon chronological; register
technical → mixed → business (depth scale); set dimensions
alphabetical by first value; ties keep editorial order (stable sort).
**Count line.** "Showing X of 62 figures · Y of N articles" (per
page: figures on SITREP, articles on Landscape, entries on DIFF);
figures are panel tiles only. When a subsection filters out entirely
it hides, heading and all. The surface H2s stay visible, framing the
per-area empty-state lines ("No figures match these filters." / "No
articles match these filters.", each with its own Clear button).
Domain dashboards hide when empty under filtering (a dashboard
heading surviving with zero visible panels is worse than a hidden
one). Only the untaggable tiles (the money bignote) are never hidden
and keep their editorial position under sorting; the interim
untagged-visible rule is retired (the backfill is complete — an
untagged article does not match a Company selection).
**Clear-all** sits at the bottom of the Filters section; it resets
the sort to Panel order and returns the panels to their defaults (it
does not reset the match mode). Filter selects go full-width on
phones (≤600px).

**Tooltips.** The first mention of a glossary term in each subsection
gets a dotted underline; hovering (desktop) or tapping (mobile) shows
the one-line definition with a link to the full glossary entry. The
wrapping happens at runtime in the browser from the glossary data
injected at build time — it skips links, code, buttons, breadcrumbs,
and share buttons, and it never wraps the same term twice in one
subsection. Two terms are in the glossary but never tooltip-wrapped:
"agent" and "agentic" — too frequent; a marker on every first mention
would be noise. The tooltip data is generated from `GLOSSARY.md`, so
every page inlining it must be regenerated whenever the glossary changes.

**No font-glyph dependency for UI.** Expand/collapse arrows are pure CSS
borders; icons are inline SVG. A glyph that renders as a weird character
on a reader's device is a defect, even if the behaviour works.

**External links open in new tabs** (`target="_blank" rel="noopener"`) —
following a source never replaces the sitrep. Internal links (anchors,
.html pages, mailto) stay in the same tab.

**The changed dot (2026-11-23).** Two reader stages: stage 1 = learn
the landscape; stage 2 = every day after, watch what changes — via
DIFF AND via the dots. The dot marks everything changed *because of
news* (not everything conceivably affected), new-or-updated in the
rolling 7-day window — the SAME window as DIFF
(`site_config.CHANGE_WINDOW_DAYS = 7`, America/New_York explicit).
The changed set derives from the FEED JOIN
(`build_html.py::add_feed_data_attrs` via
`build_dashboard.py::match_feed_entry_ids`) — NEVER from the tag
line's `source-date=` (the source's publication date, not the
report's change date). Inheritance: tiles inherit from their
evidencing article; headings/map/search inherit from children
(aggregate); The bottom line box carries one aggregate dot on its
summary line (never at paragraph ends — dots sit at the end of
headings, TOC entries, or tiles). Exclusions: NO dots on feed
entries (everything there is changed by definition), countdown
tiles, the money bignote, or the profitability strip card. Look:
static rust `#b3543f`, 10px, 2px paper ring; top-left on tiles,
beside headlines/headings/map rows; an empty span with `role="img"` +
`aria-label="Changed in the last 7 days"` (text inside `<summary>`
would leak into the slugify and break tile links). Reader state in
localStorage `ci-sitrep-seen` ({tile:<id>/article:<id> → date}):
**asymmetric hybrid clearing** — "Got it" (at the END of the article
body, shown only while the article has an un-consumed dot) clears
the article dot AND the tile dot(s); a tile click clears only the
tile dot (share clicks excepted); aggregates are derived in JS
(shown iff any descendant un-consumed); a new change date re-arms.
**Standing rule (Yorgo, 2026-11-23): better to overstate what's new
than let the user miss it — always.**

**Changed-part highlight (2026-11-23).** While an article carries its
dot, the page also identifies WHICH PART changed (§2 marking): a pale
amber wash `rgba(201, 138, 45, 0.20)` over marked bullets, prose
spans, and tile numerals (the numeral only — never the whole tile).
New articles: dot only. The highlight lives and dies with the dot —
same window, same consumption: consuming a tile's dot clears its
numeral wash; "Got it" clears the article's washes with its dot.
Headlines and headings never highlight (they get dots). Feed tags
are internal only — stripped at build time, never rendered; the "in
§" cross-domain labels on tiles are signposts, not tags, and stay.

**Tile → article + bullet deep link (2026-11-23).** Every tile
numeral/label, strip tile, and mapped countdown navigates to the
evidencing article, EXPANDS it, and lands on the bullet containing
the figure. Bullet ids `{article-id}-b{N}` are assigned at runtime
(top-level `<li>` only, 1-based); the figure's `bullet` field (plus
`bullet_token` when the display isn't verbatim in the bullet)
appends `-bN` at render; the fig-note stays outside the link; the
dot + share button stay siblings. The link field keeps the article
anchor; `-bN` is appended at render. A `check_bullet_deep_links`
failure means the mapping is stale — re-map, never work around the
check. The bottom-line sentences keep subsection links (synthesis,
no single article).

**Entry modal — "How to use the SITREP" (2026-11-25).** The
five-line block (§2) renders as a floating dialog on arrival, with
the zoom-level pyramid at the top. **The modal auto-opens on EVERY
arrival; the only suppression is the reader ticking "Don't ever
show me again" in the modal (permanent, localStorage
`ci-sitrep-howto-never`).** Closing the modal without ticking does
NOT suppress the next arrival. Every fresh page load counts as an
arrival; in-session level swaps do not re-pop. The sidebar copy is
the reference (a button that opens the modal on demand). The modal
sits outside `<main>`, so the search indexer and share JS never
touch it.

**Open Graph cards (2026-11-25).** Every built page carries OG +
Twitter Card meta (og:title, og:description, og:image, og:url —
absolute canonical prod URLs) with 1200×630 card images under
`cards/` (paper #faf6ef, navy band, rust rule). `check_og_tags`
asserts presence on every page and that og:image resolves to an
existing file.

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
  10×10 grid of 5px squares; the multiple stays the headline number;
  side rows keep the exact counts (a rounded graphic is never the only
  record); the caption names the counted set ("Share of 147
  vulnerabilities counted"). Pure multipliers and rates are not shares
  of a whole and stay ratio tiles.
- `paired` — two figures from one finding, one DOUBLE card (2 units
  wide): the figures sit SIDE BY SIDE (figures[0] left),
  each half carrying its own pie + value, label, and
  legend, separated by a vertical hairline divider, no "vs"
  connector; the whole tile links to the evidencing article;
  sentiment judges the combined finding, not either figure alone; one
  source footer below the halves. On phones the halves stack vertically
  with a horizontal hairline divider. Exactly 2 figures, each 0–100
  with a valid `pie_split`.

**A figure with a headline number renders as a visual tile, never a bare
note.** A headline number is a share, a count, a multiple, or a delta;
it renders as a big-number, pie, ratio, sparkline, or waffle tile.
Notes are ONLY for findings with no headline number: a prose finding,
a case, a qualitative judgement. A numbered finding rendered as prose
is a defect. (2026-11-20: the whole Net impact panel rendered as ten
tall, mostly empty note cards — every item carried a headline number;
Yorgo caught it from a screenshot.)

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
size (2026-11-19, Yorgo: same-size cards scan easiest). The unit is
1 unit wide (one grid column) by **205px min-height** (2026-11-25 —
tightened from 280px fixed so three rows fit Yorgo's 1280×800 logical
screen; min-height, not fixed, so an expanded footer grows the tile
instead of spilling). A 2-unit tile is two columns wide; a 3-unit
tile spans the full width and keeps its own (natural) height — the
money bignote and the profitability tile are framing elements, not
stat cards, and are exempt from the unit height, as are the countdown
tiles (their own 4→2→1 grid, uniform 3-line content). Rows align top
and bottom at multi-column widths; the source footer is pinned to
the tile's bottom (`margin-top: auto`); short tiles vertically
centre their content (the body sits centred between the top and the
footer) so a short card reads finished rather than hollow. Every
tile card carries an expandable footer — one tight line, the word
`source` (lowercase) + a CSS chevron — holding source link · date ·
rating dots (collapsed by default; footer clicks don't navigate;
Expand all/Collapse all cover footers). The rating WORD is off every
tile (dots only; the word survives in a visually-hidden span for
assistive tech). Countdown tiles and bignote tiles get NO footer (the
deadline date is content, not provenance). Content fits the unit by
budget, not by truncation: labels ≤ 84 chars, legend rows ≤ 36
chars, side rows ≤ 33 chars, source lines ≤ 99 chars (1-unit) / ≤ 146
chars (2-unit), fig-notes ≤ 66 chars, note text ≤ 190 chars,
sparkline captions ≤ 79 chars, waffle captions ≤ 36 chars — and
every tile's estimated height (`build_dashboard.py`'s estimator,
desktop widths) must be ≤ 205px; the build FAILS above 245px (the
fail line guards runaway content in the min-height era) and WARNS at
206–245px (tolerance band — band cases are decided by the live
whole-row check, not by trimming). Underfill is enforced the same
way, NOTE-ONLY: a `note` tile estimating under 88px FAILS the build —
convert the figure to a visual tile or enrich the note text. Other
tile types are never underfill-checked. The floor is calibrated, not
guessed — it catches only the worst offenders; the §6 line-13 human
check covers the rest. A single tile's overflow is fixed by trimming
that tile, never by raising the unit height; the height moves only
on systematic evidence from the live whole-row check. Fixed columns:
3 above 1100px, 2 at 601–1100px, 1 at ≤600px. On phones (≤600px,
single column) the unit height is lifted — tiles are natural height,
since there are no row neighbours to align with and full-width
content wraps short; a double tile's content stacks (the paired
tile's halves stack vertically, each ~1 unit of content). Span
collapse is explicit (a span-2 item in a 1-column grid creates an
implicit track and overflows): span-3 is always `1 / -1`; span-2
becomes `1 / -1` at ≤600px. Mapping: pie (single/range), ratio,
big-number, waffle, no-data, flag = 1 unit; segmented pie, note,
sparkline, paired = 2 units; money bignote, profitability = 3 units
(full-width, natural height). The Situation at hand strip is three
full rows of three units in the same system (see §2); the countdown
tiles keep their own 4→2→1 grid. `.tile-grid` uses dense flow: a
later 1-unit tile backfills a hole a 2-unit tile leaves — visual
order may differ from DOM order by one slot; DOM order stays
editorial. The ledger is the exception to one-grid-per-panel
(2026-11-20): its two sides are semantically disjoint (output up vs
cleanup up) and must never interleave, even under sort — each side
renders in its own `.tile-grid`, with its block-label as the grid's
first child, and the panel footnote below the second grid. The
sort/filter JS is grid-generic (it reorders within each grid, labels
per grid, counts per panel body), so two grids are safe. The second
grid carries `margin-top: 16px`, restoring the 24px inter-side gap
of the single-grid layout (12px row gap + 12px label margin; the
split would otherwise leave the 8px grid margin-bottom alone). The
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
the documented exceptions; every bullet attribution hyperlinked to its
source's own page (§3); no duplicate headlines; no literal Markdown
links in the HTML; all internal anchors resolve — article ids
assigned at runtime by the share JS are accepted via the computed id
set, see §2 Dashboard), freshness (no DIFF feed entry older than 7 days;
no past date in "What we're watching"; "Last updated" not in the
future), order (DIFF feed newest first; "What we're watching" soonest
first; section and subsection order; DIFF group order incl. the Today
group first when present), naming (Confluence<1> everywhere, with the
one documented Atlassian exception; brand all-caps CI SITREP; current
section names; zero visible "slice"), hygiene (no internal-process
strings on the public page), layout markers (H1 date, HUD map,
confidence legend, copyright line, share buttons, How-to modal,
surface headings, the embedded dashboard panels), collapse semantics
(the declared initial-open and handler-exempt sets, §4), the changed
dots + markers (feed-join consistency, dot placement — never in
paragraphs), tile→bullet deep links, nav (four surface groups in
order on every page), the DIFF single-surface property (the next H2
after DIFF is Landscape), OG tags, and domain alignment (§2). It
also curl-checks every external link. **Verify bars: 81 checks
(single-page build, for the record) / 85 checks (levels variant —
the release bar).** Run under `TZ=America/New_York` — the freshness
checks are ET-relative and the VM clock is UTC (§6).

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
count, the watch adds figures). The sentiment re-point is moot:
verify.py does not count pills (verified 2026-11-18) — tint counts
are checked statically instead.

**Test harnesses.** `_tools/tests/` holds the JS harnesses: the
filter/sort harness (`r4b-test.js` + fixture + FILTER_JS extract —
202 checks), the collapse harness (77 checks, incl. the regression
scenario "Collapse-all changes SITREP on a fresh page"), the
cold-load landing harness (13 checks), and the swap harnesses
(predicate 19 + bar 17). Each runs the real generator JS against a
fixture parsed from the built pages, expectations computed
independently. Re-run them after any filter, sort, collapse, or swap
JS change; regenerate fixtures and extracts from the current built
pages and generator when either changes.

**What automation cannot check — the worker's pre-publish re-read.**
Before publishing, re-read every new or revised segment and confirm:

1. **Necessary content is in there, and only that.** Every item from the
   day's research that passed the bar (§1) is in the report, in the right
   section; every DIFF feed entry points to content that exists;
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
4. **Content order.** DIFF feed newest first; "What we're watching"
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
check it against §4: masthead HUD and H1 band render correctly;
content before masthead on mobile; the HUD map renders compactly
(dots inline, current row marked); share buttons work (clicking one
copies the link and, for an article, does not toggle it); a shared
article URL opens the article expanded; tile clicks land on the
evidencing bullet; the entry modal auto-opens on arrival; filters
persist across pages and reloads; no glyph renders as a weird
character. A design change is not done until the live site has been
seen rendering correctly.

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
12. Whole-row visual check covers EVERY panel (added 2026-11-20 — the
    Net impact miss): the line-7 check runs over every dashboard
    panel and the strip, not a sample.
13. No tile renders mostly empty (added 2026-11-20): no card reads
    mostly empty at desktop width; a numbered figure rendered as
    bare prose fails the release.
14. Design §5 review collected IN WRITING before release (added
    2026-11-20): the design editor's verdict — pass, or findings
    fixed and re-verified — is recorded in the release note; no
    written verdict, no release.
15. Bullet citations (added 2026-11-23 — the JetBrains miss; extended
    2026-11-25): every bullet attribution links its source's own page
    (§3); the Source line lists every source the article draws on.
    verify.py enforces the bullet rule.
16. Changed dots sit at the end of headings, never at the end of a
    paragraph or block: The bottom line dot sits at the end of its
    summary line; every other dot sits at the end of its heading,
    TOC entry, or tile (added 2026-11-25 — the SOTM paragraph-dot miss).
17. Collapse-all / Expand-all (added 2026-11-23): click both on the
    QA build and confirm the behavior matches the RULES.md §4
    semantics (surface H2s exempt; Collapse-all on a fresh page must
    visibly collapse everything below the surfaces). A round that
    changes what starts open must re-check this line.
18. DOM-vs-rendered (added 2026-11-24): DOM placement ≠ rendered
    placement — a heading that terminates a section-body renders as
    a peer section. Verify the rendered heading count (a phone
    screenshot counts), not just the DOM order.
19. Timezone (added 2026-11-23): build_qa.py/build_audit.py inherit
    the caller's TZ, so past midnight UTC the freshness check fails
    and AUDIT.md stamps tomorrow's date — always run builds and
    verify under `TZ=America/New_York`.
20. Reslice/page-split checks (added 2026-11-22/25): after any
    reslice or page split, diff the unique-URL set old vs new (a
    dropped subsection-level Sources line is silent); every
    article's first subject value matches its subsection; no old
    section anchors remain; anchor check on every page; cold-load
    landing test on every rebuild; staleness guards must name a
    fix-build-only marker (the About check count cannot be trusted
    as the front-page staleness marker — CDN edges go stale
    independently).

1. Edit the canonical Markdown at `~/workspace/your_files/watches/`
   (SYNTHESIZED.md, archive/ARCHIVE.md). The repo staging dir
   (`~/workspace/ci-sitrep/`) is a copy, not the source. Tag new
   articles per §2 (one tag line above the headline) as part of the
   same edit — the daily watch cron instructions carry the tagging
   step, so new articles never arrive untagged.
2. Sync the changed files into the staging repo.
3. Regenerate the HTML with the repo's generators (`build_html.py` for
   the level pages; `build_page.py` for the other pages; `build_audit.py`
   then `build_page.py` for the Self-Audit page, title "Self-Audit —
   CI SITREP"; pipeline order is build_audit → refresh_about →
   build_page). `build_html.py` is always invoked with explicit
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
- **2026-11-20** — Net impact panel converted from notes to visual
  tiles (Yorgo, from a screenshot: the whole panel rendered as ten
  tall, mostly empty note cards — every item carried a headline
  number): nine of the ten ledger items are now visual tiles (seven
  big-number, two ratio), the FCA case stays a note with enriched
  text. New rules: a figure with a headline number renders as a
  visual tile, never a bare note (§4, pointer in §2). §6 checklist
  gains lines 12–14: the whole-row visual check covers every panel,
  no tile renders mostly empty, and the §5 design review is
  collected in writing before release — no written verdict, no
  release. §1.1 Sonar bullet aligned to "review" (was "verify"),
  matching the §2 article. An underfill check is enforced in
  `build_dashboard.py` (note tiles under 110px fail, §4); the ledger
  splits into one grid per side so the sides can never interleave.
- **2026-11-20** — Filter section-invariance decided (Yorgo): the
  three report sections (§1 Pre-commit, §2 In codebase, §3 Agentic)
  never hide under filtering — no matter what filter the reader
  uses, they always get all three sections. Implementation pending;
  rides with the usability review.
- **2026-11-20** — Headline rule now enforced mechanically (D2):
  `build_dashboard.validate()` fails the build when a figure's
  display numerals are absent from its target article's headline
  (word-forms via `headline_match`); the 9 pre-existing mismatches
  warn from `HEADLINE_KNOWN_MISMATCHES` until their A11 splits or
  data entries land, and theme-headlined articles warn. `verify.py`
  gains a relative-file-link check (D3, 54 checks) — the class that
  let the uncommitted append-only archive file 404. The local git
  checkout was reconciled to origin/main (D4).
- **2026-11-21** — Headline rule gains a confidence floor (Yorgo):
  a tile may link to an article that does not headline its figure
  when the figure is rated ●●○○ (Reported) or better — the rule is
  enforced only for ●○○○ (Claimed) figures. The 9
  `HEADLINE_KNOWN_MISMATCHES` entries (all rated 'reported' or
  better) are deleted; no A11 splits and no `headline_match` data
  entries are needed for them. `build_dashboard.validate()` passes
  ≥2-dot figures on a headline mismatch silently; the FAIL tier
  still binds Claimed figures.
- **2026-11-23** — Multi-source article rule (the JetBrains miss,
  found by Yorgo): an article drawing on more than one source lists
  every source in its Source bullet, separated by ·, primary first;
  every bullet in a multi-source article links its source inline
  unless it is about the primary source named in the Source line.
  `verify.py` gains the enforcing check (54→55 checks) and the
  pre-release checklist gains line 15. The GTIG/MadPot article's
  three-source Source line (23 Nov) is the pattern.
- **2026-11-22** — Four-section reslice (Yorgo's decision, built in
  QA): all three surfaces sliced by the same four sections in order —
  PNL (profit and loss), CIC (Agentic Staff), Codebase Certification,
  Code Sanitizing Pre-commit. Surfaces renamed: "What just changed",
  SITREP, CILAK (later Landscape). §1 definitions + the PNL boundary
  rule; figure-section rule (every figure carries its own subject);
  panel-placement rule (multi-domain panels dissolve; net-impact the
  one cross-domain panel); taxonomy v3 values `pnl/cic/cert/san`
  primary-first, `0` dropped; feed grouping at render time; counts
  on headings; Situation at hand as four paragraphs in section
  order. (Spec: four-section-reslice-spec-2026-11-22.md.)
- **2026-11-22 (Addendum)** — Situation at hand moved into SITREP
  (open by default); dashboard explainer is a collapsible "What this
  is"; ratio side rows (.tile-side) added to the orphan guard.
- **2026-11-22 (Addendum 2)** — SITREP hierarchy rebuild: "What this
  is" first; Situation at hand folded into the bottom line as its
  abstract (four paragraphs, one per section); countdown + net impact
  folded into the bottom line (abstract → strip → countdown →
  net-impact last); hierarchy scale (22/20/18/16, ~8px indents; the
  bottom-line heading is a `<p>`, never collapsible); filter panels
  (Sort separated with its own Clear sort; Filters panel; count line
  outside, always visible); multi-select + F-24 as ONE global Match
  any / Match all toggle (five checkbox dimensions, localStorage
  `ci-sitrep-match-mode`, cap note — never a silent empty result).
- **2026-11-23** — Collapse-all Option A (Yorgo): Collapse all closes
  every content heading (main h2/h3/h4); Expand all its true inverse;
  neither touches `<details>`; the initial-open set and the
  handler-exempt set declared separately in site_config.py and
  deliberately different; new verify.py collapse check (56 checks)
  + collapse harness (16 checks); initial state unchanged.
- **2026-11-23** — Changed dot: static rust #b3543f, 10px, new-or-
  updated in the rolling 7-day window derived from the feed join
  (never `source-date=`); tiles inherit from their evidencing
  article, headings/map/search from children; no dots on feed
  entries, countdowns, money bignote, profitability card; reader
  state in localStorage `ci-sitrep-seen`; new verify.py
  `check_changed_dots` (57 checks); "How to read this" rewritten
  with the two workflows. (Clearing + "Got it" placement superseded
  the same day — see tile→bullet entry below.)
- **2026-11-23** — Changed-part highlight: watch-time marking
  (`<!-- changed YYYY-MM-DD -->` bullets, `<span data-changed>`
  prose/partial, `"changed"` on figures — numeral only); new
  articles dot-only; pale amber wash rgba(201,138,45,0.20); all feed
  tags internal only ([new]/[updated] build-only); expiry lives/dies
  with the dot; `clean_changed_markers.py` at run start; weekly
  git-diff audit cron Monday ~07:00 ET; verify bar 59.
- **2026-11-23** — Tile → article + bullet deep link (Yorgo
  priority): every tile lands on the bullet containing its figure
  (`{article-id}-b{N}`, `bullet` + `bullet_token`); new
  `check_bullet_deep_links` (60 checks). Folded in: "Got it" moved
  to the END of articles; asymmetric hybrid clearing ("Got it"
  clears article + tile dots; tile click clears only the tile dot);
  two notes → big-number tiles; "Preview" masthead marker;
  ThinkingBox + METR minted (figures re-pointed + bullet-mapped).
- **2026-11-23** — Option B re-map (Yorgo's verdict Q1): regulation
  moves from CIC to a new PNL subsection §1.4 "Regulation &
  enforcement" (28 articles; CIC renumbers with no gap); tag retags
  primary-first; countdown subjects → pnl; "Regulation lives in PNL,
  not CIC — CIC keeps the governance firms build themselves; PNL
  holds the governance regulators impose."
- **2026-11-23** — Masthead navigation — four sections: one nav
  headed "SECTIONS" (SITREP, CILAK, DIFF, BACKGROUND — nav order
  matched to page order the same day: SITREP, DIFF, Landscape,
  BACKGROUND); page-specific contents at the top of each page; the
  feed renamed DIFF ("What's changed", in coder lingo); "Short on
  time?" restored; verify bar 69.
- **2026-11-23** — DIFF hoisted out of CILAK into a peer surface
  (page order SITREP → DIFF → Landscape); DIFF heading takes the
  base 22px navy H2; verify bar 71.
- **2026-11-23** — "What we're watching" moved into DIFF: DIFF is
  "what happened and what's coming" (feed + watchlist); the watch
  keeps writing `## What we're watching` in the markdown; the build
  places it inside DIFF. Same-hash anchor fix (expand on click).
- **2026-11-23** — CILAK renamed to Landscape (Yorgo): "Landscape —
  the complete picture"; the anchor stays `#report`; the glossary
  CILAK entry retitled "Landscape" and moved to the L section.
- **2026-11-24** — Single DIFF surface: the watchlist demoted to an
  H3 inside the DIFF body (one toggle opens the whole surface); the
  DIFF gloss is "What happened and what's coming." §6 gains the
  DOM-vs-rendered lesson (line 18).
- **2026-11-24** — Heading-level hues + DIFF tagline in the heading:
  section H2s in dark rust-brown #8a3f2e (dots stay bright rust);
  the DIFF heading carries "DIFF — What changed and what's coming
  (N entries)".
- **2026-11-24** — Masthead nav second levels: DIFF + Landscape
  grouped (DIFF's children: the four feed groups + What we're
  watching; Landscape's: the four domains); verify bar 73.
- **2026-11-24** — As-of date into the H1 banner, right-justified,
  floating right on the title line (the span must precede the
  subtitle `<em>`); no pill below the banner, no added line.
- **2026-11-24** — Filters + sort persist; nothing clears them
  automatically (Yorgo): the jump-clear handler deleted; state
  cached in localStorage (`ci-sitrep-filters`, `ci-sitrep-sort`);
  only Clear all / Clear sort changes them; jumps never touch them.
- **2026-11-24** — How to read cut to five lines (149 words,
  navigation only); the bar lives on Self-Audit, the rating
  definitions in the masthead legend (fullest wording + action
  guidance).
- **2026-11-24/25** — Nav + header round: Self-Audit in BACKGROUND,
  second after About; BACKGROUND order About, Self-Audit, The names,
  Glossary, R&D, Archive; dashboard slices named as dashboards with
  panel-figure counts; Situation at hand as a standalone expandable
  box first below the header.
- **2026-11-25** — How-to-read as an entry modal: floating dialog on
  arrival (the sidebar copy is the reference). Strengthened the same
  day: the modal auto-opens on EVERY arrival; the only suppression
  is the "Don't ever show me again" tick (localStorage
  `ci-sitrep-howto-never`); closing without ticking does not
  suppress. Renamed "How to use the SITREP" (item 42).
- **2026-11-25** — Levels-as-pages variant (the levels variant is
  THE site structure): four level pages (sitrep.html, diff.html,
  landscape.html, background.html); masthead nav as page links;
  minimap TOC (floating toggle, current-position highlight, read
  state, changed dots); per-page filters with SHARED localStorage
  keys; countdowns in DIFF; BACKGROUND landing page; variant verify
  bar 80 (later 85).
- **2026-11-25** — Research as a BACKGROUND subsection (renamed R&D
  the same day — see below): Technology Tracker (tracker.html) +
  The Surge Monitor (tracker-whitepaper.html); verify bar 77
  (single-page).
- **2026-11-25** — Redistribution + dot placement: domain-alignment
  check + `divergences` registry + `panel_homes`; strip in domain
  order; SOTM dot on the summary line (never paragraph ends — §6
  line 16); fixed fifth paragraph in The bottom line box
  (generator-appended); tracker knobs-panel dedup (one panel, WE ARE
  HERE kept). Single-page verify bar 81.
- **2026-11-25** — Citation rule rewrite: bullet attributions
  hyperlinked to the attributed source's own page wherever a URL
  exists, in every article; the Source line is the bibliography, not
  a substitute; new `check_bullet_citations`. OG tags on every page
  + cards path `cards/`; "Today (N)" group first in DIFF + heading
  count; tool share links (scenario params + replaceState + copy
  button).
- **2026-11-25** — Variant round 2: BACKGROUND consolidated page
  (seven inlined sections + two linked cards; anchor-first nav;
  H5/H6 collapse stack); R&D regroup (Tracker, Surge Monitor, CI vs
  EI, theses); Tools hamburger drawer (later View Manager);
  minimap no-autofocus; SITREP hierarchy ladder 22/19/17/15
  (bottom-line rust-brown + hairline); floating buttons (Contents
  bottom-left, back-to-top rust); one-click panel switch.
- **2026-11-25** — R&D rename + tool-attribution scrub: "Research" →
  "R&D" (anchors unchanged); tools are proprietary — never name the
  tools used in reader-facing content; research attributed "Yorgo
  P. Bougás, Confluence<1>" (affiliation only, not firm IP).
- **2026-11-25** — Grid terminology (Yorgo): Levels / Domains /
  Verticals; "slice" internal-only, never reader-facing; bottom
  line ↔ situation at hand inverted ("The bottom line" = most
  distilled abstract box; "Situation at hand" = fuller section);
  the site is a website, not a file; canonical record
  nomenclature-2026-11-25.md.
- **2026-11-25** — Masthead HUD round (levels variant): one
  navigation surface (the sidebar carries the minimap tree
  statically; condense rail 64px, persisted); Tools drawer → View
  Manager (Filters + Sort only; search in the HUD); entry modal
  renamed "How to use the SITREP"; speed (content-visibility,
  Speculation Rules, View Transitions); heading colour ladder
  unified; SITREP opens as a standard collapsed view; surface H2s
  not collapsible; DIFF Countdown + What we're watching as peer H3s;
  level-switch swap (hold + loading indicator); slim sticky bar;
  tool inside the standard container (siderail, same tab); tiles
  tightened to 205px min-height with the `source` footer; verify
  bar 85 (variant).
- **2026-11-25** — Taxonomy v3 approved (release verdict Q9):
  `subject` values `pnl/cic/cert/san`, primary-first, `0` dropped;
  six worked examples re-tagged. Glossary canonical merge: 133
  terms (staging base + Landscape, HHI, DIFF, PNL from the levels
  copy; no CILAK entry); identical in both trees.
