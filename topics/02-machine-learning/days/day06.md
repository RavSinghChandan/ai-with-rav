---
day: 6
video: 6
topic: Machine Learning
title: Logistic Regression — the yes/no brain
subtitle: How the spam filter decides, and every yes/no prediction
learn: When to use Logistic vs Linear Regression | The sigmoid S-curve + its formula | Why it's called "regression" (the surprise answer) | How the 0.5 threshold turns probability into YES/NO
---

@callout|yellow|In One Line: Logistic Regression answers YES/NO questions. Spam or not? Pass or fail? Fraud or safe? It gives a probability, then a threshold decides.

@h2|Start here: the watchman at the gate
A society watchman looks at each person walking up: known face, calm, has a delivery bag → **let in**. Unknown, nervous, no reason → **stop**. He's not predicting a *number* — he's making a **yes/no** call from clues.
Yesterday's Linear Regression predicted a **number** (a price). But tons of real problems are **yes or no**: is this email spam? will this customer leave? is this transaction fraud? For those, you need **Logistic Regression** — the yes/no brain.

@h2|Linear vs Logistic — the one difference
@image|images/15-linear-vs-logistic.png|Linear Regression fits a line to predict a number. Logistic Regression fits an S-curve to predict YES or NO.
@bullets
**Linear Regression** → answer is a **number** (price, sales, temperature). Straight line.
**Logistic Regression** → answer is **yes/no** (spam, fraud, pass/fail). S-curve.
@end
@callout|green|Quick test: "Am I predicting a number, or a yes/no?" Number → Linear. Yes/No (a category) → Logistic. That single question tells you which one to reach for.

@h2|The magic: the S-curve (sigmoid)
@image|images/16-sigmoid.png|The sigmoid squashes ANY score into a probability between 0 and 1. Right of the middle = likely YES, left = likely NO.
A straight line can shoot off to any number — but a probability must stay between **0 and 1**. So Logistic Regression runs the line's score through a special **S-shaped curve** (the *sigmoid*) that squashes anything into a 0–1 probability.
@bullets
A very "spammy" email → score is high → sigmoid pushes it near **1** (almost certainly spam)
A clearly normal email → score is low → sigmoid pushes it near **0** (not spam)
@end
@callout|green|The sigmoid is the whole trick. It turns "how spammy is this?" (a raw score) into "what's the probability it's spam?" (a clean number between 0 and 1).

@h2|The formula (for the curious — skip if you like)
@image|images/18-sigmoid-formula.png|The sigmoid formula. Notice z = mx + c is the exact same line from Day 5 — the sigmoid just wraps around it.
Here's the actual formula behind the S-curve. Don't be scared — it's simpler than it looks:
@bullets
**z = m·x + c** → this is literally the **same straight line from Day 5** (Linear Regression's line).
**P = 1 / (1 + e^(-z))** → we feed that line's score `z` into this, and out comes a probability `P` between 0 and 1.
**e** → just a fixed number (2.718...), like π. Nothing to memorise.
@end
@callout|green|The big idea: Logistic Regression = Linear Regression's straight line, wrapped in a sigmoid. Same `mx + c`, then squashed to a 0–1 probability. That's the entire difference. Technical folks: this is why it's linear "under the hood." Non-technical folks: just remember — it's the same line, made into a yes/no.

@h2|Wait — why is it called "regression" if it's yes/no?
Great question, and almost no course explains it. "Regression" usually means predicting a number — so why call a yes/no method "regression"?
@bullets
Because under the hood, it **first predicts a number** — the probability (like 0.94). That part IS regression (predicting a number between 0 and 1).
Only at the **very end** does the threshold turn that number into yes/no.
So the name comes from the *middle* step: it **regresses a probability**, then classifies. The classification is bolted on top.
@end
@callout|yellow|One-line answer: it's called regression because it predicts a **probability** (a number) first — the yes/no decision is just the final step on top of that. So it's really "probability regression, then a cutoff."

@h2|The threshold: turning probability into a decision
@image|images/17-threshold.png|The model gives a probability; the 0.5 threshold turns it into a final YES or NO.
The model gives a probability like **0.94**. To make a real decision, you pick a **threshold** — usually 0.5:
@bullets
probability **above 0.5** → **YES** (spam → junk folder)
probability **below 0.5** → **NO** (safe → inbox)
@end
@callout|green|You can MOVE the threshold. For fraud, you might use 0.3 (catch more, even with false alarms). For blocking someone, maybe 0.8 (only when very sure). The threshold is your control dial.

@h2|Train a spam classifier — a few lines
@code
from sklearn.linear_model import LogisticRegression

# X = features (e.g. num of $ signs, CAPS words, links)
# y = 1 for spam, 0 for not-spam
model = LogisticRegression()
model.fit(X_train, y_train)

print(model.predict([[5, 8, 3]]))         # -> [1]  (spam)
print(model.predict_proba([[5, 8, 3]]))   # -> [[0.06, 0.94]]  94% spam
@end
@callout|yellow|`predict` gives the yes/no. `predict_proba` gives the probability behind it — that 0.94 is the sigmoid's output. Same 5-line pattern as Linear Regression, just a different answer type.

@h2|Recap — the 20-second version
@bullets
Logistic Regression answers **yes/no** questions (spam, fraud, churn).
Use it when the answer is a **category**, not a number.
The **sigmoid (S-curve)** turns any score into a 0–1 **probability**.
A **threshold** (usually 0.5) turns the probability into the final YES/NO.
You can move the threshold to be stricter or looser.
@end
@callout|teal|Next up — Video 7: Decision Trees. The "20 Questions" game that can classify almost anything — and the easiest algorithm to actually see thinking. See you Day 7.
