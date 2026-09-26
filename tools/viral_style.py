"""Dark, high-contrast palette for shorts.

WHY DARK, AFTER SHIPPING LIGHT
------------------------------
The first version was white, on the reasoning that a bright phone in daylight
needs contrast. That was half right and half wrong:

  - 80%+ of Android and iOS users have dark mode enabled (platform metrics)
  - saturated accents pop against near-black, which is why every trading and
    crypto dashboard is dark — the same reason it works for fast scrolling
  - a white frame in a dark feed reads as a document, not as content

So the ground is near-black and the brand cyan does the work. The logo's own
cyan #00B8FC is already a saturated, high-contrast colour — on white it was
being wasted.

TEXT SIZES
----------
Short-form guidance is 48-60px on a 1080x1920 frame. These pages are rendered
at A4 landscape and shown full-screen, so the equivalent floor is roughly 28pt
for anything that must be read while scrolling, and 60pt+ for the hook itself.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Ground
BG = "#FFFFFF"          # white page — matches the AIWithRav brand
PANEL = "#F2F7FC"       # raised card, a hair off-white so its edge reads
LINE = "#D4E3F2"

# Brand, straight from the logo
CYAN = "#0E9CFE"        # brand accent, sampled from the wordmark
GOLD = "#0A6FC2"        # deep blue; gold has no contrast on white

# Semantic
GREEN = "#12A47A"
RED = "#E5484D"
CREAM = "#001954"       # body text — brand navy on white
MUTED = "#5B7392"       # labels
WHITE = "#FFFFFF"


def fig(w=12, h=6.2):
    f, a = plt.subplots(figsize=(w, h), dpi=220)
    f.patch.set_facecolor(BG)
    a.set_facecolor(BG)
    a.axis("off")
    return f, a


def save(f, path):
    plt.tight_layout()
    f.savefig(path, facecolor=BG, bbox_inches="tight", pad_inches=0.28)
    plt.close(f)
    print("  saved", path)


def card(a, x, y, w, h, colour, lw=2.6, fill=PANEL):
    a.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.06",
                               ec=colour, fc=fill, lw=lw))


def arrow(a, x0, y0, x1, y1, colour=MUTED, lw=2.4, dashed=False):
    a.add_patch(FancyArrowPatch((x0, y0), (x1, y1), arrowstyle="-|>",
                                mutation_scale=20, color=colour, lw=lw,
                                linestyle=(0, (4, 3)) if dashed else "solid"))


# Compatibility aliases, so diagram code written against the light palette
# renders correctly on the dark ground without being rewritten.
NAVY = CREAM        # was the darkest text; on a dark ground that is the lightest
PAPER = PANEL       # card fill
INK = CREAM
TINT = PANEL
