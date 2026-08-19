# BRIEF: build the content hash drift check for the pasted instruction sets

**DOCUMENT TYPE:** approved brief, from Claude Chat, Session 290. **Date:** 19 August 2026.
**Approved by:** Kain, in session, S290.
**Answers:** your design proposal in `ANSWERS__The_Generator_Count_The_620_Pages_And_The_Instruction_Drift_S063`, section 3.

---

## What is approved

Your design, as you wrote it. Build it.

Each versioned instruction document carries a marker line holding a content hash of everything below the marker. The hash is written by the same script that commits the file, never by hand. Whoever is reading a pasted copy reads its hash at session open, and the hash of the file in the repository is computed and compared. They match or they do not.

Kain approved this on your reasoning: a version number only catches a drift somebody has already noticed, and a hash catches an edit that forgot to bump the number as readily as a paste that never happened.

## Which documents it covers

The instruction sets that live as a file in the repository and also as a pasted copy neither of us can read back. That is the Project Instructions and the operating instructions. If your reading of the ground finds others in the same position, name them rather than assuming them in or out.

The three harness documents are not in this class, because both of us read them from disk. Say so if you disagree, because you can see the ground and this is written from the outside.

## The properties it has to hold

**The marker line survives a paste.** That is the whole reason this design was chosen over a commit hook. A hook fires where the file is, not where the copy is.

**It runs every session, not on change.** The dangerous state is the one where nothing changes for three weeks and the copies have already parted. A check that only fires when the file moves never fires in that state.

**A mismatch is loud.** Printed by the machinery, not remembered by either of us, and not something either side can wave past. Same shape as the heartbeat, and it works for the same reason.

**Nothing in it ends with Claude updating the live copy.** Neither of us can. The check reports; Kain carries the change across, which is the one thing only he can do.

## What is not asked for

Do not change the folder map generator. That was a separate question in the same file and it is settled without a code change: 42 is the recorded figure, and the Archive is now named as the deliberate exclusion in the project folder map at the root. Nothing for you there.

## Acceptance

Confirm through the channel that the check is installed, and prove it the way every gate in this system is proved: show it refusing. Change one character below a marker in a copy, run the check, and file the mismatch printout. A passing run is not evidence.

*No em or en dashes in this file; checked before writing.*
