#!/usr/bin/env python3
"""Build a standalone reading page from a Markdown file.

Generic page builder for the ci-sitrep site (explainer, theses paper, ...).
Converts the markdown to a self-contained HTML page in the same visual
language as the main report (index.html): sidebar TOC, collapsible
headings, collapsible TOC sections, and a link back to the report.

Usage: build_page.py <input.md> <output.html> [title]
The title defaults to the document's first h1.
"""

import re
import sys
from pathlib import Path

import markdown

REPO = Path.home() / "workspace" / "ci-sitrep"


def github_slugify(text, separator="-"):
    """Match GitHub's heading-anchor algorithm."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return text.replace(" ", separator)


def build(input_path, output_path, title=None):
    src = Path(input_path).read_text(encoding="utf-8")
    if title is None:
        m = re.search(r"^#\s+(.+)$", src, re.MULTILINE)
        title = m.group(1).strip() if m else Path(input_path).stem

    md = markdown.Markdown(
        extensions=["tables", "toc", "sane_lists"],
        extension_configs={
            "toc": {
                "slugify": github_slugify,
                "toc_depth": "2-4",
            },
        },
    )
    body = md.convert(src)
    # External links open in a new tab, so following a source never replaces
    # the report. Internal links (anchors, .html pages, mailto) are untouched.
    body = re.sub(
        r'<a href="(https?://[^"]+)">',
        r'<a href="\1" target="_blank" rel="noopener">',
        body,
    )
    # Mobile-only back link at the top of the content (see .back-inline):
    # on a phone the sidebar sits below the content, so the reader needs a
    # way back to the report without scrolling to the bottom of the page.
    back_inline = '<p class="back-inline"><a href="index.html">&larr; Back to the report</a></p>'
    if "</h1>" in body:
        body = body.replace("</h1>", "</h1>\n" + back_inline, 1)
    toc_html = md.toc

    html = TEMPLATE.format(
        title=title,
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
    --line: #ddd5c2;
    --accent: #283060;
    --logo-navy: #283060;
    --bg: #faf6ef;
    --side-bg: #faf6ef;
    --code-bg: #f3ede0;
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
  nav.sidebar ul {{ list-style: none; padding: 0; margin: 0; }}
  nav.sidebar li {{ margin: 2px 0; }}
  nav.sidebar li li {{ padding-left: 14px; }}
  nav.sidebar li li li {{ padding-left: 14px; }}
  nav.sidebar a {{ color: var(--ink); text-decoration: none; font-size: 14px; line-height: 1.45; display: block; padding: 3px 6px; border-radius: 4px; }}
  nav.sidebar a:hover {{ background: #e8dfcc; }}
  nav.sidebar .toc-controls {{ margin: 0 0 10px; }}
  nav.sidebar .toc-controls button {{
    font-size: 12px; padding: 2px 8px; margin-right: 4px; cursor: pointer;
    background: #fdfbf7; border: 1px solid var(--line); border-radius: 4px; color: var(--ink);
  }}
  nav.sidebar .toc-controls button:hover {{ background: #e8dfcc; }}
  nav.sidebar .toc li.has-children > a .toc-toggle {{
    display: inline-block; cursor: pointer; width: 0; height: 0;
    border-left: 4px solid transparent; border-right: 4px solid transparent;
    border-top: 5px solid var(--muted); vertical-align: middle; margin-right: 5px;
  }}
  nav.sidebar .toc li.toc-collapsed > a .toc-toggle {{ transform: rotate(-90deg); }}
  nav.sidebar .toc li.toc-collapsed > ul {{ display: none; }}
  /* Masthead: the CI Sitrep wordmark, linking back to the report. */
  .masthead {{ margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px solid var(--line); }}
  .masthead-title {{ font-family: Georgia, 'Times New Roman', Times, serif; font-size: 26px; font-weight: 700; margin: 0; line-height: 1.2; }}
  nav.sidebar .masthead-title a {{ color: #283060; text-decoration: none; display: inline; padding: 0; }}
  nav.sidebar .masthead-title a:hover {{ background: none; }}
  .masthead-vertical {{ font-family: Georgia, 'Times New Roman', Times, serif; font-size: 15px; font-weight: 600; font-style: italic; color: #283060; margin: 2px 0 0; }}
  nav.sidebar .back {{ margin: 0 0 18px; padding-bottom: 16px; border-bottom: 1px solid var(--line); }}
  nav.sidebar .back a {{ color: var(--accent); font-weight: 600; }}
  /* Mobile-only back link at the top of the content: on a phone the
     sidebar sits below the content, so the reader needs a way back to
     the report without scrolling to the bottom of the page. */
  .back-inline {{ display: none; }}
  main {{ flex: 1; min-width: 0; padding: 32px 48px 64px; max-width: 860px; }}
  main h1 {{ font-family: Georgia, 'Times New Roman', Times, serif; font-size: 28px; margin: 64px 0 8px; line-height: 1.25; color: var(--logo-navy); }}
  main h1:first-of-type {{ margin: -32px -48px 16px; padding: 28px 48px; color: #fff; background: var(--logo-navy); }}
  main h1 em {{ display: block; font-size: 20px; margin-top: 2px; }}
  main h2 {{ font-family: Georgia, 'Times New Roman', Times, serif; font-size: 22px; margin: 40px 0 12px; padding-top: 16px; border-top: 1px solid var(--line); line-height: 1.3; color: var(--logo-navy); }}
  main h3 {{ font-size: 18px; margin: 28px 0 10px; line-height: 1.35; color: var(--logo-navy); }}
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
  /* Share link: a small link icon at the end of every section heading.
     Copies the direct URL to that section. Hidden until hover on desktop;
     always visible on mobile (no hover on touch). The icon is inline SVG,
     not a font glyph. */
  .share-link {{
    display: inline-block;
    margin-left: 8px;
    padding: 4px 6px;
    border: none;
    background: none;
    color: var(--muted);
    cursor: pointer;
    opacity: 0;
    vertical-align: middle;
    line-height: 1;
    border-radius: 4px;
  }}
  .share-link svg {{ display: block; }}
  h1:hover .share-link, h2:hover .share-link, h3:hover .share-link, h4:hover .share-link,
  .share-link:focus {{ opacity: 1; }}
  .share-link:hover {{ color: var(--accent); background: #efe9da; }}
  .share-link.copied {{ font-size: 12px; font-weight: 600; color: var(--accent); opacity: 1; }}
  p:hover .share-link, summary:hover .share-link {{ opacity: 1; }}
  .table-share {{ text-align: right; margin: 2px 0 12px; }}
  table:hover + .table-share .share-link {{ opacity: 1; }}
  /* Breadcrumbs: a small trail at the top of every section body, back up
     to any ancestor level or the top of the page. Muted, one line. */
  .crumbs {{
    font-size: 13px;
    color: var(--muted);
    margin: 0 0 10px;
  }}
  .crumbs a {{ color: var(--muted); text-decoration: none; }}
  .crumbs a:hover {{ color: var(--accent); text-decoration: underline; }}
  .crumbs .crumb-sep {{ color: var(--line); margin: 0 3px; }}
  /* Back-to-top button: fixed, bottom-right, invisible until the reader
     has scrolled down the page. The arrow is inline SVG, not a font glyph. */
  .back-to-top {{
    position: fixed;
    right: 24px;
    bottom: 24px;
    width: 40px;
    height: 40px;
    border: none;
    border-radius: 50%;
    background: var(--logo-navy);
    color: #fff;
    cursor: pointer;
    opacity: 0;
    pointer-events: none;
    transition: opacity 0.2s;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  }}
  .back-to-top.visible {{ opacity: 0.85; pointer-events: auto; }}
  .back-to-top:hover {{ opacity: 1; }}
  main p {{ margin: 8px 0; }}
  main ul, main ol {{ margin: 8px 0; padding-left: 24px; }}
  main li {{ margin: 4px 0; }}
  main li > ul, main li > ol {{ margin: 4px 0; }}
  main a {{ color: var(--accent); }}
  main table {{ border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 14px; }}
  main th, main td {{ border: 1px solid var(--line); padding: 8px 10px; text-align: left; vertical-align: top; }}
  main th {{ background: var(--side-bg); font-weight: 600; }}
  main hr {{ border: none; border-top: 1px solid var(--line); margin: 32px 0; }}
  main blockquote {{ border-left: 3px solid var(--line); margin: 12px 0; padding: 4px 16px; color: var(--muted); }}
  main em {{ color: var(--muted); }}
  @media (max-width: 900px) {{
    .layout {{ flex-direction: column; }}
    /* On a phone the content comes first and the masthead/sidebar follows below it. */
    main {{ order: 1; padding: 24px 20px 48px; }}
    .share-link {{ opacity: 1; }}
    .back-to-top {{ right: 16px; bottom: 16px; }}
    .back-inline {{ display: block; margin: 0 0 16px; font-size: 14px; }}
    nav.sidebar {{ order: 2; width: 100%; flex: none; height: auto; position: static; border-right: none; border-bottom: none; border-top: 1px solid var(--line); }}
    main h1:first-of-type {{ margin: -24px -20px 16px; padding: 24px 20px; }}
  }}
</style>
</head>
<body>
<div class="layout">
  <nav class="sidebar">
    <div class="masthead">
      <p class="masthead-title"><a href="index.html">CI Sitrep</a></p>
      <p class="masthead-vertical">Code &amp; Finance</p>
    </div>
    <p class="back"><a href="index.html">&larr; Back to the report</a></p>
    <h2>Contents</h2>
    {toc}
  </nav>
  <main>
    {body}
  </main>
</div>
<button class="back-to-top" type="button" aria-label="Back to top" title="Back to top"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5"/><path d="M5 12l7-7 7 7"/></svg></button>
<script>
(function () {{
  // Sidebar TOC: make every section collapsible (drill-down / roll-up).
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
  var main = document.querySelector('main');
  if (!main) return;
  var headings = main.querySelectorAll('h2, h3, h4');
  headings.forEach(function (h) {{
    var level = parseInt(h.tagName.substring(1), 10);
    var toggle = document.createElement('span');
    toggle.className = 'toggle';
    h.prepend(toggle);
    h.style.cursor = 'pointer';
    h.classList.add('collapsed');  // Everything starts collapsed; drill in one section at a time.
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
      if (e.target.closest('a')) return;
      h.classList.toggle('collapsed');
    }});
    if (level === 4) h.classList.add('collapsed');
  }});
  // Breadcrumbs: at the top of every section body, a small trail back up
  // to any ancestor level or the top of the page ("Top · Part I …" on the
  // theses page; "Top · §3 Agentic … · §3.4 Governance" on the report).
  // A reader who drilled down jumps back without scrolling. Built from
  // the heading hierarchy, so it stays correct as sections are added or
  // renamed. Skips the two front-page sections of the report (they sit at
  // the top of the page already) and the page title.
  var crumbHeads = Array.prototype.slice.call(main.querySelectorAll('h1, h2, h3, h4'));
  var firstH1 = main.querySelector('h1');
  crumbHeads.forEach(function (h) {{
    if (h.tagName === 'H1') return;
    if (h.id === 'new-this-week' || h.id === 'what-were-watching') return;
    var level = parseInt(h.tagName.substring(1), 10);
    var ancestors = [];
    var idx = crumbHeads.indexOf(h);
    var need = level - 1;
    for (var k = idx - 1; k >= 0 && need >= 1; k--) {{
      var cand = crumbHeads[k];
      var cl = parseInt(cand.tagName.substring(1), 10);
      if (cl === need) {{
        if (cand !== firstH1) ancestors.unshift(cand);
        need--;
      }}
    }}
    var sbody = h.nextElementSibling;
    if (!sbody || !sbody.classList.contains('section-body')) return;
    var crumbs = document.createElement('p');
    crumbs.className = 'crumbs';
    var chtml = '<a href="#" class="crumb-top" title="Back to the top of the page">↑ Top</a>';
    ancestors.forEach(function (a) {{
      chtml += ' <span class="crumb-sep">·</span> <a href="#' + a.id + '">' + a.textContent.trim() + '</a>';
    }});
    crumbs.innerHTML = chtml;
    sbody.insertBefore(crumbs, sbody.firstChild);
  }});
  // The "Top" crumb smooth-scrolls to the top (no hash change).
  main.addEventListener('click', function (e) {{
    var t = e.target.closest('a.crumb-top');
    if (!t) return;
    e.preventDefault();
    window.scrollTo({{ top: 0, behavior: 'smooth' }});
  }});
  // Share links: every section heading, article headline, substantive
  // paragraph, and table gets a small link button that copies the direct
  // URL to that unit (page + #anchor). The icon is inline SVG, not a font
  // glyph, so it renders identically everywhere. On desktop the button
  // appears on hover of its unit; on touch devices it is always visible
  // (see the .share-link CSS). Clicking it never toggles its unit.
  var LINK_SVG = '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>';
  function slugify(text) {{
    var s = text.toLowerCase()
      .replace(/[^\\w\\s-]/g, '')
      .trim()
      .replace(/\\s+/g, '-')
      .replace(/-+/g, '-')
      .replace(/^-|-$/g, '');
    if (s.length > 60) {{
      s = s.slice(0, 60);
      var cut = s.lastIndexOf('-');
      if (cut > 20) s = s.slice(0, cut);
    }}
    return s;
  }}
  var usedIds = {{}};
  document.querySelectorAll('[id]').forEach(function (el) {{ usedIds[el.id] = true; }});
  function uniqueId(base) {{
    if (!base) base = 'item';
    var id = base, n = 2;
    while (usedIds[id]) {{ id = base + '-' + n; n++; }}
    usedIds[id] = true;
    return id;
  }}
  function copyUrl(id, btn) {{
    var origin = location.origin || (location.protocol + '//' + location.host);
    var path = location.pathname.replace(/\\/index\\.html$/, '/');
    var url = origin + path + '#' + id;
    function done() {{
      btn.classList.add('copied');
      btn.textContent = 'Copied';
      setTimeout(function () {{
        btn.classList.remove('copied');
        btn.innerHTML = LINK_SVG;
      }}, 1500);
    }}
    function fallbackCopy(text) {{
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try {{ document.execCommand('copy'); }} catch (err) {{}}
      document.body.removeChild(ta);
      done();
    }}
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(url).then(done, function () {{ fallbackCopy(url); }});
    }} else {{
      fallbackCopy(url);
    }}
  }}
  function makeShareButton(id, label) {{
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'share-link';
    btn.setAttribute('aria-label', label);
    btn.title = label;
    btn.innerHTML = LINK_SVG;
    btn.addEventListener('click', function (e) {{
      // Never toggle the enclosing heading or <details>: the click is
      // only for copying. preventDefault cancels the <summary> toggle,
      // stopPropagation keeps the heading collapse handler out of it.
      e.stopPropagation();
      e.preventDefault();
      copyUrl(id, btn);
    }});
    return btn;
  }}
  // Headings (all except the page title).
  var shareHeads = main.querySelectorAll('h1, h2, h3, h4');
  shareHeads.forEach(function (h, i) {{
    if (!h.id) return;
    if (i === 0 && h.tagName === 'H1') return;  // the page title is not a section
    h.appendChild(makeShareButton(h.id, 'Copy link to this section'));
  }});
  // Articles: the <details> blocks. Skips the How-to-read block, the
  // mobile Contents block, and the See-also cross-link blocks. The id
  // goes on the <details> itself; the button goes in its <summary>.
  main.querySelectorAll('details').forEach(function (d) {{
    if (d.classList.contains('how-to-read') || d.classList.contains('toc-inline')) return;
    var sum = d.querySelector(':scope > summary');
    if (!sum) return;
    var text = sum.textContent.trim();
    if (text === 'See also') return;
    if (!d.id) d.id = uniqueId(slugify(text));
    sum.appendChild(makeShareButton(d.id, 'Copy link to this article'));
  }});
  // Tables: id from the nearest preceding heading, button in a small
  // right-aligned row just below the table.
  var allHeads = Array.prototype.slice.call(main.querySelectorAll('h1, h2, h3, h4'));
  main.querySelectorAll('table').forEach(function (tbl) {{
    var head = null;
    for (var k = 0; k < allHeads.length; k++) {{
      if (allHeads[k].compareDocumentPosition(tbl) & Node.DOCUMENT_POSITION_FOLLOWING) head = allHeads[k];
      else break;
    }}
    var base = (head && head.id ? head.id + '-table' : 'table');
    if (!tbl.id) tbl.id = uniqueId(base);
    var row = document.createElement('div');
    row.className = 'table-share';
    row.appendChild(makeShareButton(tbl.id, 'Copy link to this table'));
    tbl.parentNode.insertBefore(row, tbl.nextSibling);
  }});
  // Substantive paragraphs: prose outside any <details>, long enough to be
  // worth sharing, not a Sources line or the As-of banner. The button goes
  // inline at the end of the paragraph.
  main.querySelectorAll('p').forEach(function (p) {{
    if (p.closest('details')) return;
    if (p.classList.contains('as-of-banner')) return;
    if (p.classList.contains('crumbs')) return;
    var text = p.textContent.trim();
    if (text.length < 80) return;
    if (text.indexOf('Sources:') === 0) return;
    if (!p.id) p.id = uniqueId(slugify(text));
    p.appendChild(makeShareButton(p.id, 'Copy link to this paragraph'));
  }});

  // Back-to-top button: appears once the reader has scrolled down the
  // page, smooth-scrolls back to the top. Invisible until needed.
  var toTop = document.querySelector('.back-to-top');
  if (toTop) {{
    window.addEventListener('scroll', function () {{
      toTop.classList.toggle('visible', window.scrollY > 500);
    }}, {{ passive: true }});
    toTop.addEventListener('click', function () {{
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }});
  }}
  // Jumping to an anchor expands any collapsed ancestor section.
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
      if (node.tagName === 'DETAILS') node.open = true;
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
    if len(argv) < 3:
        print("Usage: build_page.py <input.md> <output.html> [title]", file=sys.stderr)
        sys.exit(2)
    input_path = Path(argv[1])
    output_path = Path(argv[2])
    title = argv[3] if len(argv) > 3 else None
    build(input_path, output_path, title)


if __name__ == "__main__":
    main(sys.argv)
