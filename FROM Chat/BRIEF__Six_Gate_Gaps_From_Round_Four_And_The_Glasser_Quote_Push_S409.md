> CODE DISPOSITION, S151: WAITS ON a factory session opening: gate and quote push work names no page design, so the theme session S151 leaves it untouched (Harness Rule 1, two sessions).

**For Code: six gate gaps named by Cowork's round four, and one quote push. Kain's yes, S409.**

# BRIEF: the six gate gaps from round four, and the Glasser quote push (S409)

**From:** Claude Chat, S409, Tuesday 6 October 2026, on Kain's yes. **Standalone:** you cannot see this conversation; everything you need is here. **Source of the gaps:** Cowork's `DONE__The_30_Mental_Health_Pieces_Round_Four_9_Of_Thirty_Ready_S407` (FROM Cowork Archive), the "Other flags" section, and the defect register's three S409 lines (`000__THE_DEFECT_REGISTER.md`, factory folder root). **Runs after** `BRIEF__The_Gate_And_Publish_Tool_Brought_To_Standard_Version_9_S405` if that has not run yet; the two touch the same tool, so take them in order.

## Job 1. The gate (`content_gate.py` and `content_gate_standards.json`), six checks

Each is a fault the machine missed and a fresh checker caught by hand. Fix order (a) in the Standard's section 15.2 item 8: the gate gains or tightens a check. Date every new check S409 (section 15.2 item 2), so records written before it get a NOTE, never a FAIL.

1. **Corpus stem scan (Part 6 rule 8; harness reading S2 and S15).** For every record gated, find any run of seven or more words in a row that also appears in any other record in Content Records. Exclusions, from reading S2: the approved help line, text inside quote marks, the fixed approved lines, locked headings, DSRD 5 course names and nicknames, the names of bodies and books, and Related questions titles. Print each match with the other record's slug. FAIL for records dated on or after S409; NOTE before.
2. **Link text in sentence length (Part 6 rule 3; reading S18).** Count a sentence's words with its link text included. The gate strips link text today, so a 49-word sentence passed in `how-does-mental-health-affect-sleep`.
3. **The description opens with the answer (Part 2 rule 1; reading S1).** Add a NOTE, not a FAIL: print the description's first clause so the checker can read it. This is a human rule in the 15.2 table and stays one; the NOTE is a prompt.
4. **Title case (Part 1 rule 9).** Knowledge Hub article titles in title case; Help answer titles in sentence case (Cowork's reading, held). FAIL dated S409.
5. **Numbers ten and above written in words (Part 16 rule 13).** The gate missed "ten weeks" in `how-long-does-a-mental-health-course-take`. Read Part 16 rule 13 first and match the gate to exactly what it says.
6. **The six-word nickname link (exception (q)).** The gate prints a FAIL on a course link that runs past five words when it sits on that course's DSRD 5 section 9 nickname. Exception (q) allows it; the gate must too.

Acceptance: the existing suites still pass (content_gate_acceptance, stage 5 import checks, course autolink), plus one acceptance case per check above in both directions, run against the real gate. Note the `content_gate_fixtures.py` pilot plant you reported broken at S150 is still owed its update.

## Job 2. One quote push

Quote record `CQ018-062-1` (course 018, lesson 062) and the article `mental-health-without-therapy-or-medication` were corrected by Cowork at round four: the quote now reads "Everyone can change because, as William Glasser says, everyone has a choice." (the record had dropped the Glasser clause; defect register, S407 line). The quote page on the build site still carries the old text. Push the corrected record with the body update tool, which never changes a page's status. The article is not pushed by this brief; it goes with its batch when Kain signs it.

**Not in this brief:** the 360 swept quote records (they wait on Cowork's idea headings), the 72 misfits (they wait on your drift report), anything on the YouTube channel.

OWED BACK: one DONE in TO Chat naming each check's acceptance count and the quote page's new text as read from the build site.

*No em or en dashes in this file; checked before writing.*
