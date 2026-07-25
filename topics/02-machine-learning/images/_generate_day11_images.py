import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'      # true green village
ROAD='#4EC5E8'     # the road / decision boundary (blue)
MARG='#FFCF6B'     # margin edges (yellow)
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# ONE shared, simple, clearly-separable layout: orange top-left village, green bottom-right village
orange=np.array([[2,7.4],[3,8.2],[2.6,6.6],[3.6,7.4],[1.7,8.0]])
green =np.array([[7,2.8],[8,3.4],[6.6,2.0],[7.6,1.8],[8.4,2.6]])

def village(ax,show=True):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    if show:
        ax.scatter(orange[:,0],orange[:,1],c=SAF,s=170,edgecolor=FG,zorder=3)
        ax.scatter(green[:,0],green[:,1],c=GRN,s=170,edgecolor=FG,zorder=3)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,10); ax.set_ylim(0,10)
xs=np.linspace(0,10,50)

# ===== 35: TWO VILLAGES + MANY ROADS — which is best? =====
fig,ax=plt.subplots(figsize=(8.4,5.4)); fig.patch.set_facecolor(BG)
village(ax)
for (m,c) in [(-1.0,10.0),(-1.7,12.4),(-0.65,8.0)]:
    ax.plot(xs,m*xs+c,color=MUT,lw=1.8,ls='--',alpha=0.9)
ax.text(2.1,9.2,'Orange Village',color=SAF,fontsize=11,fontweight='bold')
ax.text(6.0,0.9,'Green Village',color=GRN,fontsize=11,fontweight='bold')
ax.set_title('Two villages. MANY roads can separate them.\nWhich road is best?',fontsize=13,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/35-many-roads.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 36: THE MAXIMUM MARGIN — the widest safe road =====
fig,ax=plt.subplots(figsize=(8.4,5.4)); fig.patch.set_facecolor(BG)
village(ax)
m,c=-1.0,10.0
ax.fill_between(xs,m*xs+c-2.0,m*xs+c+2.0,color=MARG,alpha=0.13,zorder=0)
ax.plot(xs,m*xs+c,color=ROAD,lw=3.2,zorder=2)
ax.plot(xs,m*xs+c+2.0,color=MARG,lw=1.8,ls='--',zorder=1)
ax.plot(xs,m*xs+c-2.0,color=MARG,lw=1.8,ls='--',zorder=1)
# one clean margin arrow across the band
xm=5.0
ax.annotate('',xy=(xm,m*xm+c+2.0),xytext=(xm,m*xm+c-2.0),arrowprops=dict(arrowstyle='<->',color=MARG,lw=2.4))
ax.text(xm+0.25,m*xm+c,'MARGIN\n(safety gap)',color=MARG,fontsize=11,fontweight='bold',va='center')
ax.text(0.3,1.4,'THE BEST ROAD\n= widest gap from both villages',color=ROAD,fontsize=11,fontweight='bold')
ax.set_title('SVM picks the road with the BIGGEST safety gap',fontsize=13,fontweight='bold',color=YEL)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/36-margin.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 37: SUPPORT VECTORS — only the nearest houses matter =====
fig,ax=plt.subplots(figsize=(8.4,5.4)); fig.patch.set_facecolor(BG)
village(ax)
ax.set_ylim(0,11)   # extra headroom so the top star clears the title
m,c=-1.0,10.0
ax.fill_between(xs,m*xs+c-2.0,m*xs+c+2.0,color=MARG,alpha=0.10,zorder=0)
ax.plot(xs,m*xs+c,color=ROAD,lw=3.0,zorder=2)
ax.plot(xs,m*xs+c+2.0,color=MARG,lw=1.5,ls='--',zorder=1)
ax.plot(xs,m*xs+c-2.0,color=MARG,lw=1.5,ls='--',zorder=1)
# the two nearest houses = support vectors, sitting on the margin edges, marked with a STAR
sv_o=(2.6,m*2.6+c+2.0)   # nearest orange, on upper margin
sv_g=(7.0,m*7.0+c-2.0)   # nearest green, on lower margin
ax.scatter([sv_o[0]],[sv_o[1]],marker='*',c=SAF,s=680,edgecolor=RED,linewidth=2.4,zorder=6)
ax.scatter([sv_g[0]],[sv_g[1]],marker='*',c=GRN,s=680,edgecolor=RED,linewidth=2.4,zorder=6)
ax.annotate('SUPPORT VECTOR\n(nearest house)',xy=sv_o,xytext=(3.6,9.6),color=RED,fontsize=10.5,fontweight='bold',
            ha='left',arrowprops=dict(arrowstyle='->',color=RED,lw=1.7))
ax.annotate('SUPPORT VECTOR\n(nearest house)',xy=sv_g,xytext=(7.5,4.6),color=RED,fontsize=10.5,fontweight='bold',
            ha='left',arrowprops=dict(arrowstyle='->',color=RED,lw=1.7,connectionstyle='arc3,rad=0.2'))
ax.text(0.3,0.6,'The far houses don\'t matter. Remove them — the road stays.',color=MUT,fontsize=9.5,style='italic')
ax.set_title('Only the NEAREST houses decide the road\n= Support Vectors',fontsize=13,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/37-support-vectors.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 38: KERNEL TRICK — bend the paper into a bowl =====
fig,axes=plt.subplots(1,2,figsize=(11,4.8)); fig.patch.set_facecolor(BG)
ang=np.linspace(0,2*np.pi,12,endpoint=False)
ring=np.c_[3.0*np.cos(ang),3.0*np.sin(ang)]        # green ring (outside)
centre=np.array([[0,0],[0.9,0.4],[-0.6,0.5],[0.3,-0.7]])  # orange centre (inside)
ax=axes[0]; ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
ax.scatter(ring[:,0],ring[:,1],c=GRN,s=130,edgecolor=FG,zorder=3)
ax.scatter(centre[:,0],centre[:,1],c=SAF,s=170,edgecolor=FG,zorder=3)
ax.set_title('Flat paper: a straight line\nCANNOT separate them',fontsize=12,fontweight='bold',color=RED)
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(-4,4); ax.set_ylim(-4,4); ax.set_aspect('equal')
# right: bend into a bowl -> centre pops up -> flat plane separates
ax=axes[1]; ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
rr=np.linalg.norm(ring,axis=1); rc=np.linalg.norm(centre,axis=1)
ax.scatter(ring[:,0],9-rr**2*0.9,c=GRN,s=130,edgecolor=FG,zorder=3)   # ring stays LOW
ax.scatter(centre[:,0],9-rc**2*0.9,c=SAF,s=170,edgecolor=FG,zorder=3) # centre pops HIGH
ax.axhline(6.0,color=ROAD,lw=2.6,zorder=2)
ax.text(0,6.5,'now a flat line separates them!',ha='center',color=ROAD,fontsize=11,fontweight='bold')
ax.set_title('Bend the paper into a bowl:\nthe centre pops UP',fontsize=12,fontweight='bold',color=GRN)
ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(-4,4); ax.set_ylim(0,10)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/38-kernel-trick.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 39: PICKING C — wide/forgiving vs thin/strict =====
fig,axes=plt.subplots(1,2,figsize=(11,4.8)); fig.patch.set_facecolor(BG)
og=np.array([[2,7.4],[3,8.2],[2.6,6.6],[3.6,7.4],[1.7,8.0]])
gr=np.array([[7,2.8],[8,3.4],[6.6,2.0],[7.6,1.8],[8.4,2.6]])
noise=np.array([[6.0,4.2]])   # an orange troublemaker in green territory
for ax in axes:
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.scatter(og[:,0],og[:,1],c=SAF,s=120,edgecolor=FG,zorder=3)
    ax.scatter(gr[:,0],gr[:,1],c=GRN,s=120,edgecolor=FG,zorder=3)
    ax.scatter(noise[:,0],noise[:,1],c=SAF,s=150,edgecolor=RED,linewidth=2.4,zorder=4)
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(0,10); ax.set_ylim(0,10)
ax=axes[0]; m,c=-1.0,10.0
ax.fill_between(xs,m*xs+c-2.2,m*xs+c+2.2,color=MARG,alpha=0.12)
ax.plot(xs,m*xs+c,color=ROAD,lw=2.6); ax.plot(xs,m*xs+c+2.2,color=MARG,lw=1.5,ls='--'); ax.plot(xs,m*xs+c-2.2,color=MARG,lw=1.5,ls='--')
ax.set_title('SMALL C = WIDE, forgiving road\n(ignores one troublemaker)',fontsize=11.5,fontweight='bold',color=GRN)
ax=axes[1]; m2,c2=-1.35,11.4
ax.fill_between(xs,m2*xs+c2-0.7,m2*xs+c2+0.7,color=MARG,alpha=0.12)
ax.plot(xs,m2*xs+c2,color=ROAD,lw=2.6); ax.plot(xs,m2*xs+c2+0.7,color=MARG,lw=1.5,ls='--'); ax.plot(xs,m2*xs+c2-0.7,color=MARG,lw=1.5,ls='--')
ax.set_title('LARGE C = THIN, strict road\n(bends to catch every point)',fontsize=11.5,fontweight='bold',color=RED)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/39-picking-c.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day11 simple diagrams generated")
