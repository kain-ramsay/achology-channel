# RULING: the project folder moves out of Documents

**From:** Claude Code, Session 095. **Date:** 2 September 2026.
**Authority:** Kain, ruled directly in the S095 sitting, on the finding in `REPORT__What_The_Machine_Move_Actually_Cost_S095.md`.
**His words, quoted:** *"yes, move it at the start of our next session"*.
**Filed under Harness Rule 14:** a ruling given in session is authority at once and reaches the record the same session, so Chat writes it into the document that owns it.

---

## What was ruled

**The `CLAUDE | Anthropic Ai` project folder leaves `~/Documents`.** It is moved at the start of S096, before other work.

## Why, in one line

A background job cannot read `~/Documents` on this Mac, so the hourly off-machine copy of the written record has been dead since 10:57 on 2 September and cannot be revived where the folder currently sits. The channel repository does the same work every two minutes without trouble from `~/achology-channel`, outside the protected folder. The move also takes the project folder out of iCloud, which closes the question S094 raised and nobody had ruled on.

## Where it goes, which is Code's call and overturnable in one word

**`~/CLAUDE | Anthropic Ai`**, keeping the folder's exact name and changing only its location. The alternative considered was renaming it to sit beside `~/achology-channel` as `~/achology`; rejected because a rename and a move at once doubles what can break and loses the name Kain reads in Finder.

## What the move breaks, named before it runs rather than found during it

**The permission rules.** `.claude/settings.json` names the Documents path in every read, edit, write and search rule. They are rewritten with the folder.

**The hook launcher.** `~/.claude/achology_hook.py` holds the one real path this project still writes out, by design, and it points at Documents. One line.

**The autosave's launch agent**, written at S095 and currently failing, names the script under Documents. One line, and it is the thing the move exists to fix.

**Code's own memory.** Memory notes are stored under a folder named after the project's path (`-Users-kainramsay-Documents-CLAUDE---Anthropic-Ai`). A different path means a different folder, so **the next-session note does not follow the project automatically** and must be carried across by hand as part of the move, or S096's successor opens blind. This is the one consequence that could quietly cost a session, which is why it is written here rather than left to be discovered.

**Nothing in git.** The repository is the folder, so its history, its remote and its state travel intact.

## What does not change

The channel, at `~/achology-channel`, is untouched. The theme's own paths are relative to the theme. Every tool that locates itself from its own file keeps working; only the four places above name the folder from outside it.

## The proof the move worked

The autosave's status file updates on its own within the hour, without anyone running it by hand. That is the whole point of the move and it is the only thing that proves it: a folder that has moved and an agent that still cannot read it would look identical to today.

---

OWED BACK: nothing. Chat writes this into the document that owns the machine's setup; Code executes it at the S096 open and reports the status file updating on its own.

*No em or en dashes in this file; checked before writing.*
