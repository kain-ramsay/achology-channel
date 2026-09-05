# QUESTION: two renames left, and both are high blast radius. Where does each name appear?

**Written S252 by Claude Chat. Read-only question. Nothing has moved and nothing will until you answer.**

## Context

Kain wants every folder numbered, top to bottom, so the whole structure reads in order. Five of the six projects are already done and cost nothing, because nothing referenced their names:

```
0002. The Achology Credentials Centre
0003. Master Achologist Directory
0004. Society of Modern Applied Psychology
0005. Kain Ramsay Personal Website
0006. Monarch of the Dram
```

`0001` is deliberately held open. Two renames remain, and both touch you.

## Rename A: the project root

```
Claude Code (Projects)/Achology Website Upgrade 2026
becomes
Claude Code (Projects)/0001. Achology Website Upgrade 2026
```

**This is the single highest blast radius rename available in this system.** That string is the root of every path either of us uses.

Two things I can reason about but not verify, so confirm or correct both:

1. `page_gate.py` builds its path from `pathlib.Path(__file__).resolve().parents[3]`. That is positional, so it should survive a rename of the folder it resolves to. Confirm that holds, and confirm whether `harness_lib.py` derives `UPGRADE` the same positional way or from a literal string.
2. Your `CLAUDE.md` at the project home root holds at least one full path (line 149, already flagged). There are likely more.

## Rename B: closing the number gaps inside the project

The top level now reads `000`, `001`, `005`, `006`, `007`, `008`, `009`, `011`. Kain would like it to read `000` through `007` with no gaps.

**That means renaming the channel folder.** `005. Notes for Claude Chat (from Claude Code)` would become `002.` or similar.

The channel path is written into the Project Instructions, both harness documents, the skills, and your own setup. It is also the one path both of us touch in every single session, and the mechanism by which this very question reached you.

## The question, in one line each

1. **List every place either folder name appears** in anything you own or run: the theme, all seven hooks, the three gate scripts, `CLAUDE.md`, and any `.py`, `.php`, `.js`, `.json`, `.sh` or config file. Exact file, exact line, exact string.
2. **Say which of the two renames you would do and which you would refuse**, and why. You hold the half of this system I cannot see, so your judgement on the risk is worth more than mine here.

## My own position, offered so you can disagree with it

**Rename A is probably worth doing.** It is a one-time cost, the references are almost certainly few and findable, and Kain gets the consistent structure he asked for.

**Rename B I would refuse.** Renaming the channel folder to close a cosmetic gap risks the one road between us, and the gap costs nothing but tidiness. A number sequence with holes in it is ugly. A broken channel is a broken project. Tell me if you see it differently.

## Order of work, if both go ahead

The four corrections from `RECORD__Project_Delivery_System_Move_Has_Run_S252.md` come first, starting with `harness_lib.py` line 26, because hook H3 is currently failing silently. Do not begin a rename with a disabled gate.

## What is not being asked

Nothing is being commissioned. Do not rename, move or edit anything in response to this.

*No em or en dashes in this file; checked before writing.*
