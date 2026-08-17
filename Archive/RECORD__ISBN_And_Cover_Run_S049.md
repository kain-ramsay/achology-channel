# RECORD: the ISBN, Amazon URL and cover run, complete over all 620 rows

**From:** Claude Code, S049. **Date:** 2026-08-06.
**Answers:** `COMMISSION__ISBN_Amazon_URL_And_Cover_Collection_Run_S250.md`, all of it.
**Misses list:** `MISSES__ISBN_And_Cover_Run_S049.md`, filed beside this.

## The one-screen summary

```
rows processed                620
ISBNs resolved                579   (93%)   Open Library first, Google Books fallback
Amazon URLs derived           579   (93%)   plain amazon.com/dp/{ISBN10}, no tag
  verified as live product      55           Amazon answered the check
  check refused by Amazon      522           challenge page, NOT a miss, see below
  dead                           2
covers saved                  556   (90%)
  high resolution, Apple Books 512   (83%)   900 to 2000px, median 2000
  low resolution fallback       44   ( 7%)   Open Library, about 500px
no usable cover                 64   (10%)   41 no ISBN, 18 no cover found, 5 too small
```

Every cover is named by the book's `post_name`, so a row and its file are paired without anybody matching titles by hand.

## The cover source changed mid-run, on Kain's instruction

The commission named Open Library. I ran it, and after the first 189 covers **Kain looked at them and said they were too low resolution.** He was right, and measuring proved it rather than his eye and mine disagreeing: Open Library, Google Books and Amazon's own image host **all cap at roughly 500px on the long edge**, tested across six titles. DSRD 8 §20.5 renders the cover at 288px wide, so 500px is barely 1x on any modern screen and visibly soft.

He then said he was sure a free high-resolution source existed. He was right about that too.

**Apple Books, through the public iTunes Search API.** No key, no account, no scraping, no cost. Apple publishes the artwork size inside the image URL, so the 100px thumbnail it advertises can simply be asked for at 2000: `.../100x100bb.jpg` becomes `.../2000x2000bb.jpg`. That is Apple's own documented URL shape, not a trick, and it returns **four times the height** of anything the other three sources hold.

The run was stopped, the cover step rewritten, and every row redone. The ISBN and Amazon work from the first pass was kept, because the identification had not changed, only where the picture comes from.

**One risk this introduced, and how it is handled.** Apple matches on words, not on ISBN, so an unchecked match is exactly how the wrong book's cover ends up on a page and nobody notices for a year. Every result is therefore checked back against the expected title and author before the file is kept, and anything that fails the check falls through to Open Library rather than being accepted. That check is why 44 rows carry a low-resolution fallback instead of a wrong picture.

## The Amazon verification, reported honestly

The commission says a dead or redirected-to-search URL counts as a miss. **522 of 579 could not be checked at all**, because Amazon answers scripted requests with a challenge page. That is not the same as the URL being wrong, and calling it a miss would have put 522 perfectly good rows on your hand-work list and buried the two that are genuinely dead.

So `blocked` is recorded as its own state. What it means: the URL is correctly formed from a real ISBN-10, and Amazon's product endpoint could not be reached to confirm it resolves. The 55 that did answer all resolved to real product pages, which is decent evidence the derivation is sound.

**The two dead ones are in the misses list** and are the only Amazon rows needing a human.

## The column contract consequence you asked about

`book_cover_image` is now a required field on the Book Note page (DSRD 8 §20.2: a missing cover blocks the page, never a rendered fallback). **64 rows have no usable cover.** Those 64 books cannot publish until somebody supplies one by hand, and that is the real deliverable of this run: the misses list is a work list, not a log.

Three of the four columns are new to the master: `isbn`, `amazon_url` and `cover_status`. `book_cover_image` already existed in the S044 contract and is now filled. **The upload CSV's 15 contract columns are unchanged**, so nothing about the importer moves; `cover_status` is a production column for you and Kain, not a field the page reads.

## What was written, and what was preserved

`Book_Note_Master.xlsx`, in place, under its own canonical name:

- 620 rows written, 0 rows unmatched. Row order and all 30 original columns untouched.
- Both sheets preserved, including `Read Me First`, which now carries a v5 note describing this change.
- The superseded file is in `Archive/` as `Book_Note_Master__superseded_S049_pre_isbn_run.xlsx`, per the one-master-one-filename rule.
- Read back after saving: 33 columns, 620 data rows, both sheets present.

The covers are in `Book Cover Images/` beside the master. That folder is new and is now on the project folder map.

## Closed at S050: verified against the folder, and three things finished

This record was written at the end of S049 and its numbers were taken on trust at the open of S050. They were checked against the workbook and the image folder rather than against this file, and they hold: 620 rows, 33 columns, 512 `ok`, 44 `low_res`, 41 `no_isbn`, 18 `missing`, 5 `low_quality`. Every one of the 556 saved images opens, none is under 400px on its long edge, the smallest is exactly 400 and the median is 2000.

Three things the run had left open are now closed.

**One, the misses list is filed.** `MISSES__ISBN_And_Cover_Run_S049.md`, beside this file. This record named it at S049 but it was never written, so the run's actual deliverable, the hand-work list, did not exist. It does now: 108 rows in four parts, plus the two dead Amazon URLs.

**Two, eleven dead cover filenames are cleared.** Eleven rows whose `cover_status` is a miss still carried a legacy `cover_Title_by_Author.png` name from the S044 contract data, and not one of those files exists anywhere on disk. The commission's contract for that column is "The saved cover filename, or blank on a miss", so they are blank. Without this, eleven books would have looked covered and failed at import. The affected slugs: `the-history-of-philosophy`, `the-social-animal-aronson`, `the-perennial-philosophy`, `the-nature-of-prejudice`, `the-psychology-of-intelligence`, `the-archetypes-and-the-collective-unconscious`, `the-stranger`, `existentialism-is-a-humanism`, `make-your-bed`, `the-book-of-joy`, `counseling-the-culturally-diverse`.

**Three, the upload CSV is regenerated.** The folder Read Me says of it: "Regenerated from the master whenever the master changes; never edited by hand." It had not been, so it still carried the 136 legacy cover filenames from before the run. It now carries the run's real ones on 556 rows, on the same 15 contract columns, 620 rows, slug order identical to the master.

The master was archived before the change as `Book_Note_Master__superseded_S050_pre_blank_fix.xlsx`, and its Read Me sheet carries a v6 note. The v5 note had been appended at the foot of that sheet, against its own newest-first convention, so it was lifted into place under v6.

## The one thing I did not decide

`cover_status` carries `low_res` on 44 rows. The commission's contract permits four values and that is not one of them. Those rows do hold a usable cover, so the value is telling the truth and is useful, but adding a fifth state to a column contract is not mine to do. It is in the misses list as an open question: fold the 44 into `ok`, or register `low_res`. Either answer is a one-minute correction.

*No em or en dashes in this file; checked before writing.*
