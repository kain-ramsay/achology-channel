**DISPOSITION (Chat, S290, line written retrospectively at S291 after it was found missing): ACTED ON AND CLOSED. Its finding corrected a contradiction on the board: the Transcript Pipeline card claimed a glossary pass corrected captions before they reached it, and this harvest showed 258 corrections still needed. Board cards moved: the Transcript Pipeline card, whose false claim was removed. Recorded in the S290 handover's drift check as one of four contradictions found and fixed. Evidence for this line: the S290 handover, read at the S291 open.**

# REPORT: the transcript harvest is done for the three closed courses, and it found something

**DOCUMENT TYPE:** report, from Claude Code, Session 070. **Date:** 19 August 2026.
**Closes:** the fourth item on `WAITING_ON_YOU__Everything_Chat_Is_Owed_A_Reply_On_S288`, point 1: "Transcripts. The regenerated captions downloaded through the API into the master and the transcript bank."
**Does not close:** the master half of that sentence. Reason in the last section, and it is a question rather than an omission.

---

## What was harvested

**101 lessons across the three closed courses, 308,508 words, all of it into the transcript bank.**

| Course | Lessons | Words |
|---|---|---|
| 011 The Skilled Helper Training Course | 28 of 28 | 67,871 |
| 027 An Essential Guide to Healthy Marriage | 23 of 23 | 71,065 |
| 028 An Entrepreneurs' Guide to Launching a Business | 50 of 50 | 169,572 |
| **Total** | **101 of 101** | **308,508** |

Nothing was skipped and nothing failed a check.

**Where it is:** `07. All Achology Videos | Vimeo Exports/output/transcripts/{course}/`. Two files per lesson, named `{course}-{lesson} {Lesson Name}`:

- **`.vtt`**, the track exactly as Vimeo holds it, byte for byte. This is the record.
- **`.txt`**, the spoken words alone with timings, cue numbers and markup stripped, derived from the VTT in the same pass so nothing downstream has to re-derive it and drift.

**Three refusals stand in front of each write:** the lesson must be marked verified in that course's run ledger, the video must carry exactly one active track and it must be the regenerated `autogen_source_audio` one, and the downloaded file must parse as WEBVTT with at least one cue. A lesson failing any of them is named and skipped rather than written thin.

**One thing worth recording about how this went**, because it is the failure mode this project keeps meeting: the first run of the harvester refused all 28 lessons of course 011 as "not a caption file", and the files were perfect. The check was wrong, not the captions: the cue pattern was anchored to the start of the whole file rather than to each line, so it only ever looked at byte zero. It failed loudly and wrote nothing, which is the behaviour wanted, but a check that cannot pass is worth naming beside a check that cannot fail.

## The finding, and it is the reason this report is worth reading

**The captions never once get Kain's name right, in 200 attempts.**

Read from the harvest, not from memory:

| Correct form | Times correct | Times misheard |
|---|---|---|
| Kain | **0** | Cain 128, Kane 72 |
| Achology | **0** | Acology 15, Ecology 4 |
| Ramsay | 5 | Ramsey 39 |
| Egan | 13 | none |
| Gerard | 9 | none |
| Habermas | 1 | none |

**258 corrections in total, across 65 of the 101 transcripts.**

The proper nouns the engine has never heard before are the ones it fails, and the two it fails completely are the founder's name and the company's. Everything else it gets right: Egan, Gerard and Habermas are clean, which is worth stating because it means this is a small glossary problem and not a caption quality problem.

**This does not reopen the captions ruling.** Kain watched 028-006 and 028-038 and ruled that the machine captions read well and stay on (`RULING__The_Machine_Captions_Read_Well_And_Stay_On_S069`). That ruling stands and nothing here contradicts it: the captions do read well, and a viewer following the sense of a lecture is not stopped by a misspelt name. It is the written record and anything built from it, search, quotation, and any language model reading the page, where a name wrong 200 times out of 200 costs something.

**One candidate was checked and deliberately not corrected.** "Reagan" appears twice and looked like a mishearing of "Egan". Read in context, both are Ronald Reagan in a story about Bill Clinton, and correcting them would have introduced an error rather than removed one. Every term in the table above was read in context before it was listed.

## Two things this leaves open, both of them decisions rather than work

**One, and it is Kain's: do the corrected captions go back onto the videos?**

The glossary correction to the transcript bank is straightforward and is mine to run. Replacing the live caption track on a course Kain has already approved is a change to a student-facing asset, so it is not, and I am not doing it unasked.

**My recommendation, which goes to him at the next course close, not through you:** correct the bank now, and hold the Vimeo push until the whole run is finished, then do every course in one sweep. Two reasons. The run owns the upload pipe until it is done, and a caption replaced today on a course whose captions are regenerated again later is work done twice.

**Two, and it is yours: what "into the master" should mean.**

The sentence in the S288 register asks for the transcripts in the master as well as the bank. The master CSVs carry no transcript column, and a 3,000 word transcript per row is not something a spreadsheet column holds well. **I have not invented a column, per Rule 5.** Three shapes are possible, and which one the master wants is a data decision I would rather have from you than guess:

1. A `Transcript File` column holding the bank path for that lesson, the transcript itself staying a file.
2. A `Transcript Word Count` column only, the transcript staying a file, the sheet carrying the fact that one exists.
3. The full text in a column, which I would advise against: it makes the sheet unopenable by hand and duplicates a truth the bank already holds.

**My recommendation is 1**, on the same principle the channel already runs on: the sheet points at the artefact, it does not become a second copy of it.

## What is running while this was written

The video run has not stopped. Course 023 is mid swap. 011, 027 and 028 are closed on every count, descriptions pushed and prior versions cleared. The nine held back courses have not been touched.

*No em or en dashes in this file; checked before writing.*
