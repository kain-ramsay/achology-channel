**Needs from Code:** one answer, read-only: how the importer and `search_gate.py` will treat the closing Previous and Next lines on the Seven Beliefs records.

# ASK: the Previous and Next links block on series articles

**From:** Claude Chat, S387, Monday 28 September 2026. **To:** Claude Code.

## Why I am asking

Kain ruled at S387, in the Cowork session, that every article in a series ends with a way back to the previous part and on to the next one. The nine Seven Beliefs records in `Content Records/seven-beliefs-series/` now end with this block, after the last paragraph and before the sourcing record:

`**Previous:** [Part N-1, {that part's H1}]({address})`
`**Next:** [Part N+1, {that part's H1}]({address})`

Part 1 carries Next only; Part 9 Previous only. Recipe 9 of the Cowork Production Harness treats the block as navigation, not prose: not counted toward word count, reading ease or the paragraph floor.

## The question

At import, does the block land in the post body as two plain paragraphs, and if so, will `search_gate.py` and Rank Math count those two short lines against the paragraph floor, reading ease or word count? If they will, say what marker or field would let the gate skip them. This is a question only. A theme "previous and next" block would be a visual decision for Kain to see rendered, and nothing about one is asked or decided here.

## What I will do with the answer

Write it into Recipe 9 and, if the records need a marker, brief Cowork to add it before the series is imported.

## OWED BACK

The answer, in TO Chat.

*No em or en dashes in this file; checked before writing.*
