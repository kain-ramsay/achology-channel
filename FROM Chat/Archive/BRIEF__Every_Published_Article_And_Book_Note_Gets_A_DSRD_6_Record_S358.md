> **CODE DISPOSITION, S131: DONE.** The machine sweep ran over every published page overnight: 354 records written, 56 skipped and named; results by chapter and where each fault belongs in `REPORT__The_DSRD_6_Machine_Sweep_S131.md`.

> **CODE DISPOSITION, S114, superseded by the line above: WAITS ON** a factory session. Arrived mid-session and read in full the moment H6 raised it, under the channel wall. It is factory work by the S333 rule, naming no page and no component, and this is a theme session: the row set, the backfill and the board count touch no theme file. Nothing in it blocked the portrait work in hand. **Testable fact it waits on:** `page_readiness_board.py` reporting a record for all 197 published articles and all 99 published book notes, found by slug.

# BRIEF: every published article and book note gets a DSRD 6 readiness record

**DOCUMENT TYPE:** brief, commissioned by Kain, written by Claude Chat, Session 358. **Date:** Monday 14 September 2026.
**Commissioned by Kain live at S358**, on being shown the gap Code found and named at S113.
**Answers:** the OWED BACK line in `REPORT__The_Five_Headings_Swept_The_Seven_Book_Notes_Published_S113.md`, section 3, which asked for a commissioned decision from Chat rather than a judgement from Code.
**Owning documents:** DSRD 6 (The Page-Readiness Standard), and standing rule 15.

---

## 1. The problem, in Code's own measurement

`page_readiness_board.py --backfill` enumerates 26 page designs covering 42 live pages. It never enumerates the published content. Read off the install at S113:

- **197 published articles** (116 field-authority, 51 author-biography, 30 instructor-attributed)
- **99 published book notes**

None of them has a DSRD 6 record, and the backfill cannot make one, because its row set does not know they exist. **The board reports 0 pages with no record while several hundred pages have none.**

That is the S054 failure shape exactly: an instrument reading clean on ground it cannot see. Standing rule 15 says a page without its written DSRD 6 record is not ready, so on today's numbers the majority of the live site is outside its own go-live gate and nothing reports it.

## 2. The convention this follows, which already exists

One record per volume page, not one per template. The 18 instructor articles each carry their own record, and that is already the convention on disk. `page_gate` finds a page's record by slug, so a per-page record is also the only shape the existing tooling can look up.

## 3. What is commissioned

**Widen the backfill so every published `article` and every published `book_note` on the install gets a DSRD 6 record, found by slug, generated from what the gate can already measure.**

1. The row set is built from the install's published posts of those two types, not from an enumerated list of page designs. A list that has to be maintained by hand is the thing that caused this.
2. Each record carries the per-chapter result the gate can measure today. A chapter the gate cannot measure is written as not measured, never as a pass. **A generated record must never show a pass that was not run**, which is the same principle the `--override` clearance already follows.
3. The board's "pages with no record" count is then read against published pages of every type, so the number means what it says.
4. Report the counts back: records created, records already present, and any published page the pass could not reach, named.

## 4. What is not commissioned

Not remediation. This brief creates the records and makes the true position visible. Fixing what the records then show failing is separate work, sized once the numbers are in, and it is Kain's to commission when he sees them.

Not the other page types. Quote pages and help answers are outside this brief; once the row set is built from published posts rather than a hand list, adding a type is a line, and that is deliberately left until the two largest sets are done.

## 5. Definition of done

Every published article and every published book note on the install has a DSRD 6 record findable by slug; the board's missing-record count is computed against published pages of those types; the counts are reported back through the channel with any unreachable page named.

OWED BACK: the counts in section 3 item 4, and a plain statement of how many of the 296 records show failing chapters, so Kain can size the remediation.

*No em or en dashes in this file; checked before writing.*
