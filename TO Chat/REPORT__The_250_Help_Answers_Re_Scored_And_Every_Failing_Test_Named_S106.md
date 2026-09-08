# REPORT: the 250 help answers re-scored, every failing test named, and each one routed

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Answers:** `BRIEF__Score_And_Finish_Every_Published_Knowledge_Hub_Page_S315.md`, jobs 2 and 3, for the help answers. **Companion:** `RULING__Kain_Moves_The_Help_Answer_Bar_And_Closes_The_Block_S106.md`, which carries Kain's ruling and must be read with this.
**Board card:** the 250 help articles.

This is the score table. The Publish Ready Pipeline section 5.2: a score is written only by Code, only from a built page, only here. Every number below was read this session by opening each page's editor and reading Rank Math's own assessor, through `tools/score_run.py`, which saves nothing and moves no modified date.

---

## 1. The scores

**250 of 250 published help answers read. 241 are under the bar of 81.**

| | |
|---|---|
| mean | 73.5 |
| median | 73 |
| lowest | 18 |
| highest | 82 |
| at or over 81 | 9 |

| band | pages |
|---|---|
| 10 to 19 | 1 |
| 60 to 69 | 26 |
| 70 to 79 | 214 |
| 80 to 89 | 9 |

**Code's score table now holds these 250 rows**, each with its live focus keyword beside it, and the table it replaced is kept beside it. That matters: the rows it replaced were wrong, not merely old. One page the old table recorded at **6** reads **79** live, and the old table's mean for these 250 was 17. Any figure taken from that table since it was written is unsafe, whoever quoted it.

## 2. Every failing test, across 248 pages read

Read with `tools/score_tests.py`. Two pages could not be read and are named at the foot.

| test | failing | passing | who owns it |
|---|---|---|---|
| `lengthContent` | 248 | 0 | **nobody: unearnable** |
| `keywordInImageAlt` | 247 | 0 | **nobody: unearnable** |
| `keywordInSubheadings` | 229 | 19 | content |
| `keywordInPermalink` | 184 | 63 | see section 4 |
| `keywordInMetaDescription` | 30 | 217 | content |
| `keywordInContent` | 26 | 222 | content |
| `keywordIn10Percent` | 25 | 222 | content |
| `titleStartWithKeyword` | 3 | 244 | content |
| `contentHasShortParagraphs` | 1 | 247 | content |
| `keywordInTitle` | 1 | 246 | content |
| `contentHasAssets` | 0 | 248 | **see the warning below** |
| `linksHasExternals` | 0 | 248 | clean |
| `linksHasInternal` | 0 | 248 | clean |
| `linksNotAllExternals` | 0 | 248 | clean |

**Do not read that table as a score, and this is the trap `score_breakdown.py` exists to stop.** `contentHasAssets` shows zero failures and earns **1 point of 6** on every page measured. A pass count is not a score. The arithmetic below comes from the per-test point values, not from this column.

## 3. Where the missing points actually are

Taken apart on three pages, at 64, 73 and 82, with `tools/score_breakdown.py`, which reads each test's own `score` and `maxScore`:

**Unearnable on every help answer, 15 of the 85 points on the sheet:** `lengthContent` 0 of 8 (Rank Math's floor is 600 words and the type is deliberately shorter), `contentHasAssets` 1 of 6 (no images), `keywordInImageAlt` 0 of 2 (no image, so no alt text).

**So the ceiling is 70 of 85, which reads as 82, and the bar is 81.** The nine pages at or over the bar are the nine that already get everything else right. This is the finding behind Kain's ruling, and it is in the companion file.

**Earnable and currently lost:** `keywordInPermalink` 5, `keywordInSubheadings` 3, `keywordIn10Percent` 3, `keywordInContent` 3, `keywordInMetaDescription` 2.

## 4. Routing, per job 3 of the S315 brief

**Not one failure is a template fault.** The theme's own tests are clean across all 248: internal link, external link, and the not-all-external check pass everywhere. Nothing here is Code's in the theme.

**Body and metadata faults, content, and therefore Cowork's or yours:**

- **`keywordInSubheadings`, 229 pages, 3 points.** The keyword appears in no H2 or H3. This is the largest single fixable block and the cheapest: one subheading per page carrying the phrase.
- **`keywordInMetaDescription` 30, `keywordInContent` 26, `keywordIn10Percent` 25.** Metadata and opening-line work.
- **`titleStartWithKeyword` 3, `keywordInTitle` 1, `contentHasShortParagraphs` 1.** Individually named on request.

**`keywordInPermalink`, 184 pages, 5 points, and this one is a decision rather than a task.** The keyword does not sit inside the address. Two routes, and they cost very different things:

1. **Move the address to fit the keyword.** 184 live addresses change, which is 184 redirect rows, on a redirect chain that is already a named blocker. Expensive, and Code's to execute.
2. **Move the keyword to fit the address.** Metadata only, no redirects, and it is the direction the `rank-math-90` skill was already corrected in at S337: "the focus keyword is the short phrase inside the question, never the whole question." The 63 pages that already pass this test average 77.7 against the other 184 at 72.1, measured across the set.

**Code recommends route 2**, on cost and on the skill's own correction. It is a keyword decision, so it is the register's owner's call, not Code's.

## 5. The one page that is a different problem

`download-achology-community-app`, post 375, scores **18**. Every other page on the site is between 64 and 82. Its keyword is "how do I download the Achology community app", eight words, the longest on the site, and it is the only page in the 10 to 19 band. It wants looking at on its own rather than as one of 241.

## 6. Two pages could not be read

`10049`, no per-test source found. `10030`, the editor's own store threw while being read. Both carry scores in the score table from the full run; only their per-test detail is missing. Neither is a fault in the page as far as this can tell, and they are re-readable on request.

---

OWED BACK: your brief on the two `keywordInPermalink` routes, and the keyword and subheading pass on the 241 routed to Cowork. The gate's own number waits on the companion ruling file.

*No em or en dashes in this file; checked before writing.*
