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

# 21: input/output = a two-way conversation
fig,ax=plt.subplots(figsize=(9.4,4.4)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('input() and print() = a two-way conversation',fontsize=12.5,fontweight='bold',color=FG)
ax.add_patch(FancyBboxPatch((0.6,3.6),3.0,3.4,boxstyle="round,pad=0.05",fc=BLU,ec=FG,lw=1.4)); ax.text(2.1,5.3,'YOUR\nPROGRAM',ha='center',va='center',color='#1a1512',fontsize=11,fontweight='bold')
ax.add_patch(FancyBboxPatch((8.4,3.6),3.0,3.4,boxstyle="round,pad=0.05",fc=GRN,ec=FG,lw=1.4)); ax.text(9.9,5.3,'THE\nUSER',ha='center',va='center',color='#1a1512',fontsize=11,fontweight='bold')
ax.annotate('',xy=(8.4,6.0),xytext=(3.6,6.0),arrowprops=dict(arrowstyle='->',color=YEL,lw=2.2))
ax.text(6.0,6.5,'print("What is your name?")',ha='center',color=YEL,fontsize=9.5,family='monospace')
ax.annotate('',xy=(3.6,4.4),xytext=(8.4,4.4),arrowprops=dict(arrowstyle='->',color=SAF,lw=2.2))
ax.text(6.0,3.9,'input() -> "Rav"',ha='center',color=SAF,fontsize=9.5,family='monospace')
ax.text(6.0,1.6,'print() speaks TO the user · input() listens FROM the user',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/21-io.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 22: input always returns a STRING
fig,ax=plt.subplots(figsize=(9.4,4.2)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Careful: input() ALWAYS gives back text (a string)',fontsize=12,fontweight='bold',color=FG)
cb(ax,0.6,7.0,10.8,1.1,'age = input("Your age? ")     # user types 30',FG,10.5)
ax.add_patch(FancyBboxPatch((2.0,4.6),3.4,1.6,boxstyle="round,pad=0.04",fc=GRN,ec=FG,lw=1.3)); ax.text(3.7,5.4,'"30"',ha='center',va='center',color='#1a1512',fontsize=15,fontweight='bold')
ax.text(3.7,4.0,'text, NOT a number!',ha='center',color=RED,fontsize=10,fontweight='bold')
ax.text(6.4,5.4,'-> so age + 1 would ERROR',ha='left',color=RED,fontsize=10.5,fontweight='bold')
cb(ax,0.6,1.6,10.8,1.1,'age = int(input("Your age? "))   # NOW it is a number',GRN,10.5)
ax.text(6.0,0.7,'Wrap it in int() (or float()) to convert text to a number',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/22-input-string.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 23: print with multiple things
fig,ax=plt.subplots(figsize=(9.4,3.8)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('print() can show several things at once',fontsize=12,fontweight='bold',color=FG)
cb(ax,0.6,6.6,10.8,1.2,'print("Age:", 30, "years")',GRN,12)
ax.add_patch(FancyBboxPatch((2.4,4.0),7.2,1.5,boxstyle="round,pad=0.04",fc=GRN,ec=FG,lw=1.4))
ax.text(6.0,4.75,'Age: 30 years',ha='center',va='center',color='#1a1512',fontsize=14,fontweight='bold')
ax.text(6.0,2.4,'Separate items with commas — print adds a space between them',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/23-print-multi.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 24: COMMENTS
fig,ax=plt.subplots(figsize=(9.4,4.0)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Comments (#): notes for humans, ignored by Python',fontsize=11.5,fontweight='bold',color=FG)
ax.add_patch(Rectangle((0.6,2.4),10.8,5.2,fc=CODE,ec='#3a2f26'))
ax.text(0.9,6.8,'# work out the total price',color=MUT,fontsize=11,family='monospace')
ax.text(0.9,5.9,'price = 100',color=GRN,fontsize=11,family='monospace')
ax.text(0.9,5.0,'tax = 18            # 18% GST',color=GRN,fontsize=11,family='monospace')
ax.text(4.9,5.0,'',color=MUT)
ax.text(0.9,4.1,'total = price + tax  # add them up',color=GRN,fontsize=11,family='monospace')
ax.text(0.9,3.1,'print(total)',color=GRN,fontsize=11,family='monospace')
ax.text(6.0,1.4,'Anything after # is a note. Explain the WHY, not the obvious.',ha='center',color=YEL,fontsize=10,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/24-comments.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()

# 25: a mini interactive program
fig,ax=plt.subplots(figsize=(9.4,4.6)); fig.patch.set_facecolor(BG); frame(ax,(0,12),(0,10))
ax.set_title('Putting it together: a tiny interactive program',fontsize=12,fontweight='bold',color=FG)
ax.add_patch(Rectangle((0.6,4.2),10.8,4.4,fc=CODE,ec='#3a2f26'))
lines=['name = input("Your name? ")','age  = int(input("Your age? "))',
       'next_age = age + 1','print(f"Hi {name}, next year you turn {next_age}")']
for i,l in enumerate(lines):
    ax.text(0.9,8.0-i*1.0,l,color=GRN,fontsize=10.5,family='monospace')
ax.add_patch(FancyBboxPatch((1.6,1.2),8.8,2.2,boxstyle="round,pad=0.04",fc=GRN,ec=FG,lw=1.4))
ax.text(6.0,2.3,'Hi Rav, next year you turn 31',ha='center',va='center',color='#1a1512',fontsize=12,fontweight='bold')
plt.tight_layout(); plt.savefig('topics/27-python/images/25-mini-program.png',dpi=150,facecolor=BG,bbox_inches='tight'); plt.close()
print("py day5 images generated")
