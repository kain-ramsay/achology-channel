# REPORT: chapter 5 re-run across every record, with item 10 in it

**From:** Claude Code, Session 079. **Date:** 24 August 2026.
**Answers:** `ASK__Re_Run_Chapter_Five_Machine_Half_Voided_By_Version_Seven_S295`, both halves of it.

---

## Your finding was right, and it was bigger than the four you could see

You wrote: "This is almost certainly not limited to those four. Every record swept on 14 August has the same problem. Chat has read four; you can see the whole set."

**You could see four. It was all twenty five.** Every §5 machine line on the site was measured before DSRD 6 moved to Version 7, so every one of them was void under the document's own reset rule. **The count you asked for is 25.**

## What was blocking it, and it is now built

Item 10's runner line names the chain-register script of DSRD 1 §11.0 as its instrument, and that script did not exist. It does now: `redirect_chain_register.py`, reported in full beside this file. So §5 could not have been re-run honestly before this session, and it can be from here.

`page_gate.py` gains check 21, `chain-register`. It does not re-measure: it reads the workbook and asks whether the five facts naming this page were recorded. **The exemption is read, not inferred**, exactly as item 10 requires: a page nothing redirects to gets "nobody's redirect destination: exempt, read from the workbook", and a page something redirects to gets its row count and the columns that are blank or false.

`page_readiness_board.py`'s §5 map now reads `links-resolve, sitemap, chain-register`, where it read `links-resolve, sitemap`. That one line is what had frozen the chapter.

## The re-run

**Twenty one of the twenty five records were re-measured.** The other four could not be, and the reason is not an oversight: `single-article.php`, `single-book_note.php`, `template-author-profile.php` and `404.php` have no built page at any address to measure. Their §5 lines stay as they were, and that is the honest state rather than a skipped step.

On the twenty one, §5's machine half now runs **4 checks where it ran 3**, and the fourth is the chain register.

## Your second point, about the two version numbers, is fixed at the source

You wrote that "page_gate v7" was the script's version and not the standard's, and that "the coincidence is a trap for whoever reads a record in six months."

**Every run header now names both, and the standard's number is read from DSRD 6 itself rather than typed into the script.** A hardcoded version would be the same copy going stale that produced the fault. The line now reads:

> **Run 2026-08-24 against https://achologytest.com/about/, page_gate v8, measured against DSRD 6 Version 7 (19 August 2026).**

You had to do date arithmetic across twenty five records to find this. Nobody will have to again.

## What the re-run found, and one thing you should look at

**The scoreboard, from the records:** 25 page designs covering 34 live pages, **0 READY**, 25 carrying a failing line, **161 chapter lines open**.

**A caution on comparing that against the 598 in my S078 note.** They are different units. That figure counted chapter lines across a per-item reading; this counts chapter states across the 25 records. **Nothing has got better or worse between them and neither number should be read as movement.** Said plainly because a board that reads a drop as progress is worse than no board.

### The lines the sweep overwrote, named because two of them are yours or Kain's

**Nothing was destroyed.** Every overwritten line carries its previous value inside it, in brackets, so the earlier verdict is still readable on the record. That is the machinery working as designed and I am not raising it as a fault. Two are worth your eye anyway.

**`/instructors/` §5 replaced a recorded exception Kain approved at S272.** The old line was the build-ground noindex contradiction. The new line is a genuinely different finding: three workbook rows point at that page and its chain is broken at `dest_schema`. **That is the Person-entity gap** reported beside this file: DSRD 3 §5.3 assigns Our People "WebPage + Person entities" and the page carries CollectionPage with no Person at all. So the exception did not become wrong; the chapter acquired a second, real reason to fail. Kain should know his exception line was moved, which is why it is here.

**Eight policy-family records had §2 overwritten**, each replacing your S295 line "headings read alone as an honest table of contents" with a machine failure. The machine is measuring a different thing from the one you read: the supporting line's length against DSRD 7 §3.3. On `/about/` it reads 44 words against a band of 12 to 25. Your reading of the headings still stands and is still in the line.

### One stale thing in the records themselves

**The runner column for §5 says "machine" on the records, and DSRD 6 Version 6 made that chapter split.** Its runner line assigns items 2 and 8 to a human reader. The board behaves correctly, leaving §5 open on a machine pass, but the records' own column disagrees with the standard. **That is a document correction and it is yours**, since Code never edits a DSRD or a record template's standing text.

## What §5's machine half still does NOT cover, said plainly

A green §5 machine line means three checks passed, not that the chapter's machine half is complete. **§5's runner assigns the machine items 1, 3, 4, 5, 6, 7, 9 and 10.** The gate today measures item 4's "the links resolve" half, item 9, and item 10.

**Items 1, 3, 5, 6 and 7 have no checker.** By name: right address against DSRD 1's structure, indexing set on purpose, breadcrumb matches the hierarchy, old address in the redirect map, and not orphaned. All five are mechanical in principle and none of them is built.

This is written into `page_readiness_board.py` beside the map, so the next reader of that file meets it. Raised here because a partial run reported as a whole one is the exact failure the map's own header warns about, and I would rather name the gap than have a record read as measured when half of it was not.

**If you want those five, say so and they are a session.** Items 6 and 7 are the two that would find real faults: item 6 is answerable straight from the workbook I have just filled, and item 7 would tell us which of the 34 live pages nothing links to.

*No em or en dashes in this file; checked before writing.*
