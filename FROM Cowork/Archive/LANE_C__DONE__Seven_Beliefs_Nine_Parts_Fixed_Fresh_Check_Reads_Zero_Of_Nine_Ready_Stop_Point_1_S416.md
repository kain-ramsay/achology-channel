LANE C

**Needs from Chat:** stop point 1 of the whole-run queue has fired on Lane C item 1 (0 of 9 Seven Beliefs parts read "Ready to sign" at the fresh check, under the 85 per cent line), so the route needs Chat's look before Lane C goes on. Lane C holds item 1 open and runs nothing else until a note from Chat lands.

# DONE (stopped at stop point 1): Seven Beliefs, nine parts fixed, fresh check read

**From:** Lane C, Thursday 8 October 2026. **Run list item:** 1, `QUEUE__The_Whole_Editorial_Run_In_One_Queue_S406` Part C item 1. **Standard version checked against:** 14. **Harness:** Version 37, Recipe 9 and Recipe 10 with all readings to S412.

BOARD: The Seven Beliefs card, Lane C's share NOT done (stopped at stop point 1).

## What was done, in order
1. **Round 1, a fresh check of the nine as they stood.** Nine fresh checkers (agents that wrote none of it). Counts of things needing Kain's eye: Part 1: 20, Part 2: 19, Part 3: 24, Part 4: 20, Part 5: 21, Part 6: 20, Part 7: 18, Part 8: 29, Part 9: 18 (189 in all). Sheets beside each record as `LANE_C__CHECK__<slug>_S416_round1.md`.
2. **Fix round.** Nine writer agents fixed each record from its sheet to Version 14 (contractions, openings, link rules, closings, practice blocks, Sources lists, course paragraphs, stances, claims tables). Every unverifiable quotation was cut to paraphrase. I then made the Previous/Next titles match each part's current H1 across all nine.
3. **Round 2, a fresh check of the fixed records.** Nine different fresh checkers. Sheets: `LANE_C__CHECK__<slug>_S416.md` beside each record.

## The fresh check's top lines (0 ready, 75 things in all, down from 189)
| Part | Slug | Top line |
|---|---|---|
| 1 | standing-on-the-shoulders-of-giants | 10 things need Kain's eye |
| 2 | can-people-change | 6 things need Kain's eye |
| 3 | know-thyself | 11 things need Kain's eye |
| 4 | thinking-errors | 8 things need Kain's eye |
| 5 | understanding-and-managing-emotions | 6 things need Kain's eye |
| 6 | emotional-responsibility | 8 things need Kain's eye |
| 7 | change-your-life-from-the-inside-out | 7 things need Kain's eye |
| 8 | sense-of-purpose | 10 things need Kain's eye |
| 9 | philosophy-of-life | 9 things need Kain's eye |

Every round 1 problem was confirmed gone by the round 2 checkers. What remains is new and smaller, and falls in four kinds: (a) sourcing: claims or quotations resting on a search summary or Wikipedia, Sources entries with a library link instead of a publisher link, a source named in the prose with no link beside it; (b) the common view written as a crowd ("most of us", "people find") in Parts 4, 9 and others (reading S14); (c) titles that are statements (Parts 3 and 9); (d) single unsupported sentences (Part 2 closing contradicts a James quote, Part 5 breathing instruction, Part 6 Satir paragraph, Part 9 Bernard of Chartres, Part 1 Korzybski wording). Each sheet carries its fix already written. The next fix round would be small, and I can run it on Chat's word.

## Gate and repeat printouts
`content_gate.py` prints FAIL (3) on Parts 2 to 9 and FAIL (2) on Part 1. Every FAIL is one of two things: the Previous/Next/Back-to-start block (link text over five words, two links counted in one paragraph), and the empty `signed` field. The block is named exception (o) in the Standard (section 15.2 item 4), which the gate does not code for records dated after the S396 line; the `signed` field stays empty by rule. The checkers read both as notes. `check_no_repeats.py` prints FAIL on the whole set only on the approved help-line wording and on Sources entries naming the same work in two parts. Printouts: in each sheet under Gate; the writers' own printouts are in Lane C's scratch folder.

## Lines of the Standard or harness I read two ways (please rule)
1. **The Seven Beliefs have no row on the stance map.** I treated the set as a type with no subject: each record's `stances` field names the stances the belief touches and the checker judges fit.
2. **Does the gate need to code exception (o)** (series links) for records dated after S396? Today it fails them. Gate fix for Code, through the defect register.
3. **`check_no_repeats.py` and the help line (Part 6 rule 8) and shared Sources entries (reading S2):** the script exempts only the seven belief statements and quoted words. Either the script gains the help line and bibliography exemptions, or the help line is to be reworded per part (which Part 7 rule 15 forbids). Lane C read the help line and shared citations as allowed.
4. **Part 1's H1 and title now read "What Are the Seven Beliefs Achology.com Is Built On?"** (a question, with "Achology.com" at first mention, S21). The writer changed it; Kain's approved title was "The Seven Beliefs Achology Is Built On". Please confirm Kain wants the series' first title changed, or restore it.
5. **Part 9's title is now "Seven Beliefs, One Attitude to Life"** (writer's change; the checker says a question is needed for the search title).
6. **Pre-draft gate** prints FAIL on all nine only because bodies already exist (a fix job, not a draft); the brief checks pass.
7. **Writer model:** CLAUDE.md sends writing to the Sonnet writer agent; Recipe 9 names the strongest model for the Seven Beliefs. I used the writer agent as CLAUDE.md says.

## Not verifiable by agents, owed to a person
- Newton's letter to Hooke (Historical Society of Pennsylvania page, 403 on every try): the quotation was cut to paraphrase; someone should open the page once.
- Schwartz's value grouping (Part 8, paper returned 403) rests on Wikipedia; Campbell's quotation checked only against Wikipedia.
- Covey (Part 7) claims rest on web summaries, publisher page 403.
- Pictures: no `.webp` found for any part; checkers marked "not looked at"; Part 7's alt text does not match the only placeholder found.
- Several Sources entries carry library-catalogue links because the publisher pages blocked the fetch.

## Housekeeping
One checker deleted its own helper files from Lane C's scratch folder (it cleared files starting `LANE_C__` there). No sheet or record was affected; I confirmed all nine round 1 and nine round 2 sheets exist. Nothing was written outside the Seven Beliefs folder, Lane C's scratch, and this file. No git command was run.

COWORK | Batch: Seven Beliefs Parts 1 to 9 | Drafted: 9 of 9 fixed | Gate and evaluator: 9 awaiting escalation (gate FAIL is the exception (o) block and the empty signed field only) | Checked: 0 ready to sign, 9 with problems (75 things in all) | Skipped: none | Outside brief: none

**OWED BACK:** Chat's call on the route (rulings 1 to 5 above) and a go for a second small fix round.

*No em or en dashes in this file; checked before writing.*
