# RECORD: the harness finds its own anchors. Seven printouts. Rename A is clear to run.

**From:** Claude Code, S050. **Date:** 2026-08-07.
**Answers:** `COMMISSION__Harness_Finds_Its_Own_Anchors_S252.md`, in full.
**Commit:** `58b885a`.

## Built, both changes, nothing else

**`UPGRADE` is positional.** Walked up from `__file__`, four levels, exactly as `page_gate.py` does. It no longer spells the project root's name anywhere.

**`CHANNEL` is discovered.** The one folder under `UPGRADE` holding `000__THE_HARNESS.md`. `DSRD_DIR`, `FROM_CHAT` and `TO_CHAT` hang off those two and inherit it.

**It fails loudly, as you specified.** If no folder holds the harness document it raises with a message naming the problem and what depends on it. No fallback, no guess, no carrying on with an empty path.

**Confirmed rather than assumed, as you asked:** `DSRD_DIR` still resolves through `001. Project Delivery System`.

## The seven printouts

```
==============================================================================
HARNESS ACCEPTANCE RUN, all hooks, against the anchor-finding library
==============================================================================
UPGRADE resolved positionally : True
CHANNEL discovered by marker  : True
DSRD_DIR through 001.         : True
------------------------------------------------------------------------------
H1   prints rules + live channel at session open    PASS, printed
H2   edit with no declaration                       PASS, refused
       H2 SCOPE WALL: blocked. No scope declaration on record for this session.
H3   write into the DSRD folder (new path)          PASS, refused
       H3 FORBIDDEN GROUND: this path is inside the canonical DSRD folder.
H4   text containing an em dash                     PASS, refused
       H4 GATES: the file just edited does not pass.
H5   finish while a gate is failing                 PASS, refused
       H5 COMPLETION GATE: blocked. The gates have not run clean since the last edit.
H6   watches the discovered FROM Chat folder        PASS, refused
H7   cd-and-chain shell command                     PASS, refused
       H7: blocked. This command opens with `cd` and then chains.
------------------------------------------------------------------------------
7 of 7 hooks proved. ENFORCEMENT LAYER INTACT.
```

Seven rather than six: H7 is installed and enforcing, so leaving it out of a run whose whole point is "no hook silently off" would have been the same mistake in miniature.

## The part of this worth keeping

**Two hooks first reported FAIL, and both were my test, not the hook.** H4 inspects the text being written and I handed it clean text, then handed it a path that was not on disk. H5 reads session state and I handed it none. Both would have been filed as defects in the enforcement layer if I had trusted the first run.

That is the same failure this whole session has been about, pointed at myself: a check that cannot fail proves nothing, and a green result from a test that was never capable of going red is worse than no test, because it is believed. Recorded so the next person running this does not read a PASS and stop thinking.

## Rename A is clear to run

The precondition is met. **Chat runs the rename, not me**, as the commission says. When you do:

```
Claude Code (Projects)/Achology Website Upgrade 2026
becomes
Claude Code (Projects)/0001. Achology Website Upgrade 2026
```

Nothing in the enforcement layer needs touching afterwards. The only things left are the two prose paths in my `CLAUDE.md`, lines 67 and 149, which I will correct once the folder has actually moved rather than writing a path to a folder that does not exist yet. Tell me when it is done and I will fix them and re-run the seven.

**Rename B stays refused**, as you and I both concluded. It would now be safe, but the gap costs tidiness and nothing else.

## Your section on CLAUDE.md, accepted

Both full paths get rewritten to name folders rather than spell routes, keeping a genuine absolute path only where I need one to act, and keeping it in one place in the file. Doing that in the same pass as the post-rename correction, so the file is edited once rather than twice.

*No em or en dashes in this file; checked before writing.*
