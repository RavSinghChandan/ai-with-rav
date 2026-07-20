#!/usr/bin/env python3
"""
Master branded PDF generator for 'AI with Rav — ML in 30 Days'.
Generates ONE top-quality dark PDF per day, directly (no md/html pipeline).
Branding: designed 'AI with Rav' logo + Rav's photo (circular) + saffron/teal theme.
Usage: python3 build_master_pdf.py  (Day 1 built in)
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Image, Table, TableStyle, HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from PIL import Image as PImage, ImageDraw
import os

# ---- palette ----
BG   = HexColor('#0d1117')
CARD = HexColor('#161b22')
FG   = HexColor('#e6edf3')
MUT  = HexColor('#9fb3c8')
SAF  = HexColor('#FF6B35')
TEAL = HexColor('#33B5E5')
GRN  = HexColor('#06D6A0')
YEL  = HexColor('#FFD166')
LINE = HexColor('#21262d')

W, H = A4

# ---- make a circular version of the photo ----
def circle_crop(src, dst, size=520):
    im = PImage.open(src).convert('RGBA')
    s = min(im.size); im = im.crop(((im.width-s)//2,(im.height-s)//2,(im.width+s)//2,(im.height+s)//2)).resize((size,size))
    mask = PImage.new('L',(size,size),0); ImageDraw.Draw(mask).ellipse((0,0,size,size),fill=255)
    out = PImage.new('RGBA',(size,size),(0,0,0,0)); out.paste(im,(0,0),mask); out.save(dst)
circle_crop('brand/rav-photo.jpg','brand/rav-circle.png')

# ---- styles ----
def st(name,**kw):
    base=dict(fontName='Helvetica',fontSize=11,leading=16,textColor=FG,spaceAfter=6)
    base.update(kw); return ParagraphStyle(name,**base)
H1   = st('H1',fontName='Helvetica-Bold',fontSize=22,leading=26,textColor=SAF,spaceAfter=4)
H2   = st('H2',fontName='Helvetica-Bold',fontSize=15,leading=19,textColor=TEAL,spaceBefore=14,spaceAfter=6)
BODY = st('BODY',fontSize=11.5,leading=17)
BULL = st('BULL',fontSize=11.5,leading=17,leftIndent=14,bulletIndent=2)
NOTE = st('NOTE',fontSize=11.5,leading=17,textColor=FG)
CODE = st('CODE',fontName='Courier',fontSize=9.5,leading=13,textColor=HexColor('#e6edf3'))
CAP  = st('CAP',fontSize=9.5,leading=13,textColor=MUT,alignment=TA_CENTER)

def hex_b(t): return f'<b><font color="#FFD166">{t}</font></b>'
def teal(t):  return f'<font color="#33B5E5">{t}</font>'

# ---- page background + footer (every page) ----
def page_bg(cnv, doc, footer=True):
    cnv.setFillColor(BG); cnv.rect(0,0,W,H,fill=1,stroke=0)
    if not footer: return
    # footer — brand name only, NO links
    cnv.setFillColor(MUT); cnv.setFont('Helvetica',8)
    cnv.drawString(16*mm, 10*mm, 'AI with Rav  ·  Machine Learning in 30 Days')
    cnv.drawRightString(W-16*mm, 10*mm, f'Day 1')
    cnv.setStrokeColor(LINE); cnv.setLineWidth(0.5); cnv.line(16*mm,13*mm,W-16*mm,13*mm)

# ---- callout box flowable ----
def callout(text, accent):
    p = Paragraph(text, NOTE)
    t = Table([[p]], colWidths=[W-32*mm-10*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1),CARD),
        ('LINEBEFORE',(0,0),(0,-1),3,accent),
        ('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),
    ]))
    return t

def codeblock(lines):
    p = Paragraph('<br/>'.join(l.replace(' ','&nbsp;') for l in lines), CODE)
    t = Table([[p]], colWidths=[W-32*mm-8*mm])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),HexColor('#0b0e13')),
        ('BOX',(0,0),(-1,-1),0.5,LINE),
        ('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)]))
    return t

# ---- COVER ----
def draw_cover(cnv, doc):
    page_bg(cnv, doc, footer=False)
    cx = W/2
    # SMALL logo, top-centered (real logo if present, else small text mark)
    logo='brand/ai-for-business-logo.png'
    if os.path.exists(logo):
        from PIL import Image as _PI; lr=_PI.open(logo); rat=lr.height/lr.width
        lw=34*mm; lh=lw*rat
        cnv.drawImage(logo, cx-lw/2, H-24*mm-lh, lw, lh, mask='auto', preserveAspectRatio=True)
        logo_bottom = H-24*mm-lh
    else:
        cnv.setFillColor(SAF); cnv.roundRect(cx-11*mm, H-30*mm, 22*mm, 22*mm, 5*mm, fill=1, stroke=0)
        cnv.setFillColor(BG); cnv.setFont('Helvetica-Bold', 20); cnv.drawCentredString(cx, H-23*mm, 'AI')
        cnv.setFillColor(FG); cnv.setFont('Helvetica-Bold', 15); cnv.drawCentredString(cx, H-40*mm, 'AI with Rav')
        logo_bottom = H-44*mm
    # photo circle — clear, face fully visible
    py = logo_bottom - 12*mm
    cnv.drawImage('brand/rav-circle.png', cx-30*mm, py-60*mm, 60*mm, 60*mm, mask='auto')
    cnv.setStrokeColor(SAF); cnv.setLineWidth(2.5); cnv.circle(cx, py-30*mm, 30*mm, stroke=1, fill=0)
    # title
    ty = py-60*mm - 20*mm
    cnv.setFillColor(SAF); cnv.setFont('Helvetica-Bold', 32); cnv.drawCentredString(cx, ty, 'MACHINE LEARNING')
    cnv.setFillColor(FG); cnv.setFont('Helvetica-Bold', 21); cnv.drawCentredString(cx, ty-13*mm, 'in 30 Days')
    # day badge
    by = ty-30*mm
    cnv.setFillColor(TEAL); cnv.roundRect(cx-34*mm, by-9*mm, 68*mm, 15*mm, 7.5*mm, fill=1, stroke=0)
    cnv.setFillColor(BG); cnv.setFont('Helvetica-Bold', 14); cnv.drawCentredString(cx, by-4*mm, 'DAY 1  ·  VIDEO 1')
    cnv.setFillColor(MUT); cnv.setFont('Helvetica', 13); cnv.drawCentredString(cx, by-22*mm, 'What is Machine Learning, really?')

# ---- build document ----
def build(out='AI-with-Rav_Day-01_Machine-Learning.pdf'):
    doc = BaseDocTemplate(out, pagesize=A4,
        leftMargin=16*mm, rightMargin=16*mm, topMargin=18*mm, bottomMargin=18*mm)
    frame = Frame(16*mm, 16*mm, W-32*mm, H-34*mm, id='main')
    doc.addPageTemplates([
        PageTemplate(id='cover', frames=[frame], onPage=draw_cover),
        PageTemplate(id='body',  frames=[frame], onPage=page_bg),
    ])
    S=[]
    from reportlab.platypus import NextPageTemplate, PageBreak
    # cover page: a tiny invisible spacer holds the first (cover) page; then switch to body
    S += [Spacer(1,1), NextPageTemplate('body'), PageBreak()]

    def h1(t): S.append(Paragraph(t,H1))
    def h2(t): S.append(Paragraph(t,H2)); S.append(HRFlowable(width='100%',thickness=0.5,color=LINE,spaceAfter=6))
    def p(t):  S.append(Paragraph(t,BODY))
    def bullets(items):
        for it in items: S.append(Paragraph('•&nbsp; '+it, BULL))
        S.append(Spacer(1,4))
    def img(path,cap=None,w=W-40*mm):
        ir=PImage.open(path); ratio=ir.height/ir.width
        S.append(Spacer(1,6)); S.append(Image(path,width=w,height=w*ratio))
        if cap: S.append(Spacer(1,3)); S.append(Paragraph(cap,CAP))
        S.append(Spacer(1,8))
    def gap(h=6): S.append(Spacer(1,h))

    h1('What is Machine Learning, <i>really?</i>')
    S.append(callout(f'{hex_b("In One Line:")} Machine Learning is teaching a computer to learn patterns from examples — instead of you writing the rules by hand.', YEL)); gap(10)

    h2('Start here: the chai stall')
    p(f'Picture {hex_b("Ramesh")}, who runs a chai stall outside a Mumbai station.')
    p('Nobody gave Ramesh a rulebook. But after 3 years, he <i>just knows:</i>')
    chai_no = "nimbu paani sells, chai doesn't"
    bullets([f'Rainy evening + train delayed → {hex_b("sell more chai, keep extra ginger")}',
             f'Hot afternoon → {hex_b(chai_no)}',
             f'Salary day (1st) → {hex_b("everyone buys, stock up")}'])
    p(f'Ramesh was never <i>programmed</i>. He {hex_b("learned from thousands of days of examples.")}')
    S.append(callout(f'{hex_b("That is Machine Learning.")} A machine, like Ramesh, looking at thousands of past examples and figuring out the pattern {hex_b("by itself")} — so it can predict the future.', GRN)); gap(10)

    h2('The big shift: old way vs ML way')
    p('This one picture is the entire reason ML exists:')
    img('images/01-traditional-vs-ml.png','In normal coding YOU write the rules. In ML you give examples and the machine writes the rules itself.')
    S.append(callout(f'{hex_b("The intuition:")} In normal coding, <i>you</i> are the smart one — you write every rule. In ML, you let the {hex_b("machine become smart")} by showing it examples.', GRN)); gap(6)
    p(f'{hex_b("Why this is revolutionary:")} some problems have too many rules to ever write by hand. How would you write if-else rules to spot a cat in a photo? Impossible. But show a machine 10,000 cat photos and it learns "cat-ness" on its own.')

    h2('How learning actually happens')
    img('images/02-how-learning-happens.png','Data → Training → Model → Prediction. The "model" is just the pattern it learned.')

    h2('You already use ML 20 times a day')
    data=[['When you…','ML is quietly working'],
          ['Open YouTube → perfect next video','Learned your watch history'],
          ['GPay/PhonePe flags a fraud txn','Learned what fraud looks like'],
          ['Instagram reels know you too well','Learned your scroll patterns'],
          ['Gmail auto-sorts spam','Learned from billions of emails']]
    t=Table(data,colWidths=[(W-40*mm)*0.5]*2)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),TEAL),('TEXTCOLOR',(0,0),(-1,0),BG),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,-1),10),
        ('TEXTCOLOR',(0,1),(-1,-1),FG),('BACKGROUND',(0,1),(-1,-1),CARD),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[CARD,HexColor('#11151b')]),
        ('GRID',(0,0),(-1,-1),0.5,LINE),('LEFTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    S.append(t); gap(10)

    h2('The Math  (technical — skip if non-technical, you lose nothing)')
    p('Every ML model learns a <b>function</b> f that maps input X to output y:')
    S.append(codeblock(['        y  =  f(X)','',
        '   X = the inputs   (weather, time, crowd)  -> "features"',
        '   y = the answer   (cups of chai sold)      -> "label"',
        '   f = the pattern  (what the machine learns)-> the "model"']))
    p(f'Training = adjusting f to shrink the gap between its guess and the truth. That gap is the {hex_b("loss")}. All of training is: "make the loss smaller."'); gap(6)

    h2("Try it — your first model in 6 lines")
    S.append(codeblock([
        'from sklearn.linear_model import LinearRegression','',
        'X = [[15],[20],[25],[30],[35]]   # temperature',
        'y = [200,170,140,110,80]         # cups sold','',
        'model = LinearRegression()',
        'model.fit(X, y)                  # <- THIS is learning','',
        'print(model.predict([[18]]))     # 18C -> ~182 cups']))
    img('images/03-chai-regression.png','Orange dots = data. Blue line = what the model learned. Green star = a new prediction.')
    S.append(callout(f'{hex_b("model.fit(X, y)")} is the entire heart of Machine Learning. Everything in the next 29 days is a more powerful version of it.', YEL)); gap(10)

    h2('Recap — the 20-second version')
    bullets(['ML = learning patterns from examples, not writing rules by hand.',
             'Old way: you write rules. ML way: the machine finds the rules.',
             'The learned pattern is called a model (y = f(X)).',
             'You already use it 20× a day — YouTube, GPay, Instagram.',
             'Training = making wrong guesses less wrong (shrinking the loss).'])
    S.append(callout(f'{teal("Next up — Video 2:")} The 3 Families of ML: Supervised, Unsupervised, Reinforcement. Just like a child learns 3 ways — see you Day 2.', TEAL))

    doc.build(S)
    print('MASTER PDF built:', out)

build()
