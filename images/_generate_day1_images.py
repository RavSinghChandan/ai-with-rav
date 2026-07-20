import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

SAFFRON='#FF6B35'; TEAL='#118AB2'; GREEN='#06D6A0'; YELLOW='#FFD166'; DARK='#073B4C'; BG='#FFFDF7'

# ---------- IMG 1: Traditional vs ML (FIXED spacing, no overlaps) ----------
fig, ax = plt.subplots(figsize=(12,5)); ax.set_xlim(0,24); ax.set_ylim(0,10); ax.axis('off')
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
def box(x,y,w,h,txt,c,tc='white',fs=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05",fc=c,ec=DARK,lw=1.8))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',color=tc,fontsize=fs,fontweight='bold')
def arrow(x1,y1,x2,y2):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=22,lw=2.4,color=DARK))

# LEFT: Traditional  (x 0..11)
ax.text(5.0,9.3,'TRADITIONAL PROGRAMMING',ha='center',fontsize=13,fontweight='bold',color=SAFFRON)
box(0.3,6.0,2.6,1.4,'Rules',SAFFRON)
box(0.3,3.2,2.6,1.4,'Data',SAFFRON)
box(4.2,4.6,2.6,1.6,'Computer',DARK)
box(8.0,4.9,2.4,1.1,'Answers',GREEN,DARK)
arrow(2.9,6.7,4.2,5.9)     # rules -> computer
arrow(2.9,3.9,4.2,5.0)     # data -> computer
arrow(6.8,5.4,8.0,5.45)    # computer -> answers

# RIGHT: ML  (x 13..24)
ax.text(18.5,9.3,'MACHINE LEARNING',ha='center',fontsize=13,fontweight='bold',color=TEAL)
box(13.2,6.0,2.6,1.4,'Data',TEAL)
box(13.2,3.2,2.6,1.4,'Answers',TEAL)
box(17.1,4.6,2.6,1.6,'Computer',DARK)
box(20.9,4.9,2.4,1.1,'RULES',YELLOW,DARK)
arrow(15.8,6.7,17.1,5.9)   # data -> computer
arrow(15.8,3.9,17.1,5.0)   # answers -> computer
arrow(19.7,5.4,20.9,5.45)  # computer -> rules

# captions (well below boxes)
ax.text(5.0,1.6,'YOU write the rules',ha='center',fontsize=11,color=DARK,style='italic')
ax.text(18.5,1.6,'The MACHINE writes the rules',ha='center',fontsize=11,color=DARK,style='italic')
# subtle divider
ax.plot([12,12],[2.5,8.5],color='#ddd',lw=1.5,ls='--')
plt.tight_layout(); plt.savefig('images/01-traditional-vs-ml.png',dpi=130,facecolor=BG,bbox_inches='tight'); plt.close()

# ---------- IMG 2: How learning happens (FIXED title above boxes) ----------
fig, ax = plt.subplots(figsize=(9,6)); ax.set_xlim(0,10); ax.set_ylim(0,11); ax.axis('off')
fig.patch.set_facecolor(BG)
ax.text(5,10.5,'How a machine actually learns',ha='center',fontsize=14,fontweight='bold',color=DARK)
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
plt.tight_layout(); plt.savefig('images/02-how-learning-happens.png',dpi=130,facecolor=BG,bbox_inches='tight'); plt.close()

print("regenerated images 1 and 2 (fixed)")
