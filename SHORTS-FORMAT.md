# The shorts format

The channel moved from 12-minute lessons to **sub-3-minute reels**. The
playlists did not change — one folder still equals one YouTube playlist. Only
the content format changed.

## What a short is

Two landscape pages. That is the whole deliverable.

| Page | Holds | You show it for |
|---|---|---|
| 1 | **one diagram**, nothing else competing | ~60 seconds |
| 2 | hook, three beats, one takeaway | ~60–90 seconds |

One diagram per short. Never two.

## Why light, not the dark premium deck

The 30-day deck is warm charcoal, built to look premium on a desk. A reel is
judged in the **first second on a bright phone**. Dark frames lose contrast
outdoors, and "premium" is not the decision a viewer is making — "is this
instantly clear?" is.

So shorts are white, with the brand colours sampled from the logo itself:

| | |
|---|---|
| cyan `#00B8FC` | the `< >` brackets |
| gold `#F6BB63` | the halo |
| navy `#14213D` | the wordmark |

Landscape A4 also matches the 16:9 frame you record in, so the PDF fills the
screen with no letterboxing.

## Writing one

`topics/<topic>/shorts/sNN.md`:

```
---
topic: Machine Learning
short: 1
title: Overfitting, in 90 seconds
---

@hook|The one line that has to land in the first second.

@image|images/short01-thing.png|Caption under the diagram

@beat|First beat. Keep it to one idea.
@beat|Second beat.
@beat|Third beat.

@takeaway|The one sentence they should still have tomorrow.
```

`**bold**` renders in brand cyan. Three beats maximum — a fourth will not fit
in the time.

## Building

```bash
python3.12 build_short_pdf.py topics/<topic>/shorts/s01.md
```

Diagrams use the light palette in `tools/short_style.py`. Generate all of them
with `python3.12 tools/make_shorts.py`.

## The 30-day factory is untouched

`build_master_pdf.py` and every existing `days/` file still work exactly as
before. The two formats live side by side — nothing was converted or deleted.
