# REPORT: the 117 salvage heroes are renamed, converted and attached, and the re-attach found a second stale thing nobody was watching

**DOCUMENT TYPE:** report, from Claude Code, Session 104, factory session. **Date:** 6 September 2026.
**Answers:** `BRIEF__Rename_Kains_117_Salvage_Masters_And_Run_The_Whole_Set_Through_The_Pipeline_S343.md`, its whole OWED BACK line.
**Board cards:** the rescued field-authority articles; Image and icon optimisation.

---

## 1. The rename, and the two-way check

`tools/salvage_hero_rename.py` is new and is committed with the run (theme repo, `6fcd3ab`). It does the brief's section 2 rule mechanically and prints the before-and-after table; the table is 117 lines and is in the run rather than pasted here, because this file is transport and not storage.

**Live run: 118 exports in, 117 renamed, 1 discarded, 0 unresolved, 0 blocking faults.**

**The discarded file is page 1**, `Why People Seek Help, and What They Actually Need From It.png`, exactly as the brief said it would be. It is identified by reading the map's own row 1 rather than by matching the filename, so a change to the Canva page order cannot quietly promote the instructor image into the run.

**The two-way check is clean in both directions: 117 map rows, 117 masters, every row has a picture and every picture has a row.** No gap either way, so nothing was reported past.

**The broken filename you asked about is already fixed and it was Chat who fixed it.** The Piaget master arrived carrying the separator, so it renamed by the ordinary rule with no key-words fallback needed. Its map row is row 36, `jean-piagets-contributions-to-developmental-psychology`, key words "building blocks, stages". Your S345 rename at source is what made that possible, and the map row itself needs no correction. The script still carries the key-words fallback, because the shape will recur the next time Canva eats a name.

**One thing worth knowing about the export.** These are 1980 by 945, not the 1760 by 840 the S340 brief names from the instructor precedent. Same 2.095 to 1 shape, more pixels, so nothing is cropped and the derivatives are if anything better fed. Named rather than silently accepted.

**The masters were moved, not copied.** The brief asks for a move in those words, and a copy would leave two canonical masters for every article and 262MB of them. Neither the Canva subfolder nor the zip was deleted; Kain deletes his own originals.

## 2. The pipeline

234 derivatives written through `image_pipeline.py` at the hero slot, 680 and 1360 wide, WebP at quality 82, into the theme's `images/knowledge-hub/articles/`. **Every one inside DSRD 7 section 12.3's 200KB budget at 2x, with nothing recompressed and nothing over.** The largest sits around 22KB.

**The 17 counselling-slug pairs already in that folder are the instructor articles' heroes**, not orphans of this set. Named here so nobody tidies them away: their records are in `Content Records/instructor-article/`, they have no master in the salvage folder because they never did, and they were left untouched.

## 3. The import and the attach

**117 of 118 records pass every import check; 117 sent as drafts; 117 verified clean off the install.** Nothing published, and the importer's `post_status` is still a hardcoded literal `draft` with no input path around it.

**The one refusal is not a record.** `Report__Row_110_Named_Exception_And_Gate_Fixes_S342.md`, a Cowork report file, is sitting in `Content Records/field-authority-article/` and is read by the importer as a record with every field missing. It is refused correctly and it costs nothing, but it makes every count in that folder read 118 where the truth is 117. **Ask: move it out of the records folder**, to wherever Cowork's reports belong. Not moved by Code, because it is not Code's file.

## 4. The re-attach, which found a second stale thing

**Section 4 item 5 of your brief was not going to happen, and the brief is what caught it.** `attach_hero()` returned on its first line the moment a post already carried a thumbnail. So Kain's revised pictures would have gone onto the 34 new drafts and never onto the 83 that already had one, and nothing downstream could have told: the page would have rendered a picture, just the wrong one.

**Then the importer's own `--verify` found the second half.** `finding-lifes-purpose-with-viktor-frankls-mans-search-for-meaning` was carrying the alt text `Man's Search for Meaning by Viktor Frank` on the install, against its record's own `Finding life's purpose with Viktor Frankl: the book behind logotherapy and its three routes to meaning`. **The cause is your S344 keyword reassignment**, which correctly rewrote that record's alt when the keyword moved to the book note; the install never heard about it, because the alt is only written on a fresh attach and that post already had one. **How many others carried a stale alt cannot be known retrospectively**, because the old value was overwritten this session; it is now impossible for any of them to be stale again, which is the useful half.

**The fix, and it is deliberately the smaller of the two available.** The kept branch now rewrites the alt from the record every run, and replaces the picture's bytes in place where they differ from the master. **The attachment id, its address and every reference to it are untouched**; only the file behind it changes, and `wp media regenerate` rebuilds the sizes WordPress derived from it. The alternative, a second attachment plus a delete of the first, breaks every reference to the old id and needs a delete against the posts table, which H9 refuses on sight and rightly.

**The run says the comparison works rather than asserting it: 83 pictures replaced, 34 kept.** That is exactly the 83 whose bytes came from the superseded masters and exactly the 34 this session had just created from the new ones. Nothing failed.

**H9's register is updated and its wall is not weaker.** `import_field_authority_articles.py` takes a new sha256 with a new reading recorded beside it, naming all four commands the changed branch runs and why none of them can publish, change a status or create or remove a post. **H9's own acceptance suite reads 63 of 63 after the edit**, including the case that proves a reviewed exception dies when its file changes.

## 5. What this brief does not close, and why

**The rendered half of step 4 has not run**, and by your own S345 ruling it cannot: srcset and sizes, width and height, lazy loading, the hero's `fetchpriority`, the image sitemap row and the `ImageObject` in the schema are all read off a rendered page, and every one of these is a draft. They run on publication, on the exemplar first, with a stop-and-report on any failure, exactly as your ruling sets out.

**Publishing is still blocked**, and not on anything in this brief. It waits on the two answers named in `ASK__Only_252_Redirect_Rows_Are_Buildable_And_The_Wall_Refuses_All_Of_Them_S104.md`, in its opening section: the DSRD 6 section 5 item 11 exception at 89, and whether DSRD 2 section 3.2 or 3.8 governs these articles. **Nothing else stands between these 117 and a publish run.**

**No theme file changed and nothing was deployed.** The derivatives sit in the theme's images folder because that is where S102 put them, but no template, stylesheet or script references that folder: it is the pipeline's working store and the importer's source, not something a page reads. Named so the absence of a deploy is not read as an omission.

---

OWED BACK: the ruling on moving Cowork's report file out of the records folder. Nothing else on this brief.

*No em or en dashes in this file; checked before writing.*
