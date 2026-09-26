"""
SHORTS TEMPLATE — AI With Rav.

Two landscape pages built for a sub-3-minute reel:

    page 1   THE HOOK, huge, plus the diagram under it
    page 2   the three beats and the takeaway

WHAT CHANGED AND WHY
--------------------
The first version put a chapter-style title on page 1 at 22pt on white. Two
things were wrong with that against how short-form actually performs:

1. Short-form guidance is a hook of six to eight words, centred, bold and high
   contrast, resolved within three seconds. A descriptive title like "Why a dot
   product is just agreement" is a heading, not a hook.
2. 80%+ of phone users run dark mode, and saturated accents pop against
   near-black. A white page in a dark feed reads as a document.

So the ground is now near-black, the hook is 40pt+ and sits alone at the top of
page 1, and the brand cyan carries the emphasis.

    python3.12 build_short_pdf.py topics/<topic>/shorts/sNN.md
"""
import os
import re
import sys

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import Paragraph

# Palette — AIWithRav brand, sampled from the channel banner.
# White ground: the slides must read on a phone in daylight and print clean.
BG = "#FFFFFF"      # page
PANEL = "#F2F7FC"   # callout panels, a hair off-white so edges show
LINE = "#D4E3F2"    # hairlines
CYAN = "#0E9CFE"    # brand accent, exact from the wordmark
GOLD = "#0A6FC2"    # secondary accent (was gold; gold dies on white)
GREEN = "#12A47A"   # success/positive
CREAM = "#001954"   # PRIMARY TEXT — brand navy, not cream
MUTED = "#5B7392"   # secondary text

W, H = landscape(A4)
HERE = os.path.dirname(os.path.abspath(__file__))
MARK = os.path.join(HERE, "brand", "rav-mark.png")
# The AIWithRav wordmark, cropped from the channel banner. On a white ground
# the full lockup reads better than the bare mark, so it is the default.
LOCKUP = os.path.join(HERE, "brand", "aiwithrav-wordmark.png")
if not os.path.exists(LOCKUP):
    LOCKUP = os.path.join(HERE, "brand", "rav-lockup.png")


def st(name, **kw):
    base = dict(fontName="Helvetica", fontSize=13, leading=18, textColor=CREAM)
    base.update(kw)
    return ParagraphStyle(name, **base)


def md(text):
    """**bold** -> cyan bold. The emphasis colour is the brand colour."""
    text = re.sub(r"\*\*(.+?)\*\*", rf'<b><font color="{CYAN}">\1</font></b>', text)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    return text


def parse(path):
    raw = open(path, encoding="utf-8").read()
    meta, body = {}, raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
        for line in fm.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta, body.strip()


def ground(c):
    c.setFillColor(BG)
    c.rect(0, 0, W, H, stroke=0, fill=1)


def brand_bar(c, topic, number):
    """A thin strip, not a header. It must not compete with the hook."""
    if os.path.exists(LOCKUP):
        try:
            img = ImageReader(LOCKUP)
            iw, ih = img.getSize()
            lh = 5.4 * mm
            c.drawImage(img, 14 * mm, H - 10.6 * mm, width=lh * iw / ih,
                        height=lh, mask="auto")
        except Exception:
            c.setFillColor(CREAM); c.setFont("Helvetica-Bold", 8.5)
            c.drawString(14 * mm, H - 9 * mm, "AIWithRav")
    else:
        c.setFillColor(CREAM)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(14 * mm, H - 9 * mm, "AIWithRav")
    c.setFillColor(CYAN)
    c.drawRightString(W - 14 * mm, H - 9 * mm, f"{topic.upper()}  ·  #{number}")
    c.setStrokeColor(LINE)
    c.setLineWidth(0.9)
    c.line(14 * mm, H - 12 * mm, W - 14 * mm, H - 12 * mm)


def footer(c, page):
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 7.5)
    c.drawString(14 * mm, 7 * mm, "Let's Make AI Simple")
    c.drawRightString(W - 14 * mm, 7 * mm, f"{page}/2")


def page_hook(c, meta, hook, image_path, caption):
    """PAGE 1 — the hook owns the top third, the diagram fills the rest."""
    ground(c)
    brand_bar(c, meta.get("topic", ""), meta.get("short", "1"))

    # THE HOOK. Big enough to read while the thumb is still moving.
    hs = st("hook", fontName="Helvetica-Bold", fontSize=34, leading=40,
            textColor=CREAM, alignment=1)
    p = Paragraph(md(hook), hs)
    hw, hh = p.wrap(W - 40 * mm, 60 * mm)
    hook_top = H - 20 * mm
    p.drawOn(c, 20 * mm, hook_top - hh)

    # A short gold rule under the hook, as a beat before the diagram.
    c.setStrokeColor(GOLD)
    c.setLineWidth(3)
    c.line(W / 2 - 16 * mm, hook_top - hh - 6 * mm,
           W / 2 + 16 * mm, hook_top - hh - 6 * mm)

    top = hook_top - hh - 12 * mm
    bottom = 16 * mm
    box_w, box_h = W - 24 * mm, top - bottom

    if image_path and os.path.exists(image_path):
        img = ImageReader(image_path)
        iw, ih = img.getSize()
        scale = min(box_w / iw, box_h / ih)
        dw, dh = iw * scale, ih * scale
        c.drawImage(img, (W - dw) / 2, bottom + (box_h - dh) / 2,
                    width=dw, height=dh, mask="auto")

    footer(c, 1)
    c.showPage()


def page_beats(c, meta, beats, takeaway):
    """PAGE 2 — three beats, then the line they keep."""
    ground(c)
    brand_bar(c, meta.get("topic", ""), meta.get("short", "1"))

    y = H - 26 * mm
    bs = st("b", fontSize=16, leading=22, textColor=CREAM)

    for i, beat in enumerate(beats[:3], 1):
        # Large numeral, used as a visual anchor rather than a bullet.
        c.setFillColor(CYAN)
        c.setFont("Helvetica-Bold", 30)
        c.drawString(16 * mm, y - 9 * mm, str(i))

        p = Paragraph(md(beat), bs)
        pw, ph = p.wrap(W - 46 * mm, 60 * mm)
        p.drawOn(c, 32 * mm, y - ph)
        y -= max(ph, 12 * mm) + 11 * mm

    if takeaway:
        box_top = max(y, 42 * mm)
        ts = st("k", fontName="Helvetica-Bold", fontSize=18, leading=24,
                textColor=GOLD)
        p = Paragraph(md(takeaway), ts)
        kw_, kh = p.wrap(W - 50 * mm, 60 * mm)
        bh = kh + 16 * mm
        c.setFillColor(PANEL)
        c.roundRect(14 * mm, box_top - bh, W - 28 * mm, bh, 3 * mm, stroke=0, fill=1)
        c.setFillColor(GOLD)
        c.rect(14 * mm, box_top - bh, 2.6 * mm, bh, stroke=0, fill=1)
        c.setFillColor(MUTED)
        c.setFont("Helvetica-Bold", 8.5)
        c.drawString(22 * mm, box_top - 8 * mm, "REMEMBER THIS")
        p.drawOn(c, 22 * mm, box_top - bh + 7 * mm)

    footer(c, 2)
    c.showPage()


def build(src_path):
    meta, body = parse(src_path)
    topic_dir = os.path.dirname(os.path.dirname(os.path.abspath(src_path)))

    hook, beats, takeaway, image, caption = "", [], "", None, ""
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("@hook|"):
            hook = line.split("|", 1)[1]
        elif line.startswith("@beat|"):
            beats.append(line.split("|", 1)[1])
        elif line.startswith("@takeaway|"):
            takeaway = line.split("|", 1)[1]
        elif line.startswith("@image|"):
            parts = line.split("|")
            image = os.path.join(topic_dir, parts[1])
            caption = parts[2] if len(parts) > 2 else ""

    slug = re.sub(r"[^a-z0-9]+", "-", meta.get("title", "short").lower()).strip("-")[:44]
    out = os.path.join(topic_dir, f"AI-With-Rav_Short-{meta.get('short','1')}_{slug}.pdf")

    c = pdfcanvas.Canvas(out, pagesize=landscape(A4))
    c.setTitle(f"{meta.get('topic','')} — {meta.get('title','')}")
    page_hook(c, meta, hook, image, caption)
    page_beats(c, meta, beats, takeaway)
    c.save()
    print("BUILT:", out)
    return out


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "topics/02-machine-learning/shorts/s01.md")
