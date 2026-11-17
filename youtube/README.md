# CI SITREP on YouTube (F-19) — MVP

A 24/7 CNBC-style live channel: the report's findings, cycled one at a time,
with CI-vs-EI gauges always visible, a glossary scroll, and a what's-new
ticker. AI voiceover reads each finding as it appears.

## Files

| File | What it is |
|---|---|
| `scene.html` + `scene.css` + `scene.js` | The broadcast scene. OBS browser source, 1920×1080. |
| `review.html` | The export as a table, for review — search and filter by section and rating. Not part of the broadcast. |
| `findings-inline.js` | The export data as a script tag (generated — do not hand-edit). Lets the pages work under `file://` in OBS, where `fetch()` of a local JSON file is blocked. |
| `../data/findings.json` | The export itself — the first F-02 database file. The scene re-fetches it every 15 minutes when served over HTTP and picks up new findings without a restart. |

## Regenerate the export

After every report change (a step in the publish pipeline, after `build_html.py`):

```bash
~/workspace/your_files/watches/_tools/venv/bin/python ~/workspace/ci-sitrep/_tools/export_findings.py
```

It writes `data/findings.json` and `youtube/findings-inline.js` in one run,
so the two can never drift. It prints the counts and any warnings (an article
without a parseable date is a warning, not a failure — the report itself
carries no date for it).

## View locally

```bash
cd ~/workspace/ci-sitrep
python3 -m http.server 8000
```

- Scene: http://localhost:8000/youtube/scene.html
- Review: http://localhost:8000/youtube/review.html

Or open either file directly in a browser — the inline data script makes
`file://` work too (the 15-minute refresh only runs over HTTP).

## OBS setup (local MVP)

1. Add a **Browser** source, 1920×1080, pointing at the local `scene.html`
   (`file:///…/ci-sitrep/youtube/scene.html`). Check "Shutdown source when
   not visible" off, so the cycle keeps running.
2. Ambient footage: either put a video source **under** the browser source
   and load the scene with `?transparent=1`, or drop a `<video>` element
   into the `#ambient` div in `scene.html` (see the comment there). Footage
   must be ours or licensed — no clips we do not own.
3. `?dev=1` shows the voiceover caption and the ambient-slot outline while
   setting up. Never on air.

## Voiceover

Each slide sets `#finding`'s `data-voiceover` attribute to the exact
speakable text — the headline plus the finding's first line, with symbols
expanded for speech (`~` → "about", `×` → "times", `%` → "percent"). The
same text is exposed as `window.CI_SITREP_VOICEOVER`, and every slide change
dispatches a `ci-sitrep-slide` event with `{index, total, kind, id,
voiceover}`. A voiceover driver listens for the event; it never scrapes
the DOM. The State of the market slide opens each cycle (75 s — the full
synthesis, spoken); articles run 15 s each, so a full cycle is ~21 minutes.

## What the gauges show

The right rail is always visible. Four gauges, all sourced from the report
— nothing invented:

- **Sajadi** — 135 confirmed vulnerabilities in AI patches vs 12 in human
  patches, same issues (SWE-bench study v4, Reported).
- **CodeRabbit** — 2.74× the vulnerability rate of human-written code
  (Claimed — the gauge says it is a vendor claim).
- **SusVibes** — a post-hoc review lifts working-and-secure to 47–56% at
  2.5× the cost of generation alone (Reported).
- **METR** — the 50%-reliability agent time horizon doubles about every
  7 months; the 80% horizon is far shorter (Corroborated). A stat, not a
  pair: the report publishes no human-side horizon, and the gauge does not
  invent one.

Gauges grow with the F-17 human-baseline audit. Rust is the CI side, blue
the human side — the same rule as the report's bottom-line strip.

## Still to come (not in this MVP)

- The voiceover driver itself (event hook is ready; no TTS wired up yet).
- YouTube live enablement (verified channel + 24 h wait) and the RTMP
  stream from OBS.
- The server version (headless Chromium + ffmpeg pipeline) to replace the
  local OBS machine.
