import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'; PUR='#c39bd3'; CODE='#140f0c'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
def box(ax,x,y,w,h,color,text,tcolor='#1a1512',fs=10,ec=None):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05,rounding_size=0.12",
                 fc=color,ec=ec or FG,lw=1.4,alpha=0.94,zorder=2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=tcolor,fontsize=fs,fontweight='bold',zorder=3)

# ===== 1: PYTHON vs OTHER LANGUAGES — same task, plainer =====
fig,axes=plt.subplots(1,2,figsize=(11,4.4)); fig.patch.set_facecolor(BG)
ax=axes[0]; frame(ax)
ax.set_title('Other languages (e.g. Java): print a line',fontsize=11.5,fontweight='bold',color=RED)
ax.add_patch(Rectangle((0.5,3.6),9,4.0,fc=CODE,ec='#3a2f26'))
ax.text(0.9,6.6,'public class Main {',color=FG,fontsize=10,family='monospace')
ax.text(1.3,5.9,'public static void main(String[] a){',color=FG,fontsize=9,family='monospace')
ax.text(1.7,5.2,'System.out.println("Hello");',color=GRN,fontsize=9,family='monospace')
ax.text(1.3,4.5,'}',color=FG,fontsize=10,family='monospace')
ax.text(0.9,3.9,'}',color=FG,fontsize=10,family='monospace')
ax.text(5,2.4,'lots of formal grammar',ha='center',color=RED,fontsize=10,fontweight='bold')
ax=axes[1]; frame(ax)
ax.set_title('Python: print a line',fontsize=11.5,fontweight='bold',color=GRN)
ax.add_patch(Rectangle((0.5,4.8),9,1.6,fc=CODE,ec='#3a2f26'))
ax.text(1.0,5.5,'print("Hello")',color=GRN,fontsize=14,family='monospace')
ax.text(5,2.8,'just say what you mean — one line',ha='center',color=GRN,fontsize=10.5,fontweight='bold')
fig.suptitle('Python = giving instructions in plain, simple English',fontsize=12.5,fontweight='bold',color=FG,y=1.03)
plt.tight_layout(); plt.savefig('topics/27-python/images/1-vs-other.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 2: WHY AI LOVES PYTHON — the ecosystem tower =====
fig,ax=plt.subplots(figsize=(9.0,5.2)); fig.patch.set_facecolor(BG); frame(ax)
ax.set_title('Why AI loves Python: the whole AI world is built on it',fontsize=12.5,fontweight='bold',color=FG)
box(ax,1.0,1.4,8.0,1.5,GRN,'PYTHON  (the simple base language)',tcolor='#1a1512',fs=12)
libs=[('NumPy',BLU,1.2),('Pandas',SAF,3.2),('scikit-learn',YEL,5.2),('PyTorch',PUR,7.0)]
for t,c,x in libs:
    box(ax,x,3.6,1.7,1.3,c,t,tcolor='#1a1512',fs=9.5)
box(ax,2.6,6.0,4.8,1.4,RED,'ChatGPT · self-driving · everything AI',tcolor='#1a1512',fs=10)
ax.annotate('',xy=(5.0,5.9),xytext=(5.0,5.0),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.2))
ax.annotate('',xy=(5.0,3.5),xytext=(5.0,3.0),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.2))
ax.text(5.0,0.6,'Learn Python once → unlock every AI tool on top of it',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/2-ecosystem.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 3: HOW CODE RUNS — write -> interpreter -> result =====
fig,ax=plt.subplots(figsize=(9.4,3.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('How your code runs',fontsize=12.5,fontweight='bold',color=FG)
box(ax,0.6,3.6,3.0,2.6,BLU,'YOU WRITE\nprint("Hi")',tcolor='#1a1512',fs=10)
box(ax,4.4,3.6,3.0,2.6,YEL,'PYTHON reads\n& runs it\n(the interpreter)',tcolor='#1a1512',fs=9.5)
box(ax,8.2,3.6,3.0,2.6,GRN,'RESULT\nHi',tcolor='#1a1512',fs=11)
ax.annotate('',xy=(4.4,4.9),xytext=(3.6,4.9),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
ax.annotate('',xy=(8.2,4.9),xytext=(7.4,4.9),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
ax.text(6.0,1.6,'Python reads your plain-English instructions and does them, top to bottom',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/3-how-runs.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 4: FIRST PROGRAM ANATOMY =====
fig,ax=plt.subplots(figsize=(9.0,4.4)); fig.patch.set_facecolor(BG); frame(ax)
ax.set_title('Your first program, taken apart',fontsize=12.5,fontweight='bold',color=FG)
ax.add_patch(Rectangle((1.6,5.4),6.8,1.5,fc=CODE,ec='#3a2f26'))
ax.text(2.0,6.0,'print("Hello, AI!")',color=GRN,fontsize=18,family='monospace')
# labels with arrows
ax.annotate('the command:\n"show this"',xy=(2.6,5.4),xytext=(1.0,2.8),color=SAF,fontsize=9.5,fontweight='bold',ha='center',arrowprops=dict(arrowstyle='->',color=SAF,lw=1.6))
ax.annotate('the brackets:\n"here is what"',xy=(4.2,5.4),xytext=(4.4,2.8),color=BLU,fontsize=9.5,fontweight='bold',ha='center',arrowprops=dict(arrowstyle='->',color=BLU,lw=1.6))
ax.annotate('the text (a "string")\nin quotes',xy=(6.2,5.4),xytext=(8.0,2.8),color=YEL,fontsize=9.5,fontweight='bold',ha='center',arrowprops=dict(arrowstyle='->',color=YEL,lw=1.6))
plt.tight_layout(); plt.savefig('topics/27-python/images/4-anatomy.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 5: THE 30-DAY PYTHON PATH =====
fig,ax=plt.subplots(figsize=(11,3.8)); fig.patch.set_facecolor(BG); frame(ax,(0,20),(0,10))
ax.set_title('Your 30-day Python journey',fontsize=12.5,fontweight='bold',color=FG)
parts=[('Days 1-8','Basics\n(you are here)',SAF),('Days 9-16','Collections\n& Loops',BLU),
       ('Days 17-24','Functions\n& OOP',GRN),('Days 25-30','AI Toolkit\n(numpy, pandas)',PUR)]
for i,(d,t,c) in enumerate(parts):
    x=0.6+i*4.85
    ax.add_patch(FancyBboxPatch((x,3.0),4.0,4.0,boxstyle="round,pad=0.06",fc=CARD,ec=c,lw=1.8))
    ax.text(x+2.0,5.7,d,ha='center',color=c,fontsize=11,fontweight='bold')
    ax.text(x+2.0,4.2,t,ha='center',color=FG,fontsize=9.5)
    if i<3: ax.annotate('',xy=(x+4.85,5.0),xytext=(x+4.05,5.0),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
plt.tight_layout(); plt.savefig('topics/27-python/images/5-path.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("py day1 images generated")
