# NOTE: Vimeo Support has answered, the storage question is closed, and the reply carries a third fact nobody asked for

**DOCUMENT TYPE:** note, from Claude Code, Session 068. **Date:** 19 August 2026.
**Closes:** question 4 of `ANSWER__Vimeo_Retains_And_Bills_Prior_Versions_And_The_Autosave_Needs_Full_Disk_Access_S285.md`, the one Chat could not settle from documentation and marked for Kain's Enterprise contact.
**Source:** Vimeo Support, Shruthi, Product Specialist, replying to Karen, pasted into the session by Kain. **Read alongside** `REPORT__The_Replacement_Cannot_Start_Yet_And_The_Storage_Sums_Were_Wrong_S068.md`, which measured the same things from the account an hour earlier.

---

## The two answers we asked for, and they agree with the measurement

**Retained versions do count against the allowance, on this account, from the vendor.** In their words: because older versions remain saved on the account, "they do continue to count toward your storage quota". **That closes the Enterprise question. There is no exemption.** It also matches what the account itself showed: 62 videos already carrying prior versions and 87.5 GB held in them.

**Prior versions can be deleted through the API, and the endpoint is the one the probe found.** Vimeo names Delete Video Version explicitly, and my refused probe had already established that `DELETE /videos/{id}/versions/{version_id}` is a live route wanting the `edit` scope. **Vendor answer and machine probe agree, independently.**

**One correction to carry, because Vimeo's reply repeats our own arithmetic back to us.** Their message quotes ~2.4 TB of replacement files and 4.9 of 7 TB used. Those are the figures Karen's email supplied, not figures Vimeo measured. **The measured figures are 2.767 TB to push and 5.324 TB held.** Their conclusion, that the run would exceed the allowance partway through, is right either way and is now confirmed twice.

## The fact nobody asked for, and it is the largest new thing in the reply

**"Replacing the video file will trigger the automated captioning process for the newly uploaded media."** Vimeo treats a replacement as a new source file for transcription.

**What that means here, in numbers from the 18 August export:** 2,146 lesson videos, of which **196 already carry a caption track and 1,950 carry none**. A full run therefore generates machine captions on roughly **1,950 lessons that have never had subtitles**.

**And they would be shown, not merely generated.** This account's own preferences carry `autocc_display_enabled_by_default: true`. Unless that is changed before the run, or the generated tracks are removed after it, **the swap quietly puts machine written subtitles in front of students on nineteen hundred lectures**.

**Why this is not a small thing for this project specifically.** The voice work already established that this material defeats a machine reader: the audio pipeline had to be fed "Ackology" to make it say Achology at all. Machine captions will spell every proper name in the curriculum however they hear it, on a paid product, with no one reading them first.

**The two watch items it creates:**

**One, the 1,950 with no captions.** New tracks appear and display. Kain's call, and it is a brand decision rather than a technical one: allow them, suppress them before the run, or generate them and hold them unpublished for review.

**Two, the 196 that already have captions.** An existing track stays attached to the video while the media underneath it is replaced. If the new master runs to a different length, the existing captions drift out of time against it. The size against length test says the Drive file and the Vimeo video are the same recording almost everywhere, so drift should be nil, but **these 196 are the rows where a wrong pair would be visible to a student as captions sliding out of sync**, and they are worth checking first rather than last.

## What this changes about the plan

**Nothing about the storage route.** Course by course, prior versions kept until the course is signed off, superseded sets cleared first: unchanged, and better supported now.

**One thing is added to the pre-flight:** the captions decision has to be taken before the first real course is replaced, because the alternative is removing tracks from hundreds of videos afterwards.

**And the one video proof gains a fourth thing to watch:** whether a caption track appears on the test video after the replace, and whether it displays. That is now a question the proof can answer for nothing, since the test video will be created for the purpose anyway.

*No em or en dashes in this file; checked before writing.*
