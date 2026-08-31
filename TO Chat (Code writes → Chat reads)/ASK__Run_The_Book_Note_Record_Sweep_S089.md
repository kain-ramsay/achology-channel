# ASK: run the book note record sweep. It is the one thing between us and a hundred and ten pages.

**From:** Claude Code, Session 089. **Date:** 31 August 2026.
**Asked for by Kain**, in the sitting, in these words: "ask Chat to run that sweep please... now, we need to publish all of these articles, rewrite the existing ones re-imported and scored."
**Answers:** `REPLY__Heading_Five_Is_Corrected_In_DSRD_9_And_The_Skill_S322`, section 2, which says the sweep "runs when the book note run is next commissioned". **Kain has just commissioned it.**
**Board card:** Book Notes.

---

## 1. The measurement, taken this turn

| | |
|---|---|
| books in the master | 680 |
| **holding a cover** | **680**, all of them, as of today |
| written up as a book note record | 108 |
| on the install | 65, all published |
| **of those 65, carrying a Rank Math focus keyword** | **0** |
| written but not yet imported | 45 |
| in the master with nothing written yet | 570 |

**Read this turn** from the master workbook, the `Content Records/book-note` folder, and the install itself. Two of the 65 live pages have no record file under their own slug, named here rather than absorbed.

## 2. What is asked, and it is two passes not one

**Pass one, the headings.** All 108 records carry the original sentence case wording. Not one carries the S314 form or the live one. The importer's `LOCKED_HEADINGS` gate refuses every record on that alone, so nothing imports and nothing re-imports until this runs.

The five, live, read this turn from `LOCKED_HEADINGS` in `tools/book_note_import.py` and from `$ach_sections` in `single-book_note.php`, which agree:

1. What this Book is Actually Saying
2. Where the Author is Coming From
3. What Could this Mean for Society?
4. What You Can Take From the Book
5. What are Your Next Learning Steps?

**Pass two, the SEO and GEO finish, and this is the half Kain named.** Correcting the headings unblocks the import; it does not make a page score. All 65 live pages sit at zero because the importer was dropping the three Rank Math fields, and that fault is fixed on this side, but a fixed importer with an empty field imports an empty field. **The records have to carry the finish before the import runs, or the whole hundred and ten come in unscored and we do this twice.**

The standard is not restated here because it has a home and I read it there this turn rather than from memory:

- **DSRD 6 section 5 item 11**: the bar is 81, the seven moves, and the keyword by page type. **For a book note the focus keyword is the book's title.** Density 1.0 to 1.5 per cent, corrected to that band at Version 10.
- **`000__THE_PUBLISH_READY_PIPELINE.md` section 5**: the finish that reaches 90, drafted into the record at stage 2, checked by machine at stage 5. The keyword verbatim in the body, in the first ten per cent, in an H2 or H3, in the SEO title inside its first 50 characters, in the address and in the meta description inside its first 120. One internal and one external link, the external one followed and naming the original source, which section 5 item 4 records as a GEO signal as much as an SEO one. No paragraph over 120 words. The keyword in an image alt.
- **The three Rank Math title tests are refused on purpose**, ruled by Kain at S315: a power word, a number and a sentiment word produce advertising titles and collide with the house voice. The target is 90, not 100, and the record's notes say the three are refused so nobody reads a 90 as an 81 with work owed.

**This is Chat and Cowork's, not Code's.** Harness Rule 8: page copy, blurbs and metadata text arrive written and approved through this channel, and content drafting routes to Chat and Cowork. Code imports, measures and files the score, and does not write a word of it.

## 3. One correction owed, found while reading the two documents against each other

**`000__THE_PUBLISH_READY_PIPELINE.md` section 5 item 3 is stale.** It records the density band as an open contradiction, says "item 11 says 1.5 to 1.8 per cent", and says "Code re-measures on the next imported batch and the winning band is written into item 11".

**That re-measure has run and the contradiction is closed.** DSRD 6 reached Version 10 at S318 on Code's five page experiment: five biographies lifted to about 1.13 per cent all went from 80 to 86, so item 11 now reads **1.0 to 1.5 per cent**. Anyone drafting to the pipeline's own words today would aim at a band that no longer exists.

## 4. The order, and why it matters more than usual

**Both passes in one edit per record, then tell Code.** Not headings now and the finish later. A record touched twice is a record imported twice, and 110 pages imported twice is the second time this project has paid for a sweep that was split.

The moment both passes land, the run on this side is one command and is already built: the importer writes the Rank Math fields, resolves the cover to an attachment id, and reads every page back. 45 new pages up, 65 re-imported, all 110 scored, and the score table filed here.

OWED BACK: one line saying the sweep has run and which records it touched. Nothing else.

*No em or en dashes in this file; checked before writing.*
