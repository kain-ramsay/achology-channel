> **CHAT DISPOSITION, S343: ARCHIVED.** The centred phone cover and the badge at the right end of the button row are written into DSRD 9 section 32.3 (the phone cover row and the tier table). The 256 cap it kept was opened to 320 one ship later. Card: Book note page template second look.

# RULING AND SHIP: v0.167.24, on a phone the book note hero centres the cover and the badge stands in the bottom right corner

**From:** Claude Code, Session 102. **Date:** 5 September 2026, late evening.
**Ruled by:** Kain, in the S102 sitting, typed, after reviewing the phone tier himself, straight after the tablet one.
**His words, quoted exactly as typed:** *"yes, the tablet looks better, but mobile isnt great - i think in mobile, the book image needs to be centralised within the container, and the badge dropped to the bottom rignt corner"*.
**His eye, given in the same message:** the tablet as built at v0.167.23 *"looks better"*.
**Filed under Harness Rule 14.** Theme commit `0d8286f`.
**Board card:** Knowledge Hub page designs.

## What changed, under 768 only

**The cover is centred in the column.** It keeps its 256 width (the phone cap it has carried since S086) and takes the column's spare width half each side: at 390 it sits at x 67 to 323 in the 350 column, 47 clear each side. The writing beneath it keeps the left edge. Every book note, badged or not, because the ruling is about the cover.

**The badge stands in the bottom right corner as the last member of the button row.** It is static, 88 square, pushed to the row's right edge by an auto margin, the Amazon button centred against it; its right edge is the grid's right edge and its foot is the grid's foot, which is the corner he named, and because it is in the row's flow rather than positioned over the grid, nothing can run under it, which is what stopped a positioned badge going into that corner at v0.167.19. It used to hang beside the cover's top at this width, and a centred cover leaves no room there. Where a note has two buttons they wrap onto two rows and the badge takes the right end of the last one.

Nothing changed at 768 and above: tablet as at v0.167.23, desktop as at v0.167.19.

**Measured on the deployed page.** At 390: cover 256 at x 67 to 323 (47 each side of the 350 column); badge 88 at x 282 to 370, its right edge 0 from the grid's right edge, its foot 0 from the grid's foot; the Amazon button at x 20 to 254, its centre on the badge's centre (difference 0); standfirst full width above the row; no horizontal overflow. At 768: two columns 256 and 384, badge static at 96 beside the button, unchanged. At 1440: badge absolute, 128, bottom right of the grid, unchanged. Stylesheet served at ver 0.167.24.

## Shipped

Theme v0.167.24, `deploy.py` three proofs passed: server identical to local, zip 700 files matching the theme, server reporting 0.167.24. Commit pushed. Opened in Safari for Kain as a new tab. **His eye on the phone as now built is not yet given.**

## Owed to the documents

DSRD 9 section 32.3's responsive rows for the hero: the phone tier's centred cover, and the badge's three states by width (desktop absolute bottom right at 128; tablet in the button row at 96; phone at the row's right end at 88). Yours, with the badge's earlier files.

OWED BACK: the section 32.3 responsive rows, yours. Nothing from Kain unless his eye says otherwise.

*No em or en dashes in this file; checked before writing.*
