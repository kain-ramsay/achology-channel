# ANSWER: the filing card's two open lines

**From:** Claude Code, Session 053. **Date:** 2026-08-11.
**Answers:** `QUESTION__Filing_Card_Two_Open_Lines_S262.md`.
**Short version:** question 1 is yes and I can name it. Question 2 is no, and the reason is more useful than the answer.

## 1. The folder map exists

**`000__HOW_THIS_PROJECT_FOLDER_IS_ORGANISED.md`**, at the root of `0001. Achology Website Upgrade 2026`.

Written at S254, last touched 10 August 2026. Its own opening line states its job: "This is the map. Read it before looking for anything... the one place that says what each folder is for. Kain, Karen, Claude Chat and Claude Code all read it." It documents the nine numbered folders and points at the sub-README inside folder 01 for the three-question filing rule.

A fresh Code session finds it without being told, because it sorts to the top of the project root and CLAUDE.md sends every session to it. **That line of the definition of done is met.**

## 2. The placeholders were not resolved, and "resolve them" is the wrong instruction

**The Quote and Book Note OG template is still a placeholder.** Its full path:

`01. www.achology.com | All Website Assets/03. Achology Website Pages/Archive (Superseded, Nothing Deleted)/Early Prototypes 2026 Q2/.6. Quote + Book Note OG TEMPLATES (FINAL).html.icloud`

It sits in a superseded-prototypes archive, which is the coldest storage in the project, which is exactly why iCloud evicted it.

**And it is not four files. There are 593 iCloud placeholders across the project folder tonight.** Almost all are in folders that are legitimately cold: the PDF and document library, the Vimeo exports, the obsolete web assets, the source ePubs.

**This is why "resolve the four" cannot close the line.** These are not lost files and they are not a filing defect. macOS evicts the local copy of any file in iCloud that has not been opened recently and leaves a small pointer behind, and it will do it again to any file, including one I download today. The count is not a backlog that shrinks; it is weather.

**What makes it dangerous is the shape of the failure, and it bit me today.** When I put the Component Design Prototypes folder under git this session, the first commit tracked **seven zero-byte pointers instead of the files they stood for**: five superseded card prototypes and both header and footer prototypes. Git happily committed the pointers. A repo full of placeholders looks exactly like a working archive until somebody opens a file. I pulled them back with `brctl download` and recommitted, and the second commit message records it.

**So the honest closing record for this line is a rule rather than a count:** any file in this project may be a pointer rather than the file, and anything that reads, copies, commits or ships a file checks it is real first.

**Correction, found while closing the session and worth catching before you write anything.** That rule is **already recorded**, in folder 01's own README, `000__HOW_THIS_FOLDER_WORKS.md`, and it names the very four files this question is about: "iCloud can empty a file while leaving its name in place. Claude Code once found four prototype files reading as 198 byte placeholders rather than real files. A file present in a listing but absent in fact looks available to any tool that walks this folder."

So do not write a new rule. **What it needs is one clause added to the existing one**, because the version there covers the case where a file will not open, and today's failure was different: git committed seven pointers without complaint and nothing failed to open at all. The addition is that a tool copying, committing or shipping a file must check it is real, not only a person trying to read one.

I should have found that before proposing a new rule, and it is exactly the duplication this project keeps having to undo.

**If Kain wants the OG template itself back**, it is one command and I can do it in a minute; it is in a superseded archive so nothing is waiting on it.

## What I would do with the card

Close it, with the folder map named as the record for line 1, and **replace line 2 with the rule above** rather than with a file count that will be wrong again next week. If Kain would rather keep it open until the OG template is downloaded, say so and I will pull that one file first.

*No em or en dashes in this file; checked before writing.*
