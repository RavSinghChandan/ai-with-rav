---
day: 15
video: 15
topic: Machine Learning
title: Overfitting & Underfitting — the most important lesson
subtitle: Why some models ace practice but fail the real exam
learn: The two ways EVERY model can fail | Signal vs noise — what to learn, what to ignore | The tell-tale sign (practice score vs exam score) | The sweet spot in the middle | How to fix each one
---

@callout|yellow|In One Line: One student learns too little and fails everything. Another memorises the practice papers word-for-word and still fails the real exam. The best student understands the pattern. Every ML model is one of these three — and today you learn to build the third one.

@h2|Start here: the most important lesson in all of ML
You've now met a whole toolbox — linear regression, trees, forests, SVM, K-Means, PCA. But here's the secret no beginner is told: **every single one of them can fail the exact same two ways.** Learning the algorithms is easy. Knowing *how they fail* is what makes you an actual ML engineer.
This is the lesson that matters more than any algorithm: **how do you build a model that works on NEW data it has never seen?** Because a model that only works on data it already saw is useless.

@h2|Three students, one exam
@image|images/55-three-students.png|Three students fitting the same dots. UNDERFIT (left): a straight line that learns too little. JUST RIGHT (middle): a smooth curve that follows the real pattern. OVERFIT (right): a wild line that memorises every single dot.
Imagine three students preparing for an exam using practice papers (the dots):
@bullets
**Student A — Underfit:** barely studies. His answer is a lazy straight line that misses the real pattern. He fails the practice papers *and* the real exam.
**Student B — Just right:** actually **understands the pattern.** A smooth curve that follows the real trend. He does well on practice *and* the real exam.
**Student C — Overfit:** **memorises every practice paper word-for-word** — even the typos. A wild wiggly line touching every dot. Perfect on practice… but the real exam has slightly different questions, and he crashes.
@end
@callout|green|That's the entire lesson in one picture. **Underfit** = learns too little. **Overfit** = memorises too much. **Just right** = understands the pattern. Your whole job in ML is to build Student B.

@h2|Signal vs noise — the key idea
@image|images/56-signal-noise.png|The green curve is the SIGNAL — the real pattern worth learning. But some dots sit off the curve just by random chance — that's NOISE. A good model learns the signal and ignores the noise.
Why does memorising (overfitting) fail? Because real data has two things mixed together:
@bullets
**Signal** → the real, repeatable pattern. This is what's actually true and worth learning.
**Noise** → random wiggles, flukes, measurement errors. A dot might sit high just by chance — it means nothing.
@end
@callout|red|The overfit student's mistake: he **chases the noise.** He bends his answer to touch every random dot, thinking the flukes are real rules. On new data, those flukes don't repeat — so he's wrong. The whole trick of ML is: **learn the signal, ignore the noise.**

@h2|The tell-tale sign: practice score vs exam score
@image|images/57-train-test.png|Compare each student's practice (train) score and real-exam (test) score. Underfit: both low. Just right: both high, small gap. Overfit: practice 100 but exam 60 — a BIG gap. That gap is how you catch overfitting.
How do you *catch* which student you've built? Simple — you split your data in two: **train** (practice papers to study from) and **test** (a fresh exam it has never seen).
@bullets
**Underfit** → low on *both* practice and exam (it never learned).
**Just right** → high on both, with a **small gap** (it truly understands).
**Overfit** → near-perfect on practice, but **much lower on the exam.** That **big gap** is the alarm bell.
@end
@callout|yellow|This is the single most useful habit in ML: **always test on data the model never saw.** If practice score is great but test score is bad, you've overfit — you memorised instead of understood. Never trust a score measured on the same data you trained on.

@h2|The sweet spot in the middle
@image|images/58-ucurve.png|As a model gets more complex, its practice error keeps dropping — but its exam error dips then RISES. Too simple = underfit (left), too complex = overfit (right). The lowest exam error, in the middle, is the sweet spot.
There's a beautiful shape hiding here. As you make a model more and more complex:
@bullets
**Practice (train) error** keeps going **down** — a complex model can always memorise more.
**Exam (test) error** goes **down, then back UP** — it improves for a while, then complexity starts chasing noise and hurts.
That U-shape means: **too simple hurts (underfit), too complex hurts (overfit).**
@end
@callout|green|The goal is the **bottom of the U** — the sweet spot where exam error is lowest. Not too simple, not too complex. This single graph is the heart of machine learning: you're always hunting for that middle point where the model *understands* without *memorising.*

@h2|How to fix each one
@image|images/59-fixes.png|If underfitting: use a stronger model, add better features, or train longer. If overfitting: use a simpler model, get more data, or add regularization (a penalty on complexity).
Good news — once you know which problem you have, the cures are clear:
@bullets
**If UNDERFIT** (learns too little) → use a **stronger/more complex** model, add **better features** (more useful clues), or **train longer.** Give it more power.
**If OVERFIT** (memorises too much) → use a **simpler** model (limit tree depth, fewer features), get **more training data**, or add **regularization** — a penalty that discourages the model from getting too complex.
@end
@callout|yellow|**Regularization** is worth knowing by name: it's a gentle "keep it simple" penalty added during training, so the model isn't allowed to bend itself into a knot chasing noise. It's the most common cure for overfitting — you'll meet it everywhere (Ridge, Lasso, dropout in neural nets).

@h2|See it in code
@code
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# ALWAYS split: train to learn, test to check honestly
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier(max_depth=3)   # limit depth = fight overfit
model.fit(X_train, y_train)

print("practice score:", model.score(X_train, y_train))
print("exam score:    ", model.score(X_test,  y_test))
# if practice >> exam, you overfit -> lower max_depth or get more data
@end
@callout|yellow|`train_test_split` is the habit that saves you: learn on one part, check honestly on another. `max_depth=3` keeps the tree from memorising. Compare the two scores — a big gap means overfit. This tiny check is what separates real ML from fooling yourself.

@h2|Recap — the 20-second version
@bullets
Every model fails two ways: **underfit** (learns too little) or **overfit** (memorises too much).
The goal is **Student B** — understand the **signal**, ignore the **noise.**
Catch overfitting by the **gap**: great practice score but poor **exam (test)** score.
There's a **sweet spot** in the middle — not too simple, not too complex.
Fix underfit with **more power**; fix overfit with **simpler model, more data, or regularization.**
@end
@callout|teal|Next up — Video 16: Cross-Validation & the Bias-Variance Tradeoff. You now know overfitting exists — next we learn the professional way to measure it and reliably find that sweet spot every time. The tools the pros actually use. See you Day 16.
