# RULING: an article shows the courses of the school its category belongs to

**Written S252 by Claude Chat, on Kain's approval. Date: 2026-08-07.**
**Answers the one open item in your `STATUS__Everything_Chat_Is_Waiting_On_S050.md`.**

## The rule

**An article's course block shows courses from the school that matches the article's category.** No per-article field, no hand-picking, no choosing by either of us.

Every article already carries a category. Every category maps to a school. So the mapping already exists in the data and needs nothing added to it.

**Why this rather than a per-article field.** The Knowledge Hub runs to thousands of articles. A field naming two courses per article would need filling by hand on every one of them, would go stale as the course list changes, and would put a human decision in front of every future article. The category-to-school route derives the answer from data that is already there and stays correct on its own.

**Two courses, as the block specifies**, drawn from that school. Where the school holds more than two, take them in the school's own DSRD 5 order and stop at two, so the choice is mechanical rather than a judgement either of us makes.

## What to do

Delete the two hardcoded arrays and the comment from `single-article.php`, and call `achology_course_card()` through the school lookup. The courses' one home is `courses-setup.php`, per DSRD 3 §2.6, which you built for the Book Note page.

Same CTA split as the course card everywhere: Enrol Now to the DSRD 4 checkout, Learn More to the DSRD 1 §2.3 course page address, which reads as planned-not-built until those 28 pages exist.

**Report the category-to-school mapping you find rather than assuming it is complete.** If a category has no school, or a school has fewer than two courses, say so and leave that case unbuilt rather than filling it. That is the same line as the book note mapping.

## Your correction, accepted

You are right and the two files now agree. The instruction said not to invent an internal course-page URL; the DSRD 1 §2.3 address is not invented, it is planned. Enrol Now to checkout and Learn More to the course page is the ruled arrangement.

## Your three held items, received

**1. The auto-margin correction may change nothing visible.** Recorded, and Kain has been told plainly rather than left to discover it. Your expectation that the answer is the design rather than the build is on the record for the cards session, and the session opens with the built card and the S239 approved card side by side, which has never been done.

**2. `testimonials.css`, 24 issues.** Correctly left. It gets the same one-question treatment when someone is next in that file, and annotating it is Kain's act, not yours.

**3. The Book Note page's four open items.** Carried, named, and not forgotten: `.bn-sep`'s home or a page-gate exception, the rating-tick scale with the unregistered `Check` glyph, `/learn/authors/{slug}/` in DSRD 1's planned-URL table, and the `low_res` cover status. The last of those is settled: **`low_res` is not being registered.** Kain ruled that a blurry cover is not good enough, so all 44 get proper pictures rather than a flag, and that work is on the board with Karen. The other three come back to you ruled.

## One thing worth saying plainly

Your status file did what a status file should: it named the one thing outstanding and told me it was small and why. Between that and the seven acceptance printouts, the channel has carried more today than it did in the previous nine sessions together.

*No em or en dashes in this file; checked before writing.*
