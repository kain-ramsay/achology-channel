# RULING AND SHIP: v0.167.16, the book note hero's meta line splits, the author under the title and the rating under the standfirst

**From:** Claude Code, Session 102. **Date:** 5 September 2026, evening.
**Ruled by:** Kain, in the S102 sitting, in chat, on the rendered page he had open, the second of his small improvements after the hero width and the overline wording.
**His words, quoted exactly as typed, first message:** *"ok, heres the second one: currently, 'Book Authored by Albert Ellis and Robert A. Harper · Achology rating · Essential Reading all sites on one line"*.
**Second message, on being asked whether the two halves split:** *"Yes, and i think that Achology rating · Essential Reading" with the ticks could be relocated to under the mini description. Does this make sense?"*
**Filed under Harness Rule 14.** A theme edit made in a factory session on Kain's word, named in the theme commit `66a9731`.
**Board card:** Knowledge Hub page designs.

## What changed

The one meta line S086 made is two lines again, in new places. In `single-book_note.php` the author line, "Book Authored by {author}", keeps its place directly under the H1 and renders only when the record names an author. The rating line, "Achology rating · {scale words}" with its ticks, moved out of it and now renders after the standfirst (the `post_excerpt`, Kain's "mini description") and before the two buttons, as `.bn-hero__meta bn-hero__meta--rating`, only when the record carries a rating. Both lines take the same rule, so both still run at the 16 step and the 500 weight Kain set at S086 ("the same sized font please"); the line half of that S086 ruling is superseded by this one and the size half stands.

In `book-note.css`: one modifier rule, `.bn-hero__meta--rating`, carries 32 below it to the buttons; one rule, `.bn-hero__lead:has(+ .bn-hero__meta--rating)`, closes the standfirst up to 16 above the rating line when the rating follows it, so the rating reads as the standfirst's footnote and the buttons sit exactly where they sat before the move. `:has()` is used the way `policies.css` and `help.css` already use it; a browser without it keeps the standfirst's 32 and the page still reads.

**Measured on the deployed page at 1440 and 390 (the gaps are identical at both):** title to author line 8, author line to standfirst 24, standfirst to rating line 16, rating line to buttons 32. The rating line holds one row at both widths and carries three ticks; the author line wraps to two rows at 390, which is what its wrap is for. Stylesheet served at ver 0.167.16. No horizontal overflow at either width.

## Shipped

Theme v0.167.16, `deploy.py` three proofs passed: server identical to local, zip 664 files matching the theme, server reporting 0.167.16. Commit pushed. The page was read in the in-app browser at the two widths above and opened in Safari for Kain as a new tab. **His approval of the rendered result is not yet given:** this file is written at the ship, and his yes or no on the page follows in chat.

## Owed to the documents

DSRD 9 section 32.3's hero stack table lists "Book author, linked" (Mulish Lead Paragraph 19px/500, 24 below) and "Standfirst" (17px/1.75, 32 below) directly under the H1, and carries no rating row of its own; section 32.9 item 1 places the rating "in the hero as Achology rating · {value}". The built page now reads: author line at 16/500 under the H1, 24 below; standfirst, 16 below when the rating follows it; rating line at 16/500 under the standfirst, 32 below, to the buttons. Yours. The S341 head note on section 32.3 holds six disputed hero values for a second-look sitting; tonight's sitting ruled only what Kain raised (the width, the overline wording, this split) and those six stand as they were.

OWED BACK: the section 32.3 stack rows for the author line and the rating line, yours.

*No em or en dashes in this file; checked before writing.*
