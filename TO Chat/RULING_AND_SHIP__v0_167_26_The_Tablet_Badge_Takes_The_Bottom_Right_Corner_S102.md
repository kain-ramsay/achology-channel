> **CHAT DISPOSITION, S343: ARCHIVED.** The tablet badge in the container's bottom right corner is written into DSRD 9 section 32.3's tier table, superseding v0.167.23's reading. This is the version Kain approved the whole hero at. Card: Book note page template second look.

# RULING AND SHIP: v0.167.26, on a tablet the badge stands in the container's bottom right corner

**From:** Claude Code, Session 102. **Date:** 5 September 2026, late evening.
**Ruled by:** Kain, in the S102 sitting, typed, on seeing the tablet badge sitting beside the Amazon button (v0.167.23).
**His words, quoted exactly as typed:** *"on tablet view, the badge need to sit in the bottom right hand corner of the container too"*.
**Filed under Harness Rule 14.** Theme commit `59bdc50`.
**Board card:** Knowledge Hub page designs.

## What changed, between 768 and 1023 only

The badge is still the button row's last member, static at 96 square with the button centred against it, but it is now pushed to the row's right edge by an auto margin, the same placement the phone tier has carried since v0.167.24. Its right edge is the container's right edge and its foot is the row's foot, which is the grid's foot whenever the writing is the taller column (at 768 it is; at 1023 the cover is 4px taller and the badge sits 2px above the grid's foot). It stays in the row's flow rather than being positioned over the grid, because the standfirst runs the whole 384 column at this width and a positioned badge would sit on its last lines; in the flow, nothing can run under it. The v0.167.23 reading of "adjacent to the amazon CTA button" (badge immediately right of the button) is superseded by this.

Nothing changed at 1024 and above or under 768.

**Measured on the deployed page.** At 768: badge 96 at x 640 to 736, its right edge 0 from the grid's right edge, its foot 0 from the grid's foot, the button's centre on the badge's centre (difference 0), no horizontal overflow. At 1023: right edge 0 from the grid's, foot 2px above it. At 390: unchanged, badge 88 in the same corner, cover 320. Stylesheet served at ver 0.167.26.

## Shipped

Theme v0.167.26, `deploy.py` three proofs passed: server identical to local, zip 700 files matching the theme, server reporting 0.167.26. Commit pushed. Opened in Safari for Kain as a new tab. **His eye on the tablet as now built is not yet given.**

## Owed to the documents

DSRD 9 section 32.3's responsive rows for the badge: desktop absolute in the grid's bottom right at 128; tablet and phone the button row's last member at the row's right edge, 96 and 88. Yours, with the badge's earlier files.

OWED BACK: the section 32.3 rows, yours. Nothing from Kain unless his eye says otherwise.

*No em or en dashes in this file; checked before writing.*
