---
day: 3
topic: Hackathons
series: Hackathon Shorts
video: 3
title: Your demo's numbers are probably fake
subtitle: The one-line check that proves it
learn: The test that takes ten seconds | What random() in a metric means | How I found it in my own app | The fix that costs nothing
---

@callout|yellow|In One Line: Run your demo twice with the same input. If the numbers move, they are noise — not results.

@h2|The ten-second test
Enter identical inputs. Run. Note the headline number. Run again.

Different answer? Nothing measured anything. Something called a random number
and dressed it as a result.

@image|images/img03-same-input.png|Identical input, two runs, two different answers. This is not a result — it is a dice roll.

@h2|I failed my own test
My app showed a confident **+6.2% improvement**.

I ran it twice. **+1.84x**, then **+0.55x**. Same campaign. Same budget. The
"improvement" was `random.uniform()` wobbling around a hardcoded table.

Worse: the learning loop was scored against that noise. It was optimising against
a dice roll and reporting the wins.

@h2|The fix is not "delete the randomness"
Variance is realistic — a model that returns one flat number for one input looks
fake in the other direction.

The fix is to **seed it from the input**:

@callout|blue|seed = hash(campaign type + product + budget + audience)

Same campaign, same seed, same numbers — every time. A real change to the input
is now the only thing that can move the result.

@h2|Why this matters more than your UI
A judge or an interviewer will ask where a number came from. "It varies" is not
an answer you can recover from.

@callout|green|Next video: the funnel step almost everyone skips — and the impossible economics it hides.
