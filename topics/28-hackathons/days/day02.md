---
day: 2
topic: Hackathons
series: Hackathon Shorts
video: 2
title: When you should NOT use AI agents
subtitle: The question to ask before you build
learn: What an agent actually is | The test that decides | Where agents genuinely help | Where they only add cost
---

@callout|yellow|In One Line: If the steps never change, you do not need an agent. You need a function.

@h2|The honest definition
An "agent" is a model that **decides what to do next**.

That is the whole thing. If your code always runs step 1, then 2, then 3 — that
is a pipeline. Calling it an agent does not make it one.

@image|images/img02-pipeline-vs-agent.png|Same five jobs. Left: fixed order. Right: the model chooses. Only the right one needs an agent.

@h2|The test
Ask one question about your build:

@callout|blue|"Could I draw the order of steps on paper before running it?"

If yes — it is a pipeline. Write the function. It will be faster, cheaper, and
you will be able to debug it.

If no, because the next step genuinely depends on what came back — that is where
an agent earns its cost.

@h2|My own app fails this test
Agentic Growth OS runs five agents in a fixed order, every single time. Audience,
copy, budget, campaign, score.

By the strict definition, that is a pipeline with LLM calls in it.

@callout|red|I said this out loud at the hackathon instead of hiding it. Naming your own limits reads as confidence, not weakness.

@h2|So when are agents worth it?
When the model must **choose**: which tool to call, whether the answer is good
enough yet, whether to retry differently.

That judgement is the product. Everything else is a for-loop with extra billing.

@callout|green|Next video: why the numbers in your demo are probably fake — and the one-line check that proves it.
