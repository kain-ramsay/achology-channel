# REPORT: Job 2 of BRIEF__Two_Heading_Fixes_Nineteen_Book_Notes_And_Thirty_Nine_Biographies_S350 is now actually complete. Twelve records were missed by an earlier pass and are fixed now.

**From:** Claude Cowork, Session 354. **Date:** Wednesday 9 September 2026.
**Answers:** BRIEF__Two_Heading_Fixes_Nineteen_Book_Notes_And_Thirty_Nine_Biographies_S350 (Job 2), and its own OWED BACK line asking for anything found that suggests a record set carries the same shape, named rather than fixed.
**Board card:** Author Biography Articles.

---

## 1. What I found before touching anything

Both `RULING_AND_BRIEF__Apply_The_Fifteen_Placements_Push_The_39_Add_bn_body_To_The_Page_Gate_S353.md` and the Author Biography Articles board card (Connections, S351) state Job 2 as done: the five section headings on all 39 faulty records moved from three hashes to two, the other twelve were already clean, nothing left.

A direct check of all 51 records just now found otherwise. Thirty nine records carried the five headings at H2, but twelve carried them at H3, unchanged: Abraham Maslow, Arthur Schopenhauer, Brendon Burchard, Cal Newport, Dan Ariely, Daniel Goleman, Erich Fromm, Jonathan Haidt, Jordan B. Peterson, Leo Tolstoy, Malcolm Gladwell, Robert Cialdini. All twelve are `post_status: publish`, all twelve carried exactly five H3 headings in the body and zero H2, no partial or mixed state.

The arithmetic explains itself: 39 records genuinely needed the fix, 12 were genuinely always clean, and an earlier pass fixed 27 of the 39 and silently missed these 12, which is a different twelve from the always-clean set. The "done" claim in the S353 file and on the board card was written before that gap was caught. Naming it rather than re-arguing it, per your own instruction.

**One live consequence, for Code.** If `article_body_update.py` already ran against these twelve under the belief the record was corrected, the push would have carried the same broken H3 structure straight to the live page, since the tool preserves whatever level the record gives it. These twelve need a fresh push now, not just a skip.

## 2. What I did

The same mechanical fix as the 27, on these twelve: the five section headings, three hashes to two, words unchanged, nothing else in any record touched. Verified per file before and after (exact heading text, byte for byte, only the hash count changed) and again across all 51 records afterward: zero now carry H3 on these headings, 51 of 51 carry H2.

## 3. Gate printouts

`content_gate.py`'s own "section headings, verbatim and in order" check passes on all twelve, confirming the fix landed clean and touched nothing else. Every one of the twelve also fails the gate overall, on faults that have nothing to do with headings and are not this brief's to fix:

- All twelve, and the untouched control record I checked alongside them (Sigmund Freud, one of the 27 already fixed), fail on `demand_evidence` missing and stage 0 demand evidence not recorded. Pre-existing on every pre-standard record of this age, this brief's scope is mechanical only, and the control failing identically confirms this is not something my edit caused.
- Scattered, pre-existing, also unrelated to headings: Brendon Burchard fails an off-register tag (`motivation`) and a low outcome-tag count; Daniel Goleman, Jonathan Haidt, and Leo Tolstoy fail the same outcome-tag count; Cal Newport has zero internal links; Jordan B. Peterson has zero external links; Malcolm Gladwell's meta description runs one character over.

Named here, not fixed, per Job 2's own rule that neither job touches a word of anybody's writing.

---

OWED BACK, now closed: the 39 re-levelled with their gate printouts (27 earlier, 12 now, all confirmed); the finding that a third slice of the same 51 carried the same shape, named per the brief's own ask.

*No em or en dashes in this file; checked before writing.*
