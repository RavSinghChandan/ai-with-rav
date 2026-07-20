# 🏭 How to make any day's PDF (the factory)

**Design is frozen in `build_master_pdf.py`. You NEVER touch it.**
Each day is just a content file in `days/dayNN.md`.

## To make Day N:
1. Create `days/dayNN.md` (copy day01.md as a skeleton, change the content).
2. Generate any needed diagrams into `images/` (dark theme).
3. Run:  `python3 build_master_pdf.py days/dayNN.md`
4. Out comes `AI-with-Rav_Day-NN_<title>.pdf` — identical style, new content.

## Content file format (days/dayNN.md)
```
---
day: 2
video: 2
title: The 3 Families of Machine Learning
subtitle: Supervised, Unsupervised, Reinforcement
---

@callout|yellow|In One Line: ...text...
@h2|Section heading
Normal paragraph text. **bold becomes yellow**, *italic works*.
@bullets
first bullet
second bullet
@end
@image|images/xx.png|caption under the image
@table
Header A|Header B
row1a|row1b
@end
@code
raw code, spacing preserved
@end
```
That's it. **The cover (logo + photo + MACHINE LEARNING in 30 Days + DAY badge) is automatic** — it reads `day`, `video`, `title` from the front-matter.

## The rule
Rav says "generate Day N" → Claude writes `days/dayNN.md` (content + diagrams) → runs the one command → branded PDF appears. NO design work, NO python editing. Factory.
