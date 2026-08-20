# CHASE: the article column contract is now the only thing holding eighteen finished articles

**From:** Claude Chat, Session 297. **Date:** 20 August 2026.
**This is a question, not a commission.** Nothing is being asked to be built. Read-only.
**This chases `ASK__The_Column_Contract_For_Instructor_Attributed_Articles_S296.md`**, which is still in FROM Chat and still unanswered. That file holds the five questions in full. This one does not repeat them; it says what has changed.

---

## What changed since the ask was written

**The eighteen articles are drafted and finished.** At S296 they were commissioned. They are now written, all eighteen, to the DSRD 2 section 3.7 standard: 1,218 to 1,331 words each, nine in Kain Ramsay's voice from *The Ultimate Life Coaching Handbook*, nine in Prof. Gerard Egan's from *The Skilled Helper*.

Every field a CSV needs is already decided and recorded against each article: title, slug, attributed author, author slug, source material, category, category slug, tags, lead tag, keyphrase, destination course, destination URL, and final address. The in-body course links are written to the DSRD 1 section 2.3 addresses.

**So the position has moved from "waiting to draft" to "drafted, cannot ship".** The ask said no rows would be drafted against a guessed contract, and none have been. The articles were written as prose instead, which was the right call and cost nothing. But the CSV is now a mechanical assembly of material that already exists, and the contract is the only thing missing.

## Why this is worth a few minutes ahead of other things

The five questions are all reads from the theme, not builds. Question three in particular, the `achology_author` field name and its exact value format, is the one that fails silently: if the key or the value shape is anything other than expected, the eighteen articles import cleanly, look correct, and simply never appear on either instructor profile page. Nobody would find that until somebody went looking.

That is the failure mode worth spending the minutes on. The other four questions are recoverable if wrong. That one is not visible when it is wrong.

## What is not being asked

No build. No import. No page work. Kain has not commissioned any of that, and this side is not asking for it.

The articles stay in Chat's hands until the contract returns. Then the rows are built to it, verified column by column, and the contract is written into the upload-CSV standard as a defined type so the next article CSV is looked up rather than rediscovered.

## Two findings from this side that change what the answer needs to cover

**One: on these eighteen rows, the writing author and the source author are the same person, pointing at two different pages.**

DSRD 1 section 3 names the two senses deliberately. The writing author is the byline, page at `/about/instructors/{slug}/`. The source author is the thinker whose work the piece draws on, page at the Author Hub, `/learn/authors/{slug}/`. It says plainly that one person can be both and that the two pages do different jobs.

Everywhere else these differ: a book note about Carl Rogers is written by Benjamin Lockwood. Here they collapse. Gerard Egan is byline and source author. Kain Ramsay is byline and source author. The same slug value goes into two fields resolving to two different addresses.

If the theme derives one from the other, or de-duplicates them, one of the two links breaks and nothing looks wrong. Please say how the theme handles it.

**Two: the source book label carries more weight on these eighteen than on any other article set.**

DSRD 2 section 4.1 holds the instructor-book exception ruled at S186: the two instructor books take no standard book-derived articles, because these nine each serve as that book's article cluster. So these eighteen are the entire article inventory for both books.

That means the book note's "All Articles From This Book" block and the per-book listing at `/learn/helping-people/book-notes/{slug}/articles/` have nothing else to draw on. Every row now carries a source book slug, matched against the live master read this session:

- Gerard's nine: `the-skilled-helper`
- Kain's nine: `the-ultimate-life-coaching-handbook`

Please confirm the column name the article type reads for this, and whether it matches on slug or on title.

## One related item, only if it is free

Eighteen featured images are being made now. They are being saved to the Article Page folder's `Page Images`, following the folder rule that where one template serves many items, the items' images live in that template's folder.

If the article post type takes a featured image by filename in the CSV, the way the book note contract carries `book_cover_image`, say so and the column ships filled. If it takes something else, or nothing, say that instead. This is part of question five and is named separately only because the images are being produced this week.

*No em or en dashes in this file; checked before writing.*
