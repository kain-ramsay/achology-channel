# COMMISSION: export the whole Vimeo library, read only, and answer the account questions

**DOCUMENT TYPE:** commission. Not a page spec. **From:** Claude Chat, Session 283. **Date:** 18 August 2026.
**Ordered by:** Kain, in session, after Karen answered the four questions the S282 call list put to her.
**Runs after:** `COMMISSION__Make_The_Number_The_Common_Identifier_And_Map_Drive_To_Every_Lesson_S283`. Run that one first. This one can be run before its map has been read by Kain, but not before it has been produced.
**Where the report goes:** TO Chat, like every other report.
**Read this cold.** Everything you need is in this file.

---

## Why this exists

**Vimeo is the only one of the three sources nobody has measured.** The spreadsheet is now twenty eight CSVs you built and counted. Google Drive is being mapped in the commission before this one. Vimeo is what Circle actually streams to students, it has been managed by hand for years, and no export of it exists anywhere.

**Karen's ruling, given in session and binding:** Google Drive holds the current, re-edited videos and they are hosted nowhere anyone can watch them. **Everything in Vimeo is an older, inconsistent, out of date version.** That gap is the whole reason the replacement job exists. So this export is not a survey of what we have; it is a measurement of what is about to be replaced.

**The spreadsheet is true north for names and descriptions**, and it mirrors Circle. Where Vimeo disagrees with it, Vimeo is wrong. **Where a number disagrees, the number is right**, which is Karen's exact wording.

## Step 0: confirm access before anything else

**Say plainly whether you can reach the Vimeo API for the Achology account, and stop the Vimeo work there if you cannot.**

The Vimeo Course Refresh board card records that the transcript extraction route was already proven through the API on an earlier card, so some access has existed. Whether it still does, and whether it is yours to use, is not something Chat can see.

**If access is missing, say exactly what is needed and from whom.** Do not work around it, do not scrape, and do not ask Kain to go hunting through settings without telling him precisely what to look for.

**Step 4 does not need Vimeo at all and runs either way.** It is a question about the theme, not about the account. No access failure is a reason to leave it unanswered.

## Step 1: the export

**Read only. Nothing in Vimeo is changed, replaced, uploaded, renamed, deleted or re-tagged by this commission.**

**One new CSV, written into the `Course + Lesson Data | MASTER` folder beside the twenty eight course files, and the folder's `Course_Lesson_Master__Read_Me_First.md` updated to name it and say what it is.** That folder is now the master and its read me is what tells the next person what is in it; a file arriving there unannounced is the drift this project keeps finding.

**Every video in the account, not only the course lectures.** The account also holds member testimonial videos and other material, and a partial export would be read later as a complete one. **Carry the folder or project path on every row so course and non-course videos can be told apart without guessing.**

**Do not write anything into the twenty eight course CSVs.** In particular, **the `Vimeo URL` and `Vimeo Video ID` columns stay empty.** Filling them means deciding which Vimeo video belongs to which lesson, and that match is not commissioned here and cannot be made safely until the Drive map and this export sit side by side. **A Vimeo ID written against the wrong lesson is the single worst outcome available in this whole stream**, because every later job trusts it and the replacement run would put the wrong video on the wrong lecture.

Each row carrying at least:

| Field | Why it is wanted |
|---|---|
| Video ID | The identifier Circle streams from. It is the thing that must survive a replacement. |
| Title | Recorded as found. It is expected to be wrong in places, and this export is how we find out how wrong. **It is not used to match anything here.** |
| Description | Compared against Lesson Description so we know how far Vimeo has drifted. |
| Folder or project, and its full path | Vimeo's own organisation, which may or may not group by course. |
| Duration in seconds | The independent check that a Vimeo video is the same lecture as a Drive file, used later rather than here. |
| File size in bytes | Half of the storage sum below. |
| Upload date and last modified date | Tells us which videos have been touched and which have sat since first upload. |
| Privacy and embed settings | Anything unlike its neighbours is a video that will behave differently after a swap. |
| Embed URL or link | Needed to trace a video back to the lesson Circle shows it on. |
| Whether captions or a transcript exist, and in what language | Decides how much of the transcript harvest is already done. |

**Add anything else the API returns that a person planning a 2,800 video replacement would want.** You can see the payload and Chat cannot.

## Step 2: the storage answer Karen asked for

**Karen stated in session that the account is at seventy one per cent of a seven terabyte allowance**, which is roughly 4.97 TB used and 2 TB free. **Confirm or correct that from the account itself rather than accepting it**, and report the plan tier, the allowance, the used figure and the free figure as the API gives them.

**Report the total size of the library**, so it can be set beside the Google Drive total from the mapping commission. The Drive files are the re-edited versions and Karen expects them to be substantially smaller. If she is right, the replacement frees real space and the hosting plan may come down, which makes this a money question rather than a technical one.

**And the question that decides whether the saving is real.** When a file is replaced through the API, does Vimeo release the storage the previous version occupied, or does it retain prior versions and keep charging for them? **If old versions still count, the saving exists on paper and never in the account**, and the plan decision changes completely. Find the answer rather than inferring it, and say which it is.

## Step 3: the account facts only the account knows

Karen was asked what she knows about the Vimeo account that nobody else does, and her answer was the storage position. These are the rest, and they are yours to read from the API rather than hers to remember:

- The plan tier and what it gates.
- Upload allowances: per file, per week, per month, whatever the plan applies.
- API rate limits, and what they mean for a bulk run. **On scale, use the real number rather than a remembered one:** the board card carries "roughly 2,800 videos", the twenty eight CSVs hold 2,146 lessons, and this export will produce a third figure. Report what the account actually holds and let the three sit side by side rather than repeating any of them as fact.
- Whether the replace-a-file path (keeping the video ID, the embed and the stats) is available on this plan at all. **This is the single fact the whole approach rests on, so answer it in the first line of your report rather than in its place in this list.** If the answer is no, everything downstream changes and Kain needs to know before he reads anything else.
- Whether auto-captioning is enabled, and whether it regenerates on a replaced file.
- Anything about the account's shape that would surprise someone planning a bulk run.

## Step 4: the website CSV column contract

Agreed with Kain at S282 as part of this same run, and it is a question rather than work.

**Confirm the column list the theme needs to render a course's curriculum on a course page and on a school page.** After the mapping commission has run, the twenty eight CSVs carry: Section, Lesson Number, Lesson Name, Lesson Description, Vimeo URL, Vimeo Video ID, Section Order, Lesson Key, Lesson Number Padded, Course Slug, Drive File Name, Drive File ID, Circle Course ID, Circle Lesson ID and Standardised Description.

**Say which of those the import actually needs, in what order, under what header names, and whether the school pages read the same file or need their own.** Nothing is guessed and no row is produced until you have answered. **Note that the website reads `Standardised Description`, never `Lesson Description`**, which is Kain's S283 ruling.

## What is NOT commissioned

**No replacement of any video.** Not one, not as a proof. The one-video proof is its own commission and it runs only after Kain has agreed what is replaced and in what order.

**No upload, deletion, re-titling, re-describing, folder move or privacy change in Vimeo.** Every one of those is a write to the thing students currently watch.

**No transcript harvest.** Report whether captions exist; do not pull them. The harvest is step 6 of the board card and comes after the replacement.

**No reconciliation, and no matching of any kind.** Export the facts. The three way match between this export, the twenty eight CSVs and the Drive map is read with Kain once all three exist, and any discrepancy list written from it is a separate job. **Nothing in this commission decides that a given Vimeo video is a given lesson.**

**No inference where the API is silent.** A fact you could not read is reported as unknown, with what would settle it.

*No em or en dashes in this file; checked before writing.*
