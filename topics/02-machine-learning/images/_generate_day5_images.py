import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; TEAL='#4EC5E8'; GRN='#3dd4a8'; YEL='#FFCF6B'; GOLD='#E0B265'; MUT='#b3a595'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# IMG 1: the best-fit line through data (house size -> price)
np.random.seed(7)
fig,ax=plt.subplots(figsize=(8.5,5)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
size=np.array([500,750,1000,1250,1500,1750,2000])
price=np.array([25,34,41,52,58,69,76])+np.random.randn(7)*2
ax.scatter(size,price,s=150,color=SAF,edgecolor=FG,zorder=3,label='Actual houses (data)')
m,b=np.polyfit(size,price,1); xs=np.linspace(400,2100,50)
ax.plot(xs,m*xs+b,color=TEAL,lw=3,zorder=2,label='Best-fit line (the model)')
ax.set_xlabel('House size (sq ft)',fontsize=12,fontweight='bold')
ax.set_ylabel('Price (lakhs)',fontsize=12,fontweight='bold')
ax.set_title('Linear Regression = the best straight line through your data',fontsize=12,fontweight='bold',color=FG)
leg=ax.legend(fontsize=10,facecolor=CARD,edgecolor='#3a2f26')
for t in leg.get_texts(): t.set_color(FG)
ax.grid(alpha=0.15,color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/12-best-fit-line.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 2: what "best" means — residuals (errors) to minimize
fig,ax=plt.subplots(figsize=(8.5,5)); fig.patch.set_facecolor(BG); ax.set_facecolor(CARD)
for s in ax.spines.values(): s.set_color('#3a2f26')
x=np.array([1,2,3,4,5]); y=np.array([2.2,3.9,5.5,7.0,9.2])
m,b=np.polyfit(x,y,1); yp=m*x+b
ax.plot(np.linspace(0.5,5.5,20),m*np.linspace(0.5,5.5,20)+b,color=TEAL,lw=3,zorder=2,label='The line')
ax.scatter(x,y,s=150,color=SAF,edgecolor=FG,zorder=4,label='Real points')
for xi,yi,ypi in zip(x,y,yp):
    ax.plot([xi,xi],[yi,ypi],color=YEL,lw=2.5,ls='--',zorder=3)
ax.plot([],[],color=YEL,lw=2.5,ls='--',label='Error (residual)')
ax.set_title('"Best" line = the one with the SMALLEST total error',fontsize=12,fontweight='bold',color=FG)
ax.set_xlabel('input',fontsize=11,fontweight='bold'); ax.set_ylabel('output',fontsize=11,fontweight='bold')
leg=ax.legend(fontsize=10,facecolor=CARD,edgecolor='#3a2f26')
for t in leg.get_texts(): t.set_color(FG)
ax.grid(alpha=0.15,color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/13-residuals.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG 3: the equation y = mx + c, annotated
fig,ax=plt.subplots(figsize=(10,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,4); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(5,3.5,'The formula behind the line',ha='center',fontsize=13,fontweight='bold',color=FG)
ax.text(5,2.2,'y  =  m·x  +  c',ha='center',fontsize=34,fontweight='bold',color=SAF,family='monospace')
notes=[('y','what we predict (price)',2.9,GRN),('m','slope — how steep',4.2,TEAL),('x','the input (size)',5.9,YEL),('c','starting value',7.4,GOLD)]
for sym,desc,x,c in notes:
    ax.annotate(desc,xy=(x,2.0),xytext=(x-0.3,0.7),fontsize=9.5,color=c,ha='center',
                arrowprops=dict(arrowstyle='->',color=c,lw=1.3))
ax.text(5,0.15,'Training just finds the best m and c so the line fits your data.',ha='center',fontsize=10,color=MUT,style='italic')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/14-line-equation.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("day5 images generated")
