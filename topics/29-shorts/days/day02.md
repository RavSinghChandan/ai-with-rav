---
day: 2
topic: Python
series: AI Shorts
video: 2
title: The Python trap that breaks quietly
subtitle: Mutable default arguments
learn: The bug that hides for months | Why Python behaves this way | The one-line fix | How to spot it in review
---

@callout|yellow|In One Line: A default list in a Python function is created ONCE — not every time you call it.

@h2|The code that looks fine
@code
def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("apple"))    # ['apple']        looks right
print(add_item("banana"))   # ['apple', 'banana']   what?
@end

The second call had nothing to do with the first. Yet the apple is still there.

@image|images/img02-mutable-default.png|The default list is created once, when the function is defined — every call shares that same list

@h2|Why this happens
Python builds the default value **when it reads the `def` line** — once, at
import time. Not on each call.

So every call that does not pass a basket shares the *same* list. Forever. One
basket for the whole programme.

@h2|The fix is one line
@code
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
@end

`None` is immutable, so there is nothing to accumulate. A fresh list is made on
every call that needs one.

@callout|red|This bites hardest in long-running services. Locally it looks fine; in production the list grows for days.

@callout|green|Rule: never put a list, dict or set in a default argument. Use None and build it inside.
