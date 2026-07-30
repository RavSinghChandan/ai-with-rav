---
day: 20
video: 20
topic: Machine Learning
title: Ensemble Methods — the wisdom of many models
subtitle: The trick behind almost every winning ML solution
learn: Why a panel beats one judge | Bagging (parallel — Random Forest) | Boosting (sequential — XGBoost) | Stacking (a head judge) | Why combining works so well
---

@callout|yellow|In One Line: One judge can have a bad day or a blind spot. A PANEL of judges voting together is far more reliable. An ensemble is exactly that — many models combined into one super-model. It's the secret behind almost every ML competition winner.

@h2|Start here: one judge vs a panel
Remember "Ask the Audience" on KBC? One random person might be wrong — but the *whole* audience voting nails the answer almost every time. You saw a hint of this back in Random Forest (Day 8): many okay trees beat one genius tree.
Today we make that idea general. Instead of trusting **one model**, we combine **many** models into a panel — an **ensemble** — and let them work together. This one trick is behind nearly every winning solution on Kaggle and in industry.

@h2|Why a panel beats one judge
@image|images/80-panel.png|One model is like a single judge — one bad day or blind spot and the answer is wrong. A panel of models votes together, so their individual mistakes cancel out and the group answer is far more reliable.
@bullets
**One model** = one judge. Smart, but it can have a blind spot or an off day → a wrong answer.
**A panel of models** = many judges, each a little different. They **vote**, and their random mistakes **cancel out.**
The group answer is more reliable than any single member.
@end
@callout|green|That's the whole idea of an ensemble: **don't bet everything on one model.** Combine several, and the crowd is almost always right. Now — there are three clever ways to run the panel. You already met two of them.

@h2|Bagging — a parallel panel
@image|images/81-bagging.png|Bagging: give each model a different random SAMPLE of the data, let them all work in parallel, then vote or average their answers. This is exactly what Random Forest does.
The first way: **bagging** (short for "bootstrap aggregating" — don't worry about the fancy name).
@bullets
Give each model a **different random sample** of the data.
They all train **in parallel** (side by side, independently).
Take a **vote** (for categories) or an **average** (for numbers).
@end
@callout|green|You've seen this already — **this is Random Forest** (Day 8)! Each tree sees different data, they vote, and the errors cancel. Bagging's superpower is cutting down **variance** (overconfidence, the swingy kind of error) — the panel is calmer and more stable than any single model.

@h2|Boosting — a sequential panel
@image|images/82-boosting.png|Boosting: models go one after another. Model 1 makes mistakes, model 2 studies and fixes those mistakes, model 3 fixes what's still left. Each learns from the last one's errors. This is XGBoost.
The second way: **boosting.** Here the judges don't work side by side — they go **one after another.**
@bullets
**Model 1** makes some mistakes.
**Model 2** studies *only those mistakes* and fixes them.
**Model 3** fixes whatever's still wrong. And so on.
@end
@callout|green|You've seen this too — **this is XGBoost** (Day 9)! Each model learns from the previous one's errors, building a sharp final answer step by step. Where bagging cuts *variance*, boosting cuts **bias** (it keeps chipping away at what the panel gets wrong). This is why boosting often wins competitions.

@h2|Stacking — a head judge
@image|images/83-stacking.png|Stacking: run several different specialist models (a tree, an SVM, a KNN), then a final "head judge" model learns how much to trust each specialist and combines them into the final answer.
The third way is the cleverest: **stacking.** Instead of a plain vote, you add a **head judge.**
@bullets
Run several **different** specialist models — say a tree, an SVM, and a KNN.
Then train a **final model** (the head judge) whose job is to learn **how much to trust each specialist.**
The head judge blends them into the final answer.
@end
@callout|yellow|The head judge learns things like "trust the tree for this kind of case, but the SVM for that kind." It's smarter than a simple vote because it **weighs** each model instead of treating them equally. Stacking is how top Kaggle teams squeeze out the last drops of accuracy.

@h2|Why does combining work so well?
@image|images/84-why.png|Five models, each getting a few DIFFERENT questions wrong. Because their mistakes don't line up, the majority vote is right on every single question. That's why the panel beats any individual.
Here's the beautiful reason it works, in one picture:
@bullets
Each model is good but **imperfect** — it gets a few questions wrong.
But if the models are **different**, they get *different* questions wrong.
So when they **vote**, the wrong answers scatter and get out-voted — while the right answer, which most agree on, wins every time.
@end
@callout|green|The key word is **different.** If all your models make the *same* mistake, voting doesn't help. Ensembles work when the members are **diverse** — different data (bagging), different focus (boosting), or different algorithms (stacking). Diversity is what makes the crowd wise.

@h2|Try it — a few lines
@code
from sklearn.ensemble import RandomForestClassifier      # bagging
from xgboost import XGBClassifier                          # boosting
from sklearn.ensemble import StackingClassifier            # stacking

bag   = RandomForestClassifier(n_estimators=100)           # a parallel panel
boost = XGBClassifier(n_estimators=200)                    # a sequential panel

stack = StackingClassifier(                                 # a head judge
    estimators=[("tree", bag), ("boost", boost)],
    final_estimator=LogisticRegression()
)
stack.fit(X_train, y_train)
@end
@callout|yellow|`RandomForestClassifier` is bagging, `XGBClassifier` is boosting, and `StackingClassifier` lets a final model combine them. You already know the first two from Days 8-9 — today you learned they're both examples of the *same* big idea: ensembles.

@h2|Recap — the 20-second version
@bullets
An **ensemble** = many models combined — a panel of judges beats one judge.
**Bagging** = parallel models on different samples, then vote → **Random Forest.**
**Boosting** = sequential models each fixing the last's mistakes → **XGBoost.**
**Stacking** = a head judge that learns how much to trust each specialist.
It works because **diverse** models make **different** mistakes that cancel out.
@end
@callout|teal|Next up — Video 21: Recommendation Systems. You've mastered the algorithms — now we start applying them. First up: how Netflix, Amazon, and Spotify seem to read your mind and know exactly what you'll like next. See you Day 21.
