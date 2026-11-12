#!/usr/bin/env python3
"""Build SYNTHESIZED.html from SYNTHESIZED.md.

Reads the knowledge-base markdown, converts it to a self-contained HTML
reading surface with:
- a sidebar table of contents (jump to any section),
- collapsible sub-sections (click a heading to fold/unfold),
- collapsible article headlines (native <details>, already in the markdown),
- a "New this week" section at the top with jump links (rolling 7-day window),
- clean typography and table styling.

Usage: build_html.py [input.md] [output.html]
Defaults: ~/workspace/your_files/watches/SYNTHESIZED.md -> SYNTHESIZED.html
"""

import re
import sys
from datetime import datetime
from pathlib import Path

import markdown

WATCHES = Path.home() / "workspace" / "your_files" / "watches"


def github_slugify(text, separator="-"):
    """Match GitHub's heading-anchor algorithm.

    Lowercase, drop punctuation (anything that is not a word char, a space,
    or a hyphen), replace each space with the separator (no collapsing).
    """
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return text.replace(" ", separator)


def convert_details_blocks(src):
    """Convert the markdown inside <details> blocks to HTML.

    The markdown library does not process markdown nested inside raw HTML
    blocks, so a <details> whose facts are bullet lists would otherwise
    render as raw "- ..." text. Convert each block's inner markdown to HTML
    first; the outer conversion then passes the whole <details> through.
    """
    def repl(m):
        inner = m.group(1)
        sm = re.match(r"(\s*<summary>.*?</summary>)(.*)", inner, re.DOTALL)
        if not sm:
            return m.group(0)
        summary, rest = sm.group(1), sm.group(2)
        html_rest = markdown.markdown(
            rest.strip(), extensions=["tables", "sane_lists"]
        )
        return "<details>\n" + summary.strip() + "\n" + html_rest + "\n</details>"

    return re.sub(r"<details>(.*?)</details>", repl, src, flags=re.DOTALL)


def strip_contents_section(src):
    """Drop the markdown's own '## Contents' section.

    The sidebar TOC (generated from the headings) replaces it, so keeping
    the section would duplicate the TOC and leave a dangling #contents
    anchor. Runs from the '## Contents' heading to the next '---' or '## '.
    """
    return re.sub(
        r"^## Contents\n.*?(?=^---\s*$|^## )",
        "",
        src,
        flags=re.DOTALL | re.MULTILINE,
    )


def build(input_path, output_path):
    src = Path(input_path).read_text(encoding="utf-8")
    src = strip_contents_section(src)
    src = convert_details_blocks(src)

    md = markdown.Markdown(
        extensions=[
            "tables",
            "toc",
            "sane_lists",
        ],
        extension_configs={
            "toc": {
                "slugify": github_slugify,
                "toc_depth": "2-4",
            },
        },
    )
    body = md.convert(src)
    toc_html = md.toc

    # "Last updated" line, taken from the header of the markdown.
    m = re.search(r"\*\*Last updated:\*\*\s*([0-9-]+)", src)
    last_updated = m.group(1) if m else ""
    # Human-readable "As of" date for the prominent banner (e.g. "Thursday, November 12, 2026").
    as_of = ""
    if last_updated:
        try:
            as_of = datetime.strptime(last_updated, "%Y-%m-%d").strftime("%A, %B %d, %Y")
        except ValueError:
            as_of = last_updated
    # Prominent timestamp banner directly under the H1, so a reader sees at a
    # glance how current the report is.
    if as_of:
        banner = f'<p class="as-of-banner">As of {as_of}</p>'
        body = body.replace("</h1>", "</h1>\n" + banner, 1)

    html = TEMPLATE.format(
        title="CI Sitrep — Code & Finance",
        last_updated=last_updated,
        toc=toc_html,
        body=body,
    )
    Path(output_path).write_text(html, encoding="utf-8")
    print(f"Wrote {output_path} ({len(html)} bytes)")


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>
  :root {{
    --ink: #1a1a1a;
    --muted: #666;
    --line: #e3e3e3;
    --accent: #1f4e79;
    --bg: #ffffff;
    --side-bg: #f7f7f5;
    --code-bg: #f4f4f2;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--ink);
    background: var(--bg);
    line-height: 1.6;
    font-size: 16px;
  }}
  .as-of-banner {{
    display: inline-block;
    margin: 0 0 18px 0;
    padding: 6px 12px;
    background: #eef4fa;
    border: 1px solid #c9d9e8;
    border-radius: 4px;
    color: var(--accent);
    font-size: 15px;
    font-weight: 600;
  }}
  .layout {{ display: flex; min-height: 100vh; }}
  nav.sidebar {{
    width: 300px;
    flex: 0 0 300px;
    background: var(--side-bg);
    border-right: 1px solid var(--line);
    padding: 24px 20px;
    position: sticky;
    top: 0;
    height: 100vh;
    overflow-y: auto;
  }}
  nav.sidebar h2 {{ font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 0 0 12px; }}
  .masthead {{ margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px solid var(--line); }}
  .masthead-title {{ font-size: 26px; font-weight: 700; margin: 0; line-height: 1.2; color: var(--ink); }}
  .masthead-vertical {{ font-size: 15px; font-weight: 600; color: var(--accent); margin: 2px 0 6px; }}
  .masthead-tagline {{ font-size: 13px; color: var(--muted); margin: 0; line-height: 1.45; }}
  .masthead-by {{ font-size: 13px; color: var(--muted); margin: 10px 0 0; }}
  .masthead-logo {{ height: 18px; width: auto; vertical-align: middle; margin-left: 2px; }}
  .masthead-nav {{ margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px solid var(--line); }}
  .masthead-nav a {{ font-weight: 600; }}
  .masthead-legend {{ margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px solid var(--line); }}
  .masthead-legend h3 {{ font-size: 13px; text-transform: uppercase; letter-spacing: 0.06em; color: var(--muted); margin: 0 0 10px; }}
  .masthead-legend p {{ font-size: 13px; color: var(--muted); margin: 0 0 8px; line-height: 1.45; }}
  .masthead-legend .dots {{ color: var(--ink); font-weight: 600; letter-spacing: 1px; }}
  nav.sidebar ul {{ list-style: none; padding: 0; margin: 0; }}
  nav.sidebar li {{ margin: 2px 0; }}
  nav.sidebar li li {{ padding-left: 14px; }}
  nav.sidebar li li li {{ padding-left: 14px; }}
  nav.sidebar a {{ color: var(--ink); text-decoration: none; font-size: 14px; line-height: 1.45; display: block; padding: 3px 6px; border-radius: 4px; }}
  nav.sidebar a:hover {{ background: #ececea; }}
  nav.sidebar .new-badge {{
    display: inline-block; font-size: 10px; font-weight: 700; color: #fff;
    background: #b3261e; border-radius: 3px; padding: 0 4px; margin-left: 4px;
    vertical-align: middle;
  }}
  nav.sidebar .toc-controls {{ margin: 0 0 10px; }}
  nav.sidebar .toc-controls button {{
    font-size: 12px; padding: 2px 8px; margin-right: 4px; cursor: pointer;
    background: #fff; border: 1px solid var(--line); border-radius: 4px; color: var(--ink);
  }}
  nav.sidebar .toc-controls button:hover {{ background: #ececea; }}
  nav.sidebar .toc li.has-children > a .toc-toggle {{
    display: inline-block; cursor: pointer; width: 0; height: 0;
    border-left: 4px solid transparent; border-right: 4px solid transparent;
    border-top: 5px solid var(--muted); vertical-align: middle; margin-right: 5px;
  }}
  nav.sidebar .toc li.toc-collapsed > a .toc-toggle {{ transform: rotate(-90deg); }}
  nav.sidebar .toc li.toc-collapsed > ul {{ display: none; }}
  main {{ flex: 1; min-width: 0; padding: 32px 48px 64px; max-width: 860px; }}
  main h1 {{ font-size: 28px; margin: 0 0 8px; line-height: 1.25; }}
  main h2 {{ font-size: 22px; margin: 40px 0 12px; padding-top: 16px; border-top: 1px solid var(--line); line-height: 1.3; }}
  main h3 {{ font-size: 18px; margin: 28px 0 10px; line-height: 1.35; }}
  main h4 {{ font-size: 16px; margin: 20px 0 8px; }}
  h2 .toggle, h3 .toggle, h4 .toggle {{
    cursor: pointer; margin-right: 6px;
    user-select: none; display: inline-block; width: 0; height: 0;
    border-left: 5px solid transparent; border-right: 5px solid transparent;
    border-top: 6px solid var(--muted); vertical-align: middle;
  }}
  /* Content headings: the .section-body is the heading's next sibling
     (inserted by the JS below), so collapse hides the adjacent sibling,
     not a child. */
  h2.collapsed + .section-body, h3.collapsed + .section-body, h4.collapsed + .section-body {{ display: none; }}
  h2.collapsed .toggle, h3.collapsed .toggle, h4.collapsed .toggle {{ transform: rotate(-90deg); }}
  main p {{ margin: 8px 0; }}
  main ul, main ol {{ margin: 8px 0; padding-left: 24px; }}
  main li {{ margin: 4px 0; }}
  main li > ul, main li > ol {{ margin: 4px 0; }}
  main a {{ color: var(--accent); }}
  main table {{ border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 14px; }}
  main th, main td {{ border: 1px solid var(--line); padding: 8px 10px; text-align: left; vertical-align: top; }}
  main th {{ background: var(--side-bg); font-weight: 600; }}
  main hr {{ border: none; border-top: 1px solid var(--line); margin: 32px 0; }}
  details {{ border: 1px solid var(--line); border-radius: 6px; margin: 10px 0; padding: 0; }}
  details > summary {{
    cursor: pointer; padding: 10px 14px; font-weight: 600; list-style: none;
    border-radius: 6px;
  }}
  details > summary::-webkit-details-marker {{ display: none; }}
  details > summary::before {{
    content: ""; display: inline-block; width: 0; height: 0;
    border-left: 4px solid transparent; border-right: 4px solid transparent;
    border-top: 5px solid var(--muted); vertical-align: middle; margin-right: 6px;
  }}
  details[open] > summary::before {{ transform: rotate(0deg); }}
  details:not([open]) > summary::before {{ transform: rotate(-90deg); }}
  details > summary:hover {{ background: var(--side-bg); }}
  details[open] > summary {{ border-bottom: 1px solid var(--line); border-radius: 6px 6px 0 0; }}
  details > ul, details > p {{ padding: 4px 14px 10px; margin: 0; }}
  details > ul {{ padding-left: 38px; }}
  blockquote {{ border-left: 3px solid var(--line); margin: 12px 0; padding: 4px 16px; color: var(--muted); }}
  .meta {{ color: var(--muted); font-size: 14px; margin: 0 0 24px; }}
  @media (max-width: 900px) {{
    .layout {{ flex-direction: column; }}
    nav.sidebar {{ width: 100%; flex: none; height: auto; position: static; border-right: none; border-bottom: 1px solid var(--line); }}
    main {{ padding: 24px 20px 48px; }}
  }}
</style>
</head>
<body>
<div class="layout">
  <nav class="sidebar">
    <div class="masthead">
      <p class="masthead-title">CI Sitrep</p>
      <p class="masthead-vertical">Code &amp; Finance</p>
      <p class="masthead-tagline">Created Intelligence in code and finance — as of today.</p>
      <p class="masthead-by">by <img src="confluence-wordmark.png" alt="Confluence&lt;1&gt;" class="masthead-logo"></p>
    </div>
    <div class="masthead-nav">
      <a href="about.html">About</a>
      <a href="explainer.html">The names: CI, CIA, CIAC</a>
      <a href="theses.html">Foundational theses</a>
      <a href="archive.html">Archive</a>
    </div>
    <div class="masthead-legend">
      <h3>Credibility</h3>
      <p><span class="dots">●●●●</span> Established — peer-reviewed and independently confirmed, or a primary regulatory document.</p>
      <p><span class="dots">●●●○</span> Corroborated — peer-reviewed single study, or a credible source confirmed independently.</p>
      <p><span class="dots">●●○○</span> Reported — single credible source, not yet independently verified.</p>
      <p><span class="dots">●○○○</span> Claimed — vendor claim or single uncorroborated report.</p>
    </div>
    <h2>Contents</h2>
    {toc}
    <p class="meta" style="margin-top: 20px;">© 2026 Confluence&lt;1&gt; Corp. All rights reserved.<br>
    Source: SYNTHESIZED.md (Markdown is the source of truth).</p>
  </nav>
  <main>
    {body}
  </main>
</div>
<script>
(function () {{
  // Sidebar TOC: make every section collapsible (drill-down / roll-up).
  // Each TOC entry with children gets a toggle arrow; Expand all /
  // Collapse all buttons sit above the TOC, and a Sections control
  // expands/collapses all content headings.
  var toc = document.querySelector('nav.sidebar .toc');
  if (toc) {{
    var controls = document.createElement('div');
    controls.className = 'toc-controls';
    controls.innerHTML = '<button type="button" data-act="expand">Expand all</button>' +
      '<button type="button" data-act="collapse">Collapse all</button>';
    toc.parentNode.insertBefore(controls, toc);
    controls.addEventListener('click', function (e) {{
      var btn = e.target.closest('button');
      if (!btn) return;
      var collapse = btn.getAttribute('data-act') === 'collapse';
      toc.querySelectorAll('li.has-children').forEach(function (li) {{
        li.classList.toggle('toc-collapsed', collapse);
      }});
    }});
    toc.querySelectorAll('li').forEach(function (li) {{
      var childUl = li.querySelector(':scope > ul');
      if (!childUl) return;
      li.classList.add('has-children');
      li.classList.add('toc-collapsed');  // TOC starts collapsed: top-level only.
      var link = li.querySelector(':scope > a');
      if (!link) return;
      var toggle = document.createElement('span');
      toggle.className = 'toc-toggle';
      // No text content: the arrow is drawn with CSS borders (see .toc-toggle),
      // so it renders identically on every system instead of depending on
      // a font carrying the U+25B8/U+25BE triangle glyphs.
      link.insertBefore(toggle, link.firstChild);
      toggle.addEventListener('click', function (e) {{
        e.preventDefault();
        e.stopPropagation();
        li.classList.toggle('toc-collapsed');
      }});
    }});
    // Sections control: expand/collapse all content headings.
    var secControls = document.createElement('div');
    secControls.className = 'toc-controls';
    secControls.innerHTML = 'Sections: <button type="button" data-act="expand">Expand all</button>' +
      '<button type="button" data-act="collapse">Collapse all</button>';
    toc.parentNode.insertBefore(secControls, toc.nextSibling);
    secControls.addEventListener('click', function (e) {{
      var btn = e.target.closest('button');
      if (!btn) return;
      var collapse = btn.getAttribute('data-act') === 'collapse';
      document.querySelectorAll('main h2, main h3, main h4').forEach(function (h) {{
        h.classList.toggle('collapsed', collapse);
      }});
    }});
  }}
  // Make h2/h3/h4 headings collapsible: clicking the heading toggles the
  // content that follows it (up to the next heading of equal or higher level).
  // Article headlines are native <details> and already collapsible.
  // Everything starts COLLAPSED so the reader drills into one section at
  // a time; Expand all (sidebar) opens the whole tree.
  var main = document.querySelector('main');
  if (!main) return;
  var headings = main.querySelectorAll('h2, h3, h4');
  headings.forEach(function (h) {{
    var level = parseInt(h.tagName.substring(1), 10);
    var toggle = document.createElement('span');
    toggle.className = 'toggle';
    h.prepend(toggle);
    h.style.cursor = 'pointer';
    h.classList.add('collapsed');
    // Wrap following siblings until the next heading of equal/higher level.
    var body = document.createElement('div');
    body.className = 'section-body';
    var node = h.nextSibling;
    var collected = [];
    while (node) {{
      var next = node.nextSibling;
      if (node.nodeType === 1 && /^H[1-4]$/.test(node.tagName)) {{
        var nl = parseInt(node.tagName.substring(1), 10);
        if (nl <= level) break;
      }}
      collected.push(node);
      node = next;
    }}
    collected.forEach(function (n) {{ body.appendChild(n); }});
    h.parentNode.insertBefore(body, h.nextSibling);
    h.addEventListener('click', function (e) {{
      // Do not toggle when the click was on a link inside the heading.
      if (e.target.closest('a')) return;
      h.classList.toggle('collapsed');
    }});
    // Start with h4 sections collapsed, h2/h3 open.
    if (level === 4) h.classList.add('collapsed');
  }});
  // Jumping to an anchor (from the sidebar or New this week) expands any
  // collapsed ancestor section so the target is visible.
  function expandForAnchor() {{
    var id = location.hash && location.hash.slice(1);
    if (!id) return;
    var el = document.getElementById(id);
    if (!el) return;
    var node = el;
    while (node) {{
      if (node.classList && node.classList.contains('section-body')) {{
        var prev = node.previousElementSibling;
        if (prev) prev.classList.remove('collapsed');
      }}
      node = node.parentElement;
    }}
    el.scrollIntoView();
  }}
  window.addEventListener('hashchange', expandForAnchor);
  expandForAnchor();
}})();
</script>
</body>
</html>
"""


def main(argv):
    input_path = Path(argv[1]) if len(argv) > 1 else WATCHES / "SYNTHESIZED.md"
    output_path = Path(argv[2]) if len(argv) > 2 else WATCHES / "SYNTHESIZED.html"
    build(input_path, output_path)


if __name__ == "__main__":
    main(sys.argv)
