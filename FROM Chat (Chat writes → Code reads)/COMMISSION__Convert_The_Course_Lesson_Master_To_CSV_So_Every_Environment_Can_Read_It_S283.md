# COMMISSION: convert the course and lesson master to CSV, so every environment can read it

**DOCUMENT TYPE:** commission. Not a page spec. **From:** Claude Chat, Session 283. **Date:** 18 August 2026.
**Ordered by:** Kain, in session, when Chat reported it could not read the master spreadsheet.
**Read this cold.** Everything you need is in this file.

---

## The problem, stated plainly

The one master for all course, section, lesson and lesson-description data is an xlsx, and **only you can read it.**

Chat cannot. The tool that copies a file from Kain's disk into Chat's own code environment is not registered in this session. Chrome is not connected. The file is not in Google Drive. It is a 925 KB zip archive, so reading it through the Filesystem connector as text destroys it rather than reads it.

Chat searched the whole spreadsheets folder: **no CSV of this data exists anywhere on disk.** It has never been extracted to text. That is the fault, and it is bigger than one blocked session.

**Four separate pieces of work all read this one asset:** the Vimeo upload, the course and school pages on the website, the 28 course handbooks, and the transcript pipeline. Three of the four are produced outside your environment. So an asset only you can open is a bottleneck on all of them, permanently, not just today.

## The file

Folder: `05. Spreadsheets | Data | CSV Files` then `Course + Lesson Data | MASTER`.

The operative file is the xlsx in that folder whose name ends COMPLETE. Its Read Me First sits beside it. **Note that the Read Me First is stale:** it names a filename that no longer matches the file, and its row counts describe the version superseded at S260, which now sits in that folder's Archive. Do not trust its numbers; read the file.

What the Read Me First does still hold true, and it matters: **sheets `001` to `028` map to the course numbering in DSRD 5 section 1, and that table is the only key.** The sheets carry no course names.

## What is commissioned

**One conversion. Read only on the master. Nothing is edited, moved or renamed.**

1. Write one CSV per sheet, into a new subfolder beside the master. Name that subfolder plainly so its purpose is obvious from the folder listing.
2. Name each CSV by its sheet number **and** the canonical course name read from DSRD 5 section 1, so a human reading the folder knows which course is which without opening anything.
3. Keep every column exactly as it is in the sheet. No renaming, no reordering, no cleaning, no trimming of whitespace, and no filling of blanks. This is a format change and nothing else.
4. Write the folder's own README, per standing rule 24, naming what is inside it, the date it was generated, and the one line that matters: **these CSVs are a derived copy, the xlsx is the master, and a re-export replaces them whole.**

## What is asked back, as facts rather than assurances

Report these in TO Chat:

- The number of sheets converted, and the number of CSVs written.
- **The row count per course**, as a table. Chat has no way to verify this independently, so it is the number everything downstream will be counted against.
- The exact column list found in the sheets, in order.
- **Any sheet whose columns differ from the others.** A single odd sheet is the thing that breaks a bulk run silently.
- Whether the Vimeo URL and Vimeo Video ID columns are still empty on every row, or whether some now carry values. The Read Me First says empty on every row, but that describes the superseded version.
- Anything you find in the file that nobody has asked about.

## What is NOT commissioned, and must not happen

**No standardisation of any description.** The house-copy pass on every lesson description is a separate, later step, run by Chat on this output. If you rewrite a description here, the master and the CSVs part company on day one and nobody will know which is right.

**No Vimeo work of any kind.** No export, no API call, no matching. That is a separate commission written from Karen's own answers and it has not been written yet.

**No new master.** The xlsx stays the master. These CSVs are a readable copy.

## Why this is worth doing properly rather than quickly

The whole point is that after this, **Chat, Cowork and you can all read the same course data**, and the standardisation pass, the website CSV, the handbooks and the reconciliation map stop waiting on which environment happens to be open. It is one small job that unblocks a stream.

*No em or en dashes in this file; checked before writing.*
