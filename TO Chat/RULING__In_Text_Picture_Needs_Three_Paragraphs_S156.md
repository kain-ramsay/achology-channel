**Needs from Chat: write Kain's S156 ruling on where the in-text picture sits into its owning document (the DSRD that holds the S116 "second paragraph" rule and the S130 quote page "book two" position). Already built and deployed as theme 0.707.156. For the factory session (a theme edit made in it on Kain's word in the sitting, Harness Rule 1).**

# RULING: an in-text picture takes a section only when it has three paragraphs or more (Kain, S156)

**From:** Claude Code, S156 factory session, Thursday 8 October 2026, 17:50.

## Kain's words

On the first Lane B quote page, read in Safari: "the problem is there's only two paragraphs in that section, which means it creates massive white space on the page ... put in place a rule that the image ... only aligns with the top of the top line of text in the second paragraph so long as there's a minimum of three paragraphs of copy within that section. If not, um, we might have to fluctuate between section three or section four."

## What was built

`achology_book_author_portrait()` in `knowledge-hub-parts.php` (shared by the article, the book note and the quote page): the section each page names is tried first, then up to two after it; the first with three paragraphs or more takes the picture, at its second paragraph (the S116 rule, unchanged). Where none has three, the named section keeps it, so no page loses its picture. Deployed as **0.707.156**; `deploy.py` proved local, server and zip agree.

**Measured:** of the build site's quote pages, 276 have three or more paragraphs in the first section and are unchanged (one read back in the browser: picture still in its first section of three paragraphs); the 17 Lane B drafts all have two, and each takes the picture in its second section (three to five paragraphs). Articles and book notes follow the same rule wherever their picture's section is short.

OWED BACK: the dated line in the owning document.

*No em or en dashes in this file; checked before writing.*
