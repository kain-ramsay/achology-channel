> **DISPOSITION, Session 267, 12 August 2026.** Closed. The decision it asked for was Kain's own word moving the figure to 4,516, given in the same Code session, which is also his acceptance of the removal. The removal itself stands on evidence rather than opinion: Code searched all 28 course sheets and 8,778 cells and found no Achology course teaches dietary content, so the review cannot be about ours. The review is a draft, not deleted, and one command restores it. Recorded on the Reviews page card, along with the fact that editorial pass two on the 897 flagged reviews is still locked behind Chat confirming pass one. Archived.

# REPORT: the nutrition review, found, checked and removed

**From:** Claude Code, Session 054. **Date:** 2026-08-12.
**Answers:** the IMMEDIATE ITEM in `COMMISSION__Reviews_Editorial_Pass_Two_All_897_S264.md`.
**Done and reversible.** Live count is now 4,516 published reviews, and section 4 below is the consequence that needs a decision.

## 1. The count found: one

**Searched all 4,517, not the 897.** The brief says "search all 897", but the review Kain spotted could be any of them and pass one only touched 897, so the wider search is the safe reading. One match for "nutrition" in the whole archive.

## 2. The review, in full, so Kain can confirm it was the right one

**post_id 29170**, published 2025-12-17, four and a half stars, reviewer "Dilogen de A.", attributed to the Diploma Course in Modern Applied Psychology (DiMAP), course 001.

> "Most good lectures/modules but the nutrition guideline and advice is out of date. There is considerable evidence to suggest that saturated fats are not the problem and significant movement away from seed oils."

## 3. Why I removed it rather than flagging it, and what I checked first

The brief allows removal only where a review is "plainly about a nutrition course (not ours)", and requires flagging where the word is metaphorical in a genuine review of ours. **This is neither obviously, so I checked the curriculum before touching it**, because deleting a genuine four-and-a-half-star criticism from a page whose whole claim is that it shows the critical ones would be a serious error.

**Searched every lesson in the master workbook: 28 sheets, 8,778 cells.** Two hits for "nutrition", both the same sentence in course 009, and it is this:

> "Physical: The physical level concerns the tangible, biological aspect of our existence... requiring care through proper nutrition, exercise, rest, and overall well-being."

That is the word "nutrition" appearing once, in a list of wellbeing factors, inside a lesson about the five levels of human experience. **DiMAP itself has zero hits across its 175 lessons.**

**A course containing one passing use of the word cannot produce a complaint that its "nutrition guideline and advice is out of date" on saturated fats and seed oils.** That review is describing a course with actual dietary content. Achology has none. It is a mis-imported Udemy review, exactly as Kain suspected, and it is removed.

## 4. THE CONSEQUENCE, and it needs a decision that is not mine

**The page now says 4,517 in seven places and 4,516 in one.**

| Where | Reads |
|---|---|
| The live results counter above the grid | "Showing 50 of **4,516** reviews" |
| The figures panel, the hero, the page title, the meta description, the schema | **4,517** |

The counter is computed from the real query, so it moved. Everything else is the figure register, and **Kain's standing S052 ruling freezes it**: "do NOT update... once the site is live, we can sporadically do number updates, but definitely not now."

So the page is now internally inconsistent by one, on the page whose entire credibility is that its numbers are real. **Three ways out, none of them mine:**

1. **Move the register to 4,516.** Correct, but it breaks the freeze ruling, and it also needs the page title and meta description changed, which are Chat's approved copy from S261.
2. **Leave it.** One counter disagrees with seven statements by one review.
3. **Restore the review.** One command; it is a draft, not deleted.

My read, offered rather than applied: option 1, taken deliberately as a single small exception to the freeze, because a page that says 4,517 and shows 4,516 undermines the thing the page exists to do. But the freeze is Kain's and the copy is Chat's, so it is not a call I should make at the end of a session.

## 5. How to reverse it

The review is a **draft, not deleted**. Nothing was destroyed.

```
wp post update 29170 --post_status=publish
```

The reason is also written onto the record itself, in a `_ach_removed_reason` meta field, so anyone finding a drafted review later learns why without needing this file.

## 6. What I need back

1. **Kain's confirmation that 29170 was the right one**, which is what section 2 is for.
2. **A decision on the count**, section 4.
3. **Note that pass two is still locked** behind Chat confirming my pass-one result, per the brief's own sequencing. Only this immediate item ran.

*No em or en dashes in this file; checked before writing.*
