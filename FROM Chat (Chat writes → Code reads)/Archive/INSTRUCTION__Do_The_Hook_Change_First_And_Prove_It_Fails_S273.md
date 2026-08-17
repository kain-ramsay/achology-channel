# INSTRUCTION: do the hook change first, and prove it fails

**From:** Claude Chat, Session 273. **Date:** 14 August 2026.
**Precedence:** this comes BEFORE `COMMISSION__The_Card_And_Chrome_Sweep_S273.md`. Do this first. Do not begin the component sweep until this is done and reported.

---

## Why this is first

Kain cannot verify Chat's or your compliance by reading documents; there is too much text and both of us report on ourselves. The S273 design produced a data-file record architecture, but almost all of it is honour system. **Exactly one part of it is real machinery: your existing build-versus-record hook.** Everything else waits until that is proved.

## The change

Re-point your build-versus-sheet hook so it compares a built component against `COMPONENT_DATA__{name}.json` in that component's prototype folder, instead of against a prose build sheet. Start with the one file that exists: `course-card/COMPONENT_DATA__course-card.json`, in the Card System folder.

## The proof Kain needs to see

Do not report that it works. **Make it fail on purpose, in front of him.**

1. Run the hook against the course card as the theme currently builds it. Print the result.
2. Deliberately change one value in the built card so it disagrees with the data file (a padding, a radius, a colour). Run the hook again. **It must fail, and it must print which value disagreed and what the record says it should be.**
3. Put the value back. Run it once more.

Paste all three printouts into your report, unedited. A hook that only ever passes proves nothing, which is the whole reason for step 2.

## If it cannot be done

Say so plainly and say why. That is a genuinely useful answer: it means the S273 design is wrong on its load-bearing point, and Kain has learned that in one short sitting rather than after twenty five component reviews. Do not work around it, do not approximate it, and do not report a partial pass as a pass.

## Report

Through TO Chat, one file: the three printouts, whether the hook now reads the data file, and anything the design assumed that turned out not to be true on your machine.

*No em or en dashes in this file; checked before writing.*
