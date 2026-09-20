---
day: 7
topic: Hackathons
series: Hackathon Shorts
video: 7
title: Ship the honest version
subtitle: Labels beat polish
learn: Why honesty wins the Q&A | The label that saves you | What to document | The one-line test before you demo
---

@callout|yellow|In One Line: You do not need real data to win. You need to be exactly clear about what your data is.

@h2|The fear, and why it is wrong
Everyone worries that admitting "this is simulated" kills the demo.

It does the opposite. Unlabelled numbers invite the question *"is this real?"* —
and once that question is in the room, nothing you say afterwards lands.

A label answers it before it is asked.

@image|images/img07-labelled.png|Same dashboard. One invites the question; the other has already answered it.

@h2|What I put on the screen
One strip above every result:

@bullets
**Projected — simulation model v1** — what kind of number this is
**Deterministic — same input, same output** — it is checkable
**Ad copy: template library** — which part is real, which is not
**Show formula** — a click reveals the actual maths
@end

@h2|What I wrote down
A `MODEL.md` with a table: orchestration real, learning loop real,
**performance metrics simulated**, ad platform not implemented.
Plus the formula, the assumptions, and a "known limits" section I wrote myself.

@callout|blue|Writing your own limits section is the strongest move available. Nobody can expose what you already published.

@h2|The test before you demo
Point at the biggest number on your screen and finish this sentence out loud:

@callout|red|"That number comes from ___, and I can show you the line of code."

If you cannot finish it, fix that before you touch the CSS.

@callout|green|That is the playlist. Build the thing, then be the person who knows exactly what it does.
