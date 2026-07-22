import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
BG='#0d1117'; FG='#e6edf3'; SAF='#FF6B35'; TEAL='#33B5E5'; GRN='#06D6A0'; YEL='#FFD166'
plt.rcParams.update({'text.color':FG})

# IMG: the 7-step ML workflow (a pipeline, like making a dish)
fig,ax=plt.subplots(figsize=(11,7)); ax.set_xlim(0,10); ax.set_ylim(0,16); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(5,15.4,'The Real ML Workflow — 7 steps',ha='center',fontsize=15,fontweight='bold',color=FG)
steps=[
 ('1. COLLECT DATA','gather examples (the raw ingredients)',SAF,13.6),
 ('2. CLEAN & PREP','fix missing values, remove noise',TEAL,11.8),
 ('3. SPLIT','train set (learn) + test set (exam)',GRN,10.0),
 ('4. CHOOSE A MODEL','pick the algorithm (regression, tree...)',YEL,8.2),
 ('5. TRAIN','model.fit() — it learns the pattern',SAF,6.4),
 ('6. EVALUATE','test on unseen data — is it good?',TEAL,4.6),
 ('7. DEPLOY','ship it, predict on real new data',GRN,2.8),
]
for title,sub,c,y in steps:
    ax.add_patch(FancyBboxPatch((2.0,y),6,1.35,boxstyle="round,pad=0.08",fc=c,ec=FG,lw=1.5))
    ax.text(5,y+0.85,title,ha='center',va='center',color='#0d1117',fontsize=12,fontweight='bold')
    ax.text(5,y+0.32,sub,ha='center',va='center',color='#0d1117',fontsize=9)
for y in [13.6,11.8,10.0,8.2,6.4,4.6]:
    ax.add_patch(FancyArrowPatch((5,y),(5,y-0.45),arrowstyle='-|>',mutation_scale=20,lw=2.4,color=FG))
# loop-back arrow from evaluate to model choice
ax.add_patch(FancyArrowPatch((8.0,5.3),(9.2,5.3),arrowstyle='-',lw=1.6,color='#9fb3c8'))
ax.add_patch(FancyArrowPatch((9.2,5.3),(9.2,8.9),arrowstyle='-',lw=1.6,color='#9fb3c8'))
ax.add_patch(FancyArrowPatch((9.2,8.9),(8.0,8.9),arrowstyle='-|>',mutation_scale=16,lw=1.6,color='#9fb3c8'))
ax.text(9.35,7.1,'not good?\nretry',ha='left',va='center',color='#9fb3c8',fontsize=8.5,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/06-ml-workflow.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG: train/test split visual
fig,ax=plt.subplots(figsize=(10,3.2)); ax.set_xlim(0,10); ax.set_ylim(0,3); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(5,2.7,'Train / Test Split — the golden rule',ha='center',fontsize=13,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((0.5,0.7),6.4,1.2,boxstyle="round,pad=0.05",fc=SAF,ec=FG,lw=1.5))
ax.text(3.7,1.3,'TRAINING SET (80%)\nmodel learns from this',ha='center',va='center',color='#0d1117',fontsize=11,fontweight='bold')
ax.add_patch(FancyBboxPatch((7.1,0.7),2.4,1.2,boxstyle="round,pad=0.05",fc=TEAL,ec=FG,lw=1.5))
ax.text(8.3,1.3,'TEST (20%)\nthe exam',ha='center',va='center',color='#0d1117',fontsize=10,fontweight='bold')
ax.text(5,0.25,'Never let the model see the test set while learning — that would be cheating.',ha='center',fontsize=9.5,color='#9fb3c8',style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/07-train-test-split.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day3 images generated")
