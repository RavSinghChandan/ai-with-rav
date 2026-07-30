---
day: 18
video: 18
topic: Machine Learning
title: The ML Project Workflow — from raw data to real users
subtitle: The 6-stage journey that actually happens on the job
learn: The 6 stages, in order | Why 80% of the work is cleaning data | Where this month's lessons fit | What "deploy" really means | Why a model is never truly "done"
---

@callout|yellow|In One Line: A great meal isn't just cooking — it's deciding the dish, buying and cleaning ingredients, prepping, cooking, serving, and keeping it fresh. A real ML project is the same 6-step journey. The algorithm is just the "cooking" part.

@h2|Start here: an algorithm is not a project
You've spent this whole month learning algorithms, tuning, and metrics. But here's the truth that surprises every beginner: **the algorithm is only a small slice of a real ML project.** On the job, no one hands you clean data and says "just pick a model." You own the *entire journey* — from a fuzzy business question all the way to a model serving real users, and keeping it working for months.
Think of it like **cooking a great thali.** You don't just throw everything in a pot. There's a proper order, and skipping any step ruins the meal — no matter how good your recipe.

@h2|The 6-stage journey
@image|images/70-workflow.png|The full ML project, like cooking a meal in order: 1) Define the dish (the question), 2) buy + clean ingredients (data), 3) prep + cut (features), 4) cook + taste-test (train), 5) serve to guests (deploy), 6) keep it fresh (monitor + retrain).
Every real ML project follows the same six stages, in order:
@bullets
**1. Define** → decide the dish. What exact question are we answering, and how will we know it worked?
**2. Data** → buy and clean the ingredients. Collect the data, then wash it (fix errors, missing values, duplicates).
**3. Features** → prep and cut. Turn raw data into useful clues the model can eat (this is feature engineering).
**4. Train + taste** → cook and taste-test. Train models, tune them, check the metrics.
**5. Deploy** → serve it to guests. Put the model where it can actually help real people.
**6. Monitor** → keep it fresh. Watch it, and re-cook (retrain) when it goes stale.
@end
@callout|green|Notice the order matters. You can't cook before you buy ingredients; you can't serve before you cook. Skip a step — serve raw or unwashed food — and the whole meal fails, however brilliant your recipe. The same is true for ML.

@h2|The big surprise: 80% is cleaning
@image|images/71-80percent.png|A pie of where the time actually goes: about 80% is collecting and CLEANING data, only ~20% is the "fun" modelling part everyone imagines.
Beginners think ML is all clever models. The reality on the job is almost the opposite:
@bullets
About **80%** of your time goes to **collecting and cleaning data** — fixing typos, filling gaps, removing duplicates, fixing wrong labels.
Only about **20%** is the "fun" modelling everyone dreams about.
@end
@callout|red|This is the honest truth no course tells beginners: **most ML work is boring data cleaning, not fancy algorithms.** But it's also the *most important* work — a brilliant model on dirty data gives garbage (garbage in, garbage out). The engineers who patiently clean data are the ones whose models actually work.

@h2|Where this month's lessons fit
@image|images/72-lessons-fit.png|Everything you learned this month — the algorithms (Days 5-13), tuning and the sweet spot (Days 15-16), precision/recall/F1 (Day 17) — all fits inside just ONE stage: "Train + taste". A real engineer owns all six stages.
Here's a humbling picture. Everything you've learned so far:
@bullets
The **algorithms** (Days 5-13), the **tuning** (Days 15-16), the **metrics** (Day 17)…
…all fit inside **just ONE** of the six stages — "Train + taste."
@end
@callout|yellow|So the month gave you a powerful toolbox — but it's the toolbox for *one* stage. A real ML engineer owns **all six**: framing the problem, wrangling the data, engineering features, training, deploying, and monitoring. That bigger view is what today adds — and it's what makes you employable.

@h2|What "deploy" really means
@image|images/73-deploy.png|Deploy means moving the trained model off your laptop onto a server (an API) that's always on, so real users — through an app or phone — can get answers from it.
A model sitting in a notebook on your laptop helps **no one.** Deploying means putting it somewhere it can actually work:
@bullets
Take the **trained model** off your laptop.
Put it on a **server** (usually wrapped in an "API") that's always on and answers requests.
Now **real users** — through an app or website — send their data and get the model's answer back instantly.
@end
@callout|green|This is the moment ML becomes real: your model goes from a science project to something that helps people every day — approving loans, catching fraud, recommending videos. Learning to deploy (even a simple API) is what turns a student into an engineer.

@h2|Why it's never truly "done"
@image|images/74-loop.png|The ML lifecycle is a loop: deploy → monitor → the world changes and data drifts → retrain → deploy again. A model is never finished; it's maintained.
Here's the final twist most people miss: **shipping a model is not the end.** The world keeps changing, and a model trained on last year's data slowly gets worse. This is called **data drift.**
@bullets
**Deploy** the model.
**Monitor** it — is it still accurate on today's real data?
The world changes → **data drifts** → the model's answers get stale.
**Retrain** on fresh data → deploy again → and the loop continues.
@end
@callout|yellow|A real ML system is a **loop, not a finish line.** Spam changes, fashion changes, prices change — so models must be watched and refreshed. "Ship it and forget it" is how models quietly rot. The pros build the retraining loop from day one.

@h2|The workflow in code (the shape of it)
@code
# 1-3: define, load, clean, and engineer features
df = load_and_clean(raw_data)          # ~80% of the real effort
X, y = make_features(df)

# 4: train + taste (everything you learned this month)
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = best_model_from_gridsearch(X_train, y_train)
print(evaluate(model, X_test, y_test))  # precision, recall, F1

# 5: deploy — wrap it so real users can call it
save_model(model, "model.pkl")          # then serve behind an API

# 6: monitor + retrain on a schedule (the loop)
if performance_dropped():
    retrain_on_fresh_data()
@end
@callout|yellow|See the shape: clean → feature → train → evaluate → deploy → monitor. Days 5-17 lived in the middle two lines; a real project is all six. Knowing the whole shape is what makes you a complete ML engineer, not just a model-fitter.

@h2|Recap — the 20-second version
@bullets
An ML project is a **6-stage journey**: define → data → features → train → deploy → monitor.
About **80%** of real work is **cleaning data**, not fancy modelling.
Everything you learned this month fits in **one** stage ("train + taste").
**Deploy** = move the model off your laptop so real users can use it.
It's a **loop, not a finish line** — models drift, so you monitor and retrain.
@end
@callout|teal|Next up — Video 19: Feature Engineering — the secret weapon. We said prepping ingredients matters most. Next we go deep on the single skill that separates good ML engineers from great ones: turning raw data into features that make even a simple model shine. See you Day 19.
