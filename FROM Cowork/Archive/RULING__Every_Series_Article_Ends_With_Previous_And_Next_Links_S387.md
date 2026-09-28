> **CHAT DISPOSITION, S387: ACTED ON, ARCHIVED.** Written into Recipe 9 (Links, the closing Previous and Next block, for every series article). Code asked: FROM Chat/ASK__How_The_Import_Treats_The_Series_Previous_And_Next_Links_S387.md. No card moved.

**Needs from Chat:** write this ruling into Recipe 9, and ask Code whether the import treats the links block as navigation.

# RULING: every article in a series ends with Previous and Next links

**From:** Claude Cowork, run of Monday 28 September 2026. **Given by Kain,** in the Cowork session.

## Kain's words
"We need a short paragraph or some way in every single article to allow the reader to link back to the previous article, if there is one, and also onto the next article, again, if there is one." Asked whether to add it to all nine articles, he replied: "Yes, please do."

## What was done
All nine Seven Beliefs parts now end with the same links block. It sits after the closing paragraph and before the sourcing record, in this shape:

`**Previous:** [Part N-1, {that part's H1}]({address})`
`**Next:** [Part N+1, {that part's H1}]({address})`

Part 1 carries Next only, and Part 9 carries Previous only. This also meets Recipe 9's line that Part 1 should point on to the parts after it, without changing Kain's approved prose.

## Two things that follow
1. **The shared bar.** `_cowork_shared_bar_S387.py` now treats the two link lines as navigation, not prose, so they are not counted towards word count, reading ease or the paragraph floor. The full gate (`content_gate.py`) will count them unless it is told the same. That is Code's call.
2. **A theme block later.** Code could later build this as a theme "previous and next" block. That is a visual decision for Kain to see rendered, and nothing about it has been decided.

## Checks after the change, run on disk
- The repeat check across all nine parts prints PASS.
- The shared bar shows no new failures. The only failures left are the ones already reported: keyword density on Parts 2 to 8, and Part 1's approved-words findings.

## OWED BACK
- From Chat: this ruling written into Recipe 9 ("Links, inside the body").
- From Code, via Chat: whether the import treats the links block as navigation.

*No em or en dashes in this file; checked before writing.*
