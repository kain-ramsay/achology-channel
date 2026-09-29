**Needs from Chat:** two things before the next workbook that is not the Karpman one: (1) the school of each course a workbook can accompany, so the logo colour can be chosen (only the CBT Practitioner course's school is confirmed); (2) whether a second workbook layout is wanted, since the tool refuses any record whose parts do not fit the Karpman layout.

# REPORT: the workbook build tool has a permanent home

**From:** Claude Code, S140 (factory), Tuesday 29 September 2026. **To:** Claude Chat.
**Answers:** the S139 carry-over "give the workbook tools a permanent home".

- **One tool, `build_workbook.py`, in a new folder `04. Workbook Build Tool` of the Educational Publishing System project,** with its own README. It joins the two S139 scripts and takes the workbook record as its input. Every S139 ruling (the rotation, both logos, the white panel, no one-word last line, typed text on the printed lines, the locked but fillable PDF, the homepage links) is written in the code beside the line that keeps it.
- **Proved by rebuilding the Karpman workbook:** the render is byte for byte the file Kain approved at S139 (`RENDER__The_Karpman_Workbook_S139.html`); the PDF is the same size with nine pages, nine fields and the same three links; all checks held. With the last-line fix switched off the check names the same six lines as at S139.
- **Not decided here, and carried as open:** Safari's PDF viewer ignores the writing boxes' character limit, so typed text can run past a space there (Kain's find at the S139 close). The next step is to test Safari, Preview and Acrobat Reader and settle one method for Kain to see before it becomes the standard. The tool keeps the approved S139 behaviour until then.
- **The folder map generator was not run:** its root is the website project and it does not cover the Educational Publishing System. The parent folder's README carries a hand-written line for the new folder.

OWED BACK: the two answers above.

*No em or en dashes in this file; checked before writing.*
