**DISPOSITION (S284): items 3, 4, 6, 7 and 9 carried on the Vimeo Course Refresh card; item 1 (the 004-001 welcome video) and the 57 MB file are Karen's, named in this session's next-steps list. Stays. Waits on two Kain decisions asked this session: the board card for the 788 superseded Vimeo videos, and the DSRD 5 lecture-count gap (2,261 against 2,146).**

# NOTE: where the course video stream stands, why, and the nine things Chat needs to check or route

**DOCUMENT TYPE:** note, written at Kain's instruction in session. Not a page spec. **From:** Claude Code, Session 64. **Date:** 18 August 2026.
**Why it exists:** Kain asked me to tell you plainly what we have been doing while you have been between turns, so you are not reading four reports cold, and so the things that actually need you sit in one list instead of scattered through them.

---

## What has happened today, in order

Four of your commissions have run end to end. Each has its own report in this folder; this note is the thread joining them, not a substitute for any of them.

**One. The course master became twenty eight CSVs** (`REPORT__The_Course_Master_Split_Into_28_CSVs_S064`). The xlsx only Code could open is retired into Archive, byte for byte intact. 2,146 lessons across 124 sections.

**Two. The Lesson Key became the number, and Google Drive was mapped to every lesson** (`REPORT__The_Drive_To_Lesson_Map_S064`). 2,145 of 2,146 lessons now carry the exact name and the Drive file ID of their video. One lesson has no video. Nothing is orphaned and nothing collides.

**Three. The Vimeo library was exported** (`REPORT__The_Vimeo_Library_Export_S064`). 3,994 videos, read only. The replace-a-file path exists on this plan, which is the fact the whole approach rested on.

**Four. The rename is proposed and stopped there** (`REPORT__The_Drive_Rename_Proposal_S064`). 2,145 files, every old and new name written out, nothing renamed. It waits on Kain reading it.

## Why it went in that order, since the order was the point

**Each step existed to make the next one safe rather than merely possible.** The split made the data readable by all four of us. The map proved which video is which lesson **before** any file was touched, because Drive holds the only copy of a 2.77 terabyte library and a filename is currently the only human-readable label on it. The Vimeo export measures what is about to be replaced. The rename is proposed before it is executed for the same reason the map came before the rename.

**The thing that vindicated the order:** the map found that five in six lesson names disagree between Drive and the spreadsheet, as sentences rather than as punctuation. Had anything matched on names, or even used them as a veto, it would have failed across 83 per cent of the library and looked clean while doing it.

---

## The nine things that need you

### Yours to route or board

**1. Course 004 has no video for lesson 1.** "Welcome to the NLP Master Practitioner training!" Its Drive folder runs 002 to 154. Either the video was never made, or the lesson should not exist. **Karen's to answer; nothing downstream can fill it.**

**2. Course 007 has one more Vimeo video than it has lessons.** 120 in the numbered Vimeo folder against 119 lessons, while the other twenty seven courses agree to the video. **Nobody has looked at which video it is.** It matters because it is the only place the three sources disagree on a count.

**3. One lesson name is corrupted in the source data.** Course 014 lesson 151 reads `The BThe Becca Sessions (Phase 2 → Session 2 → Part 4)`. That is what the master holds, not a slip of mine. **If the rename runs before Karen fixes it, the corruption becomes a filename permanently.** Five other names my check flagged are false positives and are fine.

**4. Six lesson names contain a line break** inside the name field. They sanitise cleanly, but a line break inside a lesson name is a data fault rather than a style choice, and Karen may want them gone at source.

**5. The 788 superseded videos in Vimeo.** Complete older copies of six courses sit beside the renumbered folders that replace them: unnumbered NLP Master Practitioner, NLP Practitioner, CBT Practitioner and Mindfulness Practitioner sets, and Life Coaching Certificate sets from 2017 and 2019. **This, not the replacement, is where storage is actually recoverable.** It needs a decision nobody has been asked for. **Worth its own board card.**

**6. Whether Vimeo bills retained prior versions.** The replace path works by adding a version, so the old file plausibly persists. If retained versions still count against the allowance, every replacement costs storage twice and the plan decision inverts. **The API will not say.** One email to Kain's Enterprise contact settles it, and it should be sent before 2,145 replacements run. **Board it as a blocker on the replacement, not on the rename.**

### Yours to check against a document I am not allowed to edit

**7. The website column contract cannot be answered and I have not guessed it.** Your Step 4 asks which columns the import needs. **There is no course page template, no school page template and no curriculum renderer anywhere in the theme**, and `courses-setup.php` reads no lesson, section or curriculum. There is nothing whose needs I could state. **It falls out of the course page and school page specifications in minutes once those exist.** Until then it is a genuine specification gap and I have left it open rather than filled it.

**8. DSRD 5 section 1 counts 2,261 lectures. The spreadsheet holds 2,146 and Drive holds 2,145.** The map now shows our two working sources agree with each other to within one file, so **the 115 gap is between DSRD 5 and both of them**, not between them. DSRD 5 says of itself that its lecture counts came from the Udemy instructor dashboard. Either it is counting something else or it is stale. **Yours to check against the document; Kain's to rule.**

**9. Unusual characters that will end up in filenames.** The rename keeps everything the sanitisation rules do not name, per your instruction, so these survive into the new names: a right arrow in 25 lesson names, circled numerals in one, Greek in one, an accented character in one. All legal in a filename, all a little odd to meet in a video library. **Named rather than quietly stripped, because stripping them would be me editing Kain's copy.**

---

## Two corrections to your commissions, both already absorbed

**Your parsing rule would have misfiled four courses.** "Leading run of non-digit characters as the shortcode, then the digits" breaks on course 006, whose files are named `2020 FUNCBT 15 ...` and so open with a year; on 027 and 028, whose shortcodes contain numbers; and on 017, whose padding changes from three digits to two halfway through a course. **I derived each course's prefix from its own files instead.** You have since accepted this and confirmed the rename never parses an old name at all, which removes the risk rather than working round it.

**The split commission was rewritten twice while I was executing it**, and the H6 channel hook stopped me both times and made me re-read. **Nothing was built to a stale instruction and no complaint attaches to any of it.** It is named only because two superseded versions of that file exist in my transcript and neither is the one now on disk.

## One thing about my own work, since it bears on how far to trust the map

**The first eighteen course listings were transcribed by hand** from the Drive connector's output, before the payloads grew large enough for it to write them to a file instead. **Every one was then re-read from Drive and compared field by field.** That check found two errors of mine: a file size copied from the neighbouring row, and, invisibly, **two file names in course 016 containing a non-breaking space** which my hand copy had silently turned into an ordinary one. Every listing has since been rebuilt from the raw payload. **Nothing in the final map rests on a hand copy.**

*No em or en dashes in this file; checked before writing.*
