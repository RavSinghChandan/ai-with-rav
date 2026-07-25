import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# IMG 1: one tree vs a forest (ask the audience)
fig,ax=plt.subplots(figsize=(11,5.2)); ax.set_xlim(0,12); ax.set_ylim(0,7); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,6.6,'One tree can be wrong. Ask 100 trees and vote — almost always right.',ha='center',fontsize=13,fontweight='bold',color=FG)
def tree(ax,cx,cy,ans,col,sc=1.0):
    ax.add_patch(FancyBboxPatch((cx-0.55*sc,cy-0.5*sc),1.1*sc,1.0*sc,boxstyle="round,pad=0.05",fc=col,ec=FG,lw=1.2))
    ax.text(cx,cy,ans,ha='center',va='center',color='#1a1512',fontsize=9*sc,fontweight='bold')
# left: one lonely tree, wrong
ax.text(2.2,5.2,'ONE tree',ha='center',fontsize=11,color=RED,fontweight='bold')
tree(ax,2.2,3.9,'Spam?\nNO',RED,1.4)
ax.text(2.2,2.4,'says NO\n(but it is WRONG)',ha='center',fontsize=9.5,color=RED,style='italic')
# right: a forest voting
ax.text(8.3,5.6,'A FOREST of trees',ha='center',fontsize=11,color=GRN,fontweight='bold')
votes=[('YES',GRN),('YES',GRN),('NO',RED),('YES',GRN),('YES',GRN),('NO',RED),('YES',GRN),('YES',GRN)]
for i,(a,c) in enumerate(votes):
    r=i//4; cc=i%4
    tree(ax,6.4+cc*1.25,4.7-r*1.4,a,c,0.85)
ax.add_patch(FancyBboxPatch((6.1,1.0),4.4,1.0,boxstyle="round,pad=0.06",fc=GOLD if False else YEL,ec=FG,lw=1.5))
ax.text(8.3,1.5,'VOTE: 6 say YES, 2 say NO  →  YES ✔',ha='center',va='center',color='#1a1512',fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/26-one-vs-forest.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 2: how each tree is made different (different friends, different clues)
fig,ax=plt.subplots(figsize=(11,5.4)); ax.set_xlim(0,12); ax.set_ylim(0,7); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,6.6,'The trick: make every tree a bit DIFFERENT',ha='center',fontsize=13,fontweight='bold',color=FG)
# big data box
ax.add_patch(FancyBboxPatch((0.4,2.2),2.6,2.2,boxstyle="round,pad=0.06",fc=TEAL,ec=FG,lw=1.4))
ax.text(1.7,3.3,'Full data\n+ all clues',ha='center',va='center',color='#1a1512',fontsize=10,fontweight='bold')
# three trees each get a random slice
slices=[('Tree 1\nrandom rows\n+ some clues',SAF,4.7),('Tree 2\ndifferent rows\n+ other clues',GRN,2.5),('Tree 3\nyet another mix',YEL,0.3)]
for txt,c,y in slices:
    ax.add_patch(FancyBboxPatch((5.2,y),3.4,1.5,boxstyle="round,pad=0.06",fc=c,ec=FG,lw=1.3))
    ax.text(6.9,y+0.75,txt,ha='center',va='center',color='#1a1512',fontsize=9.5,fontweight='bold')
    ax.add_patch(FancyArrowPatch((3.0,3.7),(5.2,y+0.75),arrowstyle='-|>',mutation_scale=15,lw=1.6,color=FG))
ax.text(6,0.1,'Each tree sees random rows + random clues → so they make DIFFERENT mistakes, which cancel out when they vote.',ha='center',fontsize=9,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/27-different-trees.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 3: errors cancel out — accuracy of forest vs single tree
fig,ax=plt.subplots(figsize=(9,4.6)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
n=np.array([1,5,10,25,50,100]); acc=np.array([78,85,88,90.5,91.5,92])
ax.plot(n,acc,'-o',color=GRN,lw=3,ms=9)
ax.axhline(78,color=RED,ls='--',lw=1.5)
ax.text(60,79.2,'one tree alone',color=RED,fontsize=10,fontweight='bold')
ax.annotate('more trees →\nmore accurate\n(then it flattens)',xy=(100,92),xytext=(45,86),fontsize=10,color=GRN,ha='center',arrowprops=dict(arrowstyle='->',color=GRN,lw=1.4))
ax.set_xlabel('number of trees in the forest',fontsize=12,fontweight='bold')
ax.set_ylabel('accuracy (%)',fontsize=12,fontweight='bold')
ax.set_title('More trees = fewer mistakes (their errors cancel out)',fontsize=12,fontweight='bold',color=FG)
ax.grid(alpha=0.12,color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/28-forest-accuracy.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day8 images generated")
