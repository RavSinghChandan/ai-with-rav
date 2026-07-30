import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

def frame(ax, xlim=(0,10), ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)

def box(ax,x,y,w,h,color,text,tcolor=None,fs=11,bold=True):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05,rounding_size=0.12",
                 fc=color,ec=FG,lw=1.4,alpha=0.9,zorder=2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=tcolor or '#1a1512',
            fontsize=fs,fontweight='bold' if bold else 'normal',zorder=3)

# ===== 40: THE POSTMAN — two boxes, sorting letters by words =====
fig,ax=plt.subplots(figsize=(8.6,5.8)); fig.patch.set_facecolor(BG); frame(ax)
# two mailboxes (label in the box; word lists sit in clear space BELOW, no overlap)
box(ax,1.0,7.0,3.4,1.8,RED,"JUNK box",tcolor='#1a1512',fs=13)
box(ax,5.6,7.0,3.4,1.8,GRN,"IMPORTANT box",tcolor='#1a1512',fs=13)
ax.text(2.7,6.4,'"FREE"  "WINNER"\n"PRIZE"  "CLICK"',ha='center',va='top',color=RED,fontsize=10.5,fontweight='bold')
ax.text(7.3,6.4,'"bank"  "office"\n"your name"  "meeting"',ha='center',va='top',color=GRN,fontsize=10.5,fontweight='bold')
# a new letter arriving
box(ax,3.6,1.0,2.8,1.5,YEL,'NEW letter:\n"FREE PRIZE"',tcolor='#1a1512',fs=11)
ax.annotate('',xy=(2.7,6.8),xytext=(4.2,2.6),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.2))
ax.text(6.6,2.0,'The postman reads the WORDS\nand guesses the right box',color=FG,fontsize=10.5,ha='left')
ax.set_title('The postman sorts letters by the WORDS on them',fontsize=13,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/40-postman.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 41: LEARNING = COUNTING how often each word appears in each box =====
fig,ax=plt.subplots(figsize=(9.0,5.2)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
ax.set_title('Training = just COUNTING words in past letters',fontsize=13,fontweight='bold',color=FG)
words=['FREE','PRIZE','bank','meeting']
junk =[8, 7, 1, 0]     # times seen in junk
imp  =[1, 0, 6, 7]     # times seen in important
y0=7.6
for i,(w,j,m) in enumerate(zip(words,junk,imp)):
    y=y0-i*1.7
    ax.text(1.6,y+0.35,f'"{w}"',ha='right',color=FG,fontsize=11,fontweight='bold')
    # junk bar (red) and important bar (green)
    ax.add_patch(Rectangle((1.8,y),j*0.55,0.5,fc=RED,ec=FG,lw=0.8))
    ax.text(1.8+j*0.55+0.15,y+0.25,f'{j} junk',va='center',color=RED,fontsize=9.5,fontweight='bold')
    ax.add_patch(Rectangle((1.8,y-0.62),m*0.55,0.5,fc=GRN,ec=FG,lw=0.8))
    ax.text(1.8+m*0.55+0.15,y-0.37,f'{m} important',va='center',color=GRN,fontsize=9.5,fontweight='bold')
ax.text(5.0,0.5,'"FREE" leans JUNK · "meeting" leans IMPORTANT — the counts ARE the learning',
        ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/41-counting.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 42: MULTIPLY THE CLUES — chance of junk for a new letter =====
fig,ax=plt.subplots(figsize=(9.0,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
ax.set_title('For a new letter: MULTIPLY each word\'s chance together',fontsize=13,fontweight='bold',color=FG)
box(ax,0.4,5.5,2.4,2.2,CARD,'"FREE"\n→ 80% junk',tcolor=RED,fs=11)
ax.text(3.0,6.6,'×',ha='center',color=YEL,fontsize=26,fontweight='bold')
box(ax,3.4,5.5,2.4,2.2,CARD,'"PRIZE"\n→ 90% junk',tcolor=RED,fs=11)
ax.text(6.0,6.6,'×',ha='center',color=YEL,fontsize=26,fontweight='bold')
box(ax,6.4,5.5,2.4,2.2,CARD,'(start) 50%\njunk overall',tcolor=MUT,fs=10.5)
ax.annotate('',xy=(5.0,4.6),xytext=(5.0,5.4),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
box(ax,2.6,1.4,4.8,2.4,RED,'0.8 × 0.9 × 0.5 = 0.36\n→ high junk score → JUNK box',tcolor='#1a1512',fs=12)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/42-multiply.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 43: THE "NAIVE" ASSUMPTION — words treated as independent =====
fig,axes=plt.subplots(1,2,figsize=(11,4.6)); fig.patch.set_facecolor(BG)
for ax in axes: frame(ax)
# left: reality — words go together (two boxes joined by a link arrow)
ax=axes[0]
box(ax,1.2,5.6,2.8,2.2,CARD,'"New"',tcolor=FG,fs=13)
box(ax,5.6,5.6,2.8,2.2,CARD,'"York"',tcolor=FG,fs=13)
ax.annotate('',xy=(5.5,6.7),xytext=(4.1,6.7),arrowprops=dict(arrowstyle='<->',color=GRN,lw=3))
ax.text(4.8,7.9,'linked',ha='center',color=GRN,fontsize=11,fontweight='bold')
ax.text(5.0,3.4,'Reality: "New" and "York" go together —\nwords DEPEND on each other',ha='center',color=GRN,fontsize=11,fontweight='bold')
ax.set_title('What is really true',fontsize=12,fontweight='bold',color=GRN)
# right: naive — pretend each word is on its own island
ax=axes[1]
box(ax,0.8,5.6,2.4,2.2,CARD,'"New"',tcolor=FG,fs=12)
box(ax,3.8,5.6,2.4,2.2,CARD,'"York"',tcolor=FG,fs=12)
box(ax,6.8,5.6,2.4,2.2,CARD,'"free"',tcolor=FG,fs=12)
ax.text(5.0,3.4,'NAIVE: pretend every word is ALONE\n(ignore that they go together)',ha='center',color=RED,fontsize=11,fontweight='bold')
ax.text(5.0,1.4,'Wrong assumption — but it makes the maths\nlightning-fast, and it STILL works!',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
ax.set_title('What Naive Bayes PRETENDS',fontsize=12,fontweight='bold',color=RED)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/43-naive.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 44: BAYES FORMULA — simple, tied to the story =====
fig,ax=plt.subplots(figsize=(9.0,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
ax.set_title('The Bayes rule — in postman words',fontsize=13,fontweight='bold',color=FG)
ax.text(5.0,8.2,'chance letter is JUNK  =',ha='center',color=FG,fontsize=13,fontweight='bold')
# fraction
ax.text(5.0,6.4,'(how often JUNK)  ×  (chance these words appear IN junk)',ha='center',color=RED,fontsize=11.5,fontweight='bold')
ax.plot([1.2,8.8],[5.5,5.5],color=FG,lw=2)
ax.text(5.0,4.6,'(how often these words appear at ALL)',ha='center',color=BLU,fontsize=11.5,fontweight='bold')
box(ax,1.0,1.2,8.0,2.0,CARD,'"Prior" (how common junk is)  ×  "Likelihood" (words given junk)\n'
    '÷  "Evidence" (words overall)  =  the final chance',tcolor=YEL,fs=10.5,bold=True)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/44-formula.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day12 images generated")
