# Job 10: the repair order, from the DSRD 6 records (read only)

Repository state: `kain-ramsay/achology-record` at `main` fetched fresh, commit `1e91422`. Nothing in the records was changed.

## Summary

- 847 `DSRD6_RECORD.md` files under `03. Achology Website Pages`. 623 of them list at least one failing chapter in their "Machine half, written by Code" section; 215 list none; 19 have no usable machine half (see Notes).
- Failing chapter counts, from the machine half: §1 425, §2 7, §3 42, §5 94, §7 11, §10 310, §11 119. §4, §6, §8, §9 never appear in the machine half.
- 299 of the 310 §10 failures are one message on one page type: every Help Answer fails the same boundary (`help-single__body | help-helpful`, no hairline, gap 32.0px).
- §1 (acronym used before being spelled out) fails 425 records, the second biggest block: 181 Articles, 172 Help Answers, 63 Book Notes, 1 Instructor Article and 8 single-page records.
- §5 and §11 are mostly the same finding twice: an internal link that returns 404 (or 301 for Help Answers) on the page's own links.

## How the counts were made

- A record counts as failing chapter N when its "Machine half, written by Code" section has a line `- §N: machine half FAILS. ...`. That section only ever lists §1, §2, §3, §5, §7, §10 and §11, the chapters with a machine runner, so nothing can be said about §4, §6, §8 and §9 from it. See Notes for the chapter table.
- Page type is the folder the record sits in. Under `DSRD 6 Records (pages with no design folder yet)` that is the subfolder (Articles, Help Answers, Book Notes, Instructor Articles, and single pages such as Privacy Policy); elsewhere it is the page's own design folder (for example Quote Page, FAQ Category Page). The 29 records outside the four big types are one record per folder, so each is its own page type.
- The message quoted for each failing chapter is the text after "N of M checks failed." on that line. That line carries one message only, even where more than one check failed (for example §10 on a Help Answer says "6 of 29 checks failed" or "9 of 35 checks failed" but quotes one boundary). The other failed checks are not named in the record: cannot tell from the records what they are.

## Failing records by chapter and page type

| Chapter | All | Articles (351) | Help Answers (299) | Book Notes (150) | Instructor Articles (18) | Other single-page records (29) |
|---|---|---|---|---|---|---|
| §1 Copy standards | 425 | 181 | 172 | 63 | 1 | 8 |
| §2 Page structure and headings | 7 | 0 | 0 | 0 | 0 | 7 |
| §3 Metadata and preview data | 42 | 3 | 16 | 18 | 0 | 5 |
| §5 Search visibility | 94 | 36 | 31 | 24 | 0 | 3 |
| §7 Accessibility | 11 | 1 | 0 | 0 | 0 | 10 |
| §10 Visual consistency | 310 | 1 | 299 | 0 | 0 | 10 |
| §11 Verification on the live page | 119 | 47 | 31 | 25 | 0 | 16 |

Other single-page records failing each chapter: 
- §1: Book Note Page, Cards, FAQ Article Page, FAQ Category Page, Instructors, Listing Page, Taxonomy Kh Category, Verified Student Reviews Page
- §2: (03 folder root: 404.php), About Landing Page, Book Note Page, Cards, Pricing Page, Verified Student Reviews Page, Video Testimonials Page
- §3: (03 folder root: 404.php), FAQ Category Page, Single Article, Single Faq Article, Taxonomy Kh Category
- §5: Instructors, Listing Page, Taxonomy Kh Category
- §7: Cards, FAQ Article Page, FAQ Category Page, Listing Page, Single Article, Single Faq Article, Taxonomy Kh Category, Template Author Profile, Verified Student Reviews Page, Video Testimonials Page
- §10: (03 folder root: 404.php), Book Note Page, FAQ Article Page, FAQ Category Page, Instructors, Listing Page, Quote Page, Single Faq Article, Taxonomy Kh Category, Template Author Profile
- §11: (03 folder root: 404.php), Accessibility Statement, Code of Ethics Page, Disclaimers, FAQ Article Page, FAQ Category Page, Founders Letter Page, Listing Page, Manifesto Page, Policy Page, Privacy Policy, Refund Policy, Single Faq Article, Taxonomy Kh Category, Terms And Conditions, Trust Statement

## The ten chapter-and-page-type groups with the most failing records

Ranked by failing records. §5 Help Answers and §11 Help Answers tie at 31 and share rank 7. The next group down is §3 Book Notes at 18, then §3 Help Answers at 16.

| Rank | Group | Failing records | Share of that page type | Most common single message, and how many records carry it |
|---|---|---|---|---|
| 1 | §10 Visual consistency, Help Answers | 299 | 100% of 299 | `desktop boundary 4 (help-single__body \| help-helpful): no hairline, gap 32.0px`: 299 of 299 |
| 2 | §1 Copy standards, Articles | 181 | 51% of 351 | No exact message is carried by more than 3 record(s) (each carries its own acronym and context). All 181 carry the same kind: "N acronym(s) used before being spelled out: X (…context…)". Most common first-listed acronym: NLP (23 records). Most common exact message (3): `1 acronym used before being spelled out: GROW (…oach yourself, and how would you begin? What are the main life…` |
| 3 | §1 Copy standards, Help Answers | 172 | 57% of 299 | No exact message is carried by more than 7 record(s) (each carries its own acronym and context). All 172 carry the same kind: "N acronym(s) used before being spelled out: X (…context…)". Most common first-listed acronym: CBT (27 records). Most common exact message (7): `1 acronym used before being spelled out: RSVP (…How do I join a live Achology community event? Open Upcoming E…` |
| 4 | §1 Copy standards, Book Notes | 63 | 42% of 150 | No exact message is carried by more than 1 record(s) (each carries its own acronym and context). All 63 carry the same kind: "N acronym(s) used before being spelled out: X (…context…)". Most common first-listed acronym: TED (5 records). Most common exact message (1): `3 acronyms used before being spelled out: TED (…logy Book Notes How to Fix a Broken Heart by Guy Winch: Summar…` |
| 5 | §11 Verification on the live page, Articles | 47 | 13% of 351 | Kind: internal link(s) return HTTP 404: 29 of 47. Most common exact message (4): `/learn/psychology/articles/can-people-change/ (404)`. Also: complianz.min.js?ver=1790768460 -> 502 (2) |
| 6 | §5 Search visibility, Articles | 36 | 10% of 351 | Kind: internal link(s) return HTTP 404: 30 of 36. Most common exact message (4): `/learn/psychology/articles/can-people-change/ (404)`. Also: 2 workbook rows point here; the chain is broken at dest_built, dest_in (2); 1 workbook rows point here; the chain is broken at dest_built, dest_in (2) |
| 7 | §5 Search visibility, Help Answers | 31 | 10% of 299 | Kind: internal link(s) return HTTP 404: 16 of 31. Most common exact message (12): `/help/getting-started/become-a-life-coach/ (301)`. Also: internal link(s) return HTTP 301 (12); internal link(s) return HTTP 301/404 (3) |
| 7 | §11 Verification on the live page, Help Answers | 31 | 10% of 299 | Kind: internal link(s) return HTTP 404: 16 of 31. Most common exact message (12): `/help/getting-started/become-a-life-coach/ (301)`. Also: internal link(s) return HTTP 301 (12); internal link(s) return HTTP 301/404 (3) |
| 9 | §11 Verification on the live page, Book Notes | 25 | 16% of 150 | Kind: internal link(s) return HTTP 404: 23 of 25. Most common exact message (2): `/learn/psychology/articles/can-people-change/ (404)` |
| 10 | §5 Search visibility, Book Notes | 24 | 16% of 150 | Kind: internal link(s) return HTTP 404: 23 of 24. Most common exact message (2): `/learn/psychology/articles/can-people-change/ (404)` |

Message wording is quoted from the records. For the link groups (§5, §11) the same broken addresses recur across groups: `/help/getting-started/become-a-life-coach/` returns 301 on 12 Help Answers (in both §5 and §11); `/learn/psychology/articles/can-people-change/` returns 404 on 6 records (both chapters); `/learn/psychology/articles/sense-of-purpose/` and `/learn/psychology/articles/change-your-life-from-the-inside-out/` 404 on 4 each. All counts are of records, taken from the machine half.

## The twenty records failing the most chapters

Records by number of failing chapters (machine half): 0: 224, 1: 344, 2: 204, 3: 48, 4: 24, 5: 2, 6: 1. Ranked by chapters failing, then by the total of "N of M checks failed" across those chapters, then by name. 24 records fail four chapters, so the cut at twenty falls inside that tie; the 7 four-chapter records below the cut are listed after the table.

| # | Page type | Record | Chapters failing | Total failed checks |
|---|---|---|---|---|
| 1 | Taxonomy Kh Category | `Taxonomy Kh Category` | §1, §3, §5, §7, §10, §11 | 23 |
| 2 | Listing Page | `Listing Page` | §1, §5, §7, §10, §11 | 17 |
| 3 | FAQ Category Page | `FAQ Category Page` | §1, §3, §7, §10, §11 | 10 |
| 4 | Single Faq Article | `Single Faq Article` | §3, §7, §10, §11 | 16 |
| 5 | FAQ Article Page | `FAQ Article Page` | §1, §7, §10, §11 | 14 |
| 6 | Help Answers | `albert-ellis-course` | §1, §5, §10, §11 | 12 |
| 7 | Help Answers | `become-a-certified-life-coach` | §1, §5, §10, §11 | 12 |
| 8 | Help Answers | `become-a-life-coach-for-free` | §1, §5, §10, §11 | 12 |
| 9 | Help Answers | `can-life-coaches-use-cbt` | §1, §5, §10, §11 | 12 |
| 10 | Help Answers | `choose-a-good-life-coaching-course` | §1, §5, §10, §11 | 12 |
| 11 | Help Answers | `how-much-do-cbt-therapists-earn` | §1, §5, §10, §11 | 12 |
| 12 | Help Answers | `how-to-become-a-cbt-coach` | §1, §5, §10, §11 | 12 |
| 13 | Help Answers | `how-to-become-a-cbt-therapist` | §1, §5, §10, §11 | 12 |
| 14 | Help Answers | `is-a-life-coaching-certification-worth-it` | §1, §5, §10, §11 | 12 |
| 15 | Help Answers | `learn-cbt-for-free` | §1, §5, §10, §11 | 12 |
| 16 | Help Answers | `life-coaching-as-a-career` | §1, §5, §10, §11 | 12 |
| 17 | Help Answers | `life-coaching-certification-online` | §1, §5, §10, §11 | 12 |
| 18 | Help Answers | `nhs-routes-into-cbt` | §1, §5, §10, §11 | 12 |
| 19 | Help Answers | `nlp-certification-free` | §1, §5, §10, §11 | 12 |
| 20 | Help Answers | `train-in-nlp-and-hypnosis-together` | §1, §5, §10, §11 | 12 |

Four-chapter records below the cut (page type, record, chapters, total failed checks): Help Answers `what-is-an-nlp-coach` §1,§5,§10,§11 (12); Help Answers `will-life-coaches-be-replaced-by-ai` §1,§5,§10,§11 (12); (03 folder root: 404.php) `404.php` §2,§3,§10,§11 (9); Help Answers `accredited-nlp-certification` §1,§5,§10,§11 (9); Help Answers `is-life-coaching-regulated` §1,§5,§10,§11 (9); Help Answers `is-nlp-certification-legit` §1,§5,§10,§11 (9); Articles `gerard-egan` §1,§3,§5,§11 (4).

In the table, five are single-page records (Taxonomy Kh Category with 6 chapters; Listing Page and FAQ Category Page with 5; Single Faq Article and FAQ Article Page with 4) and fifteen are Help Answers. Every Help Answer in the table fails the same four chapters: §1, §5, §10, §11.

## Notes and limits

- 19 records have no usable machine half: 7 Articles (no "Machine half" section) and 12 single-page records (policy pages, How We Write, Code of Ethics, Manifesto, Founders Letter, Courses Directory, where lines read "no machine check ran" or the section is missing). They count as no failures in the tables above, which is not the same as passing.
- The chapter table in each record (the `State` column) is a second source. It mostly agrees with the machine half (§1 427 against 425, §3 42, §5 93 against 94, §7 11, §10 311 against 310, §11 120 against 119, §2 7) but also carries fails the machine half cannot show: §6 on 2 records, §8 on 2, §9 on 1, and older dated fails on some single-page records. Where the two differ the tables above follow the machine half, as asked.
- A machine fail line is evidence, not a verdict (the records' own rule, ruled S267): reproduce on a single-page run before acting on any of it.
- Run dates: 803 records carry a machine run of 2026-10-01 and 25 of 2026-10-04; 9 carry no run line; 10 carry an older run (2026-08-14 to 2026-09-24). The older ones may no longer match the live pages.
- Nothing was rewritten. The scripts that produced these counts are in `cloud-reports/job10-method/` (`parse.py` reads the records, `analyse2.py` and `gen.py` count and write this file); they read the records and write only this report.
