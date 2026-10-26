> CODE DISPOSITION, S181: WAITS ON a factory session (the gate and autolinker change; read in full by the Manifesto theme side session, which touches no gate or content import).

**For Code, factory session. What this needs from you:** change the copy gate and the course autolinker so a course's link is its full DSRD 5 name, and never a nickname. Do this before you import the 102 instructor articles, which now link the full name.

# RULING: a course's link is its full name, never a nickname (Chat, S446, 26 October 2026, on Kain's yes)

Read from the vault first: The Course Is Named in Full and Its Full Name Is the Link, Once (05 The Page), and Ten Course Sentences Kain Approved Show How a Page Points a Reader to a Course (08 Approved).

**Kain's yes, 26 October 2026, Session 446,** from one rendered page showing every line that changes. It writes home his ruling of the same day in your S180 sitting (RULING__Product_Names_Are_Never_Shortened_Hold_The_374_Import_S180): courses and schools are products and their names are never shortened. He approved 145 book note course sentences written with the full name as the link and called them the standard.

**The rule now.** A course is named by its full official name from DSRD 5, exactly as written there, and that full name is its link, once per page and never twice. It is never written plain first with a nickname linked after it. A course's full name is the one link allowed to run past five words. It holds on every kind of page, including a quote page's source sentence and each course in a Help answer's list.

**Changed at source today:** The Achology Content Standard, now Version 34 (Part 9 rule 1, Part 13 rule 3, the Help answer courses line, the Part 19 check sheet, the table row and exceptions (m) and (q); Version 33 is in the Newsroom Archive). The house book, the PACK_03 quote page sources (files 01 and 02), and four vault notes. The S403 short name rule and exception (q) are retired.

**For your files:**
1. content_gate.py: the course link check (around _course_nicknames and the S403 short name lines) must pass a course link whose words are the full DSRD 5 name, and fail one that sits on a nickname or any shortened name. The link length check must let a course's full name run past five words.
2. course_autolink.py: it must no longer add a link on a section 9 short name. Where it links a course at all, the link goes on the full name.
3. content_gate_acceptance.py: its cases for the S403 rule need turning round to match.
4. content_gate_standards.json: any copy of the old Part 9 or Part 13 wording follows the Standard.

**What waits.** Older signed pages still link nicknames: product_name_check.py found short names in 682 quote pages, 231 hub question articles, 101 field authority articles, 100 Seven Beliefs pages, 90 workbooks, 81 author biographies and 20 hub guides. Chat mends each kind when it next goes through the desk. Do not rewrite them in the factory. Until then the gate will fail those records, which is correct.

OWED BACK: one line in your next DONE naming the gate version, and confirming the 102 instructor articles pass the course link check before they are imported.

*No em or en dashes in this file; checked before writing.*
