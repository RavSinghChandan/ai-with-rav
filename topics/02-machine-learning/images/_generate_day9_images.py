import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# IMG 1: Forest (all at once, vote) vs Boosting (one after another, fix mistakes)
fig,ax=plt.subplots(figsize=(11,5.2)); ax.set_xlim(0,12); ax.set_ylim(0,7); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,6.6,'Random Forest vs XGBoost — two ways to use many trees',ha='center',fontsize=13,fontweight='bold',color=FG)
def tbox(cx,cy,txt,c,w=1.5,h=1.0):
    ax.add_patch(FancyBboxPatch((cx-w/2,cy-h/2),w,h,boxstyle="round,pad=0.05",fc=c,ec=FG,lw=1.2))
    ax.text(cx,cy,txt,ha='center',va='center',color='#1a1512',fontsize=9,fontweight='bold')
# top: forest = side by side, then vote
ax.text(1.4,5.2,'FOREST',ha='center',fontsize=10.5,color=GRN,fontweight='bold')
for i in range(3): tbox(3.0+i*1.6,5.0,f'Tree {i+1}',GRN,1.3,0.9)
ax.text(8.8,5.0,'all built together\n→ VOTE',ha='center',va='center',fontsize=10,color=GRN,fontweight='bold')
# bottom: boosting = chain, each fixes last
ax.text(1.4,2.3,'XGBoost',ha='center',fontsize=10.5,color=SAF,fontweight='bold')
for i in range(3):
    tbox(2.6+i*2.6,2.1,f'Tree {i+1}',SAF,1.3,0.9)
    if i<2:
        ax.add_patch(FancyArrowPatch((2.6+i*2.6+0.75,2.1),(2.6+(i+1)*2.6-0.75,2.1),arrowstyle='-|>',mutation_scale=16,lw=2,color=YEL))
        ax.text(2.6+i*2.6+1.3,2.55,'fixes\nmistakes',ha='center',fontsize=8,color=YEL,fontweight='bold')
ax.text(10.6,2.1,'built one\nafter another',ha='center',va='center',fontsize=9.5,color=SAF,fontweight='bold')
ax.text(6,0.4,'Forest: all trees vote at once. XGBoost: each new tree fixes the mistakes of the ones before it.',ha='center',fontsize=9.5,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/29-forest-vs-boost.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 2: learning from mistakes — each round the error shrinks
fig,ax=plt.subplots(figsize=(11,4.4)); ax.set_xlim(0,12); ax.set_ylim(0,5); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,4.6,'Each new tree studies the LEFTOVER mistakes',ha='center',fontsize=13,fontweight='bold',color=FG)
rounds=[('Tree 1','gets a lot right,\nbut makes mistakes',SAF,1.0,'big error'),
        ('Tree 2','studies only\nthose mistakes',YEL,4.4,'smaller error'),
        ('Tree 3','fixes what is\nstill wrong',GRN,7.8,'tiny error')]
for name,desc,c,x,err in rounds:
    ax.add_patch(FancyBboxPatch((x,1.8),2.9,1.7,boxstyle="round,pad=0.06",fc=c,ec=FG,lw=1.3))
    ax.text(x+1.45,2.9,name,ha='center',fontsize=11,color='#1a1512',fontweight='bold')
    ax.text(x+1.45,2.25,desc,ha='center',fontsize=9,color='#1a1512')
    ax.text(x+1.45,1.3,err,ha='center',fontsize=9.5,color=c,fontweight='bold',style='italic')
for x in [3.9,7.3]:
    ax.add_patch(FancyArrowPatch((x,2.65),(x+0.5,2.65),arrowstyle='-|>',mutation_scale=16,lw=2,color=FG))
ax.text(6,0.4,'Add up all the trees → a super-accurate answer. Like a student who only re-studies the questions they got wrong.',ha='center',fontsize=9,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/30-learn-from-mistakes.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 3: error dropping each round
fig,ax=plt.subplots(figsize=(9,4.6)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
r=np.arange(1,13); err=8.5*np.exp(-0.35*r)+0.8
ax.plot(r,err,'-o',color=SAF,lw=3,ms=8)
ax.annotate('each new tree\nshrinks the error',xy=(3,err[2]),xytext=(6.5,6),fontsize=10,color=YEL,ha='center',arrowprops=dict(arrowstyle='->',color=YEL,lw=1.4))
ax.set_xlabel('tree number (round)',fontsize=12,fontweight='bold')
ax.set_ylabel('mistakes left (error)',fontsize=12,fontweight='bold')
ax.set_title('Round after round, the leftover mistakes shrink',fontsize=12,fontweight='bold',color=FG)
ax.grid(alpha=0.12,color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/31-error-drop.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day9 images generated")
