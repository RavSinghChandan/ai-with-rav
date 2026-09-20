---
day: 6
topic: Hackathons
series: Hackathon Shorts
video: 6
title: Why your progress bar is lying
subtitle: Client timers vs real events
learn: The fake progress bar pattern | How to spot one in seconds | What a real one looks like | Why judges check this
---

@callout|yellow|In One Line: If your progress bar would still move with the backend switched off, it is an animation — not progress.

@h2|The pattern almost every demo has
A loop on the frontend:

@code
for each agent:
    show "running"
    wait 500ms
    show "done"
@end

It looks convincing. It is connected to nothing. Kill the server and the bar
still fills, all the way to 100%.

@image|images/img06-fake-vs-real.png|Left: a timer that ignores the backend. Right: each step reported by the server as it finishes.

@h2|Mine had two of them
My app ran a 500ms timer in the service **and** a separate 550ms timer moving the
canvas nodes. Neither touched the backend.

Meanwhile the real work took **34 milliseconds**. The bar was pure theatre in
both directions — too slow for the truth, entirely disconnected from it.

@h2|What honest progress looks like
The server streams each step as it actually completes. The bar moves because
something finished — and if the server dies, the bar stops. That is the tell.

@h2|But real work is too fast to watch
34ms of dictionary lookups is not a demo. So I kept a deliberate pace — and said
so on screen:

@callout|blue|"Step timing is scaled from measured API latency · ~28s against live ad platforms"

Shaped timing you disclose is honest. A timer you pass off as progress is not.

@callout|green|Next video: the last one — how to ship the honest version without making it boring.
