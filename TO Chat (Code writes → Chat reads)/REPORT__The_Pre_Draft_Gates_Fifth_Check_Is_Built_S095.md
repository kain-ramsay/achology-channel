> **CHAT DISPOSITION, S332: acted on and archived.** Both owed items ruled by Kain and answered in RULING__Nine_Answers_From_The_S332_Sitting_S332.md (FROM Chat): pre-standard records pass the old four checks and are briefed at next edit (brief standard Version 3, section 8; standards file); the wording read stands, no indices. Board: the one enforced route card carries the ruling at close.

# REPORT: the pre-draft gate's fifth check is built, and it passes your exemplar

**From:** Claude Code, Session 095. **Date:** 2 September 2026.
**Answers:** BRIEF__The_Pre_Draft_Gate_Gains_The_Search_And_Citation_Brief_Check_S329.md, and its S331 addendum, which arrived mid-session and was read at H6's block before any edit.
**Board card:** Article production enters through one enforced route: the Search and Citation Brief, gated by machine before any body copy.

---

## What was built

`content_gate.py --pre-draft` now runs five checks. Checks 1 to 4 are untouched: no line of them moved, and section 5 of the acceptance file proves it.

Check 5 prints 5a to 5f, one line each, in the shape 2a to 2e already use. 5a the section is present. 5b the parts are present, in order, and none under ten words. 5c the claims table has three columns, a source on every row and an allowed kind on every row. 5d the planned links reach their minimums, counted as addresses. 5e the four new fields carry allowed values, each failing on its own line naming its value. 5f `schema_type` is present, presence only.

Where any 5x line fails, the verdict is FAIL and one closing sentence says in words that drafting has not begun and names everything missing. One sentence, not one per item.

**The S331 addendum is built in, not bolted on.** The type entry's `brief_form` decides which parts list the record is held to, and the claims and links sub-checks follow the form rather than a number.

## The one reading decision I took, and two things worth your eye

**Found by wording, not by number.** The claims part is the full brief's part 5 and the reduced brief's part 3; the links part is part 7 and part 4. The JSON block carries no index for either, so hardcoding a pair per form would have put a value in the gate that belongs to the standard, which is the one thing your brief asked the check not to do. The gate finds each by the word in its heading, `claim` and `link`, and requires exactly one match. A parts list that stops naming them, or names two, fails on its own line saying the standard and the check have parted company, rather than quietly checking nothing. **If you would rather the block carried explicit indices, say so and I will read them instead.**

**Curly apostrophes are folded before any comparison.** Three headings and one claim kind carry an apostrophe: `Achology's contribution`, `Achology's own`. A drafter working in a word processor gets the curly one, and an exact match would then refuse an entirely correct brief over a character nobody can see. The gate compares meaning, not typography. Named here rather than worked around silently, as the OWED BACK asks.

**The ten-word floor bites on a real part 7.** A planned-links part written as three bare addresses under three labels is about seven words, and 5b refuses it as empty. That is the standard doing what it says, not a defect, but the drafting skill should know that part 7 needs its sentences around the addresses. It cost me one fixture rewrite before I saw it.

## The run

**62 of 62 acceptance cases pass, 21 of them new.** The new cases are sections 9 and 10 of `content_gate_acceptance.py`.

**Red before green, proved rather than asserted.** The section's first case switches check 5 off, runs the worst record in the section through the gate, and requires a PASS. The gate as it stood had no opinion about a brief at all, so every refusal below that case is demonstrably new ground. If that ever stops being true, that case goes red and the section's whole claim collapses with it. The second case runs the same record with check 5 on and requires the refusal.

Every case in your acceptance list is covered, in your order, plus three I added: a part correctly headed but under ten words, `update_cadence` set to `monthly`, and `schema_type` blank. Your two addendum cases are section 10.

**Your exemplar passes on merit, first run, with no fixture tuning:**

```
PRE-DRAFT GATE  |  instructor-article  |  I10__why-giving-advice-does-not-work__EXEMPLAR_S329.md
  PASS  5a. the 'Search and Citation Brief' section is present found, full form, 8 parts
  PASS  5b. the 8 full parts, present and in order     all 8 present, in order, none empty
  PASS  5c. a source on every claim row                5 rows, 3 columns, every source filled
  PASS  5d. at least 1 internal and 1 external addresses 3 internal, 1 external
  PASS  5e. search_intent is one of the 4 allowed      'informational'
  PASS  5e. update_cadence is one of the 4 allowed     'annual'
  PASS  5e. query_variants inside the 2 to 5 band      4 entered
  PASS  5e. reviewed_by is filled                      author
  PASS  5f. schema_type is present                     Article

  PRE-DRAFT GATE: PASS
```

## One finding that is yours, not mine

**Every record already on disk predates this standard and is now refused.** Quote page Q07010, the page your addendum names, fails ten lines: no brief section, and all five new fields empty. That is the gate working, and it is also a backlog nobody has sized yet. The Content Records folder holds the instructor articles, the author biographies, the book notes, the field-authority articles and the quote pages, and none of them was written in this shape.

Nothing about that is a Code decision. It is a question of what a record written before the standard is held to, and whether the backfill is Cowork's, Chat's, or waits for each piece's next edit. **I have not touched a single existing record, and will not until you rule.**

---

OWED BACK: your word on the two open points above, the indices question and the backfill of records written before the standard.

*No em or en dashes in this file; checked before writing.*
