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

# 36: converting = translating between box types
fig,ax=plt.subplots(figsize=(9.4,4.2)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Converting = translating a value into another type',fontsize=12,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((0.8,4.4),3.2,2.6,boxstyle="round,pad=0.05",fc=BLU,ec=FG,lw=1.4))
ax.text(2.4,6.1,'"30"',ha='center',va='center',color='#1a1512',fontsize=17,fontweight='bold')
ax.text(2.4,4.9,'str (text)',ha='center',color=BLU,fontsize=10,fontweight='bold')
ax.annotate('',xy=(7.9,5.7),xytext=(4.1,5.7),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.4))
ax.text(6.0,6.3,'int(...)',ha='center',color=YEL,fontsize=12,fontweight='bold',family='monospace')
ax.add_patch(FancyBboxPatch((8.0,4.4),3.2,2.6,boxstyle="round,pad=0.05",fc=GRN,ec=FG,lw=1.4))
ax.text(9.6,6.1,'30',ha='center',va='center',color='#1a1512',fontsize=17,fontweight='bold')
ax.text(9.6,4.9,'int (number)',ha='center',color=GRN,fontsize=10,fontweight='bold')
ax.text(6.0,2.6,'int("30") turns the TEXT "30" into the NUMBER 30 you can do maths with.',ha='center',color=YEL,fontsize=10,fontweight='bold')
ax.text(6.0,1.5,'The value stays the same — only its TYPE changes.',ha='center',color=MUT,fontsize=9.5)
plt.tight_layout(); plt.savefig('topics/27-python/images/36-convert.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 37: the three converters
fig,ax=plt.subplots(figsize=(9.4,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('The three everyday converters',fontsize=12.5,fontweight='bold',color=FG)
cards=[('int()','text/decimal\n-> whole number','int("30") -> 30\nint(7.9) -> 7',GRN),
       ('float()','text/int\n-> decimal','float("3.5") -> 3.5\nfloat(7) -> 7.0',BLU),
       ('str()','anything\n-> text','str(30) -> "30"\nstr(True) -> "True"',SAF)]
x=0.6
for name,what,ex,col in cards:
    ax.add_patch(FancyBboxPatch((x,2.2),3.5,6.2,boxstyle="round,pad=0.05",fc=CARD,ec=col,lw=1.6))
    ax.text(x+1.75,7.7,name,ha='center',color=col,fontsize=15,fontweight='bold',family='monospace')
    ax.text(x+1.75,6.1,what,ha='center',va='center',color=FG,fontsize=10)
    ax.add_patch(Rectangle((x+0.25,2.6),3.0,1.9,fc=CODE,ec='#3a2f26'))
    ax.text(x+1.75,3.55,ex,ha='center',va='center',color=col,fontsize=9,family='monospace')
    x+=3.75
ax.text(6.0,0.9,'int() drops the decimal (does NOT round): int(7.9) is 7, not 8.',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/37-converters.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 38: an error is Python telling you what's wrong
fig,ax=plt.subplots(figsize=(9.4,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('An error is a helpful message, not a disaster',fontsize=12,fontweight='bold',color=FG)
ax.add_patch(Rectangle((0.6,4.6),10.8,3.6,fc=CODE,ec=RED,lw=1.5))
ax.text(0.9,7.5,'>>> "age " + 30',color=MUT,fontsize=11,family='monospace')
ax.text(0.9,6.5,'TypeError: can only concatenate',color=RED,fontsize=11.5,family='monospace',fontweight='bold')
ax.text(0.9,5.6,'str (not "int") to str',color=RED,fontsize=11.5,family='monospace',fontweight='bold')
ax.annotate('the TYPE of problem',xy=(2.3,6.5),xytext=(6.6,7.8),arrowprops=dict(arrowstyle='->',color=YEL,lw=1.5),color=YEL,fontsize=9.5)
ax.annotate('what actually went wrong',xy=(4.5,5.6),xytext=(7.0,4.9),arrowprops=dict(arrowstyle='->',color=BLU,lw=1.5),color=BLU,fontsize=9.5)
ax.text(6.0,3.4,'It tells you: you tried to glue text and a number. Fix: str(30) first.',ha='center',color=GRN,fontsize=10,fontweight='bold')
ax.text(6.0,2.0,'Read the LAST line first — it names the problem. Errors are clues, not scolding.',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/38-error.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 39: common beginner errors
fig,ax=plt.subplots(figsize=(9.4,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Three errors you WILL meet (and their fix)',fontsize=12,fontweight='bold',color=FG)
rows=[('TypeError','"age " + 30','mixing text and number','str(30), or use commas / f-string'),
      ('ValueError','int("hello")','converting text that isn\'t a number','check the text first'),
      ('NameError','print(scoree)','a typo in a variable name','fix the spelling: score')]
y=7.9
for name,code,mean,fix in rows:
    ax.add_patch(Rectangle((0.5,y-0.75),2.7,1.35,fc=CODE,ec=RED,lw=1.2))
    ax.text(1.85,y-0.08,name,ha='center',va='center',color=RED,fontsize=10.5,fontweight='bold',family='monospace')
    ax.text(3.5,y+0.25,code,ha='left',va='center',color=YEL,fontsize=9.5,family='monospace')
    ax.text(3.5,y-0.35,mean,ha='left',va='center',color=MUT,fontsize=9)
    ax.text(3.5,y-0.72,'fix: '+fix,ha='left',va='center',color=GRN,fontsize=8.8)
    y-=2.0
plt.tight_layout(); plt.savefig('topics/27-python/images/39-common-errors.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 40: Part 1 complete map
fig,ax=plt.subplots(figsize=(9.4,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Part 1 complete — the foundation is laid',fontsize=12.5,fontweight='bold',color=FG)
items=['1  Why Python','2  Variables','3  Strings','4  Numbers',
       '5  Input/Output','6  Booleans','7  If/Elif/Else','8  Convert & Errors']
xs=[0.7,3.55,6.4,9.25]; ys=[5.9,3.4]
i=0
for r,yy in enumerate(ys):
    for c in range(4):
        x=xs[c]
        ax.add_patch(FancyBboxPatch((x,yy),2.55,1.7,boxstyle="round,pad=0.04",fc=CARD,ec=GRN,lw=1.3))
        ax.text(x+1.27,yy+0.85,items[i],ha='center',va='center',color=FG,fontsize=9.5,fontweight='bold')
        ax.text(x+2.25,yy+1.35,'v',ha='center',va='center',color=GRN,fontsize=11,fontweight='bold')
        i+=1
ax.text(6.0,1.6,'You can now store data, do maths, talk to the user, and make decisions.',ha='center',color=YEL,fontsize=10,fontweight='bold')
ax.text(6.0,0.7,'Next (Part 2): Collections — lists & dictionaries — and Loops.',ha='center',color=SAF,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/40-part1-map.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("py day8 images generated")
