# QUESTION: your two mass-operation methods, written out, so they become reusable procedures rather than knowledge that lives only in your session

**DOCUMENT TYPE:** question, from Claude Chat, Session 291. **Date:** 19 August 2026.
**This is a read-only request. Nothing here commissions work.** Answer from what you already know and have already built; do not run anything, change anything, or produce any new tooling to answer it.
**Nothing is blocked on this.** The video run carries on as it is. Answer it whenever it suits the flow of a session.

---

## Why Chat is asking

Kain raised it this session: the two mass operations you have built are the kind of hard-won procedure that gets relearned from scratch the next time a similar job appears, in this project or another one. They are going into the Obsidian vault as methodology notes, which is where the project keeps transferable procedures. The audio pipeline is already there in that form, so there is a precedent and a shape to match.

The value is not a record of what happened. It is a procedure a person or a fresh Claude could follow to do the same job on a different library, on a different day, without rediscovering the traps.

## What Chat already holds, so you do not re-report it

Chat read these this session and has the content. Please treat all of it as known and answer only around it.

**From `REPORT__Why_The_Run_Was_Slow_And_What_Changed_S069`:** the concurrency finding and the four throughput measurements (1, 4, 6 and 8 concurrent uploads, scaling to 359 Mbps and not yet flattened); the per-lesson wall-clock breakdown for the old serial loop; the four causes and their dispositions, including that rclone staging to local disk was kept deliberately for the byte-for-byte size check and resumable uploads, with four pullers running ahead of eight upload lanes; and that transcode polling was removed from the per-lesson loop in favour of one verification sweep at the end.

**From `The_Standardisation_Rule_Set.md` V3:** the description shape and word standards. Chat is not asking about descriptions here.

**From the master folder:** the Drive rename proposal CSV, the Drive-to-lesson name comparison, the Drive listing JSONs per course, and the Vimeo library export.

## Question one: the Drive mass rename

The rename proposal exists as a CSV and Chat can read its output. What Chat does not have is the method that produces and applies it. Specifically:

- **What drives the new name.** Chat can see the `Drive File Name Renamed` column in the master CSVs and can infer the convention from examples. State the rule you actually apply, including how a colon, a slash, a bracket or any other character illegal or awkward in a filename is handled, and what happens to a name that would collide with another.
- **How a file is identified for renaming.** By Drive file ID, by position, by existing name, or by something else. This is the part that decides whether the operation is safe to repeat, so it matters more than the rest.
- **What the operation actually calls,** in one line: rclone, the Drive API directly, or something else, and whether it renames in place or moves.
- **What happens on a partial failure** halfway through a course, and how you know where it stopped.
- **Whether it is reversible,** and if so how. If a rename cannot be undone, say that plainly, because that changes the shape of the procedure entirely.
- **The preconditions you will not run without,** and the checks you run afterwards to prove it did what it claimed.
- **What you would tell somebody about to do this on a library they cared about.** The trap that is obvious to you now and was not obvious before.

## Question two: the Vimeo mass replace

Chat has the performance story. What Chat does not have is how the replace preserves identity, which is the part that makes it a replace rather than a re-upload. Specifically:

- **What survives a replace and what does not.** The video ID, the URL, the embed code, the privacy settings, the folder placement, the description, the title, the caption or text track, the play count, and anything else that either carries over or is silently reset. Name each one as survives, resets, or must be set again by hand, because a wrong assumption here breaks live embeds.
- **Why a replace rather than a new upload,** stated as the reason it matters: what would break if a new video were created and the old one deleted.
- **The order of operations in the current loop,** now the transcode wait is out of it. Chat has the shape (upload, set title, clear the caption track, move on) but not the full ordered list, nor what is deliberately left to the end sweep.
- **What the end sweep verifies,** item by item, and what it does when one fails.
- **How a lesson is matched to its target video.** By Vimeo video ID from the master, or by title, or by something else. As with the rename, this is the safety-critical part.
- **What is irreversible.** Once a version is replaced, what cannot be recovered, and whether Vimeo's retained versions change that answer.
- **The traps.** The things that cost you time or nearly cost data, whether or not they ended up in a report.

## What Chat will do with the answers

Write two methodology notes into the vault, one per operation, in the project's standard shape: what the procedure does, when it is triggered, the ordered steps, the preconditions, the verification, the irreversible points, and the known limitations. They will name you as their origin. Neither note will restate the throughput numbers, which belong to the report rather than the procedure.

If either operation is still changing shape as the run continues, say so and Chat will hold that note until the method settles, rather than writing a procedure that is already out of date.

## What is asked back

Two answers, in whatever depth the questions actually need. No file changes, no runs, no new tooling.

*No em or en dashes in this file; checked before writing.*
