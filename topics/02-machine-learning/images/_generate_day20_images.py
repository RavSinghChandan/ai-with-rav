import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'; PUR='#c39bd3'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
def judge(ax,x,y,col,r=0.62,label=None):
    ax.add_patch(Circle((x,y),r,fc=col,ec=FG,lw=1.3,zorder=3))
    if label: ax.text(x,y,label,ha='center',va='center',color='#1a1512',fontsize=9,fontweight='bold',zorder=4)

# ===== 80: ONE JUDGE vs A PANEL =====
fig,axes=plt.subplots(1,2,figsize=(11,4.6)); fig.patch.set_facecolor(BG)
ax=axes[0]; frame(ax)
judge(ax,5,6,SAF,r=1.0,label='1')
ax.text(5,3.6,'ONE model',ha='center',color=SAF,fontsize=12,fontweight='bold')
ax.text(5,2.2,'one bad day or blind spot\n= a wrong answer',ha='center',color=RED,fontsize=10,fontweight='bold')
ax.set_title('One judge',fontsize=12,fontweight='bold',color=RED)
ax=axes[1]; frame(ax)
cols=[SAF,GRN,BLU,YEL,PUR]
for i,c in enumerate(cols):
    judge(ax,1.7+i*1.55,6.4,c,r=0.66,label=str(i+1))
ax.text(5,3.6,'a PANEL of models',ha='center',color=GRN,fontsize=12,fontweight='bold')
ax.text(5,2.2,'they vote → mistakes cancel out\n= a reliable answer',ha='center',color=GRN,fontsize=10,fontweight='bold')
ax.set_title('A panel (an ensemble)',fontsize=12,fontweight='bold',color=GRN)
fig.suptitle('One judge can be wrong — a panel voting together is far more reliable',
             fontsize=12.5,fontweight='bold',color=FG,y=1.03)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/80-panel.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 81: BAGGING =====
fig,ax=plt.subplots(figsize=(9.6,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('BAGGING: judges score DIFFERENT samples, then vote/average',fontsize=12,fontweight='bold',color=FG)
box_x=0.6
ax.add_patch(FancyBboxPatch((box_x,4.2),2.0,2.4,boxstyle="round,pad=0.05",fc=MUT,ec=FG,lw=1.3))
ax.text(box_x+1.0,5.4,'all\ndata',ha='center',va='center',color='#1a1512',fontsize=10,fontweight='bold')
cols=[SAF,GRN,BLU]
for i,c in enumerate(cols):
    y=7.6-i*2.3
    ax.add_patch(FancyBboxPatch((4.0,y),1.9,1.5,boxstyle="round,pad=0.04",fc=CARD,ec=c,lw=1.4))
    ax.text(4.95,y+0.75,f'model {i+1}\n(sample {i+1})',ha='center',va='center',color=c,fontsize=8.5,fontweight='bold')
    ax.annotate('',xy=(4.0,y+0.75),xytext=(2.6,5.4),arrowprops=dict(arrowstyle='->',color=MUT,lw=1.2,alpha=0.7))
    ax.annotate('',xy=(8.4,5.4),xytext=(5.9,y+0.75),arrowprops=dict(arrowstyle='->',color=YEL,lw=1.4))
ax.add_patch(FancyBboxPatch((8.6,4.4),3.0,2.0,boxstyle="round,pad=0.05",fc=GRN,ec=FG,lw=1.5))
ax.text(10.1,5.4,'VOTE /\nAVERAGE',ha='center',va='center',color='#1a1512',fontsize=10,fontweight='bold')
ax.text(6.0,1.0,'Parallel · each sees a different slice · this is Random Forest (Day 8)',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/81-bagging.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 82: BOOSTING =====
fig,ax=plt.subplots(figsize=(9.6,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('BOOSTING: judges go ONE AFTER ANOTHER, each fixing mistakes',fontsize=12,fontweight='bold',color=FG)
cols=[SAF,YEL,GRN]; labels=['model 1\nmakes\nmistakes','model 2\nfixes\nmistakes','model 3\nfixes\nwhat\'s left']
for i,(c,t) in enumerate(zip(cols,labels)):
    x=0.8+i*3.7
    ax.add_patch(FancyBboxPatch((x,4.0),2.7,2.8,boxstyle="round,pad=0.05",fc=CARD,ec=c,lw=1.6))
    ax.text(x+1.35,5.4,t,ha='center',va='center',color=c,fontsize=9.5,fontweight='bold')
    if i<2: ax.annotate('',xy=(x+3.7,5.4),xytext=(x+3.5,5.4),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.6))
ax.text(6.0,1.4,'Sequential · each learns from the last one\'s errors · this is XGBoost (Day 9)',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/82-boosting.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 83: STACKING =====
fig,ax=plt.subplots(figsize=(9.6,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('STACKING: a HEAD judge learns how much to trust each specialist',fontsize=12,fontweight='bold',color=FG)
specs=[('tree',SAF),('SVM',GRN),('KNN',BLU)]
for i,(t,c) in enumerate(specs):
    y=7.6-i*2.3
    ax.add_patch(FancyBboxPatch((0.8,y),2.4,1.5,boxstyle="round,pad=0.04",fc=CARD,ec=c,lw=1.4))
    ax.text(2.0,y+0.75,f'{t}\nspecialist',ha='center',va='center',color=c,fontsize=9,fontweight='bold')
    ax.annotate('',xy=(6.4,5.4),xytext=(3.2,y+0.75),arrowprops=dict(arrowstyle='->',color=YEL,lw=1.6))
ax.add_patch(FancyBboxPatch((6.6,3.8),3.2,3.2,boxstyle="round,pad=0.05",fc=PUR,ec=FG,lw=1.6))
ax.text(8.2,5.4,'HEAD JUDGE\nweighs each\n& decides',ha='center',va='center',color='#1a1512',fontsize=10,fontweight='bold')
ax.text(6.0,1.2,'A final model learns which specialist to trust when — the "combiner"',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/83-stacking.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 84: WHY IT WORKS — independent mistakes cancel =====
fig,ax=plt.subplots(figsize=(9.0,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
ax.set_title('Why it works: independent mistakes cancel out',fontsize=12.5,fontweight='bold',color=FG)
# 5 models, each mostly right (green) with a few different wrong (red)
np.random.seed(3)
qs=8
# 5 model rows packed in the TOP half so nothing collides with the caption
for m in range(5):
    y=9.0-m*1.05
    ax.text(0.9,y,f'model {m+1}',ha='right',va='center',color=FG,fontsize=9,fontweight='bold')
    wrong=set(np.random.choice(qs,2,replace=False))
    for q in range(qs):
        c=RED if q in wrong else GRN
        ax.add_patch(Rectangle((1.3+q*0.9,y-0.34),0.7,0.68,fc=c,ec=FG,lw=0.6))
# a divider, then the VOTE row clearly separated below
ax.plot([0.4,8.5],[3.05,3.05],color='#3a2f26',lw=1.2)
ax.text(0.9,2.4,'VOTE',ha='right',va='center',color=YEL,fontsize=10,fontweight='bold')
for q in range(qs):
    ax.add_patch(Rectangle((1.3+q*0.9,2.06),0.7,0.68,fc=GRN,ec=YEL,lw=1.6))
# caption at the very bottom, in clear space
ax.text(5.0,0.7,'each model gets a few (different) wrong — but the majority is right on every question',
        ha='center',color=GRN,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/84-why.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day20 images generated")
