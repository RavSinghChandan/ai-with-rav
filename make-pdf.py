import markdown, re, pathlib
src = pathlib.Path("v01-what-is-machine-learning.md").read_text()
# ensure a blank line before any bullet list that follows a text line (fixes merged bullets)
src = re.sub(r'([^\n])\n(- )', r'\1\n\n\2', src)
here = pathlib.Path.cwd().as_uri()
src = re.sub(r'\]\(images/', f']({here}/images/', src)
html_body = markdown.markdown(src, extensions=['tables','fenced_code','codehilite','sane_lists'])
css = """
@page { size: A4; margin: 14mm 14mm; }
* { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: -apple-system,'Segoe UI',Roboto,Arial,sans-serif; color:#0f2530; line-height:1.6; font-size:12.5pt; max-width:800px; margin:0 auto; }
h1 { color:#FF6B35; font-size:24pt; border-bottom:4px solid #FFD166; padding-bottom:6px; }
h2 { color:#118AB2; font-size:16pt; margin-top:22px; border-left:5px solid #06D6A0; padding-left:10px; }
h3 { color:#073B4C; font-size:13pt; }
img { max-width:100%; display:block; margin:16px auto; border:1px solid #eee; border-radius:8px; }
blockquote { background:#FFF8E7; border-left:5px solid #FFD166; margin:12px 0; padding:8px 14px; border-radius:6px; }
table { border-collapse:collapse; width:100%; margin:12px 0; font-size:11pt; }
th { background:#118AB2; color:#fff; padding:7px 10px; text-align:left; }
td { border:1px solid #ddd; padding:6px 10px; }
tr:nth-child(even){ background:#f7fbfd; }
ul,ol { margin:10px 0 10px 6px; } li { margin:5px 0; }
code { background:#f3f3f3; padding:1px 5px; border-radius:4px; font-size:11pt; }
pre { background:#0f2530; color:#e8f0f2; padding:12px 14px; border-radius:8px; overflow-x:auto; font-size:10.5pt; }
pre code { background:none; color:inherit; }
hr { border:none; border-top:2px dashed #ccc; margin:22px 0; }
a { color:#118AB2; }
"""
html = f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{html_body}</body></html>"
pathlib.Path("/tmp/v01.html").write_text(html)
print("HTML rebuilt with fixed lists")
