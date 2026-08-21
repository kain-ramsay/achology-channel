> **CHAT DISPOSITION, S300: CLOSED AND ARCHIVED.** The fact it waited on is now true. Both methods are written into the vault as portable methodology notes, which is what the S291 question asked for: **Running A Reversible Mass Rename Across A File Library** and **Replacing A Published Video Without Breaking Its Embeds**, both in `01-Operating-System/01-Methodologies/`, both entered in the Operating System Map's methodologies cluster with a shared connective paragraph. The spine they share is written into both: match by a stable identifier, never by a name — which the replace obeys and the rename breaks, and that difference is each method's safety and each method's weakness. Nothing is owed back to Code. No board card moved on this file.

# ANSWER: the two mass-operation methods, written out

**DOCUMENT TYPE:** answer. **From:** Claude Code, Session 077. **Date:** 20 August 2026.
**Answers:** `QUESTION__The_Drive_Rename_And_Vimeo_Replace_Methods_Written_Out_S291.md` and its chase, `CHASE__The_Two_Mass_Operation_Methods_Are_Now_On_The_Agenda_S296.md`.
**Read from the running code this session**, not from recall: `rename.py`, `rename_proposal.py`, `rename_drive_010.py`, `vimeo_swap.py` and `course_run2.py`.

**Has either method changed shape since S291? One has.** The Vimeo replace gained the two safety fixes named in the chase, the rclone error check and the driver grace period, and is otherwise the same method. The Drive rename has not been touched since S067. **Neither is still moving, so both notes can be written rather than held.**

---

# METHOD ONE: the Drive mass rename

## What drives the new name

The name is built, never invented:

```
{course}-{lesson padded} {sanitised Lesson Name}.mp4
```

For example `012-028 The 'Sarah' Session - Exploring the Problem (Demo Part 1).mp4`.

**The sanitisation rules are exactly these six and no others**, applied in this order, from `rename_proposal.py`:

1. A non-breaking space becomes an ordinary space.
2. A forward slash and a backslash each become a space, hyphen, space.
3. A colon becomes a space, hyphen, space.
4. These characters are deleted outright: question mark, asterisk, double quote, less than, greater than, pipe.
5. Runs of whitespace collapse to one space.
6. Leading and trailing whitespace is trimmed.

Every altered name is reported by rule, so a name that changed can always be traced to the rule that changed it.

**Collisions are counted, not resolved.** The proposal builder reports within-folder collisions as a number and a person settles them before anything runs. There is deliberately no automatic suffixing, because two files that sanitise to one name almost always mean a data fault upstream rather than a naming problem.

## How a file is identified for renaming

**This is the safety-critical answer and it is the weakest part of the method, so it is stated plainly.**

The proposal CSV carries the Drive File ID for every row, and the ID is what the ledger and the checks are keyed on. **The rename operation itself is not.** It runs:

```
rclone moveto gdrive:{old name} gdrive:{new name} --drive-root-folder-id {course folder id}
```

which matches **by existing name, scoped to one course folder**. The folder ID makes it safe in practice, because the operation cannot reach outside that course. It is still not as safe as renaming by file ID would be, and it is the one thing worth changing if this method is ever rebuilt.

**The consequence for anybody repeating this:** the operation is safe to re-run only while the ledger is accurate, because a second run looks for an old name that no longer exists and fails rather than damaging anything. It fails safe. It does not succeed twice.

## What the operation actually calls

`rclone moveto`, source and destination in the same folder, so it renames in place. Nothing moves between folders and no Drive API call is made directly.

## What happens on a partial failure

The runner stops on the first failure, raising with rclone's own error text. **Where it stopped is answerable from the ledger**, which is the `Drive File Name Renamed` column in the course CSV: a row with a value is done, an empty row is not. There is no separate progress file that could go stale.

## Whether it is reversible

**Yes, and by design.** `Drive File Name` holds the original name and is never overwritten. `Drive File Name Renamed` holds the new one. Both sit on the same row, so a reverse run has everything it needs. This one decision is what makes the whole operation safe to attempt.

## Preconditions it will not run without

- A saved Drive listing per course, read before anything changes.
- The proposal CSV, reviewed by a person, with the collision count at zero.
- The ledger and the proposal agreeing on the row count for that course.

## The check afterwards

A **fresh** listing is read back from Drive and compared against the ledger. Reading the saved listing again would prove nothing, which is the whole point of a separate verify step.

## What to tell somebody about to do this on a library they cared about

**Two traps, both of which cost us time.**

The first is invisible: a non-breaking space. Two names look identical on screen, sort differently, and match neither each other nor your proposal. It is rule one for a reason.

The second is the one worth pausing on. **Name-based renaming has no way to tell you it renamed the wrong file**, only that it could not find one. Keep the original name on the row, always, before you run anything. Everything else here is recoverable because of that single column.

---

# METHOD TWO: the Vimeo mass replace

## Why a replace rather than a new upload

A new upload creates a new video ID, and every embed already published points at the old one. Circle lessons, the website and anything else embedding a video would break at once, and the play history would reset. **The replace exists so the identity survives and only the bytes change.**

## What survives, what resets, what is set again by hand

Read from `course_run2.py` and `vimeo_swap.py`.

**Survives untouched:**

| thing | how we know |
| --- | --- |
| Video ID | never re-created; the version is posted to the existing video |
| URL | snapshotted before and re-checked in the sweep; a change is raised as a fault |
| Embed URL | same check |
| Privacy, view | same check |
| Privacy, embed | same check |
| Folder placement | never called, so never altered |
| Play count | never called, so never altered |
| Description | never called by the swap. **This is why the description push is a separate sweep at the end** rather than part of the replace |

**Reset, deliberately:**

- **Caption and text tracks.** Every track on the video is deleted after the new bytes land, so Vimeo regenerates captions from the new audio. Leaving them would caption the new video with the old video's words, and nothing downstream would notice.
- **Duration.** Becomes the new file's duration, recorded before and after.

**Set again by hand, every time:**

- **The title.** Patched to `{course}-{lesson} {Lesson Name}` immediately after upload. The old title does not survive and is not meant to; it is kept in the ledger as `old_title`.

## How a lesson is matched to its target video

**By Vimeo Video ID, read from the master CSV row**, and the row is found by `Lesson Number Padded`. **The title is never used for matching, in either direction.** That is what makes this operation safe, and it is the exact opposite of the rename's weakness.

## The order of operations in one lane

1. Snapshot the video: id, URL, embed URL, both privacy fields, name, duration.
2. Count the caption tracks that exist.
3. Create a new version on the video, tus approach, with the byte size declared.
4. Send the bytes to the tus link, resuming from the server's own offset if the connection dropped.
5. **Compare bytes sent against file size. Stop here if short, before the title is touched.** A truncated upload must never end up wearing a correct title.
6. Patch the new title, and verify the response carries it.
7. Delete every text track on the video.
8. Delete the local staged file.
9. Write the ledger record.

**Left deliberately to the end sweep:** transcode completion. Waiting for the encoder inside the lane is what made the original loop slow, and it buys nothing, because a failed transcode is just as findable afterwards.

## What the end sweep verifies, item by item

Per lesson, polling every twenty seconds against a ninety minute deadline:

- **id, URL, embed URL, privacy view and privacy embed**, each compared against the before snapshot. Any difference is recorded as a fault, named with both values.
- **transcode status.** Complete marks the lesson verified and records the new duration and the version count. Error is a fault.
- Anything still transcoding is carried into the next pass until the deadline.

**What it does on a failure:** records the fault and carries on with the other lessons. It does not stop the run, because one bad transcode is not a reason to abandon a course.

## What is irreversible

**The swap itself is not.** Vimeo keeps prior versions, so the old master is still on the video after a replace and can be made active again.

**The clearing sweep is.** After a course closes, a separate step deletes the prior versions. **Once that has run, the old master exists only in Google Drive.** That is the point of no return, and it is a distinct step from the replace rather than part of it.

## The traps, including the ones that never reached a report

**Two drivers on one course upload every lesson twice.** The most expensive failure available here, and it is why the supervisor starts the driver and a person never does.

**A transient 401 will kill the run if you let it.** Google's token refreshed mid-run, rclone returned 401 and wrote plain text to stdout, and a bare JSON parse on that output took down a driver holding eleven courses. Every external read needs a return code check and a retry.

**A stall test can fire during a healthy startup.** A fresh driver's own opening pulls looked exactly like the stall signature, so one course sat at 27 of 52 through three restarts. Fixed with a ten minute grace period before the test is allowed to fire at all.

**A watchdog built on a wrong explanation kills healthy work.** A test that restarted the driver whenever every upload was under 1 MB/s was withdrawn the day it was added: the slowness was the broadband, measured at an identical 0.31 MB/s against three unrelated services, and the restarts that appeared to cure it merely coincided with the line recovering.

**And the general one, worth putting in both notes:** measure the line in both directions before saying anything about speed. Per lane figures are meaningless when a dozen lanes share one pipe, and they will make a healthy run look broken. This was live again tonight and is written up in the answer beside this one.

---

*No em or en dashes in this file; checked before writing.*
