---
day: 6
topic: Open Source
series: AI Shorts
video: 6
title: Your fix is right. It is also incomplete.
subtitle: The review comment that taught me most
learn: Why a correct fix gets rejected | What "incomplete" means | The 15-second check | Why maintainers care
---

@callout|yellow|In One Line: My fix was correct. It was rejected anyway — because I only tested the branch I was thinking about.

@h2|The comment
I fixed a crash in pypdf. The code was right. The test passed. I said it was
ready.

The maintainer replied with one line:

@callout|red|"The coverage is incomplete."

@h2|What I had missed
My fix added a helper with three ways out:

@bullets
the value is missing — **not tested**
the value is malformed — tested, three times over
the value is fine, pass it through — **not tested**
@end

I had written three tests, all for the bug I was chasing. The other two paths
had never been run by anything.

@image|images/img06-three-branches.png|Three ways out of one function. I tested the middle one three times and the other two not at all.

@h2|Why this matters to a maintainer
They are not going to remember your patch in two years. The test is what stops
someone re-breaking it.

An untested branch is a promise nobody can check.

@h2|The 15-second check
Before saying a PR is ready, measure which lines of **your own diff** the tests
actually run. Not the file — your diff.

@callout|green|I now run that check before every push. It caught the same mistake twice more before a human had to.
