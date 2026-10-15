> Chat: Job 3 of BRIEF__API_Worker_Takes_Help_Answers_And_Quote_Pages_Short_Reading_Lists_Quiet_Gate_S426 is built; nothing is needed from you except the points at the foot.

# DONE: short reading lists for every type, and the tokens-read column (Code, factory session, S170, Thursday 15 October 2026)

**What is in.** `READING_LISTS` in `api_worker.py`, beside `SETTINGS`, one entry per type, each naming files (nothing else is read): help answer (PACK_04 files 02 and 03; gold: the two HELP records the brief names), quote page (PACK_03 files 02 and 03; gold: record CQ001-144-1, the signed exemplar), hub question article and hub guide (PACK_01 file 06 and file 01, the kinds; gold: the approved `can-i-practise-cbt-on-my-own` record), author biography (PACK_02 files 01, 02, 03 and 05; gold: the two S298 frozen biographies, to be replaced by your five once Kain signs them), field authority article unchanged (file 06 and its gold). `cost_log.csv` has a new `tokens_read` column. The self-test now fails if a listed file is missing (and a probe proves that check can fail). Self-test passes; no API call was made.

**What is not in.** The worker is not yet taught the new types: `--type help-answer` and the others stop with a plain message and send nothing. Their writer rules, their free checks (quote text, author and book title word for word, the five biography headings) and the record splitting for the quote and biography layouts come with each type's dry run. The quiet gate (Job 5) still waits on Kain's Friday ruling on gate lines. Nothing costs money until the dry runs, which wait on your read of the 16 staged articles.

**Two small facts for you.**
1. The retry for an unreadable fact check (the one I asked your yes or no on) is already in the worker, added at the end of S169; it is the same call once, and a record whose second reply is still unreadable goes to you.
2. The quote exemplar lives in Content Records, not only in the skill library; the list points at that record.

OWED BACK: your read of the 16; your yes or no on the retry (already built, so a no means taking it out).

*No em or en dashes in this file; checked before writing.*
