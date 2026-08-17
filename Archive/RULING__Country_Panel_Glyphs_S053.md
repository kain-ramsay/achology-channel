# RULING: the country panel gets the compass and the users glyph

**From:** Claude Code, Session 053. **Date:** 2026-08-11. **Theme:** v0.57.2, live on https://achologytest.com/reviews/

## What Kain ruled

He approved the Reviews page at tablet and phone, then raised the one thing that was unclear at every width, including the desktop he had already signed off:

> "The frosted box shows locations and student numbers... it's not necessarily clear what these numbers mean. So would it be worthwhile using the same icons that you've used in the numbers at the bottom of the blocks? The compass before the country, and then the people icon before the number. And that could probably be standard for all three responsiveness layers."

He is right, and the fix is the cheapest kind: the panel showed a place and a number with nothing saying what the number counted, and the answer was already elsewhere on the same block.

## What was built

The `compass` and `users` glyphs from DSRD 7 §5.2, one before each half of each of the five rows. 14px square, `rgba(255,255,255,0.55)`, `--sp-sm` gap, centred rather than baseline-aligned, `aria-hidden` because the aside already carries the label "Students by country, top five" and a screen reader would otherwise hear "compass" ten times. Identical at all three widths, per his ruling.

**They are deliberately the same two the four figures carry directly below the panel**, compass for countries and users for students. The block now teaches its own key: a reader meets the pair beside "United States, 202,893" and meets it again under 216 and 695,578. No new glyph enters the page.

The count's glyph takes the name's alpha rather than the count's white, so the two match each other across the row and the numbers stay the only bright thing in the panel.

Verified live: ten glyphs, every one 14 by 14, no row overflow and no page overflow at 1440, 800 or 375. The panel widens from 260 to 322 at desktop to hold them and stays 260 at tablet.

## What this means for the documents

**The page spec is already updated.** `SPEC__Reviews_Page_S053.md` §3 carries the full table and the reasoning, and `Reviews_Page_S053_APPROVED.html` has been regenerated from the live page, so the signed record shows what Kain actually approved rather than what it looked like an hour earlier.

**Nothing here changes the frozen figures.** His S052 ruling stands: the country names and their numbers are untouched.

**One thing for you.** This is a change to the global impact block, which DSRD 4 §14.2 says is built once and shared by three pages, so when it lands on the other two the glyphs travel with it. That sharpens the request already sitting with you from the gate run: **DSRD 8 needs to name this block as a component**, at which point these two glyphs belong in its entry rather than in one page's spec.

*No em or en dashes in this file; checked before writing.*
