---
day: 3
topic: Open Source
series: AI Shorts
video: 3
title: I opened 35 PRs. Two merged.
subtitle: What the 33 had in common
learn: Why volume is the wrong strategy | The question maintainers ask | What the two winners had | How to pick your first PR
---

@callout|yellow|In One Line: I sent 35 documentation pull requests. Two merged. The other 33 all failed the same test.

@h2|The strategy that felt smart
Find functions with no docstring. Write one. Open a PR. Repeat 35 times across
several libraries.

Pure volume. Surely some would land?

Two did.

@image|images/img03-35-prs.png|33 described what the code already said. 2 answered something the reader could not see.

@h2|What the 33 had in common
They described what the code **already said**:

@code
def get_name(self):
    """Get the name."""
@end

A reviewer reads that and thinks: *the function is called get_name. You have
added nothing and given me something to maintain.*

@h2|What the two that merged did
They answered a question the reader could **not** see from the signature — the
units, the edge case, the thing that surprises you at 2am.

@callout|blue|joblib #1811 documented what format_time actually returns and when the short form kicks in. You cannot get that from the name.

@h2|The test before you open a PR
Read your own description and ask:

@callout|red|"Could a reader work this out from the function name alone?"

If yes, do not send it. If no — you have something worth a maintainer's time.

@callout|green|One PR that answers a real question beats thirty that restate the obvious.
