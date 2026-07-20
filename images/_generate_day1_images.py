import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# DARK theme palette
BG='#0d1117'; FG='#e6edf3'; SAFFRON='#FF6B35'; TEAL='#33B5E5'; GREEN='#06D6A0'; YELLOW='#FFD166'; NAVY='#1f2937'
plt.rcParams['text.color']=FG; plt.rcParams['axes.labelcolor']=FG
plt.rcParams['xtick.color']=FG; plt.rcParams['ytick.color']=FG

# ---------- IMG 1: Traditional vs ML (dark) ----------
fig, ax = plt.subplots(figsize=(12,5)); ax.set_xlim(0,24); ax.set_ylim(0,10); ax.axis('off')
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
def box(x,y,w,h,txt,c,tc='#0d1117',fs=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05",fc=c,ec=FG,lw=1.6))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',color=tc,fontsize=fs,fontweight='bold')
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=22,lw=2.6,color=FG))
ax.text(5.0,9.3,'TRADITIONAL PROGRAMMING',ha='center',fontsize=13,fontweight='bold',color=SAFFRON)
box(0.3,6.0,2.6,1.4,'Rules',SAFFRON); box(0.3,3.2,2.6,1.4,'Data',SAFFRON)
box(4.2,4.6,2.6,1.6,'Computer',TEAL); box(8.0,4.9,2.4,1.1,'Answers',GREEN)
arrow(2.9,6.7,4.2,5.9); arrow(2.9,3.9,4.2,5.0); arrow(6.8,5.4,8.0,5.45)
ax.text(18.5,9.3,'MACHINE LEARNING',ha='center',fontsize=13,fontweight='bold',color=TEAL)
box(13.2,6.0,2.6,1.4,'Data',TEAL); box(13.2,3.2,2.6,1.4,'Answers',TEAL)
box(17.1,4.6,2.6,1.6,'Computer',SAFFRON); box(20.9,4.9,2.4,1.1,'RULES',YELLOW)
arrow(15.8,6.7,17.1,5.9); arrow(15.8,3.9,17.1,5.0); arrow(19.7,5.4,20.9,5.45)
ax.text(5.0,1.6,'YOU write the rules',ha='center',fontsize=11,color=FG,style='italic')
ax.text(18.5,1.6,'The MACHINE writes the rules',ha='center',fontsize=11,color=FG,style='italic')
ax.plot([12,12],[2.5,8.5],color='#30363d',lw=1.5,ls='--')
plt.tight_layout(); plt.savefig('images/01-traditional-vs-ml.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ---------- IMG 2: How learning happens (dark) ----------
fig, ax = plt.subplots(figsize=(9,6)); ax.set_xlim(0,10); ax.set_ylim(0,11); ax.axis('off')
fig.patch.set_facecolor(BG)
ax.text(5,10.5,'How a machine actually learns',ha='center',fontsize=14,fontweight='bold',color=FG)
steps=[('PAST DATA\n(1000 days of chai sales)',SAFFRON,8.4),
       ('LEARNING / TRAINING\n(model adjusts until guesses match)',TEAL,6.3),
       ('THE MODEL\n(the pattern it learned = y = f(X))',GREEN,4.2),
       ('PREDICTION\n"Rainy + 6PM + salary day -> 220 cups"',YELLOW,2.1)]
for txt,c,y in steps:
    ax.add_patch(FancyBboxPatch((2.2,y),5.6,1.4,boxstyle="round,pad=0.1",fc=c,ec=FG,lw=1.6))
    ax.text(5.0,y+0.7,txt,ha='center',va='center',color='#0d1117',fontsize=11,fontweight='bold')
for y in [8.4,6.3,4.2]:
    ax.add_patch(FancyArrowPatch((5.0,y),(5.0,y-0.7),arrowstyle='-|>',mutation_scale=22,lw=2.6,color=FG))
plt.tight_layout(); plt.savefig('images/02-how-learning-happens.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ---------- IMG 3: Chai regression (dark) ----------
fig, ax = plt.subplots(figsize=(8,5))
fig.patch.set_facecolor(BG); ax.set_facecolor('#161b22')
for s in ax.spines.values(): s.set_color('#30363d')
temp=np.array([15,20,25,30,35]); cups=np.array([200,170,140,110,80])
ax.scatter(temp,cups,s=180,color=SAFFRON,edgecolor=FG,zorder=3,label='Past days (data)')
m,b=np.polyfit(temp,cups,1); xs=np.linspace(13,37,50)
ax.plot(xs,m*xs+b,color=TEAL,lw=3,zorder=2,label='What the model learned (the line)')
ax.scatter([18],[m*18+b],s=280,color=GREEN,edgecolor=FG,marker='*',zorder=4,label='NEW day: 18C -> ~182 cups')
ax.annotate('predict!',(18,m*18+b),textcoords="offset points",xytext=(15,25),fontsize=11,fontweight='bold',color=GREEN)
ax.set_xlabel('Temperature (C)',fontsize=12,fontweight='bold')
ax.set_ylabel('Cups of chai sold',fontsize=12,fontweight='bold')
ax.set_title("Ramesh's chai: colder day = more chai (a real model)",fontsize=12,fontweight='bold',color=FG)
leg=ax.legend(fontsize=9,loc='upper right',facecolor='#161b22',edgecolor='#30363d')
for t in leg.get_texts(): t.set_color(FG)
ax.grid(alpha=0.15,color=FG)
plt.tight_layout(); plt.savefig('images/03-chai-regression.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("regenerated all 3 images on DARK background")
