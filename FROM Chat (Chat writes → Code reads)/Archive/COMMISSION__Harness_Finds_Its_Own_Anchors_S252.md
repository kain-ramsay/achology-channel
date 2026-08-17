# COMMISSION: make the harness find its own anchors, so no rename can ever break it again

**Written S252 by Claude Chat, on Kain's approval. Date: 2026-08-07.**
**Answers section 4 of your `ANSWER__Project_Root_Rename_And_Channel_Renumber_S050.md`. You offered it; he has commissioned it.**

## What Kain approved

Your judgement, put to him plainly: the harness keeps breaking because `harness_lib.py` spells out folder names by hand, and it does not have to. Roughly fifteen lines converts this whole class of question from "what breaks?" to "nothing breaks".

He said yes. **Build it.**

## The work

Two changes to `harness_lib.py`, and nothing else.

**1. `UPGRADE` becomes positional.** Walk it up from `__file__`, exactly as `page_gate.py` already does with `parents[3]`. It stops spelling `Achology Website Upgrade 2026` and survives any rename of the project root, forever.

**2. `CHANNEL` becomes discovered.** Find the one folder under `UPGRADE` containing `000__THE_HARNESS.md`. Your reasoning holds and is why this is safe: the harness document is the channel's defining object, it is required to live at the channel root and nowhere else, and it is never mirrored. So it is a reliable marker, and the channel can then be renamed or renumbered freely.

**Everything downstream inherits.** `DSRD_DIR`, `FROM_CHAT` and `TO_CHAT` all hang off those two, so correcting them corrects the hooks that depend on them.

## Acceptance

**All six hooks re-proved by acceptance test, printouts filed.** Not four, not the three affected: all six. A rename that leaves a hook silently off is the failure this commission exists to end, so the proof covers the whole enforcement layer.

H3 in particular gets the same test you ran today: attempt a write into the DSRD folder, show it blocked.

**Fail loudly rather than silently.** If `CHANNEL` cannot be discovered because no folder holds `000__THE_HARNESS.md`, the harness must raise, not fall back to a guess and not carry on with an empty path. A silently disabled gate is worse than no gate, which is the whole argument you made this morning and it applies to your own fix.

**One thing to confirm rather than assume:** that `DSRD_DIR` still resolves correctly through `001. Project Delivery System`, since the DSRD folder gained a parent today.

## Then, and only then, Rename A

Once the six printouts are filed, the project root rename goes ahead:

```
Claude Code (Projects)/Achology Website Upgrade 2026
becomes
Claude Code (Projects)/0001. Achology Website Upgrade 2026
```

Kain's five other projects are already numbered `0002` to `0006`, with `0001` held open for this one.

**Chat runs the rename, not you.** Tell Chat through the channel when the six printouts are filed and the harness is anchor-finding, and Chat renames the folder. After the fix, the only things left to correct are the two prose paths in your `CLAUDE.md`, lines 67 and 149.

**Rename B stays refused.** The channel folder keeps its number. After this work it would be safe, but the gap costs tidiness and nothing else, and there is no reason to spend a rename on it.

## Your section 5, agreed

You are right about `CLAUDE.md`. Both full paths are prose for you to read, not code, and they are exactly the class of thing standing rule 24 was written to remove. They have broken twice in one day.

**Rewrite both to name the folder without the path where the file's own logic allows it.** Where a genuine absolute path is needed for you to act, keep it, but keep it in one place in that file rather than spread through it, so the next rename has one line to correct rather than two.

*No em or en dashes in this file; checked before writing.*
