---
day: 1
topic: Hackathons
series: Hackathon Shorts
video: 1
title: What a Razorpay hackathon actually asks you
subtitle: Razorpay × Replit AI Buildathon
learn: What the brief really was | The agent app I shipped | The one question that decides the winner | What I would do differently
---

@callout|yellow|In One Line: The demo does not win a hackathon. The five minutes of questions after the demo wins it.

@h2|The room
Razorpay and Replit ran an AI Buildathon at the PayPal office.
Build something with AI agents. Show it working. Then defend it.

I took **Agentic Growth OS** — five agents that plan an ad campaign end to end.
One picks the audience. One writes the copy. One splits the budget. One assembles
the campaign. One scores what came out.

@image|images/img01-five-agents.png|Five specialist agents, each doing one job, passing work down the line

@h2|The part nobody prepares for
Everyone can demo. The screen moves, the numbers appear, it looks alive.

Then a judge asks one question:

@callout|red|"Where did that number come from?"

That is the whole hackathon. Not the UI. Not the framework. That one question.

@h2|What I found in my own app
My app printed a confident **+6.2% improvement**.

I opened the code. The metric was `random.uniform()` against a hardcoded table.
Two identical runs gave **+1.84x** and then **+0.55x**. Same input. Different
answer. The improvement was noise wearing a percentage sign.

@h2|What I changed
I seeded the numbers from the campaign itself — same input, same output, every
time. I added the missing step in the funnel: a click becomes a *lead*, and only
some leads become sales. And I labelled the whole panel **Projected — simulation model v1**, with the formula one click away.

@callout|green|Honest and checkable beats impressive and vague. Every time.

@h2|The lesson
Judges are not testing your demo. They are testing whether you know what your own
system is doing.

If a number on your screen is a guess, say it is a guess — and show the formula.
That answer is stronger than any animation.

@callout|blue|Next video: the five-agent pattern, and when you should NOT use agents.
