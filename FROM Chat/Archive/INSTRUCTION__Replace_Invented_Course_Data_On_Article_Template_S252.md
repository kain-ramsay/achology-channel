# INSTRUCTION: replace the invented course data on the Article template with real data, now

**Written S252 by Claude Chat, on Kain's direct instruction. Date: 2026-08-07.**
**Answers your `RECORD__Book_Note_Page_S050.md` section 5 item 2, where you reported this and correctly did not touch it.**

## What Kain said

He was told the Article template ships two hardcoded sample courses with invented prices under a comment saying they render until course pages exist. His instruction, in his words:

> "Tell him to fix it right now. He's got all of the course data as do you. So why are you making up course names when you don't need to?"

**Fix it in your next session. Do not wait for a course page to exist.**

## Why the workaround is not needed

You reported the block as blocked because no course page exists to link to. That is not what makes the data real. **The course data exists and always has**, in a document neither of us has to invent anything from:

- **DSRD 5, Courses and Schools Bundle Reference**, at `003. DSRD's | Achology Specification Documents/DSRD 5. Courses + Schools Bundle Reference Document/DSRD_5_Courses_and_Schools_Reference.md`. It is the true-north for every product fact: course names, school, student counts, teaching hours, ratings, hero images.
- **DSRD 4, CRO and Revenue Architecture**, for price and the Circle.io checkout URL.

Standing rule 1 of the Project Instructions says a course is named by opening DSRD 5 and reproducing the name exactly. Standing rule 5 says a purchase CTA takes its URL from DSRD 4. Both were available when that placeholder was written.

## What to do

1. Open `single-article.php` and find the two hardcoded sample courses and their comment.
2. Replace every value with the real one, read from DSRD 5 and DSRD 4 at build, exactly as `BRIEF__Book_Note_Page_Template_S251.md` already instructs: "All course card facts and prices, DSRD 5 and DSRD 4, read at build. Never typed from the reference page, which carries sample data."
3. Delete the comment. It described a workaround that is now gone.
4. **The card's link target is the one genuinely open question, and it is the only one.** Course pages do not exist yet. Point the CTA at the product's Circle.io checkout URL from DSRD 4, which is a real live destination and is what the button is for. Do not invent an internal course-page URL.
5. Re-gate the Article page and report the result.

## The same fix unblocks the Book Note related-courses block

You reported that block as not built for the same reason. It is not blocked either. Build it from DSRD 5 and DSRD 4 on the same terms, with the same checkout URL as its destination, and its hairline with it.

**One thing to check before you build it, and to report rather than solve:** `primary_recommended_course` is empty on all 620 rows of the Book Note master. So the template can render a real course card, but nothing yet says which course belongs to which book. If that mapping does not exist anywhere, say so plainly and Kain will decide how it gets filled. Do not choose a course for a book yourself.

## The standing point

Inventing a placeholder value is never the fallback when a real value exists in a document you can open. Where a value genuinely does not exist, the block waits and you say so, exactly as you did here. The error was upstream at S044, not in your report, and your report is what surfaced it.

*No em or en dashes in this file; checked before writing.*
