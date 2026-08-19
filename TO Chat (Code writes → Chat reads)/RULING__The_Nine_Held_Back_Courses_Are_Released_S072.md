# RULING: the nine held back courses are released, and the twelve repeated questions are rewritten

**DOCUMENT TYPE:** ruling, from Claude Code, Session 072. **Date:** 19 August 2026.
**Ruled by:** Kain, directly in the S072 sitting. Two rulings, both acted on the same session and both filed here under Harness Rule 14.
**Changes:** `RULING__Courses_004_And_007_Join_The_Held_Back_Set_S289` and point three of the five point delivery plan.
**Read with:** `REPORT__Five_Held_Courses_Written_And_The_Twelve_Questions_Resolved_S072.md`, beside this file.

---

## Ruling one: the held back set is empty

**Kain's words, opening the session:** "Both 001 and 010 are clean on mapping now, so the nine held courses can run."

### What the ruling rests on, read from the data rather than recalled

`Karen's watch list ANSWERED (19 August 2026).csv` holds all 28 rows answered. Twenty three read yes. The five that read no are 001-018, 001-019, 010-094, 010-100 and 010-108, and all five were settled before this session opened: course 001's sheet was corrected during S070, and course 010's fourteen name offset was corrected at S071 on Kain's ruling, with the fifteen physical Drive files renamed through the Drive connector.

So the one question the held back set existed to protect, whether the file holds the lecture the spreadsheet says it holds, is answered on every row it covered.

### What was actually changed

**Three scripts each carried the same held set and each refused independently**, which is why releasing one would have produced a run that started the nine courses and then quietly did none of their closing work:

- `run_courses.py` refuses to run a held course
- `supervise_run.py` refuses to restart the driver on one
- `close_courses.py` refuses to push a held course's descriptions or bank its transcripts

All three now read `HELD = set()`, with the previous nine recorded in a comment beside it. **The set was emptied rather than deleted on purpose:** the refusal it feeds is still the thing that would stop a course running before its mapping was settled, and a guard removed is a guard nobody can put back when the next watch list arrives.

The supervisor and the closer were restarted so the change is actually in force, since both read the set once at import. The driver was deliberately left alone: it was mid course, it exits on its own when its queue empties, and the supervisor then starts the nine from the new file.

### What this means for the run order

The nineteen unheld courses run first, exactly as before. When the last of them closes, the supervisor walks into 001, 003, 004, 007, 008, 010, 012, 013 and 014 without anybody present.

## Ruling two: the twelve repeated question lines are rewritten

**Kain's words, on being shown the twelve and asked:** "Yes, please do Claude - thank you so much!"

Twelve question lines were in use on more than one lesson across the library, all of them between courses written in earlier sessions. **Thirteen rows changed, not twelve**, because one question was in use three times. The rule applied was Kain's: the later row of each pair takes the new wording, and the earliest row of each group stays exactly as it was.

Only the first line of each description moved. The answer paragraph and the closing line were left untouched, which means every new question had to be one the existing answer already answers, so each was written against that row's own answer read on the spot rather than against its title.

**Course 026's four rewritten rows were already live in Vimeo**, its descriptions having been pushed when the course closed. 026 was therefore pushed again and all thirty six read back and verified.

## What Chat is asked to do with this

Fold ruling one into the delivery plan and into the S289 held back ruling, both of which now describe a state that has passed. Fold ruling two into the record for the description commission. Nothing here needs a reply.

*No em or en dashes in this file; checked before writing.*
