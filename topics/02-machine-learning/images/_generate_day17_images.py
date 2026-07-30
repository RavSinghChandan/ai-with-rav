import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)

# ===== 65: THE ACCURACY TRAP =====
fig,ax=plt.subplots(figsize=(9.0,5.0)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('The accuracy trap: 99% "accurate" — and useless',fontsize=12.5,fontweight='bold',color=FG)
# 1000 patients grid: 10 sick (red), 990 healthy (green) -- draw a compact dotted grid
np.random.seed(1)
rows,cols=20,50
sick=set(np.random.choice(rows*cols,10,replace=False))
for k in range(rows*cols):
    r,c=divmod(k,cols)
    x=0.5+c*0.222; y=8.4-r*0.30
    col=RED if k in sick else GRN
    ax.add_patch(Circle((x,y),0.085,fc=col,ec='none'))
ax.text(6.0,2.0,'A lazy model says "healthy" to EVERYONE.\nIt is right 990/1000 = 99% of the time...',
        ha='center',color=FG,fontsize=10.5,fontweight='bold')
ax.text(6.0,0.7,'...but it caught ZERO of the 10 sick people. Useless!',ha='center',color=RED,fontsize=11,fontweight='bold')
ax.scatter([],[],c=RED,label='sick (10)'); ax.scatter([],[],c=GRN,label='healthy (990)')
leg=ax.legend(fontsize=9,facecolor=CARD,edgecolor='#3a2f26',loc='upper right')
for t in leg.get_texts(): t.set_color(FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/65-accuracy-trap.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 66: THE CONFUSION MATRIX =====
fig,ax=plt.subplots(figsize=(8.8,5.6)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
ax.set_title('The confusion matrix: 4 possible outcomes',fontsize=13,fontweight='bold',color=FG)
cells=[((5.2,5.0),GRN,'TRUE POSITIVE','sick + caught\n(correct)'),
       ((7.3,5.0),RED,'FALSE POSITIVE','healthy but\nalarmed (false alarm)'),
       ((5.2,2.4),RED,'FALSE NEGATIVE','sick but MISSED\n(dangerous!)'),
       ((7.3,2.4),GRN,'TRUE NEGATIVE','healthy + cleared\n(correct)')]
for (x,y),col,t,sub in cells:
    ax.add_patch(FancyBboxPatch((x,y),2.0,2.2,boxstyle="round,pad=0.03",fc=col,ec=FG,lw=1.4,alpha=0.85))
    ax.text(x+1.0,y+1.6,t,ha='center',color='#1a1512',fontsize=9.5,fontweight='bold')
    ax.text(x+1.0,y+0.7,sub,ha='center',color='#1a1512',fontsize=8.2)
ax.text(6.25,8.0,'What the model SAID',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
ax.text(6.2,7.4,'"sick"',ha='center',color=FG,fontsize=9.5); ax.text(8.3,7.4,'"healthy"',ha='center',color=FG,fontsize=9.5)
ax.text(4.4,6.1,'really\nsick',ha='center',color=FG,fontsize=9.5)
ax.text(4.4,3.5,'really\nhealthy',ha='center',color=FG,fontsize=9.5)
ax.text(2.2,5.0,'the TRUTH',rotation=90,va='center',color=YEL,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/66-confusion.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 67: PRECISION =====
fig,ax=plt.subplots(figsize=(8.8,4.8)); fig.patch.set_facecolor(BG); frame(ax)
ax.set_title('Precision: of everyone you CALLED sick, how many really were?',fontsize=11.5,fontweight='bold',color=FG)
# 8 people the model called "sick": 6 truly sick (green), 2 false alarms (red)
for i in range(8):
    x=1.0+i*1.05; col=GRN if i<6 else RED
    ax.add_patch(Circle((x,6.6),0.42,fc=col,ec=FG,lw=1.2))
    ax.text(x,6.6,'✓' if i<6 else '✗',ha='center',va='center',color='#1a1512',fontsize=13,fontweight='bold')
ax.text(5.0,5.3,'model called these 8 people "sick"',ha='center',color=MUT,fontsize=10)
ax.text(5.0,3.4,'6 were really sick, 2 were false alarms',ha='center',color=FG,fontsize=11,fontweight='bold')
ax.text(5.0,2.0,'PRECISION = 6 / 8 = 75%',ha='center',color=GRN,fontsize=13,fontweight='bold')
ax.text(5.0,0.9,'"When I say sick, I\'m right 75% of the time" — avoids false alarms',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/67-precision.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 68: RECALL =====
fig,ax=plt.subplots(figsize=(8.8,4.8)); fig.patch.set_facecolor(BG); frame(ax)
ax.set_title('Recall: of everyone truly sick, how many did you CATCH?',fontsize=11.5,fontweight='bold',color=FG)
# 10 truly sick people: 6 caught (green ✓), 4 missed (red ✗)
for i in range(10):
    x=0.7+i*0.95; col=GRN if i<6 else RED
    ax.add_patch(Circle((x,6.6),0.38,fc=col,ec=FG,lw=1.2))
    ax.text(x,6.6,'✓' if i<6 else '✗',ha='center',va='center',color='#1a1512',fontsize=12,fontweight='bold')
ax.text(5.0,5.3,'these 10 people were really sick',ha='center',color=MUT,fontsize=10)
ax.text(5.0,3.4,'caught 6, MISSED 4',ha='center',color=FG,fontsize=11,fontweight='bold')
ax.text(5.0,2.0,'RECALL = 6 / 10 = 60%',ha='center',color=BLU,fontsize=13,fontweight='bold')
ax.text(5.0,0.9,'"I catch 60% of the truly sick" — avoids dangerous misses',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/68-recall.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 69: THE TRADEOFF + F1 =====
fig,ax=plt.subplots(figsize=(8.8,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
ax.set_title('Precision vs Recall pull apart — F1 balances them',fontsize=12.5,fontweight='bold',color=FG)
# a see-saw / dial
ax.text(2.5,8.0,'catch MORE\n(high recall)',ha='center',color=BLU,fontsize=10.5,fontweight='bold')
ax.text(7.5,8.0,'be SURER\n(high precision)',ha='center',color=GRN,fontsize=10.5,fontweight='bold')
ax.annotate('',xy=(6.4,6.6),xytext=(3.6,6.6),arrowprops=dict(arrowstyle='<->',color=YEL,lw=3))
ax.text(5.0,7.1,'you can trade one for the other',ha='center',color=MUT,fontsize=9.5)
ax.text(2.5,5.2,'catch everyone →\nmore false alarms',ha='center',color=BLU,fontsize=9.5)
ax.text(7.5,5.2,'only sure calls →\nmiss some sick',ha='center',color=GRN,fontsize=9.5)
ax.add_patch(FancyBboxPatch((1.2,1.2),7.6,2.6,boxstyle="round,pad=0.06",fc=CARD,ec=YEL,lw=1.6))
ax.text(5.0,3.0,'F1 SCORE = one number that balances both',ha='center',color=YEL,fontsize=12,fontweight='bold')
ax.text(5.0,1.9,'(a fair blend of precision AND recall — high only when BOTH are high)',ha='center',color=FG,fontsize=9.5)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/69-f1.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day17 images generated")
