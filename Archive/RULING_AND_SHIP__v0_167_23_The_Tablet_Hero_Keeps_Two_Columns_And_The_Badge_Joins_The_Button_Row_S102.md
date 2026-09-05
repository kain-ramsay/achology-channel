> **CHAT DISPOSITION, S343: ARCHIVED.** The two columns holding to 768 is written into DSRD 9 section 32.3's grid row; its badge placement beside the button is superseded three hours later by v0.167.26 and the tier table carries the later one. Card: Book note page template second look.

# RULING AND SHIP: v0.167.23, the book note hero keeps its two columns on a tablet, and the badge sits beside the Amazon button there

**From:** Claude Code, Session 102. **Date:** 5 September 2026, late evening.
**Ruled by:** Kain, in the S102 sitting, typed, after reviewing the tablet tier of the page himself.
**His words, quoted exactly as typed:** *"Claude, the badge at the bottom of the book note article is great - but, i've just reviewed the tablet view, and the hero isn't doing too well on that layer of responsiveness. I think on tablet, you could snap all of the text to sit next to the book image, and just sit the badge in the bottom left corner adjacent to the amazon CTA button"*.
**His eye, given in the same message:** the last section's badge (v0.167.22) is *"great"*.
**Filed under Harness Rule 14.** Theme commit `ebda8a2`.
**Board card:** Knowledge Hub page designs.

## What changed

**The two columns hold down to 768.** The hero grid used to fall to one column (cover above, writing below) at 1023 and under; that fall now happens at 767 and under, the phone tier, and between 768 and 1023 the cover stands on the left with the whole text stack beside it, as on desktop. At 768 the writing's column beside the 256 cover is 384 wide; at 1023 it is 560, the same as desktop.

**The badge on a tablet is a member of the button row.** Its markup moved from before the cover into the button row, after the Amazon button, so that between 768 and 1023 it is simply the next item in that row: static, 96 square, the row's own 16 gap between the button and it, the row's items centred on each other so the button sits mid-height against the badge. That is his "bottom left corner adjacent to the amazon CTA button": the badge sits at the foot of the text column, immediately to the right of the button. On desktop (1024 and up) the badge is positioned against the grid from that row exactly as at v0.167.19, bottom right corner, 128, with the 42ch standfirst cap and the row's 152 clearance; on a phone it is positioned against the grid at 88 beside the cover's top exactly as before. Nothing else in the hero moved at any width.

**Measured on the deployed page.** At 768: grid columns 256 and 384; cover at x 32 to 288, stack at x 352 to 736; title three lines at the 33 step; badge 96 at x 602 to 698, 16 after the button's right edge (586), the button's centre on the badge's centre (difference 0); the grid 478 tall, the cover centred in it; no horizontal overflow. At 1023: columns 256 and 560, badge static beside the button, 16 after it. At 1024: the desktop badge, absolute, 128, at the grid's bottom right, unchanged. At 390: one column, the badge absolute at 88 beside the cover's top, 6px clear of it, unchanged. Stylesheet served at ver 0.167.23.

## Shipped

Theme v0.167.23, `deploy.py` three proofs passed: server identical to local, zip 700 files matching the theme, server reporting 0.167.23. Commit pushed. Opened in Safari for Kain as a new tab. **His eye on the tablet as now built is not yet given:** his word was the instruction; this file records the ship.

## Owed to the documents

DSRD 9 section 32.3's responsive notes for the hero (where the grid falls to one column, now 767) and the badge row (tablet: static in the button row, 96, centred). Yours, with the v0.167.18, v0.167.19 and v0.167.22 files as the badge's record.

OWED BACK: the section 32.3 responsive rows, yours. Nothing from Kain unless his eye says otherwise.

*No em or en dashes in this file; checked before writing.*
