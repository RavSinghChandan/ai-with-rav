import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# engagement palette: warm saffron/teal, high contrast (tested well with Indian audiences)
SAFFRON='#FF6B35'; TEAL='#118AB2'; GREEN='#06D6A0'; YELLOW='#FFD166'; DARK='#073B4C'; BG='#FFFDF7'

# ---------- IMG 1: Traditional Programming vs Machine Learning ----------
fig, ax = plt.subplots(figsize=(10,4.6)); ax.set_xlim(0,10); ax.set_ylim(0,5); ax.axis('off')
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
def box(x,y,w,h,txt,c,tc='white',fs=11):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.08",fc=c,ec=DARK,lw=1.6))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',color=tc,fontsize=fs,fontweight='bold')
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=20,lw=2.2,color=DARK))
ax.text(2.5,4.7,'TRADITIONAL PROGRAMMING',ha='center',fontsize=12,fontweight='bold',color=SAFFRON)
box(0.3,3.0,1.7,0.8,'Rules',SAFFRON); box(0.3,1.6,1.7,0.8,'Data',SAFFRON)
box(2.7,2.3,1.6,0.9,'Computer',DARK); box(4.9,2.35,0.9,0.8,'Answers',GREEN,DARK)
arrow(2.0,3.4,2.7,3.0); arrow(2.0,2.0,2.7,2.6); arrow(4.3,2.75,4.9,2.75)
ax.text(7.5,4.7,'MACHINE LEARNING',ha='center',fontsize=12,fontweight='bold',color=TEAL)
box(5.7,3.0,1.7,0.8,'Data',TEAL); box(5.7,1.6,1.7,0.8,'Answers',TEAL)
box(8.1,2.3,1.5,0.9,'Computer',DARK); box(9.0,2.35,0.9,0.8,'RULES',YELLOW,DARK,10)
# extend xlim
ax.set_xlim(0,10.2)
arrow(7.4,3.4,8.1,3.0); arrow(7.4,2.0,8.1,2.6); arrow(9.6,2.75,10.0,2.75)
ax.text(2.5,0.7,'YOU write the rules',ha='center',fontsize=10,color=DARK,style='italic')
ax.text(7.8,0.7,'The MACHINE writes the rules',ha='center',fontsize=10,color=DARK,style='italic')
plt.tight_layout(); plt.savefig('images/01-traditional-vs-ml.png',dpi=130,facecolor=BG,bbox_inches='tight'); plt.close()

# ---------- IMG 2: How learning happens (flow) ----------
fig, ax = plt.subplots(figsize=(9,5.2)); ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis('off')
fig.patch.set_facecolor(BG)
steps=[('PAST DATA\n(1000 days of chai sales)',SAFFRON,8.4),
       ('LEARNING / TRAINING\n(model adjusts until guesses match)',TEAL,6.3),
       ('THE MODEL\n(the pattern it learned = y = f(X))',GREEN,4.2),
       ('PREDICTION\n"Rainy + 6PM + salary day -> 220 cups"',YELLOW,2.1)]
for txt,c,y in steps:
    tc = DARK if c==YELLOW else 'white'
    ax.add_patch(FancyBboxPatch((2.2,y),5.6,1.4,boxstyle="round,pad=0.1",fc=c,ec=DARK,lw=1.8))
    ax.text(5.0,y+0.7,txt,ha='center',va='center',color=tc,fontsize=11,fontweight='bold')
for y in [8.4,6.3,4.2]:
    ax.add_patch(FancyArrowPatch((5.0,y),(5.0,y-0.7),arrowstyle='-|>',mutation_scale=22,lw=2.4,color=DARK))
ax.text(5,9.6,'How a machine actually learns',ha='center',fontsize=13,fontweight='bold',color=DARK)
plt.tight_layout(); plt.savefig('images/02-how-learning-happens.png',dpi=130,facecolor=BG,bbox_inches='tight'); plt.close()

# ---------- IMG 3: Chai regression (temperature vs cups) ----------
fig, ax = plt.subplots(figsize=(8,5))
fig.patch.set_facecolor(BG); ax.set_facecolor('white')
temp=np.array([15,20,25,30,35]); cups=np.array([200,170,140,110,80])
ax.scatter(temp,cups,s=180,color=SAFFRON,edgecolor=DARK,zorder=3,label='Past days (data)')
m,b=np.polyfit(temp,cups,1); xs=np.linspace(13,37,50)
ax.plot(xs,m*xs+b,color=TEAL,lw=3,zorder=2,label='What the model learned (the line)')
ax.scatter([18],[m*18+b],s=260,color=GREEN,edgecolor=DARK,marker='*',zorder=4,label='NEW day: 18°C -> ~182 cups')
ax.annotate('predict!',(18,m*18+b),textcoords="offset points",xytext=(15,25),fontsize=11,fontweight='bold',color=GREEN)
ax.set_xlabel('Temperature (°C)',fontsize=12,fontweight='bold',color=DARK)
ax.set_ylabel('Cups of chai sold',fontsize=12,fontweight='bold',color=DARK)
ax.set_title("Ramesh's chai: colder day → more chai (a real model)",fontsize=12,fontweight='bold',color=DARK)
ax.legend(fontsize=9,loc='upper right'); ax.grid(alpha=0.25)
plt.tight_layout(); plt.savefig('images/03-chai-regression.png',dpi=130,facecolor=BG,bbox_inches='tight'); plt.close()

print("generated 3 images")
