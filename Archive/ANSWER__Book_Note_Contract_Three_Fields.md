# ANSWER: two of the three extend the contract, one is deferred with a reason

**From:** Claude Code, S230. **Date:** 2026-07-29. **Answers:** `QUESTION__Book_Note_Contract_Three_Fields_Outside_It.md`.

Short version: **tags extend it, the ratings extend it, the recommended course is deferred.** Twenty one columns becomes twenty four. You asked the question in the right order, before 620 rows are produced.

## 1. Tags: yes, extend the contract

**Column 22: `tags`, pipe separated, term slugs, one or more.** Consumed exactly as categories are.

The taxonomy is registered against every Knowledge Hub type, book notes included, so nothing needs building for the terms themselves. It matters more than a pill on a page: `single-article.php` already queries related content by shared tag, and falls back to category when a piece has no tags. A book note imported without tags is not just missing its pills, it is invisible to the related-content block on every other piece and gets the weaker fallback itself. At 620 rows that is the difference between a Hub that cross-links and one that does not.

**Use the existing 36 slugs where they fit.** New terms are fine, but each one is a new page in the tag layer, so a tag used once is a page with one item on it. Worth a pass over your three authored tag columns before production: three per book across 620 books is up to 1,860 tag assignments, and if that produces 400 distinct tags, the layer is noise. If it produces 60, it is navigation.

## 2. primary_recommended_course: deferred, and here is the honest reason

**No column yet.** Not because the field is wrong, but because the thing it points at does not exist.

`single-article.php` renders the related-course block from **hardcoded prototype course data** with a comment saying exactly that: "Courses are standard WP pages and none exist ... CTAs point at the /courses/ directory meanwhile." There are no course pages on the site to link to, so a column carrying a course reference would be filled at production for 620 rows and consumed by nothing.

**What I would do instead:** leave it out of the file now, and add it when the course pages are built, as a single pass over the finished notes rather than a column filled 620 times against a placeholder. If Kain would rather have it authored once while the editorial context is fresh, add it as **column 25, `primary_recommended_course`, carrying the course page slug**, and I will build the CTA to read it the moment course pages exist. That is his call rather than mine: the cost is authoring 620 values that sit unused for a while, against the cost of a later pass.

Either way, **do not write the CTA into `body_html` at production.** A course name baked into 620 bodies is 620 edits the first time a course is renamed or retired, and DSRD 2 section 3 already keeps price and product facts out of body copy for that reason.

## 3. The two rating fields: yes, extend the contract

**Column 23: `achology_rating`.** The three-tier editorial value, written as the words DSRD 2 section 5.2 names: `Recommended`, `Highly Recommended`, `Essential Reading`. Send the words, not the numbers, and I map them to 3, 4 and 5 stars in schema at import. If the file carries the star numbers instead, the mapping lives in the spreadsheet where nobody can see it, and the day the tiers change every row is wrong.

**Column 24: `goodreads_rating`.** Numeric, one decimal place, blank permitted. Rendered on the page as social proof and, per section 5.2, **kept out of the schema**. I will build it that way: the two values never meet.

One flag on the editorial rating, since it goes into structured data. Google's guidance is that a review rating must be an honest editorial assessment, which it will be, but a set of 620 books where nothing scores below three stars reads as a promotional scale rather than a rating. That is a content decision for you and Kain, not a build one, but it is easier to decide now than after publication.

## What I need in return

Nothing blocking. When the file is final, send me the column order you settle on and I build the importer to it exactly, the way the Help/FAQ 43 ran.

**One thing to fix in the documents while you are in there:** DSRD 2 section 6.1 still describes the Book Note template as inheriting a "genius link", which the S231 decision retired. That is the second place the Genius Link retirement has not landed, the first being DSRD 1 line 150.

*No em or en dashes in this file; checked before writing.*
