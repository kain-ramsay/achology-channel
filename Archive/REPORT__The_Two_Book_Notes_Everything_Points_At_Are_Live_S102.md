> **CHAT DISPOSITION, S343: ARCHIVED.** Recorded on the Book Notes card: 67 published, not 65. The one thing owed (the exact keyword phrase in both openings) is briefed to Cowork as `ADDENDUM__Two_Book_Note_Openings_And_Article_Sections_Are_H2_S343` in TO Cowork. Code re-pushes when that DONE lands.

# REPORT: the two book notes everything points at are live, The Skilled Helper and The Ultimate Life Coaching Handbook

**From:** Claude Code, Session 102. **Date:** 5 September 2026, late evening.
**On Kain's word, in the sitting,** to "Shall I put the two book notes in now?": *"yes, please do Claude!"*. Filed under the Publish Ready Pipeline, stages 5 to 7, and the publishing wall.
**Answers, in part:** the OWED BACK of `REPORT_AND_ASK__The_Hub_Content_Backlog_Read_Tonight_And_34_Canva_Rows_Wanted_S102.md`, section 4 row 3.
**Board cards:** Book Notes, the psychologist expansion; the eighteen instructor articles; the quote pages.

## 1. What is live

| Page | Post | Headline | Rank Math title | Keyword | Rating | Score |
|---|---|---|---|---|---|---|
| /learn/helping-people/book-notes/the-skilled-helper/ | 35418 | The Skilled Helper: Summary and Key Ideas | The Skilled Helper: Summary and Key Ideas \| Achology (52) | the skilled helper | Essential Reading (badge shows) | 81 |
| /learn/helping-people/book-notes/the-ultimate-life-coaching-handbook/ | 35419 | The Ultimate Life Coaching Handbook: Summary and Key Ideas | The Ultimate Life Coaching Handbook: Summary and Key Ideas (58, tier two) | the ultimate life coaching handbook | Highly Recommended | 68 |

Both answer 200, both carry their cover (attachment ids 35415 and 35417, written into `book_cover_image` by `book_covers.py` through the importer), both read back from the install field by field. 67 book notes are now published. The fifteen instructor-article links and the 25 quote records' `source_book_reference` that pointed at these two addresses now resolve.

## 2. How they went in

Records first: the two records sat outside the S310 agreed 64, so `book_note_import.py --plan/--write/--push/--verify --slugs` ran on them alone. Before the write, three record fields were brought to the rulings already applied to the other 65 tonight and this afternoon: `post_title` to Kain's headline pattern, `prod_rm_seo_title` to his title pattern (the handbook's at tier two, 58 characters), and The Skilled Helper's keyword from `the skilled helper book summary` to `the skilled helper`, Chat's S341 rule as Cowork applied it to the 65 at S338 (record commit `3c49a60`). The master's protect-approved-values rule needed `--overwrite-columns post_title,prod_rm_seo_title,prod_rm_focus_keyword` to take them. Then the drafts, then publish clearance `f2836168f6c43a23` (both refused on the draft's 404, the S096 override route, Kain's words recorded), then `wp post update --post_status=publish` in one command, purge, and the page gate and the scorer on the live pages.

**One fault in the importer, fixed tonight (section 4):** its live lookup before a push read published posts only, so the second push (the one carrying the corrected titles) created two new drafts instead of updating the first pair. The first pair (35414, 35416, never public) was trashed under takedown clearance `17914dae264aff28` before publishing, so the addresses are clean.

## 3. What the scores say, and whose the fixes are

- **The Skilled Helper 81, The Ultimate Life Coaching Handbook 68.** Both under the 85 the other 65 reach, for one reason the gate names: keyword density. "the skilled helper" appears once in 1160 words; "the ultimate life coaching handbook" appears nowhere in its 1134 words (the body says "the handbook"). The 65 reached 85 when Cowork put the exact phrase into each opening at S338 (`RULING__The_Book_Note_Keeps_The_Exact_Phrase_S338`). The same one-sentence edit on these two records, and a re-push, is the whole distance; Cowork's, and a natural addendum to the stage 0 run already commissioned on the 65.
- **The covers are over the book-cover budget** (598.8KB and 120.7KB against 60KB) and ship as JPG, like the other 65: the cover run through the pipeline's book-cover slot, named in the v0.167.25 file, is the fix; Code's tooling.
- The remaining gate lines are the template's own, known from the S102 section 32 comparison (hero boundaries, breadcrumb rows, the H1 line), and the DSRD 6 record line, which the Book Note Page record covers for the template.

## 4. The importer fix

`tools/book_note_import.py`: the pre-push lookup now reads every status, so a second push updates a draft instead of duplicating it. Hash re-registered in `harness/h9_reviewed_scripts.json`. Named in the theme commit.

OWED BACK: the two opening sentences carrying the exact phrase (section 3, Cowork's, relayed by you); nothing else.

*No em or en dashes in this file; checked before writing.*
