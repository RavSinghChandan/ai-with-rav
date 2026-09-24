"""
SHORTS TEMPLATE — AI With Rav.

A two-page PDF built for a sub-3-minute reel, not a 12-minute lesson:

    page 1  ONE diagram, full bleed, nothing else competing with it
    page 2  the words — hook, three beats, one takeaway

Why light, not the dark premium deck: a reel is judged in the first second on a
phone. Dark frames lose contrast on a small bright screen, and "premium" is not
what a viewer is deciding — they are deciding whether this is instantly clear.

Brand colours are sampled from the logo itself (brand/rav-mark.png):
    cyan   #00B8FC   the < > brackets
    gold   #F6BB63   the halo
    navy   #2F4C79   the wordmark

The 30-day factory (build_master_pdf.py) is untouched. Both live side by side.

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

# ── brand ──────────────────────────────────────────────────────────────────
CYAN = "#00B8FC"
GOLD = "#F6BB63"
NAVY = "#14213D"
INK = "#1B2A41"
MUTED = "#5B6B82"
PAPER = "#FFFFFF"
TINT = "#F2F8FD"          # very light cyan wash
LINE = "#DCE7F1"

W, H = landscape(A4)
HERE = os.path.dirname(os.path.abspath(__file__))
MARK = os.path.join(HERE, "brand", "rav-mark.png")
LOCKUP = os.path.join(HERE, "brand", "rav-lockup.png")


def st(name, **kw):
    base = dict(fontName="Helvetica", fontSize=11, leading=15, textColor=INK)
    base.update(kw)
    return ParagraphStyle(name, **base)


def md(text):
    """**bold** -> cyan bold, *italic* -> italic."""
    text = re.sub(r"\*\*(.+?)\*\*", rf'<b><font color="{CYAN}">\1</font></b>', text)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", text)
    return text


def parse(path):
    """Front matter + body, same simple format as the 30-day files."""
    raw = open(path, encoding="utf-8").read()
    meta, body = {}, raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
        for line in fm.strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
    return meta, body.strip()


def draw_header(c, topic, number):
    """Thin brand strip: lockup left, topic right."""
    c.setFillColor(TINT)
    c.rect(0, H - 22 * mm, W, 22 * mm, stroke=0, fill=1)
    c.setStrokeColor(CYAN)
    c.setLineWidth(1.6)
    c.line(0, H - 22 * mm, W, H - 22 * mm)

    if os.path.exists(LOCKUP):
        img = ImageReader(LOCKUP)
        iw, ih = img.getSize()
        h = 11 * mm
        c.drawImage(img, 14 * mm, H - 17.5 * mm, width=h * iw / ih, height=h,
                    mask="auto")

    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(W - 14 * mm, H - 12.5 * mm, topic.upper())
    c.setFillColor(CYAN)
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(W - 14 * mm, H - 17.5 * mm, f"SHORT #{number}")


def draw_footer(c, page, total=2):
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    c.line(14 * mm, 14 * mm, W - 14 * mm, 14 * mm)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(14 * mm, 9.5 * mm, "AI With Rav  ·  Let's Make AI Simple")
    c.drawRightString(W - 14 * mm, 9.5 * mm, f"{page}/{total}")


def page_diagram(c, meta, image_path, caption):
    """PAGE 1 — the diagram, as large as it will go. Nothing competes."""
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    draw_header(c, meta.get("topic", ""), meta.get("short", "1"))

    title = meta.get("title", "")
    ts = st("t", fontName="Helvetica-Bold", fontSize=22, leading=26, textColor=NAVY)
    p = Paragraph(md(title), ts)
    tw, th = p.wrap(W - 34 * mm, 40 * mm)
    p.drawOn(c, 17 * mm, H - 33 * mm - th)

    top = H - 37 * mm - th
    bottom = 24 * mm
    box_w, box_h = W - 28 * mm, top - bottom

    if image_path and os.path.exists(image_path):
        img = ImageReader(image_path)
        iw, ih = img.getSize()
        # Fill the frame: a reel viewer sees the diagram, not the margins.
        scale = min(box_w / iw, box_h / ih)
        dw, dh = iw * scale, ih * scale
        # Sit just under the title rather than floating in the middle of a
        # box that is taller than the image.
        c.drawImage(img, (W - dw) / 2, top - dh - 4 * mm,
                    width=dw, height=dh, mask="auto")
    else:
        c.setFillColor(TINT)
        c.roundRect(14 * mm, bottom, box_w, box_h, 6 * mm, stroke=0, fill=1)

    if caption:
        c.setFillColor(MUTED)
        c.setFont("Helvetica-Oblique", 9.5)
        c.drawCentredString(W / 2, 18 * mm, caption[:110])

    draw_footer(c, 1)
    c.showPage()


def page_text(c, meta, hook, beats, takeaway):
    """PAGE 2 — the words, sized to be read from a phone."""
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    draw_header(c, meta.get("topic", ""), meta.get("short", "1"))

    y = H - 34 * mm

    # Hook — the single line that has to land in the first second.
    c.setFillColor(TINT)
    c.roundRect(14 * mm, y - 24 * mm, W - 28 * mm, 24 * mm, 4 * mm, stroke=0, fill=1)
    c.setFillColor(GOLD)
    c.rect(14 * mm, y - 24 * mm, 2.4 * mm, 24 * mm, stroke=0, fill=1)
    hs = st("h", fontName="Helvetica-Bold", fontSize=15, leading=20, textColor=NAVY)
    p = Paragraph(md(hook), hs)
    hw, hh = p.wrap(W - 44 * mm, 24 * mm)
    p.drawOn(c, 21 * mm, y - 12 * mm - hh / 2)
    y -= 30 * mm

    # Three beats, numbered.
    bs = st("b", fontSize=12.5, leading=17)
    for i, beat in enumerate(beats[:3], 1):
        c.setFillColor(CYAN)
        c.circle(19 * mm, y - 2.6 * mm, 3.6 * mm, stroke=0, fill=1)
        c.setFillColor(PAPER)
        c.setFont("Helvetica-Bold", 9)
        c.drawCentredString(19 * mm, y - 4.2 * mm, str(i))

        p = Paragraph(md(beat), bs)
        pw, ph = p.wrap(W - 44 * mm, 60 * mm)
        p.drawOn(c, 27 * mm, y - ph + 2 * mm)
        y -= ph + 8 * mm

    # Takeaway.
    if takeaway:
        y -= 2 * mm
        ts2 = st("k", fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=NAVY)
        p = Paragraph(md(takeaway), ts2)
        kw_, kh = p.wrap(W - 46 * mm, 60 * mm)
        box_h = kh + 17 * mm                      # label + text + padding
        c.setFillColor("#FEF7EA")
        c.roundRect(14 * mm, y - box_h, W - 28 * mm, box_h, 4 * mm, stroke=0, fill=1)
        c.setFillColor(GOLD)
        c.rect(14 * mm, y - box_h, 2.4 * mm, box_h, stroke=0, fill=1)
        c.setFillColor(MUTED)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(21 * mm, y - 7.5 * mm, "REMEMBER")
        p.drawOn(c, 21 * mm, y - box_h + 6 * mm)

    # Watermark mark, bottom right, faint.
    if os.path.exists(MARK):
        c.saveState()
        c.setFillAlpha(0.06)
        img = ImageReader(MARK)
        iw, ih = img.getSize()
        h = 42 * mm
        c.drawImage(img, W - h * iw / ih - 12 * mm, 18 * mm,
                    width=h * iw / ih, height=h, mask="auto")
        c.restoreState()

    draw_footer(c, 2)
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
    page_diagram(c, meta, image, caption)
    page_text(c, meta, hook, beats, takeaway)
    c.save()
    print("BUILT:", out)
    return out


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "topics/02-machine-learning/shorts/s01.md")
