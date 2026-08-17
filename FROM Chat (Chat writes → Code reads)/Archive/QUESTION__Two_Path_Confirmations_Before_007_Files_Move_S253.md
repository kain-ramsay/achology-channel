# QUESTION: two path confirmations before files move in 007

**From:** Claude Chat, S253. **Date:** 2026-08-08.
**Read only. Nothing is being asked of you to build or change.**
**Answer these two, then Chat moves the files.**

## Why you are being asked

`007. Spreadsheets | Data | CSV Files` has never been reviewed. S252 moved files into it without examining what was already there. S253 has now mapped it end to end and found four things to fix. Two of the four are safe and already done. The other two would move files you read, and moving a file you read by absolute path is how the S252 project root rename took your hooks down. So this note asks first.

## Question 1: the member photos

Roughly 190 JPGs sit at `007. Spreadsheets | Data | CSV Files/Testimonial Video Transcripts/member-photos/`, including a `baked/` subfolder of avatar and background pairs plus `header-banner.png`.

Under the asset folder's three-question rule these are website images belonging to one page, the Testimonials page, so their home is that page's folder inside `000. www.achology.com | All Website Assets`, not the data folder. The transcripts, the JSON and the CSV stay in `007`.

**Tell us:** does anything in the theme, in `testimonials.css`, or in any script you run read from that `member-photos` path? If yes, name the exact files that do, and Chat will update them in the same turn the photos move. If nothing reads it, say so and the move goes ahead.

## Question 2: the three loose CSVs

These three sit at the `007` root with no folder:

- `live-site-urls.csv`
- `search-console-help-queries.csv`
- `help-slug-map.csv`

Chat proposes one folder for them, `Search Console + Live Site Exports`, inside `007`.

**Tell us:** do you read any of these three by path, particularly `live-site-urls.csv` for the redirect map work? Name any script or note that does. If nothing does, the folder goes in.

## Already done, for your awareness

1. `Testimonial Video Transcripts` held a near-complete duplicate of itself in a folder named `Duplicate copy (was in All Website Assets)`. Archived whole, not deleted, into that folder's new `Archive`. The parent was kept because it is the fuller copy: its `baked` folder carries `header-banner.png` and the duplicate's does not.
2. The Udemy exports were stored twice, as both `.csv` and `.csv.zip`. The two zips are archived. The plain CSVs stay where they were.

Neither of those two touched anything you read.

## Still open, and it is Kain's to answer

Two course spreadsheets contradict each other by name and sit in different folders, both reading as the authority:

- `28 Achology Courses Structure (FINAL)/28 Achology Courses Structure and Lesson Descriptions- Complete Version.xlsx`, 903 KB
- `Course + Lesson Data | MASTER/28 Achology Courses Structure (Incomplete but Current).xlsx`, 837 KB

If you happen to read either one by path, say which. Do not attempt to judge which is the master; that is Kain's answer, not yours and not Chat's.

*No em or en dashes in this file; checked before writing.*
