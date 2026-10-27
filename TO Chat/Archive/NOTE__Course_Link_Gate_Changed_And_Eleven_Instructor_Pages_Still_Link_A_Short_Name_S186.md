**For Chat. What this needs from you:** mend the course sentence in eleven signed instructor records, which still write the full course name plain and link a short name after it; the other 127 instructor records pass and import now. Factory session, Code S186.

# NOTE: the course link gate is changed, and eleven instructor pages still link a short name (Code S186, factory, 27 October 2026)

**Done: RULING__A_Course_Link_Is_Its_Full_Name_Never_A_Nickname_S446.**
- `content_gate.py`: exception (m) holds on every record whatever its date, so a course's full DSRD 5 name may run past five words as its link; exception (q), the nickname link, is retired. Part 13 rule 3 now reads "course: full name is its link, once (Part 13 rule 3, S446)" and fails a page whose full name is not linked, is linked twice, or whose course link sits on a short name. A name opening on "The" may carry it inside or outside the link.
- `course_autolink.py`: links a course on its full name only (with or without its bracket), never a nickname or card title.
- `content_gate_acceptance.py` and `course_autolink_acceptance.py`: the S403 and exception (q) cases turned round, five new cases for Part 13 rule 3. Gate 438 pass, no line failing that did not fail before; autolinker 16 of 16.
- `content_gate_standards.json`: the link_rules note follows Version 34.

**The instructor records, run through the changed gate (138 signed, the 102 and the 36):** 127 pass the course line. These eleven fail it, because each writes the full name plain and links "Practitioner Diploma Course" (the checkout address) after it, which the S446 ruling forbids: a-diagnosis-actually-describing, a-false-epidemic-happen-without-anyone-lying, ai-give-you-a-second-opinion, ai-making-us-worse-thinkers, five-symptoms-mean-depression, hypomania-from-an-ordinary-mood-swing, is-my-grief-normal, self-report-decide-a-diagnosis, the-definition-of-mental-disorder, the-rise-in-autism-diagnoses-real, what-is-concept-creep. They are held from the import until mended at source.

**Separately, 66 of the 138 fail Part 9 rule 1 on links that are not courses** (another article's full question title as its link, a source's name, or a one-word web address such as alecwells.com). That rule is unchanged. Ruling needed, in one line: are an article's own title and a one-word address accepted as link words on signed pages, as for the Help answers' accept list, or mended at source?

**Found while committing: The Newsroom had no version history since 20 October.** The S434 rename left every ignore rule in the project record naming the old folder, so the Machine's scripts, the Content Records and the Vault were outside git for a week. The same rules are now written for 04. The Achology Newsroom and the folder is committed (3,887 files, commit 58e2d646, pushed). Nothing was lost; the history simply starts again today.

**NOTE__Gate_Faults_Found_On_The_Resisting_Change_Batch_S448, item 1 confirmed:** no importer in The Machine calls `body_guard.is_signed`; only body_guard.py itself does. Items 2 and 3's labels follow in the factory session's report; item 3's link text line is the change above.

OWED BACK: the eleven records mended and re-signed, and the one-line ruling on non-course title links.

*No em or en dashes in this file; checked before writing.*
