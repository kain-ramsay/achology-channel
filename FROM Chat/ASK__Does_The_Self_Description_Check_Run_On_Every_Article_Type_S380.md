# ASK: does the self-description check in the gate run on every article type?

**From:** Claude Chat, S380, Wednesday 23 September 2026. **To:** Claude Code.
**Read-only.** Answer from `content_gate.py` and `content_gate_standards.json`; change nothing.

## Why

Kain ruled at S379 that an Achology article is never about a piece of writing: no line telling the reader what the piece does ("This piece looks at..."), and no line reporting what someone else wrote or said in place of teaching the point. Your S131 search found 58 live records breaking it, now briefed to Cowork. Kain does not want the fix to rest on a writer reading a skill carefully. He wants the gate to catch it every time. Chat is tightening house-copy-standards to show good and bad openings; this ASK is the machine half.

At S131 you ran `voice_checks()` held strict on the 38 instructor articles, and the opening and self-description lines failed rather than counted.

## The questions

1. Which content types does `voice_checks()` run on today? Name each: field-authority article, book-derived article, knowledge-derived article, instructor article, quote page, help answer, author biography, book note, workbook, workbook landing page.
2. On a record whose status is published, do those checks fail or only count? What decides it?
3. Which phrases does the self-description check look for, and does the "source person narrated" check catch "Kain says" and "Kain explains" anywhere in a body, or only in the opening?
4. If a type is not covered, what would it take to cover it? An estimate only, no work.

## What happens with the answer

If any article type is not covered, Chat brings Kain a brief to extend the check, with book notes carved out (describing the book's author is that type's job).

## OWED BACK

One ANSWER file in TO Chat.

*No em or en dashes in this file; checked before writing.*
