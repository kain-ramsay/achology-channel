> Chat: the stock-take fixes are in, both runs are replayed free, and the queue has run every enabled type to the end. Needs from you: three rulings (the judge, the two held types, the gate lines), listed at the foot.

# DONE: stock-take fixes, replays and the queue run (Code, factory session, 16 to 17 October 2026)

## The numbers
- **Six-word duplicate count: 0** across all 48 psychology articles (16 from the first run, 32 from the second), read off the free replays. The same check also runs on every page the worker stages now.
- **Self-test: SELFTEST OK** (read from its own log, after the last change).
- **Money: $63.47 of the $200 cap.** The queue then finished by itself: every batch of an enabled type has run. It is stopped, not looping.
- **The queue run on 17 October (12 batches, 378 records):** ready 334, needs_chat 43, error 1. By type: hub question articles 56 records, 46 ready, 10 to you; hub guides 28, 18 ready, 9 to you, 1 error; instructor articles 138, 125 ready, 13 to you; seven beliefs 9, 6 ready, 3 to you; book notes 147, 139 ready, 8 to you (two of the first 141 ready were pulled back by the stricter six-word rule after the run; the corrected replay of that batch is `replay_20261017_164843_ook-note_20261017_144524`).
- **Free replays of the earlier runs, with the repair fix:** first run of 16, 11 ready; second run of 32, 23 ready (34 of the 48 psychology articles ready, 14 to you). Q001 (49 records) 36 ready, 13 to you (was 31 and 18). Q002 (7 records) 5 ready, 2 to you.

## What I did to your two rulings
- **Repair splice (S428 sections 1 to 3):** the repair now swaps the writer's whole changed span for the original span (it widens over the original sentences the writer merged, and swaps the whole paragraph if a duplicate would remain); a free check blocks any paragraph where two sentences share their first six words or six words in a row (an overlap the original already carries is not counted); a fact check that says "no issue" is never repaired; links are compared as sets; the writer's rules gained the keyword, comma splice and one number style lines. The "fact check unreadable" cause was not the output limit: the checker sometimes writes a second, corrected answer after the first, and the reader failed on two answers. The reader now takes the last one (the limit was raised too).
- **Gate findings 10, 12 and 13 (S428 cloud ruling):** all fixed in `content_gate.py`, each with a test. Gate tests 390 of 390 pass; fixtures 43 of 43. Worker guard: a staged record whose `kain_approved_paragraphs`, `brief_state` or `signed` differs from the original is blocked, and I added `partial_edit`, `voice_standard`, `voice_line_exception` and `post_status` to the same guard after cloud review 2.
- **Record facts:** Zimbardo's Belgian soldiers line is corrected from his 1969 chapter (read on pages 272 to 276: hooded soldiers gave shorter shocks, 1.35 seconds against 2.04, which he put down to their uniforms); the Beck link is `/doi/`. Three staged biography fixes applied (de Botton, Schopenhauer, Duhigg). Erikson and Mill Sourcing records now carry the Childhood and Society and Autobiography chapter 5 lines.
- **S428b (your Friday ruling):** four types enabled, book note heading check fixed (it now accepts the pack's five locked headings; the replay was 5 of 5 ready, so enabled), Q001 and Q002 replayed, queue restarted for enabled types only. The judge is now a NOTE in the log and TO Chat, never a hold.

## Held, and why (one line each)
- **quote-page:** held by your ruling (S428b item 5). Causes in the test runs: growth past 130 per cent on short originals, a repaired sentence that carried the course link, and old headings (the check now accepts the four locked ones). Test run before you rule: 26 of 45 ready, then 16 of 50 and stop rule 1.
- **help-answer:** held by your ruling. Causes: growth limit, a changed link text, repeated emphasis words.
- **The 14 signed biographies** are not imported yet (Kain said to leave the import for later).

## Needs from you (rulings, no rush)
1. **The judge.** It contradicted your read (it passed 1 to 3 of 5 on pages you read as ready). I made it a note, as your S428b implied. Please rule whether it stays a note, is retired, or is re-tuned to the gold.
2. **Quote pages and Help answers:** the growth limit (130 per cent) is the main cause on short originals. Your six gate lines to Kain cover it.
3. **Cloud review 2 (branch `cloud/factory-review-2-s170`, `FACTORY_REVIEW_2_S170.md`):** four ways a record can excuse its own gate lines (partial_edit plus an old date, post_status publish, any text in voice_line_exception, reviewed_by equal to author); a missing `people-setup.php` makes a voice line print PASS; weak briefs ("TBC") pass check 5; about 40 gate lines have no test that can make them fail. Changing the gate is your ruling; I changed only the worker guard.

## Findings to pass on
- **A wrong Wiley link in 14 more records:** `wiley.com/ai/` should be `/doi/` (Beck was one of 15). Not touched; say yes and I fix them in one pass.
- **Hub guide "applied-psychology"** keeps dropping a quoted search phrase ("what is the meaning of life"); the check blocks it correctly and it goes to you.
- **Two factory sessions** both carried S171 (the Data Labs note covers it). I am the one that holds `api_worker.py`.
- A small Opus test batch was submitted and stopped (under $1, not collected); the per-type writer model setting stays empty, all types on Sonnet 5.5.

OWED BACK: your three rulings above.

*No em or en dashes in this file; checked before writing.*
