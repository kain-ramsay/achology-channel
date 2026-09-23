> **CODE DISPOSITION, S131: DONE.** The nickname match is live in the publishing tool, read from DSRD 5 section 9 and proved by acceptance (no live page names a course only by an unlinked nickname today); the importer writes `destination_course_name`. Answered by `SHIP__Course_Links_And_Importer_S131.md`.

# NOTE: two things for the publishing tool, both ruled by Kain

**From:** Claude Chat, S379, Wednesday 23 September 2026. **To:** Claude Code.
**Board card:** Search and citation layer for every EPS page (the automatic course link lives there).

## 1. The course nickname list is approved, for sweep 2

Kain approved the nickname list at S379, including the six short subject nicknames ("the NLP course", "the CBT course", "the life coaching course", "the hypnotherapy course", "the counselling course", "the mindfulness course"), each linking to that subject's main practitioner course. It lives in DSRD 5 section 9; DSRD 1 section 6.4 now points there. Build it into the automatic course link alongside the full names: case-insensitive, whole phrase, first unlinked mention, once per page, inside the ceilings, same tab. Read the list from DSRD 5 section 9 rather than copying it into the tool by hand, so a future approved nickname needs one edit, not two.

## 2. The importer should write the course name for instructor articles

Your S130 SHIP named this and left it for Chat to place. It is now written into DSRD 2 section 6.5, instructor-attributed row: the article importer should write `destination_course_name` from the record as post meta, so an imported instructor-attributed article shows its course cover in the writing rather than the author's portrait, as Kain ruled at your S130. Until it does, a future import of such an article shows the wrong picture.

Both are implementation of rulings Kain has already made; no design choice is left open.

## OWED BACK

When sweep 2 ships, one line naming the nickname match as live and one page read back showing a nickname linked. When the importer writes the field, one line saying so.

*No em or en dashes in this file; checked before writing.*
