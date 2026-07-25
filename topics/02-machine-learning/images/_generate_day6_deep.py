import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; GOLD='#E0B265'; MUT='#b3a595'; RED='#e06a6a'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# Gradient descent: rolling down the loss hill to find best weights
fig,ax=plt.subplots(figsize=(8.5,5)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
w=np.linspace(-3,3,200); loss=(w-1)**2+0.4
ax.plot(w,loss,color=TEAL,lw=3)
# steps rolling down
pts=[-2.6,-1.7,-0.9,-0.2,0.4,0.8]
for i,px in enumerate(pts):
    py=(px-1)**2+0.4
    ax.scatter([px],[py],s=110,color=SAF if i<len(pts)-1 else GRN,edgecolor=FG,zorder=5)
    if i>0:
        ppx=pts[i-1]; ppy=(ppx-1)**2+0.4
        ax.annotate('',xy=(px,py),xytext=(ppx,ppy),arrowprops=dict(arrowstyle='->',color=YEL,lw=1.6))
ax.scatter([1],[0.4],s=180,color=GRN,edgecolor=FG,marker='*',zorder=6)
ax.annotate('best weights\n(lowest loss)',xy=(1,0.4),xytext=(1.6,3.2),fontsize=10,color=GRN,ha='center',arrowprops=dict(arrowstyle='->',color=GRN,lw=1.4))
ax.annotate('start (bad guess)',xy=(-2.6,(-2.6-1)**2+0.4),xytext=(-2.2,8.5),fontsize=9.5,color=MUT,ha='center',arrowprops=dict(arrowstyle='->',color=MUT,lw=1.2))
ax.set_title('Gradient Descent — roll downhill to the best weights',fontsize=12,fontweight='bold',color=FG)
ax.set_xlabel('weight value (m)',fontsize=11,fontweight='bold'); ax.set_ylabel('loss (how wrong)',fontsize=11,fontweight='bold')
ax.grid(alpha=0.12,color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/22-gradient-descent.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("gradient descent image generated")
