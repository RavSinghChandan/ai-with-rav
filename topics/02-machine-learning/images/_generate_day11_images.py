import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# two clean separable groups
orange=np.array([[2,6],[2.5,7.5],[3,6.8],[1.8,7.2],[3.3,8],[2.2,8.3],[3.5,7]])
green =np.array([[7,3],[7.8,2.2],[6.6,3.2],[8.2,3.5],[7.2,1.8],[8.5,2.6],[6.9,2.6]])

# IMG 35: many lines vs the ONE best
fig,axes=plt.subplots(1,2,figsize=(11,4.9)); fig.patch.set_facecolor(BG)
for ax in axes:
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.scatter(orange[:,0],orange[:,1],c=SAF,s=110,edgecolor=FG,zorder=3)
    ax.scatter(green[:,0],green[:,1],c=TEAL,s=110,edgecolor=FG,zorder=3)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,10); ax.set_ylim(0,10)
# left: many messy candidate lines
xs=np.linspace(0,10,50)
for (m,c,col) in [(-1.0,10,MUT),(-1.6,13,MUT),(-0.7,8.2,MUT),(-2.2,16,MUT)]:
    ax=axes[0]; ax.plot(xs,m*xs+c,color=col,lw=1.4,ls='--',alpha=0.8)
axes[0].set_title('Many lines can split them...\nwhich one is BEST?',fontsize=12,fontweight='bold',color=FG)
# right: the one best line with margin
ax=axes[1]
m,c=-1.0,10.0
ax.plot(xs,m*xs+c,color=YEL,lw=2.6,zorder=2)
ax.plot(xs,m*xs+c+2.0,color=GRN,lw=1.4,ls='--',zorder=1)
ax.plot(xs,m*xs+c-2.0,color=GRN,lw=1.4,ls='--',zorder=1)
ax.fill_between(xs,m*xs+c-2.0,m*xs+c+2.0,color=GRN,alpha=0.10)
ax.annotate('',xy=(6.0,6.0),xytext=(4.0,4.0),arrowprops=dict(arrowstyle='<->',color=GRN,lw=1.8))
ax.text(3.4,5.6,'widest\ngap',color=GRN,fontsize=10,fontweight='bold')
ax.set_title('The BEST line: the one with the\nWIDEST gap on both sides',fontsize=12,fontweight='bold',color=YEL)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/35-best-line.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 36: margin + support vectors
fig,ax=plt.subplots(figsize=(8.6,6)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
ax.scatter(orange[:,0],orange[:,1],c=SAF,s=110,edgecolor=FG,zorder=3)
ax.scatter(green[:,0],green[:,1],c=TEAL,s=110,edgecolor=FG,zorder=3)
xs=np.linspace(0,10,50); m,c=-1.0,10.0
ax.plot(xs,m*xs+c,color=YEL,lw=2.6,zorder=2,label='the road (decision line)')
ax.plot(xs,m*xs+c+2.0,color=GRN,lw=1.4,ls='--',zorder=1)
ax.plot(xs,m*xs+c-2.0,color=GRN,lw=1.4,ls='--',zorder=1)
ax.fill_between(xs,m*xs+c-2.0,m*xs+c+2.0,color=GRN,alpha=0.10)
# circle the support vectors: closest orange (3.5,7) & (3.3,8)? and closest green (6.6,3.2)
sv=[(3.5,7),(3.3,8),(6.6,3.2)]
for (x,y) in sv:
    ax.add_patch(Circle((x,y),0.45,fill=False,ec=RED,lw=2.4,zorder=4))
ax.text(1.6,2.2,'Red-ringed points = SUPPORT VECTORS\n(the edge points that hold the road in place)',color=RED,fontsize=10.5,fontweight='bold')
ax.text(6.9,8.2,'margin = the safety gap',color=GRN,fontsize=10.5,fontweight='bold')
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,10); ax.set_ylim(0,10)
ax.set_title('The margin (green gap) and the support vectors',fontsize=12,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/36-support-vectors.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 37: kernel trick — curved data can't be split by a line, lift it, then a plane splits it
fig,axes=plt.subplots(1,2,figsize=(11,4.9)); fig.patch.set_facecolor(BG)
np.random.seed(3)
# inner circle = orange, outer ring = green
ang=np.linspace(0,2*np.pi,14,endpoint=False)
inner=np.c_[1.3*np.cos(ang)+0,1.3*np.sin(ang)+0]
outer=np.c_[3.3*np.cos(ang)+0,3.3*np.sin(ang)+0]
ax=axes[0]; ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
ax.scatter(inner[:,0],inner[:,1],c=SAF,s=90,edgecolor=FG,zorder=3)
ax.scatter(outer[:,0],outer[:,1],c=TEAL,s=90,edgecolor=FG,zorder=3)
ax.set_title('A straight line CANNOT split\nthis (orange inside, green ring)',fontsize=11.5,fontweight='bold',color=RED)
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(-4.2,4.2); ax.set_ylim(-4.2,4.2); ax.set_aspect('equal')
# right: lifted — height = distance from centre; now a flat plane (line) separates
ax=axes[1]; ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
ri=np.linalg.norm(inner,axis=1); ro=np.linalg.norm(outer,axis=1)
xi=np.linspace(-3,-1,len(inner)); xo=np.linspace(1,3,len(outer))
ax.scatter(inner[:,0],ri**2,c=SAF,s=90,edgecolor=FG,zorder=3)
ax.scatter(outer[:,0],ro**2,c=TEAL,s=90,edgecolor=FG,zorder=3)
ax.axhline(5.0,color=YEL,lw=2.4,zorder=2)
ax.text(0,5.5,'now ONE flat line splits them!',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
ax.set_title('Lift it up (add "height")\nnow a straight line works',fontsize=11.5,fontweight='bold',color=GRN)
ax.set_xlabel('position'); ax.set_ylabel('height = distance from centre',fontsize=9)
ax.set_xticks([]); ax.set_yticks([])
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/37-kernel-trick.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day11 images generated")
