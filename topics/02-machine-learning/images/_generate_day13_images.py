import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'; PUR='#c39bd3'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)

# three natural groups of "kids" (playground). Fixed so every diagram is consistent.
np.random.seed(7)
g1=np.array([[2.0,7.6],[2.6,8.2],[1.6,7.0],[2.9,7.2],[2.2,6.6],[1.8,8.0]])   # by the swings
g2=np.array([[7.6,7.8],[8.2,7.2],[7.0,7.4],[8.0,8.2],[7.4,6.8],[8.4,7.6]])   # cricket pitch
g3=np.array([[4.6,2.4],[5.2,2.0],[4.2,1.8],[5.6,2.6],[4.8,3.0],[5.0,1.4]])   # under the tree
allk=np.vstack([g1,g2,g3])

# ===== 45: SCATTERED KIDS — no labels, find the natural groups =====
fig,ax=plt.subplots(figsize=(8.4,5.4)); fig.patch.set_facecolor(BG); frame(ax)
ax.scatter(allk[:,0],allk[:,1],c=MUT,s=200,edgecolor=FG,zorder=3)
ax.set_title('A playground of kids — nobody is labelled.\nCan you spot the natural groups?',fontsize=12.5,fontweight='bold',color=FG)
ax.text(2.2,5.6,'swings?',color=MUT,fontsize=10,ha='center',style='italic')
ax.text(7.7,5.6,'cricket?',color=MUT,fontsize=10,ha='center',style='italic')
ax.text(4.9,4.0,'tree?',color=MUT,fontsize=10,ha='center',style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/45-scattered.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 46: PICK K CENTERS — each kid joins the NEAREST center =====
fig,ax=plt.subplots(figsize=(8.4,5.4)); fig.patch.set_facecolor(BG); frame(ax)
centers=np.array([[2.3,7.4],[7.8,7.5],[4.9,2.2]])
cols=[SAF,GRN,BLU]
# assign each kid to nearest center
for p in allk:
    d=np.linalg.norm(centers-p,axis=1); ci=int(np.argmin(d))
    ax.plot([p[0],centers[ci,0]],[p[1],centers[ci,1]],color=cols[ci],lw=1.0,alpha=0.55,zorder=1)
    ax.scatter(*p,c=cols[ci],s=170,edgecolor=FG,zorder=3)
for c,col in zip(centers,cols):
    ax.scatter(*c,c=col,s=520,edgecolor=FG,marker='*',zorder=5,linewidth=1.5)
ax.set_title('Step 1: drop K "teacher-spots" (stars).\nEach kid joins the NEAREST star.',fontsize=12.5,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/46-assign.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 47: MOVE CENTERS TO THE MIDDLE of their group =====
fig,ax=plt.subplots(figsize=(8.4,5.4)); fig.patch.set_facecolor(BG); frame(ax)
old=np.array([[2.3,7.4],[7.8,7.5],[4.9,2.2]])
groups=[g1,g2,g3]; cols=[SAF,GRN,BLU]
for grp,col in zip(groups,cols):
    ax.scatter(grp[:,0],grp[:,1],c=col,s=170,edgecolor=FG,zorder=3)
for o,grp,col in zip(old,groups,cols):
    new=grp.mean(axis=0)
    ax.scatter(*o,c=col,s=300,edgecolor=FG,marker='*',alpha=0.35,zorder=4)   # old ghost
    ax.annotate('',xy=(new[0],new[1]),xytext=(o[0],o[1]),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
    ax.scatter(*new,c=col,s=560,edgecolor=YEL,marker='*',zorder=6,linewidth=1.8)   # new center
ax.set_title('Step 2: each star moves to the MIDDLE of its group\n(the average spot of its kids)',fontsize=12.5,fontweight='bold',color=FG)
ax.text(0.4,0.6,'faint star = old spot   ·   bright star = new middle',color=MUT,fontsize=9.5)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/47-move.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 48: REPEAT UNTIL STABLE — clean settled clusters =====
fig,axes=plt.subplots(1,2,figsize=(11,4.7)); fig.patch.set_facecolor(BG)
# left: messy start (centers off) ; right: settled
for ax,title,cen,col_note in [
    (axes[0],'Round 1: messy',np.array([[3.5,6.0],[6.5,6.0],[5.0,4.0]]),'still shuffling'),
    (axes[1],'Settled: nobody switches',np.array([g1.mean(0),g2.mean(0),g3.mean(0)]),'done!')]:
    frame(ax)
    for grp,col,c in zip([g1,g2,g3],[SAF,GRN,BLU],cen):
        # colour kids by nearest of THIS panel's centers
        pass
    # assign by nearest center in this panel
    for p in allk:
        d=np.linalg.norm(cen-p,axis=1); ci=int(np.argmin(d))
        ax.scatter(*p,c=[SAF,GRN,BLU][ci],s=150,edgecolor=FG,zorder=3)
    for c,col in zip(cen,[SAF,GRN,BLU]):
        ax.scatter(*c,c=col,s=460,edgecolor=YEL,marker='*',zorder=5,linewidth=1.5)
    ax.set_title(title,fontsize=12,fontweight='bold',color=(RED if 'messy' in title else GRN))
axes[0].text(5,0.5,'centers still in wrong spots',ha='center',color=RED,fontsize=10,fontweight='bold')
axes[1].text(5,0.5,'three clean groups found — no labels needed',ha='center',color=GRN,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/48-settle.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 49: CHOOSING K — the elbow =====
fig,ax=plt.subplots(figsize=(8.6,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,8),(0,10))
K=np.array([1,2,3,4,5,6]); err=np.array([9.2,5.0,2.2,1.7,1.4,1.2])
ax.plot(K,err,color=BLU,lw=2.6,marker='o',markersize=9,markerfacecolor=YEL,markeredgecolor=FG,zorder=3)
# elbow at K=3
ax.scatter([3],[2.2],s=420,facecolor='none',edgecolor=RED,lw=2.6,zorder=4)
ax.annotate('the "elbow" —\nbest K = 3',xy=(3,2.2),xytext=(4.4,4.6),color=RED,fontsize=11,fontweight='bold',
            arrowprops=dict(arrowstyle='->',color=RED,lw=1.8))
ax.set_xlabel('K = number of groups you try',color=FG,fontsize=10.5)
ax.set_ylabel('leftover messiness',color=FG,fontsize=10.5)
ax.set_xticks(K); ax.set_xticklabels(K,color=FG)
ax.set_title('Choosing K: pick the "elbow" where adding groups stops helping',fontsize=12.5,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/49-elbow.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day13 images generated")
