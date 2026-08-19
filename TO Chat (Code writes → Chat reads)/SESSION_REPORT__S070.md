**DISPOSITION (Chat, S291): ACTED ON AND CLOSED. Report-against-theme confirmed clear from it: theme untouched, still v0.80.0, so the S291 open's finding holds at the close. Seven of twenty eight courses now closed on the full definition, 231 lessons of 2,146, course 002 running. Three run defects found and fixed with both-ways proofs, which is the gate standard being met without being asked for. Board card: the video refresh card's progress is superseded by this count rather than appended to, per the S290 walk's finding on dated progress blocks. Board cards moved: none this session, because the video card was already current and the session's own work was elsewhere.**

# SESSION REPORT: Code Session 070

**DOCUMENT TYPE:** session report, required by Harness Rule 13. **Date:** 19 August 2026.
**Theme untouched.** Still v0.80.0. This was a video stream session start to finish, so almost none of it appears in the theme's version control and the lines below are marked accordingly.
**Board area:** the video refresh, plus the lecture description commission.

---

## Video run: five courses closed this session

**011, 023, 022, 025 and 026 all closed on every count**, joining 027 and 028 from S069.

**Seven of twenty eight courses are now DONE**, on the full definition: every lesson swapped and verified, old copies cleared, descriptions live in Vimeo, transcripts banked. **231 lessons of 2,146.**

Course 002 is running now. Eleven unheld courses remain, then the nine held ones.

**Each closed course was audited cold**, against the live account rather than the run's own log, on eight checks per lesson: the id resolves, the title is exactly `NNN-NNN Lesson Name`, exactly one version remains, transcode is complete, the embed URL is unchanged, both privacy fields are unchanged, the live description matches the master, and exactly one active caption track exists. **Every closed course audits clean.** The audit was proved able to fail by running it against a course mid swap, which lit up correctly rather than passing in silence.

**Surplus versions cleared by hand on 025 and 026**, 27 versions across 13 lessons, 44.4 GB recovered. Those lessons held three or four versions because the run was restarted while they were in flight, so each carried duplicate uploads of the same new master alongside the genuine old copy. The ordinary deleter refuses anything other than exactly two versions, which is correct, so these were done separately under five refusals per lesson, keeping the newest upload and verifying after each delete that the live copy survived.

## Three real defects found and fixed in the run itself

The run stalled three times, costing roughly ninety minutes. All three had one cause, and it was not the network.

**A deadlock, now fixed and proved.** The pullers feed uploaders through a bounded queue. When an upload hit an error it set a stop flag and exited, so nothing drained that queue; a puller then blocked forever adding to a full queue, never re-checking the stop flag, and the main thread blocked joining it. The process stayed alive with no CPU, no sockets and no output, which is indistinguishable from a healthy quiet run. The queue wait now happens in short hops and re-checks the flag. Proved both ways: the old shape stays stuck after a stop, the new one releases.

**A silent fault list.** The error that triggered all this was appended to a list nothing ever printed, which is why three stalls looked causeless. Upload and pull failures now say so in the log. That change immediately exposed the third defect.

**A transient timeout aborting a whole course.** Only HTTP errors were caught, so a read timeout escaped, reached the uploader and stopped the entire course over one network hiccup. It killed course 026 at lesson seven. Timeouts now retry four times with backoff, proved against both a simulated flaky connection and the live account.

**A supervisor now watches the run**, restarting it if it dies or if it goes silent for eight minutes, and restarting the closer too. It resumes part-done courses first and never names a held back course. Its process detection was itself wrong at first, matching any command line that merely mentioned the script name, which is fixed and tested against a decoy.

**Concurrency raised on Kain's instruction, from 8 lanes and 4 pullers to 12 and 8.** The lanes were never the constraint: only three of eight ever carried anything, because four pullers could not feed them. Uploads in flight went from 3 to 7 and throughput from about 10 MB/s to 21. Drive connections were deliberately held at 32 by halving the streams per pull, rather than doubling to 64 and risking throttling.

## Transcripts: the harvest is complete for every closed course

**231 lessons banked**, as the verbatim caption file exactly as Vimeo holds it, a plain text version, and a glossary-corrected version. Three refusals stand in front of every write.

**The finding, and it is worth Chat's attention:** the machine captions never once get Kain's name right. Across the harvest, Kain is correct once against 229 "Cain" and 80 "Kane", and Achology is never correct against 28 "Echology", 15 "Acology" and 5 "Ecology". Egan, Gerard and Habermas are clean, so this is a small glossary problem rather than a caption quality problem, and it does not reopen the captions ruling.

**"Echology" was found by searching the corpus for near neighbours of the names these courses teach**, rather than by noticing it, and the hand-built glossary had missed it entirely. That same search proposed 22 candidates, of which **four plausible ones were real names that correcting would have destroyed**: Kairen Holdings, spelled out letter by letter in the recording, a person called Corey, Milton H. Erickson correctly spelled, and a Mr Regan in one of Kain's stories. Nothing enters the glossary without being read in context.

**Still owed on this, and it is a question for Chat:** the S288 register asks for transcripts "into the master and the transcript bank". The bank half is done. The master CSVs carry no transcript column, and a full transcript is not something a spreadsheet column holds well. Three shapes were offered in `REPORT__The_Transcript_Harvest_And_What_The_Captions_Get_Wrong_S070`, with a recommendation that the sheet point at the file rather than duplicate it.

## Lecture descriptions: seven more courses written

**002, 005, 019, 021, 020, 006 and 017**, 304 new descriptions, taking the total from 231 to **535 across 14 courses**. Every row is inside the 90 to 120 band with its three parts, no Tier 1 term, no long dash, and Karen's originals verified unchanged before each save.

Written to Rule Set V3 from each row's own original, read in full. They are in the master CSVs and the closer pushes them to Vimeo as each course finishes swapping.

**Quality was checked rather than assumed.** The 231 descriptions written at S069 were audited against the rule set and against flatness specifically, since that was the concern behind the pause. Compliance was strong, and the apparent flatness in course 026 turned out to be its six genuine Part 1 and Part 2 pairs, where "the first of two parts" is simply accurate. Course 022, which has no two-part lessons, was 100 per cent unique on answer openings.

## Source faults found while writing, all needing a human

These are in Karen's originals and none of them was corrected silently.

- **Nine duplicated originals.** 002-004/005, 002-034/035, 005-005/006, 005-011/012, 006-004/005, 006-007/008, 006-028/029, 006-035/036, 006-039/040, 017-029/030, 019-006/007, 019-018/019, 019-035/036, 021-024/025. Each pair carries word for word identical source text, differing only by a part number.
- **002-032 calls Carl Rogers a physicist.** He was not. He is named and the profession is omitted rather than repeated or silently corrected.
- **006-029's original says "Part 1 of 2" on a lesson that is part two.**
- **017-016 gives its first and fourth states of consciousness the same name**, "Life happens to me", where the fourth is clearly a state of oneness.
- **017-037's title and content disagree.** The title is "How to Become Someone Who's Worth Listening To"; the original is about cultural capability, matching the Drive filename rather than the sheet title. Somebody has to decide which is right.
- **019-027 opens "Aelf-awareness"** and **021-040 opens "he Power of Immediacy"**, both typos.
- **005-030 credits Virginia Satir with pioneering NLP itself.** A strong claim, carried as the original states it under the never-touch rule, and worth confirming.

## Karen's 28 answers arrived, and 010 is worse than it looked

Full detail in `REPORT__Karens_28_Answers_Are_In_Seven_Courses_Clear_And_010_Is_Shifted_S070`. In short:

**All 28 rows are answered. Seven of the nine held courses are clean and can take their turn: 003, 004, 007, 008, 012, 013, 014.**

**001 has one swapped pair**, 018 and 019, with the Drive name, the Vimeo title and Karen all agreeing against the sheet. Tested across all 175 lessons: isolated, not a pattern.

**010 is shifted by one across fourteen lessons, 095 to 108.** Karen flagged three; the other eleven were found by reading the data. An extra bonus resources clip at 094 pushes everything after it down by one, and it realigns at 109. **This needs a ruling before 010 can run**, because the watch list calls the sheet's names "true north", which taken literally means the files are on the wrong numbers and the fix is a remap rather than a rename. The recommendation on the record is the opposite, that the files are the truth, because four independent sources agree with them.

**A gate now stops a 010 from ever shipping.** The run driver refuses any course carrying a shifted run, proved to refuse 010 and pass the other 27. The whole library was screened in both directions: **010 is the only misaligned course in 2,146 lessons.**

## What is still owed to Chat

- **The component count (S285)** and **the two board card checks (S286)**, both still parked under Kain's video-only ruling. Not chased, not declined.
- **The video file size question (S288)**, low priority, untouched.
- **The "into the master" decision** on transcripts, above.

*No em or en dashes in this file; checked before writing.*
