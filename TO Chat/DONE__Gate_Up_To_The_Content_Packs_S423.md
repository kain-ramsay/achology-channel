Needs from Chat: one ruling (change 6, the proposal below) and your eye on three findings at the foot. Everything else is done and proved.

# DONE: the content gate brought up to the content packs and the signed gate briefs (Code, factory session S168, 15 October 2026)

**Answers:** BRIEF__Bring_The_Gate_Up_To_The_Content_Packs_S423 (changes 1 to 10), BRIEF__Two_Gate_Changes_For_Workbooks_Standard_Version_13_S412, BRIEF__Six_Gate_Gaps_From_Round_Four_And_The_Glasser_Quote_Push_S409 (job 1), BRIEF__The_Gate_And_Publish_Tool_Brought_To_Standard_Version_9_S405, HANDOFF__The_Help_Line_Is_Dropped_Everywhere_S420, ASK S424 and NOTE S425 (Standard Version 25 and 26), ASK__Workbook_Learn_Becomes_Three_Pages_S421 (questions 2, 3, 6 on the gate).

**Proof:** `content_gate_acceptance.py` 264 of 264 cases pass (was 176); `content_gate_fixtures.py` 43 of 43 hold (it was already broken by the pilot's rework, now re-anchored). Commit 58f2f877 and the commits after it, pushed.

## The ten changes of the S423 brief

1. Quote page band 800 to 1,000; the S388 heading exception no longer read by the gate (its block is renamed `withdrawn_S422_...` and kept as the record of the ten slugs).
2. Book note: the five DSRD 9 section 32.7 headings locked (including the multi-author "Authors’" form); the old five kept as a dated fallback (key `book_note_headings`, S423): a NOTE before 13 October, a FAIL on or after.
3. Exception (q): a link on an approved DSRD 5 section 9 nickname passes at any length, on every date.
4. Exception (o): on `seven-beliefs-series` the Previous and Next lines are the series block and are excused.
5. Reading ease is scored on the teaching only (Sources list left out) and is a NOTE, never a FAIL (Version 21).
6. **Not built, proposal for your ruling:** records rebuilt from an old page that keep the type `field-authority-article` (what-is-counselling, learned-helplessness) FAIL "content type is not retired". Smallest fix: the retired-type line passes when the record carries an `old_address` (it is a rebuild of a live address, Standard 17.1 item 21), and stays a FAIL for a record with none. One line in the gate. Say yes and I build it.
7. Hero lengths: title 50 to 60 and subtitle 150 to 170 as NOTE lines on every Knowledge Hub type. The subtitle the templates read is the Rank Math description (the excerpt if empty); the Standard caps that description at 155, so 156 to 170 would break Part 2 rule 3, and the NOTE says so.
8. Version 21: three to six sentences; reading ease a NOTE; an article's one-question closing paragraph is excused the floor and the count (exception Part 6 rule 11).
9. Paragraph words are a target and never a fail: a NOTE for any paragraph over 150 or under 45 words. Sentence count 3 to 6 and no one-sentence paragraph still FAIL.
10. The word "technique": a NOTE per paragraph that uses it, skipping quotation marks, the Sources list and the fixed definition.

## Workbooks (S412 and S421)

Job 1: "In Achology's view" and five like phrases, once at most in a workbook; two FAIL, each sentence printed (dated S412). Job 2: the seven expected fails print as NOTE and say they would otherwise fail; a real fail still shows. Landing page band is now the hard 350 to 450 (S411); the whole-workbook band is the guide 2,200 to 3,000; Hook, Book, Look, Took as a heading or label FAIL in a workbook.

## The six gaps (S409) and the Standard Version 9 brief (S405)

S409 item 1 (the seven-word shared run) is a FAIL on a record dated on or after 6 October, a NOTE before, with the brief's exclusions: the fixed lines read live from the Standard (eighteen word lines, the technique line, the cycle line, the Part 14 example), quotation marks, italics, the Sources and Related questions lists, course names and nicknames, a copy of the record itself. Item 2: the over-40 line already counted a link's words (proved with a 47-word case); it stays a NOTE because the Standard marks it a human rule. Item 3: the description's first words already print on the "voice: meta description opens on the answer" line. Item 4: title case FAIL dated S409 (Help titles: sentence case, flagged only when every ordinary word is capitalised). Item 5: numbers of ten and above in words FAIL dated S409. Item 6: same as change 3.

S405: job 1, `course_autolink.py` never links a full course name (every full name or card title is claimed as plain text first; only a section 9 short name standing alone is linked): **Chat to correct the two DSRD lines**. Job 2: `--signing` (or ACHOLOGY_GATE_SIGNING=1) holds every dated line and ends the earlier-record allowances. Job 3: (q). Job 4: no keyword in any heading is a NOTE; "the WHO" matches "World Health Organization"; the vault is looked for in the usual places and the line says where it looked (it is not on this machine); the openers "Below, you'll find" and "By the end of this page" are caught; "actually" counts the title; the shortest-paragraph line skips Sources items. Job 5: Achology named in a biography's title, description or excerpt FAILS; on other types a sentence with Achology, a verb of influence or teaching, and a personal name FAILS (dated S405). Job 6: `Archive/000__THE_ACHOLOGY_CONTENT_STANDARD__Version_8_S405_signed.md` written from git. Version 10 and Version 7 are not in git (Versions 8, 9, 11, 13 and later are); those two cannot be written.

## The help line (S420)

The gate carries no help line check and no `help_line` field; there was nothing left to remove. An old `help_line` field would print as "fields not in the contract" and fail nothing.

## Also built this session, from the S407 follow-up brief

A record may carry a `partial_edit` field naming the check keys a ruled edit touched; those lines are measured by the edit's date and every other dated line by the record's own post_date (Version 11, item 2). Acceptance red and green. Nothing carries the field yet, so nothing moves until Cowork or Code puts it on the swept quote records.

## Three findings, for Chat and Kain

1. **Rank Math 36 on grow-self-awareness.** The test "keyword in the SEO title" is worth 36 points on that page and scores 0, because the new keyword "grow in self-awareness" is not in the SEO title. Every other test is at or near full. Putting the phrase anywhere in the SEO title lifts it to about 90. The title and address are Kain's; the SEO title is a separate field. The page was 94 before the signed body went on.
2. **The 296 "old quote card set" files are not dead weight.** 275 of them are the live Download file of 275 quote pages (`card_download_file`), still on the old card design; only 21 were unreferenced and are now in `media-holding/2026-10-15-unreferenced-quote-cards` on the server with a checksum manifest. Moving the other 275 would break 275 Download buttons. They need re-baking at the current design (a theme-session job, line added to the theme queue), after which the media check stops repeating.
3. **The gate now fails the signed Mental Health pieces on shared seven-word runs** (S409 item 1 as written). Six of nine signed records carry it, each naming the other record. It is the brief as signed; if the runs are ordinary English rather than copying, the line is one setting (`corpus_runs_fail`, in the shared block of the standards file) to turn back to a NOTE; tell me and I flip it.

OWED BACK: Chat's ruling on change 6; the DSRD correction on the autolink.

*No em or en dashes in this file; checked before writing.*
