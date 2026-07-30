import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'; PUR='#c39bd3'; CODE='#140f0c'
plt.rcParams.update({'text.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)

# 26: bool = a switch with two settings
fig,ax=plt.subplots(figsize=(9.4,3.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('A Boolean is a switch: only two settings',fontsize=12.5,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((1.4,3.4),3.6,3.4,boxstyle="round,pad=0.05",fc=GRN,ec=FG,lw=1.5))
ax.text(3.2,5.1,'True',ha='center',va='center',color='#1a1512',fontsize=20,fontweight='bold')
ax.text(3.2,2.7,'yes / on / 1',ha='center',color=GRN,fontsize=11,fontweight='bold')
ax.add_patch(FancyBboxPatch((7.0,3.4),3.6,3.4,boxstyle="round,pad=0.05",fc=RED,ec=FG,lw=1.5))
ax.text(8.8,5.1,'False',ha='center',va='center',color='#1a1512',fontsize=20,fontweight='bold')
ax.text(8.8,2.7,'no / off / 0',ha='center',color=RED,fontsize=11,fontweight='bold')
ax.text(6.0,1.2,'Capital T and F. No quotes. Every yes/no question ends up as one of these.',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/26-bool-switch.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 27: comparison operators -> True/False
fig,ax=plt.subplots(figsize=(9.4,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Comparisons ask a question, answer is True or False',fontsize=12,fontweight='bold',color=FG)
rows=[('5 > 3','is 5 bigger than 3?','True',GRN),
      ('5 < 3','is 5 smaller than 3?','False',RED),
      ('5 == 5','are they equal? (two = signs!)','True',GRN),
      ('5 != 3','are they NOT equal?','True',GRN),
      ('5 >= 5','bigger than OR equal to?','True',GRN)]
y=8.3
for op,desc,res,col in rows:
    ax.add_patch(Rectangle((0.5,y-0.5),2.2,0.95,fc=CODE,ec='#3a2f26'))
    ax.text(1.6,y-0.02,op,ha='center',va='center',color=YEL,fontsize=12,family='monospace',fontweight='bold')
    ax.text(3.0,y-0.02,desc,ha='left',va='center',color=MUT,fontsize=10.5)
    ax.text(9.4,y-0.02,'->',ha='center',va='center',color=FG,fontsize=12)
    ax.text(10.9,y-0.02,res,ha='center',va='center',color=col,fontsize=12,fontweight='bold')
    y-=1.55
ax.text(6.0,0.35,'Note: == (double equals) asks "are they equal?"  ·  = (single) means "store"',ha='center',color=SAF,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/27-comparisons.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 28: == vs = trap
fig,ax=plt.subplots(figsize=(9.4,3.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('The classic trap: == vs =',fontsize=12.5,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((0.6,4.2),5.2,3.4,boxstyle="round,pad=0.05",fc=CODE,ec=GRN,lw=1.6))
ax.text(3.2,6.9,'=  store',ha='center',color=GRN,fontsize=13,fontweight='bold')
ax.text(3.2,5.6,'age = 30',ha='center',color=GRN,fontsize=12,family='monospace')
ax.text(3.2,4.7,'"put 30 into age"',ha='center',color=MUT,fontsize=9.5)
ax.add_patch(FancyBboxPatch((6.2,4.2),5.2,3.4,boxstyle="round,pad=0.05",fc=CODE,ec=BLU,lw=1.6))
ax.text(8.8,6.9,'==  compare',ha='center',color=BLU,fontsize=13,fontweight='bold')
ax.text(8.8,5.6,'age == 30',ha='center',color=BLU,fontsize=12,family='monospace')
ax.text(8.8,4.7,'"is age equal to 30?"',ha='center',color=MUT,fontsize=9.5)
ax.text(6.0,1.9,'One = stores. Two == ask a question.',ha='center',color=YEL,fontsize=11,fontweight='bold')
ax.text(6.0,0.9,'Mixing them up is the #1 beginner bug — say it out loud when you type.',ha='center',color=RED,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/28-eq-trap.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 29: and / or / not
fig,ax=plt.subplots(figsize=(9.4,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Combine questions with and / or / not',fontsize=12,fontweight='bold',color=FG)
# and
ax.add_patch(FancyBboxPatch((0.5,5.2),3.5,3.6,boxstyle="round,pad=0.05",fc=CARD,ec=GRN,lw=1.5))
ax.text(2.25,8.3,'and',ha='center',color=GRN,fontsize=14,fontweight='bold')
ax.text(2.25,7.2,'BOTH must be\nTrue',ha='center',va='center',color=FG,fontsize=10)
ax.text(2.25,5.7,'18+ AND ticket',ha='center',color=MUT,fontsize=8.5,family='monospace')
# or
ax.add_patch(FancyBboxPatch((4.25,5.2),3.5,3.6,boxstyle="round,pad=0.05",fc=CARD,ec=BLU,lw=1.5))
ax.text(6.0,8.3,'or',ha='center',color=BLU,fontsize=14,fontweight='bold')
ax.text(6.0,7.2,'AT LEAST ONE\nis True',ha='center',va='center',color=FG,fontsize=10)
ax.text(6.0,5.7,'cash OR card',ha='center',color=MUT,fontsize=8.5,family='monospace')
# not
ax.add_patch(FancyBboxPatch((8.0,5.2),3.5,3.6,boxstyle="round,pad=0.05",fc=CARD,ec=SAF,lw=1.5))
ax.text(9.75,8.3,'not',ha='center',color=SAF,fontsize=14,fontweight='bold')
ax.text(9.75,7.2,'FLIPS it:\nTrue<->False',ha='center',va='center',color=FG,fontsize=10)
ax.text(9.75,5.7,'not raining',ha='center',color=MUT,fontsize=8.5,family='monospace')
ax.text(6.0,3.6,'Real example: can_enter = (age >= 18) and (has_ticket == True)',ha='center',color=YEL,fontsize=10.5,fontweight='bold',family='monospace')
ax.text(6.0,2.2,'and = strict (all yes)  ·  or = generous (any yes)  ·  not = the opposite',ha='center',color=FG,fontsize=10)
plt.tight_layout(); plt.savefig('topics/27-python/images/29-and-or-not.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 30: truth table for and/or
fig,ax=plt.subplots(figsize=(9.4,4.2)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('The simple truth: and vs or',fontsize=12.5,fontweight='bold',color=FG)
def cell(x,y,t,col):
    ax.add_patch(Rectangle((x,y),2.6,0.9,fc=col,ec='#3a2f26'))
    tc='#1a1512' if col in (GRN,RED) else FG
    ax.text(x+1.3,y+0.45,t,ha='center',va='center',color=tc,fontsize=10.5,fontweight='bold')
# headers
ax.text(3.0,8.6,'A and B',ha='center',color=GRN,fontsize=12,fontweight='bold')
ax.text(9.0,8.6,'A or B',ha='center',color=BLU,fontsize=12,fontweight='bold')
data=[('True','True','True','True'),('True','False','False','True'),
      ('False','False','False','False')]
y=7.2
for a,b,rand,ror in data:
    ax.text(0.7,y+0.45,f'{a[:1]} , {b[:1]}',ha='left',va='center',color=MUT,fontsize=9)
    cell(2.0,y,rand,GRN if rand=='True' else RED)
    ax.text(6.7,y+0.45,f'{a[:1]} , {b[:1]}',ha='left',va='center',color=MUT,fontsize=9)
    cell(8.0,y,ror,GRN if ror=='True' else RED)
    y-=1.25
ax.text(6.0,1.0,'and: True ONLY when both are True.   or: True unless BOTH are False.',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/30-truth-table.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("py day6 images generated")
