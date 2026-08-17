# REPORT: what is in each of the two course workbooks

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `QUESTION__Which_Course_Workbook_Is_The_Master_S254.md`, items 1 to 6.
**No judgement offered on which is the master. That is Kain's ruling.**

Both files are one sheet per course rather than one table, and both carry the
1000-row padding a Google Sheets export leaves behind. Every count below is of
rows that actually hold something, never `max_row`.

Called **A** and **B** throughout:

- **A** = `28 Achology Courses Structure (FINAL)/28 Achology Courses Structure and Lesson Descriptions- Complete Version.xlsx`
- **B** = `Course + Lesson Data | MASTER/28 Achology Courses Structure (Incomplete but Current).xlsx`

## 1. Sheets, and the shape of each

| | A | B |
|---|---|---|
| Sheets | 28 | 29 |
| Sheet names | `001` to `028` | the course, abbreviated: `DiMAP`, `CBT Prac`, `LC Cert` and so on, plus `Free Content` |
| Columns | 6 | 13 or 14 |
| Lesson rows, all sheets | **2,146** | **2,249** |

**A's header, one shape across all 28 sheets:**

> Section | Lesson Number | Lesson Name | Lesson Description | Vimeo URL | Vimeo Video ID

**B's header, three shapes, same 13 columns in different orders, one adding a
`DONE` column at the front:**

> DONE | Course | Section | Lesson Number | Lesson Name | Lesson Description | School | Content Type | Duration | Vimeo URL | Vimeo Video ID | Status | Circle Lesson ID | Circle Course ID

## 2. Which courses each holds

**A does not name its courses anywhere.** There is no course column and the
sheets are numbered, so the only way to tell which sheet is which course is by
matching it against something else.

**B names the course on every one of its 2,249 rows**, in full canonical form.
Its 29 sheets carry 28 courses plus `Free Content`, which holds The Achology
Code of Ethics Training Course (CofE).

**They are the same 28 courses.** Matching sheet by sheet on lesson count, 27 of
A's 28 sheets pair exactly with one of B's:

```
001 = DiMAP (175)          014 = Counselling Practitioner (176)
003 = NLP Prac (155)       004 = NLP Master Prac (154)
018 = MHP (130)            015 = Mind Prac (124)
009 = LC Cert (122)        007 = CBT Prac (119)
013 = Hypnotherap Prac (118)   ... and eighteen more, all exact
```

**Two differences, and they are the whole of it:**

1. **A sheet `010` holds 134 rows. B's `LC Blueprint` holds 132.** Same course,
   two rows apart. Nothing else in either file fails to pair.
2. **B has `Free Content`, 105 rows. A has no equivalent.**

## 3. The complete versus incomplete claim, tested

**On lesson descriptions the two are equal, and both are complete.**

| | A | B |
|---|---|---|
| Lesson Description filled | 2,146 of 2,146, 100% | 2,248 of 2,249, 100% |
| Blank | 0 | 1 |

So the names on the two files do not describe the difference between them. B,
the one called incomplete, holds **more** lesson rows and more description text
than A, the one called complete.

**Where B is genuinely unfinished is its operational columns:**

| Column | Filled |
|---|---|
| Course, Section, Lesson Number, Lesson Name | 100% |
| Lesson Description | 100%, one blank row |
| Status, Circle Lesson ID, Circle Course ID | 328 of 2,249, 14.6% |
| School | 50 of 2,249, 2.2% |
| Content Type, Duration, Vimeo URL, Vimeo Video ID, DONE | 0% |

**A's two extra columns are empty too:** Vimeo URL and Vimeo Video ID are 0%
across all 2,146 rows. Its Section column is filled on 2,144 of 2,146.

## 4. Anything visibly unfinished

**No placeholder text in either.** Searched every cell of both for TBC, TBD,
TODO, XXX, lorem, placeholder and question marks: zero hits in A, zero in B.
Nothing truncated that reads as truncated.

The unfinished parts are the empty columns in section 3, not damaged content.

## 5. The one thing worth knowing before the ruling

The practical difference is not completeness of the teaching content, which is
equal. It is that **B carries the identifying and operational data and A does
not**: course names, school, Circle IDs, status. A is lesson text with numbered
sheets and no key.

Stating it because it is measurable, not as a recommendation. Kain rules.

*No em or en dashes in this file; checked before writing.*
