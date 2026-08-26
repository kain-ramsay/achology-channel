> **CHAT DISPOSITION, S318: DONE. The publish gate deadlock, the importer's three Rank Math fields and the article type list are all closed on both sides; this file closes RULING__All_Eighteen_Records_Carry_Instructor_Attributed_Delete_The_Three_S318. Board: Author Biography Articles card and the instructor articles card carry the state. Archived.**

# REPORT: three jobs closed at the tail of S087, on Kain's instruction to do them rather than hand them back

**From:** Claude Code, Session 087, 26 August 2026.
**Ruled by:** Kain, in session, plainly: do it and give me what I need rather than making me the admin.
**Closes:** `RULING__All_Eighteen_Records_Carry_Instructor_Attributed_Delete_The_Three_S318`, `RULING__Instructor_Becomes_Instructor_Attributed_And_Big5_Is_Dead_S310`, and Code's own `ASK__The_Article_Type_List_Disagrees_With_Its_Own_Register_S085`.
**Corrects two lines in `SESSION_REPORT__S087`**, which was written before these ran: the publish_gate deadlock is fixed rather than owed, and the book note import fix is done rather than waiting on the Safari sitting.

---

## 1. The publish_gate deadlock, fixed

A clearance refused on any failing machine row. Two of those rows measure content quality: the Rank Math score against the bar, and density against move 7's band. **So a page scoring 80 could never be cleared, and therefore could never be updated into passing 81.** The gate blocked the only work that would satisfy the gate. It surfaced on the five page density experiment, whose whole purpose is to lift five pages from 80, every one of which was unclearable.

**The rows are now split by what they are for.** Structural rows say the page is sound: right address, trail matching the hierarchy, links resolving, assets loading, record present. Those refuse a clearance, first publish or hundredth update. Quality rows say how good it is; they still run and still print, and they are written onto the clearance as the measured state before an update, so an update always has something to be judged against afterwards.

**Quality rows still refuse a FIRST publish**, because a page going in front of the public for the first time below the bar is exactly what the wall was built to stop. They do not refuse `--update` on a page already live. Kain's words when he ruled the wall were that nothing goes in front of the public unchecked, not that nothing goes in front of the public below 81, and only the first of those is the wall's business.

## 2. The book note import carries its Rank Math fields

`META` gains `rank_math_focus_keyword`, `rank_math_title` and `rank_math_description`. **This is the single cause of all 65 published book notes scoring between 0 and 16.**

**It was safe to do ahead of the Safari sitting**, and that is worth stating because the S087 note said it should wait. The coupling was always to `LOCKED_HEADINGS` and to RUNNING the import, never to editing a different constant in the same file. Nothing has been run: proved with `--plan`, which reads the records and writes nothing. The import still waits on the headings pass exactly as it did.

**And the defect underneath it is closed.** `report_unmapped` now names, on every run, every field a record holds that the import carries nowhere. Silence on an unmapped field has cost two findings on this one script: the lead tag at S086, these three at S087. It prints rather than refuses, because a record may legitimately carry production notes and a check people switch off is worth nothing.

**Its first run found 16 stranded fields, and they were checked rather than assumed.** Against `single-book_note.php`, the template reads exactly one of them, `primary_recommended_course`, which is retired at S255 and already authorised for removal. `prod_cover_image_alt` belongs to the media upload step that waits on artwork, per the S086 attachment-ID finding. **The other fourteen are production notes.** So the import drops no page data beyond what is now fixed.

## 3. The article type list is the six-type register, and the install agrees

Both sides moved in one pass, as those rulings require.

**Eighteen rows on the install** went from `instructor` to `instructor-attributed`. Read back: zero on the old value, eighteen on the new.

**The three superseded choices are deleted** from `group_article_fields.json`, leaving exactly the six DSRD 1 §3.2 registers. `school-authority` and `big5` were checked before deleting and no row on the install carried either, so nothing was orphaned.

**One thing left alone deliberately.** `source_type` has its own `instructor` choice, meaning the source is an instructor page. Different field, not superseded. Named here because the two read alike in a search and only one of them was to go.

**The three types `RULING_AND_REPLY__Every_TO_Chat_File_Closed_Out_S306` named as missing were already added at S085.** Verified present rather than added a second time.

## 4. State

Three change sets, committed, pushed and deployed. All three deploy proofs CURRENT. The wall's acceptance run is 39 of 39.

OWED BACK: nothing on these three. The five page density experiment can now run, which it could not four hours ago.

*No em or en dashes in this file; checked before writing.*
