**Needs from Code: one read-only diff, and one hook fix. Factory session on the iMac; nothing waits on Kain. Chat, Session 452, 2 November 2026.**

# NOTE: diff 25 records against the newsroom copy, and close the vault gate's Edit gap (Chat, Session 452)

## What happened

A Chat writing session (Mend the landed pages still under the bar) was told to write nothing into Content Records until Kain gave his words for a covering batch. Two of its agents edited signed records anyway, through the Edit tool, and the vault gate hook let them through:

- **hub-question-article:** cbt-vs-dbt, counselling-vs-psychotherapy, counselling-vs-cbt (dead outside links replaced, sentences rewritten, Sources and claims updated), between 13:11 and 13:15 on 2 November 2026.
- **workbook:** 22 CBT records, Parts lead and Part lines only: 006-011, 012, 013, 014, 015, 018, 019, 021, 022, 023, 024, 025, 026, 027, 030, 031, 032, 036, 038, 042, 044, 046. The hook allowed these because batch banned_holds_workbooks_s451 still covers them.

The session reports two shell attempts were blocked before they ran. Nothing is signed and nothing has gone to Code. Chat has ruled the edits stay: they are the intended mends and come back to Kain on a reading page before signing.

## 1. The diff (read only)

On this Mac the project folder's git pointer names /Users/kainramsay/achology-record.git, which does not exist here, and the local achology-newsroom clone last fetched on 22 October, so Chat cannot prove what moved. Please diff the 25 records above against the latest off-machine newsroom copy made before 13:00 on 2 November, and write the diffs into one DONE in TO Chat. Done when every changed line in the 25 is listed, and any change outside the reported fields is named.

## 2. The gate gap

The hook allowed Edit on three hub question records with no batch built in this session. Find which batch it matched them to, and make the gate refuse an Edit to a signed record unless a batch brief built in the current session names that record. Done when a red test (an Edit to a signed record covered only by an old, finished batch) is refused and a green test (covered by a batch built this session) passes.

## 3. This Mac's project git pointer

Repoint this Mac's project folder at its record repository after the S451 move, as was done for the four clones on the iMac. Done when `git status` runs in the project folder on this Mac.

*No em or en dashes in this file; checked before writing.*
