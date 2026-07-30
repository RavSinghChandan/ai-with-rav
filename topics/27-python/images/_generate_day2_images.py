import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import numpy as np
BG='#1a1512'; CARD='#241d18'; FG='#f0e6d8'; SAF='#FF7A3D'; YEL='#FFCF6B'; MUT='#b3a595'; RED='#e06a6a'
GRN='#5fd06a'; BLU='#4EC5E8'; PUR='#c39bd3'; CODE='#140f0c'
plt.rcParams.update({'text.color':FG})
def frame(ax,xlim=(0,10),ylim=(0,10)):
    ax.set_facecolor(CARD)
    for s in ax.spines.values(): s.set_color('#3a2f26')
    ax.set_xticks([]); ax.set_yticks([]); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
def box(ax,x,y,w,h,color,text,tcolor='#1a1512',fs=10,ec=None):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05,rounding_size=0.12",
                 fc=color,ec=ec or FG,lw=1.4,alpha=0.94,zorder=2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=tcolor,fontsize=fs,fontweight='bold',zorder=3)

# 6: VARIABLE = a labelled box holding a value
fig,ax=plt.subplots(figsize=(9.0,4.4)); fig.patch.set_facecolor(BG); frame(ax)
ax.set_title('A variable = a labelled box that holds a value',fontsize=12.5,fontweight='bold',color=FG)
# the box
ax.add_patch(FancyBboxPatch((3.4,3.4),3.2,2.6,boxstyle="round,pad=0.05",fc=YEL,ec=FG,lw=1.6))
ax.text(5.0,4.7,'30',ha='center',va='center',color='#1a1512',fontsize=26,fontweight='bold')
# label
ax.text(5.0,6.6,'age',ha='center',color=SAF,fontsize=15,fontweight='bold')
ax.annotate('',xy=(5.0,6.05),xytext=(5.0,6.35),arrowprops=dict(arrowstyle='->',color=SAF,lw=2))
ax.add_patch(Rectangle((1.0,1.2),8.0,1.1,fc=CODE,ec='#3a2f26'))
ax.text(1.4,1.6,'age = 30',color=GRN,fontsize=14,family='monospace')
ax.text(5.0,0.5,'The name "age" is the label · 30 is what\'s inside the box',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/6-variable-box.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 7: THE 4 BASIC TYPES
fig,ax=plt.subplots(figsize=(9.6,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('The 4 everyday data types',fontsize=12.5,fontweight='bold',color=FG)
types=[('int','whole number','5',BLU),('float','decimal number','5.5',SAF),
       ('str','text (string)','"Rav"',GRN),('bool','yes / no','True',PUR)]
for i,(t,d,ex,c) in enumerate(types):
    x=0.6+i*2.9
    box(ax,x,4.2,2.5,3.0,c,f'{t}\n\n{d}',tcolor='#1a1512',fs=10.5)
    ax.add_patch(Rectangle((x,2.6),2.5,1.0,fc=CODE,ec='#3a2f26'))
    ax.text(x+1.25,3.1,ex,ha='center',va='center',color=YEL,fontsize=12,family='monospace',fontweight='bold')
ax.text(6.0,1.0,'int = counting · float = measuring · str = words · bool = a switch',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/7-types.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 8: REASSIGNING — the box can be refilled
fig,ax=plt.subplots(figsize=(9.4,3.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('A variable can be re-filled — the label stays, the value changes',fontsize=11.5,fontweight='bold',color=FG)
ax.add_patch(Rectangle((0.6,6.6),5.0,1.0,fc=CODE,ec='#3a2f26'))
ax.text(0.9,7.0,'score = 10',color=GRN,fontsize=12,family='monospace')
ax.add_patch(Rectangle((0.6,5.2),5.0,1.0,fc=CODE,ec='#3a2f26'))
ax.text(0.9,5.6,'score = 25',color=GRN,fontsize=12,family='monospace')
box(ax,7.0,5.6,3.4,2.2,YEL,'score\nnow holds\n25',tcolor='#1a1512',fs=11)
ax.annotate('',xy=(7.0,6.7),xytext=(5.7,6.7),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.2))
ax.text(6.0,2.6,'The second line replaces the value. "score" is now 25 (10 is gone).',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/8-reassign.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 9: NAMING RULES
fig,axes=plt.subplots(1,2,figsize=(11,4.4)); fig.patch.set_facecolor(BG)
ax=axes[0]; frame(ax)
ax.set_title('Good variable names',fontsize=12,fontweight='bold',color=GRN)
good=['user_age','total_price','is_ready','first_name']
for i,t in enumerate(good):
    ax.text(0.8,8.0-i*1.7,'✓',color=GRN,fontsize=15,fontweight='bold')
    ax.text(1.7,8.0-i*1.7,t,va='center',color=FG,fontsize=12,family='monospace',fontweight='bold')
ax.text(5,0.7,'clear · lowercase · words joined by _',ha='center',color=GRN,fontsize=9.5,fontweight='bold')
ax=axes[1]; frame(ax)
ax.set_title('Names to avoid',fontsize=12,fontweight='bold',color=RED)
bad=[('x','too vague'),('2fast','can\'t start with a number'),('my age','no spaces allowed'),('print','a Python word')]
for i,(t,why) in enumerate(bad):
    ax.text(0.8,8.0-i*1.7,'✗',color=RED,fontsize=15,fontweight='bold')
    ax.text(1.7,8.0-i*1.7,t,va='center',color=FG,fontsize=12,family='monospace',fontweight='bold')
    ax.text(5.2,8.0-i*1.7,f'({why})',va='center',color=MUT,fontsize=9)
plt.tight_layout(); plt.savefig('topics/27-python/images/9-naming.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 10: type() — asking what's in the box
fig,ax=plt.subplots(figsize=(9.0,3.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('type() tells you what kind of value a variable holds',fontsize=12,fontweight='bold',color=FG)
rows=[('age = 30','type(age)','int',BLU),('price = 9.99','type(price)','float',SAF),('name = "Rav"','type(name)','str',GRN)]
for i,(assign,call,res,c) in enumerate(rows):
    y=7.2-i*2.0
    ax.add_patch(Rectangle((0.6,y),4.4,1.2,fc=CODE,ec='#3a2f26'))
    ax.text(0.9,y+0.55,f'{assign}',color=FG,fontsize=10,family='monospace')
    ax.annotate('',xy=(7.0,y+0.6),xytext=(5.2,y+0.6),arrowprops=dict(arrowstyle='->',color=YEL,lw=1.8))
    box(ax,7.2,y,3.8,1.2,c,res,tcolor='#1a1512',fs=11)
plt.tight_layout(); plt.savefig('topics/27-python/images/10-type.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("py day2 images generated")
