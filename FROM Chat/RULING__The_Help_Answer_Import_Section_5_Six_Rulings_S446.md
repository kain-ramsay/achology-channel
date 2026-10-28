> CODE DISPOSITION, S197: WAITS ON Chat's NOTE answering TO Chat/ASK__Two_New_Help_Answers_Carry_Empty_List_Lines_S197 (item 1: 71 of the 73 new answers are on the build site, TO Chat/DONE__The_71_New_Help_Answers_On_The_Build_Site_S197; the CBT exemplar is among them; two wait on that NOTE).

> CODE DISPOSITION, S187: WAITS ON a RULING in FROM Chat answering TO Chat/ASK__The_73_New_Help_Answers_Still_Fail_Two_Gate_Lines_The_Ruling_Did_Not_Name_S187 (item 1) and Chat's NOTE that the item 4 records are mended. Items 2, 3, 5 and 6 are done and item 4.1's CSV exists: TO Chat/DONE__The_302_Help_Answers_Updated_The_73_Wait_On_One_Ruling_S187.

> CODE DISPOSITION, S183: WAITS ON a factory session (read in full by the theme main session; it touches no theme file, and the Help answers factory session was archived after delivering 286).

**For Code, factory session. What this needs from you:** finish the Help answer import on the six rulings below, and first write the Rank Math failing tests CSV item 4 names.

# RULING: the Help answer import, section 5, six rulings (Chat, S446, 26 October 2026)

Answers DONE__The_374_Help_Answers_Imported_With_Full_Product_Names_S180, section 5. Read from the vault first: the ruling "Every Article Is Checked Once and, Where It Fails, Rewritten Whole in Kain's Tone by a Session on His Plan"; PACK_04 Help Answers, file 02 (the record table). Kain's governing words for this batch, S180: "I don't want these articles rewritten. I want full canonical names built into all of these articles." So nothing below rewords signed prose except where a full name cannot go in any other way.

BRIEF__Import_The_374_Signed_Help_Answers_S445 is DONE for the 286 it delivered; it stays open only for the records named here.

## 1. The 73 new answers: mend the fields at source, accept the prose lines on Kain's signature
- **Empty stances field (73):** a field, not prose. Fill each record's stances field with the stance titles its page brief lists under "Step 9" in the vault gate's batch folder for help_answers_01 (`pages/HELP__<record>.md`). Where that brief says the subject was left to the check, use the subject the check named in its JSON.
- **Link words outside two to five (63), keyword not in the first 10 per cent (36):** these are lines in signed prose. Accepted on Kain's signature for this batch, each recorded by name on the record's DSRD 6 line as `exception, 2026-10-26, signed prose not reworded (Kain S180), approved by Kain`. Give `import_help_answers.py` an accept list of exactly these gate line names for exactly these 73 records; no other line, record or type.
- **The "(opening)" paragraph lines:** the S445 subject note and title heading read as a paragraph. Instrument line: strip both before the gate reads the body, as your converter already does.
- **The CBT exemplar** carries Kain's Version 33 signature, so it imports with the 73.

## 2. The 15 records held or refused
- **5 refused:** the 4 with no outside link are all answers about Achology itself, and PACK_04 file 02 says such an answer "carries none, and the report says so". The front door is wrong for them: let a help answer with no outside link through when its record says it is about Achology only, and import these 4. The stray "[" on best-browsers-devices-achology-community is a typing fault, not prose: remove the one character and import.
- **10 held for an alias:** DONE, see NOTE__The_Ten_Help_Answers_Mended_At_Source_S446. Chat mended these at source (the smallest change that lets the full DSRD 5 name stand, nothing else reworded) and writes a NOTE into FROM Chat naming each changed sentence. Waits on that NOTE existing; import them when it does.

## 3. The two stage 5 instrument lines: correct the checks
Check 2: for help-answer, `sections: {}` means headings are free, as `_sections_note` says. Check 3: for help-answer, the picture is read from the body, as `_record_shape_note` says, and no `featured_image` field is required. Change `stage5_import_checks.py` for the help type only, and re-run it on all 364.

## 4. The 239 pages under 90: lifted to 90 by keyword placement (Kain, S446, 26 October 2026)
Kain's ruling, asked whether the pages stand at their scores: "yes" to lifting every page to 90. A keyword placed where Rank Math reads it is optimisation, not the rewriting Kain ruled out at S180; the claimed focus keyword stays (PACK_04 file 02), and the words move to carry it. The method:
1. **Code, first:** for every Help answer page under 90 (the 286 on the build site and, once imported, the 88 from items 1 and 2), write one CSV into the help-answer folder of the content records (The Stock), `RANKMATH_FAILS__Help_Answers_S446.csv`, with the columns record, post, score, focus_keyword, and one column per failing Rank Math test (keyword in title, in the description, in the first 10 per cent, in the content, in a subheading, in an image alt, density, length, links), each true where it fails. Read with score_run.py from the editor, nothing saved. Then a NOTE into TO Chat saying the CSV exists.
2. **Chat:** a writing session makes only the fixes each row names, in the records, by the smallest change: the focus keyword into the opening sentences, into one existing subheading where it reads naturally, into the content to Rank Math's density, into the SEO description, and into the picture's alt text. No other sentence changes. Chat then writes a NOTE into FROM Chat.
3. **Code:** import the mended records with `--with-seo`, rescore every page, and report each score. A page that cannot reach 90 only because the keyword is not in its address (addresses are never re-slugged) is named with its score; no address changes.
Waits on: the CSV existing.

## 5. The smaller lines in the NAMES file
- **14 lines missing "the":** add the one word "the" before the full name where English needs it. Nothing else changes.
- **Short names in four records' page fields** (dimap-course-upgrade title, first-course-complete-beginner description, skilled-helper-course keyword and title): replace with the full DSRD 5 name. Where a field then runs over its length limit, say which in your DONE and Chat words it.
- **"the DiMAP Course Upgrade":** accepted. It is a product name in DSRD 4 section 1.1b ("DiMAP Course Upgrade"), and "the" before it is ordinary English. Add it to `product_name_check.py`'s accepted list with that source.
- **17 records naming a per answer picture:** DSRD 1 section 8.2b keeps one picture per category. Correct the 17 records to their category picture; the live pages are already right.

## 6. Secondary keywords: ruled
Kain's yes, S180, is written into PACK_04 file 02 as the row "Other phrasings": each record's `query_variants`, up to four, go into Rank Math's secondary keyword slots at import, never into the body. Apply it on this import and on the 286 already on the build site. Copy the row into the pack's kit in The Machine.

OWED BACK: one DONE naming the records imported under each item, and any field that ran over its limit.

*No em or en dashes in this file; checked before writing.*
