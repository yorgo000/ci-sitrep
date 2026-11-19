#!/usr/bin/env python3
"""Build the QA mirror of CI SITREP into qa/ (same repo, GitHub Pages).

The QA server is a review deployment: Yorgo reviews here, Barnaby revises
here, and only a Chief Editor release decision promotes changes to the live
report. Live at https://yorgo000.github.io/ci-sitrep/qa/ after push.

Assumes the staging root is already built (normal build: build_html.py,
build_page.py for the sub-pages, build_audit.py, export_findings.py).

Steps:
  1. Run verify.py on the staging-root build; abort on failure.
  2. Rebuild qa/ from scratch as a mirror of the servable site (html, md,
     json, png, css, js at root, plus archive/, data/, youtube/).
     _tools/ is NOT mirrored (not linked from any page).
  3. Post-process qa/*.html: strip the GoatCounter snippet (QA visits must
     not pollute production analytics) and inject a sticky QA banner plus
     a noindex meta tag.
  4. Report file counts.

Usage: python3 _tools/build_qa.py   (run from ~/workspace/ci-sitrep)
Push:  loop github.py put over qa/ (see the QA runbook in RULES.md §6).
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QA = ROOT / "qa"
VENV_PY = ROOT / "_tools" / "venv" / "bin" / "python"
PY = str(VENV_PY) if VENV_PY.exists() else sys.executable

ROOT_EXTS = {".html", ".md", ".json", ".png", ".css", ".js"}
MIRROR_DIRS = ("archive", "data", "youtube")

GOAT_RE = re.compile(r'<script[^>]*goatcounter[^>]*></script>\n?', re.IGNORECASE)
BANNER = (
    '<div style="position:sticky;top:0;z-index:9999;background:#b3543f;'
    'color:#fff;font:600 15px/1.4 system-ui,sans-serif;padding:8px 16px;'
    'text-align:center">QA &mdash; review copy, not the live report &middot; '
    '<a href="../index.html" style="color:#fff;text-decoration:underline">'
    'live report &rarr;</a></div>\n'
)
NOINDEX = '<meta name="robots" content="noindex, nofollow">\n'


def run(cmd, **kw):
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, **kw)
    return r


def main():
    # 1. Verify the staging-root build first; a failing build never reaches QA.
    v = run([PY, "_tools/verify.py", "SYNTHESIZED.md", "index.html"])
    tail = (v.stdout + v.stderr).strip().splitlines()[-5:]
    print("\n".join(tail))
    if v.returncode != 0:
        print("verify.py FAILED — QA build aborted.", file=sys.stderr)
        sys.exit(1)

    # 2. Rebuild qa/ from scratch.
    if QA.exists():
        shutil.rmtree(QA)
    QA.mkdir()
    n_files = 0
    for p in sorted(ROOT.iterdir()):
        if p.name in ("qa", "_tools") or p.name.startswith("."):
            continue
        if p.is_file() and p.suffix in ROOT_EXTS:
            shutil.copy2(p, QA / p.name)
            n_files += 1
    for d in MIRROR_DIRS:
        src = ROOT / d
        if src.is_dir():
            shutil.copytree(
                src, QA / d,
                ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
            )
            n_files += sum(1 for _ in (QA / d).rglob("*") if _.is_file())

    # 3. Post-process QA HTML: strip analytics, add banner + noindex.
    n_html = 0
    n_stripped = 0
    for html in sorted(QA.rglob("*.html")):
        text = html.read_text(encoding="utf-8")
        new, n = GOAT_RE.subn("", text)
        n_stripped += n
        if "<body" in new:
            new = re.sub(r"(<body[^>]*>)", r"\1\n" + BANNER, new, count=1)
        if "</head>" in new:
            new = new.replace("</head>", NOINDEX + "</head>", 1)
        html.write_text(new, encoding="utf-8")
        n_html += 1

    print(f"QA mirror built: {n_files} files, {n_html} HTML pages, "
          f"GoatCounter stripped from {n_stripped} page(s).")
    print("Live at https://yorgo000.github.io/ci-sitrep/qa/ after push.")


if __name__ == "__main__":
    main()
