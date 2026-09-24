"""The hook for each short.

The first version used chapter headings: "Why a dot product is just agreement".
Short-form guidance is a hook of six to eight words that resolves within three
seconds, and the formulas that actually stop a scroll are narrow:

    the correction    "You have been taught X wrong"
    the number        "99% accurate. Catches zero fraud."
    the cost          "This one line costs companies lakhs"
    the confession    "I sent 35 PRs. Two merged."
    the stakes        "Your model is getting worse right now"

Each hook below is one of those, under eight words where possible, and states a
claim the viewer wants resolved. The title stays descriptive for YouTube search;
the hook is what appears on screen.
"""

# folder: (title for search, on-screen hook, [3 beats], takeaway)
HOOKS = {
 "01-mathematics": (
   "Dot product, explained in 60 seconds",
   "Every AI similarity score is **one question**",
   ["Two arrows pointing the **same way** give a big positive number.",
    "**At right angles**, you get zero. No agreement at all.",
    "Pointing **opposite ways** gives a negative. That is the whole idea."],
   "Search, recommendations, embeddings — all of it is this one question."),

 "02-machine-learning": (
   "Overfitting, explained with an exam",
   "**99% in practice. 60% in the real exam.**",
   ["Rohan memorised last year's paper, word for word. Meera understood the chapters.",
    "Practice test: Rohan 99%, Meera 85%. Rohan looks better.",
    "Real exam, new questions: Rohan drops to **60%**. Meera holds **84%**."],
   "The GAP between training and test accuracy IS overfitting. Nothing else."),

 "03-deep-learning": (
   "What 'deep' in deep learning actually means",
   "'Deep' does not mean clever. It means **layers**.",
   ["Layer 1 sees only **edges** — light meeting dark.",
    "Layer 2 combines those edges into **shapes**.",
    "Layer 3 combines shapes into **things**: an eye, a wheel, a letter."],
   "Nobody programmed those stages. Depth forced the network to find them."),

 "04-transformers": (
   "Attention explained without the maths",
   "Same word. **Two completely different meanings.**",
   ["'The **bank** was steep.' 'The **bank** was closed.'",
    "The model reads the whole sentence and **weights** which words matter.",
    "'Steep' pulls it toward the river. 'Closed' pulls it toward money."],
   "That weighting is attention. It is why context finally worked."),

 "05-llms": (
   "What ChatGPT is actually doing",
   "ChatGPT is **not thinking**. Here is what happens.",
   ["Given 'The capital of Maharashtra is', it scores **every word it knows**.",
    "'Mumbai' scores **0.94**. It gets picked. Then the whole thing repeats.",
    "Fluency is the **side effect** of doing that billions of times."],
   "Knowing this tells you exactly when it will confidently invent something."),

 "06-rag-systems": (
   "RAG explained in one image",
   "Stop asking AI to answer **from memory**",
   ["Without RAG, the model sits the exam from memory. It guesses.",
    "With RAG, your question first **searches your documents**.",
    "Those pages go into the prompt. It answers from what is in front of it."],
   "You did not make the student smarter. You changed the exam."),

 "07-agentic-ai": (
   "When you should NOT build an AI agent",
   "Most 'AI agents' are just **for-loops**",
   ["An agent is a model that **decides what to do next**. That is the definition.",
    "Fixed order every single time? That is a pipeline with a bigger bill.",
    "Agents earn their cost when the next step **depends on what came back**."],
   "If you can draw the steps on paper first, you do not need an agent."),

 "08-langchain": (
   "LangChain, explained honestly",
   "LangChain's core idea fits in **one line**",
   ["The output of one step is the input of the next. That is a chain.",
    "The real value is the **plumbing**: retries, parsing, swapping models.",
    "You could write this yourself. The library saves the boring parts."],
   "Learn the pattern, not the library. The pattern outlives every framework."),

 "09-mlops": (
   "Why your model gets worse on its own",
   "Your model is **getting worse right now**",
   ["Nothing in your code changed. The **world** changed.",
    "A model trained on 2023 shoppers meets 2026 shoppers.",
    "Accuracy falls quietly. **No error. No crash. No alert.**"],
   "You find out when a customer complains. Monitor inputs, not just uptime."),

 "10-ai-evaluation": (
   "Why 99% accuracy can be worthless",
   "**99% accurate. Catches zero fraud.**",
   ["1,000 transactions. 10 are fraud. Predict 'not fraud' every single time.",
    "Accuracy: **99%**. Fraud caught: **zero**. The model learned nothing.",
    "**Recall** asks the real question: of all the fraud, how much did I catch?"],
   "On imbalanced data, accuracy makes a useless model look excellent."),

 "11-system-design": (
   "What to cache and what never to cache",
   "Cache the wrong thing. **Serve stale data.**",
   ["IRCTC train list, Delhi to Patna: changes daily, asked 50,000 times an hour. **Cache it.**",
    "Live seat availability: asked just as often, but changes **every second**. Never cache.",
    "Your booking history: barely changes, but asked **once per login**. Not worth it."],
   "Slow to compute AND often repeated AND stays valid. All three, or don't."),

 "12-projects": (
   "Why finishing beats perfecting",
   "Your perfect half-project teaches you **nothing**",
   ["Finishing forces the boring parts: errors, edge cases, deployment.",
    "Those boring parts are **exactly what interviews ask about**.",
    "A perfect half-project has no boring parts — so it has no lessons."],
   "Scope down until you can finish this week. Then do it again."),

 "13-neural-networks": (
   "What one neuron actually does",
   "A neuron does **three things**. That is all.",
   ["Multiply each input by a **weight** — how much that input matters.",
    "Add the results into one number. Income 0.9, credit 0.7, loans 0.4 → **0.61**.",
    "Over the threshold? It **fires**. Loan approved."],
   "Learning is only this: nudging weights until the answers come out right."),

 "13-open-source": (
   "How to get your first PR merged",
   "I sent **35 pull requests. Two merged.**",
   ["The 33 that failed all described what the code already said.",
    "'Get the name.' on a function called getName. Nothing added.",
    "The two that merged answered something you **cannot see** from the signature."],
   "Could a reader work this out from the function name? Then do not send it."),

 "14-java": (
   "The Java bug that fails silently",
   "These two Strings are **equal but not equal**",
   ["`==` asks: are these the **same box in memory**?",
    "`.equals()` asks: do they **hold the same value**?",
    "Small strings get reused by the JVM, so `==` sometimes works — by accident."],
   "Use .equals() for values. The times == works are luck, not logic."),

 "15-spring-boot": (
   "Dependency injection in 60 seconds",
   "Stop writing **new**. Let Spring hand it over.",
   ["Your class declares what it needs: a `UserRepository`.",
    "Spring finds one, builds it, and passes it in.",
    "Your class never knows which implementation it got. That is the point."],
   "Testing gets easy, because you can hand it a fake instead."),

 "16-langgraph": (
   "Chain vs graph, explained",
   "A chain **cannot go backwards**. A graph can.",
   ["Chain: prompt → model → answer. One direction, always.",
    "Graph: if the answer fails a check, **route back** and try differently.",
    "That loop is what makes agentic behaviour possible at all."],
   "If your flow never needs to retry, you do not need a graph yet."),

 "17-prompt-engineering": (
   "The prompt fix nobody teaches",
   "One **example** beats three paragraphs of rules",
   ["'Reply politely and formally' gets you 'Dear Esteemed Customer, we are in receipt...'",
    "Show one example instead: 'order late?' → 'Sorry sir, aapka order kal tak aa jayega.'",
    "Now it matches your tone, your length and your language."],
   "When a prompt is not working, add an example before adding more words."),

 "18-ai-tools": (
   "How to choose an AI tool",
   "Wrong question: **which AI tool is best?**",
   ["Drafting a WhatsApp reply? A wrong answer costs you **ten seconds**.",
    "Summarising a rent agreement? A wrong answer costs you **a clause**.",
    "Same model. Same speed. Completely different amount of checking."],
   "Match the effort to the cost of the mistake, not to the hype."),

 "19-ai-for-everyone": (
   "What AI actually understands",
   "AI does **not understand you**. It matches patterns.",
   ["It has read 'The capital of Bihar is Patna' millions of times.",
    "So it answers Patna, correctly, every time.",
    "Now ask about a village nobody wrote about. **It still answers confidently.**"],
   "The SHAPE of an answer is all it knows. You stay responsible for the facts."),

 "20-ai-careers": (
   "Why 'I know Python' gets rejected",
   "Python is table stakes. **Nobody hires for it.**",
   ["**Tools** — Python, an API call, a notebook. Everyone applying has this.",
    "**Judgement** — which model, and why. This is where the interview happens.",
    "**Evidence** — something running that another person actually used."],
   "One deployed project you can defend beats ten tutorials you followed."),

 "21-ai-qna": (
   "Why AI invents fake research papers",
   "It just cited a **paper that never existed**",
   ["'Sharma & Patel (2021), Indian Journal of Agricultural Science.' Looks perfect.",
    "Real-sounding authors. Real journal. Perfect format. **The paper is invented.**",
    "Nothing looked it up. There is **no lookup step** in the model."],
   "A convincing fake scores as well as a real one. Never cite what you have not opened."),

 "22-ai-news": (
   "How to read an AI headline",
   "'AI beats doctors' — **three questions first**",
   ["**Which test?** 1,000 clean textbook images, not a real OPD queue.",
    "**Versus whom?** Junior residents, not senior radiologists.",
    "**Did the data leak?** The test images were online. Often nobody checked."],
   "Three questions turn most AI headlines into something much smaller."),

 "23-build-ai-projects": (
   "The AI project that gets you hired",
   "8 tutorials or **1 thing people use**?",
   ["Eight notebooks that ran perfectly, first time, prove you can follow steps.",
    "One WhatsApp bot answering your hostel mess menu, used by 40 students.",
    "It broke twice. You fixed it. You wrote down what it still gets wrong."],
   "The boring parts ARE the interview. Only the second one has them."),

 "24-angular": (
   "Angular signals, explained simply",
   "Stop telling the screen to update",
   ["A signal holds a value **and a list of who is watching it**.",
    "Change the value, and every watcher is notified automatically.",
    "No manual change detection. No wondering why the screen is stale."],
   "Same idea as a spreadsheet cell: change one, the rest recalculate."),

 "25-cnn": (
   "How a CNN actually sees an image",
   "A CNN never looks at the **whole image**",
   ["It slides a window a few pixels wide, looking for **one pattern**.",
    "On flat colour: nothing. Straddling a boundary: **edge found**.",
    "Stack many windows and you detect many patterns at once."],
   "The SAME small window slides everywhere. That is why CNNs need so little data."),

 "26-rnn": (
   "Why RNNs forget, explained",
   "By word 50, word 1 is **almost gone**",
   ["'Ravi, who grew up in Patna and later moved to Pune, speaks ___'",
    "Each word updates a small memory passed to the next step.",
    "By the blank, 'Patna' is down to **6%**. It cannot tell you Hindi."],
   "That fading is the vanishing gradient. Attention was invented to fix it."),

 "27-python": (
   "The Python bug that hides for months",
   "This Python function **breaks silently**",
   ["`def add(item, basket=[])` — the list is built **once**, when Python reads the def.",
    "Every call that does not pass a basket shares that **same list**. Forever.",
    "Call it twice and the first item is still there."],
   "Never put a list, dict or set in a default argument. Use None."),

 "28-hackathons": (
   "What hackathon judges actually ask",
   "The demo does not win. **The questions do.**",
   ["Everyone can demo. The screen moves, numbers appear, it looks alive.",
    "Then one judge asks: **'where did that number come from?'**",
    "My own app printed +6.2%. It was `random.uniform()` against a fixed table."],
   "If a number on your screen is a guess, say so — and show the formula."),
}
