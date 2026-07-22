---
day: 5
video: 5
topic: Machine Learning
title: Linear Regression — your first real algorithm
subtitle: Drawing the best line to predict a number
learn: What Linear Regression actually does | The y = mx + c formula, in plain English | What "best fit" means (minimising error) | Train one yourself in 5 lines of code
---

@callout|yellow|In One Line: Linear Regression draws the best straight line through your data — then uses that line to predict a number (price, sales, temperature) for anything new.

@h2|Start here: the property dealer
Ask any Mumbai property dealer the price of a 1,200 sq ft flat and they'll answer in seconds. How? Years of seeing flats: bigger → costlier. In their head, they've drawn a rough **line** between size and price.
Linear Regression is a machine doing exactly this — but with maths instead of gut feeling. It's the **simplest, most-used ML algorithm in the world**, and once you get it, every other algorithm makes more sense.

@h2|What it does: draw the best line
@image|images/12-best-fit-line.png|Each orange dot is a real house (size vs price). Linear Regression finds the one blue line that fits them best.
Give it examples — house size → price. It finds the single straight line that runs through the middle of your data. Then for a **new** size, you just read the price off the line.
@callout|green|Use it whenever you're predicting a NUMBER from inputs: house price, next month's sales, tomorrow's temperature, a student's marks. If the answer is a number → think Linear Regression first.

@h2|The formula: y = mx + c
@image|images/14-line-equation.png|Every straight line is just y = mx + c. Training finds the best m (slope) and c (starting point).
Remember school maths? A straight line is `y = mx + c`:
@bullets
**y** → what you predict (the price)
**m** → the slope: how much price rises per extra sq ft
**x** → the input (the size)
**c** → the starting value (base price when size = 0)
@end
@callout|green|"Training" a Linear Regression model = the machine searching for the best **m** and **c** so the line hugs your data as closely as possible. That's the whole magic — just finding two numbers.

@h2|What does "best" line mean?
@image|images/13-residuals.png|The yellow dashed lines are the errors — the gap between each real point and the line. Best line = smallest total error.
There are infinite lines you could draw. The "best" one is the line where the **total distance from the points to the line is smallest.** Each gap (point to line) is an **error** (a *residual*). Add up all the errors — the best line has the least.
@callout|green|This "minimise the total error" idea is the seed of ALL machine learning. Every model, even ChatGPT, is just minimising an error (a "loss") — Linear Regression is where you see it in its purest form.

@h2|Train one yourself — 5 lines
@code
from sklearn.linear_model import LinearRegression

X = [[500],[750],[1000],[1500],[2000]]   # house sizes
y = [25, 34, 41, 58, 76]                  # prices (lakhs)

model = LinearRegression()
model.fit(X, y)                           # finds best m and c

print(model.predict([[1200]]))            # new flat -> ~48 lakhs
print(model.coef_, model.intercept_)      # the learned m and c
@end
@callout|yellow|That's a real, working ML model in 5 lines. `model.coef_` is your **m**, `model.intercept_` is your **c** — the machine found them for you.

@h2|Recap — the 20-second version
@bullets
Linear Regression predicts a **number** by drawing the best straight line through data.
The line is `y = mx + c` — training just finds the best **m** and **c**.
"Best" line = the one with the **smallest total error** (residuals).
Minimising error is the core idea behind ALL of ML.
5 lines of code trains a real one.
@end
@callout|teal|Next up — Video 6: Logistic Regression. When the answer isn't a number but a YES/NO (spam or not? pass or fail?) — the spam-filter brain. See you Day 6.
