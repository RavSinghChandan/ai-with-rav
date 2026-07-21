import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
BG='#0d1117'; FG='#e6edf3'; SAF='#FF6B35'; TEAL='#33B5E5'; GRN='#06D6A0'; YEL='#FFD166'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# IMG 1: the 3 families (like 3 ways a child learns)
fig,ax=plt.subplots(figsize=(12,5.2)); ax.set_xlim(0,24); ax.set_ylim(0,10); ax.axis('off'); fig.patch.set_facecolor(BG)
def box(x,y,w,h,txt,c,tc='#0d1117',fs=11):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.1",fc=c,ec=FG,lw=1.6))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',color=tc,fontsize=fs,fontweight='bold')
ax.text(12,9.4,'The 3 Families of Machine Learning',ha='center',fontsize=15,fontweight='bold',color=FG)
cols=[(SAF,'SUPERVISED','Learn with a TEACHER','Data has ANSWERS (labels)','e.g. spam / not-spam,\nhouse price prediction',1.2),
      (TEAL,'UNSUPERVISED','Learn by EXPLORING','Data has NO answers','e.g. customer groups,\ntopic discovery',8.5),
      (GRN,'REINFORCEMENT','Learn by REWARD','Trial, error, feedback','e.g. game AI, robotics,\nChatGPT (RLHF)',15.8)]
for c,title,sub,mid,ex,x in cols:
    box(x,6.6,7,1.5,title,c,fs=13)
    ax.text(x+3.5,5.9,sub,ha='center',fontsize=11,fontweight='bold',color=c)
    ax.add_patch(FancyBboxPatch((x,3.9),7,1.4,boxstyle="round,pad=0.1",fc='#161b22',ec=FG,lw=1))
    ax.text(x+3.5,4.6,mid,ha='center',va='center',fontsize=10,color=FG)
    ax.text(x+3.5,2.7,ex,ha='center',va='center',fontsize=9.5,color='#9fb3c8',style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/04-three-families.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 2: supervised = labelled data visual (dots with labels vs unlabelled)
fig,axes=plt.subplots(1,2,figsize=(11,4.6)); fig.patch.set_facecolor(BG)
np.random.seed(3)
for ax,title,labelled in [(axes[0],'SUPERVISED: data has labels',True),(axes[1],'UNSUPERVISED: no labels, find groups',False)]:
    ax.set_facecolor('#161b22')
    for s in ax.spines.values(): s.set_color('#30363d')
    a=np.random.randn(15,2)*0.6+[2,2]; b=np.random.randn(15,2)*0.6+[5,5]
    if labelled:
        ax.scatter(a[:,0],a[:,1],c=SAF,s=90,edgecolor=FG,label='Class A (given)')
        ax.scatter(b[:,0],b[:,1],c=TEAL,s=90,edgecolor=FG,label='Class B (given)')
        ax.legend(fontsize=9,facecolor='#161b22',edgecolor='#30363d',labelcolor=FG)
    else:
        allp=np.vstack([a,b]); ax.scatter(allp[:,0],allp[:,1],c=YEL,s=90,edgecolor=FG,label='All same color\n(machine finds groups)')
        ax.legend(fontsize=9,facecolor='#161b22',edgecolor='#30363d',labelcolor=FG)
    ax.set_title(title,color=FG,fontsize=11,fontweight='bold'); ax.set_xticks([]); ax.set_yticks([])
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/05-supervised-vs-unsupervised.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day2 images generated")
