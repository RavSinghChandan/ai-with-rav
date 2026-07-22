# 📏 The Rulebook — how every ML video PDF is made
> Rav's lifetime template. Follow this EVERY day without being asked. This is the standard.

## The goal
Each video = a `.md` file (renders on GitHub) **and** a `.pdf` (Rav teaches from it, annotates on screen in Preview). The PDF is what the audience sees. It must look **premium, dark, clean, and instantly understandable** — technical AND non-technical.

---

## 🖼 IMAGE RULE (added 2026-07-22, non-negotiable) — ONE IMAGE PER MAJOR SECTION
**Every major @h2 teaching section that explains a CONCEPT must have its own diagram.** Do NOT ship a PDF with only 2 images. Rav's words: "as many topics there are, that many images there should be." Target: a visual for EACH concept section (typically 4–6 images per video, not 2).
- Section explains an idea → it needs a diagram that shows that idea (not just text).
- The only sections that may skip an image: the "In One Line" callout, the recap, and pure code/story intros.
- Diagrams stay dark-themed (see below), generated into the topic's `images/` folder, VIEWED before pushing.
- When writing a new day: list the @h2 sections FIRST, then make sure each conceptual one has an `@image|...`. If a section has none, generate one.

---

## PDF LOOK — PREMIUM WARM (approved 2026-07-22, LOCKED). This is the LinkedIn-viral standard.
1. **WARM CHARCOAL-BROWN background** — `#1a1512` (cards `#241d18`). NOT black, NOT white. Premium, easy on eyes, "expensive notebook" feel. This replaced the old flat black.
2. **Cream text** — `#f0e6d8` (warm, not harsh white). Muted `#b3a595`.
3. **Accents:** saffron `#FF7A3D` (H1 topic), **gold `#E0B265` (H2 headers + day badge)**, teal `#4EC5E8`, green `#3dd4a8`, yellow `#FFCF6B`. Warm, premium, Indian-audience friendly.
4. **Images on the warm-dark background** — every diagram redrawn dark so it blends. No white rectangles.
5. **Code blocks** — `#140f0c` card, cream text. Crisp, selectable.

## BRANDING ON EVERY PAGE (LOCKED — makes it unmistakably Rav's, screenshot-proof)
- **Faint logo watermark** centered on EVERY page (`brand/logo-watermark.png`, ~7% opacity, 110mm). Subtle, never blocks text.
- **Small circular photo** bottom-right corner of every content page (15mm, gold ring).
- Footer: "AI with Rav · <Topic> in 30 Days · Day N" (NO links in footer body).

## THE COVER (page 1) — TOPIC-LED, sells what they'll LEARN (LOCKED)
Leads with the VALUE, not the photo. Layout top→bottom:
- Top strip: small logo (white card) + "AI with Rav / Learn AI the way you actually think" (left), small circular photo (right).
- Gold **"DAY N of 30"** badge.
- HUGE saffron **TOPIC** (e.g. "MACHINE LEARNING") + the day's specific title below in cream.
- **"WHAT YOU'LL LEARN TODAY"** card (teal accent bar) with 3–5 `›` bullets — from the `learn:` front-matter field (pipe-separated). THIS is the hook; viewer instantly sees the value.
- Footer: "youtube.com/@aiwithrav · A premium AI learning series".
- Photo is SECONDARY now — the topic + learn-list dominate. (Old cover was photo-centric; that's retired.)

### Content-file addition: the `learn:` front-matter field (required for cover)
```
learn: Features (X) vs Labels (y) | Garbage in, garbage out | Why more data beats a fancy model | Feature engineering
```
Pipe-separated, 3–5 short items = the "What you'll learn today" cover bullets.

## WHAT TO REMOVE from the PDF (clutter — cut every time)
- ❌ **Navigation links** — "Back to the map", "Watch on YouTube", any `[text](link)`. A PDF is not a webpage. Strip all markdown links → keep just the text.
- ❌ **Excess divider lines** — do NOT render every `---` as a line. Max 1 subtle divider between major sections, or none. No "wall of dashes".
- ❌ **Raw/broken emoji** — if an emoji won't render cleanly as a glyph, drop it. Never show `\ud83c...` mojibake or a tofu box. One clean emoji per heading MAX, only if it renders.
- ❌ **"Day X of 30 · ~7 min · links…" clutter line** — keep only a clean one-liner if useful (e.g. the "In One Line" summary), drop the rest.
- ❌ Anything that looks like a webpage artifact. The PDF should read like a designed slide deck / handout.

## WHAT TO KEEP
- ✅ The one-line summary ("In One Line: …") — that's a good hook, keep it.
- ✅ All teaching content, all images, all color-coded boxes (🟢 intuition / 🔵 math / 🟡 remember / 🔴 mistake) — but rendered as clean colored callout boxes, not raw emoji + text.
- ✅ Code blocks, tables, the recap.

## IMAGE RULES
- Dark background `#0d1117`, bright elements. Palette above.
- High DPI (150+), no overlapping boxes, titles ABOVE boxes with clear gaps.
- **ALWAYS view each generated image before pushing** — check alignment, no collisions, text fits. (Day 1 v1 had overlapping boxes; caught only by looking.)
- Every video's images live in `images/` with a matching `_generate_*.py` so the style is reproducible.

## PROCESS EVERY VIDEO (do all of this, unprompted)
1. Write/curate the `vNN-*.md` (story-first: Indian analogy → intuition → math → code → recap).
2. Generate images on DARK bg. **View each one.** Fix misalignments.
3. Run `make-pdf.py` → produces the dark, link-stripped, clean PDF.
4. **View 2–3 PDF pages** to confirm: black bg, no links, no broken emoji, images blend, text crisp.
5. Only then commit + push. Give Rav the PDF path + GitHub link. (Rav pushes final per his rule — but PDFs/images inside the ml-in-30-days repo Rav has said to just prepare; confirm before first push each session.)

## QUALITY BAR
> "This is my template that I share with my audience. My lifetime thing." — it must look like a product, not a text dump. If a page looks cluttered, cramped, or has a broken glyph, it's NOT done. Fix before showing.
