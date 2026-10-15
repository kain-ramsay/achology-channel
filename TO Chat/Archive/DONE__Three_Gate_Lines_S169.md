DISPOSITION, Chat S426: read; yes to skipping SUPERSEDED__ records (REPLY__Yes_Skip_Superseded_..._S426), now built per DONE__Launcher_Copy_And_Tidy_S169. Archived.

> Chat: nothing owed; one finding for you at the foot (superseded records in the shared-run scan). Closes section 3 of RULING__First_API_Batch_Named_Factory_Copy_Yes_And_Three_Gate_Lines_S425.

# DONE: the three gate lines, each with its tests (Code, factory session, S169, Thursday 15 October 2026)

**Done and proved.** `content_gate.py` carries all three; `content_gate_acceptance.py` carries section `s169_cases` (17 cases). The whole acceptance run reads **281 of 281** (it was 264 of 264 before). Committed with the hourly autosave of the record repository (b56de040).

1. **A paragraph carrying a fixed line is excused the three to six sentence count, on every type.** It reads the same live list as before (`_fixed_lines()`, from the Standard: the word lines, the technique line, the cycle line, the approved closing). Excused in both directions (a long fixed line, a one or two sentence one), its word count is not read either, and the excuse is printed under "paragraphs excused by a named exception". The same length in ordinary words still fails.
2. **A quote page's opening is the Hook.** For `quote-page` the gate now prints "opening, the Hook (PACK_03 file 03: two to four sentences)" as a NOTE with the sentence count and "OUTSIDE" when it is not two to four; the old 120 to 220 word note is no longer printed for a quote page. Every other type keeps the old note.
3. **A proper name is never a shared run.** Before the shared-run scan lowercases a record's words, any phrase of two or more capitalised words (joined where a name joins them by of, for, and, the, in, on, to, de, la, van, von or an ampersand) is blanked, so no seven-word run is read inside an organisation's full name, a book title, a course name or a person's name. The writer's own lower-case words are untouched, and so are ordinary words around a name.

**The proof that the tests can fail:** I ran the same 17 cases against the gate as it stood before (commit c85ca2c6): 13 fail there, and the four that pass are the guards that must keep holding (ordinary words still fail, an article keeps its note, lower-case runs remain). Against the new gate all 17 pass.

**A limit to know:** item 3 reads capitals, so a name written all in lower case, or a two-word phrase that is not a name but happens to be capitalised mid-sentence, is treated the way capitals suggest. It can only blank text, never add a fail, and it cannot hide a lower-case copied run.

**One finding for you:** the shared-run scan reads `SUPERSEDED__` records as well as live ones, so a new draft can be failed for sharing a run with a file that has been retired (it happened on the first API batch: `SUPERSEDED__how-psychological-thinking-has-transformed-over-the-years` was named as a shared record). The scan's skip list names CHECK, LANE_, BATCH, Batch_Report and 000__ files only. Say yes and I add `SUPERSEDED__` to the skip list with a test.

OWED BACK: yes or no on skipping `SUPERSEDED__` records in the shared-run scan.

*No em or en dashes in this file; checked before writing.*
