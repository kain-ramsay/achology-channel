> CODE DISPOSITION, S169: WAITS ON the first API batch's COST_REPORT being filed (the batch is in its last rounds); the three gate lines this brief repeats are already DONE (DONE__Three_Gate_Lines_S169).

First line of need: Code, factory session: teach the API worker Help answers, quote pages, hub question articles and hub guides, give every type a short fixed reading list, and stop the gate printing FAIL on the four lines every record fails. Start after the first API batch's COST_REPORT is filed.

# BRIEF: the API worker takes Help answers and quote pages; short reading lists; a quiet gate (Chat, Session 426, Thursday 15 October 2026)

**Why (Kain's yes, S426).** Chat's audit (`AUDIT__Editorial_System_And_The_Multi_Agent_Question_S426.md`, in the Content Production Factory folder) found the worker is the right engine for the Full Editorial Programme, and that more agents would cost more and write worse. Kain signed PACK_03 (quote pages, 1.0) and PACK_04 (Help answers, 1.0) at S425. Those two rows are 754 of the 1,317 pages left, and today the worker refuses both. Reading is most of the cost (S425 model test: 100,000 to 190,000 tokens an agent a round), so each type gets a short list and nothing else.

**What stays exactly as it is.** Rule 12: Sonnet 5.5 writes and Sonnet 5.5 checks, writer effort high, checker effort medium. Batch mode. Output to `runs/<run>/out/` only; never into Content Records; never a record with a `signed` line or uncommitted changes. The $20 cap per run. Free checks before the paid checker. One batch, then stop and report. No lane is touched.

## Job 1. Help answers (`help-answer`, PACK_04)
- **Writer reads only:** PACK_04 file 02 (What a Finished Help Answer Is) and file 03 (How a Help Answer Is Made, including "The moves"), and the two gold examples named in file 05: `help-answer/HELP__cbt-practitioner-vs-cbt-therapist.md` and `help-answer/HELP__what-is-achology.md`.
- **Checker reads only:** the same four, plus the original record. It tests every paragraph against every move in file 03, the shape in file 03, and file 03's fixed lines, and returns JSON in the same shape the article checker uses.
- **Free checks:** no dashes; headings, links and fixed lines unchanged from the original unless file 03 asks for them; growth within the limit file 02 sets (tell Chat if file 02 sets none, and use 130 per cent until Chat rules); then `content_gate.py` as `help-answer`.

## Job 2. Quote pages (`quote-page`, PACK_03)
- **Writer reads only:** PACK_03 file 02 (What a Finished Quote Page Is) and file 03 (How a Quote Page Is Made: the spine Hook, Book, Look, Took; the voice; the moves; what never appears; the eight questions), and the gold example in file 05: `quote-page-EXEMPLAR__Why_Security_Comes_At_The_Cost_Of_Freedom_S420.md` (record CQ001-144-1).
- **Checker reads only:** the same three, plus the original record. It answers file 03's eight questions and tests every paragraph against every move.
- **Free checks, as well as Job 1's:** `quote_text`, `quote_author` and `source_book_title` are word for word the original's; a changed quote is a fail with no paid check. Then `content_gate.py` as `quote-page`.

## Job 2b. Hub question articles and hub guides (`hub-question-article`, `hub-guide`, PACK_01; added S426, Kain's yes)
Both are under the signed articles pack, so they run exactly as field authority articles do: the same writer and checker rules, the same moves file (PACK_01 file 06) and gold example, and the gate as their own type. Where PACK_01 file 01 (The Kinds of Article) sets a different length or shape for either kind, the writer and checker read that section too, and the 1,600 to 2,400 teaching word line follows it. 58 and 28 records are unsigned. Include them in Job 4's dry run: three of each.

## Job 3. Short reading lists, for every type
Put each type's list in one place in the worker (beside `SETTINGS`), named by file, so the list is read, never remembered. Field authority articles keep what they read now. Cache each list once per batch. Add one column to `cost_log.csv`: the tokens each call read, so Chat can see the list working.

## Job 4. A dry run per new type, then stop
Five records per type, chosen by you: unsigned, not in a PROOF folder, not on any lane's card, mixed in length. Cap $5 a type. File one DONE with both COST_REPORTs. Chat reads all ten against the gold examples before any volume run is briefed.

## Job 5. A quiet gate
Every record now fails four lines that everyone excuses by hand: the retired type key, the course name line, `stances` empty, `signed` empty. A gate that always says FAIL stops being read.
1. **Retired type key and course name:** find why every record fails them and fix them at the source (the records by script, or the gate's list, whichever is wrong). Report which, with a count.
2. **`stances` empty and `signed` empty:** print them on one status line, `NOT YET SIGNED`, never as FAIL, for a record with no `signed` line. The importer still refuses any record without `signed`. That is where the rule bites, and it stays.
3. A test for each change, in `content_gate_acceptance.py`.

The three gate lines owed from `RULING__First_API_Batch_Named_Factory_Copy_Yes_And_Three_Gate_Lines_S425` go in the same session.

## Not in this brief
The fact check on flagged claims (the audit's item 5) waits on the first batch's results and comes as its own brief. Book notes and workbooks wait on PACK_02 and PACK_05 being signed.

OWED BACK: one DONE with both dry runs' COST_REPORTs and the ten staged records named; the gate changes with their tests; the reading list column working.

*No em or en dashes in this file; checked before writing.*
