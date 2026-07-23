---
day: 1
topic: Machine Learning
video: 1
title: What is Machine Learning, really?
subtitle: What is Machine Learning, really?
learn: What Machine Learning really is | Old way vs ML way | How a machine learns from examples | You already use ML 20x a day
---

@callout|yellow|In One Line: Machine Learning is teaching a computer to learn patterns from examples — instead of you writing the rules by hand.

@h2|Start here: the chai stall
Picture **Ramesh**, who runs a chai stall outside a Mumbai station.
Nobody gave Ramesh a rulebook. But after 3 years, he *just knows:*
@bullets
Rainy evening + train delayed → **sell more chai, keep extra ginger**
Hot afternoon → **nimbu paani sells, chai doesn't**
Salary day (1st) → **everyone buys, stock up**
@end
Ramesh was never *programmed*. He **learned from thousands of days of examples.**
@callout|green|That is Machine Learning. A machine, like Ramesh, looking at thousands of past examples and figuring out the pattern **by itself** — so it can predict the future.

@h2|The big shift: old way vs ML way
This one picture is the entire reason ML exists:
@image|images/01-traditional-vs-ml.png|In normal coding YOU write the rules. In ML you give examples and the machine writes the rules itself.
@callout|green|The intuition: In normal coding, *you* are the smart one — you write every rule. In ML, you let the **machine become smart** by showing it examples.
**Why this is revolutionary:** some problems have too many rules to ever write by hand. How would you write if-else rules to spot a cat in a photo? Impossible. But show a machine 10,000 cat photos and it learns "cat-ness" on its own.

@h2|How learning actually happens
@image|images/02-how-learning-happens.png|Data → Training → Model → Prediction. The "model" is just the pattern it learned.

@h2|You already use ML 20 times a day
@table
When you…|ML is quietly working
Open YouTube → perfect next video|Learned your watch history
GPay/PhonePe flags a fraud txn|Learned what fraud looks like
Instagram reels know you too well|Learned your scroll patterns
Gmail auto-sorts spam|Learned from billions of emails
@end

@h2|The Math (technical — skip if non-technical, you lose nothing)
Every ML model learns a function f that maps input X to output y:
@code
        y  =  f(X)

   X = the inputs   (weather, time, crowd)  -> "features"
   y = the answer   (cups of chai sold)      -> "label"
   f = the pattern  (what the machine learns)-> the "model"
@end
Training = adjusting f to shrink the gap between its guess and the truth. That gap is the **loss**. All of training is: "make the loss smaller."

@h2|Try it — your first model in 6 lines
@code
from sklearn.linear_model import LinearRegression

X = [[15],[20],[25],[30],[35]]   # temperature
y = [200,170,140,110,80]         # cups sold

model = LinearRegression()
model.fit(X, y)                  # <- THIS is learning

print(model.predict([[18]]))     # 18C -> ~182 cups
@end
@image|images/03-chai-regression.png|Orange dots = data. Blue line = what the model learned. Green star = a new prediction.
@callout|yellow|model.fit(X, y) is the entire heart of Machine Learning. Everything in the next 29 days is a more powerful version of it.

@h2|Recap — the 20-second version
@bullets
ML = learning patterns from examples, not writing rules by hand.
Old way: you write rules. ML way: the machine finds the rules.
The learned pattern is called a model (y = f(X)).
You already use it 20× a day — YouTube, GPay, Instagram.
Training = making wrong guesses less wrong (shrinking the loss).
@end
@callout|teal|Next up — Video 2: The 3 Families of ML: Supervised, Unsupervised, Reinforcement. Just like a child learns 3 ways — see you Day 2.