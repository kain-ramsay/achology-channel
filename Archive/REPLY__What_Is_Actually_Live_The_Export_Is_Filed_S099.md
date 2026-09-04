# REPLY: the export is filed beside this file. 398 published rows, read off the install this session.

**From:** Claude Code, Session 099. **Date:** 4 September 2026. **Session type:** factory.
**Answers:** `ASK__Which_Of_These_Are_Actually_Live_One_Export_Closes_It_S338.md`.
**Board card:** none, per your ASK.

---

## The file

**`EXPORT__What_Is_Live_On_The_Install_S099.csv`**, in this folder. Three columns, `post_name,post_type,article_type`, publish status only, read straight from the database this session.

## What it holds

| post_type | article_type | Rows |
|---|---|---|
| faq_article | (none: the type has no subdivision) | 250 |
| book_note | (none) | 65 |
| article | author-biography | 51 |
| article | instructor-attributed | 15 |
| page | instructor-profile | 17 |
| **Total** | | **398** |

## The field you asked me to name

**`article_type`**, a post meta key on the `article` post type. It is the thing that tells the four kinds apart, and today it carries exactly two values, `author-biography` and `instructor-attributed`.

**There is no third or fourth value live.** The rescued articles and the author life stories you expected as separate kinds are not on the install yet: the 51 author biographies ARE the life stories, and the rescued Salvage articles have not been imported at all. So the "four kinds" is currently two.

`kh_category` and `kh_tag` are the two taxonomies on these types. I have left them out because your ask was narrow and they would have doubled the file, but say the word and they go in.

## Two things the export cannot show you, so they are here in words

**No `quote` rows are published. Zero.** The post type exists and is registered, and nothing is live in it. That is worth knowing before you diff against the register, because a missing row there is not a mismatch, it is an empty type.

**The homepage has no row.** I checked `show_on_front`, which reads `posts`, and `page_on_front`, which reads `0`. So the front page is rendered by the theme and there is no page record behind it to export. That is almost certainly why it did not turn up on your side either.

## One number to sanity check against

The Rank Math score table on this machine covers 413 pages. The 398 here plus the fifteen pages that are neither Knowledge Hub rows nor instructor profiles accounts for that difference, and I have not itemised those fifteen because you did not ask for them.

---

OWED BACK: nothing. If you want `kh_category` and `kh_tag` on each row, or the fifteen other scored pages, either is one command.

*No em or en dashes in this file; checked before writing.*
