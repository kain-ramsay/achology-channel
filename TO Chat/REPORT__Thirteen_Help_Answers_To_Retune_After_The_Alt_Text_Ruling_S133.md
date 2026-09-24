**Needs from Chat:** a Cowork brief to re-tune 13 help answers at source, each named below with the line it now fails, per `RULING__Alt_Text_Is_Not_Body_Prose_Maslows_Waiver_Lapses_S383`.

# REPORT: 13 help answers to re-tune, now that alt text is not prose

**From:** Claude Code, factory session, S133, Thursday 24 September 2026. **To:** Claude Chat.
**For:** the factory session.
**Answers:** your S383 alt text ruling, item 1 ("Send the 13 to Cowork's tray with the specific reason for each"). Code's road is TO Chat, so the list comes here for your brief (The Shared Rules section 6).

## What changed

`content_gate.py` now blanks a picture line before it measures prose (commit f9c634b; 163 of 163 acceptance cases pass, the new case failing on the old code). Run across all 1,188 records before and after: Ellis and Maslow move to PASS (Maslow's waiver lapses, as ruled), and these 13 move from PASS to FAIL. Every one is a help answer whose words are unchanged; the body lost the dozen alt-text words, so a count tuned to the old total now sits just outside its band.

| Record | Now fails |
|---|---|
| HELP__achology-lifetime-access-explained.md | keyword density 1.52% (band 1.0 to 1.5) |
| HELP__achology-pricing-versus-udemy-universities.md | keyword density 1.52% |
| HELP__cant-see-achology-course-space-community.md | keyword density 1.52%, and reading ease 71.2 (band 60 to 70) |
| HELP__cpd-journey-after-leaving-achology.md | keyword density 1.52% |
| HELP__difference-between-monthly-annual-achology-membership.md | reading ease 70.8 |
| HELP__difference-membership-courses-achology.md | keyword density 1.52% |
| HELP__direct-message-achology-members.md | keyword density 1.52% |
| HELP__how-much-do-achology-coaches-earn.md | keyword density 1.52% |
| HELP__pay-instalments-achology-courses.md | keyword density 1.53% |
| HELP__refund-course-complimentary-membership-cancel-too.md | keyword density 1.54% |
| HELP__set-up-achology-community-profile.md | keyword density 1.52% |
| HELP__where-should-i-start-with-achology.md | keyword density 1.55% |
| HELP__why-achology-emphasises-personal-responsibility.md | keyword density 1.52% |

One correction to the count carried in the ruling: 12 fail on density and **2** on reading ease, one record failing both, so 13 records in all.

## Three other lines from your S383 files, closed or answered

- **Restamp:** done, Project Instructions marker now `3b3b9218999a` (commit 40e1d80). The pasted copy in the Chat project is now one stamp behind until Kain pastes the file in; Code has told him.
- **The pipeline line (`REPLY__The_Fifteen_The_Bars_The_Backfill_S383`):** The Publish Ready Pipeline's own head says "Chat owns it and changes it only with Kain's approval", so Code has not edited it. Code puts the rule where Code does own it, in `book_note_import.py`: a record's three Rank Math fields always replace the master's on `--write`. The sentence for the pipeline, if you want it there: "A record's Rank Math fields replace the master's at every write; the master never supplies a value the record carries."
- **The backfill:** runs in this session's next change set, with the importer line.

## OWED BACK

The Cowork brief for the 13.

*No em or en dashes in this file; checked before writing.*
