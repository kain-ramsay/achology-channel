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

## The same block, used a second time the same evening, and approved again

Kain then asked for the same treatment on the six AI wisdom articles: "these 6 images, the same as before with the dsm ones - my face is on all of them in the article body - can we find an appropriate ai image or cartoon that we could use and attribute to whoever needs it?"

**The picture is the original ELIZA, 1966**, the program that imitated a Rogerian psychotherapist, having exactly the kind of conversation those six articles are about. Public domain, no restrictions, found on Wikimedia Commons and credited under the picture naming Weizenbaum who described it and Landsteiner who made this implementation. **A second candidate was rejected on its own metadata:** Commons records `ELIZA chatbot.png` with the restriction "ai", meaning the picture is itself AI generated, which on articles about being honest regarding AI is the wrong object entirely. Nothing about either licence was assumed: both were read from Commons' own extmetadata and printed before anything was chosen.

This is the same route the site already stands behind for its author photographs, whose licence and credit live in `images/book-authors/credits.json` and are printed by `achology_photograph_credit_line()`.

**Then three rulings in a row on the rendered draft, each acted on and re-rendered before the next:**

> "it reads small, on this 6 article only, the image needs to be a bit bigger please - but ONLY in these 6 articles!"

> "The image could probably be 25% smaller on all 6."

> "10% bigger please."

> "perfect!!!"

**The width is decided by the picture's shape, not by a list of six pages.** A portrait keeps the 240 that suits a face; a subject picture wider than it is tall takes three eighths of the reading column plus a tenth, which is 330 today. Measured at each step rather than assumed: the six carry it and a DSM article, checked in the same breath, does not, because the DSM cover is portrait. A list of six post ids in a stylesheet would rot the first time a seventh article wanted a wide picture; a rule does not. Theme versions 0.439.0, 0.439.1 and 0.439.2, each gated (`css_gate`: knowledge-hub.css PASS), deployed and read back off the server.

**The fold-back still does not apply, for the same reason given above:** this block has no prototype and no build sheet, so under the S257 transition note it is DSRD 8 that governs and carrying it across is Chat and Kain's act. His three sizing rulings and his approval are recorded here so that whoever carries it across has them.

## A real fault found underneath, fixed in the same change set

`achology_image_dimensions()` could not read a picture from the media library at all. Every caller before today handed it a theme asset, so an uploads URL fell through to a path inside the theme that does not exist and the helper returned nothing: no width, no height, and the writing beside the picture moving as the file arrived. Found on the first render of the DSM cover, which is the first caller ever to pass one. Fixed for every caller, not just this one, by asking WordPress where its uploads live rather than spelling it. Commit `e552705`.

OWED BACK: nothing. Recorded here for the document that owns it.

No em or en dashes in this file; checked before writing.
