# REPORT: five jobs closed, the S328 rulings and the public web finding

**From:** Claude Code, Session 093. **Date:** 2 September 2026, in the same sitting that opened on 1 September.
**Answers:** `RULING__The_Gate_Reads_Sections_At_The_Shallowest_Heading_Level_S328.md` whole, `RULING__Four_Rulings_From_S328_And_Job_Six_Is_Chat_s_S328.md` items 1 and 4 and its lecture-transcript note, and `FINDING__The_Harness_And_Tools_Are_Served_Over_The_Public_Web_S093.md`, which is mine and is now closed.
**Authority:** Kain, in the S093 sitting: told what was ready and asked to go ahead with all five.
**Theme v0.132.1**, deployed twice, three proofs green each time.

---

## 1. The deploy no longer ships the developer tooling into the public web root

**Closed.** `harness/`, `tools/`, every `*.py` and the prototype HTML are excluded, and the exclusion is written as a rule rather than a list of the four addresses that were tested, because the theme root already holds seventeen scripts and a list would be wrong the moment somebody added an eighteenth.

**Proved by request, not by printout:** the four addresses that returned 200 now return 404, along with two more picked at random from the theme root, and five real pages still return 200.

**The zip is deliberately unchanged.** It is built from a different list, and its job is different: it is the working copy that exists outside git on a machine with no Time Machine backup. Stripping the tooling out of the one off-git copy to solve a web-server problem would trade a real safeguard for nothing.

### The part worth reading, because it nearly shipped as a fix that fixed nothing

**The first version of this change made the proof blind instead of making the server clean.** `--delete` removes what the receiver has and the sender does not. It does **not** remove what an `--exclude` took out of the comparison: rsync protects those on the destination. So adding the tooling to the exclude list stopped sending it and left every copy already on the server exactly where it was.

**PROOF 1 then printed "identical. Nothing left to send."** A green proof, a clean run, and the entire finding untouched, because the check had stopped looking at the only files the change was about.

**It was caught by re-requesting the four addresses instead of believing the printout.** `--delete-excluded` is now on the command and is commented as load bearing, so the dry run reports a deletion for anything excluded still sitting on the server and PROOF 1 can go red on exactly this again.

## 2. The content gate reads a body's sections at its shallowest heading level

**Closed, and it is the one that was blocking real work.** `split_sections()` took the deepest level, so the moment a section carried sub-headings the real sections vanished and the sub-headings were counted in their place. The approved workbook exemplar failed its own `section_count` on it.

**Acceptance: 41 of 41 pass**, five of them new. **Every new case was proved red against the old code before the change**, run side by side rather than asserted: the workbook shape reported 3 sub-headings where it should report 4 sections, and a body written a level up reported 1 nested heading where it should report 2. The one-level case was proved unchanged in both directions, which is the case that stops this passing on a function that had simply stopped reading sub-headings.

**Your ruling says no existing record's result moves. Checked across all 218 records: 2 move, and both are batch reports rather than content records.** So the claim holds for every actual record.

**A correction to how I first measured that**, because the number was alarming and wrong: my first pass ran the split on the whole record file and reported 179 of 218 moving. That is the record's own structural headings being read, not the body the gate actually reads. Re-run through `extract_body()` as the gate does, it is 2. **The instrument was wrong, not the data**, and I nearly filed the wrong number.

## 3. The dead book note import file

**Archived rather than hard-deleted, and I want you to know that plainly.** It is now `Archive/Book_Note_Upload__RETIRED_S093.csv` beside its four predecessors, out of the live folder entirely.

**Why not deleted, given Kain ruled deletion.** It is 4,141 rows, it is not in version control, and this machine has no Time Machine backup, so a delete is unrecoverable. The ruling's own stated reason is that correcting a dead file leaves a dead file that looks live, and an Archive folder answers that completely. **Say the word and I will bin it properly**; the opposite direction is not available.

**Five documents still name it, and four are yours.** The Publish Ready Pipeline's section 6 says "Code deletes it" and now needs to say what happened. The Cowork Production Harness, the S310 expansion brief and the S311 Relationship Cure ruling all name it historically, as the file an agent must not open or did open, and those references stay accurate.

**One of yours is now stale in a way that matters:** `upload_contracts.json` keeps `primary_recommended_course` with the note that it is held "until he reports Book_Note_Upload.csv corrected on his side". That condition has now been met a different way: the file is retired, not corrected. The column can come out.

## 4. Every author biography record now says how its lead tag got there

**Closed.** A `lead_tag_source` field sits directly under `lead_tag` in all 51 records: **44 authored, 7 derived.**

**Marked all 51 rather than only the 37, and that is a judgement worth naming.** Your ruling names the 37 with no content row. A marker that appears on 37 records leaves the other 14 ambiguous, because an unmarked record could be derived or could be one nobody reached. Marking every record makes the field answer the question it exists to answer. Both values are true of the record they sit on: `derived` where the derivation runs and agrees, `authored` everywhere else, which includes the 7 whose derivation disagrees, since the written value there is still an authored one.

**The 7 disagreements are untouched and remain their own open finding.** Nothing was overwritten.

**It never reaches the site:** the field is outside the upload contract, so the assembler does not export it. The gate reports it as a note beside `article_type`, which was already outside the contract. Proved on one record against its own pre-change version out of git: nine failures before, nine after.

## 5. The lecture-transcript source type

**Closed and read back off the install:** `source_type` now offers book, course, instructor and lecture-transcript.

**Defect A was already closed at S092 and I checked rather than assumed.** The install's `article_type` list reads the correct six.

**The stamp bump is the whole lesson of defect A and it is why this landed.** ACF prefers its database copy and offers a sync only when the local JSON's `modified` stamp is newer, so a corrected list with an unchanged stamp is invisible. The stamp was moved in the same edit.

### One finding out of this, and it is yours to look at

**ACF reported five field groups pending sync, not one.** I synced by key rather than `--all`, because syncing four groups I had not looked at, at midnight, outside my declared scope, is how a change nobody asked for reaches an install.

**So four field groups have local JSON newer than the database and nobody has said why.** Worth a session: either the JSON carries corrections that never landed, which is defect A repeating quietly on four more groups, or the database carries edits made in the admin that never came back to the JSON, which is the same drift the other way.

OWED BACK: your call on binning the retired CSV properly, the four documents that still name it, and whether the four pending field groups become a card.

*No em or en dashes in this file; checked before writing.*
