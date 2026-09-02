> **CHAT DISPOSITION, S332: acted on and archived.** Kain ruled: Rank Math's density test is refused site-wide and the house band governs; RULING__Rank_Maths_Density_Test_Is_Refused_And_The_House_Band_Governs_S332.md in FROM Chat; DSRD 6 Version 11 item 11 records both refusals. Board: the site-wide Rank Math bar card at close.

DONE: the Content AI test is off site-wide, proved on six page types, and one finding needs a ruling. Answers BRIEF__Switch_Off_Rank_Maths_Content_AI_Test_Site_Wide_S332.md.

# REPORT: the Content AI test is off site-wide, and the two density measures disagree

**From:** Claude Code, Session 096. **Date:** 2 September 2026.
**Answers:** the OWED BACK line of `BRIEF__Switch_Off_Rank_Maths_Content_AI_Test_Site_Wide_S332.md`.
**Board card:** the site-wide Rank Math 81 bar by page type.
**Shipped:** theme v0.133.0, deployed and proved (server, local and zip all agree).

---

## 3. The mechanism, answered first because it changes how the rest reads

**It is the same mechanism widened, not a second one beside it.** One filter on `rank_math/researches/tests`, in `rank-math-feed.php`, holding one list. That is where the policy-page fix was made on 19 July and it is where this was made tonight.

**And it had never worked.** The filter unset `contentAI`. Rank Math's key is `hasContentAI`. So the Content AI test was never declined, and every article, book note, biography, help answer and page on the install had been carrying its failure for six weeks. The old comment in that file said unsetting a key Rank Math does not define is harmless, which is true and is exactly how the silence survived: it made a miss read as a deliberate allowance.

**It cannot fail quietly again.** Every declined name is now checked against what Rank Math actually offered, and a name that matches nothing is written to the error log with the keys on offer. A rename now announces itself instead of costing another six weeks. Kain found this one, on a page he expected to be clean.

## 1. Six page types, before and after

Read with `tools/score_run.py`, which opens each editor, reads the analyser's own number and saves nothing, so no modified date moved.

| Page type | Post | Before | After |
|---|---|---|---|
| Instructor article (draft) | 34254 | 75 | **79** |
| Book note | 33852 | 18 | **19** |
| Author biography | 33718 | 80 | **84** |
| Help answer | 10878 | 47 | **49** |
| Policy page (Privacy Policy) | 126 | 86 | **91** |
| About | 184 | 89 | **94** |

**Every one moved, which is the proof the test is gone on every type rather than on articles alone.**

**One substitution, named rather than quietly made.** The brief asked for the homepage. `show_on_front` reads `posts`, so the front page is not a page object and Rank Math has no analysis of it at all. About was used in its place, and the homepage cannot be scored by anything until it becomes a page.

## 2. The fifteen instructor articles, re-read

| Before | After | Count |
|---|---|---|
| 75 | **79** | 13 |
| 77 | **81** | 2 |

**Two now meet the 81 bar. Thirteen are two points short.** Post IDs 34254 to 34282, the full table is in `RULING__The_Fifteen_Are_Held_To_The_Standards_They_Were_Written_To_S096.md`.

## The finding, and it needs a ruling before anyone tries to close those two points

**Our density band and Rank Math's density test measure different things, and on a multi-word keyword they pull in opposite directions.**

`content_gate.py` line 585, read this turn: `dens = round(100.0 * hits * kw_words / len(ws), 2)`. It multiplies the hit count by the number of words in the keyword. Rank Math counts occurrences against total words and does not.

On I01, whose keyword is three words: the gate reads 1.54 per cent and calls it **too high** against the 1.0 to 1.5 band. Rank Math reads 0.34 per cent on the same body and calls it **too low**. Both are correct arithmetic on the same page.

**What that means in practice.** For a three-word keyword, the gate's ceiling of 1.5 is about 0.5 on Rank Math's scale, and Rank Math wants considerably more than that. **No article with a multi-word focus keyword can pass both**, and every keyword in this batch is three to six words. Chasing Rank Math's test breaks the gate; satisfying the gate guarantees Rank Math's failure.

**This is not Code's to settle.** DSRD 6 section 5 item 11 owns the band, and the band was set at S318 from Code's own re-measure, which means it may have been measured the gate's way rather than Rank Math's. Either the band is restated in Rank Math's terms, or the density test joins the four already refused. **Both are rulings, and until one is given the two points on thirteen articles cannot honestly be chased.**

The other failing row on those articles is the address length, 97 characters against Rank Math's preference. That is the S309 ruling's own consequence: the addresses were deliberately set to the full focus keyword. Naming it here so nobody treats it as a defect.

---

OWED BACK: Kain's ruling on which density measure governs, through Chat, before any work is done on the remaining two points.

*No em or en dashes in this file; checked before writing.*
