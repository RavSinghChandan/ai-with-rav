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
def cb(ax,x,y,w,h,text,col=GRN,fs=11):
    ax.add_patch(Rectangle((x,y),w,h,fc=CODE,ec='#3a2f26'))
    ax.text(x+0.3,y+h/2,text,va='center',color=col,fontsize=fs,family='monospace')

# 16: THE BASIC OPERATORS
fig,ax=plt.subplots(figsize=(9.6,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Python is a calculator: the everyday operators',fontsize=12.5,fontweight='bold',color=FG)
ops=[('+','add','7 + 2','9',BLU),('-','subtract','7 - 2','5',SAF),
     ('*','multiply','7 * 2','14',GRN),('/','divide','7 / 2','3.5',PUR)]
for i,(o,d,ex,res,c) in enumerate(ops):
    x=0.6+i*2.9
    ax.add_patch(FancyBboxPatch((x,4.4),2.5,3.0,boxstyle="round,pad=0.05",fc=c,ec=FG,lw=1.3))
    ax.text(x+1.25,6.6,o,ha='center',color='#1a1512',fontsize=22,fontweight='bold')
    ax.text(x+1.25,5.2,d,ha='center',color='#1a1512',fontsize=10,fontweight='bold')
    ax.add_patch(Rectangle((x,2.7),2.5,1.1,fc=CODE,ec='#3a2f26'))
    ax.text(x+1.25,3.25,f'{ex}={res}',ha='center',va='center',color=YEL,fontsize=10,family='monospace',fontweight='bold')
ax.text(6.0,1.2,'Note: / always gives a decimal (float): 4 / 2 = 2.0',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/16-operators.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 17: THE SPECIAL THREE // % **
fig,ax=plt.subplots(figsize=(9.6,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Three special operators worth knowing',fontsize=12.5,fontweight='bold',color=FG)
sp=[('//','floor divide\n(whole part only)','17 // 5','3',BLU),
    ('%','modulo\n(the remainder)','17 % 5','2',SAF),
    ('**','power','2 ** 3','8',GRN)]
for i,(o,d,ex,res,c) in enumerate(sp):
    x=0.8+i*3.7
    ax.add_patch(FancyBboxPatch((x,4.2),3.1,3.2,boxstyle="round,pad=0.05",fc=c,ec=FG,lw=1.3))
    ax.text(x+1.55,6.7,o,ha='center',color='#1a1512',fontsize=22,fontweight='bold')
    ax.text(x+1.55,5.1,d,ha='center',color='#1a1512',fontsize=9.5,fontweight='bold')
    ax.add_patch(Rectangle((x,2.6),3.1,1.1,fc=CODE,ec='#3a2f26'))
    ax.text(x+1.55,3.15,f'{ex} = {res}',ha='center',va='center',color=YEL,fontsize=11,family='monospace',fontweight='bold')
ax.text(6.0,1.2,'% is secretly useful: "is it even?" -> n % 2 == 0',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/17-special.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 18: INT vs FLOAT
fig,axes=plt.subplots(1,2,figsize=(11,3.8)); fig.patch.set_facecolor(BG)
ax=axes[0]; frame(ax)
ax.set_title('int — whole number',fontsize=12,fontweight='bold',color=BLU)
ax.add_patch(FancyBboxPatch((2.5,4.0),5,2.6,boxstyle="round,pad=0.05",fc=BLU,ec=FG,lw=1.4))
ax.text(5,5.3,'7',ha='center',va='center',color='#1a1512',fontsize=30,fontweight='bold')
ax.text(5,2.6,'for counting things\n(people, items)',ha='center',color=FG,fontsize=10,fontweight='bold')
ax=axes[1]; frame(ax)
ax.set_title('float — decimal number',fontsize=12,fontweight='bold',color=SAF)
ax.add_patch(FancyBboxPatch((2.5,4.0),5,2.6,boxstyle="round,pad=0.05",fc=SAF,ec=FG,lw=1.4))
ax.text(5,5.3,'7.5',ha='center',va='center',color='#1a1512',fontsize=30,fontweight='bold')
ax.text(5,2.6,'for measuring\n(price, weight, %)',ha='center',color=FG,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/18-int-float.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 19: ORDER OF OPERATIONS (BODMAS)
fig,ax=plt.subplots(figsize=(9.4,4.0)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Order matters: Python does × ÷ before + −  (like maths)',fontsize=11.5,fontweight='bold',color=FG)
cb(ax,0.6,6.6,10.8,1.2,'2 + 3 * 4   ->  14    (not 20 — the * happens first)',GRN,11)
cb(ax,0.6,4.4,10.8,1.2,'(2 + 3) * 4  ->  20    (brackets force the + first)',GRN,11)
ax.text(6.0,2.6,'Use brackets ( ) to control the order — and to make code clear',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/19-order.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 20: SHORTCUTS +=
fig,ax=plt.subplots(figsize=(9.4,4.0)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Handy shortcut: += (add to a variable)',fontsize=12,fontweight='bold',color=FG)
cb(ax,0.6,6.8,5.0,1.1,'score = 10',GRN,11)
cb(ax,0.6,5.4,5.0,1.1,'score = score + 5',MUT,11)
cb(ax,6.2,5.4,5.2,1.1,'score += 5',GRN,12)
ax.text(8.8,6.7,'same thing,\nshorter!',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
ax.annotate('',xy=(6.2,5.95),xytext=(5.6,5.95),arrowprops=dict(arrowstyle='->',color=YEL,lw=2))
ax.add_patch(FancyBboxPatch((3.4,2.0),5.2,1.6,boxstyle="round,pad=0.04",fc=GRN,ec=FG,lw=1.4))
ax.text(6.0,2.8,'score is now 15',ha='center',va='center',color='#1a1512',fontsize=12,fontweight='bold')
ax.text(6.0,0.9,'-= *= /= work the same way',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/20-shortcut.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("py day4 images generated")
