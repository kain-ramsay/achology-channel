# SHIP: the page title takes 24 above its reading text. Theme 0.230.0

**From Code, S109. Deployed, cache purged, and measured on the live pages.**

## What changed

Two declarations and one comment. The quote page and the book note give 24 under
the page title where they gave 16. The article is untouched at 8. The rule's own
record at `.kh-article__title` in knowledge-hub.css now carries three values and
its open line is closed.

## Why

Kain's ruling in the S109 sitting, on photographs of the two real pages at 16 and
at 24. It is filed whole as
`RULING__The_Page_Title_Takes_24_Above_Its_Reading_Text_S109`.

## What was measured after the deploy

On the live pages, through a real browser: 24 on the quote page and on the book
note, 8 on the article, and all four page titles still rendering at the same size
and weight in an h1. Local, the server and the zip agree at 0.230.0, each
measured rather than assumed.

**The gate's verdict on the book note is FAIL, and it is not this change.**
`page_gate.py` has no check on the space under a page title at all, which is the
recommendation in the ruling file. That page's 27 failing lines are its own
images: a cover whose stated dimensions do not match the file, a cover well over
its slot budget, and sixteen images with no srcset. They stood before this change
set and are untouched by it. Raised here rather than left in a printout.

## What I need from Chat

The three values into DSRD 7 section 4.3, and a yes or no on the gate check. Both
are in the ruling file.

---

OWED BACK: nothing beyond the ruling file's two lines.

*No em or en dashes in this file; checked before writing.*
