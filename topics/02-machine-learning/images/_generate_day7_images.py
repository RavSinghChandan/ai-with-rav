import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; GOLD='#E0B265'; MUT='#b3a595'; RED='#e06a6a'
plt.rcParams.update({'text.color':FG})

def box(ax,x,y,w,h,txt,c,tc='#1a1512',fs=10):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.06",fc=c,ec=FG,lw=1.4))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',color=tc,fontsize=fs,fontweight='bold')
def arr(ax,x1,y1,x2,y2,label='',lc=MUT):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=16,lw=1.8,color=FG))
    if label: ax.text((x1+x2)/2,(y1+y2)/2+0.15,label,ha='center',fontsize=9,color=lc,fontweight='bold')

# IMG 1: a decision tree = 20 questions (should I play outside?)
fig,ax=plt.subplots(figsize=(11,6.5)); ax.set_xlim(0,12); ax.set_ylim(0,10); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,9.6,'A Decision Tree = a flowchart of yes/no questions',ha='center',fontsize=14,fontweight='bold',color=FG)
box(ax,4.5,7.7,3,1.1,'Is it raining?',YEL,fs=11)
box(ax,1.2,5.3,2.6,1.0,'Play inside',TEAL,fs=10)          # rain=yes
box(ax,7.4,5.3,3.0,1.0,'Is it too hot?',YEL,fs=10)        # rain=no
box(ax,6.0,2.8,2.6,1.0,'Play outside!',GRN,fs=10)         # hot=no
box(ax,9.4,2.8,2.4,1.0,'Stay in shade',TEAL,fs=9.5)       # hot=yes
arr(ax,5.4,7.7,2.5,6.3,'YES',RED); arr(ax,6.6,7.7,8.9,6.3,'NO',GRN)
arr(ax,8.4,5.3,7.3,3.8,'NO',GRN); arr(ax,9.6,5.3,10.6,3.8,'YES',RED)
ax.text(6,1.4,'Each box asks a question; each branch is an answer; the leaves are the final decisions.',ha='center',fontsize=9.5,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/19-decision-tree.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 2: how the tree PICKS the best question (split that separates classes)
fig,axes=plt.subplots(1,2,figsize=(11,4.4)); fig.patch.set_facecolor(BG)
import numpy as np; np.random.seed(2)
for ax,title,good in [(axes[0],'BAD split\n(mixes both types)',False),(axes[1],'GOOD split\n(separates cleanly)',True)]:
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    # two classes
    a=np.random.rand(20,2); b=np.random.rand(20,2)
    if good:
        a[:,0]=a[:,0]*0.45; b[:,0]=0.55+b[:,0]*0.45
    ax.scatter(a[:,0],a[:,1],c=SAF,s=70,edgecolor=FG,label='Spam')
    ax.scatter(b[:,0],b[:,1],c=TEAL,s=70,edgecolor=FG,label='Not spam')
    ax.axvline(0.5,color=YEL,ls='--',lw=2)
    ax.set_title(title,fontsize=11,fontweight='bold',color=(GRN if good else RED))
    ax.set_xticks([]); ax.set_yticks([])
    if good: ax.legend(fontsize=8,facecolor=CARD,edgecolor='#3a2f26',labelcolor=FG,loc='upper center')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/20-best-split.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 3: overfitting — a tree grown too deep
fig,ax=plt.subplots(figsize=(10,3.8)); ax.set_xlim(0,12); ax.set_ylim(0,5); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,4.6,'Trees can grow TOO deep (memorising, not learning)',ha='center',fontsize=13,fontweight='bold',color=FG)
box(ax,0.5,2.0,3.3,1.3,'Shallow tree\nsimple rules',GRN,fs=10)
box(ax,4.6,2.0,3.0,1.3,'Just right\ngeneralises',TEAL,fs=10)
box(ax,8.4,2.0,3.3,1.3,'Too deep\nmemorises data',RED,tc=FG,fs=10)
ax.text(2.15,1.3,'underfit',ha='center',color=MUT,fontsize=9,style='italic')
ax.text(10.05,1.3,'overfit',ha='center',color=MUT,fontsize=9,style='italic')
ax.text(6,0.5,'A tree with too many questions memorises the training data and fails on new data. Fix: limit its depth.',ha='center',fontsize=9.5,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/21-tree-overfit.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day7 images generated")
