# Job 13: other page types with the same shape of chapter 10 failure (read only, facts only)

Sources: `kain-ramsay/achology-record` `main` `1e91422` (the 847 `DSRD6_RECORD.md` files; job 10's parse of their "Machine half, written by Code" sections, branch `cloud-report/job10-board-failures`) and `page_gate.py` in `kain-ramsay/achology-theme` `origin/main` `2bc5aeb`. Nothing was changed; nothing is recommended.

**The shape.** The gate (`page_gate.py` PROBE and `check_page`) takes the direct children of the page's content container as blocks and measures each adjacent pair. A pair with no line on the facing edges, and none of the gate's named cases (breadcrumb junction, reading bar, `kh-foot__signature`, a boxed card, the About uneven-columns line), is reported as `desktop boundary N (A | B): no hairline, gap Xpx`, which is the shape of `help-single__body | help-helpful`. Block names in the message are the element's class string cut at 26 characters; the gap is the box-to-box distance between the two blocks.

## Result: seven page types, one record each

| Page type (record folder, template) | Block above | Block below | Gap (desktop) | Records | Run in the record, and what else it says |
|---|---|---|---|---|---|
| Listing Page (`learn-listing.php`, /learn/) | `kh-listing__hero` | `kh-controls` | 24.0 px | 1 | 2026-08-24, page_gate v8; 13 of 24 checks failed |
| Taxonomy Kh Category (`taxonomy-kh_category.php`, /learn/{category}/) | `kh-hub__hero` | `kh-pills` | 24.0 px | 1 | 2026-08-24, v8; 18 of 29 failed |
| Template Author Profile (`template-author-profile.php`) | `ap-hero` | `ap-bio` | 48.0 px | 1 | no run line; table dated 2026-08-13; 6 of 17 failed |
| Single Faq Article (`single-faq_article.php`, one article, /help/achology-basics-and-identity/what-is-achology/) | `help-single__header` | `help-divider` | 28.0 px | 1 | 2026-08-24, v8; 13 of 29 failed. The current template has no `help-divider`; the block there is now `ach-listen-bar` (job 12), so this message describes an older layout |
| FAQ Category Page (`taxonomy-faq_category.php`, /help/{category}/) | `help-hero help-hero--categ` (cut; `help-hero help-hero--category`) | `help-articles` | 48.0 px | 1 | 2026-08-24, v8; 6 of 17 failed |
| FAQ Article Page folder (`archive-faq_article.php`, the /help/ landing) | `help-hero help-hero--landi` (cut; `help-hero help-hero--landing`) | `help-group` | 48.0 px | 1 | 2026-08-24, v8; 11 of 26 failed |
| Book Note Page (`single-book_note.php`) | `bn-read` | `kh-foot__signature` | 32.0 px | 1 | 2026-09-05, v9; 9 of 27 failed. See note 1 |

In the message numbering the Book Note pair is boundary 1 and the others boundary 2. Each is the first failing message quoted for chapter 10 in that record. Each of the seven page types has exactly one record, so "records carrying it" is 1 for each; the whole record set (847) has 7 of these plus the 299 help answers. No Article, Book Note, Instructor Article or other help answer record carries this shape.

## Notes on the table

1. **Book Note Page.** The pair `bn-read | kh-foot__signature` is a case the gate now carves out by name: `page_gate.py:1312-1313` reports a no-line boundary whose lower block starts with `kh-foot__signature` as a CARVE-OUT ("the author signature closes the writing above it"), added in commit `b50ebea` (2026-09-28, S136). The record's run (2026-09-05) predates it. Whether this record would still fail on a re-run: cannot tell.
2. **Taxonomy Kh Category.** DSRD 7 §4.3 Exception 3 (category hub, S313) says the boundaries between the hub's five page-level blocks, "its four content type sections and its tag strip", draw no hairline and carry 48 (32 on phones). `kh-hub__hero | kh-pills` is the hero against the tag strip; as written the exception names the four boundaries among the five blocks, and whether it was meant to cover hero-to-strip: cannot tell. The measured gap is 24, not 48. `page_gate.py` has no code naming this exception (no match for `kh-hub` or `S313`); the DSRD says it is recorded "as a named CARVE-OUT row on the category hub's readiness record", and this record's machine half reads `0 recorded carve-outs` under §2.
3. **Listing Page.** DSRD 7 §4.3 says the listing page's hairline between its control bar and its card grid keeps the standard 48/48 and is not covered by Exception 3 (reference to DSRD 9 §21.5). The failing pair here is the hero against the control bar, a different edge.
4. **Gap equal to 48.** Template Author Profile, FAQ Category Page and FAQ Article Page show a gap of 48 with no line. For a boundary with no line the gate does not compare the gap with 48; it fails on the missing line (`page_gate.py:1335-1337`).
5. **Record age.** Six of the seven are v8 runs of 2026-08-24 or older (Template Author Profile's table is 2026-08-13 and has no run line); the gate gained its card-border, reading-bar and signature carve-outs on 2026-09-28 (`b50ebea`) and its measurement changes of 2026-10-04 (`4ca046c`, `7bbb66c`, `2bc5aeb`, which only affect boundaries that have a line). Whether any of the six would now read differently: cannot tell without re-running the gate on the live pages.
6. **Only the first message per chapter is quoted.** Each record names one failing check for chapter 10 ("N of M checks failed"). These page types may carry further no-hairline boundaries that the record does not name: cannot tell. Only the desktop tier is quoted; tablet and phone: cannot tell.

## Chapter 10 failures in other records that are not this shape

| Page type | Message in the record | Why it is not the same shape |
|---|---|---|
| 404.php (record at the `03` folder root) | `desktop boundary 2 (policy-header \| policy-next): 43.0 above, 80.0 below (want 48/48)` | A line is present; the spacing either side is wrong (`hairline-spacing`) |
| Instructors | `desktop boundary 3 (pp-group \| pp-group): 24.0 above, 80.0 below (want 48/48)` (run 2026-10-01) | A line is present; spacing either side is wrong |
| Quote Page | `desktop: 384.3px (want 48)` | The `header-to-content` check (`page_gate.py:1459-1460`), not a block boundary |
| Articles (one record, `what-is-a-saviour-complex`, run 2026-10-04) | `desktop: 950.9px (want 48)` | `header-to-content` |
| Book Note Page, chapter table line | `fail, 2026-08-13, [machine] desktop: 588.8px (want 48)` | `header-to-content` (the table line differs from the machine half quoted above) |
| Courses Directory Page (no machine half; table line 2026-09-29) | `desktop boundary 2 (help-close cd-questions \| help-single__credit cd-cre): 24.0 outside th...` | A boxed card: the gate measures the space outside the card and the record's own text calls it a recorded exception approved by Kain (24 above the UKRLP line) |

Records with no chapter 10 failure in their machine half (all 150 Book Notes, 17 of 18 Instructor Articles, 350 of 351 Articles and the rest) are not listed. 19 records have no usable machine half (job 10, Notes); for those, chapter 10: cannot tell.
