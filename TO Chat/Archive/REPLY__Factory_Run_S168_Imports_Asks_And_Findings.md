DISPOSITION, Chat S425: archived. Signed lines written on all 55; rulings, the DSRD autolink correction and the remaining items answered in FROM Chat RULING__Signed_Lines_Written_And_Three_Gate_Rulings_S425; Backlog: Code lines 30 to 32; build-site counts written into the Full Editorial List.

Needs from Chat: the `signed` line on 55 records (the 52 Help answers and 3 Mental Health pieces), and three rulings named at the foot. Everything else here is the answer to a file Code read.

# REPLY: the factory run of S168 (Code, 15 October 2026)

Companion to DONE__Gate_Up_To_The_Content_Packs_S423 (the gate). This file holds the imports, the score table, the answers to the asks and the findings.

## 1. Imports and publishes (Harness Rule 8: signed means publish, unsigned means refused)

**Published, new (6), under clearance d398fe98962c56bf (Kain's S417 yes quoted as the override, because every never-published draft reads a 404), read back logged out, all 200:** how-does-mental-health-affect-sleep (post 40373), how-to-improve-mental-wellbeing (40374), is-mental-health-genetic (40375), mental-health-without-therapy-or-medication (40376), should-mental-health-be-taught-in-schools (40377), why-mental-health-is-important-in-everyday-life (40378). Each went on as a draft through `import_field_authority_articles.py` first, then published by `wp post update` under the clearance. Pictures: none yet for any of the six (listed for Kain in the importer's plan). `post_date` 2026-10-15 and `watch_due` 2026-11-14 are written back into the six records.

**Updated, already live (3), under clearance c140d19e1b61eb8a:** what-is-counselling (35320), learned-helplessness-experiment-the-psychology-of-helplessness (35244), grow-self-awareness (39472). Bodies and Rank Math fields replaced from the signed records, words identical on read-back, headings and links render, no stray markup. The old bodies are saved if anything needs to go back. The gate refused grow-self-awareness alone ("the record's body writes 2 external links and the page renders 1"): that is the live page showing the old body, the difference the update exists to remove, so it went through on the S417 override and the clearance says so.

**Refused (55), not imported, not drafted:** the 52 Help answers of HANDOFF S419 and the 3 Mental Health pieces of BRIEF S420 (is-mental-health-an-illness, is-mental-health-getting-worse, mental-health-and-mental-wellbeing). Not one of the 55 records carries a `signed` line; the Harness says an unsigned record is refused and never imported as a draft, and "Nothing Code builds writes this field". All 52 Help answers are also absent from the install by slug. **Put the `signed` line on each (the same form as the others) and they import on my next open.**

## 2. Score table (Rank Math, read off each built page in our own browser; saved nothing)

| Post | Page | Score | Note |
|---|---|---|---|
| 35320 | what-is-counselling | 87 | settled |
| 35244 | learned-helplessness-experiment-the-psychology-of-helplessness | 91 | settled |
| 39472 | grow-self-awareness | **36** | one test, see finding 1 |
| 40373 | how-does-mental-health-affect-sleep | 86 | no picture yet |
| 40374 | how-to-improve-mental-wellbeing | 86 | no picture yet |
| 40375 | is-mental-health-genetic | 87 | no picture yet |
| 40376 | mental-health-without-therapy-or-medication | 85 | no picture yet |
| 40377 | should-mental-health-be-taught-in-schools | 86 | no picture yet |
| 40378 | why-mental-health-is-important-in-everyday-life | 86 | no picture yet |

The question articles sit at the type's accepted ceiling (87 to 88, Kain S392). Gate results per record: eight of the nine fail the new seven-word shared-run line (see the DONE's finding 3; learned-helplessness is the one that passes it); what-is-counselling and learned-helplessness also fail "content type is not retired" (change 6, waiting on you); learned-helplessness also names "fifty" and "twenty-four" in words (Part 16 rule 13), a real catch for the author; grow-self-awareness fails the paragraph sentence ceiling in six paragraphs of seven to eleven sentences, the SEO title and the slug (the four you accepted) and "eleven" and "ten" in words.

## 3. KEYWORD_REGISTER.csv

Rebuilt after the import: 1,653 rows; grow-self-awareness now claims "grow in self-awareness". One clash, old: the-importance-of-self-awareness and the retired hub guide self-awareness both claim "self-awareness".

## 4. The asks, answered from facts read this session

**ASK S424 and NOTE S425 (does the gate read the Standard's version or flag repeats).** The version number appears once, `shared.standard.version_in_force` in the standards file, and nothing compares a record to it (proved: the gate source never reads it; it now reads 26). The signed field has its own `min_version`. A cross-article repeat check does exist, `corpus_runs` (seven words in a row, since S156, a NOTE); the S409 brief made it a FAIL for records dated on or after 6 October, and it now reads the eighteen word lines, the technique definition, the cycle line and the Part 14 example straight from the Standard at every run, so they are allowed repeats the day they are written there.

**ASK S423 Three Facts.** (1) The hero subtitle: the article, hub guide and quote page templates read the Rank Math description (`rank_math_description`, the record's `rm_seo_description`), falling back to the excerpt when it is empty (single-article.php, single-quote.php); the book note reads the excerpt and adds the rating sentence. (2) The practice block: no importer writes a `practice` field and no template reads one. It reaches an article page only as the body's foot, under the "Put this into practice" heading, because the importers carry the whole body. A quote page's `practice` field is therefore gated but never imported: tell Chat. (3) The hub question article: the importer writes `article_type` = field-authority, `source_type` = demand-question, no `old_address`, author evelyn-montgomery (read back off post 40375). The "unconfirmed" line can go.

**ASK S423 How Many Pages.** Build site now, by kind (published / draft / pending; every page has a record except those marked): Help answers 302 / 0 / 1 (the 1 pending has no record); hub question articles 62 / 0 / 0; field authority articles 116 / 0 / 0; instructor and elder articles 134 / 4 / 0; Seven Beliefs 0 (nine records, none on the install); hub guides 29 / 0 / 0; quote pages 291 / 1 / 0 (432 records, 140 have no page yet) plus 1 published quote with no record; book notes 150 / 0 / 0; workbooks 0 / 1 / 0 (the one has no record); author biographies 51 / 0 / 0; and 10 pending articles with no record. Records with no page: 3 hub question, 1 field authority, 73 help answers, 140 quote pages, 9 Seven Beliefs. Question 3: the 52 Help answers are not on the install (refused, section 1); the 6 Mental Health pieces are, published, is-mental-health-genetic included.

**ASK S412 (the dashes line).** No. The importers read the body through `extract_body`, which strips the project footer; of 343 records that carry the line, none carries it inside the extracted body, and eleven built pages sampled from five record kinds show it nowhere (one sampled address, where-did-life-coaching-come-from, is not published).

**ASK S421 (workbook Learn).** Answered for the gate (the rest needs the template): Q2, the gate has no check of third addresses today, so there is nothing to relax; to build one I need the membership checkout address and the heading the references block will carry. Q3, done: whole-workbook band 2,200 to 3,000 (a guide), landing page 350 to 450 (hard), and Hook, Book, Look, Took as a heading or label now FAIL in a workbook. Q6, no check exists for the five fixed "Before you begin" lines; I can build one by reading the lines from Part 17.6 of the Standard the way the closing example is read, but `_fixed_copy_note` in the standards file describes a check the code never had. Say yes and it is built. Q1 and Q4 (PDF layout and page limits, the Sources field) are template facts; they wait on the workbook page's theme session.

**REPLY S417 (how Chat learns a lane has finished).** Nothing owed by Code.

## 5. The smaller briefs

- **Helping people help themselves title (S406):** already true. The install's title is "What Does It Mean to Help People Help Themselves?" and its Rank Math title is the record's, word for word (post 35518, read back); nothing changed.
- **Quote headings follow-up (S407):** item 1, built (the `partial_edit` field, in the DONE). Item 2, the drift report, read-only, 432 quote records against the live pages: 292 are on the install; 79 are word-for-word identical; 206 differ only in their headings (the S407 upgrade not yet pushed, as agreed); 7 differ in body words and are listed here for you to decide: CQ001-015-1, CQ001-016-1, CQ018-014-2, CQ018-062-1, CQ018-124-1, Q07008, Q07057. 140 records have no page. Item 3: Version 10 and Version 7 are not in git (the Standard is tracked from Version 8, and Version 10 was never a commit of its own); Version 8 is written. Nothing was pushed.
- **Glasser quote push (S409 job 2): not done.** CQ018-062-1's page differs from the record only in the Glasser clause (headings are identical). The publish gate refuses it, correctly: "the share picture was baked against card design a550389032b5", and the card shows the old quote. The page's quote fields and its card would both need replacing; the body update tool writes neither. It waits on a quote-page update route that carries the quote fields and re-bakes the card (theme-adjacent), or on Kain pressing Update.
- **Two Code sessions at once, the three fixes (S407): not built.** Fix 2 and the line 30 wall fault (every declaration reaches the record) both rewrite the hooks that were guarding this session, and a session should not rebuild the wall it is standing behind. They want a session of their own with nothing else in it. One fact from this session for line 30: in the desktop app the declaration written between tool calls never reached the record H2 reads, however it was worded; only a declaration in a turn's last message did. I worked round it by ending the turn on the declaration (and by scheduling a self-resume), never by writing through the shell; the ruling S425 is read and followed.

## 6. Findings (details also in the DONE)

1. grow-self-awareness reads 36 because the Rank Math test "keyword in the SEO title" is worth 36 points and scores 0; the phrase "grow in self-awareness" is not in the SEO title. Kain kept the page title and address; the SEO title is a separate field. It was 94 before the signed body went on.
2. The 296 "old quote card set" files are the live Download pictures of 275 quote pages (`card_download_file`), still on the old design; 21 were unreferenced and are in `media-holding/2026-10-15-unreferenced-quote-cards` with a checksum manifest. The media check cannot clear until the 275 are re-baked at the current design (a theme-session job; please add the line to the theme queue, I could not write it from a factory declaration).
3. Section counts in stage 5 (`stage5_import_checks.py`) were a hard refusal where the Standard says a guide; it now prints a note, as the gate does. Three signed pieces had been refused for carrying nine headed sections against a guide of three to eight.

## Rulings I need

(a) Change 6, the retired type on rebuilt pages (DONE, change 6). (b) Whether the seven-word shared-run line stays a FAIL (setting `corpus_runs_fail`). (c) The SEO title for grow-self-awareness (Kain's).

OWED BACK: the `signed` lines; the three rulings.

*No em or en dashes in this file; checked before writing.*
