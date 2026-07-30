import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'; PUR='#c39bd3'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
def box(ax,x,y,w,h,color,text,tcolor='#1a1512',fs=10,ec=None):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05,rounding_size=0.12",
                 fc=color,ec=ec or FG,lw=1.4,alpha=0.94,zorder=2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=tcolor,fontsize=fs,fontweight='bold',zorder=3)

# ===== 1: YOU'RE NOT STARTING FROM ZERO — the house already has a foundation =====
fig,ax=plt.subplots(figsize=(9.2,5.2)); fig.patch.set_facecolor(BG); frame(ax)
ax.set_title('You are NOT starting from zero — you already built the foundation',fontsize=12.5,fontweight='bold',color=FG)
# foundation = existing dev skills (wide green base)
box(ax,1.2,1.4,7.6,1.8,GRN,'YOUR DEV SKILLS  (already yours)\ncoding · logic · debugging · APIs · git · shipping',tcolor='#1a1512',fs=10.5)
# the new floor to add
box(ax,2.4,3.7,5.2,1.6,YEL,'+ AI layer on top\n(the new floor)',tcolor='#1a1512',fs=11)
ax.annotate('',xy=(5.0,3.6),xytext=(5.0,3.25),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.6))
box(ax,3.2,6.0,3.6,1.4,SAF,'AI ENGINEER',tcolor='#1a1512',fs=13)
ax.annotate('',xy=(5.0,5.9),xytext=(5.0,5.4),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.6))
ax.text(5.0,0.6,'Becoming an AI engineer = adding a floor, NOT rebuilding the house',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/20-ai-careers/images/1-foundation.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 2: THE 5-STAGE ROADMAP =====
fig,ax=plt.subplots(figsize=(12,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,24),(0,10))
ax.set_title('The roadmap: 5 floors, built one at a time (I teach each, month by month)',fontsize=12.5,fontweight='bold',color=FG)
stages=[('1  Python\n+ Data','pandas, numpy,\nthe basics',BLU),
        ('2  Machine\nLearning','the algorithms\n+ how to use them',SAF),
        ('3  Deep\nLearning','neural nets,\nCNN, RNN',GRN),
        ('4  GenAI\n+ LLMs','transformers,\nLLMs, RAG, agents',PUR),
        ('5  Ship it\n(MLOps)','deploy, APIs,\nreal projects',YEL)]
for i,(t,sub,col) in enumerate(stages):
    x=0.6+i*4.7
    ax.add_patch(FancyBboxPatch((x,3.0),4.0,4.0,boxstyle="round,pad=0.06",fc=CARD,ec=col,lw=1.9))
    ax.text(x+2.0,5.9,t,ha='center',color=col,fontsize=11.5,fontweight='bold')
    ax.text(x+2.0,4.1,sub,ha='center',color=FG,fontsize=9.5)
    if i<4: ax.annotate('',xy=(x+4.7,5.0),xytext=(x+4.05,5.0),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.6))
plt.tight_layout(); plt.savefig('topics/20-ai-careers/images/2-roadmap.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 3: WHAT TO SKIP vs WHAT TO LEARN (myth-busting) =====
fig,axes=plt.subplots(1,2,figsize=(11,4.8)); fig.patch.set_facecolor(BG)
ax=axes[0]; frame(ax)
ax.set_title("You DON'T need (the myths)",fontsize=12,fontweight='bold',color=RED)
skips=['A PhD or a Master\'s degree','Heavy university-level maths','To memorise every algorithm','To build models from scratch','Years before you start']
for i,t in enumerate(skips):
    ax.text(0.6,8.2-i*1.55,'✗',color=RED,fontsize=15,fontweight='bold')
    ax.text(1.4,8.2-i*1.55,t,va='center',color=FG,fontsize=10.5,fontweight='bold')
ax=axes[1]; frame(ax)
ax.set_title('You DO need (the truth)',fontsize=12,fontweight='bold',color=GRN)
dos=['Python + a bit of maths intuition','To USE libraries (sklearn, PyTorch)','To understand WHEN to use what','To build real projects','To start now, learn as you build']
for i,t in enumerate(dos):
    ax.text(0.6,8.2-i*1.55,'✓',color=GRN,fontsize=15,fontweight='bold')
    ax.text(1.4,8.2-i*1.55,t,va='center',color=FG,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/20-ai-careers/images/3-myths.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 4: LEARN BY BUILDING — the project ladder =====
fig,ax=plt.subplots(figsize=(9.2,5.4)); fig.patch.set_facecolor(BG); frame(ax)
ax.set_title('Escape "tutorial hell" — climb the project ladder',fontsize=12.5,fontweight='bold',color=FG)
rungs=[('a price / spam predictor',BLU,1.4),
       ('a recommendation app',SAF,3.0),
       ('an image classifier',GRN,4.6),
       ('a chatbot with your own docs (RAG)',PUR,6.2),
       ('a deployed AI product (portfolio!)',YEL,7.8)]
for t,c,y in rungs:
    box(ax,2.0,y,6.6,1.15,c,t,tcolor='#1a1512',fs=10)
    if y<7.0: ax.annotate('',xy=(5.3,y+1.55),xytext=(5.3,y+1.1),arrowprops=dict(arrowstyle='->',color=MUT,lw=1.8))
ax.text(5.3,0.6,'Each project teaches more than 10 tutorials — and becomes your portfolio',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/20-ai-careers/images/4-projects.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 5: THE 4-5 MONTH TIMELINE =====
fig,ax=plt.subplots(figsize=(11,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Your 4-5 month journey (follow along — one topic at a time)',fontsize=12.5,fontweight='bold',color=FG)
# timeline
ax.annotate('',xy=(11.4,7.2),xytext=(0.6,7.2),arrowprops=dict(arrowstyle='->',color=MUT,lw=2))
months=[('Month 1','Python +\nML basics',BLU),('Month 2','ML mastery\n+ projects',SAF),
        ('Month 3','Deep Learning\n(NN, CNN, RNN)',GRN),('Month 4','GenAI: LLMs,\nRAG, agents',PUR),
        ('Month 5','Deploy +\nportfolio',YEL)]
for i,(m,t,c) in enumerate(months):
    x=0.9+i*2.25
    ax.add_patch(Circle((x+0.5,7.2),0.24,fc=c,ec=FG,lw=1.2,zorder=3))
    ax.add_patch(FancyBboxPatch((x-0.35,3.4),2.0,3.0,boxstyle="round,pad=0.05",fc=CARD,ec=c,lw=1.5))
    ax.text(x+0.65,5.6,m,ha='center',color=c,fontsize=10,fontweight='bold')
    ax.text(x+0.65,4.3,t,ha='center',color=FG,fontsize=8.8)
ax.text(6.0,1.4,'5 months of steady effort while working → AI Engineer. I teach each step.',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/20-ai-careers/images/5-timeline.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("dev-to-ai images generated")
