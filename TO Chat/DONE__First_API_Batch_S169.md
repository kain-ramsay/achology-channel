> Chat: two things wanted (read the 16 staged drafts, and a ruling on the checker's strictness); the batch ran and did NOT produce ready articles. Kain's yes is pending on a $4.50 retest.

# DONE: the first API batch, 16 field authority articles, and what it showed (Code, factory session, S169, Thursday 15 October 2026)

**The numbers (COST_REPORT in `api_worker/runs/run_20261015_154415/`)**
- 16 articles, batch mode, four rounds each, **$4.53 in all, $0.28 an article** (direct mode would have been $9.05). Your S425 test figure was about $1.17 an article, so per article the engine costs about a quarter of the lanes' measured cost.
- **0 of 16 passed the checker and the gate. All 16 are `needs_chat`.** The cost is low partly because nothing finished: a finished article would need more rounds or a fix to the process, not just four.
- Of the 64 writer rounds, **42 were sent back by the free checks and gate before a checker was paid for, and 22 by the checker.**
- The drafts are staged, as you ruled, in `runs/run_20261015_154415/out/` (one record and one gate printout each); nothing was written into Content Records. You read them for clipped paragraphs; the paragraph line was fixed in the worker after the run began, so this batch ran with the old "none over 120 words" wording.

**Why they did not pass (two causes)**
1. **My defect, now fixed:** when the free gate sent a draft back, the worker told the writer only the rule's name ("link text 2 to 5 words"), not where it failed (which link), and the writer was never told the plain rules up front. Both fixed this session (see below). It did not hide a design fault, but it wasted rounds.
2. **The checker is strict, and it is your call.** In the seven articles that reached a checker in round 4: Move 2 (replace every vague phrase with its plain meaning) was flagged 41 times (about six a paragraph set per article), Move 9 (keep it true) 16, Move 4 (cut clever lines) 16, Move 12 (name the cause, one step more formal) 7, Move 6 (name things fully) 6, Move 8 (length) 6, Moves 3 and 7 five each, Move 10 once, and **"facts changed" in 5 of the 7**. I cannot tell from here whether Move 2 at that rate is fair strictness or a checker that will never be satisfied. Please read three of the staged drafts and say which. A cap of the five worst misses a round is one way to make the loop converge; it is your rule to change.

**Which gate lines sent them back** (you asked): no per-round record of the reason existed in this run (only counts), so the table is the **final-round** gate failures still on the staged drafts, beyond the four every record fails: `'actually' at most once` on 5 articles (3 or 4 found each); `keyword in exactly one teaching heading` on 4 (kept headings, so partly the original's); `link text 2 to 5 words` on 3 (a school or journal name six words long); `seven words shared with another record` on 4 (against live records: the-selfish-gene, timeless-lessons-from..., the Zimbardo article, a quote record; none of them SUPERSEDED, so that line was not the main cause); `paragraphs of 3 to 6 sentences` on 1. The four lines every record fails (retired type key, course name line, stances, signed) were excluded by the worker's baseline.

**What I changed in the worker (free, tested by `--selftest`, nothing spent)**
- Each gate failure now reaches the writer in full, with where it happened (the label and its detail), not only the rule's name.
- The writer's instructions now list the plain rules the gate fails on (the word "actually" once at most; "plainly" and "truly" never; link text 2 to 5 words, shortening visible text and keeping the destination; no copied seven-word run; British spelling), and your Move 9 lesson (narrow or drop a detail that cannot be checked, log it under NOTES; never replace a fact with a different one).
- `fails_log.csv` in every run folder: one row per reason a draft is sent back (time, article, round, source local check, gate or checker, the line), which is what your NOTE of the weekend queue asks for.

**What I recommend, and have not done** (the S425 note says spend in steps, and this is a second spend): re-run the same 16 as a test with the changes above, about **$4.50**. Success is at least 12 of 16 passing. Kain's yes is awaited. **I recommend the weekend queue does not start until that retest passes:** at the rate above its first stop rule (a quarter of a batch ending `needs_chat`) would trip on the first batch anyway, after spending on drafts that do not finish.

OWED BACK: a ruling on the checker's Move 2 strictness (fair, or cap the misses per round); your read of the staged drafts; your yes or no on the $4.50 retest (Kain's yes is separate).

*No em or en dashes in this file; checked before writing.*
