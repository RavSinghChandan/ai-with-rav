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
def codebox(ax,x,y,w,h,text,col=GRN,fs=12):
    ax.add_patch(Rectangle((x,y),w,h,fc=CODE,ec='#3a2f26'))
    ax.text(x+0.3,y+h/2,text,va='center',color=col,fontsize=fs,family='monospace')

# 11: A STRING IS A ROW OF CHARACTERS with index numbers
fig,ax=plt.subplots(figsize=(9.6,4.2)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('A string is a row of characters, each with a position (index)',fontsize=12,fontweight='bold',color=FG)
word="PYTHON"
for i,ch in enumerate(word):
    x=2.4+i*1.2
    ax.add_patch(FancyBboxPatch((x,4.6),1.0,1.6,boxstyle="round,pad=0.03",fc=BLU,ec=FG,lw=1.2))
    ax.text(x+0.5,5.4,ch,ha='center',va='center',color='#1a1512',fontsize=16,fontweight='bold')
    ax.text(x+0.5,3.9,str(i),ha='center',color=YEL,fontsize=11,fontweight='bold')
ax.text(1.9,5.4,'',ha='right')
ax.text(6.0,2.6,'Counting starts at 0! P is at index 0, Y at 1, ... N at 5',ha='center',color=YEL,fontsize=10.5,fontweight='bold')
ax.text(6.0,7.4,'word = "PYTHON"',ha='center',color=GRN,fontsize=12,family='monospace')
plt.tight_layout(); plt.savefig('topics/27-python/images/11-string-index.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 12: SLICING — pulling out a piece
fig,ax=plt.subplots(figsize=(9.6,4.2)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Slicing: pull out a piece with [start:end]',fontsize=12,fontweight='bold',color=FG)
word="PYTHON"
for i,ch in enumerate(word):
    x=2.4+i*1.2
    c=GRN if i in (0,1,2) else BLU
    ax.add_patch(FancyBboxPatch((x,5.0),1.0,1.6,boxstyle="round,pad=0.03",fc=c,ec=FG,lw=1.2))
    ax.text(x+0.5,5.8,ch,ha='center',va='center',color='#1a1512',fontsize=15,fontweight='bold')
    ax.text(x+0.5,4.4,str(i),ha='center',color=YEL,fontsize=10,fontweight='bold')
codebox(ax,2.4,2.2,4.2,1.1,'word[0:3]  ->  "PYT"',GRN,11)
ax.text(9.0,3.0,'takes index 0,1,2\n(stops BEFORE 3)',ha='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/12-slice.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 13: JOINING (concatenation)
fig,ax=plt.subplots(figsize=(9.4,3.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Joining strings with +  ("concatenation")',fontsize=12,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((0.6,5.4),2.6,1.6,boxstyle="round,pad=0.04",fc=SAF,ec=FG,lw=1.3)); ax.text(1.9,6.2,'"Rav"',ha='center',va='center',color='#1a1512',fontsize=12,fontweight='bold')
ax.text(3.6,6.2,'+',ha='center',color=YEL,fontsize=22,fontweight='bold')
ax.add_patch(FancyBboxPatch((4.2,5.4),2.6,1.6,boxstyle="round,pad=0.04",fc=SAF,ec=FG,lw=1.3)); ax.text(5.5,6.2,'" Singh"',ha='center',va='center',color='#1a1512',fontsize=11,fontweight='bold')
ax.text(7.2,6.2,'=',ha='center',color=YEL,fontsize=22,fontweight='bold')
ax.add_patch(FancyBboxPatch((7.8,5.4),3.6,1.6,boxstyle="round,pad=0.04",fc=GRN,ec=FG,lw=1.3)); ax.text(9.6,6.2,'"Rav Singh"',ha='center',va='center',color='#1a1512',fontsize=11,fontweight='bold')
codebox(ax,2.4,2.4,7.0,1.1,'full = "Rav" + " Singh"   ->  "Rav Singh"',GRN,11)
plt.tight_layout(); plt.savefig('topics/27-python/images/13-join.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 14: F-STRINGS
fig,ax=plt.subplots(figsize=(9.4,4.0)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('f-strings: drop variables straight into text',fontsize=12,fontweight='bold',color=FG)
codebox(ax,0.6,6.4,10.8,1.2,'name = "Rav" ;  age = 30',FG,11)
codebox(ax,0.6,4.4,10.8,1.4,'f"Hi {name}, you are {age}"',GRN,12)
# show the slots filled
ax.text(6.0,3.2,'the { } slots get filled with the variable values',ha='center',color=YEL,fontsize=10,fontweight='bold')
ax.add_patch(FancyBboxPatch((2.4,1.2),7.2,1.4,boxstyle="round,pad=0.04",fc=GRN,ec=FG,lw=1.4))
ax.text(6.0,1.9,'Hi Rav, you are 30',ha='center',va='center',color='#1a1512',fontsize=13,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/14-fstring.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 15: HANDY STRING METHODS
fig,ax=plt.subplots(figsize=(9.4,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Handy string tools (methods)',fontsize=12.5,fontweight='bold',color=FG)
rows=[('.upper()','"rav".upper()','"RAV"',BLU),
      ('.lower()','"RAV".lower()','"rav"',SAF),
      ('.strip()','"  rav  ".strip()','"rav"  (trims spaces)',GRN),
      ('.replace()','"cat".replace("c","b")','"bat"',PUR),
      ('len()','len("Rav")','3  (how many characters)',YEL)]
for i,(m,call,res,c) in enumerate(rows):
    y=7.6-i*1.5
    ax.text(1.4,y+0.3,m,ha='right',color=c,fontsize=11,family='monospace',fontweight='bold')
    ax.text(1.8,y+0.3,call,va='center',color=FG,fontsize=9.5,family='monospace')
    ax.text(7.4,y+0.3,'-> '+res,va='center',color=YEL,fontsize=9.5,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/15-methods.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("py day3 images generated")
