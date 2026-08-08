import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

# DARK theme palette (same as every other topic)
BG='#0d1117'; FG='#e6edf3'; SAFFRON='#FF6B35'; TEAL='#33B5E5'; GREEN='#06D6A0'; YELLOW='#FFD166'; RED='#F85149'; MUT='#8b949e'
plt.rcParams['text.color']=FG; plt.rcParams['axes.labelcolor']=FG
plt.rcParams['xtick.color']=FG; plt.rcParams['ytick.color']=FG

OUT=os.path.dirname(os.path.abspath(__file__))
def save(name):
    plt.savefig(os.path.join(OUT,name),dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# ---------- IMG 1: the inconsistency — same object, two outcomes ----------
fig, ax = plt.subplots(figsize=(12,5.4)); ax.set_xlim(0,24); ax.set_ylim(0,11); ax.axis('off')
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
def box(x,y,w,h,txt,c,tc='#0d1117',fs=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.05",fc=c,ec=FG,lw=1.6))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',color=tc,fontsize=fs,fontweight='bold')
def arrow(x1,y1,x2,y2,c=FG):
    ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=22,lw=2.6,color=c))

ax.text(12,10.3,'One object. Two different answers.',ha='center',fontsize=15,fontweight='bold',color=FG)
box(8.7,7.6,6.6,1.5,'BIDSPath object\n(has __fspath__)',YELLOW,fs=12)

# left branch: load works
arrow(10.0,7.5,6.2,6.0,GREEN)
box(3.0,4.4,6.4,1.5,'joblib.load(path)',TEAL,fs=13)
arrow(6.2,4.3,6.2,3.2,GREEN)
box(3.0,1.6,6.4,1.5,'works',GREEN,fs=14)

# right branch: dump fails
arrow(14.0,7.5,17.8,6.0,RED)
box(14.6,4.4,6.4,1.5,'joblib.dump(v, path)',TEAL,fs=13)
arrow(17.8,4.3,17.8,3.2,RED)
box(14.6,1.6,6.4,1.5,'ValueError',RED,fs=14)

ax.text(6.2,0.9,'open() honours the protocol',ha='center',fontsize=10.5,color=MUT,style='italic')
ax.text(17.8,0.9,'needs a real str, never got one',ha='center',fontsize=10.5,color=MUT,style='italic')
plt.tight_layout(); save('01-same-object-two-answers.png')

# ---------- IMG 2: the protocol vs the concrete class ----------
fig, ax = plt.subplots(figsize=(11,6)); ax.set_xlim(0,22); ax.set_ylim(0,12); ax.axis('off')
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(11,11.3,'What counts as "a path"?',ha='center',fontsize=15,fontweight='bold',color=FG)

# outer set: os.PathLike
ax.add_patch(FancyBboxPatch((1.2,1.4),19.6,8.6,boxstyle="round,pad=0.15",
                            fc='#161b22',ec=TEAL,lw=2.4))
ax.text(11,9.2,'os.PathLike   —   anything with __fspath__',ha='center',
        fontsize=13,fontweight='bold',color=TEAL)

# inner set: pathlib.Path
ax.add_patch(FancyBboxPatch((2.4,2.4),7.4,5.4,boxstyle="round,pad=0.15",
                            fc='#1f2937',ec=SAFFRON,lw=2.2))
ax.text(6.1,7.0,'pathlib.Path',ha='center',fontsize=12.5,fontweight='bold',color=SAFFRON)
ax.text(6.1,5.4,'Path("model.pkl")\nPosixPath\nWindowsPath',ha='center',va='center',
        fontsize=11,color=FG)
ax.text(6.1,3.2,'the old check saw\nONLY this box',ha='center',va='center',
        fontsize=10.5,color=SAFFRON,style='italic')

# the rest of the protocol
ax.text(15.6,6.6,'BIDSPath  (mne-bids)\nyour own path class\nanything else with __fspath__',
        ha='center',va='center',fontsize=11.5,color=FG,linespacing=1.7)
ax.text(15.6,3.2,'real paths, silently rejected',ha='center',va='center',
        fontsize=10.5,color=RED,style='italic')

ax.text(11,0.6,'Checking the class excludes valid inputs.  Checking the protocol includes them all.',
        ha='center',fontsize=11.5,color=YELLOW,fontweight='bold')
plt.tight_layout(); save('02-protocol-vs-class.png')

# ---------- IMG 3: before / after, the one-word fix ----------
fig, ax = plt.subplots(figsize=(12,4.6)); ax.set_xlim(0,24); ax.set_ylim(0,9); ax.axis('off')
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)

ax.text(5.6,8.3,'BEFORE',ha='center',fontsize=13,fontweight='bold',color=RED)
ax.add_patch(FancyBboxPatch((0.5,4.3),10.2,3.3,boxstyle="round,pad=0.12",
                            fc='#161b22',ec=RED,lw=2.0))
ax.text(5.6,5.95,'if Path is not None and \\\n        isinstance(filename, Path):\n    filename = str(filename)',
        ha='center',va='center',fontsize=11.5,color=FG,family='monospace',linespacing=1.8)
ax.text(5.6,3.5,'checks one concrete class',ha='center',fontsize=11,color=MUT,style='italic')

arrow(11.2,5.95,12.8,5.95,YELLOW)

ax.text(18.4,8.3,'AFTER',ha='center',fontsize=13,fontweight='bold',color=GREEN)
ax.add_patch(FancyBboxPatch((13.3,4.3),10.2,3.3,boxstyle="round,pad=0.12",
                            fc='#161b22',ec=GREEN,lw=2.0))
ax.text(18.4,5.95,'if isinstance(filename, os.PathLike):\n    filename = os.fspath(filename)',
        ha='center',va='center',fontsize=11.5,color=FG,family='monospace',linespacing=1.8)
ax.text(18.4,3.5,'checks the protocol',ha='center',fontsize=11,color=MUT,style='italic')

ax.text(12,1.2,'Same two lines in dump() and in load().  +29 / -9 in total.',
        ha='center',fontsize=12,color=YELLOW,fontweight='bold')
plt.tight_layout(); save('03-before-after.png')

# ---------- IMG 4: the path from issue to merge ----------
fig, ax = plt.subplots(figsize=(12,5)); ax.set_xlim(0,24); ax.set_ylim(0,10); ax.axis('off')
fig.patch.set_facecolor(BG); ax.set_facecolor(BG)
ax.text(12,9.3,'Issue to merge: 9 days',ha='center',fontsize=15,fontweight='bold',color=FG)

ax.plot([1.6,22.4],[5.6,5.6],color='#30363d',lw=2.4,zorder=1)
steps=[(2.6,'2 Mar','user files\nissue #1784',SAFFRON),
       (7.4,'6 Jul','PR opened\nfix + test',TEAL),
       (12.2,'6 Jul','review same day\n"few things"',YELLOW),
       (17.0,'6 Jul','changes\npushed',TEAL),
       (21.6,'15 Jul','MERGED',GREEN)]
for x,date,label,c in steps:
    ax.plot([x],[5.6],marker='o',markersize=17,color=c,zorder=3)
    ax.plot([x],[5.6],marker='o',markersize=8,color=BG,zorder=4)
    ax.text(x,7.0,date,ha='center',fontsize=11.5,fontweight='bold',color=c)
    bold='bold' if label=='MERGED' else 'normal'
    lc=GREEN if label=='MERGED' else FG
    ax.text(x,4.2,label,ha='center',va='top',fontsize=10.5,color=lc,fontweight=bold)

ax.annotate('', xy=(7.0,3.0), xytext=(2.6,3.0),
            arrowprops=dict(arrowstyle='<->',color=MUT,lw=1.6))
ax.text(4.8,2.4,'4 months unclaimed',ha='center',fontsize=10.5,color=MUT,style='italic')
ax.text(12,0.9,'The bug waited. The fix took an afternoon.',
        ha='center',fontsize=12,color=YELLOW,fontweight='bold')
plt.tight_layout(); save('04-issue-to-merge.png')

print('day01 images written to', OUT)
