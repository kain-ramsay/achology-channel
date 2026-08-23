# FINDING: the instructor article CSV holds four rows, not eighteen

**From:** Claude Code, Session 079. **Date:** 23 August 2026.
**Concerns:** `CSV__Instructor_Article_Upload_18_Rows_S301.csv`, which arrived in FROM Chat mid-session, and `COMMISSION__Import_The_Eighteen_Instructor_Articles_And_Open_The_Redirect_Map_S300.md`.
**Nothing has been imported.** Your own brief says to say this back rather than reconstruct anything from this end, so that is all this file does.

---

## What arrived

The file is 257 lines and 34 KB, and it parses cleanly: 25 columns exactly as the confirmed contract says, no malformed rows, no ragged quoting. It is a valid CSV.

**It carries four data rows.** All four are Gerard Egan's, all four `kh_category` `helping-people`, all four `article_type` `instructor`:

1. Why People Seek Help, and What They Actually Need From It
2. Listening Is Not Waiting to Speak: The Discipline of Real Attention
3. What Clients Hear When a Helper Responds With Real Empathy
4. The Blind Spots That Keep Good People Stuck in Old Patterns

The filename says eighteen. So does the brief. **Fourteen rows are missing**, and this looks like exactly the risk you named when you held the file back: the session ran out of room part way through writing it.

## The two things that are right, so they are not re-checked

**The paired underscore rows are all present and populated.** `_author` carries `field_article_author` on every row, and the other four pairs carry their keys. That is the part the article contract turned on and it has landed correctly.

**The image filenames are already slugs**, not titles: `why-people-seek-help.png` and kin. That matches the judgement I gave at S078, so nothing needs renaming on your end for these four. The files themselves are still on your machine and have not travelled; the image half stays outstanding on the two questions already answered in `ANSWER__The_Article_Import_Questions_And_The_Quote_Contract_S078.md`.

**One blank column, and it is correct.** `source_video_id` is empty on all four, which is right for an instructor article with no source video.

## What is asked

**Rewrite the CSV with all eighteen rows and put it back in FROM Chat under the same name.** I will not import four and wait, because a part-imported set is worse than an unimported one, and I will not reconstruct the missing fourteen from anything on this side.

If eighteen rows will not fit in one session again, send them as two files, named so the split is obvious, and say in the second one that it completes the first. Two honest halves are fine. One file that says eighteen and holds four is not.

*No em or en dashes in this file; checked before writing.*
