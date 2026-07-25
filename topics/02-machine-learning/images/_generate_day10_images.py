import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# IMG 1: the new point + its nearest neighbours vote
np.random.seed(11)
fig,ax=plt.subplots(figsize=(8.5,6)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
# two groups
mangoes=np.array([[2,7],[3,8],[2.5,6],[1.5,7.5],[3.5,7],[2,8.5],[4,8]])  # class A (orange)
apples=np.array([[7,3],[8,2.5],[6.5,3.5],[7.5,2],[8.5,3],[7,1.5],[6,2.5]])  # class B (teal)
ax.scatter(mangoes[:,0],mangoes[:,1],c=SAF,s=130,edgecolor=FG,label='Team Orange',zorder=3)
ax.scatter(apples[:,0],apples[:,1],c=TEAL,s=130,edgecolor=FG,label='Team Green',zorder=3)
# the new unknown point, sitting near orange
newp=np.array([3.2,6.2])
ax.scatter(*newp,c=YEL,s=260,edgecolor=FG,marker='*',zorder=5,label='NEW (which team?)')
# draw lines to 3 nearest (all orange here)
allpts=np.vstack([mangoes,apples])
d=np.linalg.norm(allpts-newp,axis=1); nn=np.argsort(d)[:3]
for i in nn:
    ax.plot([newp[0],allpts[i,0]],[newp[1],allpts[i,1]],color=YEL,ls='--',lw=1.6,zorder=2)
ax.add_patch(Circle(newp,2.2,fill=False,ec=YEL,ls=':',lw=1.5))
ax.set_title('Which team does the NEW point belong to?\nLook at its 3 closest neighbours.',fontsize=12,fontweight='bold',color=FG)
ax.text(3.2,4.3,'3 closest are all Orange\n→ NEW is Orange!',ha='center',fontsize=10,color=SAF,fontweight='bold')
leg=ax.legend(fontsize=9,facecolor=CARD,edgecolor='#3a2f26',loc='upper right')
for t in leg.get_texts(): t.set_color(FG)
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,10); ax.set_ylim(0,10)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/32-knn-neighbours.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 2: what K means — K=3 vs K=7 can change the answer
fig,axes=plt.subplots(1,2,figsize=(11,4.8)); fig.patch.set_facecolor(BG)
np.random.seed(5)
# a point near a border
orange=np.array([[3,5],[4,6],[2,4],[3.5,4.5],[5,5.5],[4.5,4]])
green=np.array([[6,5],[7,6],[6.5,4],[5.5,6.5],[7.5,5],[6,3.5]])
newp2=np.array([5.2,5.0])
for ax,k,title in [(axes[0],3,'K = 3 neighbours'),(axes[1],7,'K = 7 neighbours')]:
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.scatter(orange[:,0],orange[:,1],c=SAF,s=110,edgecolor=FG,zorder=3)
    ax.scatter(green[:,0],green[:,1],c=TEAL,s=110,edgecolor=FG,zorder=3)
    ax.scatter(*newp2,c=YEL,s=220,edgecolor=FG,marker='*',zorder=5)
    allp=np.vstack([orange,green]); lab=['O']*6+['G']*6
    d=np.linalg.norm(allp-newp2,axis=1); nn=np.argsort(d)[:k]
    for i in nn: ax.plot([newp2[0],allp[i,0]],[newp2[1],allp[i,1]],color=YEL,ls='--',lw=1.3,zorder=2)
    votes=[lab[i] for i in nn]; o=votes.count('O'); g=votes.count('G')
    ans='Orange' if o>g else 'Green'; ac=SAF if o>g else TEAL
    ax.set_title(f'{title}\n{o} orange, {g} green → {ans}',fontsize=11,fontweight='bold',color=ac)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(1,9); ax.set_ylim(2.5,7.5)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/33-choosing-k.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 3: distance = a ruler between points
fig,ax=plt.subplots(figsize=(8.5,4.6)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
ax.scatter([2],[2],c=YEL,s=240,edgecolor=FG,marker='*',zorder=4); ax.text(2,1.4,'NEW point',ha='center',color=YEL,fontsize=10,fontweight='bold')
ax.scatter([6],[5],c=SAF,s=160,edgecolor=FG,zorder=4); ax.text(6,5.5,'a neighbour',ha='center',color=SAF,fontsize=10,fontweight='bold')
ax.plot([2,6],[2,5],color=GRN,lw=2.5,zorder=2)
ax.plot([2,6],[2,2],color=MUT,lw=1.3,ls=':'); ax.plot([6,6],[2,5],color=MUT,lw=1.3,ls=':')
ax.text(4,1.6,'4 across',ha='center',color=MUT,fontsize=9)
ax.text(6.4,3.5,'3 up',ha='left',color=MUT,fontsize=9)
ax.text(3.6,3.9,'distance = 5\n(straight line)',ha='center',color=GRN,fontsize=10.5,fontweight='bold')
ax.set_title('"Distance" is just a ruler between two points',fontsize=12,fontweight='bold',color=FG)
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,9); ax.set_ylim(0,6.5)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/34-distance.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day10 images generated")
