# DELIVERY: the review export for the tagging and titling pass, and the two field names

**From:** Claude Code, Session 053. **Date:** 2026-08-10.
**Answers:** `COMMISSION__Export_Reviews_And_Name_The_Two_New_Fields_S258.md`
**Supersedes:** my `ANSWER__Route_To_Write_Two_Columns_Into_The_Review_Bank_S053.md`, which answered the withdrawn Notion question. Kain's correction of the premise is right and that answer can be archived unread.

## 1. The export

**Path:** `05. Spreadsheets | Data | CSV Files/Reviews Page Data/reviews-for-tagging-S053.csv`
**Shape:** CSV, UTF-8, header row, 4,517 data rows, one per published review.

| Column | What it is |
|---|---|
| `review_key` | The stable id. **This is the column Cowork must return.** |
| `post_id` | The WordPress post id, for convenience only. See the warning below. |
| `course_number` | The DSRD 5 number, 001 to 028 |
| `course_name` | The full canonical course name |
| `star_rating` | 5, 4.5, 4, 3.5 or 3 |
| `review_text` | The review's whole text, unedited |

Generated from the live site rather than from the theme's shipped export, so it is exactly what /reviews/ is rendering today.

**Verified before sending, not assumed:** 4,517 rows, 4,517 distinct `review_key` values, no empty review text, and the star distribution matches the source row for row (2,897 at 5; 621 at 4; 542 at 4.5; 234 at 3; 223 at 3.5).

## 2. Return the `review_key`, not the `post_id`

Worth being blunt about, because it is a trap I walked into twice today.

`review_key` is a fingerprint computed from the review's own content: course number, date, student and the opening of the text. It is stable across a rebuild of the bank.

`post_id` is not. I rebuilt the whole bank twice this session, correcting the reviewer-name transform and then adding a display-order value, and every post id changed both times. It is in the file because it is useful for a spot check and for Kain looking a row up, and it is not the key.

**So Cowork returns `review_key`, and I resolve it.** If a returned key matches nothing, I report that row rather than guessing at it.

## 3. The two field names

Named to match the six the review type already carries (`reviewer_name`, `review_text`, `course_name`, `star_rating`, `review_tier`, `is_featured`), so nothing about the type reads as bolted on later:

- **`review_title`**
- **`review_theme`**

`review_title` is already live in the card renderer: DSRD 8 section 14.2 item 2's title element is built and simply does not print while the field is empty, so titles appear the moment the values land, with no further build.

## 4. The file I want back

```
review_key,review_title,review_theme
718ab3d05541491b520559d32b3a70ad77eb251e,"Good place to start learning psychology",Practical application
```

Three columns, that order, CSV or JSONL, one row per review. Nothing else in it: no review text echoed back, no course, no rating. The less that travels, the fewer places a value can drift.

**The theme value:** the exact visible label as DSRD 9 section 29.7 O1 spells it, not a slug and not a shortening. If a review carries two, separate them with a semicolon and I will store it as a multiple. **If the pass cannot decide, send it empty.** An empty theme is a review that does not appear under a filter, which is recoverable in one pass; a wrong theme is a review filed under something it never said, and nobody will ever find it to fix.

**The title:** whatever the frozen exemplar standard produces. I do not check it, edit it, or write one, and a row with an empty title renders exactly as the card does today.

## 5. What I will do with it, so the boundary is clear

Add the two fields to the review type, write the values in against `review_key`, and report how many landed, how many keys did not match, and how many came back empty. Kain then edits any title he does not like directly in WordPress, and the Theme control comes alive for him to rule on in Safari.

**I do not build the Theme control until the tags are in.** It is left out of the bar rather than rendered inert, which is where it stands today.

*No em or en dashes in this file; checked before writing.*
