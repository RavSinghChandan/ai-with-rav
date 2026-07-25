import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
plt.rcParams.update({'text.color':FG})

# Three fruit baskets: pure, half-half, mixed — with Gini scores
fig,ax=plt.subplots(figsize=(11,5)); ax.set_xlim(0,12); ax.set_ylim(0,6.5); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,6.1,'Gini score = how MIXED a basket is (0 = all same, 0.5 = fully mixed)',ha='center',fontsize=13,fontweight='bold',color=FG)

def basket(cx, cy, fruits, label, gini, gcolor):
    ax.add_patch(FancyBboxPatch((cx-1.5,cy-1.3),3.0,2.6,boxstyle="round,pad=0.08",fc=CARD,ec=FG,lw=1.6))
    # draw fruit dots in a grid
    n=len(fruits); cols=3
    for i,col in enumerate(fruits):
        r=i//cols; c=i%cols
        fx=cx-0.85+c*0.85; fy=cy+0.65-r*0.75
        ax.add_patch(Circle((fx,fy),0.28,fc=col,ec=FG,lw=1.2))
    ax.text(cx,cy-1.75,label,ha='center',fontsize=10.5,fontweight='bold',color=FG)
    ax.text(cx,cy-2.4,f'Gini = {gini}',ha='center',fontsize=12,fontweight='bold',color=gcolor)

# pure: 6 mangoes (orange)
basket(2.2,3.5,[SAF]*6,'All mangoes\n(clean!)','0.0',GRN)
# half: 3 mango 3 apple
basket(6.0,3.5,[SAF,SAF,SAF,GRN,GRN,GRN],'Half mango, half apple\n(fully mixed)','0.5',RED)
# mostly mango
basket(9.8,3.5,[SAF,SAF,SAF,SAF,SAF,GRN],'Mostly mangoes\n(a little mixed)','0.28',YEL)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/23-gini.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("simple gini basket image generated")
