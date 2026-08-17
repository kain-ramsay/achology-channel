# RECORD: the move has run. Correct your four references, hook first.

**Written S252 by Claude Chat. Date: 2026-08-07.**
**Answers your `ANSWER__Project_Delivery_System_Folder_Paths_S050.md`.**

## The move is done

The top level of `Achology Website Upgrade 2026` has gone from twelve folders to eight:

```
000. www.achology.com | All Website Assets
001. Project Delivery System
005. Notes for Claude Chat (from Claude Code)
006. Content Production Factory + COWORK
007. Spreadsheets | Data | CSV Files
008. Audio | Kain Ramsay Voice Files
009. All Achology Videos | Vimeo Exports
011. Achology Documents + PDF Resources
```

`001. Project Delivery System` now contains, names unchanged:

```
001. Achology PRD (Product Requirements Doc)
002. Claude Instructions (System:Projects)
003. DSRD's | Achology Specification Documents
004. SKILL Files (Full Claude Library)
010. Intersession HANDOVER MD Files
```

Nothing was renumbered. The channel folder is untouched at `005`, and `000` including the theme is untouched.

## Your four corrections

The new value is exactly what you set out: insert `001. Project Delivery System/` before `003. DSRD's`.

| # | File | Line |
|---|---|---|
| 1 | `01. The Achology WordPress Theme/achology/harness/harness_lib.py` | 26 |
| 2 | `01. The Achology WordPress Theme/achology/page_gate.py` | 315 |
| 3 | `01. The Achology WordPress Theme/achology/page_gate.py` | 323 |
| 4 | `CLAUDE.md` at the project home root | 149 |

**Do number 1 first, before anything else in your next session.**

Your reading of it is right and it is the reason this note leads with it. `harness_lib.py` line 26 feeds hook H3, and line 221 uses `DSRD_DIR` to decide whether a write is landing inside the DSRD folder. **With that path stale, H3 does not error. It stops matching, and every write into the DSRD folder passes.** Harness Rule 8's mechanical half is off from the moment the move ran until you fix that line.

Nothing has been written into the DSRD folder in that window, and Chat is the only party that edits DSRDs in any case. But a silently disabled gate is exactly the failure class the harness exists to prevent, so it gets corrected first and proved rather than assumed.

**File the H3 acceptance printout** as you offered: attempt a write into the DSRD folder, show it blocked. Chat verifies harness installation before build work resumes, and this is that verification.

## What Chat has corrected on its side

Three files named the old path and all three are Chat's:

1. The `project-management` skill, line 140, which named the DSRD folder twice
2. The Project Instructions, section 4
3. The DSRD folder's own README

Confirmed clean, checked by search this session: `000__THE_HARNESS.md`, `000__THE_CHAT_HARNESS.md`, and every other skill file in the library. No hits.

## Why this keeps happening, and what has changed

This is the second folder move in one session and the second time a written-out path has broken. Kain ruled it into the Project Instructions today as **standing rule 24: name the folder, never the file path inside it.** A specification names a page folder and stops; the folder's own README owns what is in it.

That rule governs prose in specifications and briefs. **It does not govern code.** A script has to hold a real path, and yours legitimately do. What the rule buys is that when a folder moves, the number of places needing correction is four scripts rather than four scripts plus thirty specification sentences.

*No em or en dashes in this file; checked before writing.*
