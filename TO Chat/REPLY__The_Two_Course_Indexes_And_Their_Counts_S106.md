> **CHAT DISPOSITION, S351: read, acted on, ARCHIVED.** Both index files moved to their home beside the 28 course CSVs in the Course + Lesson Data folder, read whole at S351, and the hub subjects were clustered from them with Kain in the sitting. The complete question layer (2,146 of 2,146) is recorded in the S351 plan as the source of every spoke title.

# REPLY: both indexes are in your tray, and the question layer is complete

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Answers:** `ASK__Section_And_Lesson_Index_Across_The_Twenty_Eight_Courses_S351.md`, whole.
**Board card:** 315 Product Question Articles.

---

## 1. The two files

**`SECTION_INDEX__Twenty_Eight_Courses_S351.csv`** and **`LESSON_INDEX__Twenty_Eight_Courses_S351.csv`**, both in this tray, both generated from the 28 CSVs and neither typed.

## 2. The three counts you asked for

| | |
|---|---|
| section index rows | **125** |
| lesson index rows | **2,146** |
| lessons with an empty `standardised_question` | **0** |

**Every expected figure lands.** 2,146 lessons, exactly. The `lesson_count` column sums to 2,146 independently, so the two files agree with each other rather than only with your number.

**125 rather than 124, and it is the row you asked for.** 124 named sections plus one row with an empty `section_name`, which is course 012, the Skilled Helper Practitioner Course, carrying its 2 sectionless lessons exactly as the folder's Read Me First describes. The count still sums.

## 3. The answer inside the third count, which is the one worth reading

**Not one lesson has an empty `standardised_question`. All 2,146 carry one.**

Your ask was worded expecting gaps, "so Chat knows how much of the question layer is already written". **The answer is all of it.** The question layer across every lesson in all 28 courses is complete, so the spokes under each hub can be named from real questions rather than invented ones.

A sample row, so you can see the shape before opening it: lesson `001-001`, course 001, section order 1, lesson 1, "Introducing the Diploma in Modern Applied Psychology", question "What makes Modern Applied Psychology different...", transcript 1,043 words.

## 4. Two things about how it was built, so the counts can be trusted

**The 28 were separated by test, not by a list.** That folder holds 37 CSVs: 28 numbered course files and 9 unnumbered working files (Vimeo length comparisons, Karen's watch list, a rename proposal, an off-by-one investigation). The script takes only files whose name begins with three digits and a space, so a working file dropped into that folder cannot quietly join the count and a new course cannot be missed.

**A section is keyed on its order and its name together**, never on the name alone, so a course repeating a section name under two orders comes out as two rows rather than one merged row carrying a wrong lesson count.

**`standardised_question` is the first line of the Standardised Description column and nothing else.** Where that column is empty the cell is empty, and it is never filled from Lesson Description. That path exists in the script and was simply never taken.

## 5. What was not done

Nothing changed. No course file, no record, no page, no install write. Read only, as your file asked.

---

OWED BACK: nothing. Both files and all three counts are here.

*No em or en dashes in this file; checked before writing.*
