import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
plt.rcParams.update({'text.color':FG})

def draw_basket(ax,cx,cy,fruits,w=2.6,h=2.2):
    ax.add_patch(FancyBboxPatch((cx-w/2,cy-h/2),w,h,boxstyle="round,pad=0.08",fc=CARD,ec=FG,lw=1.5))
    cols=3
    for i,col in enumerate(fruits):
        r=i//cols; c=i%cols
        fx=cx-0.72+c*0.72; fy=cy+0.5-r*0.62
        ax.add_patch(Circle((fx,fy),0.24,fc=col,ec=FG,lw=1.1))

# ---- IMG A: the Gini formula shown on the half-half basket ----
fig,ax=plt.subplots(figsize=(11,4.8)); ax.set_xlim(0,12); ax.set_ylim(0,6); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,5.6,'The Gini formula — on our half-and-half basket',ha='center',fontsize=13,fontweight='bold',color=FG)
draw_basket(ax,2.3,3.2,[SAF,SAF,SAF,GRN,GRN,GRN])
ax.text(2.3,1.7,'3 orange, 3 green',ha='center',fontsize=10,color=FG,fontweight='bold')
# the formula worked out, step by step, to the right
ax.text(5.0,4.2,'Gini = 1',ha='left',fontsize=15,color=SAF,fontweight='bold')
ax.text(5.0,3.3,'− (chance of orange)²',ha='left',fontsize=13,color=SAF)
ax.text(5.0,2.5,'− (chance of green)²',ha='left',fontsize=13,color=SAF)
ax.text(5.0,1.5,'= 1 − (½)² − (½)²  =  0.5',ha='left',fontsize=14,color=YEL,fontweight='bold')
# annotate the ½
ax.annotate('half are orange\nso chance = ½',xy=(7.4,3.3),xytext=(9.3,4.2),fontsize=9.5,color=TEAL,ha='center',arrowprops=dict(arrowstyle='->',color=TEAL,lw=1.2))
ax.text(6,0.5,'Fully mixed basket → Gini 0.5 (the worst). A clean basket would give 0.',ha='center',fontsize=9.5,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/24-gini-formula.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ---- IMG B: how it chooses — messy basket splits into 2 cleaner baskets ----
fig,ax=plt.subplots(figsize=(11,5))
ax.set_xlim(0,12); ax.set_ylim(0,7); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,6.6,'How the tree chooses: pick the question that makes cleaner baskets',ha='center',fontsize=13,fontweight='bold',color=FG)
# before: one messy basket
draw_basket(ax,2.3,4.0,[SAF,GRN,SAF,GRN,SAF,GRN])
ax.text(2.3,2.4,'BEFORE\nmixed (Gini 0.5)',ha='center',fontsize=10,color=RED,fontweight='bold')
# question box
ax.add_patch(FancyBboxPatch((4.7,3.3),2.2,1.3,boxstyle="round,pad=0.06",fc=YEL,ec=FG,lw=1.4))
ax.text(5.8,3.95,'Is it\norange?',ha='center',va='center',color='#1a1512',fontsize=11,fontweight='bold')
ax.add_patch(FancyArrowPatch((3.7,4.0),(4.7,4.0),arrowstyle='-|>',mutation_scale=18,lw=2,color=FG))
# after: two clean baskets
draw_basket(ax,9.2,5.2,[SAF,SAF,SAF],w=2.2,h=1.7)
ax.text(9.2,4.05,'all orange (Gini 0) ✔',ha='center',fontsize=9.5,color=GRN,fontweight='bold')
draw_basket(ax,9.2,2.3,[GRN,GRN,GRN],w=2.2,h=1.7)
ax.text(9.2,1.15,'all green (Gini 0) ✔',ha='center',fontsize=9.5,color=GRN,fontweight='bold')
ax.add_patch(FancyArrowPatch((6.9,4.3),(8.1,5.2),arrowstyle='-|>',mutation_scale=16,lw=1.8,color=GRN))
ax.add_patch(FancyArrowPatch((6.9,3.7),(8.1,2.3),arrowstyle='-|>',mutation_scale=16,lw=1.8,color=GRN))
ax.text(6,0.3,'A good question turns one messy basket into two clean ones. That drop in mess = "information gain".',ha='center',fontsize=9.5,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/25-how-it-chooses.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("2 more day7 diagrams generated")
