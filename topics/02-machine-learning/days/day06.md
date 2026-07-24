---
day: 6
video: 6
topic: Machine Learning
title: Logistic Regression — the yes/no brain
subtitle: How the spam filter decides, and every yes/no prediction
learn: When to use Logistic vs Linear Regression | The S-curve (sigmoid) that gives a probability | How the 0.5 threshold turns probability into YES/NO | Train a spam classifier in a few lines
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
