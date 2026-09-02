DONE: the folder is back in Documents and the S095 move ruling is overturned. Supersedes RULING__The_Project_Folder_Moves_Out_Of_Documents_S095.md.

# RULING: the project folder stays in Documents and is never moved again

**From:** Claude Code, Session 096. **Date:** 2 September 2026.
**Authority:** Kain, ruled directly in the S096 sitting, after the move he had approved at S095 was executed and cost him an evening.
**His words, quoted:** *"Yes, just dont ever move this again - this has just created unneeded problems."*
**Filed under Harness Rule 14.**
**Board card:** Hosting and Go-Live.

---

## What was ruled

**The project folder stays where it has been for seven months, in `~/Documents`, and is never moved again.** `RULING__The_Project_Folder_Moves_Out_Of_Documents_S095.md` is overturned by the same authority that gave it. The folder was moved at this open and moved back in the same session; it is back, with every path restored, git intact and clean at commit `9b56454`, and the hooks resolving normally.

## What the move actually cost, said plainly because it is the lesson

The move itself worked and the backup job came alive. Everything after that was the problem. iCloud kept restoring the old folder, met the signpost left in its place, and made numbered duplicates. Chat could no longer see the project files. Kain was asked to change a setting he should never have had to think about, and was then told that setting would empty his Documents folder. None of that was foreseen in the S095 ruling, and all of it was foreseeable.

**The judgement error, named:** the S095 ruling weighed what the move fixed and not what it disturbed. A folder that three Claudes, a connector, a sync service and seven months of habit all point at is not a plumbing detail, and moving it was never the small technical call it was filed as.

## The backup job

The hourly off-machine copy of the written record cannot run from `~/Documents`, which is what the move existed to fix. **The launch agent is now unloaded rather than left failing every hour.** Fixing it is Code's, by a route that does not touch Kain's folders: the obvious one is a small copy of the record kept outside `~/Documents` for the agent to read, which is Code's to build and needs nothing from anybody.

Until it runs, every change set is committed and pushed by hand, which Rule 9 already requires.

## Nothing for Kain

The Filesystem connector question is dead: the folder is where it always was, so nothing needs repointing. No setting on his machine was changed.

---

OWED BACK: nothing. Chat writes this into the document that owns the machine's setup and strikes the S095 ruling there.

*No em or en dashes in this file; checked before writing.*
