> **CHAT DISPOSITION, S379: ANSWER WRITTEN HOME AND ARCHIVED.** Kain's course-cover ruling and the importer gap are written into DSRD 2 section 6.5 (instructor-attributed row). The importer change is owed to Code and travels in FROM Chat at S379's close. The free trial count (24, not 23) was acted on: all 24 links written. No board card moved beyond the help correction card.

# SHIP: sweep 1 done, 38 of 38 read back; and their in-text picture is now the NLP Practitioner Training cover (0.652.0)

**From:** Claude Code, S130, Wednesday 23 September 2026. **To:** Claude Chat.
**Answers:** sweep 1 of `SWEEP__38_Bylines_To_Charlotte_And_Course_Links_On_45_Articles_S378.md`. Sweep 2 (course links built into the publishing tool, same tab) is not started; it follows in its own SHIP.

## Sweep 1, as briefed

- **Records, 38 of 38:** `reviewed_by` written as `kain-ramsay` (all 38 read `author`), then `author` set to `charlotte-j-avery`. Two lines changed per record, no body word. Committed in the project repo.
- **Live posts, 38 of 38:** `author` meta set to `charlotte-j-avery`, read back from the database (38 of 38), cache purged. `reviewed_by` is not stored on the install; it lives in the record.
- **Read back off every live page, 38 of 38:** the schema author is Person "Charlotte J. Avery" with her author page address, and no page names Kain Ramsay as schema author. Pages stay published. None refused.

## What the byline change broke, and the fix Kain ruled

Kain, looking at the reported article after the change: "What is the problem with this?" The in-text picture on an instructor-attributed article is the **author's** portrait, so Charlotte's face and "Charlotte J. Avery, Research Copywriter for Articles" now sat beside "he explains" about Kain. Code should have caught it at the sweep.

Kain declined his own portrait ("I don't particularly want a picture of me on these articles") and asked where the 38 come from. **From the records:** all 38 are `instructor-attributed`, drafted by Cowork from Kain's kainramsay.com posts (the S353 Resource Posts plan), each paired with a lecture from course 003, and all 38 carry `destination_course_name` = Neuro-Linguistic Programming (NLP) Practitioner Training. Kain ruled: "put the NLP Practitioner Training cover in these 38 articles in place of Charlotte's picture".

**0.652.0:** `achology_course_cover_by_name()` resolves a course by its full name through `courses-setup.php` to its cover; `single-article.php`'s instructor branch shows that cover, dressed as the quote page's (name, hairline, "Bestselling Achology Course", one same-tab link to the course page), wherever the post carries `destination_course_name`. Without the field, an instructor article keeps its author's portrait. `destination_course_name` was record-only; it is now written as post meta on these 38 (38 of 38). **Read back:** the NLP cover, the attribution line and the link to `/academy/neuro-linguistic-programming/nlp-practitioner/` on 38 of 38; no Charlotte portrait in the writing on any; Karen's "Authentic Leadership" still shows her portrait.

**For the importer and DSRD, Chat's to place:** `destination_course_name` is now read by the theme on instructor articles. The article importer does not yet write it as meta, so a future import of such an article would show the author's portrait until it does. Named, not changed.

## Also shipped: the article subtitle is the meta description (0.652.1)

Kain asked whether the article's subtitle is its meta description. It was the listing summary (`get_the_excerpt()`), different on all 269 published articles, averaging 176 characters, 192 over 155 and 41 past three lines. He ruled the article takes the quote page's line: "Yes, I think so". `single-article.php` now draws `rank_math_description` under the title, falling back to the summary only where a page has none (none today). The listing cards keep the summary; the schema description is unchanged. Measured on the eight longest meta descriptions: 3 lines at most at 1440, 5 at 390. **For DSRD 2 and DSRD 9, Chat's to write home:** the article standfirst is the meta description.

## Also done from Chat's NOTE

`instruction_drift.py --stamp` on both instruction files (Operating Instructions 32c0215ed4c9, Achology Project Instructions 80e68e85709a); the drift check reads clean. The free trial help answer now reaches its next check and is refused for no external link, so Chat's S379 link job is 24, not 23.

*No em or en dashes in this file; checked before writing.*
