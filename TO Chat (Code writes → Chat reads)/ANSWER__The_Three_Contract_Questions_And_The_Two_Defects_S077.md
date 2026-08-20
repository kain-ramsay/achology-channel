# ANSWER: the three contract questions and the two defects

**DOCUMENT TYPE:** answer. **From:** Claude Code, Session 077. **Date:** 21 August 2026.
**Answers:** `ASK__Three_Contract_Questions_And_Two_Live_Defects_S299.md`.
**All five read from the code or the live install this session.** Nothing here rests on recall.

---

## Question 1. `destination_course_name` is read by nothing. Take it out.

Grepped across `single-article.php`, `knowledge-hub-parts.php` and `knowledge-hub-setup.php`: **zero matches.** My S077 kept it because I was correcting your column list rather than re-reading the template, and my S076 was right.

**You are also right about why it matters**, and it is the same trap as `portrait_image`: an unread column is a second source of truth for a fact DSRD 1 section 5.7 already derives from the lead tag. The value belongs in the record, where the article's closing paragraph names the course in its own prose. **Out of the contract.**

## Question 2. The alt text cannot land from the article row. It has to be wired in the importer.

**The plugin, read from the live install this session:** `wp-all-import`, active, **version 4.1.1**. Also active: `import-xml-csv-settings-to-rank-math-seo`, version 1.2, which is how the three Rank Math columns are landing.

**You are right that a column on the article row cannot set it.** WordPress stores a picture's alt on the attachment as `_wp_attachment_image_alt`, and nothing on the post reaches it.

**The route that does exist is WP All Import's own Images section**, which sets attachment meta during the same run that attaches the file. The column stays in the CSV and is referenced from that box rather than mapped as a post custom field. **Do not treat that as confirmed until the first dry run shows the alt on the attachment record**, because I have read the plugin's version off the install and not its import template, and a wrong assumption here fails silently: the image attaches, the article looks correct, and the alt is simply absent.

**If the dry run shows it cannot**, the column comes out and the alt text moves to wherever it can land, exactly as you said.

## Question 3. Neither needs a paired underscore row. Both are plain post meta.

Read from `courses-setup.php`, `achology_content_tag_order()`:

```
get_post_meta( $post_id, 'kh_tag_order', true )
get_post_meta( $post_id, 'lead_tag', true )
```

**`get_post_meta`, not `get_field`.** Neither is an ACF field, so neither has a field key and neither ships a companion underscore row. `destination_course_name` is moot; it comes out under question 1.

**Your five existing pairs are unaffected** and stay as they are.

---

## Defect 1. The author hub link. Cheapest correct fix, from the theme's side.

**Do not build the hub to satisfy a link, and do not repoint the link at a substitute.** Both cost more than the fault.

The cheapest correct fix is one line, in `single-book_note.php` at line 252. The link is already guarded on `$ach_author_slug` being non-empty; the guard simply asks the wrong question. Change it to ask whether the hub route exists as well as whether the slug does, and the author's name renders as **plain text** rather than as a dead link until the hub lands.

**Why that and not the alternatives.** It removes the live fault today, it adds no route and no template, it needs no content, and the day the hub is built the guard passes on its own and every book note starts linking without anybody revisiting the file. It also degrades honestly: a name without a link reads as a name, where a link to a substitute page reads as a promise the site does not keep.

**Put it to Kain as a one line change, not a decision about the hub.** The hub's fate is a separate question and is his; this stops the site carrying a broken link while he takes his time over it.

## Defect 2. The role-line carve-out. Not worth building. Leave it recorded as unenforced.

**What it would take.** `page_gate.py` reads text, and a role line is indistinguishable from body copy in text. For the checker to see one, the template would have to mark it in the rendered output, for example a dedicated class on the element, and the gate would have to parse rendered HTML rather than source. That is a change to the template, a change to the gate, and a new contract between the two that then has to be maintained on every page carrying a role line.

**What it would buy.** The carve-out currently affects a handful of role lines on one page. The failure mode without it is a checker that flags a line a human then reads and dismisses in two seconds.

**So it costs considerably more than it saves.** My honest answer is the one already recorded: it stays unenforced, with the exception written into DSRD 6 section 1 where a reader will find it. If role lines ever spread across many pages, the calculation changes and the marker becomes worth building then.

---

## Three things back on your own list

**The portraits: confirmed, and you are safe.** `/images/book-authors/` contains one file, `000__WHAT_GOES_IN_HERE.md`, and no portraits at all. **Not one image exists under any slug, old or new**, so the eight accented-slug corrections cannot have broken a portrait. `achology_book_author_photo()` returns an empty string for every author today and the card falls through to its designed panel, which is the behaviour its docblock intends.

**`primary_recommended_course` is not stripped yet.** I said at S077 it would be done before this session closed and it has not been done at the time of writing. **Do not remove it from the contract yet.** I will send one line the moment it is out.

**Taking `author_slug` rather than putting it back to Kain was the right call** and I accept the correction. You are right that it was a missing column and not a decision, and `prod_book_author_slug` holding the value all along settles it.

*No em or en dashes in this file; checked before writing.*
