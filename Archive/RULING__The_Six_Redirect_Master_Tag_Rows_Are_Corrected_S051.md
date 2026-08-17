# RULING: the six stale tag addresses in the Redirect Master are corrected

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Filed under Harness Rule 14.**
**Follows:** `REPORT__The_Redirect_Master_Tag_Rows_Are_Six_Not_Three_S051.md`.

## What was put to him

Reported: six rows in the Redirect Master point at three tag addresses that no
longer exist, so those redirects would land on a dead page. Asked, in one
question, with a recommendation to do it:

> "Shall I correct those six addresses in the spreadsheet?"

## Kain's ruling, his word in full

> "yes"

## What was done, and the check that came first

**Before touching it, the workbook was surveyed.** openpyxl rewrites an xlsx
whole on save and is known to drop charts, images, pivot tables and some
formatting. Six cells are not worth damaging a file Kain works in. The survey
found none of those things: no charts, drawings, media, pivots, comments or
tables in the container; no merged cells, no conditional formatting, no defined
names, no autofilters on any of the 17 sheets. A backup was taken first.

**Cells were found by content, never by row number**, so a row inserted since
the report could not have made the write land in the wrong place.

| Cell | Before | After |
|---|---|---|
| `Old tags!E29` | `/learn/tags/find-purpose-direction/` | `/learn/tags/find-purpose-and-direction/` |
| `Old tags!E52` | `/learn/tags/find-purpose-direction/` | `/learn/tags/find-purpose-and-direction/` |
| `Old tags!E89` | `/learn/tags/manage-stress-anxiety/` | `/learn/tags/manage-stress-and-anxiety/` |
| `Old tags!E122` | `/learn/tags/find-purpose-direction/` | `/learn/tags/find-purpose-and-direction/` |
| `Old tags!E125` | `/learn/tags/find-purpose-direction/` | `/learn/tags/find-purpose-and-direction/` |
| `Miscellaneous!E40` | `/learn/tags/start-grow-a-business/` | `/learn/tags/start-and-grow-a-business/` |

**Verified from disk after saving:** no old spelling remains anywhere in the
workbook, and all 17 sheets are present.

**Verified against the live site**, because a redirect map is only right if its
destination exists:

```
/learn/tags/find-purpose-and-direction/    200
/learn/tags/manage-stress-and-anxiety/     200
/learn/tags/start-and-grow-a-business/     200
/learn/tags/find-purpose-direction/        404   (the address that was written)
```

## The wider question I raised, now closed without needing anyone

I asked whether the other 33 tags might carry the same fault. **They cannot.**
The divergence only ever existed where a tag name held an ampersand, and the
S253 ruling names all three that do. The other 33 have no ampersand, so there
is no spelling for the old rule to have got wrong.

Closing it here rather than leaving it sitting in your inbox as a question.

## One consequence to know about

The workbook holds 81 formula cells. They are preserved as formulas, but a save
through openpyxl does not carry their cached results, so Excel or Numbers will
recalculate them on the next open. Nothing to do; worth knowing before someone
sees a flicker of recalculation and wonders what changed.

The backup taken before the edit is in this session's scratchpad and will not
survive the session. If you want one kept, say so and it goes to the folder's
Archive under the convention.

*No em or en dashes in this file; checked before writing.*
