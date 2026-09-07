# DONE: Evernote exports inventoried; articles counted and viewed, quotes counted and quality-checked

**From:** Claude Cowork. **Date:** 7 September 2026, same session as the brief.
**Follows:** BRIEF__Inventory_The_Evernote_Exports_Articles_And_Quotes_S348.md (also in this folder).
**Governed by:** 000__COWORK_PRODUCTION_HARNESS.md. Job type: measurement. Nothing was drafted, corrected, or gated.

## 1. The summary, pasted whole

```
# Evernote salvage inventory, summary

Records read from Content Records: 402
Old site URLs read: 2061
Master workbook: checked

## Notes per notebook
- 1. Psychology: 53 notes
- 2. Wisdom for Life: 51 notes
- 3. Personal Growth: 53 notes
- 4. Mental Wellness: 51 notes
- 5. General Interest: 62 notes
- 6. Helping People: 48 notes
- 7. Motivation: 53 notes
- Q1. Quotes by Person (A-Z): 129 notes, quote lines found: 2448
- Q2. Quotes by Topic (A-Z): 110 notes, quote lines found: 6174

## Article verdicts
- candidate: never on the old site, no record: 295
- covered: a record exists: 40
- candidate: was on the old site, no record: 36

Total article notes: 371
Total quote lines: 8622
Distinct people in Q1: 128
Distinct topics in Q2: 109

Every input was read only. Nothing was written outside the inventory folder.
```

Step 2 did not apply. The summary line read "Master workbook: checked" on the first run; openpyxl is already installed on Kain's Mac, so no install was needed.

## 2. Article candidates, by view

331 rows carried a candidate verdict. Every one now carries a `cowork_view` value and a short `cowork_note`, written into `INVENTORY__Evernote_Articles.csv` in place, in the same inventory folder.

- **Worth rewriting: 271.** Real, on-brand, recognisable psychology, philosophy, and personal-development titles with no site coverage found. This is the raw material.
- **Not worth it: 53.** Two kinds, both named in each row's `cowork_note`. Six are Evernote's own folder-index notes, titles like "All Psychology Books" and "50 Wisdom for Life Books", which are lists, not books or articles. The other 47 are duplicates within the Evernote export itself: the same book filed into two or three different topic notebooks, or the same book with a slightly different subtitle, author-name spelling, or a stray Evernote annotation on the title. Kain's own library carries the same book more than once by nature of cross-filing into several categories (Mindset, for one example, sits in Psychology, Personal Growth, and Motivation, all three candidates before this pass). Where a book appears more than once, one instance is marked worth rewriting, or already covered where that applies, and the rest are marked not worth it, so nothing gets counted, or rewritten, twice.
- **Already covered under another title: 7.** Five distinct books, all missed by the script's exact-title match. The Road Less Traveled by M. Scott Peck (the site's book note spells it "Travelled"). Civilisation and Its Discontents by Freud (the site's record uses the American spelling, "Civilization"). Cognitive Behavior Therapy by Judith Beck (the Evernote note specifies "Second Edition"; the record's title does not carry it). The Time Paradox by Zimbardo (the Evernote note carries the book's full subtitle and spells "Phillip" with two Ls; the record's title field is the bare title with one L). And Atomic Habits by James Clear, which is two rows here because Kain's export holds it twice under two slightly different subtitles, both pointing at the same already-started record. That last one is worth flagging on its own: `book-note/atomic-habits-clear.md` exists, but its `post_status` is `draft`, not `publish`, so it is started, not finished, and not live yet.

**Why the script missed these, in one line, for whoever tightens it:** `find_record` only tests for an exact match on the normalised full note title, subtitle included. A record indexed only under its bare book title, with no subtitle stored in any of its fields, will never match a note whose title carries a subtitle, however close the two strings otherwise are. Every miss above is that same gap, not five separate problems.

## 3. The quotes, one paragraph

8,622 quote lines, 128 distinct people in Q1, 109 distinct topics in Q2, and both distinct counts hold even after stripping Kain's own workflow tags out of the person or topic field, so they are not inflated. The extraction itself is clean: 222 rows, 2.6% of the total, are not real quotes. 217 of those are the note's own "TAGS: ..." or "COURSE: ..." lines, swept up because the script's skip list catches "keywords:" and "meta description" but not "tags:" or "course:", and both open a line in nearly every Q2 note. The other 5 are proper names, not quotes, all from one note, "# Great Thinkers A-Z" in Q1, which is a list of thinkers rather than a set of quotations. Outside those 222, a further 22 rows have no attribution captured but are genuine quote text; most of those are quotes whose attribution sits after a closing curly quote the pattern does not match, plus one lone orphaned fragment, "- Dita Von Teese.", whose quote was on a separate line the parser did not rejoin. Worth naming separately, and not a fault in the script: about seven rows in ten, 6,293 of 8,622, carry one of Kain's own Evernote workflow annotations in the person or topic field, things like "(Done)" or "(Done - needs uploaded)". Nothing surprised me more than how clean the underlying quote text is under all of that; the field is just not fit to show or export as-is and wants that suffix stripped before it goes into anything a reader sees or a batch job runs from.

## 4. No script error

None. The script ran clean on the first pass, wrote all three files, and finished in under seven seconds.

## What I did beyond the brief's literal ask, named so it can be overturned

Step 3 asked for one column, `cowork_view`. I added a second, `cowork_note`, a short reason on every row I did not mark worth rewriting, so the already-covered and duplicate calls are checkable without re-deriving them by hand. Nothing was drafted, corrected, or gated to produce it; it is commentary on the same inventory file the brief already named as the output.

OWED BACK: nothing; this file is itself what was owed.

*No em or en dashes in this file; checked before writing.*
