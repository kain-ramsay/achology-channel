# RULING: the earlier gate brief is withdrawn, and the workbook standard is rebuilt

**From:** Claude Chat, Session 325. **Date:** 1 September 2026.
**Withdraws:** `BRIEF__Teach_The_Content_Gate_A_Section_Range_And_The_Half_Rule_S325.md`, written earlier the same day and sitting beside this file. **Do not build it.** Both things it asked for describe a workbook shape that no longer exists.

## What happened

That brief asked you to teach `content_gate.py` two things: a section guide that is a range, and a rule that Core Content be at least half the workbook. Both belonged to a five-heading workbook shape ruled that morning and overturned by Kain the same afternoon, after he read the exemplar it produced and found it taught the reader nothing.

`content_gate_standards.json` has been rewritten accordingly. The `workbook` entry no longer carries a `sections` map with a two-number guide, and no longer carries `section_min_share`. **No new script capability is needed.** The entry now uses `section_count: 4`, which you already taught the script to read at S090, so the type gates today with no change to the code.

## The workbook, as it now stands

Five parts, around 1,500 words: a front cover, the teaching at around 600 words, an exercise carrying one real situation through the model, five or six discussion questions, and a back cover carrying every ask. It accompanies one lecture in one course and it teaches that lecture's idea inside itself, so a reader who never watched the lecture can still work through it. DSRD 2 section 3.4 carries the whole thing and section 3.4.1 carries the fixed copy, which is Kain's own words and is reproduced verbatim on every workbook.

## What this means for you

Nothing to build. Three things to know, for when workbooks reach import:

1. **The `workbook` type gates on structure only, deliberately.** Its entry carries a note saying so. The check that matters, whether a reader who has not seen the lecture could complete the exercise, is a human read and cannot be scripted. The shape this replaced passed every automated check it had.
2. **Two link destinations only.** Inside the working pages, the course page. On the back cover and above the discussion questions, the Achology Membership (monthly) checkout, `community.achology.com/checkout/community-subscription`, from DSRD 4 section 1.4. A third address in a workbook is a fault.
3. **The upload column contract is not settled.** The entry's `required_fields` is my reading of the type, not a fact about the theme. No workbook record exists yet. When the first one is ready to import, its contract goes through `upload_contracts.json` and is confirmed with you then.

## If you have already started

Say so through the channel and I will tell Kain. Nothing built to the withdrawn brief is wasted in principle, since a ranged section guide may be useful to a later type, but it is not needed now and should not be finished on my account.

*No em or en dashes in this file.*
