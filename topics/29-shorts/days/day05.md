---
day: 5
topic: Machine Learning
series: AI Shorts
video: 5
title: 99% accurate and completely useless
subtitle: Why accuracy is the wrong metric
learn: The 99% model that finds nothing | Why accuracy hides failure | Precision vs recall in plain words | Which metric to pick
---

@callout|yellow|In One Line: If 99 of 100 transactions are genuine, a model that says "genuine" every time is 99% accurate — and catches zero fraud.

@h2|The model that does nothing
Fraud detection. Out of 1,000 transactions, 10 are fraud.

Build a model that predicts **"not fraud"** every single time. No thinking at all.

Accuracy: **99%**. It caught nothing. It is worthless.

@image|images/img05-accuracy-trap.png|990 right, 10 missed — and every missed one is the only kind that mattered

@h2|The two questions that matter
@bullets
**Precision** — of the ones I flagged, how many were really fraud? *(Am I crying wolf?)*
**Recall** — of all the real fraud, how much did I catch? *(Am I missing it?)*
@end

Our do-nothing model has **zero recall**. It caught none of the 10. Accuracy
never showed that, because 990 easy correct answers drowned out 10 expensive
mistakes.

@h2|You must choose which error hurts
@callout|red|Missing fraud costs money. Flagging a good customer costs trust. Cancer screening and spam filters sit at opposite ends of that trade.

Pick the one your business actually feels. Then optimise for it, and say out loud
which one you chose.

@callout|green|When classes are imbalanced, accuracy is the metric that makes a useless model look excellent.
