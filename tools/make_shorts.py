"""Generate one short (content + diagram) for every topic folder.

One idea per topic, chosen to be the thing a beginner most often gets wrong.
Each produces a two-page landscape PDF: the diagram, then the words.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from viral_style import *          # noqa: F403

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# topic folder -> (Topic name, title, hook, [3 beats], takeaway, caption, draw fn key)
SHORTS = {
 "01-mathematics": ("Mathematics", "Why a dot product is just agreement",
   "A dot product asks one question: **are these two arrows pointing the same way?**",
   ["Two vectors pointing the **same way** give a big positive number.",
    "**At right angles** gives zero — no agreement at all.",
    "**Opposite ways** gives a negative number. That is the whole intuition."],
   "Every similarity score in AI — search, recommendations, embeddings — is this one question.",
   "Same direction, no direction, opposite direction", "agreement"),

 "03-deep-learning": ("Deep Learning", "What 'deep' actually means",
   "Deep does not mean clever. It means **layers**, each one seeing a bigger picture.",
   ["Layer 1 sees **edges**. Just light and dark boundaries.",
    "Layer 2 combines edges into **shapes** — a curve, a corner.",
    "Layer 3 combines shapes into **things** — an eye, a wheel, a letter."],
   "Nobody programmed those stages. The network found them because depth forces it to.",
   "Edges become shapes become objects", "layers"),

 "04-transformers": ("Transformers", "Attention, in one sentence",
   "Attention lets every word **look at every other word** before deciding what it means.",
   ["'The **bank** was steep' and 'The **bank** was closed' — same word, different meaning.",
    "The model reads the whole sentence and **weights** which other words matter.",
    "'Steep' pulls *bank* toward the river. 'Closed' pulls it toward money."],
   "That weighting is attention. It is why context finally worked.",
   "The same word, pulled two ways by its neighbours", "attention"),

 "05-llms": ("LLMs", "An LLM only predicts the next word",
   "ChatGPT is not thinking. It is answering: **what word comes next?** — again and again.",
   ["Given 'The capital of Maharashtra is', it scores every word it knows.",
    "'Mumbai' scores highest, so it is picked. Then the whole thing repeats.",
    "Fluency is the **side effect** of doing that billions of times."],
   "Knowing this tells you exactly when it will confidently invent something.",
   "One word at a time, each one fed back in", "nextword"),

 "06-rag-systems": ("RAG Systems", "RAG is an open-book exam",
   "A model without RAG sits the exam from memory. With RAG, it gets **the book**.",
   ["Your question first **searches your documents** for the relevant pages.",
    "Those pages are pasted into the prompt alongside your question.",
    "The model answers from what is in front of it, not from memory."],
   "That is why RAG cuts hallucination — you changed the exam, not the student.",
   "Retrieve first, then answer from what was retrieved", "rag"),

 "07-agentic-ai": ("Agentic AI", "When you do NOT need an agent",
   "If you can **draw the steps on paper** before running it, you need a function, not an agent.",
   ["An agent is a model that **decides what to do next**. That is the whole definition.",
    "Fixed order every time? That is a pipeline with extra billing.",
    "Agents earn their cost when the next step **depends on what came back**."],
   "Most 'agent' demos are for-loops. Know which one you are building.",
   "Fixed path versus the model choosing", "agent"),

 "08-langchain": ("LangChain", "A chain is just a pipeline",
   "LangChain's core idea is small: **the output of one step is the input of the next**.",
   ["Prompt → model → parse → next prompt. Nothing magical.",
    "The value is the **plumbing**: retries, parsing, swapping models.",
    "You can write this yourself. The library saves the boring parts."],
   "Learn the pattern, not the library. The pattern outlives every framework.",
   "Output of one step feeds the next", "chain"),

 "09-mlops": ("MLOps", "Your model will get worse on its own",
   "Nothing in the code changed. The **world** changed. That is data drift.",
   ["A model trained on 2023 shopping habits meets 2026 shoppers.",
    "Accuracy falls quietly — no error, no crash, no alert.",
    "You only find out when someone complains about the results."],
   "Monitor the inputs, not just uptime. Drift is silent by nature.",
   "Same model, shifting world, falling accuracy", "drift"),

 "10-ai-evaluation": ("AI Evaluation", "99% accurate and useless",
   "If 99 of 100 transactions are genuine, saying **'genuine' every time** is 99% accurate.",
   ["That model catches **zero** fraud. It has learned nothing.",
    "**Recall** asks: of all the real fraud, how much did I catch? Here, none.",
    "Accuracy hid it because 990 easy answers drowned 10 expensive mistakes."],
   "On imbalanced data, accuracy is the metric that makes a useless model look excellent.",
   "990 right, 10 missed — and the 10 were the point", "accuracy"),

 "11-system-design": ("System Design", "Cache the expensive thing, not everything",
   "A cache is a bet: **this will be asked again**. Bet wrong and you have added complexity for nothing.",
   ["Cache what is **slow to compute** and **often repeated**.",
    "Never cache what changes per user per second — you pay the cost, never the benefit.",
    "Every cache needs an answer to: **when does this become wrong?**"],
   "If you cannot say when an entry goes stale, you are not ready to cache it.",
   "Slow and repeated is worth caching; nothing else is", "cache"),

 "13-neural-networks": ("Neural Networks", "A neuron is a weighted vote",
   "One neuron does three things: **multiply, add, decide**. That is it.",
   ["Each input is multiplied by a **weight** — how much that input matters.",
    "The results are added together into a single number.",
    "If that number crosses a threshold, the neuron **fires**."],
   "Learning is nothing more than adjusting those weights until the votes come out right.",
   "Multiply, add, decide", "neuron"),

 "14-java": ("Java", "== compares boxes, .equals compares contents",
   "Two Strings that look identical can still be **not equal** in Java. Here is why.",
   ["`==` asks: are these the **same object in memory**?",
    "`.equals()` asks: do they **hold the same value**?",
    "Small strings get reused by the JVM, so `==` sometimes works — by accident."],
   "Use .equals() for values. The times == works are luck, not logic.",
   "Same box, or same contents?", "equals"),

 "15-spring-boot": ("Spring Boot", "Dependency injection in one picture",
   "You stop writing `new`. Spring **hands you** what you asked for.",
   ["Your class declares: I need a `UserRepository`.",
    "Spring finds one, builds it, and passes it in.",
    "Your class never knows which implementation it got — that is the point."],
   "Testing becomes easy because you can hand it a fake instead.",
   "You declare the need; the container supplies it", "di"),

 "16-langgraph": ("LangGraph", "A graph lets the agent go backwards",
   "A chain only moves forward. A **graph** can loop back and try again.",
   ["Chain: prompt → model → answer. One direction, always.",
    "Graph: if the answer fails a check, **route back** and retry differently.",
    "That loop is what makes 'agentic' behaviour possible at all."],
   "If your flow never needs to go back, you do not need a graph yet.",
   "One direction versus a loop that can retry", "graph"),

 "17-prompt-engineering": ("Prompt Engineering", "Show, don't describe",
   "One **example** beats three paragraphs of instructions. Every time.",
   ["'Write formally' is vague — the model guesses what you mean.",
    "Give one input and one ideal output, and it matches the pattern.",
    "Two or three examples pin down tone, length and format together."],
   "When a prompt is not working, add an example before adding more words.",
   "Instructions guess; examples pin it down", "fewshot"),

 "18-ai-tools": ("AI Tools", "Pick the tool by the failure you can afford",
   "The question is not which tool is best. It is **what happens when it is wrong**.",
   ["Drafting an email? A wrong answer costs you ten seconds.",
    "Summarising a contract? A wrong answer costs you a clause.",
    "The second case needs citation and review. The first does not."],
   "Match the checking effort to the cost of the mistake, not to the hype.",
   "Cheap mistakes and expensive mistakes need different tools", "risk"),

 "19-ai-for-everyone": ("AI for Everyone", "AI does not understand you",
   "It has read enormous amounts of text and learned **which words follow which**.",
   ["That is genuinely useful — most work is patterned language.",
    "It is also why it can be confidently, fluently wrong.",
    "It has no way to know the difference between true and plausible."],
   "Use it for the first draft. You stay responsible for the facts.",
   "Pattern, not understanding", "understand"),

 "20-ai-careers": ("AI Careers", "Why 'I know Python' is not enough",
   "Every AI job asks for Python. **None of them hire you for Python.**",
   ["**Tools** — Python, an API call, a notebook. Everyone applying has this.",
    "**Judgement** — which model, and why. This is where interviews happen.",
    "**Evidence** — something running that another person actually used."],
   "One deployed project you can defend beats ten tutorials you followed.",
   "Most stop at layer 1 and apply anyway", "layers3"),

 "21-ai-qna": ("AI Q&A", "Why it invents citations",
   "A made-up reference is not a lie. It is the model doing **exactly what it was built to do**.",
   ["It predicts text that *looks* like a citation — author, year, journal.",
    "A plausible-looking fake scores as well as a real one during prediction.",
    "It has no lookup step, so nothing checks whether the paper exists."],
   "Never accept a citation you have not opened. This failure is structural.",
   "Plausible shape, no lookup step", "citation"),

 "22-ai-news": ("AI News", "Read the benchmark, not the headline",
   "'Beats humans at X' usually means: **on this test, under these conditions**.",
   ["Ask what the test actually measured — and who chose it.",
    "Ask what it was compared against. Untrained humans? Experts?",
    "Ask whether the test data leaked into training. Often nobody checked."],
   "Three questions turn most AI headlines into something much smaller and more honest.",
   "The headline, and the three questions under it", "news"),

 "23-build-ai-projects": ("Build AI Projects", "Ship the smallest useful thing",
   "Your first AI project should do **one task for one person** — and actually run.",
   ["A tutorial notebook proves you can follow steps. Nothing more.",
    "Something deployed, that another person used, proves you can finish.",
    "Write down honestly what it does badly. Almost nobody does this."],
   "That honest limitations note is the strongest thing in an AI portfolio.",
   "Notebook versus something someone used", "ship"),

 "24-angular": ("Angular", "A signal is a value that tells you it changed",
   "The old way: you tell the view to update. The **signal** way: it already knows.",
   ["A signal holds a value and a **list of who is watching it**.",
    "Change the value and every watcher is notified automatically.",
    "No manual change detection, no wondering why the screen is stale."],
   "This is the same idea as a spreadsheet cell. Change one, the rest recalculate.",
   "The value notifies its watchers", "signal"),

 "25-cnn": ("CNN", "A filter is a tiny sliding window",
   "A CNN does not look at the whole image. It slides a **small window** over it.",
   ["The window is a few pixels wide and looks for one pattern — say a vertical edge.",
    "It slides across the entire image, marking where that pattern appears.",
    "Stack many windows and you detect many patterns at once."],
   "Sliding the same small filter everywhere is why CNNs need so little data per feature.",
   "One small window, slid across everything", "filter"),

 "26-rnn": ("RNN", "Memory that fades",
   "An RNN reads a sentence word by word, carrying a **memory** forward. That memory leaks.",
   ["Each word updates a small hidden state passed to the next step.",
    "By word fifty, the influence of word one has almost vanished.",
    "That fading is the vanishing gradient — the reason attention was invented."],
   "RNNs taught us sequence matters. Transformers fixed the forgetting.",
   "Early words fade as the sentence grows", "memory"),

 "12-projects": ("Projects", "Finish beats perfect",
   "An unfinished impressive project teaches you **less** than a finished simple one.",
   ["Finishing forces the boring parts: errors, edge cases, deployment.",
    "Those boring parts are exactly what interviews ask about.",
    "A perfect half-project has no boring parts, so it teaches nothing."],
   "Scope down until you can finish this week. Then do it again.",
   "Where the learning actually is", "finish"),
}


def draw(key, ax, a):
    """Each diagram is hand-drawn to show its specific idea."""
    a.set_xlim(0, 12); a.set_ylim(0, 6)

    if key == "agreement":
        for x, ang, lbl, col, val in [(2.2, 0, "same way", GREEN, "+1"),
                                      (6.0, 90, "right angles", MUTED, "0"),
                                      (9.8, 180, "opposite", RED, "-1")]:
            import math
            a.add_patch(FancyArrowPatch((x, 2.4), (x + 1.3, 2.4), arrowstyle="-|>",
                                        mutation_scale=20, color=NAVY, lw=3))
            dx = 1.3 * math.cos(math.radians(ang)); dy = 1.3 * math.sin(math.radians(ang))
            a.add_patch(FancyArrowPatch((x, 2.4), (x + dx, 2.4 + dy), arrowstyle="-|>",
                                        mutation_scale=20, color=col, lw=3))
            a.text(x + 0.6, 1.5, lbl, ha="center", color=MUTED, fontsize=12)
            a.text(x + 0.6, 0.85, val, ha="center", color=col, fontsize=22, fontweight="bold")
        a.text(6, 5.3, "DOT PRODUCT  =  HOW MUCH DO THEY AGREE?", ha="center",
               color=NAVY, fontsize=14, fontweight="bold")

    elif key == "layers":
        for i, (lbl, detail, col) in enumerate([
                ("LAYER 1", "edges", CYAN), ("LAYER 2", "shapes", GOLD),
                ("LAYER 3", "objects", GREEN)]):
            x = 1.0 + i * 3.7
            card(a, x, 1.6, 3.0, 2.6, col, lw=2.4)
            a.text(x + 1.5, 3.5, lbl, ha="center", color=col, fontsize=13, fontweight="bold")
            a.text(x + 1.5, 2.6, detail, ha="center", color=NAVY, fontsize=19, fontweight="bold")
            if i < 2:
                arrow(a, x + 3.05, 2.9, x + 3.65, 2.9)
        a.text(6, 5.2, "EACH LAYER SEES A BIGGER PICTURE", ha="center",
               color=NAVY, fontsize=14, fontweight="bold")
        a.text(6, 0.8, "Nobody programmed these stages — depth forced them",
               ha="center", color=MUTED, fontsize=12)

    elif key == "attention":
        a.text(6, 5.3, 'THE SAME WORD, PULLED TWO WAYS', ha="center",
               color=NAVY, fontsize=14, fontweight="bold")
        for y, sent, pull, col in [(3.7, "The  bank  was  steep", "river", GREEN),
                                   (1.9, "The  bank  was  closed", "money", CYAN)]:
            a.text(2.6, y, sent, ha="left", color=NAVY, fontsize=16, fontweight="bold")
            arrow(a, 7.2, y + 0.1, 8.6, y + 0.1, col, lw=2.4)
            a.text(9.6, y + 0.1, pull, ha="center", color=col, fontsize=16, fontweight="bold")
        a.text(6, 0.8, "Attention weights which neighbours matter",
               ha="center", color=MUTED, fontsize=12)

    elif key == "nextword":
        a.text(6, 5.3, "ONE WORD AT A TIME", ha="center", color=NAVY,
               fontsize=14, fontweight="bold")
        card(a, 0.8, 3.0, 4.6, 1.3, LINE, lw=2)
        a.text(3.1, 3.65, "The capital of Maharashtra is", ha="center", color=NAVY, fontsize=12.5)
        arrow(a, 5.5, 3.65, 6.4, 3.65, CYAN, lw=2.4)
        for i, (w, p, col) in enumerate([("Mumbai", "0.94", GREEN),
                                         ("Pune", "0.03", MUTED),
                                         ("Nagpur", "0.01", MUTED)]):
            y = 4.0 - i * 0.95
            card(a, 6.6, y - 0.32, 2.2, 0.72, col, lw=1.8)
            a.text(7.7, y, w, ha="center", color=col if col != MUTED else NAVY,
                   fontsize=13, fontweight="bold")
            a.text(9.4, y, p, ha="left", color=col, fontsize=13, fontweight="bold")
        a.text(6, 1.0, "Pick the top word, add it, repeat",
               ha="center", color=MUTED, fontsize=12)

    elif key == "rag":
        for i, (lbl, col) in enumerate([("YOUR\nQUESTION", NAVY),
                                        ("SEARCH YOUR\nDOCUMENTS", CYAN),
                                        ("PASTE PAGES\nINTO PROMPT", GOLD),
                                        ("MODEL\nANSWERS", GREEN)]):
            x = 0.6 + i * 2.95
            card(a, x, 2.1, 2.4, 1.9, col, lw=2.2)
            a.text(x + 1.2, 3.05, lbl, ha="center", va="center", color=col,
                   fontsize=12, fontweight="bold")
            if i < 3:
                arrow(a, x + 2.45, 3.05, x + 2.9, 3.05)
        a.text(6, 5.2, "OPEN-BOOK EXAM", ha="center", color=NAVY,
               fontsize=14, fontweight="bold")
        a.text(6, 1.2, "The model answers from the pages, not from memory",
               ha="center", color=MUTED, fontsize=12)

    elif key == "agent":
        a.text(3.0, 5.2, "PIPELINE", ha="center", color=CYAN, fontsize=14, fontweight="bold")
        a.text(9.0, 5.2, "AGENT", ha="center", color=GOLD, fontsize=14, fontweight="bold")
        a.plot([5.9, 5.9], [1.2, 4.6], color=LINE, lw=1.6, ls=(0, (5, 4)))
        for i, s in enumerate(["Step 1", "Step 2", "Step 3"]):
            y = 3.7 - i * 1.2
            card(a, 1.6, y, 2.8, 0.85, CYAN, lw=2)
            a.text(3.0, y + 0.42, s, ha="center", va="center", color=NAVY,
                   fontsize=13, fontweight="bold")
            if i < 2:
                arrow(a, 3.0, y - 0.05, 3.0, y - 0.3, MUTED, lw=1.8)
        a.text(3.0, 0.55, "always the same path", ha="center", color=MUTED, fontsize=11.5)
        a.add_patch(plt.Circle((9.0, 3.6), 0.6, ec=GOLD, fc=PANEL, lw=2.4))
        a.text(9.0, 3.6, "model", ha="center", va="center", color=GOLD,
               fontsize=12, fontweight="bold")
        for dx, lbl in [(-1.85, "Tool A"), (0, "Tool B"), (1.85, "Tool C")]:
            card(a, 9.0 + dx - 0.78, 1.5, 1.56, 0.8, MUTED, lw=1.8)
            a.text(9.0 + dx, 1.9, lbl, ha="center", va="center", color=NAVY, fontsize=11)
            arrow(a, 9.0, 2.95, 9.0 + dx, 2.4, MUTED, lw=1.6, dashed=True)
        a.text(9.0, 0.55, "chooses based on what came back", ha="center",
               color=MUTED, fontsize=11.5)

    elif key in ("chain", "di", "signal", "graph"):
        titles = {"chain": ("PROMPT", "MODEL", "PARSE", "NEXT"),
                  "di":    ("YOUR CLASS", "asks for", "CONTAINER", "hands it in"),
                  "signal": ("SIGNAL", "value changes", "WATCHERS", "all update"),
                  "graph": ("START", "CHECK", "PASS →", "FAIL ↺")}
        t = titles[key]
        for i, lbl in enumerate(t):
            x = 0.7 + i * 2.9
            col = [CYAN, GOLD, GREEN, NAVY][i]
            card(a, x, 2.3, 2.4, 1.5, col, lw=2.2)
            a.text(x + 1.2, 3.05, lbl, ha="center", va="center", color=col,
                   fontsize=12.5, fontweight="bold")
            if i < 3:
                arrow(a, x + 2.45, 3.05, x + 2.85, 3.05)
        if key == "graph":
            a.add_patch(FancyArrowPatch((10.3, 2.25), (1.9, 2.25),
                                        arrowstyle="-|>", mutation_scale=18,
                                        color=RED, lw=2.2,
                                        connectionstyle="arc3,rad=0.28"))
            a.text(6, 1.05, "the loop back is what a chain cannot do",
                   ha="center", color=RED, fontsize=12.5, fontweight="bold")
        a.text(6, 5.2, key.upper(), ha="center", color=NAVY, fontsize=14, fontweight="bold")

    elif key == "drift":
        import numpy as np
        xs = np.linspace(0, 10, 100)
        a.plot(xs + 1, 4.2 - 0.0 * xs, color=CYAN, lw=3, label="model (unchanged)")
        a.plot(xs + 1, 4.2 - 0.22 * xs, color=RED, lw=3, ls=(0, (6, 3)),
               label="real accuracy")
        a.text(6, 5.3, "NOTHING IN THE CODE CHANGED", ha="center",
               color=NAVY, fontsize=14, fontweight="bold")
        a.text(11.2, 4.25, "what you\nassume", ha="left", va="center", color=CYAN,
               fontsize=11.5, fontweight="bold")
        a.text(11.2, 2.0, "what is\nhappening", ha="left", va="center", color=RED,
               fontsize=11.5, fontweight="bold")
        a.text(6, 0.9, "No error. No crash. No alert.", ha="center",
               color=MUTED, fontsize=12.5)

    elif key == "accuracy":
        cols_, rows_ = 25, 4
        for r in range(rows_):
            for c_ in range(cols_):
                i = r * cols_ + c_
                x = 1.0 + c_ * 0.40; y = 4.3 - r * 0.42
                a.add_patch(plt.Circle((x, y), 0.145,
                                       color=RED if i >= 99 else "#2A3854"))
        a.text(6, 5.4, 'THE MODEL THAT ALWAYS SAYS "NOT FRAUD"',
               ha="center", color=NAVY, fontsize=14, fontweight="bold")
        card(a, 1.4, 0.7, 4.0, 1.2, GOLD, lw=2.2)
        a.text(3.4, 1.55, "ACCURACY", ha="center", color=MUTED, fontsize=11)
        a.text(3.4, 1.05, "99%", ha="center", color=GOLD, fontsize=22, fontweight="bold")
        card(a, 6.6, 0.7, 4.0, 1.2, RED, lw=2.2)
        a.text(8.6, 1.55, "FRAUD CAUGHT", ha="center", color=MUTED, fontsize=11)
        a.text(8.6, 1.05, "0%", ha="center", color=RED, fontsize=22, fontweight="bold")

    elif key == "layers3":
        for lbl, sub, col, y, w in [
                ("LAYER 3 · EVIDENCE", "something running that others used", GREEN, 3.7, 7.0),
                ("LAYER 2 · JUDGEMENT", "which model, and why", GOLD, 2.4, 8.4),
                ("LAYER 1 · TOOLS", "Python, an API call, a notebook", CYAN, 1.1, 9.8)]:
            card(a, 6 - w / 2, y, w, 1.1, col, lw=2.4)
            a.text(6, y + 0.72, lbl, ha="center", color=col, fontsize=12.5, fontweight="bold")
            a.text(6, y + 0.32, sub, ha="center", color=NAVY, fontsize=11.5)
        a.text(6, 5.3, "WHAT COMPANIES ACTUALLY HIRE FOR", ha="center",
               color=NAVY, fontsize=14, fontweight="bold")
        a.text(6, 0.55, "Most stop at layer 1 and apply anyway", ha="center",
               color=RED, fontsize=12.5, fontweight="bold")

    else:
        # Two-panel contrast, used by the remaining topics.
        pairs = {
          "cache":   ("WORTH CACHING", "slow + repeated", "NOT WORTH IT", "changes every second"),
          "neuron":  ("MULTIPLY  ·  ADD", "inputs × weights, summed", "DECIDE", "over threshold? fire"),
          "equals":  ("==", "same box in memory", ".equals()", "same contents"),
          "fewshot": ("DESCRIBE", '"write formally"', "SHOW", "one input, one ideal output"),
          "risk":    ("CHEAP MISTAKE", "a draft email", "EXPENSIVE MISTAKE", "a contract clause"),
          "understand": ("WHAT IT DOES", "predicts likely words", "WHAT IT DOES NOT", "know true from plausible"),
          "citation": ("LOOKS RIGHT", "author, year, journal", "NEVER CHECKED", "no lookup step exists"),
          "news":    ("THE HEADLINE", '"beats humans at X"', "THE QUESTIONS", "which test? vs whom? leaked?"),
          "ship":    ("A NOTEBOOK", "proves you followed steps", "SOMETHING USED", "proves you finished"),
          "filter":  ("ONE SMALL WINDOW", "looks for one pattern", "SLID EVERYWHERE", "marks every match"),
          "memory":  ("WORD 1", "strong signal", "WORD 50", "almost gone"),
          "finish":  ("PERFECT HALF", "no boring parts", "FINISHED SIMPLE", "errors, edges, deploy"),
        }
        left_t, left_s, right_t, right_s = pairs.get(key, ("A", "", "B", ""))
        card(a, 0.7, 1.5, 4.9, 3.0, MUTED, lw=2.2)
        a.text(3.15, 3.55, left_t, ha="center", color=MUTED, fontsize=15, fontweight="bold")
        a.text(3.15, 2.7, left_s, ha="center", color=NAVY, fontsize=12.5)
        card(a, 6.4, 1.5, 4.9, 3.0, CYAN, lw=2.6)
        a.text(8.85, 3.55, right_t, ha="center", color=CYAN, fontsize=15, fontweight="bold")
        a.text(8.85, 2.7, right_s, ha="center", color=NAVY, fontsize=12.5)
        arrow(a, 5.75, 3.0, 6.3, 3.0, GOLD, lw=2.6)


def main():
    made = 0
    for folder, (topic, title, hook, beats, takeaway, caption, key) in SHORTS.items():
        tdir = os.path.join(ROOT, "topics", folder)
        if not os.path.isdir(tdir):
            print("  skip (no folder):", folder); continue
        os.makedirs(os.path.join(tdir, "shorts"), exist_ok=True)
        os.makedirs(os.path.join(tdir, "images"), exist_ok=True)

        img_rel = f"images/short01-{key}.png"
        f, a = fig(12, 6.0)
        draw(key, None, a)
        save(f, os.path.join(tdir, img_rel))

        body = [f"---", f"topic: {topic}", "short: 1", f"title: {title}", "---", "",
                f"@hook|{hook}", "", f"@image|{img_rel}|{caption}", ""]
        for b in beats:
            body += [f"@beat|{b}", ""]
        body += [f"@takeaway|{takeaway}", ""]
        open(os.path.join(tdir, "shorts", "s01.md"), "w").write("\n".join(body))
        made += 1
    print(f"\n  {made} shorts written")


if __name__ == "__main__":
    main()
