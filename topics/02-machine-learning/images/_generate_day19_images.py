import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'; PUR='#c39bd3'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
def box(ax,x,y,w,h,color,text,tcolor='#1a1512',fs=10,ec=None):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.04,rounding_size=0.1",
                 fc=color,ec=ec or FG,lw=1.3,alpha=0.92,zorder=2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=tcolor,fontsize=fs,fontweight='bold',zorder=3)

# ===== 75: RAW vs PREPPED — the chef idea =====
fig,ax=plt.subplots(figsize=(9.2,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Feature engineering = a chef prepping raw ingredients',fontsize=12.5,fontweight='bold',color=FG)
box(ax,0.6,3.8,3.4,2.8,MUT,'RAW DATA\n(a whole onion,\nunpeeled ginger)',fs=10.5)
ax.annotate('',xy=(6.2,5.2),xytext=(4.2,5.2),arrowprops=dict(arrowstyle='->',color=YEL,lw=3))
ax.text(5.2,6.0,'PREP\n(engineer)',ha='center',color=YEL,fontsize=10,fontweight='bold')
box(ax,6.4,3.8,4.8,2.8,GRN,'USEFUL FEATURES\n(chopped, ground,\nmeasured — ready to cook)',fs=10.5)
ax.text(6.0,1.8,'Same ingredients, smarter prep → a far tastier dish, even with a simple recipe',
        ha='center',color=YEL,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/75-raw-vs-prep.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 76: SPLIT ONE COLUMN INTO MANY =====
fig,ax=plt.subplots(figsize=(9.4,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Trick 1: split one column into many useful ones',fontsize=12.5,fontweight='bold',color=FG)
box(ax,0.6,4.0,3.2,2.4,BLU,'date:\n2026-08-15',tcolor='#1a1512',fs=11)
outs=[('day: 15',GRN),('month: 8',GRN),('weekday: Sat',YEL),('is_weekend: yes',SAF)]
for i,(t,c) in enumerate(outs):
    box(ax,7.4,7.0-i*1.7,4.0,1.3,c,t,tcolor='#1a1512',fs=10)
    ax.annotate('',xy=(7.4,7.65-i*1.7),xytext=(3.9,5.2),arrowprops=dict(arrowstyle='->',color=MUT,lw=1.3,alpha=0.7))
ax.text(6.0,0.8,'One raw date hides the day, month, weekday, and whether it\'s a weekend — all useful clues!',
        ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/76-split.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 77: TURN CATEGORIES INTO NUMBERS (one-hot) =====
fig,ax=plt.subplots(figsize=(9.4,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Trick 2: turn words into numbers (one-hot encoding)',fontsize=12.5,fontweight='bold',color=FG)
box(ax,0.6,3.8,3.0,3.0,BLU,'city:\nDelhi\nMumbai\nDelhi',tcolor='#1a1512',fs=10.5)
ax.annotate('',xy=(5.4,5.3),xytext=(3.8,5.3),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.6))
# one-hot table
hdr=['is_Delhi','is_Mumbai']
rows=[[1,0],[0,1],[1,0]]
x0=5.8
for j,h in enumerate(hdr):
    ax.text(x0+0.9+j*2.3,7.2,h,ha='center',color=SAF,fontsize=10,fontweight='bold')
for i,r in enumerate(rows):
    for j,v in enumerate(r):
        c=GRN if v==1 else CARD
        ax.add_patch(Rectangle((x0+j*2.3,6.2-i*1.0),1.8,0.8,fc=c,ec=FG,lw=1.0))
        ax.text(x0+j*2.3+0.9,6.6-i*1.0,str(v),ha='center',va='center',color=('#1a1512' if v==1 else FG),fontsize=10,fontweight='bold')
ax.text(6.0,1.0,'Models eat numbers, not words — so each category becomes a 0/1 column',
        ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/77-onehot.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 78: SCALING — same ruler =====
fig,axes=plt.subplots(1,2,figsize=(11,4.4)); fig.patch.set_facecolor(BG)
# left: before scaling -> salary dwarfs age
ax=axes[0]; frame(ax,(0,10),(0,10))
ax.barh([7],[9.0],color=BLU,edgecolor=FG); ax.text(9.2,7,'salary\n(50,000)',va='center',color=BLU,fontsize=10,fontweight='bold')
ax.barh([4],[0.4],color=SAF,edgecolor=FG); ax.text(1.0,4,'age (30)',va='center',color=SAF,fontsize=10,fontweight='bold')
ax.set_title('BEFORE: salary\'s big numbers drown out age',fontsize=11.5,fontweight='bold',color=RED)
# right: after scaling -> both 0..1
ax=axes[1]; frame(ax,(0,10),(0,10))
ax.barh([7],[6.5],color=BLU,edgecolor=FG); ax.text(6.9,7,'salary (0.7)',va='center',color=BLU,fontsize=10,fontweight='bold')
ax.barh([4],[5.5],color=SAF,edgecolor=FG); ax.text(5.9,4,'age (0.6)',va='center',color=SAF,fontsize=10,fontweight='bold')
ax.set_title('AFTER scaling: both on the SAME 0–1 ruler — fair',fontsize=11.5,fontweight='bold',color=GRN)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/78-scaling.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 79: COMBINE FEATURES into a smarter one =====
fig,ax=plt.subplots(figsize=(9.4,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Trick 3: combine columns into a smarter feature',fontsize=12.5,fontweight='bold',color=FG)
box(ax,0.6,5.4,3.0,1.6,BLU,'price:\n80 lakh',tcolor='#1a1512',fs=10.5)
box(ax,0.6,3.0,3.0,1.6,BLU,'area:\n1000 sq ft',tcolor='#1a1512',fs=10.5)
ax.text(4.4,5.0,'÷',ha='center',color=YEL,fontsize=28,fontweight='bold')
ax.annotate('',xy=(6.6,5.0),xytext=(5.0,5.0),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.6))
box(ax,6.8,4.2,4.6,1.8,GRN,'price_per_sqft:\n8,000 /sq ft',tcolor='#1a1512',fs=11)
ax.text(6.0,1.6,'Price alone is misleading — price PER sq ft is the clue that really predicts value',
        ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/79-combine.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day19 images generated")
