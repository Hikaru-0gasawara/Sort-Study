"""Gera um PDF para cada resumo .md desta pasta.

Uso:  pip install markdown-it-py mdit-py-plugins
      python build_pdfs.py            (requer Microsoft Edge instalado)
"""
import html, re, subprocess, sys, tempfile
from pathlib import Path
from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
HERE = Path(__file__).parent
KATEX = "https://cdn.jsdelivr.net/npm/katex@0.16.11/dist"

CSS = """
@page { size: A4; margin: 16mm 15mm; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; color: #1d2330; background: #fff; }
h1 { color: #0b3d91; border-bottom: 3px solid #0b3d91; padding-bottom: 4px; font-size: 21pt; }
h2 { color: #0b3d91; border-bottom: 1px solid #c8d3e6; padding-bottom: 2px; margin-top: 26px; break-after: avoid; }
h3 { color: #234; margin-top: 18px; break-after: avoid; }
h4 { color: #345; break-after: avoid; }
code { font-family: Consolas, monospace; font-size: 9.5pt; background: #f1f3f7; padding: 0 3px; border-radius: 3px; }
pre { background: #f6f8fb; border: 1px solid #dde3ee; border-radius: 6px; padding: 8px 10px; break-inside: avoid; white-space: pre-wrap; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; margin: 8px 0; font-size: 9.5pt; break-inside: avoid; }
th, td { border: 1px solid #c8d3e6; padding: 4px 7px; vertical-align: top; }
th { background: #e8eef8; }
blockquote { margin: 10px 0; padding: 6px 12px; background: #fff8e6; border-left: 4px solid #f0a500; border-radius: 4px; break-inside: avoid; }
blockquote p { margin: 4px 0; }
.katex-display { margin: 8px 0; overflow-x: auto; overflow-y: hidden; }
a { color: #0b5cd5; text-decoration: none; }
"""

md = MarkdownIt("commonmark", {"html": False}).enable("table").use(dollarmath_plugin, double_inline=True)


def to_html(src: str, title: str) -> str:
    body = md.render(src)
    body = re.sub(r'href="([^"/:]+)\.md(#[^"]*)?"', r'href="\1.pdf\2"', body)  # links entre resumos apontam para os PDFs
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{html.escape(title)}</title>
<link rel="stylesheet" href="{KATEX}/katex.min.css"><style>{CSS}</style></head><body>{body}
<script src="{KATEX}/katex.min.js"></script>
<script>document.querySelectorAll('.math').forEach(function (el) {{
  katex.render(el.textContent, el, {{displayMode: el.classList.contains('block'), throwOnError: false}});
}});</script></body></html>"""


def main(names):
    files = [HERE / n for n in names] if names else sorted(HERE.glob("[0-9][0-9]_*.md"))
    with tempfile.TemporaryDirectory() as tmp:
        for f in files:
            title = f.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
            page = Path(tmp) / (f.stem + ".html")
            page.write_text(to_html(f.read_text(encoding="utf-8"), title), encoding="utf-8")
            out = f.with_suffix(".pdf")
            # perfil separado: sem ele o Edge já aberto absorve a chamada e não gera o PDF
            subprocess.run([EDGE, "--headless", "--disable-gpu", "--no-pdf-header-footer", f"--user-data-dir={tmp}/perfil",
                            "--virtual-time-budget=15000", f"--print-to-pdf={out}", page.as_uri()],
                           check=True, capture_output=True)
            print("ok", out.name)


if __name__ == "__main__":
    main(sys.argv[1:])
