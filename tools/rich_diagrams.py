"""Rich, worked diagrams for the twelve topics that had a thin fallback.

Each one carries a real Indian example end to end: a chai stall, a ration shop,
a Mumbai local, an IRCTC booking. The rule is that a viewer who pauses the reel
on this single frame should be able to reconstruct the whole idea from it.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from viral_style import *          # noqa: F403
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def title(a, text, sub=None):
    a.text(6, 5.62, text, ha="center", color=NAVY, fontsize=15, fontweight="bold")
    if sub:
        a.text(6, 5.18, sub, ha="center", color=MUTED, fontsize=12)


def chip(a, x, y, w, h, text, colour, fs=11.5, bold=True, fill=PANEL, tc=None):
    a.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                               ec=colour, fc=fill, lw=2.0))
    a.text(x + w / 2, y + h / 2, text, ha="center", va="center",
           color=tc or colour, fontsize=fs,
           fontweight="bold" if bold else "normal")


# ── 1. Prompt engineering: show, don't describe ────────────────────────────
def fewshot(a):
    title(a, "SAME TASK, TWO PROMPTS", "asking a model to reply to a customer on WhatsApp")
    # left: describe
    chip(a, 0.5, 3.4, 5.1, 1.5, "", MUTED)
    a.text(3.05, 4.62, "DESCRIBE IT", ha="center", color=MUTED, fontsize=12.5, fontweight="bold")
    a.text(3.05, 4.05, '"Reply politely and formally"', ha="center", color=NAVY, fontsize=12)
    a.text(3.05, 3.65, "model guesses what you mean", ha="center", color=MUTED, fontsize=10.5)
    arrow(a, 3.05, 3.32, 3.05, 2.85, MUTED, lw=1.8)
    chip(a, 0.5, 1.2, 5.1, 1.6, "", RED, fill="#2A1620")
    a.text(3.05, 2.45, "OUT:", ha="center", color=RED, fontsize=10.5, fontweight="bold")
    a.text(3.05, 1.95, '"Dear Esteemed Customer,\nWe are in receipt of your\nvalued communication..."',
           ha="center", va="center", color=NAVY, fontsize=11)
    # right: show
    chip(a, 6.4, 3.4, 5.1, 1.5, "", CYAN)
    a.text(8.95, 4.62, "SHOW ONE EXAMPLE", ha="center", color=CYAN, fontsize=12.5, fontweight="bold")
    a.text(8.95, 4.08, 'IN: "order late?"', ha="center", color=NAVY, fontsize=11)
    a.text(8.95, 3.68, 'OUT: "Sorry sir, aapka order\nkal tak aa jayega."',
           ha="center", va="top", color=NAVY, fontsize=10.5)
    arrow(a, 8.95, 3.32, 8.95, 2.85, CYAN, lw=1.8)
    chip(a, 6.4, 1.2, 5.1, 1.6, "", GREEN, fill="#0F2A26")
    a.text(8.95, 2.45, "OUT:", ha="center", color=GREEN, fontsize=10.5, fontweight="bold")
    a.text(8.95, 1.95, '"Sorry ma\'am, delay ho gaya.\nAaj shaam tak deliver\nho jayega."',
           ha="center", va="center", color=NAVY, fontsize=11)
    a.text(6, 0.55, "One example fixed tone, length and language together",
           ha="center", color=GOLD, fontsize=12.5, fontweight="bold")


# ── 2. Java: == vs .equals ─────────────────────────────────────────────────
def equals(a):
    title(a, "TWO NAMES THAT LOOK THE SAME", 'String a = "Ravi";   String b = new String("Ravi");')
    for x, lbl, addr, col in [(2.6, "a", "0x1A4", CYAN), (9.0, "b", "0x7F2", GOLD)]:
        a.text(x, 4.55, lbl, ha="center", color=col, fontsize=17, fontweight="bold")
        arrow(a, x, 4.3, x, 3.75, col, lw=2.0)
        chip(a, x - 1.6, 2.5, 3.2, 1.2, "", col)
        a.text(x, 3.28, addr, ha="center", color=MUTED, fontsize=10.5)
        a.text(x, 2.9, '"Ravi"', ha="center", color=NAVY, fontsize=16, fontweight="bold")
        a.text(x, 2.15, "box in memory", ha="center", color=MUTED, fontsize=10.5)
    a.text(5.8, 3.1, "≠", ha="center", va="center", color=RED, fontsize=26, fontweight="bold")
    chip(a, 0.6, 0.55, 5.1, 1.25, "", RED, fill="#2A1620")
    a.text(3.15, 1.45, "a == b", ha="center", color=RED, fontsize=14, fontweight="bold")
    a.text(3.15, 0.95, "different boxes  →  false", ha="center", color=NAVY, fontsize=11.5)
    chip(a, 6.3, 0.55, 5.1, 1.25, "", GREEN, fill="#0F2A26")
    a.text(8.85, 1.45, "a.equals(b)", ha="center", color=GREEN, fontsize=14, fontweight="bold")
    a.text(8.85, 0.95, "same contents  →  true", ha="center", color=NAVY, fontsize=11.5)


# ── 3. System design: caching ──────────────────────────────────────────────
def cache(a):
    title(a, "IRCTC: WHAT IS WORTH CACHING?", "same question from thousands of users")
    rows = [("Train list: Delhi → Patna", "changes once a day", "asked 50,000×/hour", True),
            ("Seat availability, this train", "changes every second", "asked 50,000×/hour", False),
            ("Your booking history", "changes rarely", "asked once per login", False)]
    y = 4.35
    for label, churn, freq, good in rows:
        col = GREEN if good else RED
        chip(a, 0.6, y - 0.42, 4.9, 0.92, "", col if good else LINE,
             fill="#0F2A26" if good else PANEL)
        a.text(3.05, y + 0.14, label, ha="center", color=NAVY, fontsize=11.5, fontweight="bold")
        a.text(3.05, y - 0.22, churn, ha="center", color=MUTED, fontsize=10)
        a.text(6.4, y - 0.02, freq, ha="left", color=MUTED, fontsize=10.5)
        a.text(11.3, y - 0.02, "CACHE" if good else "don't", ha="right",
               color=col, fontsize=12, fontweight="bold")
        y -= 1.25
    a.text(6, 0.52, "Slow to compute AND often repeated AND stays valid — all three, or don't",
           ha="center", color=GOLD, fontsize=12, fontweight="bold")


# ── 4. Neural networks: one neuron ─────────────────────────────────────────
def neuron(a):
    title(a, "ONE NEURON DECIDES: LEND OR NOT?", "a small loan application")
    inputs = [("Income", "0.9", "×0.6", 4.35), ("Credit score", "0.7", "×0.3", 3.35),
              ("Existing loans", "0.4", "×-0.5", 2.35)]
    for lbl, val, w, y in inputs:
        a.text(0.5, y, lbl, ha="left", color=NAVY, fontsize=12)
        chip(a, 2.9, y - 0.28, 0.85, 0.56, val, CYAN, fs=11.5)
        a.text(4.35, y + 0.08, w, ha="center", color=GOLD, fontsize=12, fontweight="bold")
        arrow(a, 4.9, y, 6.1, 3.35, MUTED, lw=1.5)
    a.add_patch(plt.Circle((6.9, 3.35), 0.78, ec=NAVY, fc=PANEL, lw=2.4))
    a.text(6.9, 3.5, "Σ", ha="center", va="center", color=NAVY, fontsize=20, fontweight="bold")
    a.text(6.9, 3.02, "0.61", ha="center", va="center", color=CYAN, fontsize=12, fontweight="bold")
    arrow(a, 7.75, 3.35, 8.7, 3.35, NAVY, lw=2.0)
    chip(a, 8.8, 2.75, 2.7, 1.2, "", GREEN, fill="#0F2A26")
    a.text(10.15, 3.6, "over 0.5?", ha="center", color=MUTED, fontsize=10.5)
    a.text(10.15, 3.15, "APPROVE", ha="center", color=GREEN, fontsize=14, fontweight="bold")
    a.text(6, 1.35, "multiply each input by its weight  →  add them up  →  cross the line or not",
           ha="center", color=NAVY, fontsize=12)
    a.text(6, 0.7, "Learning is only this: nudging those weights until the answers come out right",
           ha="center", color=GOLD, fontsize=12, fontweight="bold")


# ── 5. AI tools: match checking to the cost of being wrong ─────────────────
def risk(a):
    title(a, "WHAT DOES A WRONG ANSWER COST YOU?", "same tool, two very different jobs")
    chip(a, 0.6, 2.2, 5.1, 2.7, "", GREEN, fill="#0F2A26")
    a.text(3.15, 4.5, "DRAFTING A WHATSAPP REPLY", ha="center", color=GREEN, fontsize=12, fontweight="bold")
    a.text(3.15, 3.9, "wrong answer costs:", ha="center", color=MUTED, fontsize=10.5)
    a.text(3.15, 3.4, "10 seconds", ha="center", color=GREEN, fontsize=19, fontweight="bold")
    a.text(3.15, 2.75, "just retype it", ha="center", color=NAVY, fontsize=11.5)
    a.text(3.15, 2.42, "→ no checking needed", ha="center", color=MUTED, fontsize=10.5)
    chip(a, 6.3, 2.2, 5.1, 2.7, "", RED, fill="#2A1620")
    a.text(8.85, 4.5, "SUMMARISING A RENT AGREEMENT", ha="center", color=RED, fontsize=12, fontweight="bold")
    a.text(8.85, 3.9, "wrong answer costs:", ha="center", color=MUTED, fontsize=10.5)
    a.text(8.85, 3.4, "a missed clause", ha="center", color=RED, fontsize=17, fontweight="bold")
    a.text(8.85, 2.75, "you find out in court", ha="center", color=NAVY, fontsize=11.5)
    a.text(8.85, 2.42, "→ cite + read the source", ha="center", color=MUTED, fontsize=10.5)
    a.text(6, 1.25, "Same model. Same speed. Completely different amount of checking.",
           ha="center", color=NAVY, fontsize=12.5)
    a.text(6, 0.6, "Match the effort to the cost of the mistake, not to the hype",
           ha="center", color=GOLD, fontsize=12.5, fontweight="bold")


# ── 6. AI for everyone: pattern, not understanding ─────────────────────────
def understand(a):
    title(a, "IT HAS READ, NOT UNDERSTOOD", 'ask: "what is the capital of Bihar?"')
    chip(a, 0.6, 3.1, 10.8, 1.7, "", CYAN)
    a.text(1.1, 4.35, "It has seen these sentences millions of times:", ha="left",
           color=MUTED, fontsize=11)
    a.text(1.1, 3.88, '"The capital of Bihar is Patna."', ha="left", color=NAVY, fontsize=12.5)
    a.text(1.1, 3.45, '"Patna, the capital of Bihar, sits on the Ganga."', ha="left",
           color=NAVY, fontsize=12.5)
    arrow(a, 6, 3.02, 6, 2.55, MUTED, lw=1.8)
    chip(a, 2.4, 1.6, 7.2, 0.92, 'answers "Patna" — correctly', GREEN, fs=13, fill="#0F2A26")
    a.text(6, 1.0, "Now ask about a village it has never seen written down.",
           ha="center", color=NAVY, fontsize=12)
    a.text(6, 0.48, "It will still answer confidently — because the SHAPE of the answer is all it knows",
           ha="center", color=RED, fontsize=12, fontweight="bold")


# ── 7. AI Q&A: invented citations ──────────────────────────────────────────
def citation(a):
    title(a, "WHY IT INVENTS A PANEL", 'ask: "cite a study on AI in Indian agriculture"')
    chip(a, 1.6, 3.2, 8.8, 1.5, "", GOLD, fill="#2A2214")
    a.text(6, 4.32, "Sharma, R. & Patel, K. (2021).", ha="center", color=NAVY,
           fontsize=14, fontweight="bold")
    a.text(6, 3.86, '"Machine Learning for Crop Yield Prediction in Punjab."',
           ha="center", color=NAVY, fontsize=12)
    a.text(6, 3.45, "Indian Journal of Agricultural Science, 58(3), 214–229.",
           ha="center", color=MUTED, fontsize=11)
    a.text(1.0, 2.75, "Author names:  plausible ✓", ha="left", color=GREEN, fontsize=11.5)
    a.text(1.0, 2.3, "Journal:  real ✓", ha="left", color=GREEN, fontsize=11.5)
    a.text(1.0, 1.85, "Format:  perfect ✓", ha="left", color=GREEN, fontsize=11.5)
    chip(a, 6.4, 1.6, 5.0, 1.4, "", RED, fill="#2A1620")
    a.text(8.9, 2.62, "The paper does not exist.", ha="center", color=RED,
           fontsize=13.5, fontweight="bold")
    a.text(8.9, 2.1, "Nothing looked it up. There is no", ha="center", color=NAVY, fontsize=11)
    a.text(8.9, 1.8, "lookup step in the model at all.", ha="center", color=NAVY, fontsize=11)
    a.text(6, 0.85, "A convincing fake scores exactly as well as a real one while predicting text",
           ha="center", color=NAVY, fontsize=12)
    a.text(6, 0.35, "Never accept a citation you have not opened", ha="center",
           color=GOLD, fontsize=12.5, fontweight="bold")


# ── 8. AI news: read the benchmark ─────────────────────────────────────────
def news(a):
    title(a, '"AI BEATS DOCTORS AT DIAGNOSIS"', "the same result, read three ways")
    chip(a, 2.0, 4.15, 8.0, 0.95, "AI scores 94%. Doctors score 89%.", NAVY, fs=14)
    qs = [("Which test?", "1,000 clean textbook images —\nnot a real OPD queue", CYAN),
          ("Versus whom?", "junior residents,\nnot senior radiologists", GOLD),
          ("Did data leak?", "the test images were online —\nthe model may have seen them", RED)]
    for i, (q, ans, col) in enumerate(qs):
        x = 0.5 + i * 3.75
        chip(a, x, 1.5, 3.4, 2.2, "", col)
        a.text(x + 1.7, 3.35, q, ha="center", color=col, fontsize=12.5, fontweight="bold")
        a.text(x + 1.7, 2.45, ans, ha="center", va="center", color=NAVY, fontsize=10.5)
    a.text(6, 0.8, "Three questions turn most AI headlines into something much smaller",
           ha="center", color=GOLD, fontsize=12.5, fontweight="bold")


# ── 9. Build projects: ship the smallest useful thing ──────────────────────
def ship(a):
    title(a, "TWO PORTFOLIOS, SAME SIX WEEKS", "which one gets the interview?")
    chip(a, 0.6, 1.5, 5.1, 3.4, "", MUTED)
    a.text(3.15, 4.5, "8 TUTORIAL NOTEBOOKS", ha="center", color=MUTED, fontsize=12.5, fontweight="bold")
    for i, t in enumerate(["House price predictor", "Handwritten digit demo",
                           "Movie review sentiment", "Chatbot from a YouTube video"]):
        a.text(3.15, 3.9 - i * 0.45, "· " + t, ha="center", color=NAVY, fontsize=11)
    a.text(3.15, 1.9, "all ran perfectly, first time", ha="center", color=MUTED, fontsize=10.5)
    chip(a, 6.3, 1.5, 5.1, 3.4, "", GREEN, fill="#0F2A26")
    a.text(8.85, 4.5, "1 THING PEOPLE USE", ha="center", color=GREEN, fontsize=12.5, fontweight="bold")
    a.text(8.85, 3.9, "A WhatsApp bot that answers", ha="center", color=NAVY, fontsize=11)
    a.text(8.85, 3.55, "questions about your hostel mess menu", ha="center", color=NAVY, fontsize=11)
    for i, t in enumerate(["40 students used it", "broke twice, you fixed it",
                           "you wrote down what it gets wrong"]):
        a.text(8.85, 2.95 - i * 0.42, "· " + t, ha="center", color=NAVY, fontsize=11)
    a.text(8.85, 1.75, "you can answer 20 minutes of questions on it", ha="center",
           color=GREEN, fontsize=10.5, fontweight="bold")
    a.text(6, 0.7, "The second one has the boring parts — and the boring parts are the interview",
           ha="center", color=GOLD, fontsize=12.5, fontweight="bold")


# ── 10. CNN: the sliding filter ────────────────────────────────────────────
def filt(a):
    title(a, "FINDING A VERTICAL EDGE", "one small window, slid across the whole photo")
    # pixel grid
    gx, gy, cell = 0.8, 1.5, 0.42
    for r in range(8):
        for c in range(8):
            shade = "#2A3854" if c < 4 else PANEL
            a.add_patch(plt.Rectangle((gx + c * cell, gy + r * cell), cell, cell,
                                      fc=shade, ec=LINE, lw=0.8))
    a.text(gx + 4 * cell, gy + 8 * cell + 0.3, "the image", ha="center",
           color=MUTED, fontsize=11)
    # the sliding window at two positions
    # Two window positions, far enough apart that neither the boxes nor their
    # labels collide.
    for cx, cy, col, lbl in [(0, 5, GOLD, "no edge"), (3, 2, GREEN, "EDGE FOUND")]:
        a.add_patch(plt.Rectangle((gx + cx * cell, gy + cy * cell), cell * 2, cell * 2,
                                  fc="none", ec=col, lw=3))
        a.text(gx + (cx + 1) * cell, gy + (cy + 2) * cell + 0.18, lbl, ha="center",
               color=col, fontsize=10.5, fontweight="bold")
    arrow(a, 4.6, 3.2, 5.6, 3.2, MUTED, lw=2.0)
    chip(a, 5.8, 2.5, 2.4, 1.4, "", CYAN)
    a.text(7.0, 3.62, "the filter", ha="center", color=CYAN, fontsize=11.5, fontweight="bold")
    a.text(7.0, 3.05, "dark | light", ha="center", color=NAVY, fontsize=12)
    a.text(7.0, 2.72, "2×2 window", ha="center", color=MUTED, fontsize=10)
    arrow(a, 8.3, 3.2, 9.0, 3.2, MUTED, lw=2.0)
    chip(a, 9.1, 2.3, 2.4, 1.8, "", GREEN, fill="#0F2A26")
    a.text(10.3, 3.72, "match map", ha="center", color=GREEN, fontsize=11.5, fontweight="bold")
    a.text(10.3, 3.1, "bright exactly", ha="center", color=NAVY, fontsize=11)
    a.text(10.3, 2.75, "where the edge is", ha="center", color=NAVY, fontsize=11)
    a.text(6, 0.7, "The SAME small window slides everywhere — that is why CNNs need so little data",
           ha="center", color=GOLD, fontsize=12, fontweight="bold")


# ── 11. RNN: fading memory ─────────────────────────────────────────────────
def memory(a):
    title(a, "MEMORY THAT LEAKS", '"Ravi, who grew up in Patna and later moved to Pune, speaks ___"')
    words = [("Ravi", 1.0), ("Patna", 0.72), ("moved", 0.48), ("Pune", 0.3),
             ("speaks", 0.16), ("___", 0.06)]
    for i, (w, strength) in enumerate(words):
        x = 0.9 + i * 1.85
        h = 0.35 + strength * 1.5
        col = GREEN if strength > 0.6 else (GOLD if strength > 0.25 else RED)
        a.add_patch(FancyBboxPatch((x - 0.62, 2.0), 1.24, h, boxstyle="round,pad=0.04",
                                   ec=col, fc=col, lw=0, alpha=0.9))
        a.text(x, 1.7, w, ha="center", color=NAVY, fontsize=12, fontweight="bold")
        a.text(x, 2.0 + h + 0.2, f"{int(strength*100)}%", ha="center", color=col,
               fontsize=11, fontweight="bold")
        if i < len(words) - 1:
            arrow(a, x + 0.66, 2.3, x + 1.18, 2.3, MUTED, lw=1.4)
    a.text(6, 4.55, "how much of each word still survives in memory", ha="center",
           color=MUTED, fontsize=11.5)
    a.text(6, 1.05, 'By the blank, "Patna" is nearly gone — so it cannot tell you Hindi',
           ha="center", color=RED, fontsize=12.5, fontweight="bold")
    a.text(6, 0.5, "That fading is the vanishing gradient. Attention was invented to fix it.",
           ha="center", color=GOLD, fontsize=12, fontweight="bold")


# ── 12. Projects: finish beats perfect ─────────────────────────────────────
def finish(a):
    title(a, "WHERE THE LEARNING ACTUALLY IS", "the same idea, taken two different distances")
    stages = ["idea", "happy path", "errors", "edge cases", "deployed", "someone used it"]
    for i, s in enumerate(stages):
        x = 0.55 + i * 1.92
        done_a = i < 2
        done_b = True
        # top track: the "perfect" half-project
        col = CYAN if done_a else LINE
        a.add_patch(FancyBboxPatch((x, 3.55), 1.62, 0.78, boxstyle="round,pad=0.04",
                                   ec=col, fc=PANEL, lw=2.0))
        a.text(x + 0.81, 3.94, s, ha="center", va="center",
               color=NAVY if done_a else "#4A5A74", fontsize=10)
        # bottom track: the finished simple project
        a.add_patch(FancyBboxPatch((x, 1.75), 1.62, 0.78, boxstyle="round,pad=0.04",
                                   ec=GREEN, fc="#0F2A26", lw=2.0))
        a.text(x + 0.81, 2.14, s, ha="center", va="center", color=NAVY, fontsize=10)
    a.text(0.55, 4.62, "PERFECT, UNFINISHED", ha="left", color=CYAN, fontsize=12.5, fontweight="bold")
    a.text(0.55, 2.82, "SIMPLE, FINISHED", ha="left", color=GREEN, fontsize=12.5, fontweight="bold")
    a.text(6.3, 3.05, "everything after here is what interviews ask about",
           ha="center", color=RED, fontsize=11.5, fontweight="bold")
    a.text(6, 0.9, "A perfect half-project has no boring parts — so it teaches you nothing",
           ha="center", color=GOLD, fontsize=12.5, fontweight="bold")


DIAGRAMS = {
    "17-prompt-engineering": ("short01-fewshot.png", fewshot),
    "14-java": ("short01-equals.png", equals),
    "11-system-design": ("short01-cache.png", cache),
    "13-neural-networks": ("short01-neuron.png", neuron),
    "18-ai-tools": ("short01-risk.png", risk),
    "19-ai-for-everyone": ("short01-understand.png", understand),
    "21-ai-qna": ("short01-citation.png", citation),
    "22-ai-news": ("short01-news.png", news),
    "23-build-ai-projects": ("short01-ship.png", ship),
    "25-cnn": ("short01-filter.png", filt),
    "26-rnn": ("short01-memory.png", memory),
    "12-projects": ("short01-finish.png", finish),
}


def main():
    for folder, (fname, fn) in DIAGRAMS.items():
        out = os.path.join(ROOT, "topics", folder, "images", fname)
        f, a = fig(12, 6.0)
        a.set_xlim(0, 12); a.set_ylim(0, 6)
        fn(a)
        save(f, out)
    print(f"\n  {len(DIAGRAMS)} rich diagrams regenerated")


if __name__ == "__main__":
    main()
