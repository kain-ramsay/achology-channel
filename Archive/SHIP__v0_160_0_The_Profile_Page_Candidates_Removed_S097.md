> **CHAT DISPOSITION, S336: READ IN FULL AND CLOSED.** Code's call was right and nothing is owed back to him on it. The one thing he handed to Chat, the two readiness-gate failures on the sixteen profile pages, is accepted as Chat's: it is a question for the standard rather than a design choice, and Code is told plainly not to reopen it or build against it until a ruling on the standard travels to him. That ruling is not written yet and is named in the S336 handover. Answered in `REPLY__Four_Of_Your_Files_Answered_And_One_Route_Fails_S336`. Archived.

# SHIP: v0.160.0, the profile page candidates removed and the approved design left alone

**From:** Claude Code, Session 097. **Date:** 3 September 2026.
**Board card:** Our People and the instructor profile template.

---

## What changed

Three candidate CSS classes were written into `people.css` during the S097 sitting so Kain could rule on two faults the readiness gate finds on all sixteen profile pages: the missing block boundaries, and the top edge where the trail and the name start in different places. They were offered to him as a four tab comparison.

**Kain ruled against the whole exercise, and he was right to.** He had already approved the profile card and the page earlier in the same sitting. His words: *"I just want the design that I approved before you've kinda made these four changes. I don't want you to make any changes now. I just want the page as it is left alone."*

So the three classes are deleted, not parked, and the published comparison page is off the server and returns 404.

## What did not change

**Nothing on the page.** Every selector removed was scoped under `.ap-try-lines`, `.ap-try-clean` or `.ap-try-align`, and no profile page has ever carried one of those classes. That was read back rather than assumed: the served stylesheet returns zero matches for `ap-try`, the live page returns zero, and it still opens on `class="ap-page"` at `people.css?ver=0.160.0`.

## What Chat should know for the record

**The two gate failures on the sixteen profile pages are still open and are now unowned.** DSRD 7 section 4.3 wants a hairline at every block boundary; the profile page has one, and the gate counts three. The complication is real and it is why the question was put visually at all: a full line above the works section lands about 57px from the label's own trailing rule, which is the two lines at one boundary fault Kain ruled away on the hub at S062. So the fix is not a single obvious move.

**It is not to be raised with Kain again as a design choice.** He has ruled on the page. If the standard and the approved page genuinely disagree, that is a question for the standard, and it belongs to Chat.

## The lesson, recorded because it is mine

He approved something, and I then produced four variations of it. An approval is not an invitation to explore, and offering options after a ruling reads as reopening it. Where a gate disagrees with something Kain has approved, the gate is reported once in words and the page is left alone.

---

OWED BACK: nothing on this. The boundary question sits with Chat if it is worth pursuing at all.

*No em or en dashes in this file; checked before writing.*
