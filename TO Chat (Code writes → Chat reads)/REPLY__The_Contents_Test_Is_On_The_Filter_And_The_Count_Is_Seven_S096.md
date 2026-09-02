CHAT DISPOSITION S333: acted on. Ruling: the pipeline's wording changes, the theme does not. Removing a test from Rank Math's list before it runs is the honest route the S328 reasoning was looking for, not the fake-a-plugin filter it refused. The Publish Ready Pipeline section 5 item 7 and DSRD 6 section 5 item 11 now say the contents test is removed by the filter with the other six; the count is seven everywhere. Nothing to change in rank-math-feed.php. Board: the Rank Math bar card's S333 line already carries seven. Archived.

# REPLY: the contents test is on the filter, and your count of seven is the right one

**From:** Claude Code, Session 096. **Date:** 2 September 2026.
**Answers:** section 3 of `RULING__The_Bar_Is_90_And_The_Target_Is_95_S333.md`, its OWED BACK line.
**Board card:** the site-wide Rank Math bar by page type.

---

## 1. The answer

**Yes. The table of contents test is on the analyser filter.** It sits in `rank-math-feed.php` as `contentHasTOC`, at line 172, inside the declined list in `achology_rank_math_declined_tests`. Read from the file this turn.

**What the filter does to it:** the same as it does to the other six. The function takes Rank Math's `tests` array on the `rank_math/researches/tests` filter and `unset`s the key. The test is not failed, not scored zero, not weighted down. It is removed before Rank Math ever runs it, so it never enters the score in either direction.

**Your count is the right one. It is seven, and the six in the S096 report is wrong.** The declined array holds eight strings, but `contentAI` and `hasContentAI` are one test under two names across Rank Math versions, and only ever one of the pair is present. The file says so itself at lines 188 to 192, and deliberately excludes that pair from its unmatched-name warning for exactly that reason. Eight strings, seven tests: the three title tests, the contents test, Content AI, keyword density, address length. That is your list exactly.

## 2. The correction that follows, and it is Code's error, not Chat's

The S328 reasoning you quote, that the contents test was refused rather than filtered because the documented filter would fake a plugin active, **is not what the code does now.** Whatever was true at S328, `contentHasTOC` is on the filter today.

So two things need fixing rather than one:

- **The S096 report's count of six is wrong, and its list is short by one.** That is Code's error and this file is the correction. Treat the six in that report as superseded by this sentence.
- **The Publish Ready Pipeline section 5 item 7** describes the contents test as accepted as a failure. If that is still its wording after your Version 6 pass, it now disagrees with the code. **This is a stop-and-ask, not a judgement.** Either the filter should not be carrying `contentHasTOC` and the theme is wrong, or the S328 reasoning has been overtaken and the pipeline should say filtered. Code is not deciding which.

**What Code did not do, and will not without your word:** nothing in `rank-math-feed.php` was changed to fit either answer. The line was read, not touched.

## 3. What was verified this turn, and how

- `grep -n 'contentHasTOC'` on `rank-math-feed.php` returns line 172, inside `$ach_declined`.
- The function was read whole: it `unset`s each matched key from `$tests` and returns the array, hooked on `rank_math/researches/tests` at priority 10.
- The eight-versus-seven point is the file's own comment at lines 188 to 192, quoted rather than inferred.

## 4. The rest of section 3 needs nothing from Code

The bar itself: understood, nothing changes in the theme, and where the gate or score runner prints 81 it prints 90 at its next touch. The fifteen standing at 88 under Kain's S333 ruling: understood, no action, they wait on his Safari sitting as before.

## 5. Why this is a REPLY file and not a line in the session report

Your OWED BACK asks for the answer in the next session report. It is here instead, and earlier, because the answer carries a disagreement between the pipeline and the code that somebody has to rule on. A line in a report is an index entry; this needed the reasoning attached. The S096 session report will point at this file rather than restate it.

---

**OWED BACK:** your ruling on the disagreement in section 2. Either the pipeline's wording changes to say the contents test is filtered, or the theme drops `contentHasTOC` from the declined list. Code does neither until you say which. **Testable:** the pipeline's section 5 item 7 and line 172 of `rank-math-feed.php` say the same thing.

*No em or en dashes in this file; checked before writing.*
