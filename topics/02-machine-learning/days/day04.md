---
day: 4
video: 4
topic: Machine Learning
title: Data — the fuel of Machine Learning
subtitle: Features, labels, and why data beats fancy algorithms
---

@callout|yellow|In One Line: Data is the fuel of ML. The inputs are called features (X), the answer is the label (y). Better data beats a smarter algorithm — every time.

@h2|Start here: a chef and their ingredients
Give a 5-star chef rotten vegetables — the dish will be terrible. Give an average cook fresh, quality ingredients — the dish will be good.
In Machine Learning, **the data is the ingredients** and **the algorithm is the chef.** Everyone obsesses over fancy algorithms. But the pros know a secret: **great data with a simple model beats messy data with a genius model.** Data is where you win.

@h2|What a dataset actually looks like
@image|images/08-features-vs-label.png|Every row is one example. The input columns are features (X); the one answer column is the label (y).
Two words you'll hear a thousand times — learn them now:
@bullets
**Features (X)** → the *inputs*, the clues the machine looks at. (Temperature, day, festival.)
**Label (y)** → the *answer* you want it to predict. (Cups of chai sold.)
@end
@callout|green|Simple test: "What am I trying to predict?" → that's your **label**. "What clues help me predict it?" → those are your **features**. Every supervised ML problem is just: features → label.

@h2|Garbage in, garbage out
@image|images/09-garbage-in-out.png|The same model gives useless predictions if the data going in is messy. No algorithm can fix bad data.
Real-world data is *always* messy:
@bullets
**Missing values** → some days the temperature wasn't recorded
**Wrong units** → some prices in rupees, some in lakhs
**Typos & duplicates** → "Mumbai", "mumbai", "Bombay" all mean the same city
**Outliers** → one day sold 50,000 cups (a wedding order) — misleads the model
@end
@callout|red|This is why ML engineers spend ~80% of their time cleaning data, not tuning models. It's unglamorous, but it's where accuracy is actually won or lost.

@h2|More data usually beats a cleverer model
@image|images/10-more-data.png|A simple model fed lots of good data (blue) catches up to and beats a fancy model with little data.
A famous result in ML: throw *more good examples* at a simple model and it often beats a complex model with little data. Why? Because the model learns the pattern from examples — more examples = a clearer pattern.
@bullets
100 chai-sales days → the model has a rough idea
5,000 days → it now understands weekends, festivals, weather, salary days
@end
@callout|green|Rule of thumb: before reaching for a fancier algorithm, first ask — "can I get more data, or cleaner data?" That usually helps more.

@h2|Good features = the real magic
@image|images/11-feature-engineering.png|A raw date is useless to the model. Engineer it into clues (is_weekend, is_salary_day, month) and now it can learn.
Sometimes the raw data isn't enough — you *create* better features. This is called **feature engineering** (a whole video later).
@bullets
Raw: a date "2026-07-22" → useless to the model as-is
Engineered: "is_weekend = No", "is_salary_day = No", "month = July" → now the model can learn patterns!
@end
@callout|green|Same data, smarter features = a much better model. This is where experienced ML engineers quietly win.

@h2|Recap — the 20-second version
@bullets
Data is the fuel; the algorithm is just the engine.
**Features (X)** = the inputs/clues. **Label (y)** = the answer to predict.
**Garbage in, garbage out** — no model fixes bad data (80% of the job is cleaning).
More good data often beats a fancier algorithm.
Smart **features** (feature engineering) is where the real magic happens.
@end
@callout|teal|Next up — Video 5: Linear Regression — your first real algorithm. Drawing the best line through your data to predict a number. See you Day 5.
