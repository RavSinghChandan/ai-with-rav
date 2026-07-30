import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)

# shared: a wavy TRUE pattern + noisy dots around it
np.random.seed(6)
xt=np.linspace(0.6,9.4,22)
true=lambda x: 5 + 2.2*np.sin(x*0.6)
yt=true(xt)+np.random.randn(22)*0.8

# ===== 55: THREE STUDENTS — underfit / just right / overfit =====
fig,axes=plt.subplots(1,3,figsize=(14,4.6)); fig.patch.set_facecolor(BG)
xs=np.linspace(0.4,9.6,200)
titles=[('UNDERFIT','learns too little\n(fails practice AND exam)',RED),
        ('JUST RIGHT','understands the pattern\n(does well on both)',GRN),
        ('OVERFIT','memorises every dot\n(perfect practice, fails exam)',RED)]
for ax,(t,sub,col) in zip(axes,titles):
    frame(ax); ax.scatter(xt,yt,c=BLU,s=45,zorder=3,edgecolor='none')
    if t=='UNDERFIT':
        m,b=np.polyfit(xt,yt,1); ax.plot(xs,m*xs+b,color=SAF,lw=3)   # a flat-ish straight line
    elif t=='JUST RIGHT':
        ax.plot(xs,true(xs),color=GRN,lw=3)                          # the smooth true curve
    else:
        z=np.polyfit(xt,yt,15); ax.plot(xs,np.clip(np.polyval(z,xs),0,10),color=RED,lw=2.2)  # wild wiggly overfit
    ax.set_title(t,fontsize=13,fontweight='bold',color=col)
    ax.text(5,0.4,sub,ha='center',color=col,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/55-three-students.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 56: SIGNAL vs NOISE =====
fig,ax=plt.subplots(figsize=(8.8,4.8)); fig.patch.set_facecolor(BG); frame(ax)
ax.scatter(xt,yt,c=BLU,s=55,zorder=3,edgecolor='none',label='the data (dots)')
ax.plot(xs,true(xs),color=GRN,lw=3,zorder=2,label='SIGNAL: the real pattern')
# point out a noisy dot that sits FAR above the true curve — label it in clear
# space to the right so nothing overlaps the title
i=np.argmax(yt-true(xt))   # the dot most ABOVE the curve
ax.annotate('NOISE: a random wiggle\n(do NOT chase this)',xy=(xt[i],yt[i]),xytext=(xt[i]+1.4,yt[i]-0.2),
            color=RED,fontsize=10,fontweight='bold',ha='left',va='center',
            arrowprops=dict(arrowstyle='->',color=RED,lw=1.8))
ax.set_title('Signal (the real pattern) vs Noise (random wiggles)',fontsize=12.5,fontweight='bold',color=FG)
leg=ax.legend(fontsize=9.5,facecolor=CARD,edgecolor='#3a2f26',loc='lower right')
for tx in leg.get_texts(): tx.set_color(FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/56-signal-noise.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 57: TRAIN score vs TEST score — the tell-tale gap =====
fig,ax=plt.subplots(figsize=(8.8,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
groups=['UNDERFIT','JUST RIGHT','OVERFIT']
train=[55,90,100]; test=[52,88,60]
x0=1.3
for i,(g,tr,te) in enumerate(zip(groups,train,test)):
    x=x0+i*3.0
    ax.add_patch(Rectangle((x,1.6),0.9,tr*0.07,fc=BLU,ec=FG,lw=1.0))
    ax.text(x+0.45,1.6+tr*0.07+0.3,f'{tr}',ha='center',color=BLU,fontsize=10,fontweight='bold')
    ax.add_patch(Rectangle((x+1.0,1.6),0.9,te*0.07,fc=YEL,ec=FG,lw=1.0))
    ax.text(x+1.45,1.6+te*0.07+0.3,f'{te}',ha='center',color=YEL,fontsize=10,fontweight='bold')
    ax.text(x+0.95,1.0,g,ha='center',color=FG,fontsize=10,fontweight='bold')
ax.text(0.6,9.2,'blue = practice (train) score   ·   yellow = real-exam (test) score',color=MUT,fontsize=10)
ax.text(8.2,4.6,'BIG GAP\n= overfit!',ha='center',color=RED,fontsize=10.5,fontweight='bold')
ax.set_title('The tell-tale sign: compare practice score vs real-exam score',fontsize=12,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/57-train-test.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 58: THE U-CURVE — test error dips then rises =====
fig,ax=plt.subplots(figsize=(8.8,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
cx=np.linspace(0.6,9.4,100)
train_err=8.5*np.exp(-cx*0.45)+0.4          # train error keeps dropping
test_err=8.0*np.exp(-cx*0.5)+0.25*(cx-3.2)**2+0.6   # test error dips then rises (U)
ax.plot(cx,train_err,color=BLU,lw=2.6,label='practice (train) error')
ax.plot(cx,test_err,color=YEL,lw=2.6,label='real-exam (test) error')
# sweet spot = min of test error
mi=int(np.argmin(test_err))
ax.scatter([cx[mi]],[test_err[mi]],s=340,facecolor='none',edgecolor=GRN,lw=2.6,zorder=4)
ax.annotate('sweet spot\n(just right)',xy=(cx[mi],test_err[mi]),xytext=(cx[mi]+1.3,test_err[mi]+2.2),
            color=GRN,fontsize=10.5,fontweight='bold',arrowprops=dict(arrowstyle='->',color=GRN,lw=1.8))
ax.text(1.4,8.6,'UNDERFIT',color=RED,fontsize=10,fontweight='bold')
ax.text(8.0,8.6,'OVERFIT',color=RED,fontsize=10,fontweight='bold')
ax.set_xlabel('model complexity  →  (simple ... complex)',color=FG,fontsize=10.5)
ax.set_ylabel('error (lower = better)',color=FG,fontsize=10.5)
leg=ax.legend(fontsize=9.5,facecolor=CARD,edgecolor='#3a2f26',loc='upper center')
for tx in leg.get_texts(): tx.set_color(FG)
ax.set_title('Too simple OR too complex both hurt — aim for the middle',fontsize=12,fontweight='bold',color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/58-ucurve.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 59: THE FIXES — cure underfit vs overfit =====
fig,axes=plt.subplots(1,2,figsize=(11,4.6)); fig.patch.set_facecolor(BG)
for ax in axes: frame(ax)
ax=axes[0]
ax.set_title('If UNDERFIT (learns too little)',fontsize=12,fontweight='bold',color=SAF)
fixesU=['Use a stronger / more complex model','Add more useful features (clues)','Train longer']
for i,f in enumerate(fixesU):
    ax.add_patch(FancyBboxPatch((0.6,7.0-i*2.0),8.6,1.4,boxstyle="round,pad=0.05",fc=CARD,ec=SAF,lw=1.4))
    ax.text(5.0,7.7-i*2.0,f,ha='center',va='center',color=FG,fontsize=11,fontweight='bold')
ax=axes[1]
ax.set_title('If OVERFIT (memorises too much)',fontsize=12,fontweight='bold',color=BLU)
fixesO=['Simpler model / limit depth','More training data','Regularization (a penalty on complexity)']
for i,f in enumerate(fixesO):
    ax.add_patch(FancyBboxPatch((0.6,7.0-i*2.0),8.6,1.4,boxstyle="round,pad=0.05",fc=CARD,ec=BLU,lw=1.4))
    ax.text(5.0,7.7-i*2.0,f,ha='center',va='center',color=FG,fontsize=11,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/59-fixes.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day15 images generated")
