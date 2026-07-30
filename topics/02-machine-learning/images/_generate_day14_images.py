import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse, Rectangle
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)

# ===== 50: THE SHADOW — a 3D object casts a 2D shadow that still shows what it is =====
fig,ax=plt.subplots(figsize=(8.8,5.0)); fig.patch.set_facecolor(BG); frame(ax)
# light source
ax.scatter(1.0,8.4,s=520,c=YEL,edgecolor=FG,zorder=4)
ax.text(1.0,9.2,'light',ha='center',color=YEL,fontsize=10,fontweight='bold')
# 3D object (a little cube-ish hand drawn as stacked shapes) in the middle
ax.add_patch(FancyBboxPatch((4.0,4.6),1.6,1.6,boxstyle="round,pad=0.02",fc=BLU,ec=FG,lw=1.4,alpha=0.9,zorder=3))
ax.add_patch(FancyBboxPatch((4.5,5.3),1.6,1.6,boxstyle="round,pad=0.02",fc=SAF,ec=FG,lw=1.4,alpha=0.7,zorder=2))
ax.text(4.9,4.0,'3D object\n(many dimensions)',ha='center',color=FG,fontsize=10,fontweight='bold')
# wall on the right
ax.plot([8.6,8.6],[0.6,9.4],color=MUT,lw=3)
ax.text(9.0,5.0,'wall',color=MUT,fontsize=10,rotation=90,va='center')
# shadow on the wall (flat 2D)
ax.add_patch(FancyBboxPatch((8.0,4.4),0.5,2.0,boxstyle="round,pad=0.02",fc='#333',ec=MUT,lw=1.2,zorder=2))
ax.text(7.4,3.4,'flat 2D shadow\n— still shows the shape',ha='center',color=GRN,fontsize=9.5,fontweight='bold')
# light rays
for y0,y1 in [(8.4,6.2),(8.4,4.4)]:
    ax.annotate('',xy=(8.0,y1),xytext=(1.4,8.2),arrowprops=dict(arrowstyle='->',color=YEL,lw=1.1,alpha=0.6))
ax.set_title('PCA = casting a shadow: squish many dimensions to 2, keep the shape',fontsize=12,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/50-shadow.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 51: TOO MANY COLUMNS — a wide table you can't "see" =====
fig,ax=plt.subplots(figsize=(9.0,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
cols=['age','income','height','weight','steps','sleep','heart','...','col 100']
for i,c in enumerate(cols):
    x=0.6+i*1.25
    ax.add_patch(Rectangle((x,6.6),1.1,1.6,fc=CARD,ec=SAF,lw=1.2))
    ax.text(x+0.55,7.4,c,ha='center',va='center',color=SAF,fontsize=9,fontweight='bold')
    for r in range(3):
        ax.add_patch(Rectangle((x,6.6-(r+1)*1.15),1.1,1.0,fc='#2b221c',ec='#3a2f26',lw=0.8))
        ax.text(x+0.55,6.6-(r+1)*1.15+0.5,'·',ha='center',va='center',color=MUT,fontsize=14)
ax.text(6.0,0.6,'100 columns — impossible to SEE the pattern by eye',ha='center',color=YEL,fontsize=11,fontweight='bold')
ax.set_title('The problem: too many columns to picture',fontsize=12.5,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/51-toomany.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 52: THE BEST ANGLE — direction where data spreads the MOST =====
np.random.seed(3)
fig,ax=plt.subplots(figsize=(7.6,6.0)); fig.patch.set_facecolor(BG); frame(ax)
# an elongated data cloud (spreads most along a diagonal)
t=np.random.randn(120)
x=5+t*2.2+np.random.randn(120)*0.5
y=5+t*1.3+np.random.randn(120)*0.5
ax.scatter(x,y,c=BLU,s=45,alpha=0.75,edgecolor='none',zorder=2)
# main direction (PC1) — long yellow arrow along the spread
ax.annotate('',xy=(8.6,7.1),xytext=(1.4,2.9),arrowprops=dict(arrowstyle='->',color=YEL,lw=3))
ax.text(8.2,7.6,'PC1: the direction of\nMOST spread (most info)',color=YEL,fontsize=10.5,fontweight='bold',ha='right')
# second direction (PC2) — short arrow, perpendicular
ax.annotate('',xy=(3.6,6.7),xytext=(5.4,3.9),arrowprops=dict(arrowstyle='->',color=GRN,lw=2))
ax.text(2.6,6.9,'PC2: less spread',color=GRN,fontsize=9.5,fontweight='bold')
ax.set_title('PCA finds the BEST angle: where the data spreads out most',fontsize=12,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/52-bestangle.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 53: BAD ANGLE vs GOOD ANGLE shadow (real projection onto a line) =====
fig,axes=plt.subplots(1,2,figsize=(11,4.8)); fig.patch.set_facecolor(BG)
np.random.seed(1); t=np.linspace(-3,3,70)+np.random.randn(70)*0.3
# same elongated cloud spreading along the 45-degree diagonal
X=t+np.random.randn(70)*0.35; Y=t+np.random.randn(70)*0.35

def project(ax, ux, uy, dotcol, title, tcol):
    frame(ax,(-6,6),(-6,6))
    ax.scatter(X,Y,c=MUT,s=30,alpha=0.35,zorder=1)                 # original cloud (faint)
    # the projection LINE (the wall we cast the shadow on) through origin, direction (ux,uy)
    L=6.5
    ax.plot([-ux*L,ux*L],[-uy*L,uy*L],color=tcol,lw=2.2,ls='--',zorder=2)
    # project each point onto that line; draw the drop line + the shadow dot
    for x,y in zip(X,Y):
        s=x*ux+y*uy                 # scalar projection
        px,py=s*ux,s*uy             # foot on the line = the "shadow"
        ax.plot([x,px],[y,py],color=tcol,lw=0.5,alpha=0.35,zorder=1)
        ax.scatter(px,py,c=dotcol,s=42,zorder=3)
    ax.set_title(title,fontsize=11.5,fontweight='bold',color=tcol)

# BAD: cast onto the line PERPENDICULAR to the spread -> shadows pile into a tiny clump
project(axes[0], -0.707, 0.707, RED, 'BAD angle: shadows pile up —\nlose the shape', RED)
# GOOD: cast onto the line ALONG the spread -> shadows spread out along the line
project(axes[1],  0.707, 0.707, GRN, 'GOOD angle: shadows spread out —\nkeep the shape', GRN)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/53-good-bad.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 54: HOW MUCH SHAPE YOU KEEP — variance explained =====
fig,ax=plt.subplots(figsize=(8.6,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
pcs=['PC1','PC2','PC3','PC4','PC5']
var=[62,28,6,3,1]  # % variance
cum=np.cumsum(var)
x0=1.2
for i,(p,v) in enumerate(zip(pcs,var)):
    x=x0+i*1.7
    ax.add_patch(Rectangle((x,1.8),1.1,v*0.1,fc=(GRN if i<2 else MUT),ec=FG,lw=1.0))
    ax.text(x+0.55,1.8+v*0.1+0.3,f'{v}%',ha='center',color=(GRN if i<2 else MUT),fontsize=10,fontweight='bold')
    ax.text(x+0.55,1.3,p,ha='center',color=FG,fontsize=10,fontweight='bold')
ax.text(5.0,9.2,'PC1 + PC2 keep 62% + 28% = 90% of the shape',ha='center',color=GRN,fontsize=11.5,fontweight='bold')
ax.text(5.0,8.2,'→ throw away PC3-5 (just noise), keep only 2 columns',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
ax.set_title('Keep the few directions that hold most of the shape',fontsize=12.5,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/54-variance.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day14 images generated")
