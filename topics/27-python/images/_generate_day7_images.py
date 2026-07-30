import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'; PUR='#c39bd3'; CODE='#140f0c'
plt.rcParams.update({'text.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)

# 31: the road that forks (if/else)
fig,ax=plt.subplots(figsize=(9.4,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('if / else = the road that forks',fontsize=13,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((4.4,7.6),3.2,1.5,boxstyle="round,pad=0.05",fc=YEL,ec=FG,lw=1.4))
ax.text(6.0,8.35,'age >= 18 ?',ha='center',va='center',color='#1a1512',fontsize=11,fontweight='bold')
ax.annotate('',xy=(2.6,4.9),xytext=(5.2,7.5),arrowprops=dict(arrowstyle='->',color=GRN,lw=2.2))
ax.annotate('',xy=(9.4,4.9),xytext=(6.8,7.5),arrowprops=dict(arrowstyle='->',color=RED,lw=2.2))
ax.text(3.2,6.4,'True',ha='center',color=GRN,fontsize=11,fontweight='bold')
ax.text(8.8,6.4,'False',ha='center',color=RED,fontsize=11,fontweight='bold')
ax.add_patch(FancyBboxPatch((0.8,3.0),3.6,1.9,boxstyle="round,pad=0.05",fc=GRN,ec=FG,lw=1.4))
ax.text(2.6,3.95,'"You may enter"',ha='center',va='center',color='#1a1512',fontsize=10,fontweight='bold')
ax.add_patch(FancyBboxPatch((7.6,3.0),3.6,1.9,boxstyle="round,pad=0.05",fc=RED,ec=FG,lw=1.4))
ax.text(9.4,3.95,'"Sorry, too young"',ha='center',va='center',color='#1a1512',fontsize=10,fontweight='bold')
ax.text(6.0,1.4,'The condition decides which road the program takes.',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/31-fork.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 32: anatomy of an if (colon + indent)
fig,ax=plt.subplots(figsize=(9.4,4.0)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('The shape of an if: colon, then indent',fontsize=12,fontweight='bold',color=FG)
ax.add_patch(Rectangle((0.8,2.6),10.4,5.6,fc=CODE,ec='#3a2f26'))
ax.text(1.2,7.2,'if age >= 18:',color=YEL,fontsize=13,family='monospace')
ax.text(2.6,5.7,'print("You may enter")',color=GRN,fontsize=13,family='monospace')
# annotate colon
ax.annotate('the colon : ends the question',xy=(4.6,7.2),xytext=(6.4,7.9),
            arrowprops=dict(arrowstyle='->',color=SAF,lw=1.6),color=SAF,fontsize=9.5,va='center')
# annotate indent
ax.annotate('4 spaces of INDENT =\n"this runs if True"',xy=(2.5,5.7),xytext=(6.2,4.6),
            arrowprops=dict(arrowstyle='->',color=BLU,lw=1.6),color=BLU,fontsize=9.5,va='center')
ax.text(6.0,1.3,'Python uses INDENTATION (spaces) to group code — not { } braces.',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/32-anatomy.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 33: if / elif / else ladder
fig,ax=plt.subplots(figsize=(9.4,4.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('if / elif / else = checking in order, top to bottom',fontsize=11.5,fontweight='bold',color=FG)
steps=[('if  marks >= 90:','Grade A',GRN),
       ('elif marks >= 70:','Grade B',BLU),
       ('elif marks >= 40:','Grade C',YEL),
       ('else:','Fail',RED)]
y=8.2
for cond,res,col in steps:
    ax.add_patch(Rectangle((0.6,y-0.55),5.6,1.0,fc=CODE,ec=col,lw=1.3))
    ax.text(0.9,y-0.05,cond,va='center',color=col,fontsize=11,family='monospace')
    ax.annotate('',xy=(8.0,y-0.05),xytext=(6.4,y-0.05),arrowprops=dict(arrowstyle='->',color=MUT,lw=1.6))
    ax.add_patch(FancyBboxPatch((8.2,y-0.5),3.0,0.9,boxstyle="round,pad=0.03",fc=col,ec=FG,lw=1.0))
    ax.text(9.7,y-0.05,res,ha='center',va='center',color='#1a1512',fontsize=10.5,fontweight='bold')
    y-=1.25
ax.text(6.0,0.5,'Python checks top to bottom, STOPS at the first True. else = "none matched".',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/33-ladder.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 34: stops at first True
fig,ax=plt.subplots(figsize=(9.4,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('It stops at the FIRST match (marks = 75)',fontsize=12,fontweight='bold',color=FG)
rows=[('marks >= 90 ?','False - skip',RED,False),
      ('marks >= 70 ?','True - RUN THIS, then stop','#5fd06a',True),
      ('marks >= 40 ?','never checked',MUT,None),
      ('else','never reached',MUT,None)]
y=8.0
for cond,note,col,hit in rows:
    ec = GRN if hit else ('#3a2f26')
    lw = 2.2 if hit else 1.0
    ax.add_patch(Rectangle((0.6,y-0.55),4.6,1.0,fc=(CODE if hit is not None else '#1e1712'),ec=ec,lw=lw))
    ax.text(0.85,y-0.05,cond,va='center',color=(FG if hit else MUT),fontsize=11,family='monospace')
    ax.text(5.6,y-0.05,note,va='center',color=col,fontsize=10.5,fontweight=('bold' if hit else 'normal'))
    y-=1.2
ax.text(6.0,1.6,'-> Grade B',ha='center',color=GRN,fontsize=13,fontweight='bold')
ax.text(6.0,0.7,'Once one condition is True, the rest are ignored. Order matters!',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/34-first-match.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 35: indentation groups the block
fig,ax=plt.subplots(figsize=(9.4,4.2)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Indentation decides what belongs inside',fontsize=12,fontweight='bold',color=FG)
ax.add_patch(Rectangle((0.6,2.4),10.8,6.0,fc=CODE,ec='#3a2f26'))
lines=[('if logged_in:',YEL,1.2),
       ('    print("Welcome!")',GRN,2.6),
       ('    show_dashboard()',GRN,2.6),
       ('print("Done")',FG,1.2)]
yy=7.6
for txt,col,x in lines:
    ax.text(x,yy,txt,color=col,fontsize=12,family='monospace')
    yy-=1.15
# bracket showing inside block
ax.annotate('',xy=(2.4,6.6),xytext=(2.4,5.3),arrowprops=dict(arrowstyle='-',color=BLU,lw=2))
ax.text(7.9,6.0,'indented = INSIDE the if',color=BLU,fontsize=9.5,fontweight='bold')
ax.text(7.9,2.9,'not indented = always runs',color=MUT,fontsize=9.5,fontweight='bold')
ax.text(6.0,1.2,'Line up the spaces (4 is standard). Wrong indent = wrong meaning.',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/35-indent-block.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("py day7 images generated")
