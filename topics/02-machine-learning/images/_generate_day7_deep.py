import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# Gini impurity: how "mixed" a group is. Pure=0, 50/50=0.5
fig,ax=plt.subplots(figsize=(8.5,5)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
p=np.linspace(0,1,200); gini=1-(p**2+(1-p)**2)
ax.plot(p,gini,color=TEAL,lw=3)
ax.scatter([0,1],[0,0],s=140,color=GRN,edgecolor=FG,zorder=5)
ax.scatter([0.5],[0.5],s=160,color=RED,edgecolor=FG,zorder=5)
ax.annotate('all one class\n= PURE (Gini 0)',xy=(0,0),xytext=(0.15,0.18),fontsize=10,color=GRN,ha='center',arrowprops=dict(arrowstyle='->',color=GRN,lw=1.3))
ax.annotate('50/50 mix\n= WORST (Gini 0.5)',xy=(0.5,0.5),xytext=(0.5,0.32),fontsize=10,color=RED,ha='center',arrowprops=dict(arrowstyle='->',color=RED,lw=1.3))
ax.set_title('Gini impurity — how "mixed up" a group is',fontsize=12,fontweight='bold',color=FG)
ax.set_xlabel('fraction of class A in the group',fontsize=11,fontweight='bold'); ax.set_ylabel('Gini (messiness)',fontsize=11,fontweight='bold')
ax.grid(alpha=0.12,color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/23-gini.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("gini image generated")
