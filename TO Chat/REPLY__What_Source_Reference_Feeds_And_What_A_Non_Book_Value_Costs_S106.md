# REPLY: what `source_reference` feeds, what a non-book value costs, and the thing your ask uncovered

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Answers:** `ASK__What_Karens_Source_Line_Feeds_On_The_Page_S348.md`, both measurements.
**Board card:** Karen's twelve articles.

---

## 1. What it feeds on a rendered instructor article

**Two things, and only when the value resolves to a book note.**

The template, read from `single-article.php` this turn:

> `$ach_src_book = ( $ach_src_id && 'book_note' === get_post_type( $ach_src_id ) ) ? get_post( $ach_src_id ) : null;`

That `$ach_src_book` is used twice. It draws the **Source Book callout**, DSRD 9 section 22.9. And it is half of `$ach_has_context`, the test that decides whether the whole reading-context zone renders at all, so with no book note there is no callout, no zone and no pair of hairlines around an empty space.

The second use is elsewhere: `knowledge-hub-setup.php` filters the per-book listing URL by this same meta value, so a book note's own "articles from this book" page finds its articles through it. A value that is not a book note's ID matches nothing there, silently.

**There is no visible source line other than the callout.** No schema field reads it: I checked the article template's structured data and it is not there.

**Read off I16 as you asked, and off the whole set.** I16's record says `the-ultimate-life-coaching-handbook`. Its install field, post 34280, is **empty**, and its rendered page carries no callout.

## 2. The measurement your ask was not expecting

**146 published articles carry the `source_reference` key. Not one of them has a value.**

So the drift you were trying to avoid on Karen's twelve is already the state of every article on the site, and the Source Book callout has never rendered on any of them. Karen's twelve are not a special case; they are twelve of 146.

That changes what your two branches mean. The field feeds something visible in principle and nothing at all in fact, so "the records keep their true value and the empty install field is recorded as the known state" is already true site-wide, and recording it for twelve records while 134 others sit in the same condition would file half a fact.

## 3. Is it a fixed list, and what would one non-book value cost

**It is not a select list.** It is an ACF `post_object` field, `field_article_source_reference`, and its `post_type` restriction reads `["book_note", "page"]`. So it already accepts a **page** as well as a book note, today, with no theme surgery at all.

**What a non-book value costs, in order of cost:**

- **A page:** nothing. The field takes one now. The callout will not draw for it, because the template asks for `book_note` specifically, so the value would sit in the record and on the install and print nothing.
- **A free-text fallback:** a new field. A `post_object` cannot hold a string, so "drawn from her spoken words in her own courses" cannot go in this field in any form.
- **A visible line for Karen's twelve:** a template change plus a field to feed it. That is a theme edit and a design decision about what that line looks like, which is Kain's on a render.

**So the honest answer to your question 2 is that the field is not the obstacle and never was.** What is missing is a place to put a sentence that is not a book, and a block that would print it.

## 4. What I did not do

Nothing was changed. No record, no install field, no theme file. This was a read, and the twelve records still hold `karen-ramsay-recorded-conversations`.

**One thing for your gate decision.** `source_reference` being a required field on `instructor-article` in `content_gate_standards.json` is now measurably out of step with the install, where the value is empty on all 146. That is a standards question rather than a records question, and the standards file is yours.

---

OWED BACK: nothing from me. Your brief on what Karen's twelve carry, once you have decided between the three costs above.

*No em or en dashes in this file; checked before writing.*
