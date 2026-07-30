import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Wedge
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'; PUR='#c39bd3'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)

# ===== 70: THE FULL WORKFLOW — 6 stages, cooking-a-meal thread =====
fig,ax=plt.subplots(figsize=(12,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,24),(0,10))
ax.set_title('The ML project journey — like cooking a great meal, in order',fontsize=13,fontweight='bold',color=FG)
stages=[('1  Define','the dish\n(the question)',SAF),
        ('2  Data','buy + clean\ningredients',BLU),
        ('3  Features','prep + cut',YEL),
        ('4  Train','cook +\ntaste-test',GRN),
        ('5  Deploy','serve to\nguests',PUR),
        ('6  Monitor','keep fresh\n(retrain)',SAF)]
for i,(t,sub,col) in enumerate(stages):
    x=0.6+i*3.85
    ax.add_patch(FancyBboxPatch((x,3.2),3.2,3.6,boxstyle="round,pad=0.06",fc=CARD,ec=col,lw=1.8))
    ax.text(x+1.6,5.9,t,ha='center',color=col,fontsize=11,fontweight='bold')
    ax.text(x+1.6,4.4,sub,ha='center',color=FG,fontsize=9.5)
    if i<5: ax.annotate('',xy=(x+3.85,5.0),xytext=(x+3.25,5.0),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/70-workflow.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 71: 80% IS THE BORING DATA PART =====
fig,ax=plt.subplots(figsize=(8.4,5.2)); fig.patch.set_facecolor(BG)
ax.set_facecolor(BG); ax.axis('off')
# donut: 80% data prep (blue), 20% modelling (green). Labels placed at each
# wedge's own centroid via the returned wedge objects so they can never mismatch.
sizes=[80,20]; cols=[BLU,GRN]
wedges,_=ax.pie(sizes,colors=cols,startangle=90,counterclock=False,
                wedgeprops=dict(edgecolor=BG,linewidth=3,width=0.55))
lbls=['Data\n& cleaning\n80%','Modelling\n20%']
lcols=[BLU,GRN]
for wdg,lb,lc in zip(wedges,lbls,lcols):
    ang=np.deg2rad((wdg.theta1+wdg.theta2)/2)          # mid-angle of THIS wedge
    r=1.32
    ax.text(r*np.cos(ang),r*np.sin(ang),lb,ha='center',va='center',color=lc,fontsize=11.5,fontweight='bold')
ax.text(0,0,'where the\ntime goes',ha='center',va='center',color=FG,fontsize=11,fontweight='bold')
ax.set_xlim(-1.9,1.9); ax.set_ylim(-1.7,1.7)
ax.set_title('The surprise: most ML work is CLEANING data, not fancy models',fontsize=12,fontweight='bold',color=FG,y=1.02)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/71-80percent.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 72: WHERE THE MONTH'S LESSONS FIT =====
fig,ax=plt.subplots(figsize=(9.2,5.0)); fig.patch.set_facecolor(BG); frame(ax,(0,10),(0,10))
ax.set_title('Everything you learned this month slots into ONE stage: "Train + taste"',fontsize=11.5,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((0.6,5.2),8.8,3.4,boxstyle="round,pad=0.06",fc=CARD,ec=GRN,lw=1.8))
ax.text(5.0,8.1,'Stage 4: Train + Taste-test',ha='center',color=GRN,fontsize=12,fontweight='bold')
items=['the algorithms (Days 5-13)','tuning & the sweet spot (Days 15-16)','precision / recall / F1 (Day 17)']
for i,t in enumerate(items):
    ax.text(5.0,7.2-i*0.7,'• '+t,ha='center',color=FG,fontsize=10.5,fontweight='bold')
ax.text(5.0,3.6,'But that\'s only 1 of the 6 stages.',ha='center',color=YEL,fontsize=11,fontweight='bold')
ax.text(5.0,2.4,'A real ML engineer owns ALL six — data, features, deploy, and monitoring too.',
        ha='center',color=FG,fontsize=10)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/72-lessons-fit.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 73: DEPLOY — laptop to real users =====
fig,ax=plt.subplots(figsize=(9.2,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Deploy: the model leaves your laptop and serves real people',fontsize=12.5,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((0.6,3.6),3.0,3.2,boxstyle="round,pad=0.06",fc=CARD,ec=MUT,lw=1.6))
ax.text(2.1,6.0,'your laptop',ha='center',color=MUT,fontsize=10,fontweight='bold')
ax.text(2.1,4.7,'trained\nmodel',ha='center',color=FG,fontsize=10,fontweight='bold')
ax.add_patch(FancyBboxPatch((4.6,3.6),3.0,3.2,boxstyle="round,pad=0.06",fc=CARD,ec=BLU,lw=1.6))
ax.text(6.1,6.0,'a server (API)',ha='center',color=BLU,fontsize=10,fontweight='bold')
ax.text(6.1,4.7,'always on,\nanswers requests',ha='center',color=FG,fontsize=9.5)
ax.add_patch(FancyBboxPatch((8.6,3.6),3.0,3.2,boxstyle="round,pad=0.06",fc=CARD,ec=GRN,lw=1.6))
ax.text(10.1,6.0,'real users',ha='center',color=GRN,fontsize=10,fontweight='bold')
ax.text(10.1,4.7,'the app / phone',ha='center',color=FG,fontsize=9.5)
ax.annotate('',xy=(4.6,5.2),xytext=(3.6,5.2),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
ax.annotate('',xy=(8.6,5.2),xytext=(7.6,5.2),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
ax.text(6.0,1.8,'A model that stays on your laptop helps no one — deploying is what makes it real',
        ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/73-deploy.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ===== 74: THE LOOP — monitor, drift, retrain =====
fig,ax=plt.subplots(figsize=(7.6,6.0)); fig.patch.set_facecolor(BG); frame(ax); ax.set_aspect('equal')
ax.set_title('It is never "done": models go stale, so you loop',fontsize=12,fontweight='bold',color=FG)
# 4 nodes in a circle
nodes=[('Deploy',5,8.4,GRN),('Monitor',8.4,5,BLU),('Data drifts\n(world changes)',5,1.6,RED),('Retrain',1.6,5,SAF)]
for t,x,y,col in nodes:
    ax.add_patch(Circle((x,y),1.15,fc=CARD,ec=col,lw=2))
    ax.text(x,y,t,ha='center',va='center',color=col,fontsize=9.5,fontweight='bold')
# arrows clockwise — shorten each so it starts/ends at the CIRCLE EDGE (r=1.15),
# not the centre, so the arrowheads never clip the node labels.
centres=[(5,8.4),(8.4,5),(5,1.6),(1.6,5)]
R=1.35
for k in range(4):
    (x0,y0)=centres[k]; (x1,y1)=centres[(k+1)%4]
    dx,dy=x1-x0,y1-y0; d=(dx*dx+dy*dy)**0.5
    sx,sy=x0+dx/d*R, y0+dy/d*R          # start on the edge of node k
    ex,ey=x1-dx/d*R, y1-dy/d*R          # end just before node k+1
    ax.annotate('',xy=(ex,ey),xytext=(sx,sy),
                arrowprops=dict(arrowstyle='->',color=YEL,lw=2.2,connectionstyle='arc3,rad=0.22'))
ax.text(5,5,'the ML\nlifecycle',ha='center',va='center',color=MUT,fontsize=10,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/74-loop.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day18 images generated")
