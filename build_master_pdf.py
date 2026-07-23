#!/usr/bin/env python3
"""
FACTORY TEMPLATE — AI with Rav · ML in 30 Days.
Design is FROZEN here. Content comes from days/dayNN.md.
Usage:  python3 build_master_pdf.py days/day02.md
Output: AI-with-Rav_Day-02_<slug>.pdf   (identical style, new content)
"""
import sys, os, re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, Image, Table, TableStyle, HRFlowable, NextPageTemplate, PageBreak)
from reportlab.lib.styles import ParagraphStyle
from PIL import Image as PImage, ImageDraw

# ===== FROZEN BRAND (never changes) — WARM CHARCOAL-BROWN PREMIUM =====
BG=HexColor('#1a1512'); CARD=HexColor('#241d18'); FG=HexColor('#f0e6d8'); MUT=HexColor('#b3a595')
SAF=HexColor('#FF7A3D'); TEAL=HexColor('#4EC5E8'); GRN=HexColor('#3dd4a8'); YEL=HexColor('#FFCF6B'); LINE=HexColor('#3a2f26')
GOLD=HexColor('#E0B265')
ACCENT={'yellow':YEL,'green':GRN,'teal':TEAL,'saffron':SAF}
W,H=A4
LOGO='brand/ai-for-business-logo.png'; PHOTO='brand/rav-photo.jpg'; CIRCLE='brand/rav-circle.png'; WMARK='brand/logo-watermark.png'

def circle_crop(src,dst,size=680,fcx=0.55,top_frac=0.06,frac=0.52):
    im=PImage.open(src).convert('RGBA'); w,h=im.size; side=int(h*frac); cx=int(w*fcx)
    left=min(max(0,cx-side//2),w-side); top=min(max(0,int(h*top_frac)),h-side)
    im2=im.crop((left,top,left+side,top+side)).resize((size,size))
    m=PImage.new('L',(size,size),0); ImageDraw.Draw(m).ellipse((0,0,size,size),fill=255)
    out=PImage.new('RGBA',(size,size),(0,0,0,0)); out.paste(im2,(0,0),m); out.save(dst)

def st(n,**k):
    b=dict(fontName='Helvetica',fontSize=11.5,leading=17,textColor=FG,spaceAfter=6); b.update(k); return ParagraphStyle(n,**b)
H1=st('H1',fontName='Helvetica-Bold',fontSize=22,leading=26,textColor=SAF,spaceAfter=4)
H2=st('H2',fontName='Helvetica-Bold',fontSize=15,leading=19,textColor=GOLD,spaceBefore=14,spaceAfter=6)
BODY=st('BODY'); BULL=st('BULL',leftIndent=14,bulletIndent=2)
NOTE=st('NOTE'); CODE=st('CODE',fontName='Courier',fontSize=9.5,leading=13); CAP=st('CAP',fontSize=9.5,leading=13,textColor=MUT,alignment=1)

def md(t):  # inline **bold**->yellow, *italic*
    t=re.sub(r'\*\*(.+?)\*\*',r'<b><font color="#FFD166">\1</font></b>',t)
    t=re.sub(r'\*(.+?)\*',r'<i>\1</i>',t); return t

def callout(text,accent):
    p=Paragraph(md(text),NOTE); t=Table([[p]],colWidths=[W-32*mm-10*mm])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),CARD),('LINEBEFORE',(0,0),(0,-1),3,accent),
        ('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9)])); return t
def codeblock(lines):
    p=Paragraph('<br/>'.join(l.replace(' ','&nbsp;') for l in lines),CODE)
    t=Table([[p]],colWidths=[W-32*mm-8*mm])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),HexColor('#140f0c')),('BOX',(0,0),(-1,-1),0.5,LINE),
        ('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)])); return t

DAY=1; VIDEO=1; TITLE=''; SUBTITLE=''; TOPIC='MACHINE LEARNING'; LEARN=[]; BASEDIR='.'

def _brand_watermark(cnv):
    # faint centered logo watermark on every page
    if os.path.exists(WMARK):
        wr=PImage.open(WMARK); rat=wr.height/wr.width; ww=110*mm; wh=ww*rat
        cnv.drawImage(WMARK, W/2-ww/2, H/2-wh/2, ww, wh, mask='auto', preserveAspectRatio=True)

def _corner_photo(cnv):
    # small circular photo tucked into the FOOTER band (below the content frame,
    # aligned with the footer text) so it NEVER overlaps body text.
    if os.path.exists(CIRCLE):
        d=11*mm
        y=7.5*mm            # centred on the footer line (~10mm), fully below the 16mm frame
        cnv.drawImage(CIRCLE, W-16*mm-d, y, d, d, mask='auto')
        cnv.setStrokeColor(GOLD); cnv.setLineWidth(1.1); cnv.circle(W-16*mm-d/2, y+d/2, d/2, stroke=1, fill=0)

def page_bg(cnv,doc,footer=True):
    cnv.setFillColor(BG); cnv.rect(0,0,W,H,fill=1,stroke=0)
    _brand_watermark(cnv)
    if not footer: return
    _corner_photo(cnv)
    cnv.setFillColor(MUT); cnv.setFont('Helvetica',8)
    cnv.drawString(16*mm,10*mm,f'AI with Rav  ·  {TOPIC.title()} in 30 Days')
    cnv.drawRightString(W-16*mm-18*mm,10*mm,f'Day {DAY}')
    cnv.setStrokeColor(LINE); cnv.setLineWidth(0.5); cnv.line(16*mm,13*mm,W-34*mm,13*mm)

def draw_cover(cnv,doc):
    cnv.setFillColor(BG); cnv.rect(0,0,W,H,fill=1,stroke=0)
    _brand_watermark(cnv)
    cx=W/2
    # --- top brand strip: small logo card + name (left) , small photo (right) ---
    if os.path.exists(LOGO):
        lr=PImage.open(LOGO); rat=lr.height/lr.width; lw=20*mm; lh=lw*rat
        cnv.setFillColor(HexColor('#ffffff')); cnv.roundRect(18*mm, H-20*mm-lh-4*mm, lw+6*mm, lh+8*mm, 4*mm, fill=1, stroke=0)
        cnv.drawImage(LOGO, 21*mm, H-20*mm-lh, lw, lh, mask='auto', preserveAspectRatio=True)
    cnv.setFillColor(FG); cnv.setFont('Helvetica-Bold',15); cnv.drawString(48*mm, H-28*mm, 'AI with Rav')
    cnv.setFillColor(GOLD); cnv.setFont('Helvetica',9.5); cnv.drawString(48*mm, H-33*mm, 'Learn AI the way you actually think.')
    if os.path.exists(CIRCLE):
        d=22*mm; cnv.drawImage(CIRCLE, W-18*mm-d, H-20*mm-d, d, d, mask='auto')
        cnv.setStrokeColor(SAF); cnv.setLineWidth(1.6); cnv.circle(W-18*mm-d/2, H-20*mm-d/2, d/2, stroke=1, fill=0)
    # --- DAY badge ---
    by=H-58*mm
    cnv.setFillColor(GOLD); cnv.roundRect(18*mm, by, 52*mm, 12*mm, 6*mm, fill=1, stroke=0)
    cnv.setFillColor(BG); cnv.setFont('Helvetica-Bold',12); cnv.drawCentredString(18*mm+26*mm, by+3.6*mm, f'DAY {DAY}  of 30')
    # progress dots
    for k in range(1,31):
        fx=76*mm+((k-1)%15)*8.0*mm/1.0*0  # keep simple: skip dot row (avoid clutter)
    # --- BIG topic title (the hero) ---
    cnv.setFillColor(SAF); cnv.setFont('Helvetica-Bold',30); cnv.drawString(18*mm, by-16*mm, TOPIC.upper())
    # the day's specific title, wrapped
    from reportlab.lib.utils import simpleSplit
    cnv.setFillColor(FG); cnv.setFont('Helvetica-Bold',19)
    lines=simpleSplit(TITLE, 'Helvetica-Bold', 19, W-36*mm)
    yy=by-28*mm
    for ln in lines[:3]:
        cnv.drawString(18*mm, yy, ln); yy-=8.5*mm
    # --- "What you'll learn" box ---
    box_y=yy-8*mm
    items=LEARN[:5] if LEARN else []
    if items:
        bh=14*mm+len(items)*8*mm
        cnv.setFillColor(CARD); cnv.roundRect(18*mm, box_y-bh, W-36*mm, bh, 5*mm, fill=1, stroke=0)
        cnv.setStrokeColor(TEAL); cnv.setLineWidth(2); cnv.line(18*mm, box_y-8*mm, 18*mm, box_y-bh+4*mm)
        cnv.setFillColor(TEAL); cnv.setFont('Helvetica-Bold',13); cnv.drawString(25*mm, box_y-9*mm, "WHAT YOU'LL LEARN TODAY")
        cnv.setFillColor(FG); cnv.setFont('Helvetica',12)
        ly=box_y-18*mm
        for it in items:
            cnv.setFillColor(SAF); cnv.drawString(25*mm, ly, '›')
            cnv.setFillColor(FG); cnv.drawString(30*mm, ly, it); ly-=8*mm
    # footer brand line
    cnv.setFillColor(MUT); cnv.setFont('Helvetica',9)
    cnv.drawCentredString(cx, 16*mm, 'youtube.com/@aiwithrav  ·  A premium AI learning series')

# ===== CONTENT PARSER (the only thing that varies per day) =====
def parse(path):
    raw=open(path).read()
    meta={}; body=raw
    m=re.match(r'---\n(.*?)\n---\n(.*)',raw,re.S)
    if m:
        for line in m.group(1).splitlines():
            if ':' in line: k,v=line.split(':',1); meta[k.strip()]=v.strip()
        body=m.group(2)
    return meta, body.strip()

def build_flowables(body):
    S=[Spacer(1,1), NextPageTemplate('body'), PageBreak()]
    S.append(Paragraph(md(TITLE.replace('really?','<i>really?</i>')),H1))
    lines=body.splitlines(); i=0
    def para(t): S.append(Paragraph(md(t),BODY))
    while i<len(lines):
        ln=lines[i].rstrip()
        if ln.startswith('@callout|'):
            _,acc,txt=ln.split('|',2); S.append(callout(txt,ACCENT.get(acc,YEL))); S.append(Spacer(1,4))
        elif ln.startswith('@h2|'):
            S.append(Paragraph(md(ln[4:]),H2)); S.append(HRFlowable(width='100%',thickness=0.5,color=LINE,spaceAfter=6))
        elif ln.startswith('@image|'):
            parts=ln.split('|'); path=parts[1]; cap=parts[2] if len(parts)>2 else None
            # resolve image relative to the content file's folder, then repo root as fallback
            cand=[os.path.join(BASEDIR,path), path]
            real=next((c for c in cand if os.path.exists(c)), None)
            if real:
                ir=PImage.open(real); r=ir.height/ir.width; w=W-40*mm
                S.append(Spacer(1,6)); S.append(Image(real,width=w,height=w*r))
                if cap: S.append(Spacer(1,3)); S.append(Paragraph(cap,CAP))
                S.append(Spacer(1,8))
            else:
                # LOUD failure instead of silent skip — so a missing diagram is never invisible
                print(f"  !! IMAGE NOT FOUND: {path}  (looked in {BASEDIR} and repo root)")
        elif ln=='@bullets':
            i+=1
            # auto-close on @end OR when the next @directive starts (forgiving if @end is missing)
            while i<len(lines) and lines[i].rstrip()!='@end' and not lines[i].lstrip().startswith('@'):
                if lines[i].strip(): S.append(Paragraph('•&nbsp; '+md(lines[i].strip()),BULL))
                i+=1
            if i<len(lines) and lines[i].lstrip().startswith('@') and lines[i].rstrip()!='@end':
                i-=1   # step back so the next directive is processed normally
            S.append(Spacer(1,4))
        elif ln=='@code':
            i+=1; buf=[]
            while i<len(lines) and lines[i].rstrip()!='@end': buf.append(lines[i]); i+=1
            S.append(codeblock(buf)); S.append(Spacer(1,6))
        elif ln=='@table':
            i+=1; rows=[]
            while i<len(lines) and lines[i].rstrip()!='@end':
                if lines[i].strip(): rows.append([c.strip() for c in lines[i].split('|')])
                i+=1
            data=[[Paragraph(md(c),st('c',fontSize=10,textColor=(BG if r==0 else FG))) for c in row] for r,row in enumerate(rows)]
            t=Table(data,colWidths=[(W-40*mm)/len(rows[0])]*len(rows[0]))
            t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),TEAL),('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
                ('BACKGROUND',(0,1),(-1,-1),CARD),('ROWBACKGROUNDS',(0,1),(-1,-1),[CARD,HexColor('#1c1611')]),
                ('GRID',(0,0),(-1,-1),0.5,LINE),('LEFTPADDING',(0,0),(-1,-1),8),
                ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
            S.append(t); S.append(Spacer(1,8))
        elif ln.strip():
            para(ln)
        i+=1
    return S

def main():
    global DAY,VIDEO,TITLE,SUBTITLE,TOPIC,BASEDIR,LEARN
    src=sys.argv[1] if len(sys.argv)>1 else 'days/day01.md'
    # BASEDIR = the topic folder (content file is in <topic>/days/, images in <topic>/images/)
    BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(src)))  # up from days/ to topic root
    meta,body=parse(src)
    DAY=int(meta.get('day',1)); VIDEO=int(meta.get('video',DAY))
    TITLE=meta.get('title',''); SUBTITLE=meta.get('subtitle',TITLE)
    TOPIC=meta.get('topic','MACHINE LEARNING')
    # "learn" front-matter: pipe-separated bullets for the cover "What you'll learn" box
    LEARN=[x.strip() for x in meta.get('learn','').split('|') if x.strip()]
    circle_crop(PHOTO,CIRCLE)
    slug=re.sub(r'[^a-z0-9]+','-',TITLE.lower()).strip('-')[:40]
    # write the PDF INTO the topic folder so each topic keeps its own PDFs
    out=os.path.join(BASEDIR, f"AI-with-Rav_Day-{DAY:02d}_{slug}.pdf")
    doc=BaseDocTemplate(out,pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=18*mm,bottomMargin=22*mm)
    # frame bottom raised to 22mm so body text NEVER reaches the footer band / corner photo (fixes overlap)
    frame=Frame(16*mm,22*mm,W-32*mm,H-40*mm,id='main')
    doc.addPageTemplates([PageTemplate(id='cover',frames=[frame],onPage=draw_cover),
                          PageTemplate(id='body',frames=[frame],onPage=page_bg)])
    doc.build(build_flowables(body))
    print("BUILT:",out)

if __name__=='__main__': main()
