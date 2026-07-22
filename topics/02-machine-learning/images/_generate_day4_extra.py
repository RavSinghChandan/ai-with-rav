import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
BG='#0d1117'; FG='#e6edf3'; SAF='#FF6B35'; TEAL='#33B5E5'; GRN='#06D6A0'; YEL='#FFD166'; MUT='#9fb3c8'
plt.rcParams.update({'text.color':FG,'axes.labelcolor':FG,'xtick.color':FG,'ytick.color':FG})

# IMG: more data beats a cleverer model — accuracy rises with data
fig,ax=plt.subplots(figsize=(9,4.8)); fig.patch.set_facecolor(BG); ax.set_facecolor('#161b22')
for s in ax.spines.values(): s.set_color('#30363d')
x=np.array([100,500,1000,2000,5000])
simple=np.array([62,74,82,87,91])
fancy=np.array([70,78,84,88,92])
ax.plot(x,simple,'-o',color=TEAL,lw=3,ms=9,label='Simple model + more data')
ax.plot(x,fancy,'--s',color=SAF,lw=2,ms=7,label='Fancy model')
ax.axhline(91,color=GRN,ls=':',lw=1.5)
ax.annotate('simple model with 5000 rows\nbeats fancy model with few rows',
            xy=(5000,91),xytext=(1600,66),fontsize=10,color=GRN,
            arrowprops=dict(arrowstyle='->',color=GRN,lw=1.5))
ax.set_xlabel('Amount of good data (rows)',fontsize=12,fontweight='bold')
ax.set_ylabel('Accuracy (%)',fontsize=12,fontweight='bold')
ax.set_title('More good data usually beats a cleverer model',fontsize=12,fontweight='bold',color=FG)
leg=ax.legend(fontsize=10,facecolor='#161b22',edgecolor='#30363d')
for t in leg.get_texts(): t.set_color(FG)
ax.grid(alpha=0.15,color=FG)
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/10-more-data.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# IMG: good features = raw date -> engineered features
fig,ax=plt.subplots(figsize=(11,4.2)); ax.set_xlim(0,12); ax.set_ylim(0,6); ax.axis('off'); fig.patch.set_facecolor(BG)
ax.text(6,5.5,'Feature Engineering — turn raw data into useful clues',ha='center',fontsize=13,fontweight='bold',color=FG)
# raw
ax.add_patch(FancyBboxPatch((0.5,2.2),3.2,1.4,boxstyle="round,pad=0.06",fc='#5a2020',ec=FG,lw=1.4))
ax.text(2.1,2.9,'RAW\n"2026-07-22"',ha='center',va='center',color=FG,fontsize=11,fontweight='bold')
ax.text(2.1,1.7,'useless to the model',ha='center',color=MUT,fontsize=9,style='italic')
# arrow
ax.add_patch(FancyArrowPatch((3.9,2.9),(5.1,2.9),arrowstyle='-|>',mutation_scale=22,lw=2.4,color=YEL))
ax.text(4.5,3.4,'engineer',ha='center',color=YEL,fontsize=9,fontweight='bold')
# engineered - three chips
chips=[('is_weekend = No',GRN,8.6),('is_salary_day = No',TEAL,4.0),('month = July',SAF,1.4)]
for txt,c,y in chips:
    ax.add_patch(FancyBboxPatch((5.4,y),4.2,1.0,boxstyle="round,pad=0.05",fc=c,ec=FG,lw=1.2))
    ax.text(7.5,y+0.5,txt,ha='center',va='center',color='#0d1117',fontsize=10,fontweight='bold')
ax.text(7.5,0.6,'now the model can learn patterns!',ha='center',color=GRN,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/02-machine-learning/images/11-feature-engineering.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("2 extra day4 images generated")
