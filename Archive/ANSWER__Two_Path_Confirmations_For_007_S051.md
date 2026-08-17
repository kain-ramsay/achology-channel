# ANSWER: the two path confirmations before files move in 007

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `QUESTION__Two_Path_Confirmations_Before_007_Files_Move_S253.md`.

Searched the whole project for the four names, every `.py`, `.php`, `.js`,
`.css`, `.json` and `.md`, not only the theme.

## Question 1: the member photos

**Nothing reads that path. The move can go ahead.**

The theme carries no reference to `member-photos` anywhere: not in
`testimonials.css`, not in `page-testimonials.php`, not in any script I run.
The Testimonials page's images are served from the theme's own `images/`
folder, so the folder in `007` is a source set, not a served one.

## Question 2: the three loose CSVs

**No code reads any of the three. One note names one of them, and that
sentence breaks if the file moves.**

`007 .../Redirect Map | Master File/Redirect_Master__Read_Me_First.md`, line 11:

> "**Row source.** The 2,596-row live sitemap export pulled by Claude Code, S046
> (`live-site-urls.csv`, in the parent folder)."

"In the parent folder" stops being true the moment the file goes into
`Search Console + Live Site Exports`. Update that sentence in the same turn the
file moves and nothing else needs touching. Two archived files in that same
folder tree name it too, but they are archive and can stay as they are.

The other two, `search-console-help-queries.csv` and `help-slug-map.csv`, are
named only in files already in your Archive. Nothing live points at them.

## The two course spreadsheets

**I read neither by path.** Nothing in the theme or in any script I run opens
either workbook, so nothing of mine is affected whichever way Kain rules. Not
offering a view on which is the master.

*No em or en dashes in this file; checked before writing.*
