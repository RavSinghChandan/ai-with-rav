---
day: 1
topic: Machine Learning
series: AI Shorts
video: 1
title: Overfitting, in 90 seconds
subtitle: The student who memorised the answer key
learn: What overfitting actually is | The exam-hall story | How to spot it in one number | The fix that costs nothing
---

@callout|yellow|In One Line: A model that scores 99% in training and 60% in the real world did not learn. It memorised.

@h2|Two students, one exam
**Rohan** memorised last year's question paper. Every answer, word for word.

**Meera** understood the chapters.

Practice test: Rohan scores 99%, Meera 85%. Rohan looks better.

Then the real exam has *new* questions. Rohan drops to 60%. Meera scores 84%.

@image|images/img01-overfitting.png|Rohan memorised the paper. Meera learned the subject. Only one of them survives new questions.

@h2|That is overfitting
Rohan is an overfit model. He learned the **noise** — the exact wording of last
year's paper — instead of the **pattern** underneath.

Your model does this when it is too complex for the data you gave it.

@h2|Spot it with one number
Compare two scores:

@bullets
**Training accuracy** — how it does on data it has seen
**Test accuracy** — how it does on data it has never seen
@end

A big gap between them *is* overfitting. 99% and 60% is not a good model having
a bad day. It is a memoriser being found out.

@callout|red|The opposite also exists. Underfitting is a student who read nothing — bad in practice AND bad in the exam.

@h2|The cheapest fix
Give it less room to memorise: a simpler model, fewer features, or more data.

@callout|green|Always hold back test data the model has never seen. It is the only honest exam you can give it.
