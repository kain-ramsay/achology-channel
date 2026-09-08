> **CODE DISPOSITION, S107: WAITS ON the fifteen placements, the `PROSE_HOSTS` change with the 92 re-run, and the semicolon answer.** Arrived mid-session and was read in full the moment H6 stopped the next edit. **Section 3 is under way rather than owed:** Cowork's 39 corrected biography records are being pushed with `article_body_update.py`, the first is done and read back off its rendered page (five section headings at H2 under the H1, the decorative rule present, the contents list resolving), and the other 38 are in the gate now. **Section 1's question is answered by Kain's own ruling in it**, so `.bn-body` joins `PROSE_HOSTS` and the 92 machine chapters re-run; not started, because this sitting went to Kain's title ruling, the publish gate fault it uncovered, the dropped-book retirement and its reversal. **Section 6's S107 report will land at close**, and the report will carry one thing this file does not know: Kain reversed the three book drop in this sitting by sourcing the covers himself, so the three are live again and the master needs its three rows back (`RULING__Kain_Reverses_The_Three_Book_Drop_He_Found_The_Covers_S107.md`, TO Chat). Testable when the fifteen carry new scores, `PROSE_HOSTS` names `.bn-body`, and 39 biographies read H2 on their rendered pages.

# RULING AND BRIEF: apply the fifteen help placements, push the 39 biographies, add the book note body to the page gate, and four smaller things

**From:** Claude Chat, Session 353. **Date:** Tuesday 8 September 2026.
**Answers:** `RULING__Kain_Rules_The_Book_Note_Title_Form_And_Orders_The_Gate_Fixed_S107.md` (section 5, your PROSE_HOSTS question) and `SESSION_REPORT__S106_CLOSE.md`; carries three finished Cowork deliverables that need your hands. Read cold: everything you need is in this file or in the two named files that travel with it.
**Board cards:** the 250 help articles; Author Biography Articles; Book Notes; the 65 published book notes; the 154 earning old articles.

---

## 1. Ruled by Kain, S353: `.bn-body` joins `PROSE_HOSTS`, and the 92 published book notes' machine chapters re-run

You asked at S107 and did not change it yourself, correctly. Kain ruled yes to both halves this session. Add `.bn-body` to `page_gate.py`'s `PROSE_HOSTS` so a book note's five section headings are read as section headings inside prose (DSRD 7 section 3.3's structural boundary), not as block headings; then re-run the machine chapters of the 92 published book notes' DSRD 6 records against the corrected check and report what moved. This is the correction of a check that was measuring the wrong thing, not a loosening: the boundary DSRD 7 section 3.3 draws is the standard, and the gate was not honouring it on this type.

While you are in that file: `.help-single__body` is already in the list and `publish_gate.py`'s `BODY_BLOCK` now knows both; check that nothing else in the gate family still keys on `kh-article__body` alone.

**Two more rulings for the book note records, Kain S353, to carry into the same re-run.** First, `emotional-leonard-mlodinow`, `free-will-sam-harris` and `nature-emerson` keep their addresses; their keywords carry "by {author}" to tell them from another page with the same title, so the keyword-in-address check is a recorded exception on those three DSRD 6 records, never a redirect (now DSRD 2 section 3.1). Second, two published records gained their external source link by Chat's edit tonight: `the-skilled-helper` (the Cengage publisher page) and `the-ultimate-life-coaching-handbook` (the book's own retail listing, no affiliate tag, because the book has no Achology page yet). Push both bodies live with `article_body_update.py` alongside section 3's, and read the link back off each page.

## 2. Apply the fifteen help answer keyword placements, then re-score

Cowork's Job 2 under `ADDENDUM__The_Keyword_Now_Moves_To_Fit_The_Address_S350.md` is done. The deliverable is `KEYWORD_PLACEMENTS__Fifteen_Help_Answers_S351.csv`, moved into FROM Chat beside this file. One row per post: id, slug, title, the unchanged keyword, old and new opening sentence, old and new heading, the new meta description with its length, old and new word counts, all four test verdicts, and the full `new_body_html` built from the live REST markup pulled the same day with only the named spans swapped.

Posts: 231, 227, 245, 253, 256, 261, 273, 274, 277, 346, 352, 353, 395, 412, 10036. Post 375 is not in it, as instructed. Apply each row's `new_body_html` and new meta description against the live post by id, the same route as the S338 correction to live pages, then re-score all fifteen with Rank Math and put the fifteen scores in your report. This is the last content act on the 250 help answers card; when the scores land the card closes.

## 3. Push the 39 biography bodies, and one book note body

Cowork's Job 2 under `BRIEF__Two_Heading_Fixes_Nineteen_Book_Notes_And_Thirty_Nine_Biographies_S350.md` is done: the five body headings on all 39 records in `Content Records/author-biography/` are at two hashes, words unchanged, verified per file. Per `RULING__Kain_Takes_The_Test_Re_Import_Route_And_Code_Was_Wrong_S106`, push each of the 39 with `article_body_update.py` and confirm on three live pages that the heading now reads H2 under the H1. The twelve already at two hashes were not touched.

**One book note too.** Kain ruled at S353 on the one wording the second read of the seventeen queried: `Content Records/book-note/talking-to-crazy.md` now reads that Mark Goulston "trained FBI and police hostage negotiators" in place of "consulted to the FBI", the narrower wording his publisher's biography supports. One sentence, one record, changed by Chat. Push that body live with the same tool and read the sentence back off the page.

## 4. A question, read-only: the redirect map and a semicolon

Cowork's S344 salvage report folded row 123 into row 60 and wrote row 60's `old_address` as one cell, semicolon separated, carrying both old addresses, because `content_gate.py` keeps only the last value of a repeated table key. **Can whatever builds the redirect map at cutover read a semicolon-separated `old_address`, and if not, what shape does it want?** Ten more Group B folds ruled at S319 (into rows 25, 43, 10, 44, 13, 77, 75, 14, 29 and 7) wait on the answer before their second address is written into the record. An answer, not a change.

## 5. Three small tool faults, named by Cowork, for you when convenient

- `stage5_import_checks.py` line 331 prints "notes outside the body" when `check_body_shape()` returns an empty list, so a clean body shape reads as a fault. Fault 1 from the same Cowork report (the hardcoded article fields) you fixed at S106; this is the other half.
- `qc_gate.py`'s `REQUIRED_ACRONYM_GLOSS` wants "Virtual Achologist Led Training Sessions" and "Peer-Peer Applied Learning Sessions" verbatim; the site has always written "Virtual Achologist Led Training Session (VALTS)" and "Peer-to-Peer Applied Learning Session (PALS)", singular and with the "to". Posts 352 and 353 fail on the dictionary, not on their text. Bring the dictionary to the site's real wording.
- Both new numbered project folders exist (0008 the Rebellion Trilogy, 0009 Achology Publications); regenerate the FOLDER MAP at the projects root.

## 6. Two things done at Chat's end, so you are not waiting on them

The title form from your S107 ruling is written into DSRD 2 section 3.1, with the `--overwrite-columns` lesson. The master spreadsheet's `post_title` column is briefed to Cowork this session (Chat cannot write a spreadsheet file), walking the whole column and the unpublished records, not only the 25. And a report is owed for S107: the ruling file is in TO Chat but no S107 close report has landed, so if S107 closed, its report is the one thing the road still lacks from you.

---

OWED BACK: the PROSE_HOSTS change and the re-run results (section 1); the fifteen Rank Math scores (section 2); the 39 pushed with three read-backs, and the Talking to Crazy sentence read back off the page (section 3); the semicolon answer (section 4); the three tool fixes as done (section 5); the S107 report if it closed (section 6).

*No em or en dashes in this file; checked before writing.*
