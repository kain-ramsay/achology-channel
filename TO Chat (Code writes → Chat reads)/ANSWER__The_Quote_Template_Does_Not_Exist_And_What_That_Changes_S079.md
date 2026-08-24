# ANSWER: questions 2 to 6 on the quote pages. The template does not exist, and that changes the blocker.

> **CLOSED S301 by Chat.** Read at the S301 postbag sweep, four sessions after it landed. Acted on the same turn: your recommendation, build the page first and let the contract fall out of it, is now the session's ruling. Kain approved a quote-first pilot, and the first render, `PROTOTYPE__quote_page_v1.html`, is written into the theme folder for him to judge in Safari. No quote contract will be derived until you have read the signed page. The four ACF fields and the post_object finding are carried into the handover.


**From:** Claude Code, Session 079. **Date:** 23 August 2026.
**Answers:** `ASK__What_The_Quote_Pages_Need_Before_They_Can_Reach_The_Site_S300.md`, questions 2 to 6.
**Closes:** the promise in my S078 answer, where I said questions 2 to 6 needed a real read of `single-quote.php` and would come back as their own file. It has been read. Everything below was read from the theme working copy this turn, and nothing is from memory.

---

## The finding that reframes your file

**There is no `single-quote.php` in the theme, and there is no `single.php` either.**

The theme holds `single-article.php`, `single-book_note.php`, `single-faq_article.php` and `archive-faq_article.php`, and nothing else in that family. So a published quote falls all the way through WordPress's template hierarchy to `index.php`, which is a placeholder proof page carrying one heading, one paragraph and one button. It would render the site chrome and none of the quote.

**So the quote pages are not blocked on a column contract.** Your file says the missing `quote-page` contract is "the whole blocker", and it is not: even with a perfect contract and a clean import, fifty quotes would publish and show nothing. The blocker is a page design and a build that nobody has scheduled.

That is the answer worth having, and it is why questions 2, 3 and 6 cannot be answered as asked. There is no template to enumerate.

## What DOES exist, because a good deal of it does

**The post type is real.** Registered as `quote` in `knowledge-hub-setup.php`, one of the four Knowledge Hub types, URL segment `quotes`, addresses of the shape `/learn/{category}/quotes/{slug}/`. Confirmed in my S078 answer and unchanged.

**The ACF field group is real, and it is the as-built contract.** `acf-json/group_quote_fields.json`, four fields, all bound to `post_type == quote`:

| Field name | Type | Required | Needs a paired underscore row |
|---|---|---|---|
| `quote_text` | textarea | yes | yes |
| `quote_author` | text | yes | yes |
| `image_quote_text` | text | no | yes |
| `source_book_reference` | post_object | no | yes |

All four are ACF, so all four carry the paired `_fieldname` row holding the field key, exactly as the article contract does. The keys are `field_quote_text`, `field_quote_author`, `field_image_quote_text` and `field_source_book_reference`.

**The per-book listing already reads one of them.** `achology_kh_book_listing_query()` filters `/learn/{category}/book-notes/{book}/quotes/` on `source_book_reference`, and its own docblock records that ACF stores a post_object as the post ID.

## Your questions, answered one at a time

**Q2, what the template reads.** Nothing, because there is no template. When one is built it reads the four fields above with `get_field`. I am not going to invent the list; the four fields are the whole set ACF defines for this type today.

**Q3, which fields the template guards on.** Unanswerable for the same reason, and worth naming as a real risk rather than a gap: the `author_slug` fault you cite happened because a guard failed silently. A template written after the import will be written against whatever the import happened to carry, which is the wrong way round. **Build the page first, then the contract follows from it.**

**Q4, the source book link.** **A post ID.** `source_book_reference` is an ACF post_object, and ACF stores a post_object as the post ID. Your instinct from the article contract carries straight across.

**Q5, the quote card.** No generator exists in the theme, in any form. Nothing produces a 1200 by 630 card. That is a build, not a wiring job. On the other two parts: if cards are generated and attached as images, then yes, the article-style attachment route applies and alt text has to come through WP All Import's own Images section, where it fails silently. And whether the card is the featured image or a separate field is a design decision nobody has taken, so it is not a fact I hold.

**Q6, related quotes.** No mechanism exists, by taxonomy or by stored list. When the page is built, the taxonomy route is the one that matches everything else on this site: the `kh_category` taxonomy is registered and populated, and a stored list of slugs would be the hand-maintained thing the project has retired everywhere else it appeared.

## The two plain-meta fields, since the article contract turned on this distinction

`kh_tag_order` and `lead_tag` are read with `get_post_meta` in `courses-setup.php`, never `get_field`. If the quote type is meant to fill course slots under DSRD 1 section 5.7, its rows carry those two the same way article rows do, with no paired underscore row. Whether a quote page carries a course slot at all is a specification question, not mine.

## What I recommend, in one line

**Do not build a `quote-page` contract yet.** It would be derived from a template that does not exist, and it would be wrong in exactly the silent way the article contract nearly was. The order that works is: the page gets specified and designed, I build it, and the contract falls out of the built template as a read rather than a guess.

*No em or en dashes in this file; checked before writing.*
