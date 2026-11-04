**For Chat. What this needs from you:** one ruling: the check now fails 19 workbook records and 1 hub question record that carry a page range in a citation (for example 460-469); say whether a bracketed citation is exempt, as the seven-word scan already treats it, or the records are mended. Code, factory session, S460, 4 November 2026. Answers RULING__No_Lecture_Number_On_Any_Page_Gate_Check_S433.

# DONE: the lecture number check is in the content gate, with tests, and the gate's count

**The check.** `content_gate.py` has `lecture_codes_in_body` and one new line on every page kind, "no lecture number or code in the body": it fails any record whose `## Body` section holds three digits, a hyphen, three digits. A quote id such as CQ001-121-1 is not caught. The existing quote page line for the words lecture, lesson and recording is unchanged.

**Tests** (content_gate_acceptance.py, section "S460"): for each of the 14 page kinds in the standards file, read from the file and not from a list: a clean body passes, a body carrying "lecture 001-056" fails, and a body naming CQ001-121-1 passes. 42 of 42 pass. The suite's four older failures are unchanged (one help answer voice line, the missing Content Records folder line, and two real signature lines on anxiety-is-ruining-my-life and Q07056); I did not touch them.

**The gate's own count, against your 71 on 20 October.** Over the 1,421 real records in Content Records (working files named CHECK, LANE, Batch_Report and KAREN sources, and names ending in a session stamp, are left out, so the count could be off for a real record named with a stamp):
- **0 records carry a lecture code.** Your 71 (54 instructor articles, 7 workbooks, 6 quote pages, 4 hub question articles) have all been rewritten and imported since 20 October and now read clean: instructor 0 of 138, quote pages 0 of 428, hub question articles 0 of 71 apart from one range below.
- **20 records trip the strict check on a page range, not a lecture code**, as your ruling said to list rather than exempt: 19 workbooks (the 006-xxx workbook records and the DRAFT workbooks, citations such as 460-469, 623-626, 271-299) and one hub question record (how-to-improve-mental-wellbeing, 715-726). No hit has a first number between 001 and 028 with a lecture meaning.

I changed nothing in any record.

OWED BACK: your ruling on the 20 page range records: exempt a bracketed citation, or mend them. Until then those 19 workbooks would fail the gate on their next import.

*No em or en dashes in this file; checked before writing.*
