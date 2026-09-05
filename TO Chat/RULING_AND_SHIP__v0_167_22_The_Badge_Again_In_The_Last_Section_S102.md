# RULING AND SHIP: v0.167.22, the Essential Reading badge once more, at the head of "What are Your Next Learning Steps?"

**From:** Claude Code, Session 102. **Date:** 5 September 2026, late evening.
**Ruled by:** Kain, in the S102 sitting, typed, with a screenshot of the section on the rendered page; his final suggestion of the evening.
**His words, quoted exactly as typed:** *"OK, and here my final suggestion - we also place the badge up against the right side of the container in the final section 'What are Your Next Learning Steps?' - and just aligl the top of the badge with the top of the top line of text"*.
**Filed under Harness Rule 14.** Theme commit `bf0cc12`.
**Board card:** Knowledge Hub page designs.

## What changed

In `single-book_note.php`, on an Essential Reading note, the same badge (the two pipeline files of v0.167.18) is inserted into the body's HTML directly after the closing tag of the last ruled section's H2, and floated right, so the section's first paragraph and what follows run round it. The H2 is found by its id, which is the same `sanitize_title()` of the last entry in the page's section array that `achology_article_anchors()` writes, so the contents list, the anchors and this insertion read one array. It renders only for `essential-reading`, like the hero badge; alt empty for the same reason (the seal repeats a fact the page states in words); `loading="lazy"` because it sits far below the fold.

In `book-note.css`: `.bn-body__badge` floats right at 128 square with the writing's gutter on its left (40, the same number the floated aside carries) and 16 beneath, and a 4px top margin that lifts its top from the first line box's top to the top of the type, the 16px face sitting 4px into its 28px line. On a phone it is 96 with a 24 gutter, so the lines beside it keep at least 230px of the 350 column.

**Measured on the deployed page.** At 1440: badge 128 square at x 1032 to 1160, its right edge on the column's right edge; its top at 3255, the first line's type top also 3255, a difference of 0; the lines running beside it end at x 988, 44 clear of the badge; the 2x file is the one loaded on the retina pane. At 390: badge 96 at x 274 to 370, top on the first line's top (difference 0), the lines beside it ending at x 241, no horizontal overflow. Stylesheet served at ver 0.167.22.

## Shipped

Theme v0.167.22, `deploy.py` three proofs passed: server identical to local, zip 700 files matching the theme, server reporting 0.167.22. Commit pushed. Opened in Safari for Kain as a new tab at the section's anchor. **His eye on the placed badge is not yet given:** his word was the instruction; this file records the ship.

## Owed to the documents

DSRD 9 section 32.4 (the reading zone) or wherever section 32 places the body's floated blocks: a row for the last section's badge (float right, 128/96, the 40 and 24 gutters, the 4px type alignment, Essential Reading only, alt empty, lazy). Yours, with this file and the v0.167.18 and v0.167.19 files as the badge's record.

OWED BACK: the section 32 row, yours. Nothing from Kain unless his eye says otherwise.

*No em or en dashes in this file; checked before writing.*
