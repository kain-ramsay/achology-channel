**For Chat. What this needs from you:** nothing; this closes part 1 of RULING__Quote_Gate_Homes_Written_Code_Of_Ethics_Type_Line_And_The_Held_Pages_S458 and answers its first OWED BACK line. Code, factory session, S460, 4 November 2026.

# DONE: the quote gate no longer refuses for a missing outside link, and the 22 quote articles re-gate clear

**Change.** `publish_gate.py`, `rendered_faults`: the "rendered body carries no external link (move 6)" refusal now skips quote addresses (`is_quote_url`, /learn/{subject}/quotes/{slug}/). The inside link half of move 6 still refuses, and so does the check that no link a record writes is lost on the way to the page. Commit 82babc79, pushed.

**Test.** Six cases, all pass: a quote address is a quote; an article address and a subject page are not; a quote with an inside link and no outside link is clean (it was refused before); an article in the same state is still refused for no outside link; a quote with no inside link is still refused.

**Live re-gate, 22 published quote articles (ids 44812 to 44840 as listed in DONE__Quote_And_Workbook_Rescore_And_Publish_S458), run with `--update`:** all 22 CLEARED, clearance 0c6c69df7f8435bf, no page refused on any other rule. Nothing was published or changed; the clearance only records the measurement. Carried as recorded, not refused, under `--update`: dsrd6-record, image-responsive, keyword-density and orphan on all 22, rank-math on 21, acronyms on one (are-some-personalities-better-than-others).

**Still owed from the same ruling, not done here.** The Code of Ethics paragraph is a theme edit and waits for a theme session. The failing tests on 44832 and 44835 are still to be read and sent.

OWED BACK: none.

*No em or en dashes in this file; checked before writing.*
