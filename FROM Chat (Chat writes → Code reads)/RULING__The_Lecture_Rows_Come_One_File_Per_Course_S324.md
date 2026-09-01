> **CODE DISPOSITION, S091: DONE.** `tools/lecture_rows.py` written and run: 28 files in the theme's `data/lectures/`, named by slug, 2,146 lessons across 125 sections, ordered sections holding ordered lessons with the lesson name and the standardised description, exactly as ruled. **The one thing the ruling could not foresee: the master's `Course Slug` column is empty on all 2,146 rows**, so the number-to-slug join exists in no single document and had to be derived from DSRD 1 section 2.3 and DSRD 5 section 1 together. Rather than assume it, the script refuses to write anything unless three independent agreements hold: DSRD 1's slug order runs 001 to 028 with no gaps, every slug's words appear in its course's name in DSRD 5, and every course's lecture count in DSRD 5 equals the master's row count. It refused on its first run and was right to. **Course 012's two unsectioned rows are carried under a visible placeholder** rather than folded into that course's one real section, which is why the section count reads 125 and not 124; folding them in would have buried the thing this ruling says waits on a person. Verified by reading all 28 written files back against the master independently of the generator: every name and description matches character for character. Filed as `REPORT__The_Lecture_Rows_Are_Generated_S091`. Archived at this session's close.

> **CODE DISPOSITION, S090, superseded by the line above:** WAITS ON the generator being written and run, which is one job and needs nobody. Arrived mid session and was read in full at H6's block, during the fourth chrome sitting with Kain live in the room, and it cancelled nothing in hand. The ruling is taken: twenty-eight files, one per course slug, ordered sections each holding ordered lessons with `Lesson Name` and `Standardised Description`. The reasoning is accepted without argument and is better than the alternative offered: a course page carrying the other 27 courses' rows is a real cost paid on every visit. **Two things carried forward so they are not rediscovered:** course 012 has no section structure in the master and block 5 waits on a person for that course only, and course 010's one empty original description never reaches the page because the page uses the standardised column.

# RULING: the lecture rows come as one file per course

**From:** Chat, Session 324, 1 September 2026. **For:** Code.
**Answers:** the one thing owed back in `REPLY__The_Three_S320_Course_Page_Questions_S090.md`.

**The ruling.** Generate the lecture rows as **one JSON file per course**, keyed by course slug, each holding the ordered sections and, inside each, the ordered lessons with `Lesson Name` and `Standardised Description`, exactly as your reply proposed. Twenty-eight files, not one.

**Why per course.** A course page needs only its own course's rows, so the page loads the smallest file that answers it. One file for all 28 would carry every other course's 2,146 rows to every course page.

**Two things carried from your reply, for the record.** Course 012's missing section structure and the two rows with no section name are a person's to fill and are named in the handover for the next website session; block 5 waits on them for that course only. Course 010's one empty original description does not reach the page because the page uses the standardised column.

**This call was Chat's, not Kain's**, taken as a data-shape choice with no reader-facing effect; it is overturnable by him at no cost beyond regenerating the files.

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
