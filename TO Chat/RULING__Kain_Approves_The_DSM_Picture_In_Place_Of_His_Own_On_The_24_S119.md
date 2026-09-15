# RULING: the DSM cover replaces Kain's photograph in the body of the 24 DSM articles, per article, and he approved it on the rendered page

**Filed by Claude Code, Session 119. Date:** 15 September 2026.
**Given by Kain directly in this sitting, and approved by him on the live page in Safari.** Filed under Harness Rule 14 so Chat writes it into the document that owns it.

---

## What he asked for, in his words

> "See in the twenty five DSM... sorry, the twenty four DSM related articles. do you think it'd be possible to replace the picture of me, which is kind of a little bit inappropriate in these twenty four articles, with a picture of the DSM, the actual book instead? with the appropriate text underneath it. Is that is that doable?"

Told that the block is drawn by one shared piece of the theme, so a straight swap would take his photograph off every instructor article on the site, and that the better shape was a picture chosen per article, he ruled:

> "The DSM is just a book like any other - there will be many free images of it we can choose from. Rather than just write it up as a theme job with that shape, per-article picture rather than a site-wide swap - could we deliver it right now so it doesn't get deferred and forgotten about?"

## What was built, and why a factory session built it

Per article, never site-wide. Three new article fields, `aside_image`, `aside_caption` and `aside_credit`. An article that sets none behaves exactly as it did before, so every instructor article where Kain is writing from his own experience still carries his photograph. `achology_book_author_portrait()` gained one flag, `$subject`, which changes only the crop: a portrait stays held to 4 by 5 so faces line up across the site, a subject picture keeps the shape of its own file so a book cover does not lose the edges of its jacket. Position, float, hairline and both caption lines are untouched, because none of Kain's S113 and S115 rulings on this block was about who is in the picture.

A factory session made a theme change, which Harness Rule 1 as corrected at S334 allows on Kain's word in the sitting: "Where Kain rules a change in a sitting, that sitting makes it and lands it, whichever type it is." His ruling is named in both theme commits, `d87260f` and `e552705`, and in this file, which is the price that rule sets. Theme version 0.438.1, deployed, with local, server and zip all measured as agreeing.

## The picture, and the one that was thrown away

The cover came through the project's own cover ladder in `tools/book_cover_source.py`, the same route that sourced 599 of this site's book covers, not from a picture chosen off the open web. **The first result was refused on sight:** Apple Books returned a third-party reprint of the 1952 DSM-I carrying a stock photograph of a shaved head with a brain drawn on it, which is the wrong book and a worse picture for these articles than the one being replaced. The genuine DSM-5-TR cover came from Open Library by ISBN, 349 by 500, and was checked by eye before anything was built on it.

Nothing in the caption was drafted. The line above the hairline is the book's own title and the line below it names the edition, the publisher, the year and the source the picture came through.

## His approval, on the rendered live page

Shown one of the 24 live in Safari and asked whether the picture was the right size on the page:

> "yes, its the right size on the page - perfect size in fact!"

**Rule 14's fold-back does not apply here, and this says why rather than leaving it unwritten.** The fold-back asks that an approved rendered component be exported into its design folder as the prototype's next version with its build sheet updated. This block has neither: `NOTE__What_Governs_A_Component_With_No_Build_Sheet_S257.md` puts every component except the book note card in the not-yet-carried-across state, where DSRD 8 governs and there is no prototype for a new version to sit on top of. The same note says carrying a component across is Chat and Kain's act, not Code's. So this ruling, with his two quoted sentences, is the whole record until this block is carried across, and when it is, his approval of the subject variant at 240px is already written here.

## A real fault found underneath, fixed in the same change set

`achology_image_dimensions()` could not read a picture from the media library at all. Every caller before today handed it a theme asset, so an uploads URL fell through to a path inside the theme that does not exist and the helper returned nothing: no width, no height, and the writing beside the picture moving as the file arrived. Found on the first render of the DSM cover, which is the first caller ever to pass one. Fixed for every caller, not just this one, by asking WordPress where its uploads live rather than spelling it. Commit `e552705`.

OWED BACK: nothing. Recorded here for the document that owns it.

No em or en dashes in this file; checked before writing.
