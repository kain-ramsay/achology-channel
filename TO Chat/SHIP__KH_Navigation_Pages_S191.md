**For Chat. What this needs from you:** read the proofs below and mark the Knowledge Hub Nav pages card's seven jobs (T1, T2, T10 to T14) against them; re-read chapters 1 and 7 of the tag page record, whose fails these jobs answer.

# SHIP: Knowledge Hub navigation pages, brief S448 jobs T1, T2, T10 to T14 (Code S191, theme)

**Version 0.707.636**, deployed 27 October 2026 from a clean copy of origin/main (commit 3d7c21ea). Server, local and zip agree (deploy.py's three proofs); the zip is copied to `../achology.zip`.

## What changed and the proof, job by job

**T1, tag pages in the sitemap.** Rank Math sitemap: `tax_kh_tag_sitemap` on, and `tax_kh_tag_include_empty` on, so learn-hypnotherapy is listed too. Read back live: `sitemap_index.xml` now lists `kh_tag-sitemap.xml`, which holds 36 addresses, all 36 tag pages. **Flag:** learn-hypnotherapy has no published page of any kind; its tag page answers 200 with its banner, counters and courses only. Listed because the done test asks for all 36; say if it should wait until it holds a page. **Workbook:** `pt_workbook_sitemap` stays off: no workbook is published, so there is nothing to list. Switch it on with the first published workbook.

**T2, the 36 search titles and focus keywords.** Set on each `kh_tag` term, word for word from RULING__The_36_Tag_Page_Search_Titles_And_Focus_Keywords_S448 (`rank_math_title`, `rank_math_focus_keyword`), parsed from the ruling's table by machine, no hand typing. Read back from the served page source one by one: **36 of 36 titles match the ruling exactly, none reads "Archives"**, and Open Graph titles match too. Focus keyword answer: **Rank Math keeps the focus keyword on a taxonomy term**; all 36 read back from the term meta, 36 of 36 exact. The 144 view-all pages are untouched: /learn/tags/build-confidence/articles/ still reads "Articles on Build Confidence | Achology TEST Site", follow, noindex. Descriptions untouched.

**T10, focus never under the pinned bars (WCAG 2.4.11).** Measured first: the header and the pinned bars end at 145 at 834 and 1280, and at 137 on phones, while the scroll stop was 80. kh-tag.css now sets the scroll stop to 153 on pages that carry the pinned bar (`html:has(.tgp-live)`), so no other page changes. Proof in WebKit at 320, 375, 390, 834 and 1280: tabbing 140 stops down /learn/tags/build-confidence/ and shift-tabbing 140 back up, **0 of 280 focus stops covered** at every width.

**T11, course card stats whole (WCAG 1.4.10).** cards.css: below 768 wide the shared course card's stats line may wrap, each stat staying whole; nothing changes at tablet or desktop. Measured in WebKit: before, the third stat ran 26 past the card edge at 320; now every stat ends inside the card at 320 (40 clear), 375 and 390, and the row is the same single line at 834 and 1280 as before. The style gate shows no new line on either stylesheet (kh-tag.css 39 before and after, cards.css 47 before and after, all old).

**T12, the pause link named.** taxonomy-kh_tag.php: the link keeps its visible words and gains the name "Read This Quote Article: {the quote article's title}". Read live: "Read This Quote Article: Two Signs of Low Self-Esteem Worth Telling Apart".

**T13, no more guessed pages.** functions.php switches off WordPress's guess redirect site-wide (`do_redirect_guess_404_permalink`). Read live: /academy/personal-growth/, /people/ and /courses/life-coaching/ each answer **404**. Every redirect set on purpose still works: **51 of 51** active Rank Math redirects answer 301 to their own target, probed one by one. redirect_one_hop.py: **0 faults across 2595 rows**.

**T14, "delve".** taxonomy-kh_tag.php and knowledge-hub-parts.php: "ready to delve into human psychology" becomes "ready to go deeper into human psychology". Read live on /learn/tags/build-confidence/ and /learn/personal-growth/: the new words show, no "delve". No theme file carries "delve" outside the quoted reviews (data/reviews.csv.php, left alone as the brief says).

## The two checks re-run

See SESSION_REPORT__S191 for the tag page record and chain register results.

## Reach

T11 lands everywhere the shared course card appears below tablet width (Courses page, tag pages, any page with the card). T13 is site-wide by design. T10 and T12 are tag pages only. **Reach line for Chat:** R2 of BRIEF__Page_Readiness_Reader_Halves_Fixes_For_Code_S448 widens T10 to the subject bar; the same one-line pattern in kh-subject.css would cover it, for the next theme session.

*No em or en dashes in this file; checked before writing.*
