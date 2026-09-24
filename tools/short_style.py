"""Light-mode diagram palette for the shorts template.

The 30-day deck uses dark diagrams on a warm charcoal page. A reel is watched
on a bright phone in daylight, so these are the opposite: white ground, brand
cyan and gold, heavy type. One diagram per short, readable at a glance.

Colours sampled from brand/rav-mark.png.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

CYAN = "#00B8FC"
GOLD = "#F6BB63"
NAVY = "#14213D"
INK = "#1B2A41"
MUTED = "#5B6B82"
PAPER = "#FFFFFF"
TINT = "#F2F8FD"
LINE = "#DCE7F1"
GREEN = "#12A594"
RED = "#E5484D"


def fig(w=12, h=6.2):
    f, a = plt.subplots(figsize=(w, h), dpi=220)
    f.patch.set_facecolor(PAPER)
    a.set_facecolor(PAPER)
    a.axis("off")
    return f, a


def save(f, path):
    plt.tight_layout()
    f.savefig(path, facecolor=PAPER, bbox_inches="tight", pad_inches=0.25)
    plt.close(f)
    print("  saved", path)


def card(a, x, y, w, h, colour, lw=2.2, fill=PAPER):
    a.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                               ec=colour, fc=fill, lw=lw))


def arrow(a, x0, y0, x1, y1, colour=MUTED, lw=2.0, dashed=False):
    a.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                mutation_scale=18, color=colour, lw=lw,
                                linestyle=(0, (4, 3)) if dashed else "solid"))
