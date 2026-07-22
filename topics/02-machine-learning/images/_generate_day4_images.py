import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
BG='#0d1117'; FG='#e6edf3'; SAF='#FF6B35'; TEAL='#33B5E5'; GRN='#06D6A0'; YEL='#FFD166'; MUT='#9fb3c8'
plt.rcParams.update({'text.color':FG})

# IMG 1: a data table — features (X) vs label (y)
fig,ax=plt.subplots(figsize=(11,4.6)); ax.set_xlim(0,12); ax.set_ylim(0,8); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,7.4,'A dataset = rows of examples, columns of features + 1 label',ha='center',fontsize=13,fontweight='bold',color=FG)
# header
cols=['Temp (°C)','Day','Festival?','  →  ','Cups sold']
xs=[0.5,3.0,5.3,7.6,8.6]; ws=[2.3,2.1,2.1,0.9,3.0]
colors=[TEAL,TEAL,TEAL,None,SAF]
for c,x,w,col in zip(cols,xs,ws,colors):
    if col:
        ax.add_patch(FancyBboxPatch((x,5.8),w,0.9,boxstyle="round,pad=0.03",fc=col,ec=FG,lw=1.2))
        ax.text(x+w/2,6.25,c,ha='center',va='center',color='#0d1117',fontsize=10,fontweight='bold')
    else:
        ax.text(x+w/2,6.25,c,ha='center',va='center',color=MUT,fontsize=13)
rows=[['18','Mon','No','','182'],['32','Sat','No','','95'],['25','Fri','Yes','','210'],['15','Sun','No','','200']]
for r,row in enumerate(rows):
    y=4.9-r*0.95
    for val,x,w,col in zip(row,xs,ws,colors):
        if col is None: 
            ax.text(x+w/2,y+0.35,'→',ha='center',va='center',color=MUT,fontsize=12); continue
        fc='#161b22' if col==TEAL else '#3a1e10'
        ax.add_patch(FancyBboxPatch((x,y),w,0.75,boxstyle="round,pad=0.02",fc=fc,ec='#30363d',lw=0.8))
        ax.text(x+w/2,y+0.37,val,ha='center',va='center',color=FG,fontsize=10)
ax.text(3.2,0.3,'FEATURES (X) — the inputs the machine looks at',ha='center',fontsize=10,color=TEAL,fontweight='bold')
ax.text(10.1,0.3,'LABEL (y) — the answer',ha='center',fontsize=10,color=SAF,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/08-features-vs-label.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 2: garbage in garbage out
fig,ax=plt.subplots(figsize=(10,3.4)); ax.set_xlim(0,10); ax.set_ylim(0,3); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(5,2.7,'Garbage In → Garbage Out',ha='center',fontsize=14,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((0.4,0.9),2.6,1.1,boxstyle="round,pad=0.05",fc='#5a2020',ec=FG,lw=1.4))
ax.text(1.7,1.45,'Messy data\n(typos, gaps,\nwrong units)',ha='center',va='center',color=FG,fontsize=9.5,fontweight='bold')
ax.add_patch(FancyBboxPatch((3.7,0.9),2.6,1.1,boxstyle="round,pad=0.05",fc=TEAL,ec=FG,lw=1.4))
ax.text(5.0,1.45,'Same model',ha='center',va='center',color='#0d1117',fontsize=11,fontweight='bold')
ax.add_patch(FancyBboxPatch((7.0,0.9),2.6,1.1,boxstyle="round,pad=0.05",fc='#5a2020',ec=FG,lw=1.4))
ax.text(8.3,1.45,'Bad predictions\n(useless)',ha='center',va='center',color=FG,fontsize=9.5,fontweight='bold')
ax.add_patch(FancyArrowPatch((3.0,1.45),(3.7,1.45),arrowstyle='-|>',mutation_scale=18,lw=2,color=FG))
ax.add_patch(FancyArrowPatch((6.3,1.45),(7.0,1.45),arrowstyle='-|>',mutation_scale=18,lw=2,color=FG))
ax.text(5,0.35,'The best algorithm cannot fix bad data. Clean data beats a clever model.',ha='center',fontsize=9.5,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/09-garbage-in-out.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day4 images generated")
