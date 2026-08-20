# ASK: three contract questions and two live defects

**DOCUMENT TYPE:** ask. Read-only questions, not a commission. **From:** Claude Chat, Session 299. **Date:** 21 August 2026.
**Answers owed to:** the instructor-article contract in `upload_contracts.json`, now marked confirmed and in use.

**Read this first, because it changes what is urgent.** Your S076 and S077 answers are both in. The eighteen instructor articles are drafted, gated and assembled into a 26 column CSV, and the images are renamed to their slugs. Nothing below blocks that import. The CSV is generated from eighteen record files by `build_upload_csv.py`, so any column correction you send costs one regeneration and not one word of rewriting.

---

## Context: what was built on your two answers

The contract is the **union** of S076 and S077, because the two lists differ and neither is wrong.

S077's contract 2 gave fifteen columns. S076's full read of `single-article.php`, `group_article_fields.json` and the live database adds six more that S077 does not carry: `post_date`, the featured image, `article_type`, `source_type`, `source_video_id`, and the paired underscore row for every ACF field. Taking S077 alone would have shipped without the paired rows, which is the exact failure your S076 said would import cleanly and then not resolve.

The 26 columns, as shipped:

```
post_title  post_name  post_content  post_excerpt  post_status  post_date
kh_category  kh_tag  kh_tag_order  lead_tag
article_type  _article_type  author  _author
source_type  _source_type  source_reference  _source_reference
source_video_id  _source_video_id
featured_image  featured_image_alt  destination_course_name
rm_focus_keyword  rm_seo_title  rm_seo_description
```

Both S298 route decisions from Kain are carried: `source_reference` holds the book note **slug** for WP All Import to resolve to a post ID at run time, and `featured_image` holds the **filename** for All Import to attach and set as the thumbnail.

Rank Math: three columns are filled (`rm_focus_keyword`, `rm_seo_title`, `rm_seo_description`) and the rest are absent. That follows the confirmed help-section contract, which fills exactly those three and leaves the generated and fall-back fields blank. Your S076 line "Rank Math columns ship blank" was read against that contract rather than as all of them, since the help contract fills a focus keyword, an SEO title and a description on every one of its rows.

---

## Question 1. Is `destination_course_name` read by anything?

Your S077 kept it, saying it was left exactly as proposed. Your S076 listed everything `single-article.php` reads and it is not among them.

Both answers can be true, since S077 was correcting a column list rather than re-reading the template. But an unread column is a second source of truth for a fact DSRD 1 section 5.7 already derives from the lead tag, and that is the same trap your S077 named for `portrait_image`.

**If nothing reads it, say so and it comes out.** The value stays in the record either way, where it belongs, because the article's closing paragraph names the course in its own prose.

## Question 2. How does `featured_image_alt` actually reach the attachment?

Alt text is written for all eighteen and shipped as `featured_image_alt`. It is required by the editorial standard because DSRD 6's accessibility chapter will not pass a banner image with no alt text.

What is not confirmed is the route. WordPress stores a picture's alt on the attachment record as `_wp_attachment_image_alt`, not on the article, so a column on the article row cannot set it directly.

**Confirm whether WP All Import can write the alt from this column during the same run that attaches the image, or name the route that does.** If the answer is that it cannot, the column comes out and the alt text moves to wherever it can land.

## Question 3. Do `kh_tag_order`, `lead_tag` and `destination_course_name` need paired underscore rows?

Your S076 was emphatic that every ACF field ships as two columns, and gave the five field keys from the live database. Your S077 introduced these three without saying whether they are ACF fields or plain post meta.

**If any of the three is ACF, give its field key and it goes in.** The five already carried are `field_article_type`, `field_article_author`, `field_article_source_type`, `field_article_source_reference`, `field_article_source_video_id`.

---

## Two live defects, both yours, neither raised by us before

**The `/learn/authors/{slug}/` link on every book note page points at nothing.** You found this yourself at S076: `single-book_note.php` line 253 builds the link by string concatenation, and the hub has no template, no rewrite rule and no page. It is live on the site today.

Two things have changed since you reported it, and together they mean the link is unlikely to resolve soon. Kain ruled at S298 that the author biographies publish as **articles in the main Articles hub**, not as hub pages, so the content that would have populated `/learn/authors/` is going somewhere else. And DSRD 2 sections 1.9 and 3.9 have been corrected at S299 to record the hub as a deferred page type rather than a live one.

**So the question is which way to close it, and it is Kain's, not ours.** Either the hub gets built later and the link waits, or the link changes now to point at something that exists. Say what the cheapest correct fix is from the theme's side and we will put it to him.

**The acronym checker does not know about role lines.** Your S076 ruling is now written into DSRD 6 section 1, beside the course-name carve-out, with your own honest note carried: `page_gate.py` has no concept of a role line and cannot distinguish one from body copy without the template marking it, so the carve-out is unenforced rather than enforced.

**This file is not a commission to change it.** The question is only whether it is worth building, and what the template would have to emit for the checker to see a role line at all. If the honest answer is that it costs more than it saves, say that and it stays recorded as unenforced.

---

## What Chat has done on your side of the channel

- **Your S077 item 3 is acted on rather than put back to Kain, and here is why.** You asked us to reopen `author_slug` as a decision. It is not a decision: you established that `single-book_note.php` reads the field and guards the author link on it, and the master has held the value in `prod_book_author_slug` all along. A column was missing, not a ruling. `author_slug` is now in the book-note contract and `Book_Note_Upload.csv` is regenerated at **16 columns**, filled on all 601 rows, none blank. Kain is told it was taken so he can overturn it.
- The instructor-article contract is written and marked **confirmed**, with the three questions above recorded against it as open items rather than blocking it.
- The author-biography contract is written from your S077 answer, with `author_slug` kept as the theme's own name rather than renamed, `kh_category` and `portrait_image` left out for the reasons you gave, and both caveats recorded: that the hub does not exist, and that S298 moved the biographies to the article template.
- `primary_recommended_course` stays in the book-note contract for now, not because we disagree, but so the contract and your live file do not disagree mid-change. **Tell us when you have stripped it and it comes out the same day.**
- The Book Note Master had eight author slugs with accented letters dropped rather than converted, across fourteen rows. All corrected: `brene-brown`, `gabor-mate`, `rene-descartes`, `soren-kierkegaard`, `niccolo-machiavelli`, `pema-chodron`, `clarissa-pinkola-estes`, `antoine-de-saint-exupery`. **This now matters more than it did an hour ago**, because those slugs ship in `author_slug` and are what the book note author link is built from. **Worth your eye:** `achology_book_author_photo()` resolves a portrait from the slug, so if any portrait file was ever named to an old slug it will stop resolving. We believe none exists yet. Confirm.
- Both instructor book notes are drafted, gated and written into the master's `post_content`: The Skilled Helper and The Ultimate Life Coaching Handbook. They are the first two of the 601 to carry a body.

*No em or en dashes in this file; checked before writing.*
