# SHIP BRIEF: v0.36.30, testimonials corrections and the 48/48 hairline sweep

**From:** Claude Code · **Date:** 2026-07-27 · **Filed late, and that is noted below.**

## What shipped

v0.36.30 is live on achologytest.com. Kain uploaded it; theme source and server
are byte-identical across all 58 files, verified after the fact.

**Testimonials page corrections** (Kain's, made 2026-07-27, previously built but
never uploaded):
- The opening paragraph darkened to body colour and released from its 60ch
  measure. It was grey and narrow, which made the page's opening line read as a
  stray caption.
- A section heading added above the question chooser, in the same treatment as
  the page's other section heading, so the page has one heading voice.
- The question numbers all set to one size, with colour carrying the selection
  instead of the hover swell: grey for unchosen, orange for the live question.
- Member count corrected from "Ten" to "Nine" in the page copy and in the SEO
  description. Nine is right; Kain confirmed. The page had said ten since it was
  built.

**Also in this version:** every section hairline swept to 48/48, three blocks
promoted to shared renderers in `shared-parts.php` with their CSS moved to
components.css, the site-wide icon registry, and all previews rebuilt to read
the real theme.

**The WordPress page itself** was created and published by Kain today, so
`/testimonials/` now exists and the four dead links to it (nav, footer, About)
resolve.

## The gate: FAILED, and this shipped anyway

`python3 css_gate.py` → **GATE FAILED on 8 files, 53 findings**, unchanged from
your S223 first run. Nothing in the backlog has been worked.

I am not pasting a PASS I do not have. Two versions went out today, v0.36.29 and
v0.36.30, and neither carried a gate result, because your note introducing the
rule sat unread in my inbox while they shipped. The rule was broken twice on the
day it was made. Recording it rather than quietly starting to comply from here.

From the next ship onward, no version leaves without the gate output in its
brief, PASS or otherwise.

## What I need from you on the backlog

Asked in full in `Reply__CSS_Gate_Backlog_And_Collapse_Brief_Acknowledged.md`
and repeated here in one line: **do the 53 findings fold into each page's pass
during the walk, or are they a separate authorised sweep?** Under the standing
instruction a sweep across 8 CSS files is exactly what is forbidden, so I have
touched none of them.

## Live verification

The testimonials page was checked rendered in a browser after upload: the
corrected copy, the darkened intro, the question chooser and the video pop-ups
all behave. `page_gate.py` has since been built and its first printout for a
policy page is filed separately.
