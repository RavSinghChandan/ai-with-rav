import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; GOLD='#E0B265'; MUT='#b3a595'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# IMG 1: regression (line, number) vs logistic (yes/no) — the difference
fig,axes=plt.subplots(1,2,figsize=(11,4.6)); fig.patch.set_facecolor(BG)
np.random.seed(4)
# left: linear = predict a number
ax=axes[0]; ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
x=np.array([1,2,3,4,5]); y=np.array([20,35,52,68,85])
ax.scatter(x,y,s=110,color=SAF,edgecolor=FG); m,b=np.polyfit(x,y,1)
ax.plot(np.linspace(0.5,5.5,20),m*np.linspace(0.5,5.5,20)+b,color=TEAL,lw=3)
ax.set_title('Linear Regression\npredicts a NUMBER',fontsize=12,fontweight='bold',color=FG)
ax.set_xticks([]); ax.set_yticks([])
# right: logistic = yes/no
ax=axes[1]; ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
xs=np.linspace(-6,6,200); sig=1/(1+np.exp(-xs))
ax.plot(xs,sig,color=GRN,lw=3)
ax.axhline(0.5,color=YEL,ls='--',lw=1.5)
ax.scatter([-4,-2.5,2.5,4],[0.02,0.08,0.92,0.98],s=90,color=SAF,edgecolor=FG)
ax.set_title('Logistic Regression\npredicts YES / NO',fontsize=12,fontweight='bold',color=FG)
ax.set_yticks([0,0.5,1]); ax.set_yticklabels(['NO (0)','50%','YES (1)']); ax.set_xticks([])
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/15-linear-vs-logistic.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 2: the S-curve (sigmoid) squashes any number into 0-1 probability
fig,ax=plt.subplots(figsize=(8.5,5)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
xs=np.linspace(-8,8,300); sig=1/(1+np.exp(-xs))
ax.plot(xs,sig,color=TEAL,lw=3.5)
ax.axhline(0.5,color=YEL,ls='--',lw=1.5); ax.axvline(0,color=MUT,ls=':',lw=1)
ax.fill_between(xs,0.5,sig,where=(sig>=0.5),alpha=0.15,color=GRN)
ax.fill_between(xs,sig,0.5,where=(sig<0.5),alpha=0.15,color=SAF)
ax.text(-4.5,0.22,'left of 0.5\n= NO (not spam)',ha='center',color=SAF,fontsize=10,fontweight='bold')
ax.text(4.5,0.78,'right of 0.5\n= YES (spam)',ha='center',color=GRN,fontsize=10,fontweight='bold')
ax.set_title('The Sigmoid ("S-curve") — squashes anything into a 0–1 probability',fontsize=11.5,fontweight='bold',color=FG)
ax.set_xlabel('score (from the line)',fontsize=11,fontweight='bold')
ax.set_ylabel('probability',fontsize=11,fontweight='bold')
ax.set_yticks([0,0.5,1]); ax.grid(alpha=0.12,color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/16-sigmoid.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 3: the decision threshold — spam filter flow
fig,ax=plt.subplots(figsize=(11,4.0)); ax.set_xlim(0,12); ax.set_ylim(0,5); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,4.6,'How the spam filter decides',ha='center',fontsize=13,fontweight='bold',color=FG)
def box(x,y,w,h,txt,c,tc='#1a1512',fs=10):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.06",fc=c,ec=FG,lw=1.4))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',color=tc,fontsize=fs,fontweight='bold')
box(0.3,2.0,2.4,1.3,'Email\n"WIN FREE $$$"',SAF,fs=9.5)
box(3.3,2.0,2.6,1.3,'Model gives\nprobability = 0.94',TEAL,fs=9.5)
box(6.5,2.0,2.2,1.3,'0.94 > 0.5 ?',YEL,fs=10)
box(9.3,3.0,2.4,1.1,'YES -> Spam',GRN,fs=10)
box(9.3,0.8,2.4,1.1,'NO -> Inbox',MUT,fs=10)
for a,b in [((2.7,2.65),(3.3,2.65)),((5.9,2.65),(6.5,2.65))]:
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,lw=2,color=FG))
ax.add_patch(FancyArrowPatch((8.7,2.9),(9.3,3.4),arrowstyle='-|>',mutation_scale=16,lw=1.8,color=GRN))
ax.add_patch(FancyArrowPatch((8.7,2.4),(9.3,1.4),arrowstyle='-|>',mutation_scale=16,lw=1.8,color=MUT))
ax.text(6,0.2,'The 0.5 line is the "threshold" — you can move it to be stricter or looser.',ha='center',fontsize=9.5,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/17-threshold.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day6 images generated")
