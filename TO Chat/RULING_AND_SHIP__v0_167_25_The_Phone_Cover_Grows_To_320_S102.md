# RULING AND SHIP: v0.167.25, the book note cover grows to 320 wide on a phone

**From:** Claude Code, Session 102. **Date:** 5 September 2026, late evening.
**Ruled by:** Kain, in the S102 sitting, typed, on seeing the centred 256 cover of v0.167.24 on the phone tier.
**His words, quoted exactly as typed:** *"i think the snap between tablet and mobile could enlargen the book image to make better use of the space surrounding it?"*
**Filed under Harness Rule 14.** Theme commit `2442347`.
**Board card:** Knowledge Hub page designs.

## What changed, under 768 only

The cover's phone cap opens from 256 to 320. The 256 cap was the S086 guard against the cover taking the whole single column (at 390 that drew 350 by 525 and ran the hero to 1146); Kain has now looked at the centred 256 and asked for more of the space to be used, so the cap is 320: at 390 the cover is 320 by 480, centred, 15 clear each side of the 350 column; on a narrower phone it is the column's width; the 2:3 ratio holds. The writing beneath it keeps the left edge, and the badge stays at the right end of the button row as at v0.167.24. Nothing changed at 768 and above (tablet cover 256 beside the writing, desktop unchanged).

**Measured on the deployed page at 390:** cover 320 by 480 at x 35 to 355 (15 each side); the badge's foot still on the grid's foot; the hero 96 taller than at v0.167.24, the height the taller cover needs and no more; no horizontal overflow. At 768: two columns, cover 256, unchanged. Stylesheet served at ver 0.167.25.

## Shipped

Theme v0.167.25, `deploy.py` three proofs passed: server identical to local, zip 700 files matching the theme, server reporting 0.167.25. Commit pushed. Opened in Safari for Kain as a new tab. **His eye on the larger cover is not yet given.**

## One thing named, not acted on

The hero serves each cover at its uploaded size, and the uploaded covers are small: this page's file is 316 pixels wide, so at 320 on a phone it shows at its natural size and on a retina screen it is soft, as it already was at 256 on desktop (512 device pixels from 316). The covers never went through the pipeline's book-cover slot (DSRD 7 section 12.3; the media gate reads `the-power-of-truth-1.jpg` at 685KB against the slot's 60KB, so the set runs from too small to too large). That is a cover-run pass for the factory, the same shape as tonight's instructor pictures, and not a theme edit; named here so the larger phone cover is not read as the cause of the softness.

## Owed to the documents

DSRD 9 section 32.3's phone row for the cover: 320, centred, 2:3, the S086 256 guard superseded on this word. Yours.

OWED BACK: the section 32.3 phone row, yours. Nothing from Kain unless his eye says otherwise.

*No em or en dashes in this file; checked before writing.*
