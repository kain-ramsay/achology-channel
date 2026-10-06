> **CHAT DISPOSITION, S404: ARCHIVED, done. Kain ruled 5.1 and 5.2 as named exceptions (n) and (o), 5.3 no subject field, and signed Standard Version 7 carrying them and the 15.2 table rewritten to section 4. Answered in FROM Chat, REPLY__Your_Packet_F_Questions_And_Article_Page_Ruling_Answered_S404. The pilot's `signed` field still waits on the Recipe 10 batch list. No board card moved.**

> **CHAT DISPOSITION, S403: STAYS, waiting on four rulings Kain gives at the S404 open (his word, S403): 5.1 Related questions links; 5.2 the series links; 5.3 a subject field for the no-map types; and the Standard's 15.2 table corrected to section 4's thirteen retired checks (Version 7, signed). The pilot is in Cowork's Recipe 10 batch (BRIEF S403), so its `signed` field is written from that batch list, not its S402 sheet. Read S403; nothing in it is lost.**

Needs from Chat: correct the Standard's 15.2 table from the retired-checks list below, answer the three questions in section 5, and write `signed` into the pilot's record once Kain signs its sheet (the gate then passes it whole). For the factory session.

# DONE: Packet F, the content gate rebuilt as a copy of the signed Standard

**Filed by Claude Code, factory session S148. Date:** Monday 5 October 2026, late evening.
**Answers:** `BRIEF__Packet_F_Rebuild_The_Content_Gate_From_The_Signed_Standard_S402.md` (FROM Chat).
**Read first, whole:** `000__THE_ACHOLOGY_CONTENT_STANDARD.md`. It carries **Version 5** today (the same day's Version 4 plus section 15.2 item 8, the defect register); the gate is built to Version 5, and nothing in item 8 changes a machine rule.
**Nothing was imported or published.** The pilot (post 39803) was not touched on the install.

## 1. On disk

`content_gate.py`, `content_gate_standards.json`, `content_gate_acceptance.py` and a new `content_gate_fixtures.py`, all in the Content Production Factory folder beside the Standard, plus `upload_contracts.json`. Commits 288ddbb8 and the 21:44 autosave c858a1df (which caught the work in progress), pushed. Acceptance 176 of 176 (163 before; every case the Standard changed was rewritten to the new rule and still goes red as well as green). Fixtures 36 of 36. Course link acceptance 14 of 14, import checks acceptance 6 of 6.

## 2. One line per brief item

1. **signed field: BUILT.** `signed_check()`. Fails an empty field, a signer other than Kain Ramsay, a missing YYYY-MM-DD date, a missing version, and a version below `min_version` 2 (every hard rule dates from S398 or earlier). Format read: `Signed by; Date; Standard version`, e.g. `Kain Ramsay; 2026-10-06; Version 5`. Nothing Code built writes it.
2. **stances field: BUILT.** `stances_check()`. The map is read from the Standard's foundation at every run (23 rows; bold means written), never copied. Fails empty, a name not in the map, an unwritten stance, and a stance the map does not give the record's subject. The subject is found by the record's `post_title` in the question bank; failing that, by a "Map row N" note in the field. The vault is not on this Mac: where `ACHOLOGY_VAULT` names a folder the note files are looked for there; otherwise the written state is read from the map and the gate says so in a NOTE. See question 5.3.
3. **Guide bands as NOTE: BUILT.** Total words, section word guides, the workbook share, section counts, the practice block's 40 to 60 words and the landing page's two-heading floor all print NOTE. Hard, still FAIL: the quote page's closing question (79 to 89 characters), the landing page's 750 to 900 words, locked headings (book note, author biography, quote page). Keyword density is a NOTE. A test proves a far-out guide adds no FAIL.
4. **Dated checks: BUILT.** `check_introduced` maps every new check to its session; `session_dates` maps S396 and S398 to 4 October, S399 and S402 to 5 October. A record dated before a check gets a NOTE reading "NOT HELD: record dated X, before this line". Older `field_introduced` lines are untouched.
5. **Part 6 body: BUILT.** One band on every type, Help answers included: 3 to 4 sentences AND 50 to 120 words. The S357 floor, the S131 Help one-sentence line and the S356 Help ceiling are retired. Lists (the Sources list among them) are not paragraphs. Exceptions: (e) provenance formula and practice block excused the floor; (k) the knowledge-derived and hub guide close (last teaching paragraph) excused the floor; (l) Kain-approved paragraphs excused the sentence count, keeping the ceiling, recognised by a word-for-word match to the Standard's Part 14 example or by a new per-record field `kain_approved_paragraphs` (opening words, separated by semicolons); (g) Seven Beliefs keep their type exemption.
6. **Part 5 headings: BUILT.** Keyword in exactly one teaching heading; the foot headings (Put this into practice, Sources, Learning this at Achology, read off all ten records carrying the foot) are not counted. The pilot now reads 8, as the sheet does. Zero still fails on every record; the new ceiling of one is dated S396. Locked-heading types stand down, author biography now among them.
7. **Part 9 links: BUILT.** Two to five words with exception (m) read from `course_autolink.py`'s course names; at most one link per paragraph; each destination once; no link in a heading (dated S399); banned labels unchanged; the minimums stay. See question 5.1 on Related questions.
8. **Part 10 picture: BUILT.** Alt present stays a FAIL; the keyword in the alt is a NOTE.
9. **Part 11 Sources: BUILT, record level.** Where a record carries a Sources list: every outside link in the teaching must be on it (by DOI or address), services excepted (`services_not_sources`: findahelpline.com, 988lifeline.org, samaritans.org, nhs.uk, the Part 7 rule 15 approved wording's services); every entry must appear in the body (by surname, title words or DOI). A source named in prose with no link is the checker's to catch. The template block waits on Kain's signed spec, as the brief says.
10. **Part 13 course: BUILT.** `destination_course_name` present and linked at its first mention; any currency sign before a digit fails in an article or Help answer body.
11. **Part 16 words: BUILT.** The lists are copies of Part 16, proved word for word by the fixtures run on every run. "plainly" and "truly" moved to their own failing line (rules 7, 8). Watched words (rule 9) and the stance Never words (rule 1) print as NOTE. The quote exemption now applies on quote pages only. "actually" unchanged. Contractions: Help answers fail with none; every other type gets a NOTE count.
12. **Part 17 types: CONFIRMED.** Every band and section count in the gate matches 17.1 to 17.7 as written: book-derived 1,600 to 2,400 and 4; knowledge-derived 1,200 to 1,800 and 4 to 6; instructor 1,200 to 2,200 and 4 to 8; hub question 850 to 2,000 and 3 to 8; Seven Beliefs 2,500 to 3,700 and 6 to 11; hub guide 2,500 to 4,000 (5 to 13 sections, a guide); book note 1,100 to 1,400; author biography 1,600 to 2,000; quote page 650 to 825; workbook 1,100 to 1,900; landing page 750 to 900; Help 320 to 1,500. The elder article takes the instructor entry (noted; no elder type). buyer-intent-answer removed from the types still to enter. field-authority-article marked retired: its records on the install are still measured, a new one dated from 5 October is refused.
13. **Part 1 "proven" allowance: BUILT.** Titles, search titles, descriptions and excerpts are now checked against the always-banned lists (they were not before); a phrase on `title_question_allowance` passes inside a question in `post_title` or `rm_seo_title` only. The body still fails on it.
14. **Older records: BUILT.** `signed` and `stances` fail only where the record's date is 5 October or later. The record's date is the later of `post_date` and its last edit stamp, read from git (the file's last commit, or today if it has uncommitted changes). Across the 1,369 records on disk, 1,250 get the NOTE; the 119 edited today are held.
15. **Fixtures: BUILT.** `content_gate_fixtures.py`. Known-good is the pilot where it lives; known-bad is the pilot with 21 planted faults, rebuilt fresh each run (so no file carries the planted dash). Printout in section 3.
16. **UK spelling: BUILT, NOTE only.** The Mac's own British English dictionary through JavaScript for Automation, no outside code. Runs on single-record command-line runs, not inside the importers' bulk calls (it costs about a second a record). Prints NOT RUN where there is no Mac checker.

**What you return, the other half:** `stances` and `signed` added to every contract in `upload_contracts.json` (book-note, instructor-article, author-biography, faq-article, plus a `packet_f_fields` entry naming them). WP All Import is retired, so "the mapping" is each importer's payload: `import_field_authority_articles.py` now carries both (its H9 hash re-reviewed, theme repo commit 871ce0d). The help, quote, instructor, biography and book note importers build their own payloads and are owed the same change, each with its own H9 review.

## 3. The pilot, before and after

**Before (the gate as it stood):** FAIL (5): total body words 2153; headed sections 11; paragraphs, 3 breaches (the two approved closing paragraphs and "Sources p1"); keyword density 0.37%; keyword in image alt text.

**After, unsigned (tonight):** FAIL (1), the signature. Every other line passes or prints a NOTE:

```
  NOTE  body words, a guide (Part 17)                  1909 in the teaching, 2153 in all (guide 850 to 2000)
  NOTE  teaching sections, a guide                     8 found (guide 3 to 8)
  NOTE  paragraphs excused by a named exception        The question underneath your cousin's p1 (l) Kain approved word for word; ... p2 (l)
  PASS  keyword in exactly one teaching heading (Part 5 rule 4) 1 of 8 headings
  NOTE  keyword density, retired as a fail             0.37% (2 hits; the old band 1.0 to 1.5)
  PASS  link text 2 to 5 words (Part 9 rule 1)         all within; 1 full course name, exception (m)
  PASS  every outside source linked in the body is listed (Part 11 rule 4) 4 outside links, all listed or services
  PASS  every Sources entry appears in the body (Part 11 rule 4) 4 entries, each named in the body
  PASS  stances field present and valid (foundation item 2) Thinking and Mindset, Self Awareness, Self Knowledge; subject 5
  FAIL  signed by Kain (Part 19 rule 7)                the signed field is empty
  NOTE  UK spelling, words not in the British dictionary (Part 16 rule 13) Galante, findahelpline.com, randomized
  GATE: FAIL (1)
```

**After, signed: WAITS ON Kain signing the check sheet and Chat writing `signed` into the record.** The pass path is already proved on a temporary copy carrying a simulated signature (not a record, deleted at once): GATE PASS.

**Fixtures run:** known-good holds (fails on the signature alone, as it must until Kain signs); known-bad fails on all 21 plants (banned word, machine tell, plainly, actually twice, dash, one-sentence paragraph, nine-word link, two links in a paragraph, a destination twice, keyword in two headings, link in a heading, a price, the course named unlinked first, a Sources entry the body never names, an outside link not listed, no alt, a banned label, process text, no stances, no signature, a banned phrase in the description); a second form fails a stance not in the map, a stance not given to subject 5, a signer other than Kain and Version 1; an older record gets NOTEs, never FAILs. 36 of 36.

**Impact across all 1,369 records (old gate against new, read-only):** no record that passed before fails now except one, Seven Beliefs Part 2 (edited 4 October, so held to Part 9; see question 5.2). Four records that failed before now pass (guide bands). New FAIL lines sit on records already failing: 119 unsigned and 36 without stances (records edited today), 20 with the keyword in two or more headings, 49 on link length, 43 on the paragraph band, 40 on links per paragraph. 96 "truly" lines are not new failures, only renamed.

## 4. Checks retired, so the 15.2 table can be corrected

1. Total body words as a FAIL (now a NOTE).
2. Section word guides as a FAIL (now NOTE); the workbook half rule (share) as a FAIL (NOTE).
3. Headed section count as a FAIL (NOTE, teaching sections only).
4. The S357 paragraph floor ("three sentences OR 50 words, one short per section").
5. The S131 Help one-sentence paragraph line (folded into the band).
6. The S356 Help paragraph ceiling (60 words, 3 sentences).
7. The separate "no paragraph over 120 words" line in the search finish (folded into the band).
8. Keyword density as a FAIL (NOTE).
9. Keyword in image alt text as a FAIL (NOTE).
10. "Keyword in a subheading" (at least one), replaced by "exactly one teaching heading".
11. The practice block's 40 to 60 words as a FAIL (NOTE; the block's presence still fails).
12. The landing page's two-heading floor as a FAIL (NOTE).
13. The verbatim-quote exemption on articles (quote pages only now).

The table's "title unique" (Part 1) and "description unique" (Part 2) are not measured by this gate and were not before; the keyword register's uniqueness is. Correct the table, or commission the two lines.

## 5. Three questions

5.1 **Related questions links.** A Help answer's four Related questions are links whose text is a question title, often 6 to 10 words; Part 9 rule 1 says 2 to 5. The gate prints them as a NOTE today. Is a Related questions list held to rule 1, or excepted (a new exceptions register line)?
5.2 **Series links.** Seven Beliefs closing blocks link each part by its full title (7 to 9 words), which Part 17.1 asks for and Part 9 rule 1 fails. Part 2 is now held (edited 4 October). An exception, or shorter link text?
5.3 **Stances on types the question bank does not carry.** Book notes, quote pages, biographies and workbooks have no map row, so the gate checks their stances exist and are written but cannot check them against a subject; it prints a NOTE. Should those records carry a subject number field, or is the checker's read enough?

## 6. Readings I made, each overturnable

The record date uses git, so a bulk edit to old records (a field backfill) puts them under the new rules from that day. The approved closing is matched word for word, after straightening quotes. The (k) short close is the last teaching paragraph only. The services list is the approved helpline wording's services. Stance names are read from the field with notes in brackets and after a full stop dropped, so the pilot's field reads as its three stances.

## 7. Addendum, later in S148: the two S403 rulings folded in

Answers `NOTE__Two_S403_Rulings_For_Packet_F_The_Course_Link_And_Help_Courses_S403`. Project commit 0437658b. Gate acceptance 176 of 176, fixtures 39 of 39, course linker 16 of 16, import checks 6 of 6.

1. **Course links on the short name.** The gate's Part 13 line, for records dated from 6 October 2026 (S403): the full DSRD 5 name written plain at least once and never linked; exactly one link to the course, on one of its DSRD 5 section 9 short names. Exception (m) is retired from S403, so a full name linked whole fails link length; older records keep it, by date. Proved both ways in the fixtures (section 7). `course_autolink.py` now links section 9 short names only: every full name and card title is claimed as plain text first, so no short name inside a full name is ever linked, and a course already linked anywhere is left alone. Its tests were turned round to the new rule. **Question 5.1 shrinks with this:** a Help answer's Related questions links are still question titles, still a NOTE.
2. **Several courses in a Help answer.** No one-course check exists in the gate, so nothing needed exempting; noted in the standards file. The Standard's version in force is recorded as 6.
3. **Nothing was re-linked on any record or page.** The linker runs when a page is next pushed; records written under exception (m) are not rewritten in bulk.

OWED BACK: Chat's answers to 5.1 to 5.3, the 15.2 table correction, and `signed` written into the pilot when Kain signs; the after-signed gate run is then Code's, one command.

*No em or en dashes in this file; checked before writing.*
