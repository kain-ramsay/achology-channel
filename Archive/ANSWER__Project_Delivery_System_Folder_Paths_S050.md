# ANSWER: yes, four references, and one of them is a safety mechanism

**From:** Claude Code, S050. **Date:** 2026-08-07.
**Answers:** `QUESTION__Project_Delivery_System_Folder_Consolidation_S252.md`.

## The short answer

**Yes. Four live references, all to `003. DSRD's | Achology Specification Documents`. None to the other four folders.**

`004. SKILL Files`, `010. Intersession HANDOVER MD Files`, `001. Achology PRD` and `002. Claude Instructions` are referenced by nothing I own or run. Those four can move with no coordination at all.

**The DSRD folder cannot.** Correct these four in the same pass as the move.

## The four, exact file and exact string

| # | File | Line | The exact string | What breaks |
|---|---|---|---|---|
| 1 | `01. The Achology WordPress Theme/achology/harness/harness_lib.py` | 26 | `DSRD_DIR = os.path.join(UPGRADE, "003. DSRD's \| Achology Specification Documents")` | **Hook H3 stops protecting the DSRDs.** See below. |
| 2 | `01. The Achology WordPress Theme/achology/page_gate.py` | 315 | `/ "003. DSRD's \| Achology Specification Documents"` | `planned_urls()` cannot read DSRD 1, so every planned-but-unbuilt URL is reported as a broken link instead of NOT-BUILT |
| 3 | `01. The Achology WordPress Theme/achology/page_gate.py` | 323 | `/ "003. DSRD's \| Achology Specification Documents"` | The boundary-owner check cannot read DSRD 8's component list |
| 4 | `CLAUDE.md`, at the project home root | 149 | `Claude Code (Projects)/Achology Website Upgrade 2026/003. DSRD's \| Achology Specification Documents/` | The standing instruction naming the canonical DSRD home points at nothing |

**New value for all four:** insert `001. Project Delivery System/` before `003. DSRD's`.

A note on 2 and 3: `page_gate.py` builds the path from `pathlib.Path(__file__).resolve().parents[3]`, which resolves to `Achology Website Upgrade 2026`. That half still works after the move. Only the segment following it changes.

## The one that is not merely a broken read

**`harness_lib.py` line 26 feeds hook H3, forbidden ground.** Line 221 uses `DSRD_DIR` to decide whether a write is landing inside the DSRD folder, and H3 blocks it if so. That hook is the mechanical half of Harness Rule 8, "Code never edits a DSRD".

If that path goes stale, **H3 does not error. It stops matching, and every write into the DSRD folder is allowed through.** A gate that fails loudly is a nuisance. A gate that fails silently is worse than no gate, because everyone goes on believing the protection is there. This is the reference to correct first.

I will re-run H3's acceptance test after the move (attempt a write into the DSRD folder, show it blocked) and file the printout, rather than assume a corrected string works.

## What I checked, so you can judge the answer's reach

`grep -rn` for all five folder names, at any depth, across: the whole theme including all seven harness hooks and the three gate scripts, the project-home `CLAUDE.md`, and every `.py`, `.php`, `.css`, `.js`, `.json` and `.sh` file in `Achology Website Upgrade 2026`. Four hits, all above, none elsewhere. That is the complete result, not a sample.

## What I have not done

Nothing was moved, renamed or edited in response to this, as the question asked. The four corrections wait on your word that the move has run.

*No em or en dashes in this file; checked before writing.*
