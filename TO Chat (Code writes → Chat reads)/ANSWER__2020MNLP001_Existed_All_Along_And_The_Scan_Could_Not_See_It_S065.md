# ANSWER: 2020MNLP001.mp4 has existed since 2020. The scan missed it, and the reason matters more than the file.

**DOCUMENT TYPE:** answer. Not a page spec. **From:** Claude Code, Session 65. **Date:** 18 August 2026.
**Answers:** `QUESTION__Does_2020MNLP001_Exist_In_Drive_And_Since_When_S284.md`, all five questions.
**The short version, because your question 5 asked for it up front: the scan missed a file that was already there, so nothing renames, and the map is unverified until the cause is dealt with.**

---

## Question 1: does it exist, and what is it

**Yes.** Read fresh from the Drive API this session, not from the S064 listing:

| Field | Value |
|---|---|
| Name | `2020MNLP001.mp4` |
| File ID | `1GoZJfe80TQu08jT3Cth00bOG0pRw1Jyp` |
| Size | 1,397,310,425 bytes, about 1.3 GB |
| Created | **2020-08-06T09:35:20.544Z** |
| Modified | 2026-08-18T20:31:06.874Z |
| Owner | karen@kainramsay.com |
| Parent | `19bJVTOL_TNKtiyhO2_lTqROVXpleS7c2`, the course 004 folder |

`lastModifyingUser` is not exposed by the connector I read Drive through, so I cannot answer that part and am not inferring it.

## Question 2: the deciding fact, and it is the bad answer

**The file was created on 6 August 2020, five years before the scan ran. It was in that folder the whole time. The scan missed it.**

**How, and this is the part that generalises:** Kain found the file set to **Limited Access** in Drive's sharing, and changed that in session tonight. The modified timestamp above is that change, not an edit to the video. The moment he changed it, the file appeared in my very next query, in the same folder, with a 2020 creation date.

So the scan did not fail to look. **It was not permitted to see the file, and Drive answered the query truthfully for the identity it was asked under: 153 files.** No error was raised, no permission warning, nothing in the payload marked the folder as partially visible.

**That is the whole problem in one sentence: an incomplete answer and a complete answer look identical.** It is the same failure shape as the channel outage the git move fixed, where a stalled road looked exactly like a quiet one.

**What it means for the map.** Every count in the S064 map is a count of what one identity was allowed to see. The map is not wrong where it speaks, and the 2,145 matches it made are each backed by a real file with a real ID. What it cannot do any longer is support a claim of completeness, because absence from the scan does not mean absence from Drive.

**One thing that limits the damage, stated so the risk is sized rather than feared.** The rename targets files by Drive File ID, and every ID comes from the scan. A file the scan never saw is therefore a file the rename never touches: it is left alone, not renamed wrongly. The real exposure is narrower and it is this: a lesson whose true video was hidden while a second, visible file carried the same number, so the map matched the wrong one. Course 004 is the only course where the scan saw fewer files than the course has lessons, and that gap is exactly this file.

## Question 3: the re-count

**Course 004 reads 154 with this file included**, against 154 lessons, so that course now balances for the first time.

**The whole-library re-count has not been run and I am not reporting one.** Running the same scan under the same identity would return the same numbers whether or not other files are hidden, so it would produce a confident figure that proves nothing. **A green check that cannot go red is worse than no check**, and that is precisely what a re-scan under unchanged access would be.

## Question 4: is the file stable

**Yes.** Size read twice, minutes apart: 1,397,310,425 bytes both times, identical to the byte. Not mid-transfer.

## Question 5: stopping, as you asked

**Nothing renames.** Confirmed before you asked it. I had already told Kain that nothing gets renamed on a map I can no longer vouch for, and that stands.

## What the next step actually is, since effort will not fix this

**Re-scanning harder is not the answer, because the constraint is permission rather than diligence.** The three routes that would genuinely settle it:

1. **Give the identity my Drive reads run under access to everything in the curriculum folder**, so a scan can see what Karen and Kain see. Then one re-scan is decisive, and any count it returns can be trusted.
2. **Kain or Karen list the restricted files from their side**, which their view can show and mine cannot. Kain has already said that from his end this looks like the only one in 2,146, which is real evidence and is recorded as his observation rather than as a measurement.
3. **Verify per course rather than per library:** compare each folder's live file count against its lesson count. Course 004 was the only one where those disagreed, and it is now explained.

**The decision between them is Kain's**, exactly as your question 5 says. He has asked me to check all 28 courses, and I have told him plainly that a check run under the same access cannot prove what he wants it to prove.

## Two corrections to the record, already made

The recovered file is now written into the master on the `004-001` row, `Drive File Name` and `Drive File ID`, and a row for it has been added to the rename proposal, which now stands at 2,146 rows rather than 2,145. `Drive File Name` was not overwritten anywhere; it was empty on that row and is now filled for the first time.

*No em or en dashes in this file; checked before writing.*
