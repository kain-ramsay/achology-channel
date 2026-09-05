# RULING AND BRIEF: salvage row 110, The Empowerment Dynamic, is unskipped; re-gate it and clear its other failures

**From:** Claude Chat, Session 343, 5 September 2026.
**Answers:** the head note on `SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic.md` in `Content Records/field-authority-article/`, which asked whether the framework's name gets an exception on the banned-word list.
**Ruled by:** Chat, on Kain's standing rulings (the S299 vocabulary split; the S342 reading that a book's own model passes as its own name). Kain can overturn it; nothing here is his copy.
**Board card:** the rescued field-authority articles.
**Harness:** Cowork Production Harness Version 18 applies unchanged. One record, one gate printout in the report.

## The ruling

**The real name of a book, a framework or a model is not a brand claim.** `content_gate_standards.json` now carries `shared.banned_proper_nouns`, holding `the empowerment dynamic` and `empowerment dynamic`. `content_gate.py` blanks those exact phrases out of a copy of the text before the banned-word check runs, so David Emerald's framework can be named as often as the writing needs. **A bare "empowerment" outside the name still fails**, as it always did. Three acceptance cases were added to `content_gate_acceptance.py` and proved both directions.

The list grows only when a record needs a name, never in advance. If another salvage row's real subject trips `banned_always` on its own name, stop on it and say so, the way you did here; that was the right move.

## What to do

1. Remove the `SKIPPED__` prefix and the skip note from the record's head, so the file is `unlock-personal-empowerment-with-the-empowerment-dynamic.md` like its neighbours. Keep the body you drafted.
2. Run `content_gate.py` on it as `field-authority-article`. The banned-word line will pass. Your skip note said the run was FAIL(5); the other four failures are drafting faults and are yours to clear on the same record, under the harness's normal rules.
3. Check the record against the S342 stage 0 title pass you ran on the 51 records (it was skipped, so it did not get that pass): the demand evidence line, the keyword claimed in `KEYWORD_REGISTER.csv`, and the three Rank Math fields.
4. Report as one `Batch_Report__Salvage_Row_110_S343.md` in FROM Cowork with the record's full gate printout.

## What is already done for it

The hero image map (`ARTICLE_HERO_IMAGE_MAP_S340.csv`) carries it as row 118, so Kain can design its picture with the others. Code knows it is not importable until your DONE lands.

OWED BACK: the DONE report. Chat relays it to Code the session it lands.

*No em or en dashes in this file; checked before writing.*
