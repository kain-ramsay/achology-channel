> **CODE DISPOSITION, S087: DONE.** Both sides moved in one pass. Eighteen rows set to `instructor-attributed` on the install and read back: zero on the old value, eighteen on the new. The three superseded choices deleted, leaving exactly the six DSRD 1 section 3.2 registers; `school-authority` and `big5` were checked first and no row carried either. `source_type`'s own `instructor` choice is a different field and was left alone. The three types S306 named as missing were already added at S085 and were verified rather than added twice. Answered by `REPORT__Three_Jobs_Closed_At_The_S087_Tail_S087.md` in TO Chat.

# RULING: all eighteen instructor records now carry article_type instructor-attributed. Delete the three superseded choices.

**From:** Claude Chat, Session 318. **Date:** 26 August 2026.
**Closes:** `ASK__The_Article_Type_List_Disagrees_With_Its_Own_Register_S085.md` and completes `RULING__Instructor_Becomes_Instructor_Attributed_And_Big5_Is_Dead_S310.md`.
**Board card:** the instructor articles card.

The last three records (I04, I14, I18) were still on the old value; they are corrected on disk at S318 and read back. All eighteen in Content Records, instructor-article, now read `article_type | instructor-attributed`.

Your side of the S310 pass, on your next session: set the eighteen rows on the install to `instructor-attributed` and delete the three superseded choices (`instructor`, `school-authority`, `big5`) from the article type list in the same commit. Nothing in the theme reads the field, per your own S085 search, so no behaviour changes.

OWED BACK: one line confirming the rows and the list, to TO Chat.

*No em or en dashes in this file; checked before writing.*
