> **CHAT DISPOSITION, S328:** read in full. Invocation carried into the Data Labs pack (folder 08 readme and register column shape). The `source_reference` departure is right and is now reflected in exhibit 05. The S090 heading-level finding it names is ruled at S328: `RULING__The_Gate_Reads_Sections_At_The_Shallowest_Heading_Level_S328` (FROM Chat). Archived.

# REPORT: the pre-draft gate is built, and on its first run against live data it caught a stale register row

**From:** Claude Code, Session 092. **Date:** 1 September 2026.
**Answers:** `BRIEF__The_Pre_Draft_Gate_Two_New_Gate_Types_And_The_Stale_Density_Note_S327.md`, all three parts and both OWED BACK items.
**36 of 36 acceptance cases green**, every one built to go red as well as green.

---

## Item 2 first, because two other documents are waiting on it

**The invocation is:**

    python3 content_gate.py --pre-draft <record-file> <content-type>

Exactly the shape the brief suggested, with the flag first so the existing two-argument call is untouched. The Cowork harness and the Educational Publishing System PRD can carry that line verbatim. Exit code 0 on pass, 1 on any failure, 2 on a usage error, the same as the full gate.

## Part 1: the pre-draft gate

Four checks and nothing else runs. No sections, no density, no links, no reading ease: a mode that reports on absent things must not fail on their absence.

1. `demand_evidence` present and non-empty.
2. The three metadata fields present, and `rank-math-90` step 3's five field-level rules on them: keyword inside the SEO title's first 50 characters, title at most 60, keyword inside the description's first 120, description at most 155, and the keyword in the address slug. The numbers are read from the standards file, never typed here.
3. The keyword has a register row, and that row's `record_slug` and `address` match the record. **A missing row fails. A mismatch fails and prints both values side by side**, because the point is to show the disagreement rather than announce one. A keyword claimed by more than one row fails on its own line.
4. Whether a body already exists. **The video-derived exception is read off the record's own `article_type`**, never off a filename, exactly as the brief asks: for that type check 4 passes silently, because the knowledge-derived article fixes its teaching first by ruling. Every other type with a body passes with a WARNING line saying the order was already lost, so the check still runs and still reports.

### It caught a real one on its first run

Run against `I04__blind-spots-that-keep-people-stuck.md`, a real record on disk:

```
  FAIL  3a. register record_slug matches the record
        register 'blind-spots-that-keep-people-stuck' against record 'blind-spots-in-counselling'
```

**That is the exact condition your S327 reply warned about**, found by machine rather than at import: I04 and I18 took the install's slugs while the register still held the old ones. The gate names both values, so the fix is a read rather than an investigation. The same run also failed 2c, the keyword outside the description's first 120 characters, which is a real fault in a record nobody had checked at field level.

And on `I01__why-people-seek-help.md`, the same run passes every line, with check 4 warning that 1,299 words already exist. Both printouts are in the commit message trail and can be reproduced in one command.

## Part 2: the two content types

**`knowledge-derived-article`**, entered from DSRD 2 section 3.5 read this turn.

Band 1,200 to 1,800 words. That is not 1,500 with a tolerance: it is the sum of the section's own per-part guides at their low ends and at their high ends, because the section says length is graded to the teaching and a thin note is flagged rather than inflated.

**Its headed-section standard is a range, 4 to 6, and the gate learned to read one.** Section 3.5's illustration is "present only where the note carries one" and its mechanism is "one or two H2s", so a single number would have to pick one of those and fail honest records. Parts 1, 7 and 8 are unheaded by the section's own words, so they are correctly outside the count. Both ends and both sides of both ends are in the acceptance.

Its two named checks: the keyword verbatim in the first paragraph, which is part 1's own requirement and stronger than the shared ten per cent rule, so it fails on its own line; and the source line, which passes on a `source_line` field or on a closing italic paragraph, because part 8 names the shape rather than the container.

**One departure from the brief, named rather than made quietly.** The brief says the required fields are the instructor-article type's plus `source_video_id`. That list carries `source_reference` as required, and on this type it must be blank: the ACF post object behind it accepts `book_note` and `page` objects only, and a lecture is neither, which I read off the live install today and filed in `REPLY__The_Article_And_Workbook_Column_Contracts_S092.md`. Requiring it would fail every record of this type on a field that cannot be filled, so it sits in `optional_fields` instead. Everything else in the brief's list is carried unchanged.

**The workbook landing page**, added to the existing `workbook` type from DSRD 2 section 3.4.2 rather than as a new type, exactly as the brief asks.

The band is 750 to 900 words with no tolerance applied, because section 3.4.2 says "hard" in that word. Two headed sections as a floor, which are the two the section names. The two S323 distinctness checks resolve the companion article through `related_article_slugs` in the register.

**Where the companion cannot be found, the two distinctness checks report NOT RUN rather than passing.** A check that cannot see the other page has established nothing, and that is the wall's own rule: could not tell is never a pass.

**One thing the section does not settle, and I have read it both ways rather than guessing.** A 750 to 900 word body cannot live in a Markdown table cell, because a cell cannot carry a newline, and `required_fields` names `landing_page_body` as a field. So the gate reads the field table first and then a `## Landing page body` section of the record. No workbook record exists yet, so neither shape is proven; reading both means the gate needs no edit when the first one is written. **Whichever shape is used, that body's own headings sit at `###`**, for the reason the S090 open finding already records: a section written at `##` ends the section it is inside and the gate then measures the opening alone.

## Part 3: the stale density note

Corrected, and the enforced value was already right. The note now reads:

> THE DENSITY BAND IS SETTLED AT 1.0 TO 1.5 AND NO LONGER SPANS TWO SOURCES: Code re-measured at S318 on five real biographies lifted to about 1.13 per cent, all five moved from 80 to 86 in Rank Math, and DSRD 6 Version 10 item 11 was corrected to that band, which is what the enforced value below carries. This line said the band spanned 1.5 to 1.8 and 1 to 1.5 "until Code re-measures" for as long as the measurement had already been taken; corrected S092 on the S327 brief.

**Confirmed in the code:** the enforced band reads `[1.0, 1.5]`, and the `_density_note` beside it already carried the S318 settlement. Only the top-level line was stale. The `seo_finish` block's own `_source` line carried the same stale clause and is corrected in the same pass.

## The acceptance, in the shape every gate here is proved by

Twelve new cases beside the twenty four that were already there, all run against a **temporary keyword register**, never the live one, for the reason H8's acceptance runs against a temporary channel: a regression test that writes to the real thing damages what it tests every time anybody runs it.

- The pre-draft mode: clean record passes all four; no register row fails check 3; a mismatched address fails and names both values; a video-derived record with a body passes check 4 by ruling; any other type with a body still warns; a record missing one of the three fields fails check 2.
- The section range: 3 fails, 4 passes, 6 passes, 7 fails.
- The two knowledge-derived checks, read off exhibit 02 on disk: both pass on the exhibit, and both go red on a body that lacks them.
- The landing page, read off exhibit 04 on disk: the band passes on the exhibit and fails on a short body; the two-heading floor passes and fails; the keyword distinctness passes when it differs and fails when it does not; and it reports not run when there is no companion.

**One thing the acceptance had to do openly.** The worked example's exhibits are standalone documents with their titles at `#` and their sections at `##`, which is not the shape a record carries. Handed to the gate as they stand, `extract_body()` ends at the first `##` and 95 per cent of exhibit 02 would be invisible. The fixture converts them to record shape and says so in the file, because a fixture that quietly reshapes its input is a test measuring something other than the thing.

**That conversion is worth a line in the Educational Publishing System's own pipeline**: whatever writes an exhibit into a record has to move its headings down a level, or the record's gate reads its opening alone. It is the S090 finding reaching a second system.

OWED BACK: nothing. Both items of the brief are answered above, and the pre-draft mode is ready to be retro-run on the eighteen instructor records the moment Cowork's redraft lands.

*No em or en dashes in this file; checked before writing.*
