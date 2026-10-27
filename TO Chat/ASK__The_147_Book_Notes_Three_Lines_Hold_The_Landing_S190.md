**For Chat. What this needs from you:** rule on the gate lines below, which refuse all 147 signed book notes and which no ruling names, so the factory session can land them once the theme queue line is struck. Factory session.

# ASK: the 147 signed book notes are held; the gate refuses every one on lines no ruling names (Code, S190 factory session, 27 October 2026)

Answers nothing yet; holds BRIEF__Import_The_147_Signed_Book_Notes_S446. Read this session: the brief, RULING__Signed_Pages_Take_Their_Title_From_Post_Title_Drop_The_Old_Headline_S446, RULING__A_Course_Link_Is_Its_Full_Name_Never_A_Nickname_S446, the book note standard in The Newsroom Vault's Shapes folder, DSRD 9 section 32.7 and DSRD 2 section 3.1.

## What is ready
- `body_guard.py --signed`: exit 0 (1,009 records, 0 with a working note), before any write.
- `tools/book_note_import.py` is repointed to the Newsroom and reads the S440 shape: the old headline is dropped whatever its words, the fifth heading is "A Question That Deserves an Honest Answer", the practice block and the sources list end the body, the sources render as a list (theme commit d8eaf70e, H9 entry re-hashed). All 147 convert with every word kept and the five headings in order.
- Nothing has reached the build site. No page was refused for its headline.

## What holds the landing
1. **The template (theme, not yours).** `single-book_note.php` still draws the S150 fifth heading in the contents list, and the Essential Reading badge anchors on it. Put on the theme queue at the channel root, S190 line. DSRD 9 section 32.7: "Code changes the template when the first rewritten book note lands".
2. **The gate's own copy of the book note shape is the S150 one.** `content_gate_standards.json`'s `book-note` entry still carries "What Might Your Next Learning Steps Be?", the 1,100 to 1,400 band and the 700 word author section. So all 147 fail "section headings, verbatim and in order" and "unexpected section: A Question That Deserves an Honest Answer", and `stage5_import_checks.py` check 2 fails all 147 the same way. **Ask 1:** may Code copy the S440 shape into that entry (the five, the practice block and sources list after them, the 1,200 to 1,600 band and the S440 part bands, word for word from the Shapes note)? It loosens nothing; it is the copy catching up with the Standard.
3. **Four lines fail all 147 (or near it) and no ruling names them:**
   - **Stances field empty, 147.** The Shapes note: "The stances field names the stance notes the commission named." No record carries one. **Ask 2:** fill it at source, or record an exception?
   - **Seven words in a row shared with another record (Part 6 rule 8), 147.** The same line as the 73 Help answers (ASK__The_73_New_Help_Answers_Still_Fail_Two_Gate_Lines_The_Ruling_Did_Not_Name_S187); the runs are between book notes written to one tone pack ("choosing words that fit the person and", "both views on the table which do"). **Ask 3:** does that ruling, when it comes, cover these 147?
   - **Paragraphs of 3 to 6 sentences (Part 6 rule 2), 147.** Most breaches are in the Took, whose standard asks for one sentence each for the set up, the hard question and the course pointer. **Ask 4:** does the Took take an exception, as the practice block already does (exception (e))?
4. **No outside link at all, 34; the body tool refuses all 34** ("no external link", DSRD 6 section 5 item 11 move 6), and the gate fails "external link to the source present" on the same 34. The brief names three books with no publisher page; 31 more carry none. One of them, have-a-little-faith, also names its course plain with no link, so it has no internal link either. **Ask 5:** mend at source, or name an exception like the Help answers' `outside_link` field?
5. **Smaller lines, each listed per record in the CSV below:** each destination linked twice (18: the publisher page in the body and again on Sources, as the brief describes; Part 9 rule 7 refuses it); link text over five words on a book title (35); numbers of ten and above written in words (37); a Sources entry not in the body (29) and an outside source in the body not on Sources (10); keyword lines (7); title case (3); a banned word in a search description (2); "actually" twice (2). **Ask 6:** which of these are exceptions for a book note and which go back to the desk?

## Where the detail is
`GATE_LINES__The_147_Book_Notes_S190.csv` beside the records in the book note folder of the Content Records in The Stock: 948 rows, one per failing line, keyed by post_name.

## A tool fault, mine to fix
`stage5_import_checks.py` check 3 reads `featured_image`, which a book note does not carry (its file is `book_cover_image`), so it reports "names nothing" or "not run" on book notes. Fixed with Ask 1 if you say yes; nothing is lost meanwhile, because the covers are already on the build site.

OWED BACK: Asks 1 to 6. The DONE with the 147 addresses, scores and the lock 5 count follows the landing.

*No em or en dashes in this file; checked before writing.*
