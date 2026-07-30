---
day: 8
video: 8
topic: Python
title: Type Conversion & Errors — translating between box types
subtitle: Turn text into numbers (and back), and read Python's error messages calmly
learn: Converting = changing a value's type | The three converters int() float() str() | int() drops the decimal | Errors are helpful messages | The three errors you'll meet
---

@callout|yellow|In One Line: Values come in types — text, whole numbers, decimals. Often you need to translate between them (that pesky input() gives text!). Today you learn int(), float(), str() to convert safely — and how to read the error message Python shows when a type is wrong. This finishes Part 1.

@h2|Start here: types don't always match
You've hit this already — `input()` gives you **text**, but you often need a **number**. Or you have a number and want to glue it into a sentence (which needs text). Values have a **type**, and sometimes the type in your hand isn't the type you need. The fix is **conversion**: translate the value from one type to another.

@h2|Converting = changing the type
@image|images/36-convert.png|Converting translates a value into another type. The text "30" (str) becomes the number 30 (int) via int(...). The value stays the same — only its type changes, so you can now do maths with it.
Converting keeps the **value** but changes its **type** — the box's contents look the same, but now you can *use* them differently:
@code
text = "30"           # this is text (a string)
number = int(text)    # convert it to a whole number
print(number + 1)     # -> 31   (now maths works!)
@end
@callout|green|`int("30")` reads the text `"30"` and hands back the actual number `30`. The value didn't change — but its *type* did, so now `+ 1` works. This is exactly why we wrote `int(input(...))` on Day 5: input gives text, we convert it to a number.

@h2|The three everyday converters
@image|images/37-converters.png|Three converters: int() turns text/decimal into a whole number (int("30")->30, int(7.9)->7), float() turns text/int into a decimal (float("3.5")->3.5, float(7)->7.0), str() turns anything into text (str(30)->"30"). int() drops the decimal, it does not round.
Three functions do almost all the converting you'll ever need — each named after the type it makes:
@bullets
`int(x)` → make a **whole number**: `int("30")` → `30`.
`float(x)` → make a **decimal**: `float("3.5")` → `3.5`.
`str(x)` → make **text**: `str(30)` → `"30"`.
@end
@code
str(30)          # -> "30"     number to text (for messages)
float("3.5")     # -> 3.5      text to decimal
int("100")       # -> 100      text to whole number
@end
@callout|yellow|Notice the pattern: the function's name **is** the type you want. Need text? `str()`. Need a whole number? `int()`. This is how you fix the "can't add text and number" problem from Day 3 — convert first, then combine.

@h2|Watch out: int() drops the decimal
@image|images/39-common-errors.png|Three common errors and fixes: TypeError from "age " + 30 (mixing text and number, fix with str(30)), ValueError from int("hello") (converting text that isn't a number), NameError from print(scoree) (a typo in a variable name, fix the spelling).
One surprise worth calling out before we hit errors:
@code
print(int(7.9))      # -> 7    (NOT 8!)
@end
@callout|red|`int()` **chops off** the decimal part — it does **not** round. `int(7.9)` is `7`, not `8`. If you actually want rounding, use `round(7.9)` → `8`. Also: `int("hello")` will **error** — you can only convert text that *looks* like a number. `int("30")` works; `int("thirty")` does not.

@h2|Errors are helpful messages, not disasters
@image|images/38-error.png|An error is a helpful message. "age " + 30 gives a TypeError: can only concatenate str to str. The error names the TYPE of problem and what went wrong. Read the last line first — it names the problem. Fix: str(30).
Every coder — even experts — sees errors constantly. An error isn't Python scolding you; it's Python **telling you exactly what went wrong** so you can fix it:
@code
print("age " + 30)
# TypeError: can only concatenate str (not "int") to str
@end
@callout|green|Don't panic at the red text — **read it.** The **last line** names the problem: `TypeError` (a type mismatch) and the detail "can only add str to str" — meaning you tried to glue text and a number. The fix is right there: convert the number first with `str(30)`, or just use commas in `print`. Errors are clues, not failure.

@h2|The three errors you'll meet
Ninety percent of your early errors are one of these three — learn to recognise them and you'll fix them in seconds:
@bullets
**TypeError** → wrong *types* together, like `"age " + 30`. Fix: convert (`str(30)`) or use commas.
**ValueError** → converting text that isn't a valid number, like `int("hello")`. Fix: check the text.
**NameError** → a **typo** in a variable name, like `print(scoree)`. Fix: correct the spelling.
@end
@callout|yellow|Make a habit: when you see red, **read the last line, spot which of these it is, and the fix usually follows.** Errors feel scary on Day 8 and boring by Day 30 — because you'll have read hundreds and know they're just Python pointing at the exact line to fix. That calm is what separates a beginner from an engineer.

@h2|Part 1 complete — the foundation is laid
@image|images/40-part1-map.png|Part 1 complete: Days 1-8 all done — Why Python, Variables, Strings, Numbers, Input/Output, Booleans, If/Elif/Else, Convert & Errors. You can now store data, do maths, talk to the user, and make decisions. Next in Part 2: Collections (lists and dictionaries) and Loops.
@callout|green|Take a breath — you just finished the **entire foundation** of Python. In eight days you learned to store data, work with text and numbers, talk to the user, make decisions, and handle errors. That's genuinely enough to write small, useful programs. Everything from here builds on these blocks.

@h2|Recap — the 20-second version
@bullets
**Converting** changes a value's **type** (not its value): text ↔ number.
`int()` → whole number, `float()` → decimal, `str()` → text.
`int()` **drops** the decimal (doesn't round); only converts text that looks numeric.
An **error** is Python telling you what's wrong — read the **last line** first.
The big three: **TypeError** (wrong types), **ValueError** (bad conversion), **NameError** (typo).
@end
@callout|teal|Next up — Part 2 begins with Video 9: Lists. So far each variable held ONE value. But real data comes in groups — a class of students, a shopping cart, a month of temperatures. Next we learn Lists: one box that holds many values in order. This is where Python gets powerful. See you tomorrow.
