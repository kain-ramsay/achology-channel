> **CHAT DISPOSITION, S332: read and archived.** Its one decision, moving the project folder out of Documents, was ruled by Kain in the same sitting and is carried by RULING__The_Project_Folder_Moves_Out_Of_Documents_S095.md. The Kit plan limit is noted on the S311 Kit ruling's own line by Code. No further action here.

# REPORT: what the machine move actually cost, measured on a full working day

**From:** Claude Code, Session 095. **Date:** 2 September 2026.
**Why:** S094 moved onto the 2019 iMac and reported what it had proved that night. S095 is the first full working day on it, so this is the move judged on real work rather than on a checklist. Kain asked what you need to know.
**Board card:** the machine move.

---

## The move is good, and today is the evidence

S095 ran a full day's work with **no failure caused by the move**. Everything the project depends on was exercised on real targets, not tested: the hooks fired and refused work four times, SSH and WP-CLI read the build install repeatedly, the Search Console service account signed and pulled 47,541 rows from the live property, the URL inspection run resumed from its own file and added 250 addresses, both git repositories committed and pushed all day, and the channel watcher carried every file.

**Two things S094 left open are now closed.** Time Machine's first backup completed at 16:05 today, encrypted, hourly from here. And the URL inspection's resumable state did come across: the tail file was at 1,770 rows and picked up cleanly, which S094 could not confirm.

## One thing the move broke, and nobody had looked

**The hourly record autosave has not run since 10:57 today, and it cannot run at all on this machine as things stand.**

Its launch agent did not come across. I rebuilt it and loaded it, and it fails every time with the same fault: **`Operation not permitted`** reading `record_autosave.py`.

**The cause is where the project folder now lives.** It sits in `~/Documents`, which modern macOS protects. This session can read it because Kain granted the Claude app access when it asked. **A background job is never asked, so it is simply refused.** The proof sits beside it: the channel watcher does the same kind of work every two minutes without complaint, and the only relevant difference is that the channel repository lives at `~/achology-channel`, outside the protected folder.

**What this costs.** The written record's hourly off-machine copy is the S058 protection against a machine with no other backup. It has been silent for seven hours. Today's work is safe because Rule 9 had me commit and push every change set by hand, but anything nobody commits by hand, and there are uncommitted files in the project repo right now, has no automatic route off this Mac.

**I have left the agent installed and failing rather than removing it.** The script's own header says a job that has not run for a week must look different from a job that failed, and a silently deleted agent looks like neither. It will start working the moment the cause is fixed, with nothing further to do.

## The decision this hands Kain, and it settles two open questions at once

**Move the project folder out of `~/Documents`.**

It fixes the autosave, because a background job can read a folder outside the protected ones, as the channel watcher proves every two minutes. And it closes the iCloud question S094 raised and nobody has ruled on: `Desktop and Documents` sync is on, the project folder is inside it, and that is the same stub road the channel deliberately left. Zero `.icloud` stubs today, checked at the open, but the risk is structural rather than lucky.

**The alternative is granting a permission**, and today gave a clear reading on that route: the same protection blocked the Time Machine check, and the grant there would have had to be redone at every Claude update. Permissions granted to work around a location are a standing maintenance cost. Moving the folder once is not.

**This is Kain's, not mine.** It moves the whole project folder, it touches how every path in every tool resolves, and it is his machine. I have not moved anything.

## One capability lost, unrelated to the move

The Kit account now answers that this plan does not include the connection I read it with. `RULING__Install_Kits_Plugin_S311`'s second check cannot be verified from this side until that changes.

---

OWED BACK: Kain's ruling on moving the project folder out of `~/Documents`, which is the one thing standing between the written record and its hourly off-machine copy.

*No em or en dashes in this file; checked before writing.*
