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

# ===== FROZEN BRAND (never changes) =====
BG=HexColor('#0d1117'); CARD=HexColor('#161b22'); FG=HexColor('#e6edf3'); MUT=HexColor('#9fb3c8')
SAF=HexColor('#FF6B35'); TEAL=HexColor('#33B5E5'); GRN=HexColor('#06D6A0'); YEL=HexColor('#FFD166'); LINE=HexColor('#21262d')
ACCENT={'yellow':YEL,'green':GRN,'teal':TEAL,'saffron':SAF}
W,H=A4
LOGO='brand/ai-for-business-logo.png'; PHOTO='brand/rav-photo.jpg'; CIRCLE='brand/rav-circle.png'

def circle_crop(src,dst,size=680,fcx=0.55,top_frac=0.06,frac=0.52):
    im=PImage.open(src).convert('RGBA'); w,h=im.size; side=int(h*frac); cx=int(w*fcx)
    left=min(max(0,cx-side//2),w-side); top=min(max(0,int(h*top_frac)),h-side)
    im2=im.crop((left,top,left+side,top+side)).resize((size,size))
    m=PImage.new('L',(size,size),0); ImageDraw.Draw(m).ellipse((0,0,size,size),fill=255)
    out=PImage.new('RGBA',(size,size),(0,0,0,0)); out.paste(im2,(0,0),m); out.save(dst)

def st(n,**k):
    b=dict(fontName='Helvetica',fontSize=11.5,leading=17,textColor=FG,spaceAfter=6); b.update(k); return ParagraphStyle(n,**b)
H1=st('H1',fontName='Helvetica-Bold',fontSize=22,leading=26,textColor=SAF,spaceAfter=4)
H2=st('H2',fontName='Helvetica-Bold',fontSize=15,leading=19,textColor=TEAL,spaceBefore=14,spaceAfter=6)
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
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),HexColor('#0b0e13')),('BOX',(0,0),(-1,-1),0.5,LINE),
        ('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),
        ('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10)])); return t

DAY=1; VIDEO=1; TITLE=''; SUBTITLE=''; TOPIC='MACHINE LEARNING'
def page_bg(cnv,doc,footer=True):
    cnv.setFillColor(BG); cnv.rect(0,0,W,H,fill=1,stroke=0)
    if not footer: return
    cnv.setFillColor(MUT); cnv.setFont('Helvetica',8)
    cnv.drawString(16*mm,10*mm,'AI with Rav  ·  Machine Learning in 30 Days')
    cnv.drawRightString(W-16*mm,10*mm,f'Day {DAY}')
    cnv.setStrokeColor(LINE); cnv.setLineWidth(0.5); cnv.line(16*mm,13*mm,W-16*mm,13*mm)

def draw_cover(cnv,doc):
    page_bg(cnv,doc,footer=False); cx=W/2
    if os.path.exists(LOGO):
        lr=PImage.open(LOGO); rat=lr.height/lr.width; lw=26*mm; lh=lw*rat
        cw=lw+8*mm; ch=lh+8*mm; cxx=cx-cw/2; cy=H-22*mm-ch
        cnv.setFillColor(HexColor('#ffffff')); cnv.roundRect(cxx,cy,cw,ch,6*mm,fill=1,stroke=0)
        cnv.drawImage(LOGO,cx-lw/2,cy+4*mm,lw,lh,mask='auto',preserveAspectRatio=True)
        ny=cy-9*mm; cnv.setFillColor(FG); cnv.setFont('Helvetica-Bold',18); cnv.drawCentredString(cx,ny,'AI with Rav'); logo_bottom=ny-4*mm
    else:
        cnv.setFillColor(FG); cnv.setFont('Helvetica-Bold',18); cnv.drawCentredString(cx,H-40*mm,'AI with Rav'); logo_bottom=H-44*mm
    py=logo_bottom-10*mm
    cnv.drawImage(CIRCLE,cx-30*mm,py-60*mm,60*mm,60*mm,mask='auto')
    cnv.setStrokeColor(SAF); cnv.setLineWidth(2.5); cnv.circle(cx,py-30*mm,30*mm,stroke=1,fill=0)
    ty=py-60*mm-20*mm
    cnv.setFillColor(SAF); cnv.setFont('Helvetica-Bold',32); cnv.drawCentredString(cx,ty,TOPIC.upper())
    cnv.setFillColor(FG); cnv.setFont('Helvetica-Bold',21); cnv.drawCentredString(cx,ty-13*mm,'with Rav')
    by=ty-30*mm; cnv.setFillColor(TEAL); cnv.roundRect(cx-34*mm,by-9*mm,68*mm,15*mm,7.5*mm,fill=1,stroke=0)
    cnv.setFillColor(BG); cnv.setFont('Helvetica-Bold',14); cnv.drawCentredString(cx,by-4*mm,f'DAY {DAY}  ·  VIDEO {VIDEO}')
    cnv.setFillColor(MUT); cnv.setFont('Helvetica',13); cnv.drawCentredString(cx,by-22*mm,SUBTITLE or TITLE)

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
                ('BACKGROUND',(0,1),(-1,-1),CARD),('ROWBACKGROUNDS',(0,1),(-1,-1),[CARD,HexColor('#11151b')]),
                ('GRID',(0,0),(-1,-1),0.5,LINE),('LEFTPADDING',(0,0),(-1,-1),8),
                ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
            S.append(t); S.append(Spacer(1,8))
        elif ln.strip():
            para(ln)
        i+=1
    return S

def main():
    global DAY,VIDEO,TITLE,SUBTITLE,TOPIC,BASEDIR
    src=sys.argv[1] if len(sys.argv)>1 else 'days/day01.md'
    # BASEDIR = the topic folder (content file is in <topic>/days/, images in <topic>/images/)
    BASEDIR=os.path.dirname(os.path.dirname(os.path.abspath(src)))  # up from days/ to topic root
    meta,body=parse(src)
    DAY=int(meta.get('day',1)); VIDEO=int(meta.get('video',DAY))
    TITLE=meta.get('title',''); SUBTITLE=meta.get('subtitle',TITLE)
    TOPIC=meta.get('topic','MACHINE LEARNING')
    circle_crop(PHOTO,CIRCLE)
    slug=re.sub(r'[^a-z0-9]+','-',TITLE.lower()).strip('-')[:40]
    # write the PDF INTO the topic folder so each topic keeps its own PDFs
    out=os.path.join(BASEDIR, f"AI-with-Rav_Day-{DAY:02d}_{slug}.pdf")
    doc=BaseDocTemplate(out,pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=18*mm,bottomMargin=18*mm)
    frame=Frame(16*mm,16*mm,W-32*mm,H-34*mm,id='main')
    doc.addPageTemplates([PageTemplate(id='cover',frames=[frame],onPage=draw_cover),
                          PageTemplate(id='body',frames=[frame],onPage=page_bg)])
    doc.build(build_flowables(body))
    print("BUILT:",out)

if __name__=='__main__': main()
