# COMMISSION: split the course master into twenty eight CSVs, and make them the master

**DOCUMENT TYPE:** commission. Not a page spec. **From:** Claude Chat, Session 283. **Date:** 18 August 2026.
**Ruled by:** Kain, in session: the twenty eight CSVs become the master and the xlsx is retired.
**Supersedes:** the earlier S283 commission of the same name, which asked only for a readable copy. This one changes what the master is.
**Read this cold.** Everything you need is in this file.

---

## Why this exists

The one master for all course, section, lesson and lesson-description data is an xlsx, and **only you can read it.**

Chat cannot, and this was proved this session rather than assumed. The tool that copies a file from Kain's disk into Chat's own code environment is not registered. Chrome is not connected. The file is not in Google Drive. And reading it through the Filesystem connector returns `PK` followed by mangled bytes, because an xlsx is a compressed zip archive and the connector hands back text.

Chat walked the whole spreadsheets folder: **no CSV of this data has ever existed.**

**Four separate pieces of work read this one asset:** the Vimeo upload, the course and school pages on the website, the twenty eight course handbooks, and the transcript pipeline. Three of the four are produced outside your environment. An asset only you can open is a permanent bottleneck on all of them.

## The ruling that makes this more than a conversion

**The twenty eight CSVs become the master. The xlsx is retired.**

Kain ruled this in session on one argument: if the xlsx stayed the master, every column we add to the CSVs would be wiped by the next re-export, so the added columns would be unsafe by construction. Karen has confirmed the spreadsheet is finished, so nothing is lost by closing it.

This is why the CSVs go into the existing `Course + Lesson Data | MASTER` folder as its operative files, not into a derived subfolder.

## The source

Folder: `05. Spreadsheets | Data | CSV Files` then `Course + Lesson Data | MASTER`.

The source is the xlsx in that folder whose name ends COMPLETE.

**Its Read Me First is stale and must not be trusted for any number.** It names a filename that no longer matches the file, and its row counts describe the version superseded at S260, which now sits in that folder's Archive.

One thing in it does still hold, and it is the only key you have: **sheets `001` to `028` map to the course numbering in DSRD 5 section 1.** The sheets carry no course names. Read that table from DSRD 5, never from the Read Me First and never from memory.

## What is commissioned

**One split. Read only on the xlsx until step 5.**

1. **Write one CSV per sheet**, into the `Course + Lesson Data | MASTER` folder itself.
2. **Name each CSV by its sheet number and its canonical course name** from DSRD 5 section 1, so the folder listing tells a human which course is which without opening anything.
3. **Carry every existing column through untouched**: no renaming, no reordering, no cleaning, no trimming, no filling of blanks. Every value arrives exactly as Karen left it.
4. **Add the seven columns below**, appended after the existing ones. Two you fill in this pass. Five are created empty by design, each filled by a later separately commissioned job, so no file is ever restructured mid-stream.

   **Filled by you, in this pass:**

   | Column | What it holds |
   |---|---|
   | Section Order | An integer, 1 upward, in the order the sections appear in the sheet, restarting at 1 for each course. Every row of a section carries its section's number. **This exists because nothing in the source states section order except the physical row order, so one sort would scramble a course silently and nothing would report it.** Derive it from the row order as found, and change nothing else. |
   | Lesson Key | A unique label for one lesson, in the exact form `001-S03-L07`: the three-digit sheet number, then `S` and the two-digit Section Order, then `L` and the two-digit Lesson Number from the source. **This exists because no column in the source identifies a lesson: names repeat across courses and are about to be rewritten by the standardisation pass, Vimeo Video ID is empty on every row, and the Circle IDs cover roughly a seventh of rows. Row position is currently the only identifier, and row positions move.** Every downstream job is a matching job (Drive file to lesson, Vimeo video to lesson, website row to lesson) and each becomes checkable with this key and guesswork without it. **Report any duplicate key you generate rather than resolving it**, and report any Lesson Number that is blank or not a number; either means the source holds something we do not yet understand. |

   **Created empty, filled later:**

   | Column | What fills it, later |
   |---|---|
   | Course Slug | The same value on every row of one file. **Read from the site URL structure in DSRD 1, never invented**, or the website import points at pages that do not exist. Left empty here because that mapping is its own verification job. |
   | Drive File Name | The Drive to spreadsheet match, once Karen has named the folders and the naming relationship. |
   | Circle Course ID | Recovery from the archived `28 Achology Courses Structure (Incomplete but Current) SUPERSEDED S254.xlsx`, which carries these on roughly 328 rows. |
   | Circle Lesson ID | The same recovery. |
   | Standardised Description | The house-copy standardisation pass, run by Chat. **It writes here, never over Lesson Description**, so the original is always visible beside the rewrite and any disagreement is checkable rather than lost. |

5. **Retire the xlsx** into that folder's Archive, renamed so its status is readable from the name, in the same shape the other superseded files there already use.
6. **Rewrite `Course_Lesson_Master__Read_Me_First.md`** to describe what the folder now is: the twenty eight CSVs are the master, one per course, named by sheet number and canonical course name; the seven appended columns, which two are filled and which five wait; the Lesson Key's exact form, so anyone can read one and know what it means; the DSRD 5 numbering as the key; and the xlsx named as retired with its date. Its current contents are stale and are replaced, not appended to.

## What is asked back, as facts rather than assurances

Report these in TO Chat:

- The number of sheets found, and the number of CSVs written.
- **The row count per course, as a table.** Chat cannot verify this independently, so it is the number every downstream job is counted against.
- The exact column list found in the source sheets, in order, before your seven were appended.
- **The section count per course**, beside the row count, since Section Order is now a fact we are asserting rather than inferring.
- Any duplicate Lesson Key, any blank or non-numeric Lesson Number, and any row that carries no section at all.
- **Any sheet whose columns differ from the others.** One odd sheet is what breaks a bulk run silently.
- Whether Vimeo URL and Vimeo Video ID are still empty on every row, or whether some now carry values.
- Anything in the file nobody has asked about.

## What is NOT commissioned, and must not happen

**No standardisation of any description.** That pass is Chat's, run later on these files, and it writes only into Standardised Description.

**No Vimeo work of any kind.** No export, no API call, no matching. That is a separate commission, written from Karen's own answers, and it does not exist yet.

**No Circle ID recovery in this pass.** The columns are created empty. Filling them is its own job with its own verification.

**No deletion of anything.** The xlsx is archived, never removed.

*No em or en dashes in this file; checked before writing.*
