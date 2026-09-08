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

## 5. Addendum, 8 September 2026: the re-run, three counts, and the S318 check

Kain asked for three follow-ups once Chat had tightened the script for the leaks named in section 3. All three below, plus what changed on the re-run itself.

**The re-run.** `evernote_inventory.py` ran clean a second time, six seconds, no error, and it now keeps the `cowork_view` and `cowork_note` columns exactly as written. The quotes fix worked precisely: all 217 TAGS:/COURSE: rows are gone from `INVENTORY__Evernote_Quotes.csv`, and nothing else was removed with them (8,622 rows down to 8,404, and I checked the difference row by row, not just the count). The "# Great Thinkers A-Z" name list is untouched, still five rows, still five names sitting where quotes should be. That half of what I flagged is still open.

Sixteen article rows changed verdict. Twelve moved from candidate to covered, matching the summary's covered count going from 40 to 52. Eleven of those twelve are genuine: the matching was tightened to catch subtitle and edition differences, and it now also finds Authentic Happiness (Seligman), Emotional Intelligence (Goleman), The Power of Now (Tolle), and Boundaries (Cloud and Townsend) as already covered, on top of the five books I had flagged by hand (Road Less Traveled/Travelled, Civilisation and Its Discontents, Cognitive Behavior Therapy Second Edition, The Time Paradox, and both Atomic Habits rows, all confirmed again on this run). I have not changed any `cowork_view` value to match; the four newly-caught ones still read worth rewriting in the CSV, because updating the column wasn't asked for this round. Recommend reading those four as covered before anyone drafts them, and say the word if you want me to update the column itself.

The twelfth flip is wrong, and it is the one worth catching before anyone trusts it. "The Social Animal: The Hidden Sources of Love, Character, and Achievement" by David Brooks now shows as covered, matched to `book-note/the-social-animal-aronson.md`. I read that record in full: it is Elliot Aronson's 1972 book, and its own text states plainly that it is "not the David Brooks book of the same name," because the record exists partly to tell searchers the two are different books. It names Brooks specifically in order to rule him out. Whatever the tightened matching checks now, it reads as though it is scanning into the record's body text as well as its Page Fields table, and a record that discusses a rival title in order to disambiguate from it now looks, to that kind of check, like it covers it. Brooks's book is not on the site. My original call stands: worth rewriting, not covered.

The other four changed rows are not coverage changes. The three "Mindset: The New Psychology of Success" rows and the one "Mindset: The Psychology of Success" row (a different, shorter title, same author) all moved from "never on the old site" to "was on the old site, no record". All four stay candidates, all four keep the `cowork_view` I gave them before, nothing to act on there.

**Count one.** Of the 271 rows I marked worth rewriting: 263 read yes in `in_master_workbook`, 8 read no. Five of those 271 have since flipped to covered on the re-run, as above; I have counted all 271 as originally marked, since that is what was asked.

**Count two.** Of the quote lines that are real quotes, the 8,399 rows left once the five-row name list is set aside: 8,323 read yes in `in_master_workbook`, 76 read no.

Worth flagging plainly on both counts rather than passed over: yes outnumbers no by more than thirty to one on the first and more than a hundred to one on the second. Either the master workbook is genuinely close to comprehensive for what sits in Kain's Evernote library, or the workbook check is looser than the name suggests, since it tests every cell in the sheet rather than one books-and-quotes column, and a short common phrase could hit something unrelated. I have not checked which of those it is. Flagging the pattern rather than trusting the number without saying so.

**BRIEF__Fix_The_Seventeen_Substantive_Book_Note_Failures_S318: still open.** I checked all seventeen named records against the exact fault text the S310 re-verification wrote into each one, not just file dates. All seventeen still carry their original "S310 re-verification (non-drafting agent): FAILED, awaiting escalation" paragraph, word for word, with the specific fault it named still sitting there uncorrected: born-for-love, on-the-tranquility-of-mind, originals, the-origins-of-intelligence-in-children, come-together, have-a-little-faith, identity-youth-and-crisis, resilient, talking-to-crazy, the-quick-and-easy-way-to-effective-speaking, critique-of-practical-reason, meditations-for-mortals, mothers-who-cant-love, multiple-intelligences-new-horizons, shyness-what-it-is-what-to-do-about-it, the-beck-diet-solution, and yes-50-scientifically-proven-ways-to-be-persuasive. None has been redrafted. There is no batch report and no pointer file for this brief in FROM Cowork, its Archive, or TO Cowork's Archive. The brief's own preamble explains why: as of S321 it was waiting on Kain's order ruling, behind what it calls the Salvage run, named there as the Content Production Factory's first job. I checked the brief's status, not what unblocks it, so whether the Salvage run itself is finished is a separate question I have not answered here.

OWED BACK: nothing; this file is itself what was owed.

*No em or en dashes in this file; checked before writing.*

## 6. Addendum 2, 8 September 2026: the four rows updated

Kain confirmed. The four rows flagged in Addendum 1 above (Authentic Happiness by Seligman, Emotional Intelligence by Goleman in the "1. Psychology" notebook, The Power of Now by Tolle in the "2. Wisdom for Life" notebook, and Boundaries by Cloud) now read cowork_view = already covered under another title in INVENTORY__Evernote_Articles.csv, each carrying a cowork_note naming its matched record and the reason: the tightened S348 re-run caught it as covered, and cowork_view was synced to match on Kain's instruction. The duplicate rows carrying the same titles in other notebooks (the "3. Personal Growth" copies of Emotional Intelligence and The Power of Now) were left alone; they already read cowork_view = not worth it as duplicates and stay that way.

Tally after the change: worth rewriting 267, not worth it 53, already covered under another title 11, blank (covered, not a candidate) 40. That totals 371, the full set of article notes.

OWED BACK: nothing.
