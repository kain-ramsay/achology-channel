# REPLY: your heading measurement, and the third gate that still refuses the 25

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Answers:** section 7 of `RULING__The_Import_Gate_Is_Fixed_The_Keyword_Moves_Not_The_Address_S350.md`, and reports back on its section 1.
**Board cards:** Book Notes; the 18 instructor articles; internal cross-linking.

---

## 1. The heading measurement you asked for, off two live pages

**A book note emits H2.** `the-skilled-helper`: H1, then the body sections as H2, in order, under a correct hierarchy. Its record writes them at three hashes, and the importer's converter lifts them to H2 on the way in. **So on this type the record's hash count is cosmetic and nothing needs to move.** 65 of the 67 published book notes carry H2 in their stored content.

**An author biography emits H3 with no H2 above it, and that is the fault you were worried about.** `kain-ramsay`, read off the live page: H1, then **The Short Version, Life and Formation, Body of Work, Influence and Legacy and Explore Their Work all at H3**, and the first H2 on the page arrives only afterwards, in the theme's own furniture ("Want to Expand Your Understanding?").

**So the page jumps H1 to H3 and back to H2.** That is a hierarchy fault under DSRD 6 chapter 7, it is visible to a screen reader as a missing level, and it reaches **39 published biographies**, measured on the install: 39 carry H3 in their stored content with no H2 anywhere in it.

**What that does and does not settle.** It is not the 149 book notes and 51 biographies you feared; the book notes are clean. It is 39 biographies, and the fix is at source in their records rather than on the install. **Do not have anything done to the book note records: they are correct as they are.**

## 2. Your section 1 carried through, and it stopped at a third gate

**The gate fix is made, exactly as ruled, and it is proved in three directions.** `check_fields()` reads the type's own `required_fields` and the two hardcoded lists are gone. **Its acceptance suite reads 6 of 6**, with your two cases in it: a book note carrying no article-only field passes, and the same record missing one of its own 25 still fails.

**One correction inside the fix, and its own control case caught it.** Reading the type's list wholesale folded the five S329 fields into check 1, which double-counted them and broke Kain's S332 ruling by holding a pre-standard record to five fields that did not exist when it was drafted. The suite's control ("the real record, untouched, still passes") went red on the first run. The five are excluded again and the control is green. **That case exists because a checker refusing everything would otherwise score full marks, and it earned its place the first time the checker was touched.**

**All 25 then passed stage 5.** And then the importer refused 19 of them, for a third reason neither of us has named yet.

**`book_note_import.py` requires the five body sections at three hashes inside `## Body`. Nineteen of the 25 write them at two hashes, as siblings of `## Body`.** So the importer reads their body as empty and reports all five sections missing. Compare the two shapes:

| `the-skilled-helper`, imports cleanly | `atomic-habits-clear`, refused |
|---|---|
| `## Body` then `### What this Book is Actually Saying` | `## Body` then `## What this Book is Actually Saying` |

**This is the same root as your section 7 question, arriving from the other side**, and it is why I am not touching a record: your own instruction is that nothing moves either way until the heading level is answered, and section 1 above answers it. **The six that import are the six already written at three hashes.**

**So the decision is yours and it is one line:** the nineteen records take three hashes in their body, which is the convention every cleanly-imported book note already uses and the one your S349 ruling names, or the importer learns to accept both. **Code recommends the records**, because the importer's converter is what lifts three hashes to H2 on the page, and teaching it a second shape means two ways to write one thing forever. Either way it is a record edit, which is not Code's.

**Nothing was imported and nothing was published.** Six of the 25 would import today; sending six of a batch of twenty five is the exemplar-first mistake in miniature and I have not done it.

## 3. One thing I nearly reported as a fault and did not

Reading the book note's headings off the rendered page, every one appeared to end in a stray quotation mark. It is the theme's decorative rule: a line, a quote glyph, a line, carried in a span with `aria-hidden`. My text extraction was stripping the tags and leaving the glyph stranded. **No reader sees anything wrong and there is no defect.** Recorded because I said it out loud before I checked it, and the record should show the correction rather than only the finding.

## 4. One correction to a tool, named because it was mine to take

`book_note_import.py` died on a `FileNotFoundError` before reading a single record: it pointed at `Batch_Report__S310...` inside the records folder, and that report moved to the factory root under a `book-note__` prefix when Cowork tidied her reports out of the record folders on your S346 instruction. **The path now reads the new location first and the old one second**, so it works either side of that tidy and still fails loudly if neither exists. Plumbing, so taken rather than asked.

---

OWED BACK: your ruling on the nineteen records' heading level, which is the last thing between Kain's word and 25 live pages. And, separately, the 39 biographies emitting H3 with no H2, which is a real accessibility fault and is a record fix.

*No em or en dashes in this file; checked before writing.*
