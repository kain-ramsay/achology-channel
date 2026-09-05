# RULING AND SHIP: v0.167.14, the book note hero and its breadcrumb sit on the 880 reading column

**From:** Claude Code, Session 102. **Date:** 5 September 2026, evening.
**Ruled by:** Kain, in the S102 sitting, in chat, on the rendered page he had open.
**His words, quoted exactly as typed:** *"ok, in the book note page hero, i think we should bring the breadcrumbs and all of the heros content into the same width of container that the rest of the page sits in. Does this make sense?"*
**Approved on the rendered page after the ship, his words:** *"yes, the hero looks much better like this claude"*.
**Filed under Harness Rule 14.** A theme edit made in a factory session on Kain's word, named in the theme commit `73caf2d`.
**Board card:** Knowledge Hub page designs.

## What changed, and what did not

One rule added to `book-note.css`: the hero's breadcrumb bar and the hero grid take `max-width: var(--container-article)` with `margin-inline: auto`, the same two declarations `.bn-read` already carries. The band and its wash stay full width; the picture, the title, the standfirst and the meta line now sit on the column the writing sits on. Nothing else in the hero moved: cover width, gap, type, spacing and the wash are as before.

**Measured on the deployed page, before and after, at 1440:** the breadcrumb and the grid sat at x 168, 1104 wide, while the reading column sat at x 280, 880 wide; now all three sit at x 280, 880 wide. At 1024 all three sit at x 72, 880 wide. At 768 and 390 the container is already narrower than 880, so nothing there moved (704 and 350). No horizontal overflow at any width. The title still wraps to two lines at 1440, now in a 560 column beside the 256 cover rather than 784.

## Shipped

Theme v0.167.14, `deploy.py` three proofs passed: server identical to local, zip 664 files matching the theme, server reporting 0.167.14. The page was read in the in-app browser at the four widths above and opened in Safari for Kain as a new tab.

## What is owed to the documents

DSRD 9 section 32.3's hero table records the grid inside the 1200 frame's 1104; it is now the 880 column, which section 32.2 already asserts for the page as a whole ("no exception, 880px like every other content page"). Yours, with this file as the ruling. The S102 morning comparison of section 32 against the built page (`REPORT__DSRD_9_Section_32_Read_Against_The_Built_Book_Note_Page_S102.md`) named the hero measurements among its disagreements; this ruling settles the width one.

OWED BACK: the section 32.3 row, yours.

*No em or en dashes in this file; checked before writing.*
