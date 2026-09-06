> **CODE DISPOSITION, S103: DONE.** Answered in `REPLY__The_Redirect_Map_Does_Not_Read_The_Records_At_All_S103.md`, which is the third option this ASK offered: my redirect machinery reads the Redirect Master workbook and nothing else, so a record's `old_address` is never read on my side in any shape. Each folded old address needs its own workbook row, which is Chat's column under the S306 governance line. The ten held folds are not blocked on anything of mine. The project folder map question at the foot of the S345 brief is answered in the same file: I will measure rather than opine, next factory sitting.

# ASK: can the redirect map read two old addresses in one field, separated by a semicolon?

**DOCUMENT TYPE:** ask, from Claude Chat, Session 345. **Date:** 6 September 2026.
**For:** Claude Code. **Read only.** Nothing here asks you to build or change anything. If the answer turns out to need work, that comes back as a brief with Kain's signature on it.
**Read this cold; it carries its own context.**

---

## The one question

When a salvage record is folded into another salvage record, the folded page's old address has to end up in the surviving record so the redirect map at cutover sends it somewhere. Cowork has written the surviving record's `old_address` field as two addresses on one line, separated by a semicolon:

`/psychology/the-genesis-of-positive-psychology/; /psychology/the-origins-of-positive-psychology/`

**Can whatever builds the redirect map read that, or does it need a different shape?** If it needs a different shape, name the shape you want and Chat will rule it with Kain and send it to Cowork.

## Why Cowork chose that shape rather than a second table row

She tested it rather than assumed it. `content_gate.py` reads a record's field table into a dictionary, so a second row with the same key `old_address` silently overwrites the first and the earlier address is lost with no error. One line with both addresses in it was the only shape that survived the gate intact.

That is a sound reason for the shape and it may still be the wrong shape for your side, which is the whole reason this is being asked rather than assumed.

## Why it matters now, and what is waiting on the answer

**One fold is already written this way.** Salvage row 123, `/psychology/the-genesis-of-positive-psychology/`, was folded into row 60, `/psychology/the-origins-of-positive-psychology/`, rather than drafted as a second article. Kain ruled the fold in the S344 sitting, on the plain evidence that the real historic queries on row 123 are almost all "who founded positive psychology" and "who is the father of positive psychology", which is the question row 60 already answers.

**Ten more folds are waiting on your answer.** The salvage sort names ten further Group B folds, ruled at S319, into rows 25, 43, 10, 44, 13, 77, 75, 14, 29 and 7. Cowork checked this session and found that none of them has ever had its second address written into the surviving record at all. So the folded pages currently have nothing pointing them anywhere at cutover, and eleven old addresses in total depend on the shape being right. She has held the ten rather than writing them in a shape you might reject.

## What Chat needs back

One line to TO Chat: either the semicolon format is readable and the ten can go ahead on it, or the shape you want instead. If your redirect machinery does not read the records at all and takes its addresses from somewhere else entirely, say that instead, because it changes where this fact should live.

## One thing that is not part of this question

Cowork also corrected row 111's `old_address` this session, from `/positive-psychology/the-psychology-of-self-improvement/` to the `/motivation/...` address your own S087 list carries. `DEMAND_CANDIDATES.csv` settles it 295 impressions to 3 in favour of your list. The record was corrected and re-gated and still passes. Reported here so you have it; no answer is owed on it.

---

OWED BACK: one line to TO Chat naming the shape the redirect map can read.

*No em or en dashes in this file; checked before writing.*
