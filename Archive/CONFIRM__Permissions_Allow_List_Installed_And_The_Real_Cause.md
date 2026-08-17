# CONFIRM: the allow list is installed, and the prompts were my habit, not the list

**From:** Claude Code, S046. **Date:** 2026-08-05.
**Closes:** `BRIEF__Permissions_Allow_List_To_Stop_Approval_Prompts.md` (Chat, S235).
**Supersedes the open state of:** `PROPOSAL__Permissions_Allow_List.md`, now approved
and installed.

## What happened today

Kain was interrupted again, this time to approve **reading a specification
document**, and asked why. He then approved the proposed list.

**It was already installed.** I opened `.claude/settings.json` and every rule in the
proposal was present: the allow list, the ask list, the deny list, all as proposed
and unchanged. So there was nothing to install, and installing it would not have
helped him.

## The real cause, which my own proposal had already named

From `PROPOSAL__Permissions_Allow_List.md` §"the actual cause": "Permission patterns
match the whole command string, and almost every command I run is a compound one...
Every `cd X && Y` I run is unmatched, whatever Y is, and that is most of what I do."

I wrote that on Monday and then spent this session doing precisely that. The command
that stopped Kain today began with a folder change, so it matched nothing, exactly as
predicted. The list was never the defect. The habit was.

The proposal also said the second half of the fix "is mine, not Kain's" and "needs no
approval". That half had not been done.

## What I have changed, permanently

1. **No compound `cd X && Y` commands.** Absolute paths everywhere.
2. **Files are read with the Read tool and searched with Grep**, both of which run
   silently across the whole project home. Shelling out to read is what produced most
   of today's interruptions.
3. **No python heredocs for reading.** `Bash(python3:*)` sits in the ask list on
   purpose, because arbitrary python can delete or transmit anything. That prompt is
   correct and I have not weakened it. Where analysis genuinely needs python, the
   prompt stands.

This is written into my memory index so it survives the session, which is the only
place a habit fix can actually live.

## The confirmation the brief asks for, in one line

Since the change, every read-only command in this session has run without stopping
Kain: the specification reads, the theme searches, the git status and log calls, and
the gate runs. The prompts that remain are the ones that should: the deploy over SSH,
the network fetch, and the file moves.

## The harness is unaffected, re-confirmed

Nothing in the permission lists can write into the DSRD folder, edit
`000__THE_HARNESS.md`, or touch a file outside the declared scope, because the hooks
are a separate mechanism. Today's evidence, unarranged: **H2 blocked four writes**
this session for undeclared paths, twice while accept-edits mode was on, and **H4
blocked one edit** for an em dash it caught in text I had just written. Both refused
regardless of what the permission system said.

## One thing left, and it is Kain's to decide, not urgent

`.claude/settings.local.json` has grown to **347 lines** of one-off approvals, each a
whole compound command string approved once and never matching again. They are now
mostly dead weight, and every one of them is a rule nobody has reviewed. It could be
emptied safely, since the reviewed list in `settings.json` is what actually governs.
I have not touched it. Raise it with him when nothing more useful is competing.

*No em or en dashes in this file; checked before writing.*
