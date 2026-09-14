> **CODE DISPOSITION, S116: WAITS ON the book being drawn in the three places left, the book note card, the Knowledge Hub home page and the author biography's book list. Kain's ruling is given:** he locked the component at 0.425.3 with the words "that's good Claude, lets lock in all of these changes", after four changes of his own in the same sitting. The prototype and build sheet are exported at that state into the Book (ach-book) component folder, and everything below is in `RULING__The_Drawn_Book_Is_Approved_And_The_Cover_Refetch_Is_Dropped_S116.md`. Drawn today on the book note hero, the book note side column, the quote page's source block and the article's source callout. **Two halves of this brief are overtaken by his word in the same sitting.** Read in full the moment it arrived, mid-session, under the channel wall. **Section 0's hold is lifted by Kain**, who asked for the book image next, ahead of the quote page, which the S357 version's own section 5 allowed for in the words "unless Kain says otherwise". **Section 1's fetch is dropped by Kain**, on measurements taken before it ran: the covers this site already serves are 1000 by 1500, Open Library's largest for these titles is about 320 by 500, one came back at 128 by 193, and Google Books answers 429 to every call. So section 2's gate line, "the cover must come from the ISBN fetch at or above 1200px", cannot be met by the source section 1 names, and the fetch would have replaced good files with worse. `ach-book` is built and live on the book note hero at 0.423.0, from the covers already held. Filed as a RULING in TO Chat. Testable: this file goes DONE when Kain has ruled the drawn book in Safari and it is drawn in every place a cover shows.

# BRIEF: the book cover becomes a drawn book everywhere, clean covers fetched by ISBN, a baked PNG per book

**From:** Claude Chat. **Date:** Monday 14 September 2026 (S360; rewritten from the S357 record after the original brief was found missing from disk).
**For:** Claude Code.
**Authority:** Kain, ruled S357: the web-sourced covers on the hero "look terrible," and every cover should look like a real book, automated, everywhere a cover shows.
**Board card:** Book note page template: second look in Safari.
**Read this cold.**

---

## 0. Sequencing: do not start yet

This brief was scoped, at S357, to run after two things: the type-and-spacing foundations sweep, and three named content imports. Neither has happened as of this session (S360); the foundations sweep is still an open item in TO Chat, waiting on a dedicated sitting. Do not begin this brief until Chat confirms both prerequisites have cleared.

## 1. What is being asked for

**Clean covers, fetched by ISBN.** Open Library first, Google Books as the fallback. Every book note's cover comes from this fetch rather than whatever inconsistent web-sourced image currently sits in the record, fixing the crop and shape inconsistency DSRD 8 §31 already papered over with a centre-crop rule. This brief's fetch should normalise every cover to 2:3 as it lands, per the answer already given in `REPLY__The_Book_Note_Batch_From_S114_And_S115_Answered_S360.md`, retiring that crop rule rather than needing it.

**One sealed component, `ach-book`.** Draws the cover as a three-dimensional book, wherever a cover shows: the hero, the book note card, the side-column thumbnail, anywhere else a cover appears. One component, one set of rules, everywhere.

**A worked, real, open-source starting point exists; read it before building from nothing.** `scastiel/book-cover-3d` (GitHub, MIT licence, verified live and current this session: 88 stars, still maintained). Built for exactly this. It is a React component, but it also exposes `getCssForSettings()`, a function that returns plain HTML and CSS for a given cover with no framework required, which fits this theme's PHP/vanilla-CSS build far better than the React component would. Its settings list is the right shape to study before designing `ach-book`'s own: rotation, hover rotation, perspective, spine thickness, corner radius, width, height, background colour of the inside cover. Read it for the technique and the settings shape; do not import it wholesale, since the component still needs to be Achology's own, sealed and consistent with the rest of the design system.

**A baked PNG per book, for the share image.** Stamped and gated the same way the quote card's share image already is.

## 2. The gate lines this adds to the book-note type

Two new lines, book-note type: the cover must come from the ISBN fetch at or above 1200px; the share image must carry its stamp.

## 3. The not-found rule

A published book note whose ISBN fetch fails keeps its old cover and stays live, until Kain or Karen supply a replacement by hand. An unpublished one fails outright rather than importing with a placeholder.

## 4. The look is Kain's, in Safari, tabbed

Before this ships, the rendered look goes to Kain in Safari, tabbed, one variable changed at a time, per standing rule 16 and the S277 tabbed instruction: rotation, thickness, and corner radius are the three most likely candidates for a first pass, but confirm the actual variable set against what `ach-book`'s build ends up needing.

---

OWED BACK: confirmation the two prerequisites have cleared before this starts. Once started: the built component, the fetch pipeline proven on a real ISBN, and the tabbed render ready for Kain's Safari sitting.

*No em or en dashes in this file; checked before writing.*
