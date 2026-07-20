#!/usr/bin/env python3
# Rulebook-compliant md -> DARK pdf. Usage: python3 make-pdf.py vNN-file.md "Output Title"
import markdown, re, pathlib, sys, subprocess

md_file = sys.argv[1] if len(sys.argv)>1 else "v01-what-is-machine-learning.md"
out_pdf = sys.argv[2] if len(sys.argv)>2 else "Day-01-What-is-Machine-Learning.pdf"

src = pathlib.Path(md_file).read_text()

# ---- RULEBOOK CLEANUP (strip webpage clutter) ----
# 1. remove the "Day X · ~min · links" nav line entirely
src = re.sub(r'^>\s*\*\*Day.*?\n', '', src, flags=re.M)
# 2. strip ALL markdown links -> keep just the text  [text](url) -> text
src = re.sub(r'\[([^\]]+)\]\((?!images/)[^)]+\)', r'\1', src)
# 3. collapse runs of '---' dividers: keep content, we render only a few subtle ones via CSS hr — drop most
#    (leave hr in markdown; CSS makes them very subtle. But remove 3+ consecutive.)
# 4. fix images path to absolute for Chrome
here = pathlib.Path.cwd().as_uri()
src = re.sub(r'\]\(images/', f']({here}/images/', src)
# 5. ensure blank line before bullet lists (fixes merged bullets)
src = re.sub(r'([^\n])\n(- )', r'\1\n\n\2', src)

html_body = markdown.markdown(src, extensions=['tables','fenced_code','codehilite','sane_lists'])

# strip any leftover broken/mojibake sequences just in case
html_body = html_body.replace('�','')
# EMOJISTRIP: remove decorative emoji so nothing renders as a rough glyph in the PDF.
# Keep useful arrows (→ ← ↑ ↓ ⟶) — only strip pictographic emoji + variation selectors.
_emoji = re.compile('['
    '\U0001F300-\U0001FAFF\U0001F000-\U0001F0FF\U0001F1E6-\U0001F1FF'
    '\U00002600-\U000026FF\U00002700-\U000027BF\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F]+', re.UNICODE)
html_body = _emoji.sub('', html_body)
html_body = re.sub(r'(<h[1-3][^>]*>)\s+', r'\1', html_body)


css = """
@page { size: A4; margin: 13mm 13mm; background:#0d1117; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; box-sizing:border-box; }
html,body { background:#0d1117 !important; }
body { font-family:-apple-system,'Segoe UI',Roboto,Arial,sans-serif; color:#e6edf3;
       line-height:1.65; font-size:12.5pt; max-width:820px; margin:0 auto; padding:6px 4px; }
h1 { color:#FF6B35; font-size:23pt; font-weight:800; border-bottom:3px solid #FF6B35; padding-bottom:8px; margin-bottom:4px; }
h2 { color:#33B5E5; font-size:16pt; margin-top:26px; border-left:5px solid #06D6A0; padding-left:11px; }
h3 { color:#e6edf3; font-size:13pt; }
p,li { color:#e6edf3; }
strong { color:#FFD166; }
em { color:#9fb3c8; }
img { max-width:100%; display:block; margin:18px auto; border-radius:10px; }
blockquote { background:#161b22; border-left:5px solid #FFD166; margin:14px 0; padding:10px 16px; border-radius:8px; color:#e6edf3; }
blockquote strong { color:#FFD166; }
table { border-collapse:collapse; width:100%; margin:14px 0; font-size:11pt; }
th { background:#33B5E5; color:#0d1117; padding:8px 11px; text-align:left; font-weight:800; }
td { border:1px solid #30363d; padding:7px 11px; color:#e6edf3; }
tr:nth-child(even) td { background:#161b22; }
ul,ol { margin:10px 0 10px 8px; } li { margin:6px 0; }
code { background:#161b22; color:#79c0ff; padding:2px 6px; border-radius:5px; font-size:11pt; font-family:'SF Mono',Menlo,monospace; }
pre { background:#161b22; color:#e6edf3; padding:14px 16px; border-radius:10px; overflow-x:auto; font-size:10.5pt; border:1px solid #30363d; }
pre code { background:none; color:#e6edf3; }
hr { border:none; border-top:1px solid #21262d; margin:20px 0; }
a { color:#33B5E5; text-decoration:none; }
"""
html = f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{html_body}</body></html>"
pathlib.Path("/tmp/_vid.html").write_text(html)

chrome="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
subprocess.run([chrome,"--headless=new","--disable-gpu","--no-pdf-header-footer",
    f"--print-to-pdf={out_pdf}","file:///tmp/_vid.html"],
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("PDF built:", out_pdf)
