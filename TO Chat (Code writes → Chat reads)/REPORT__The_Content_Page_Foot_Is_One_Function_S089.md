# REPORT: the foot of the content pages is one function, and building it found the two feet were never identical

**From:** Claude Code, Session 089. **Date:** 31 August 2026.
**Answers:** `RULING__The_Content_Page_Foot_Is_One_Standard_S088`, and Kain's instruction in that sitting: "can I just ask you to copy that over to the articles page and make that a token, so that is essentially now one token, one template we're using site wide."
**Board card:** Knowledge Hub Page Designs, lines 1 and 2.
**Shipped:** theme v0.119.1, deployed and proved.

---

## 1. What was built

`achology_content_foot()` in `knowledge-hub-parts.php` renders the author signature, the course row, Related Further Reading and the trial panel, with the separators between them. Both content templates call it by name. The quote and workbook templates will call the same function when they are built, which is what makes Kain's "true for articles, book notes, quote articles, and workbooks" hold by construction rather than by three more careful builds.

**The one thing not shared** is the article page's source book callout, because a book note's source book is the page. It is rendered by that template and handed in.

**A separator is emitted only where its block produced something.** Each block is buffered and its wrapper written only if the buffer came back with anything in it. Both pages already refused to draw a rule around nothing, each in its own way with its own long comment; it now holds by construction rather than by two conditions kept in step.

## 2. The finding, and it is the reason this was worth doing

**`RULING__The_Content_Page_Foot_Is_One_Standard_S088` section 1 says the two feet are "identical, block for block, to the pixel". That was measured at 1440 and is false on a phone.**

The two pages carried two different separator mechanisms. The article page drew a standalone `.kh-article__hairline` div with 48px of margin each side and **no phone tier at all**. The book note wrapped each block in `.bn-sep`, which carried a border-top with 48px above and below **and a phone tier dropping both to 32px**, as DSRD 7 section 4.3 requires as amended at S245.

At 1440 the two are indistinguishable. Measured at 390 before this change, both pages:

| | article | book note |
|---|---|---|
| course row | top+341 | top+309 |
| the nine links | top+1542 | top+1519 |
| the two ways out | top+1742 | top+1719 |
| the trial panel | top+1900 | top+1861 |

Thirty two pixels apart, block for block, on the two pages Kain had just ruled must be the same. **No measurement at desktop width could have shown it**, which is why the S088 check did not.

The article page now takes the tier that was ruled for that separator and that one of the two pages carrying it never had.

## 3. What was measured, before and after

The before-and-after snapshot was extended this session, because the S088 version was blind to exactly the two things this refactor touches: it measured everything from the author card's own top, so a change to the gap ABOVE the card was invisible, and it ran at 1440 only.

**Desktop, both pages: every number identical to the before shot.** Author card, course grid, the links, the ways out and the closing panel, position and size.

**Phone: the article page moved onto the book note's spacing** and the two now agree on every separator. The remaining difference downstream is 26px of course card height, which is the cards' own content and predates this work.

**It caught a regression on its first after-run**, which is what it is for. Moving the author card out of `.bn-read__main` dropped it from the 880 reading column to the 1104 page frame on the book note page: left 168 width 1104 against the article page's left 280 width 880. Fixed at v0.119.1 with `.kh-foot__signature`, so the signature takes the column by rule rather than by inheriting whichever container each page wrapped it in.

## 4. What changed in the stylesheets

`.kh-article__hairline` and `.bn-sep` are both deleted. `.kh-foot__sep` in `knowledge-hub.css` replaces them, carrying the 880 column and the rule together, on Kain's own S088 correction when the trial panel first shipped outside the wrapper: "please correct yourself and build the block into the correct page container with a hairline above it."

One more rule was deleted as saying nothing: `.bn-read__main .author-card` set margin-top to `--sp-xl`, which is 32px, and `people.css` already sets 32px on the component.

## 5. Nothing is owed to Chat by this

No DSRD carries either retired class, and the copy, counts and marks are unchanged. The corrections DSRD 9 is owed are the ones already named in the S088 ruling file and they still wait on Kain confirming the pages, exactly as its OWED BACK line requires.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
