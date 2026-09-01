> **CODE DISPOSITION, S093: DONE, the run is complete and reported as `REPORT__The_Done_Card_Strip_Is_Complete_S093.md`.** Every card the board returns at Status Done carries a closing record and nothing else: eight at S092 and eighty seven this session. Nothing outside the four fields was touched on any of them, no card was deleted and no open card was opened, confirmed by read-back on three. The pre-change backup this brief requires exists as twelve batch files in the `Notion Done Card Backup S092` folder, 95 cards with no duplicates, and it is now in version control, which it was not: the ignore rule on that tree was swallowing it. **Six cards carry `Closed. Reason not recorded on the card`**, per this brief's own instruction, and they are listed in the report. **Two things are still mine and both are one query:** the after character count, and a recount, because the board answered 95 Done cards today where the S092 record says 103. The workspace's SQL quota ran out before either could run.

> **CODE DISPOSITION, S085, superseded by the line above: WAITS ON** the Notion run itself. No report exists in the channel Archive, so it has not been run; the pre-change backup file it requires does not exist either.

# BRIEF: strip the 82 Done cards on the Notion board to their closing record

**DOCUMENT TYPE:** approved brief, from Claude Chat, Session 289. **Date:** 19 August 2026.
**Approved by:** Kain, in session, S289.
**Priority: LOW. This queues behind the video swap run. Do not interrupt courses 002 to 027 for it.**

---

## Why this exists, in one line

Kain's ruling at S289: **the board is a task board, not a decision capture filing cabinet.** It should go down as work completes.

## The measurement, taken this session

The board holds **76 open cards and 82 Done cards**.

- The 76 open cards carry **227,643 characters** between their Purpose, Definition of Done, Connections and Source fields. Average 2,995 characters a card.
- The 82 Done cards carry **152,043 characters**. Average 1,854 a card.

**Not one word of those 152,043 characters will ever be acted on.** That is 40 per cent of the board's total text weight sitting in cards whose work is finished.

## The standard this comes from

`notion-registry-audit`, the Board Item Standard, rule 2, tightened at S289:

> A row holds only what someone acts on. Every passage in every field either tells a named person what to do, or supplies a fact they need in order to do it. The test, which anyone can run on any card: read each passage and name the person who acts on it. Where no name can be given, the passage goes.

On a Done card, no passage can name anyone. So the whole body goes, except the closing record.

## What each Done card keeps

Exactly four things:

1. **Task** (the title), unchanged.
2. **Status** Done, unchanged. **Triage, Phase, Area, Owner, Type** all unchanged.
3. **Definition of Done**, replaced with one short closing record: what closed it, and where its work went if it went anywhere. Three shapes cover almost all of them:
   - `Completed. <one line on what was delivered>.`
   - `Merged into '<card name>'. <one line on what travelled with it>.`
   - `Removed: <reason>. No work was delivered.`
4. **Purpose**, replaced with one line naming what the card was for. **Connections** and **Source**, emptied unless they name a card that is still open, in which case keep only that pointer.

## What you must not do

**Do not delete any card.** Claude never deletes in Notion; Kain performs all deletions.

**Do not touch any card whose Status is not Done.** The 76 open cards get a judgement pass with Kain across three later sittings, and it is not this job.

**Do not invent a closing reason.** Where a card's existing text does not say why it closed, write `Closed. Reason not recorded on the card.` and list that card's name in your report. Guessing is worse than admitting the record is thin.

**Do not lose a pointer.** If a Done card's body names another card that is still open, that pointer survives into the new Connections line. Read the open card list before you start so you can tell.

## How to do it

Read each Done card through the Notion API, derive its closing record from its own existing text, write the four fields back, and read each one back to confirm the write landed. Chat cannot do this: it has no bulk write and would need 82 separate calls. You can loop it.

Kain gave one caution worth repeating: six card bodies were overwritten at S286 and had to be recovered from Notion page history. **Save every card's current four fields to a file before you change it**, so the whole run is reversible from disk rather than from Notion's history.

## What to report back

One file to TO Chat carrying: cards processed, the character count before and after, the list of any card where the closing reason was not recorded, and confirmation that the pre-change backup file exists and where it is.

*No em or en dashes in this file; checked before writing.*
