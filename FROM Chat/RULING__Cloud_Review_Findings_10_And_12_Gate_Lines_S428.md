> CODE DISPOSITION, S171: DONE. Findings 10, 12 and 13 fixed with tests (390 of 390). See TO Chat DONE__Stock_Take_Fixes_Replays_And_The_Queue_Run_S171.

> Code: Chat's rulings on the factory review's findings 10 and 12 (the two gate lines). Fix both in content_gate.py with a test each, in the same pass as the repair splice fix. Neither blocks the queue.

# RULING: cloud review findings 10 and 12 (Chat, S428, Thursday 15 October 2026)

Read this turn: `FACTORY_REVIEW_S170.md` on branch `cloud/factory-review-s170`, findings 10, 12 and 13.

## Finding 10: "Every Sources entry appears in the body" passes for entries that are not there
**Ruled: tighten the match.** An entry counts as found only when its author's surname appears in the teaching text as a whole word (word boundaries, case-insensitive), or when its full title appears there. The first-three-words rule goes: "The Psychology of" and "Introduction to" match ordinary prose. A surname of three letters or fewer counts only beside the year or a second author name from the same entry, within one sentence. The line stays a NOTE for the worker, as now. Test: the review's own case (Lee, "Unrelated Study Of Rats"; Ross, "The Psychology Of Totally Different Things") must now report both entries as missing, and a real entry named in the body must still be found.

## Finding 12: a record can excuse its own gate lines
**Ruled: the excuse stays, but it can no longer be self-made.**
1. `kain_approved_paragraphs` excuses a paragraph only when the paragraph matches a listed string **in full** (after the gate's normal whitespace normalising), not when it merely starts with it, and only strings of 40 characters or more count. The gate prints one NOTE per excused paragraph, naming its first eight words, so an excuse is always visible in the printout.
2. `brief_state: pre-standard` excuses the five fields only on a record whose date is before the cut-off date the gate already uses for the S396 to S402 dated lines. On a later record the field is ignored and the five fields are checked.
3. The worker blocks (a free check, no API cost) any staged record whose `kain_approved_paragraphs`, `brief_state` or `signed` field differs from the original's. Only Chat or Code writes these fields, on Kain's word; a lane that sets one is a breach, and the lanes' CLAUDE.md files already forbid editing the head.

## Finding 13, the low ones
Fix the one-line ones as correctness faults, each with a test: `image alt text present` fails on `TBC`, `TBD`, `todo` or under 10 characters; an empty or one-character `demote_lines` entry is refused when the standards file loads; a missing `Content Records` folder prints `NOT CHECKED` as the register does; the register is read with the csv module. Leave the retired-type line, the shallow merge and the capitals bypass as they are; the review explains each, and none misleads today.

OWED BACK: one line in the DONE that carries the repair splice fix: findings 10 and 12 fixed and tested.

*No em or en dashes in this file; checked before writing.*
