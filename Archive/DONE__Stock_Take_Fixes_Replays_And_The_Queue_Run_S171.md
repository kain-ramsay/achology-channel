DISPOSITION, Chat S438 open (21 October 2026): ACTED ON AND ARCHIVED. The rulings it asks for (the judge, the growth limit and the six gate lines, cloud review 2, the quote page provenance wording, Joseph Campbell) are answered in NOTE__The_API_Worker_Stands_Down_Until_The_Vault_Is_Proved_S438: the worker stands down until plan step 7 passes; the gate's lines are rebuilt from the vault's 04 Words and 06 Shapes at step 2; a book title repeated is one name, not a splice, but nothing is imported until Kain says. Board cards moved: the API worker card.

DISPOSITION, Chat S437 close (21 October 2026): the fact this file waited on, the S430 newsroom session and Kain's reading of the exact instructions, has passed. It is cleared at the Session 438 open as that session's first act, before step 1 of the vault plan: acted on, its facts written into the document that owns them, and archived. Named in the Session 437 Handover as the harness break it is.

DISPOSITION, Chat S429 close: stays for one fact: the Fable newsroom session (Chat S430) has checked the newsroom plan and house book and Kain has read the exact instructions; Kain ruled at S429 that nothing goes to Code before that. Named in the Session 429 Handover.

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

**Update, 17 October:** the Wiley link fix is done on Kain's yes: 29 links in 15 Content Records changed from `wiley.com/ai/` to `wiley.com/doi/`; none is left. Pages already on the install keep the old link until they are next updated from these records.

**Update, 17 October, the biography import (Kain said yes):** 13 of the 14 signed biographies are updated on the build site and read back (all 13 pages answer 200 and carry the record's last paragraph): Schopenhauer, Ariely, Goleman, Fromm, Erikson, Mate, Yalom, Piaget, J S Mill, Plato, Hanson, Greene, William James. Route: gate run on each, `publish_gate.py --clear --update` (clearance 7fb0a1147f7ddd95, 13 pages, nothing an update breaks), then `update_published_records.py`. Gate: every record fails only the known lines (the empty stances field on all, one short paragraph on Goleman, seven shared words on Yalom and Piaget); nothing new. The DSRD 6 spot check drew these five for the human read: Mate, Hanson, Erikson, Yalom, William James.
- **Held off the update: Joseph Campbell.** My six-word check finds one hit (the title "The Hero with a Thousand Faces" twice in one paragraph, "five years before The Hero with a Thousand Faces"). Your ruling takes any hit off the list, so I held it. Say the title repeat is allowed and I update it.
- Rank Math scores are not read; Kain's one-click rescore is the route.

**Update, 17 October, quote pages and Help answers prepared for the day Kain rules (free replays, nothing sent):**
- Quote pages, Q011 (45 records) now 28 ready (was 26); Q012 (50 records) now 22 ready (was 16). The biggest cause left in Q012 is the writer using "I" ("I read it as", "I'd"), which the gold quote page never does; I added a writer rule against it. Other causes: link text (5) and short originals growing past 130 per cent (2).
- Help answers: the two five-record test runs replay at 4 of 5 and 3 of 5 ready; the causes are a changed link text and one fragment the fact check named.
- The types stay held by your ruling. When Kain rules on the growth limit and gate lines, the worker needs one status change and a restart.

**Final update, 18 October (Kain said yes to running quote pages and Help answers, and asked for batches side by side):**
- **The queue now submits up to four batches of one type at once** (self-test passes, including a parallel case). It is finished again at **$100.13 of the $200 cap**.
- **Totals, from the queue log: 28 of 31 batches, 1,065 of 1,180 records. Ready about 805, needs_chat 244, error 1.** (The log says 807 ready; two book notes were pulled back by the replay.)
- **Help answers: all 8 batches, 324 records: 285 ready, 38 to you** (growth limit did not block them with the word budget given to the writer).
- **Quote pages: 6 of 9 batches, 300 records: 150 ready, 145 to you. Stop rule 1 holds the type with 3 batches (115 records) not run.** First pass 35 of 200 ready; after the provenance-sentence fix 84 of 200. What still blocks most pages: the writer follows the pack's ruled provenance sentence ("taken from his course", with the course link), the fact check repairs it back to the record's original wording, and the link is lost. **Needs your ruling: which wording wins, the pack's formula or the record's original, and the repair should then keep the link.** I did not loosen any check.
- **Still held for you:** Joseph Campbell's biography (title repeated), the judge ruling, the cloud review 2 gate lines. Nothing is on the live site; all pages wait for your read and Kain's signature.

OWED BACK: the quote page provenance ruling, plus the three rulings above.
