# BRIEF: the pre-draft gate gains a fifth check, the Search and Citation Brief

**From:** Claude Chat, Session 329. **Date:** 2 September 2026.
**Authority:** Kain, who approved THE SEARCH AND CITATION BRIEF Version 1 in the S329 sitting (000__THE_SEARCH_AND_CITATION_BRIEF.md, at the root of the Content Production Factory folder). Section 9 of that document names this extension. This is an approved commission, not a question.
**Board card:** Article production enters through one enforced route: the Search and Citation Brief, gated by machine before any body copy (Knowledge Hub, To Do, Launch Step 6.1).
**Reads with:** `content_gate_standards.json`, which already carries the new `shared.search_citation_brief` block and the five new required fields on every type (written and re-parsed by Chat, S329). The gate reads the standard from that file and invents nothing; your check reads the block, never a constant.

---

## What exists, and what you build

`content_gate.py --pre-draft` runs four checks before a body exists: demand evidence, the three Rank Math fields with their five field-level rules, the register row and its two values, and the body-order check with the video-derived exception. **You add a fifth, in the same shape, and it refuses a record whose Search and Citation Brief is incomplete.** Everything about the four existing checks stays exactly as it is.

## The standard, in the machine's terms

Read `shared.search_citation_brief` in the standards file. It gives you: the section heading (`Search and Citation Brief`), the eight part headings in order, the claims table shape (three columns) and the three allowed claim kinds, the four `search_intent` values, the four `update_cadence` values, the `query_variants` count band, and the planned-links minimums. The owning document is the standard's section 5 (what the machine checks) and section 4 (the eight parts); where the JSON block and the document disagree, the document wins and Chat corrects the block.

## The fifth check, line by line

**5. The Search and Citation Brief is complete.** Print one line per sub-check, numbered 5a onward, PASS or FAIL, the way checks 2a to 2e and 3a to 3c already print.

- **5a. The section is present.** A `## Search and Citation Brief` heading exists between `## Page fields` and `## Body`. Read it the way `extract_body()` reads a section: everything from that heading to the next `## `. Absent: FAIL, naming the heading.
- **5b. The eight parts are present, in order, and non-empty.** Each is a `### ` heading matching the standards block's `parts` list exactly (number, full stop, wording). Match in order; a part out of order or missing fails 5b naming the first missing or misplaced part. Non-empty means at least ten words of text under the heading before the next `### ` or the end of the section; a part that does not apply satisfies this by saying so in words, per the standard.
- **5c. Part 5 is a three-column table with a source on every row.** Under part 5, the first Markdown table found has exactly three columns; every data row's second cell is non-empty; every data row's third cell is one of `claim_kinds`. Zero data rows is FAIL (a page with no claims to evidence is not a page). Any empty source cell is FAIL naming the row number.
- **5d. Part 7 names the minimum links.** Under part 7, at least `planned_links_min.internal` addresses beginning `/` and at least `planned_links_min.external` beginning `http`. Count addresses, not words.
- **5e. The four new fields carry allowed values.** `search_intent` is one of the four; `update_cadence` is one of the four; `query_variants` splits on commas into a count inside the band; `reviewed_by` is non-empty. Each fails on its own line naming the field and the value found.
- **5f. `schema_type` is present.** Non-empty. Whether the value is the right one for the type is DSRD 10 section 9's and is a human read; the gate checks presence only.

**The refusal wording.** Where any 5x line fails, the PRE-DRAFT GATE verdict is FAIL and the summary line says, in words, that drafting has not begun and names the missing parts. The standard's rule is that a missing part is a refusal, never a value the gate fills in.

**The knowledge-derived article.** No special case in check 5. Its exception lives in check 4 already (a video-derived body passes by ruling). The brief check runs on it exactly as on every other type; the standard's section 1 line 4 records that its brief is written after its teaching and before its metadata, which is a matter of when the record is run, not of what the gate accepts.

## What you do not build

- No check that a body honours its brief; the gate runs before the body exists.
- No check of whether a contribution is original or a source says what the claim says; those are human reads (standard, section 5).
- No reduced brief for quote pages or help answers; that is Kain's decision at S330 and until then every type takes all eight parts.
- No change to checks 1 to 4.

## Acceptance

Extend `content_gate_acceptance.py` in the S327 section's pattern: a temporary register, a temporary record, every case red as well as green, run against the old code first where a case claims to have caught something. At minimum:

1. A record carrying a complete brief and the four new fields passes 5a to 5f and the four existing checks: PRE-DRAFT GATE PASS.
2. The same record with the section removed fails 5a.
3. The same record with part 6 deleted fails 5b naming part 6; with parts 3 and 4 swapped fails 5b naming the first misplaced part.
4. A part 5 table with one empty source cell fails 5c naming the row; a part 5 table with a fourth kind fails 5c; a part 5 with no table fails 5c.
5. Part 7 with an internal address and no external one fails 5d.
6. `search_intent` set to `curious` fails 5e; `query_variants` with one entry fails 5e; `reviewed_by` blank fails 5e.
7. A video-derived record with a body and a complete brief passes: check 4 by ruling, check 5 on merit.
8. The S327 cases still pass unchanged.

Print the run. The definition of done is the printout in a REPORT to TO Chat with the case count, every new case red-before-green named, and the one line of the gate's own `--pre-draft` output on the instructor exemplar record once Chat has written its brief (S329, in progress).

## Sequence

Chat is drafting the instructor-article exemplar's brief now, against the standard, as the first live record in this shape. Your check is the thing that proves it. Build the check first; run it on that record when it lands in the Content Records folder; report both.

OWED BACK: the REPORT above, and any part of the standard's section 5 you find the machine cannot read as written, named rather than worked around.

*No em or en dashes in this file; checked before writing.*
