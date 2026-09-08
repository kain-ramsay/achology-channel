# ASK: a section index and a lesson index across the twenty eight courses

**DOCUMENT TYPE:** ask, from Claude Chat, Session 351. **Date:** Tuesday 8 September 2026. **Session type:** planning.
**Board card:** 315 Product Question Articles (being replaced this session by the keyword cluster plan).
**Read-only.** This asks for two generated files. It commissions no change to any record, any page or the install.

---

## 1. What is being built, and why the answer is needed now

S351 is writing the keyword cluster plan for the Knowledge Hub: which hub pages exist, which spokes feed each one, and how the links run between hubs, spokes and course pages. Kain ruled in the sitting that the hub subjects come from the concepts the 28 courses actually teach, read from the course content itself, not from the seven school names and not from what the old site happened to rank for.

The source for that is the course and lesson master: the 28 CSV files in the Course + Lesson Data folder inside the Spreadsheets folder of the website project. They hold 2,146 lesson rows across 124 sections. Chat cannot read 4.6 MB of CSV inside a session, and the section names and lesson names are the only columns the plan needs. One script extracts them.

## 2. The two files asked for

Both written into TO Chat. Both generated from the 28 CSVs, never typed.

**File one: `SECTION_INDEX__Twenty_Eight_Courses_S351.csv`.** One row per section, 124 rows expected. Columns: `course_number`, `course_name` (the filename's canonical name), `section_order`, `section_name`, `lesson_count`. Course 012 has two lessons with no section (lessons 47 and 49, per the folder's Read Me First); report them as a separate row with `section_name` empty so the count still sums to 2,146.

**File two: `LESSON_INDEX__Twenty_Eight_Courses_S351.csv`.** One row per lesson, 2,146 rows expected. Columns: `lesson_key`, `course_number`, `section_order`, `lesson_number`, `lesson_name`, `standardised_question`, `transcript_word_count`. The `standardised_question` is the first line of the Standardised Description column, which is written as a question on the rows Chat has read (course 011 carries it on all 28). Where that column is empty, leave the cell empty; do not fill it from Lesson Description.

**One line back in the same reply:** how many rows each file holds, and how many lessons have an empty `standardised_question`, so Chat knows how much of the question layer is already written.

## 3. What Chat will do with them

Read the section index whole with Kain and cluster the 124 sections into hub subjects, then use the lesson index to name the spokes under each hub. The plan is written from those two files. Nothing else is asked of Code on this item.

---

OWED BACK: the two files and the three counts, into TO Chat.

*No em or en dashes in this file; checked before writing.*
