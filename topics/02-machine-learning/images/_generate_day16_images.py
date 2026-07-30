import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)

# ===== 60: ONE TEST IS RISKY — a single split can be lucky/unlucky =====
fig,ax=plt.subplots(figsize=(9.0,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('One test can be lucky or unlucky — not enough to trust',fontsize=12.5,fontweight='bold',color=FG)
# a row of data blocks, one chunk marked TEST
for i in range(10):
    col=YEL if i==7 else BLU
    ax.add_patch(Rectangle((0.6+i*1.05,5.4),0.95,2.2,fc=col,ec=FG,lw=1.2,alpha=0.9))
ax.text(0.6+7*1.05+0.47,6.5,'TEST',ha='center',va='center',color='#1a1512',fontsize=9,fontweight='bold',rotation=90)
ax.text(0.6+3*1.05,4.7,'train on these',color=BLU,fontsize=10,fontweight='bold')
ax.text(0.6+7*1.05,8.0,'the ONE test chunk',ha='center',color=YEL,fontsize=10,fontweight='bold')
ax.text(6.0,2.6,'What if this one chunk happened to be easy (lucky)\nor really hard (unlucky)? Your score could fool you.',
        ha='center',color=RED,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/60-one-test.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 61: K-FOLD CROSS-VALIDATION — rotate the test fold, average =====
fig,ax=plt.subplots(figsize=(9.4,5.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Cross-validation: 5 mock tests, then AVERAGE the scores',fontsize=12.5,fontweight='bold',color=FG)
K=5; scores=[88,85,90,84,87]
for row in range(K):
    y=8.2-row*1.5
    for col in range(K):
        c=YEL if col==row else BLU
        ax.add_patch(Rectangle((1.2+col*1.3,y),1.15,1.1,fc=c,ec=FG,lw=1.0,alpha=0.9))
    ax.text(0.9,y+0.55,f'Round {row+1}',ha='right',va='center',color=FG,fontsize=9.5,fontweight='bold')
    ax.text(1.2+row*1.3+0.57,y+0.55,'test',ha='center',va='center',color='#1a1512',fontsize=8,fontweight='bold')
    ax.text(8.2,y+0.55,f'score {scores[row]}%',va='center',color=MUT,fontsize=9.5)
ax.text(3.7,0.9,'yellow = the test fold (rotates each round) · blue = train',ha='center',color=MUT,fontsize=9.5)
ax.text(9.6,4.6,f'AVERAGE\n= {int(np.mean(scores))}%\n(reliable!)',ha='center',color=GRN,fontsize=12,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/61-kfold.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 62: BIAS vs VARIANCE — the dartboard =====
fig,axes=plt.subplots(1,2,figsize=(10.6,5.6)); fig.patch.set_facecolor(BG)
np.random.seed(4)
def dartboard(ax,cx,cy,spread,title,col):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(-3,3); ax.set_ylim(-3,3); ax.set_aspect('equal')
    for r,c in [(2.4,'#3a2f26'),(1.6,'#463124'),(0.8,'#5a3d28')]:
        ax.add_patch(Circle((0,0),r,fc=c,ec='none',zorder=1))
    ax.add_patch(Circle((0,0),0.28,fc=GRN,ec=FG,lw=1,zorder=2))  # bullseye = truth
    px=cx+np.random.randn(8)*spread; py=cy+np.random.randn(8)*spread
    ax.scatter(px,py,c=col,s=70,edgecolor=FG,zorder=4)
    ax.set_title(title,fontsize=12,fontweight='bold',color=col)
# left: HIGH BIAS — shots clustered but OFF-centre (consistently wrong)
dartboard(axes[0],1.5,-1.2,0.28,'HIGH BIAS\n(tight, but WRONG spot)',RED)
axes[0].text(0,-2.9,'too simple → underfit',ha='center',color=RED,fontsize=9.5,fontweight='bold')
# right: HIGH VARIANCE — shots scattered all around (swingy)
dartboard(axes[1],0.1,0.1,1.25,'HIGH VARIANCE\n(scattered everywhere)',YEL)
axes[1].text(0,-2.9,'too sensitive → overfit',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
fig.suptitle('Bias = consistently off · Variance = wildly scattered  (green centre = the truth)',
             fontsize=12,fontweight='bold',color=FG,y=1.02)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/62-dartboard.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 63: THE TRADEOFF CURVE — bias down, variance up, total U =====
fig,ax=plt.subplots(figsize=(8.8,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
cx=np.linspace(0.6,9.4,100)
bias2=7.5*np.exp(-cx*0.5)+0.3          # bias falls as complexity rises
var=0.35*np.exp(cx*0.32)              # variance rises
total=bias2+var+0.4
ax.plot(cx,bias2,color=BLU,lw=2.4,label='bias (too simple)')
ax.plot(cx,var,color=YEL,lw=2.4,label='variance (too sensitive)')
ax.plot(cx,total,color=RED,lw=3,label='total error')
mi=int(np.argmin(total))
ax.scatter([cx[mi]],[total[mi]],s=340,facecolor='none',edgecolor=GRN,lw=2.6,zorder=5)
ax.annotate('sweet spot\n(balanced)',xy=(cx[mi],total[mi]),xytext=(cx[mi]+1.2,total[mi]+2.2),
            color=GRN,fontsize=10.5,fontweight='bold',arrowprops=dict(arrowstyle='->',color=GRN,lw=1.8))
ax.set_xlabel('model complexity  →',color=FG,fontsize=10.5)
ax.set_ylabel('error',color=FG,fontsize=10.5)
leg=ax.legend(fontsize=9.5,facecolor=CARD,edgecolor='#3a2f26',loc='upper center')
for tx in leg.get_texts(): tx.set_color(FG)
ax.set_title('The tradeoff: less bias means more variance — balance them',fontsize=12,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/63-tradeoff.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 64: THE PRO WORKFLOW =====
fig,ax=plt.subplots(figsize=(9.4,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('How the pros find the sweet spot every time',fontsize=12.5,fontweight='bold',color=FG)
steps=[('1','Try a few settings\n(e.g. tree depth 2,4,6,8)',SAF),
       ('2','Cross-validate EACH\n(5-fold average score)',BLU),
       ('3','Pick the setting with\nthe best average',GRN)]
for i,(n,t,col) in enumerate(steps):
    x=0.6+i*3.9
    ax.add_patch(FancyBboxPatch((x,3.4),3.4,3.2,boxstyle="round,pad=0.06",fc=CARD,ec=col,lw=1.6))
    ax.add_patch(Circle((x+0.5,6.1),0.42,fc=col,ec=FG,lw=1.2))
    ax.text(x+0.5,6.1,n,ha='center',va='center',color='#1a1512',fontsize=13,fontweight='bold')
    ax.text(x+1.75,4.7,t,ha='center',va='center',color=FG,fontsize=10,fontweight='bold')
    if i<2: ax.annotate('',xy=(x+3.9,5.0),xytext=(x+3.4,5.0),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
ax.text(6.0,1.6,'This is exactly what GridSearchCV does for you automatically',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/64-workflow.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day16 images generated")
