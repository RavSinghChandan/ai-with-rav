import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import os

# DARK theme palette (identical to every other topic)
BG='#0d1117'; FG='#e6edf3'; SAFFRON='#FF6B35'; TEAL='#33B5E5'; GREEN='#06D6A0'
YELLOW='#FFD166'; RED='#F85149'; MUT='#8b949e'; PANEL='#161b22'
plt.rcParams['text.color']=FG; plt.rcParams['axes.labelcolor']=FG
plt.rcParams['xtick.color']=FG; plt.rcParams['ytick.color']=FG

OUT=os.path.dirname(os.path.abspath(__file__))
def save(name):
    plt.savefig(os.path.join(OUT,name),dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
def arrow(ax,x1,y1,x2,y2,c=FG,lw=2.6):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=22,lw=lw,color=c))

# ========== DAY 2: 4-bit RGB unpacking ==========
fig, ax = plt.subplots(figsize=(12,5.6)); ax.set_xlim(0,24); ax.set_ylim(0,11); ax.axis('off')
fig.patch.set_facecolor(BG)
ax.text(12,10.3,'One 4-bit RGB pixel = three samples, packed',ha='center',fontsize=15,fontweight='bold',color=FG)

# packed bytes strip
ax.text(2.0,8.6,'On disk:',ha='left',fontsize=11.5,color=MUT)
labels=[('R','F',SAFFRON),('G','0',GREEN),('B','0',TEAL),('R','8',SAFFRON),('G','8',GREEN),('B','8',TEAL)]
X0=6.4; CW=1.7   # cell pitch; cell body is CW wide so bytes tile exactly
for i,(comp,val,c) in enumerate(labels):
    x=X0+i*CW
    ax.add_patch(Rectangle((x,8.0),CW,1.3,fc=PANEL,ec=c,lw=2.0))
    ax.text(x+CW/2,8.65,val,ha='center',va='center',fontsize=13,color=c,fontweight='bold',family='monospace')
    ax.text(x+CW/2,7.5,comp,ha='center',fontsize=10,color=MUT)
# byte brackets: each byte holds exactly 2 samples
for b in range(3):
    bx=X0+b*2*CW
    ax.plot([bx,bx+2*CW],[9.55,9.55],color=MUT,lw=1.4)
    ax.text(bx+CW,9.8,'1 byte',ha='center',fontsize=9,color=MUT)
# pixel spans: 3 samples each
for p,(px,pc) in enumerate([(X0,YELLOW),(X0+3*CW,YELLOW)]):
    ax.plot([px,px+3*CW],[7.05,7.05],color=pc,lw=1.6)
    ax.text(px+1.5*CW,6.6,f'pixel {p+1}',ha='center',fontsize=9.5,color=pc)
ax.text(2.0,8.6,'',ha='left')

# wrong read
ax.add_patch(FancyBboxPatch((0.8,3.5),10.4,2.4,boxstyle="round,pad=0.12",fc=PANEL,ec=RED,lw=2.0))
ax.text(6.0,5.3,'OLD:  for x in range(width)',ha='center',fontsize=11.5,color=RED,family='monospace',fontweight='bold')
ax.text(6.0,4.3,'reads 1 sample per pixel\nstops a third of the way through the row',
        ha='center',va='center',fontsize=10.5,color=FG)

# right read
ax.add_patch(FancyBboxPatch((12.8,3.5),10.4,2.4,boxstyle="round,pad=0.12",fc=PANEL,ec=GREEN,lw=2.0))
ax.text(18.0,5.3,'NEW:  range(width * colors)',ha='center',fontsize=11.5,color=GREEN,family='monospace',fontweight='bold')
ax.text(18.0,4.3,'reads all 3 components\nthen scales 0-15 up to 0-255',
        ha='center',va='center',fontsize=10.5,color=FG)

ax.text(12,2.3,'4-bit value 15  ->  255   (factor = 255 // mask)',ha='center',
        fontsize=12,color=YELLOW,fontweight='bold')
ax.text(12,1.1,'Greyscale and palette images have 1 component, so they never hit the bug.',
        ha='center',fontsize=10.5,color=MUT,style='italic')
plt.tight_layout(); save('05-4bit-rgb-unpacking.png')

# ========== DAY 3: three paths, one fix ==========
fig, ax = plt.subplots(figsize=(12,5.8)); ax.set_xlim(0,24); ax.set_ylim(0,11); ax.axis('off')
fig.patch.set_facecolor(BG)
ax.text(12,10.4,'The fix lived on one branch only',ha='center',fontsize=15,fontweight='bold',color=FG)
ax.text(12,9.5,'PDF image  ->  which filter?',ha='center',fontsize=11.5,color=MUT)

paths=[(3.4,'FlateDecode\nRunLength',GREEN,'_handle_flate',True),
       (12.0,'no filter\nat all',RED,'_image_from_bytes',False),
       (20.6,'LZW /\nASCII85',RED,'_image_from_bytes',False)]
for x,label,c,fn,fixed in paths:
    ax.add_patch(FancyBboxPatch((x-3.0,6.6),6.0,1.5,boxstyle="round,pad=0.08",fc=PANEL,ec=c,lw=2.0))
    ax.text(x,7.35,label,ha='center',va='center',fontsize=11,color=FG,fontweight='bold')
    arrow(ax,12,9.2,x,8.25,MUT,2.0)
    ax.add_patch(FancyBboxPatch((x-3.0,4.3),6.0,1.3,boxstyle="round,pad=0.08",
                                fc=PANEL,ec=MUT,lw=1.4))
    ax.text(x,4.95,fn,ha='center',va='center',fontsize=10,color=MUT,family='monospace')
    arrow(ax,x,6.5,x,5.75,MUT,2.0)
    if fixed:
        ax.text(x,3.4,'expansion ran here',ha='center',fontsize=10.5,color=GREEN,fontweight='bold')
        ax.text(x,2.5,'#3929 fixed this',ha='center',fontsize=10,color=MUT,style='italic')
    else:
        ax.text(x,3.4,'raw "4bits" -> Pillow',ha='center',fontsize=10.5,color=RED,fontweight='bold')
        ax.text(x,2.5,'still broken',ha='center',fontsize=10,color=MUT,style='italic')

ax.add_patch(FancyBboxPatch((1.0,0.5),22.0,1.4,boxstyle="round,pad=0.1",fc=PANEL,ec=YELLOW,lw=2.0))
ax.text(12,1.2,'#3938:  pull the expansion into _expand_low_bit_samples(), call it from all three',
        ha='center',va='center',fontsize=11.5,color=YELLOW,fontweight='bold')
plt.tight_layout(); save('06-three-paths-one-fix.png')

# ========== DAY 4: finding untested code ==========
fig, ax = plt.subplots(figsize=(11.5,5.6)); ax.set_xlim(0,23); ax.set_ylim(0,11); ax.axis('off')
fig.patch.set_facecolor(BG)
ax.text(11.5,10.3,'Find the gap in four seconds',ha='center',fontsize=15,fontweight='bold',color=FG)

ax.add_patch(FancyBboxPatch((0.8,2.2),9.6,7.0,boxstyle="round,pad=0.12",fc=PANEL,ec=TEAL,lw=2.0))
ax.text(5.6,8.5,'nltk/util.py  exports',ha='center',fontsize=12,color=TEAL,fontweight='bold')
fns=[('everygrams',GREEN),('transitive_closure',RED),('invert_dict',RED),
     ('pad_sequence',RED),('...more',MUT)]
y=7.4
for name,c in fns:
    ax.text(5.6,y,name,ha='center',fontsize=11.5,color=c,family='monospace')
    y-=0.95

ax.add_patch(FancyBboxPatch((12.6,2.2),9.6,7.0,boxstyle="round,pad=0.12",fc=PANEL,ec=SAFFRON,lw=2.0))
ax.text(17.4,8.5,'test_util.py  imports',ha='center',fontsize=12,color=SAFFRON,fontweight='bold')
ax.text(17.4,6.9,'from nltk.util import\n    everygrams',ha='center',va='center',
        fontsize=11.5,color=GREEN,family='monospace')
ax.text(17.4,4.6,'one function.\nthat is the whole file.',ha='center',va='center',
        fontsize=11,color=MUT,style='italic')

ax.text(11.5,1.1,'Everything red is a contribution waiting to happen.',
        ha='center',fontsize=12.5,color=YELLOW,fontweight='bold')
plt.tight_layout(); save('07-finding-untested-code.png')

# ========== DAY 5: guard clause paths ==========
fig, ax = plt.subplots(figsize=(11.5,5.6)); ax.set_xlim(0,23); ax.set_ylim(0,11); ax.axis('off')
fig.patch.set_facecolor(BG)
ax.text(11.5,10.3,'append_to_last_row: four inputs, two outcomes',ha='center',fontsize=15,fontweight='bold',color=FG)

cases=[(3.2,'header +\ndata rows',GREEN,'appends\nreturns True',GREEN),
       (8.9,'header + data\nmany values',GREEN,'appends all\nreturns True',GREEN),
       (14.6,'header\nonly',RED,'no write\nreturns False',YELLOW),
       (20.3,'empty\nfile',RED,'no write\nreturns False',YELLOW)]
for x,inp,ic,out,oc in cases:
    ax.add_patch(FancyBboxPatch((x-2.4,7.4),4.8,1.9,boxstyle="round,pad=0.08",fc=PANEL,ec=ic,lw=2.0))
    ax.text(x,8.35,inp,ha='center',va='center',fontsize=11,color=FG,fontweight='bold')
    arrow(ax,x,7.3,x,5.9,oc,2.2)
    ax.add_patch(FancyBboxPatch((x-2.4,3.9),4.8,1.9,boxstyle="round,pad=0.08",fc=PANEL,ec=oc,lw=2.0))
    ax.text(x,4.85,out,ha='center',va='center',fontsize=10.5,color=oc,fontweight='bold')

ax.add_patch(FancyBboxPatch((12.0,0.6),10.4,2.5,boxstyle="round,pad=0.1",fc=PANEL,ec=YELLOW,lw=2.0))
ax.text(17.2,1.85,'the guard.\nbreaks silently, no exception.',ha='center',va='center',
        fontsize=11.5,color=YELLOW,fontweight='bold')
ax.text(5.6,1.85,'these two fail loudly\nif you break them',ha='center',va='center',
        fontsize=11,color=MUT,style='italic')
plt.tight_layout(); save('08-guard-clause-paths.png')

# ========== DAY 6: volume vs value ==========
fig, ax = plt.subplots(figsize=(11.5,5.4)); ax.set_xlim(0,23); ax.set_ylim(0,11); ax.axis('off')
fig.patch.set_facecolor(BG)
ax.text(11.5,10.3,'Where the merges actually came from',ha='center',fontsize=15,fontweight='bold',color=FG)

# 35 docs PRs as a grid of dots
ax.text(5.8,8.9,'35 docstring PRs',ha='center',fontsize=12.5,color=SAFFRON,fontweight='bold')
i=0
for row in range(5):
    for col in range(7):
        merged = i in (11,27)
        ax.plot([1.9+col*1.1],[7.9-row*0.85],marker='o',markersize=11,
                color=GREEN if merged else '#30363d')
        i+=1
ax.text(5.8,2.9,'2 merged',ha='center',fontsize=12,color=GREEN,fontweight='bold')
ax.text(5.8,2.0,'6% hit rate',ha='center',fontsize=10.5,color=MUT,style='italic')

ax.plot([11.5,11.5],[2.2,9.2],color='#30363d',lw=1.6,ls='--')

# 3 real bugs
ax.text(17.2,8.9,'3 real bug fixes',ha='center',fontsize=12.5,color=TEAL,fontweight='bold')
for k in range(3):
    ax.plot([15.6+k*1.6],[7.5],marker='o',markersize=22,color=GREEN)
ax.text(17.2,5.9,'3 merged',ha='center',fontsize=12,color=GREEN,fontweight='bold')
ax.text(17.2,5.0,'100%',ha='center',fontsize=10.5,color=MUT,style='italic')
ax.text(17.2,3.4,'each one found by\nusing the library',ha='center',va='center',
        fontsize=11,color=FG)

ax.text(11.5,0.9,'Same effort. Very different return.',ha='center',
        fontsize=12.5,color=YELLOW,fontweight='bold')
plt.tight_layout(); save('09-volume-vs-value.png')

# ========== DAY 7: anatomy of a reviewable PR ==========
fig, ax = plt.subplots(figsize=(10.5,6.2)); ax.set_xlim(0,21); ax.set_ylim(0,13); ax.axis('off')
fig.patch.set_facecolor(BG)
ax.text(10.5,12.2,'What a maintainer needs, in order',ha='center',fontsize=15,fontweight='bold',color=FG)

rows=[('1','SCOPE','what changed, as a list or table',GREEN,'5 seconds'),
      ('2','WHY','one sentence on the gap it fills',TEAL,'10 seconds'),
      ('3','RISK','"no logic changes" / what is opt-in',YELLOW,'5 seconds'),
      ('4','PROOF','test that fails without the fix',SAFFRON,'the review'),
      ('5','CHECKS','linter / pre-commit already run',MUT,'0 seconds')]
y=10.2
for num,head,body,c,cost in rows:
    ax.add_patch(FancyBboxPatch((1.2,y-0.05),18.6,1.55,boxstyle="round,pad=0.08",fc=PANEL,ec=c,lw=1.8))
    ax.plot([2.4],[y+0.72],marker='o',markersize=20,color=c)
    ax.text(2.4,y+0.72,num,ha='center',va='center',fontsize=11,color=BG,fontweight='bold')
    ax.text(4.0,y+0.72,head,ha='left',va='center',fontsize=12,color=c,fontweight='bold')
    ax.text(8.0,y+0.72,body,ha='left',va='center',fontsize=10.5,color=FG)
    ax.text(19.3,y+0.72,cost,ha='right',va='center',fontsize=9.5,color=MUT,style='italic')
    y-=1.95

ax.text(10.5,0.5,'A table beats a paragraph: it hands over the list instead of hiding it.',
        ha='center',fontsize=11.5,color=YELLOW,fontweight='bold')
plt.tight_layout(); save('10-reviewable-pr-anatomy.png')

print('day02-07 images written to', OUT)
