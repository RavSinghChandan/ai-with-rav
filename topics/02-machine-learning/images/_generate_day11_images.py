import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
# real GREEN for the second group (was rendering blue before) + a separate blue for the center line
GRN='#5fd06a'     # true green group
CENT='#4EC5E8'    # center line (blue) — distinct from margin
MARG='#FFCF6B'    # margin lines (yellow) — distinct from center
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# two clean, clearly separable groups (orange top-left, green bottom-right)
orange=np.array([[2,6],[2.5,7.5],[3,6.8],[1.8,7.2],[3.3,8],[2.2,8.3],[3.5,7]])
green =np.array([[7,3],[7.8,2.2],[6.6,3.2],[8.2,3.5],[7.2,1.8],[8.5,2.6],[6.9,2.6]])

def plot_groups(ax):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.scatter(orange[:,0],orange[:,1],c=SAF,s=110,edgecolor=FG,zorder=3)
    ax.scatter(green[:,0],green[:,1],c=GRN,s=110,edgecolor=FG,zorder=3)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,10); ax.set_ylim(0,10)

xs=np.linspace(0,10,50)

# ============ IMG 35: THREE panels ============
# panel 1: one clean line that separates them
# panel 2: a DIFFERENT line that also separates them (many are possible)
# panel 3: the BEST line — labelled centre line + labelled margin, distinct colours
fig,axes=plt.subplots(1,3,figsize=(15,4.9)); fig.patch.set_facecolor(BG)
for ax in axes: plot_groups(ax)

# Panel 1: one line works
m1,c1=-1.0,10.0
axes[0].plot(xs,m1*xs+c1,color=CENT,lw=2.4,zorder=2)
axes[0].set_title('One line separates them.\nAll orange on one side, green on the other.',fontsize=11,fontweight='bold',color=FG)

# Panel 2: a DIFFERENT line also works
m2,c2=-1.7,12.3
axes[1].plot(xs,m2*xs+c2,color=MUT,lw=2.4,ls='--',zorder=2)
axes[1].set_title('A DIFFERENT line ALSO works.\nSo which line should we trust?',fontsize=11,fontweight='bold',color=MUT)

# Panel 3: the BEST line with labelled centre + margin
ax=axes[2]
m,c=-1.0,10.0
ax.fill_between(xs,m*xs+c-2.0,m*xs+c+2.0,color=MARG,alpha=0.12,zorder=0)
ax.plot(xs,m*xs+c,color=CENT,lw=2.8,zorder=2)                 # centre line (blue)
ax.plot(xs,m*xs+c+2.0,color=MARG,lw=1.8,ls='--',zorder=1)     # margin (yellow)
ax.plot(xs,m*xs+c-2.0,color=MARG,lw=1.8,ls='--',zorder=1)
ax.annotate('',xy=(6.3,5.7),xytext=(4.3,3.7),arrowprops=dict(arrowstyle='<->',color=MARG,lw=2.0))
# labels in their own colours
ax.text(0.4,3.0,'CENTRE line\n(the decision boundary)',color=CENT,fontsize=9.5,fontweight='bold')
ax.text(6.4,7.8,'MARGIN\n(the safety gap)',color=MARG,fontsize=9.5,fontweight='bold')
ax.set_title('The BEST line: widest gap on both sides',fontsize=11,fontweight='bold',color=YEL)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/35-best-line.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ============ IMG 36: name the 3 words — Support Vector, Margin, Machine ============
fig,ax=plt.subplots(figsize=(9.4,6.6)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
m,c=-1.0,10.0
def onmarg(x,side): return m*x+c+2.0*side   # y on upper(+1)/lower(-1) margin

# non-support orange points, comfortably ABOVE the upper margin (their own side, not on the edge)
orange_far=np.array([[1.6,8.9],[2.6,8.9],[1.4,7.6],[3.2,9.3],[2.0,9.8]])
# non-support green points, comfortably BELOW the lower margin
green_far =np.array([[7.2,1.4],[8.2,1.6],[6.9,0.9],[8.7,2.3],[7.9,0.8]])
ax.fill_between(xs,m*xs+c-2.0,m*xs+c+2.0,color=MARG,alpha=0.12,zorder=0)
ax.plot(xs,m*xs+c,color=CENT,lw=3.0,zorder=2)              # the MACHINE's line
ax.plot(xs,m*xs+c+2.0,color=MARG,lw=1.8,ls='--',zorder=1)  # margin edges
ax.plot(xs,m*xs+c-2.0,color=MARG,lw=1.8,ls='--',zorder=1)
ax.scatter(orange_far[:,0],orange_far[:,1],c=SAF,s=120,edgecolor=FG,zorder=3)
ax.scatter(green_far[:,0],green_far[:,1],c=GRN,s=120,edgecolor=FG,zorder=3)

# the SUPPORT VECTORS: exactly ON the margin edges, red-ringed
sv1=(3.0,onmarg(3.0,+1))   # orange, on upper margin
sv2=(2.0,onmarg(2.0,+1))   # orange, on upper margin
sv3=(7.0,onmarg(7.0,-1))   # green, on lower margin
ax.scatter([sv1[0],sv2[0]],[sv1[1],sv2[1]],c=SAF,s=190,edgecolor=RED,linewidth=2.8,zorder=5)
ax.scatter([sv3[0]],[sv3[1]],c=GRN,s=190,edgecolor=RED,linewidth=2.8,zorder=5)

# MARGIN: double-headed arrow straight across the band (from lower edge to upper edge at x=5)
xm=5.0
ax.annotate('',xy=(xm,onmarg(xm,+1)),xytext=(xm,onmarg(xm,-1)),
            arrowprops=dict(arrowstyle='<->',color=MARG,lw=2.4))
ax.text(xm+0.2,(m*xm+c),'MARGIN\n= the gap width',color=MARG,fontsize=10.5,fontweight='bold',va='center',ha='left')

# SUPPORT VECTOR label (top-left, short arrow to sv2)
ax.annotate('SUPPORT VECTORS\n(edge points that hold the line)',
            xy=sv2,xytext=(0.3,3.2),color=RED,fontsize=10,fontweight='bold',
            arrowprops=dict(arrowstyle='->',color=RED,lw=1.7,connectionstyle='arc3,rad=-0.2'))
ax.annotate('',xy=sv3,xytext=(3.4,2.9),
            arrowprops=dict(arrowstyle='->',color=RED,lw=1.7,connectionstyle='arc3,rad=0.2'))

# MACHINE label (right side, arrow to centre line)
lx=8.2
ax.annotate('the MACHINE\n(the line it learns)',
            xy=(lx,m*lx+c),xytext=(5.6,8.6),color=CENT,fontsize=10,fontweight='bold',
            arrowprops=dict(arrowstyle='->',color=CENT,lw=1.7))
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,10); ax.set_ylim(0,10)
ax.set_title('S-V-M in one picture: Support Vectors + Margin + the Machine',fontsize=12,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/36-support-vectors.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ============ IMG 37: kernel trick (fix green colour too) ============
fig,axes=plt.subplots(1,2,figsize=(11,4.9)); fig.patch.set_facecolor(BG)
ang=np.linspace(0,2*np.pi,14,endpoint=False)
inner=np.c_[1.3*np.cos(ang),1.3*np.sin(ang)]
outer=np.c_[3.3*np.cos(ang),3.3*np.sin(ang)]
ax=axes[0]; ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
ax.scatter(inner[:,0],inner[:,1],c=SAF,s=90,edgecolor=FG,zorder=3)
ax.scatter(outer[:,0],outer[:,1],c=GRN,s=90,edgecolor=FG,zorder=3)
ax.set_title('A straight line CANNOT split\nthis (orange inside, green ring)',fontsize=11.5,fontweight='bold',color=RED)
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(-4.2,4.2); ax.set_ylim(-4.2,4.2); ax.set_aspect('equal')
ax=axes[1]; ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
ri=np.linalg.norm(inner,axis=1); ro=np.linalg.norm(outer,axis=1)
ax.scatter(inner[:,0],ri**2,c=SAF,s=90,edgecolor=FG,zorder=3)
ax.scatter(outer[:,0],ro**2,c=GRN,s=90,edgecolor=FG,zorder=3)
ax.axhline(5.0,color=MARG,lw=2.4,zorder=2)
ax.text(0,5.5,'now ONE flat line splits them!',ha='center',color=MARG,fontsize=10.5,fontweight='bold')
ax.set_title('Lift it up (add "height")\nnow a straight line works',fontsize=11.5,fontweight='bold',color=GRN)
ax.set_xlabel('position'); ax.set_ylabel('height = distance from centre',fontsize=9)
ax.set_xticks([]); ax.set_yticks([])
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/37-kernel-trick.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ============ IMG 38: picking C — small C (wide, forgiving) vs large C (thin, strict) ============
fig,axes=plt.subplots(1,2,figsize=(11,4.9)); fig.patch.set_facecolor(BG)
# same two groups but with ONE orange "troublemaker" sitting deep in green territory
og=np.array([[2,7],[2.6,7.6],[3,6.9],[1.9,7.3],[3.3,8],[2.3,8.2]])
gr=np.array([[7,3],[7.8,2.3],[6.6,3.2],[8.2,3.4],[7.2,1.9],[8.4,2.6]])
noise=np.array([[6.2,4.0]])   # an orange point sitting on the green side
for ax in axes:
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.scatter(og[:,0],og[:,1],c=SAF,s=100,edgecolor=FG,zorder=3)
    ax.scatter(gr[:,0],gr[:,1],c=GRN,s=100,edgecolor=FG,zorder=3)
    ax.scatter(noise[:,0],noise[:,1],c=SAF,s=140,edgecolor=RED,linewidth=2.4,zorder=4)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,10); ax.set_ylim(0,10)
# LEFT small C: wide margin, ignores the troublemaker
ax=axes[0]; m,c=-1.0,10.0
ax.fill_between(xs,m*xs+c-2.2,m*xs+c+2.2,color=MARG,alpha=0.12)
ax.plot(xs,m*xs+c,color=CENT,lw=2.6); ax.plot(xs,m*xs+c+2.2,color=MARG,lw=1.5,ls='--'); ax.plot(xs,m*xs+c-2.2,color=MARG,lw=1.5,ls='--')
ax.set_title('SMALL C = WIDE, forgiving margin\n(ignores the odd troublemaker)',fontsize=11,fontweight='bold',color=GRN)
ax.text(0.4,1.0,'wider gap = safer on new data',color=GRN,fontsize=9.5,fontweight='bold')
# RIGHT large C: thin margin, bends to catch the troublemaker
ax=axes[1]; m2,c2=-1.35,11.4
ax.fill_between(xs,m2*xs+c2-0.7,m2*xs+c2+0.7,color=MARG,alpha=0.12)
ax.plot(xs,m2*xs+c2,color=CENT,lw=2.6); ax.plot(xs,m2*xs+c2+0.7,color=MARG,lw=1.5,ls='--'); ax.plot(xs,m2*xs+c2-0.7,color=MARG,lw=1.5,ls='--')
ax.set_title('LARGE C = THIN, strict margin\n(bends to get every point right)',fontsize=11,fontweight='bold',color=RED)
ax.text(0.4,1.0,'thinner gap = can overfit noise',color=RED,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/38-picking-c.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day11 images regenerated")
