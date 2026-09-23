> **CODE DISPOSITION, S131: DONE.** Voice checks widened, quote pages and help answers added, the 38 marked s130, acceptance 125 of 125, re-run hit list filed in `SHIP__Voice_Checks_Widened_S131.md`.

# BRIEF: widen the voice checks so the gate catches "about a piece of writing" on every article type that needs it

**From:** Claude Chat, S380, Wednesday 23 September 2026. **To:** Claude Code.
**Approved by Kain in session, S380:** "Yes, please do."
**Built on:** your `ANSWER__The_Voice_Checks_By_Type_S131.md` (TO Chat), which this brief answers.
**Board card:** Search and citation layer for every EPS page.

## Why

Kain's rule (S379): an Achology article is never about a piece of writing, and never about itself. He does not want it to rest on a writer reading a skill carefully. house-copy-standards now shows good and bad openings (S380); this brief is the half that holds without anyone reading anything. Your S131 search found 58 live records breaking the rule; Cowork is fixing them now.

## The work

1. **Widen the self-description phrases** in "no paragraph describing the article". Add: `This post`, `In this post`, `What follows`, `It closes with` (if not already caught), and the lower-case forms `this piece`, `this article`, `this post` anywhere in a body paragraph. Leave out `By the end` and `Along the way`; your S131 search showed them in honest sentences.
2. **Add quote pages to the voice checks**, with two lines only: "no paragraph describing the article", and "source person narrated". For the named person, read the quote's own author field (the quoted person), since quote pages carry no `reviewed_by`. The standard source line naming the lecture must still pass. No opening line, no first-heading line, no meta line for this type.
3. **Add help answers to the voice checks**, with one line only: "no paragraph describing the article".
4. **Mark the 38 rewritten instructor articles `voice_standard: s130`** in their records, so their published pages are checked strictly from now on. The 58 Cowork is fixing get the same mark later, on Chat's word once her work is checked.
5. **Book notes, author biographies, workbooks and workbook landing pages stay out.** A book note describing its book's author is that type's job.

## Done when

- Acceptance cases cover each new phrase, both new types, the quote page's source line passing, and a book note not being checked. `content_gate_acceptance.py` passes in full.
- A read-only re-run over every live record of the covered types reports its hits, so the new lines' reach is known. Change no page.
- One SHIP in TO Chat: what changed, the case count, and the hit list from the re-run (it should match the 58 Cowork is fixing, plus anything new).

## Not this brief

No live page is edited. The 58 are Cowork's; their pushes come to you separately.

*No em or en dashes in this file; checked before writing.*
