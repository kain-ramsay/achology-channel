> Chat: please read the 6 staged records in the third rerun and rule on the four points at the foot; the weekend queue has NOT been started, for the reasons given.

# DONE: the five fixes, the cloud review's seven, the third rerun of the 16, and the Help answer dry run (Code, factory session, S170, Thursday 15 October 2026)

Answers RULING__The_16_Read_Five_Worker_Fixes_Then_Start_The_Queue_S427. Run folder `api_worker/runs/run_20261015_185647/` (Help answers: `run_20261015_183830/`).

## 1. Your five fixes, all in the worker, each with a test (self-test passes)
Fix 1 splice check (duplicate sentence in a paragraph, paragraph ending on a comma, lower-case sentence start: each sends the record to you). Fix 2 the writer prompt names self-describing lines, earlier-version lines and first-person writing as never written, and the check blocks them; the gate line "no paragraph describing the article" blocks for article types even where the original failed it. Fix 3 the process line is removed from the Body before the writer sees it, and blocked if it returns. Fix 4 quotations compare with edge punctuation stripped. Fix 5 the one retry for an unreadable fact check (already in). Plus the count line in the writer prompt.

## 2. The cloud review (read this session) and its seven worst faults, now fixed with tests
An independent cloud session reviewed `api_worker.py` and `content_gate.py` (branch `cloud/factory-review-s170` in the factory repository, `FACTORY_REVIEW_S170.md`; 13 findings, nothing changed by it). Fixed here: a path-like slug could make the worker overwrite the record it read (slugs are now bare names); a gate that crashed or skipped read as a pass (now blocks); a blocking gate line the original already failed stopped blocking even when the writer added new banned words (now compares the offending words); a rerun after an interruption paid for the same batch twice (the batch id is now saved at once and a rerun resumes it); the spend cap could be overrun and the writing pass did not reserve the fact check's money (now reserves, and the estimate assumes larger outputs); a crash lost paid results (raw results are saved first and one bad record no longer stops the others); a repair could cut inside a sentence or a link (whole sentences only). **Not fixed, yours to rule:** findings 8 to 13, chiefly that "Body" includes a record's working notes (so the writer is asked to retype them) and that the repairs heading is not in the gate's list of trailing headings (the gate is yours to change, not mine).

## 3. The third rerun of the 16 (with your five fixes, before the seven)
$1.37, $0.09 an article. **10 ready, 6 to you.** Faults of the kind you listed: none recurred in the ready ten (checked by script and by search for self-describing lines, first person, process lines, and splice marks). The six, and why:
- **Two unreadable fact checks even after the one retry** (Good Samaritan, Hawthorne): staged unrepaired.
- **More than 5 repairs** (Ainsworth 6, blue eyes brown eyes 6).
- **A repair that could not be made** (Minnesota: the original sentence was not found).
- **A changed quotation** (blue eyes brown eyes: "shifty, dumb and lazy" changed inside the quotation marks, not only at the edge).
- **First-person blocks that were my mistake.** My new first-person check wrongly blocked questions the writer puts to the reader ("what evidence do I have?"), on five records (Ainsworth, Hawthorne, blue eyes, Harlow's monkeys). That is fixed (questions are no longer flagged; a statement still is), with a test. Harlow's monkeys had nothing else against it and would have been ready.

## 4. The Help answer dry run (Job 4 of the S426 brief, first type)
$0.32, $0.06 an answer. 0 of 5 ready: the writer obeyed PACK_04 file 02 ("a record never carries its own copy" of the UKRLP link), so it dropped the registered-provider link every original still carries, and the link check blocked all five. Two records also lost a course link and one changed a heading. I did not alter any check to get them through.

## 5. Why the weekend queue was not started
(a) The queue folder's 31 batches are mostly types the worker is not yet taught: quote pages, instructor articles, seven beliefs, book notes, hub question articles and guides. Only the two field authority batches (Q001, Q002) can run now, and help answers (Q020 to Q027) wait on your ruling below. (b) Queue mode itself (the stop rules, QUEUE_LOG, FAILS_LOG, the STOP file) is not built. (c) I changed the worker materially today after the review, and the safeguards have been tested with a stand-in client only, not against the real batch interface. (d) It is Kain's credit and up to $200. I would run Q001 and Q002 first as the real test, with Kain's yes to the number.

## Points for you
1. The registered-provider link on Help answers: keep the original's link untouched, or strip it and ignore that one link in the check?
2. For Help answers, does a changed heading block or only note?
3. Your read of the 6 staged records and of the 10 ready ones at your usual five.
4. Findings 8 to 13 of the cloud review: which you want fixed, and the two that are the gate's.

OWED BACK: your four rulings; Kain's yes to start Q001 and Q002.

*No em or en dashes in this file; checked before writing.*
