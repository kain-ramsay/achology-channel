# REPORT: every old folder number found, and the three that were breaking things

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Answers:** `BRIEF__Folders_Renumbered_S254_Find_Every_Old_Path.md`.
**Searched:** every `.py`, `.php`, `.js`, `.css`, `.json`, `.sh`, `.txt` and
`.md` in the project, plus `~/.claude/achology_hook.py`, `~/.claude/settings.json`
and the project `CLAUDE.md` outside it. All thirteen strings, plus
`02. Page + Components`.

## 1. Live code: three stale paths, all mine, all fixed, and one of them mattered

**`harness/harness_lib.py`**

| Line | Held | Consequence |
|---|---|---|
| 83 to 87 | `DSRD_DIR` built from `001. Project Delivery System` and `003. DSRD's ...` | **H3's folder arm stopped matching** |
| 93 to 95 | `THEME` built from `000. www.achology.com \| All Website Assets` | pointed at nothing |

**What the stale `DSRD_DIR` actually cost, measured rather than assumed.** H3 has
two arms and only one went stale:

```
a file named like a DSRD        stale path: blocked   fixed path: blocked
a file NOT named like a DSRD    stale path: ALLOWED   fixed path: blocked
```

So a write into the DSRD folder was still caught if its filename looked like a
DSRD, by the mirror arm, which reads the name. A write into that same folder
under any other filename went through. Rule 8's mechanical half was holding by
its second arm only, and nothing said so.

I said in session that H3 was down. That was too strong and the guard above
corrected it: half of it was, and the half that was down is the half that reads
the path.

**`page_gate.py`**, lines 313 to 331: `DSRD1` and `DSRD8` reached through the
same two numbers. Worse than the path, and this is the part worth recording:
`planned_urls()` and `component_classes()` each returned an **empty set** when
the file was missing. The gate would have gone on printing PASS with its
specification gone, and the links-resolve check would have called every planned
but unbuilt address a broken link. Both now stop the run and name the document
they cannot find.

**The fix, in one sentence:** both files now find a folder by the end of its
name, because the number at the front is the only part that ever moves. Same
approach as `_find_channel`, same refusal to fall back.

**Acceptance printout, the real hook against a real event:**

```
DSRD_DIR   exists=True  .../02. Project Delivery System/03. DSRD's | ...
THEME      exists=True  .../01. The Achology WordPress Theme/achology
CHANNEL    exists=True  .../03. Notes for Claude Chat (from Claude Code)

H3 against a real DSRD path       exit 2   blocked, correct
H3 against a path outside it      exit 0   allowed, correct
GUARD: the pre-fix path lets the second case through, so the test can go red
```

`page_gate` re-run afterwards on `/policies/cookie-policy/`: 28 passed, 0 failed,
with DSRD 1's planned-url list present.

Commit `fbda1cf`. **Third rename in three sessions to break a written path, and
the first one caught on purpose rather than by accident.** The brief was right
to ask.

## 2. Live documents, yours to fix. Twelve hits across nine files

**`02. Project Delivery System/03. DSRD's .../README.md`**
- line 3: "This folder sits inside `001. Project Delivery System`"
- line 49: "This folder now sits inside `001. Project Delivery System`"

**DSRD 1**, line 575: the Redirect Master's row source, `007. Spreadsheets | Data | CSV Files/Redirect Map | Master File/...`

**DSRD 2**
- line 263: the Book Note reference page, `000. www.achology.com | All Website Assets/03. Achology Website Pages/`
- line 955: the Book Note Master, `006. Content Production Factory + COWORK/...`
- line 957: the books and quotes workbook, `006. Content Production Factory + COWORK/...`
- line 1043: "the root of the 006. Content Production Factory folder"

**DSRD 9**, line 1512: the Book Note page folder, `000. www.achology.com | All Website Assets/03. Achology Website Pages/`

**DSRD 10**, line 64: "Every DSRD lives in *003. DSRD's | Achology Specification Documents*"

**`01. www.achology.com .../000__HOW_THIS_FOLDER_WORKS.md`**, lines 15, 26, 84 and 103: `007. Spreadsheets`, the folder's own name as `000.`, and `011. Achology Documents + PDF Resources`

**`04. Content Production Factory + COWORK/000__COWORK_PRODUCTION_HARNESS.md`**, line 127: "the root of the 006. Content Production Factory folder"

**Also carrying old numbers, not line-listed here because they are yours to
sweep whole:** `Achology Project Instructions.md`, `page-design-brief-SKILL.md`,
`project-management-SKILL.md`, the channel's own READ ME FIRST note for Chat,
and the Code of Ethics page's `README__Where This Page's Images Live.md`.

(That READ ME FIRST filename carries an em dash, so it is described rather than
quoted here: the gate refuses the character even inside a filename, which is
correct and worth knowing before you go looking for the exact string.)

## 3. `CLAUDE.md`, which is Kain's and not mine to edit

Four hits, and they matter because this file loads at every session open:

- line 8: the harness at the root of `005. Notes for Claude Chat (from Claude Code)/`
- line 42: the FROM Chat folder under the same `005.`
- lines 154 to 155: the DSRD folder as `003. ...` inside `001. Project Delivery System`

Worth noting against its own standing rule 24, which that file states: folders
are named, never spelled as routes. These four are the exception it warns about.

## 4. Archive and handover files: 60 files, deliberately not listed

Every remaining hit is in an `Archive/` folder or an intersession handover.
They are historical records of what was true when written, and correcting them
would falsify the record. Flagging the count only.

Two archived scripts hold the old DSRD path and are not fixed for the same
reason, neither being on any live path:
`03. Notes for Claude Chat .../Archive/register.py` line 31 and
`.../Archive/linkmap_pass.py` line 50.

## 5. Clean

`~/.claude/achology_hook.py`: no hits. It finds the harness by marker, exactly
as commissioned at S252, and survived this renumbering untouched.
`~/.claude/settings.json`: no hits.
Nothing anywhere points at `02. Page + Components (HTML Design Files)`.

## 6. One thing I did that the brief did not ask for

I fixed `harness/README.md` line 4, which named the channel by its old number.
It is my document, it is one line, and the brief says my own files are mine.
Flagging it rather than leaving it unsaid.

*No em or en dashes in this file; checked before writing.*
