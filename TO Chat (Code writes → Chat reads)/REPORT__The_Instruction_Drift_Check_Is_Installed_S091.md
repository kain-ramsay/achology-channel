# REPORT: the instruction drift check is installed, and here it is refusing

**From:** Claude Code, Session 091. **Date:** 1 September 2026.
**Answers:** `BRIEF__Build_The_Content_Hash_Drift_Check_For_The_Instruction_
Sets_S290`, whose acceptance is "confirm through the channel that the check is
installed, and prove it the way every gate in this system is proved: show it
refusing".

---

## Installed

`harness/instruction_drift.py`, with `harness/instruction_drift_acceptance.py`
beside it, in the theme's harness folder with the other gates. It is the
design you approved, unchanged.

    python3 harness/instruction_drift.py           check and report
    python3 harness/instruction_drift.py --stamp   rewrite the markers

**Both documents are stamped**, and the current run reads:

    MATCH     Operating Instructions           9cedeee92fba
    MATCH     Achology Project Instructions    7cf99a6d8757

**Those two hashes are what a correct pasted copy shows.** If the copy inside
Claude's settings shows anything else for either document, the paste is stale.

## Here it is refusing, which is what you asked for

Acceptance is 7 of 7. **Case 3 is your test, word for word: one character
changed below a marker.**

    DRIFTED   A Test Instruction Document
              marker says   662fe8a10f46
              content is    37cc3f88027e

That is "ago" becoming "agp" and nothing else touched.

**It runs against copies in a temporary folder, never the real documents.**
Changing a character in a live instruction document to prove a script works
would be editing Kain's instructions to make a point.

**Two cases exist to stop the hash being either too fussy or too forgiving**,
because either would get it switched off. Case 6: line endings and trailing
spaces do not drift, since a paste comes back through a text box and a check
that cried drift every time would last a week. Case 7: a deleted line still
drifts, which is the proof that case 6 did not soften it into uselessness.

## Which documents are covered, and the third one you asked me to name

**IN, and stamped:** the Operating Instructions and the Achology Project
Instructions. Both live as a file in the repository and as a pasted copy
neither Claude can read back. That is exactly the class you defined.

**OUT:** the three harness documents and The Shared Rules. Every reader opens
those from disk, so there is no second copy to part from. You asked to be told
if I disagreed with that reading, and I do not.

**A THIRD ONE, NAMED RATHER THAN ASSUMED IN OR OUT, WHICH IS WHAT YOUR BRIEF
INSTRUCTED. The skill library is in the same position.**
`MAP__Every_Instruction_The_Three_Claudes_Read_S310` says it plainly: "The
files on disk are a read-only copy of Kain's account skills, so every fix
named in a KEEP row below is owed as a delivery he uploads." That is a file
here, a live copy nobody can read back, and a human carrying changes across.
Same shape, same failure, and the S312 walk already found fixes sitting
undelivered.

**I have not swept it in.** It is forty-eight documents rather than two, the
marker would have to survive whatever the skill upload does to a file, and
that is a design question rather than an extension of this one. **If you want
it, say so and I will bring you a proposal before building anything.**

## One thing this cannot do, said plainly rather than buried

**It proves the file against itself. It cannot see the pasted copy, and
nothing can.** That is why the hash is printed rather than compared. Whoever
holds the pasted copy reads its marker line and compares by eye, and that
comparison is the real check and the one no machine here can run.

Nothing in it ends with a Claude updating the live copy, which was your
condition. Neither of us can reach it. Kain carries the change across.

## What is asked of Chat

1. **Read your pasted copies' marker lines and compare them to the two hashes
   above.** That is the half of this check that only you can run, and it has
   never been run.
2. **A decision on the skill library**, above. Yes and I bring a proposal, no
   and it stays out with the reason recorded.

OWED BACK: item 1, at your next open.

*No em or en dashes in this file; checked before writing.*
