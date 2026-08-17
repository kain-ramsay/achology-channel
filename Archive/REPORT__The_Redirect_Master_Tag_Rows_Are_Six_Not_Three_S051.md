# REPORT: the Redirect Master's old tag spellings, and there are six of them

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `RULING__Course_Selection_Lead_Tag_Plus_Slug_Correction_S253.md` §3.
**Read only. The workbook was opened and not written to.**

## What the ruling expected, and what is there

The ruling said: "Three rows there will still carry the old spelling."

**There are six, across two sheets.** All of them are `new_url` values pointing
at a tag address that no longer exists.

### Sheet "Old tags", five rows

| Row | old_url | points at |
|---|---|---|
| 29 | `/tag/direction-in-life/` | `/learn/tags/find-purpose-direction/` |
| 52 | `/tag/life-design/` | `/learn/tags/find-purpose-direction/` |
| 89 | `/tag/reduce-stress/` | `/learn/tags/manage-stress-anxiety/` |
| 122 | `/tag/understanding-core-values/` | `/learn/tags/find-purpose-direction/` |
| 125 | `/tag/values-priorities/` | `/learn/tags/find-purpose-direction/` |

### Sheet "Miscellaneous", one row

| Row | old_url | points at |
|---|---|---|
| 40 | `/quote_topic/entrepreneurship/` | `/learn/tags/start-grow-a-business/` |

**Four rows point at `find-purpose-direction`, one at `manage-stress-anxiety`,
one at `start-grow-a-business`.** All three tags now carry the written-out
"and" spelling, so all six of these redirects would land on a 404.

Every one carries the same basis note: "S247 ruling, group A: old tag maps to a
new 36-tag taxonomy tag (DSRD 1 §5 ...)". The mapping is right; only the
address spelling is wrong.

## One near miss, checked and not a hit

Sheet "Courses + commerce" row 34 sends `/product/how-to-start-and-grow-a-business/`
to `/academy/personal-growth/entrepreneurship-business/`. It matches on the
words but it is a product URL going to a school page, not a tag address, and
its spelling is already correct. Nothing to do.

## What I have not done

**Not edited.** The ruling said not to without saying so first, so this is the
saying. Six cells in a `new_url` column, three distinct corrections:

```
find-purpose-direction     -> find-purpose-and-direction     (4 rows)
manage-stress-anxiety      -> manage-stress-and-anxiety      (1 row)
start-grow-a-business      -> start-and-grow-a-business      (1 row)
```

Say the word and I will make those six edits and report the before-and-after
of each cell. It is a workbook Kain and others also work in, so I would rather
be told than assume the door is open because the correction is obvious.

**One thing worth deciding at the same time:** whether anything else in that
workbook was written from DSRD 1 §5.6's old spelling rule. I checked only the
three slugs the ruling named. If the tag tab was built from that rule, the
other 33 tags are worth the same pass, and I can run it in one go.

*No em or en dashes in this file; checked before writing.*
