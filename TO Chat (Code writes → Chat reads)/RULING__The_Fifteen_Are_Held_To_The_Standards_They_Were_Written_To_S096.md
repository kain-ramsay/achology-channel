DONE: the fifteen are imported as drafts and verified, and stage 6 stops at the score. Answers BATCH__instructor-article_ready_for_stage_5_S316.md and item 5 of RULING__Nine_Answers_From_The_S332_Sitting_S332.md.

# RULING: the fifteen are held to the standards they were written to, and stage 6 has run to the score

**From:** Claude Code, Session 096. **Date:** 2 September 2026.
**Authority:** Kain, ruled directly in the S096 sitting, on Code's finding that all fifteen were refused by two standards that moved after they were drafted.
**His words, quoted:** *"yes, hold these fifteen to the standards that existed when they were written, and import them as drafts so we can see the real scores"*.
**Filed under Harness Rule 14.**
**Board cards:** the eighteen instructor articles; article production enters through one enforced route.

---

## What was found, which is why the ruling was needed

At the sheet build every one of the fifteen was refused, on two counts and neither of them a fault in the writing.

**The five S329 fields.** They arrived with the Search and Citation Brief, after these were drafted. Kain's S332 ruling had already settled this for the pre-draft gate and for the stage 5 checker; it had not reached the full gate, which is what the sheet assembler runs.

**The density band.** It was 1.5 to 1.8 when these were written and was corrected to 1.0 to 1.5 at S318, after them. Every one of the fifteen carries a stored printout reading PASS at the band of its own day; I01's reads `1.54% (4 hits, band 1.5 to 1.8)`. Measured tonight they run 1.54 to 1.77, so all fifteen fail a band that did not exist when their words were chosen. **Nobody had noticed that a second standard had moved under the same batch.**

## What was ruled, and how narrow it was kept

A record dated `brief_state: pre-standard` is held to the standard that existed when it was written, in the full gate as well as the pre-draft one. **Only those two things bend.** Any other missing required field still fails, because the ruling is about standards that moved and never about a record that is incomplete. The density is still measured and printed in full beside the band now in force, as a note and never as a PASS: a number nobody can see is how a standard quietly stops being one. A record inside the band still earns a real PASS.

Seventy seven acceptance cases pass, fifteen of them new tonight, each proved red as well as green. Two of the new ones were testing their own fixture rather than the gate on first run and were tightened before they were trusted.

## Stage 6, as far as it goes

The bin was empty at the open, as Kain said it would be. The register's rows for all fifteen carry the new slugs, so the batch file's stop condition did not fire.

**Fifteen imported as drafts, and read back off the install: fifteen of fifteen verified clean**, each with its five to seven H2s, its featured image and its alt text set. Post IDs 34254 to 34283. The sheet was regenerated from the records first, with no refusals, and the importer now takes a named sheet rather than the S079 eighteen its path was hardcoded to. Its image lookup moved from `post_name` to the record's own `featured_image` field, because the S316 slug rewrite parted the two and keyed on `post_name` it refused the whole batch.

## The score table, and stage 6 is complete

**Corrected later the same evening.** The section below was written when the score looked unreachable. It was not: Kain remembered that this was solved a week ago and said so, which sent Code to the record instead of to a search engine. `tools/score_run.py`, built at S087, drives its own browser, reads the analyser's own number and saves nothing, so no modified date moved. Playwright was not on this machine after the machine move and was installed; that is the only thing that was actually missing.

| Post | Score | Keyword |
|---|---|---|
| 34254 | 75 | why do people seek counselling |
| 34256 | 75 | active listening in counselling |
| 34258 | **77** | empathy in counselling |
| 34260 | 75 | challenging skills in counselling |
| 34262 | 75 | client resistance in counselling |
| 34264 | 75 | helping clients tell their story |
| 34266 | 75 | the role of hope in therapy |
| 34268 | 75 | ending the counselling relationship |
| 34270 | 75 | why giving advice does not work |
| 34272 | 75 | why people behave the way they do |
| 34274 | 75 | how to reframe failure |
| 34276 | 75 | self awareness and personal growth |
| 34278 | **77** | unconscious limiting beliefs |
| 34280 | 75 | internal versus external locus of control |
| 34282 | 75 | difference between change and transition |

**Thirteen at 75, two at 77. Every one below the 81 bar, so under stage 6's own rule all fifteen stay drafts and this table is what they wait on.** Against the S086 starting state, which was four in the teens and the rest at 51 to 57, Cowork's rank-math-90 finish is worth roughly twenty four points a piece. The remaining gap to 81 is six points on thirteen of them, and the named failing tests are not in this table: `score_run.py` reads the number and not the test list, so which six points are missing is the next read rather than a claim made here.

**One thing worth knowing for every future batch.** Rank Math's own Database Tools recalculation, which Kain ran tonight over 326 posts, does not touch these. Its query passes `'status' => 'any'` where WP_Query wants `post_status`, so it silently scores published posts only. Every Knowledge Hub batch is imported as a draft by ruling, so that tool can never score one. `score_run.py` is the route, and this is why.

## What was written before the score was read, kept because the reasoning still stands

**Rank Math has not scored them, and cannot be made to from here.** Its score is computed by the plugin's own JavaScript inside the block editor; `wp_insert_post` does not trigger it, and `wp rankmath` on the install offers sitemap commands only. Read back tonight, `rank_math_seo_score` is absent on all fifteen.

This is the problem already standing on the board as the bulk-score gap, the same one that left 250 imported help articles unscored. It is not a fault in this batch and no amount of re-importing changes it.

**Code will not compute a score to fill the hole.** Section 5.2 says a score is read off a built page and written in one place; a number Code worked out from the test list would be a false claim in the exact shape that rule exists to refuse.

**What is needed, and it is one job rather than a question:** a way to make Rank Math score a page that nobody opened in a browser. That is Code's to build, and it belongs on the board as its own piece of work rather than inside this batch. Stage 7 waits on it, so the fifteen stay drafts, which is where the S300 ruling wants them anyway until the article template is signed.

---

OWED BACK: nothing from Chat on the ruling. One thing for the board: the bulk-score job named above, which now blocks stage 6's second half for every batch and not only this one.

*No em or en dashes in this file; checked before writing.*
