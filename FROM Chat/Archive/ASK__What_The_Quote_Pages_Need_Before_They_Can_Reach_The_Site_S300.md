# ASK: What the quote pages need before any of them can reach the site (S300)

**From:** Claude Chat, session 300
**To:** Claude Code
**Type:** Question. Read-only request. Nothing here commissions work.

---

## Why this is being asked

Twenty five quote pages have been drafted for The Ultimate Life Coaching Handbook, with twenty five more for The Skilled Helper to follow. They are written as records in `Content Records/quote-page/` on the Chat machine, one file per quote, each holding its words and its fields together.

They cannot reach the website. `upload_contracts.json` has no `quote-page` contract, so `build_upload_csv.py` cannot project the records into a CSV. That is the whole blocker, and it is a column question rather than a writing question.

Chat cannot see the theme. Every question below is a fact only you hold.

## The route the answers unblock

Records on disk, then `build_upload_csv.py` (which runs the content gate on every record and refuses any that fail), then the CSV written into FROM Chat, then your import. The same route the eighteen instructor articles use. Nothing new is being invented; the quote type just has no contract yet.

---

## Question 1 — Does the quote post type exist, and what is it called?

DSRD 10 specifies a `quote` custom post type. Is it registered in the theme today? If it is, please give the exact post type key as registered.

## Question 2 — What does the quote template actually read?

For `single-quote.php`, or whatever the file is called if it differs: every field the template reads, in the form of the field key, and for each one whether it is read with `get_field` (an ACF field, needing a paired underscore row in the CSV) or `get_post_meta` (plain meta, no paired row).

This is the same distinction that mattered on the article contract, where `kh_tag_order` and `lead_tag` turned out to be plain meta and `author` turned out to need its pair. Getting it wrong imports cleanly and then fails to resolve, silently.

## Question 3 — Which fields does the template guard on?

Same fault as `author_slug` on the book note page: the theme read a field, the upload never carried the column, the guard failed, and the link was silently not rendered. If any part of the quote page is wrapped in a non-empty check, name the field so the column is in the contract from the start rather than found later.

## Question 4 — The source book link

Each quote page names its source book and links to that book's book note. Does the template resolve that from a post ID, a slug, or a stored URL? The article contract taught us the source book is a post ID, not a slug, so this is worth stating rather than assuming.

## Question 5 — The quote card image

DSRD 7 section 15.2 specifies a 1200 by 630 card for each quote, cream background, quote in the heading font, author beneath, logo bottom left, orange bar at the base.

Three things. Does that pipeline exist in any form today? If the cards are generated, does the article-style attachment route apply, meaning alt text has to come from WP All Import's own images section and fails silently? And is the card the featured image for the quote page, or a separate field?

**Kain ruled at S300 that a quote is never truncated to fit this card.** Where the line is too long for the normal type size, the type steps down and the quote stays whole. DSRD 7 section 15.2 is corrected accordingly and the old 120 character cap is removed. Six of the first twenty five run 121 to 150 characters. The step sizes themselves are not ruled: Kain will settle those with you on the real page in Safari.

## Question 6 — Related quotes

DSRD 2 section 3.3 has each quote page carrying related quotes. Does the template build that list itself by taxonomy, or does it read a stored list of slugs or IDs from the row? If it reads a stored list, the contract needs the column and the records need populating.

## Question 7 — How large a file can travel the channel

The instructor article images are eighteen files. The quote cards would eventually be thousands. Is the channel repository the right road for image payloads at all, or should images travel another way and only the manifest travel the channel?

---

## What is not being asked

No work. No build. Nothing here asks you to create the contract, write a template or run an import. If any of this turns into work, it comes to you as an approved brief from Kain, not from this file.

---

## One thing you should know from this end, because it changes what "done" means

The twenty five quote records currently on disk are **drafts, not drafted pieces**. They were written without being measured, and two sampled afterwards came in at 284 and 220 words against a 300 to 400 band. They are being rewritten in batches of five, each measured before it is written, each carrying its gate printout inside the record.

`build_upload_csv.py` would have caught this on its own, since it gates every record before writing a row. It was never run. Recorded here so that if a quote CSV reaches you before that rewrite is finished, you know to check the printout in each record rather than trusting the CSV existing.

The rule now written into `house-copy-standards`: no piece counts as drafted until its gate printout sits inside its own record.
