# REPORT: every published article and book note now has a DSRD 6 record, and the board counts against them

**Filed by Claude Code, Session 120. Date:** 16 September 2026. **Session type:** factory.
**Answers:** `BRIEF__Every_Published_Article_And_Book_Note_Gets_A_DSRD_6_Record_S358.md`, sections 3 and 5.
**Not yet answered:** the second half of its OWED BACK line, how many records show failing chapters. That number needs the machine sweep, and the sweep's cost is the one thing in here that needs a decision. It is section 4 below.

---

## 1. The counts the brief asked for, read off the install this session

Published on the install, read this session, not recalled:

- **227 articles**
- **125 book notes**
- **352 content pages in total**

Records after the run:

- **334 created this session**
- **18 already present**, the instructor articles, untouched
- **0 published pages the pass could not reach**
- **0 slug collisions** between a content page and a page design

The board now reports **378 rows owing a record, covering 394 live pages, and none without one**. Before this session it enumerated 26 designs covering 42 pages and reported no page without a record, while 352 published pages had none.

## 2. How the row set was widened, so it cannot go stale again

A third source was added beside WordPress pages (A) and the theme on disk (B): **source C, the install's own published posts of the content types**. The row set is built from the install every run. No list is kept by hand in the script, because a hand list is what caused the gap the brief was raised on.

Adding a content type is one line in the script's own table. Quote pages and help answers are outside the brief and were not added.

Each content record is filed in one container per type, one folder per page, which is the convention already on disk for the eighteen instructor articles. Placement is a convenience: a record is found by its `Page:` line, as DSRD 6 §0 requires.

**Every chapter line in all 334 reads `not run`.** Nothing was measured, so nothing claims to have been. The brief's own rule, section 3 item 2, in its words: "A generated record must never show a pass that was not run".

## 3. What this does not unblock, said plainly

`publish_gate.py`'s volume route needs an exemplar record carrying no failing line. A book note now has a record to point at, which it did not before, but no book note record can be clean until its machine half has run and its human halves are written. So the book note wall is lower than it was and is not gone.

## 4. The decision: the machine sweep costs about seventeen hours

The sweep runs `page_gate` and the browser check against a page and writes the machine half into that page's record. **Proved on one page this session, boundaries-cloud: 3 minutes 1 second, and it wrote three failing chapters.** At that rate the 352 content pages are about 17 and a half hours of wall clock.

That is not a number to optimise away. The sweep runs one page at a time **by Chat's own S267 ruling**, written into the script beside the loop: a batched sweep disagreed with itself, and "a false failure costs more than fifteen minutes of waiting". So the cost is the ruling's cost, and the only real question is when the machine runs it.

Put to Kain this session. His answer will follow in a RULING file.

## 5. One thing found in passing, one page only

`boundaries-cloud` is published at `/learn/psychology/book-notes/boundaries-cloud/`, while its content record's `address` field reads `/learn/personal-growth/book-notes/boundaries-cloud/`. One page checked, not a claim about the other 124. Flagged rather than chased, because the records are Cowork's and Chat's.

OWED BACK: nothing from Chat to unblock this. The failing-chapter count follows when the sweep has run.

*No em or en dashes in this file; checked before writing.*
