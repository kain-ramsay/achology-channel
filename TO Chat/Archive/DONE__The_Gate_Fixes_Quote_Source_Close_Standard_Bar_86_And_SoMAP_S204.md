ARCHIVED, Chat S452 (2 November 2026): the six calls accepted and section 7 placed on Backlog: Code, in the S452 ruling.

**For Chat. What this needs from you:** a read of the six calls in section 6 (each overturnable in a line), and the four findings in section 7, which are yours or wait on a session.

# DONE (Code, factory side session A of S203, numbered S204): the five gate files

Answers NOTE__Quote_Pages_Need_No_External_Source_Link_Gate_Fault_S449, RULING__Quote_Closing_Question_Has_No_Character_Band_S450, NOTE__Gate_Faults_Found_On_The_Resisting_Change_Batch_S448 items 2 and 3, RULING__The_Article_Publish_Bar_Is_86_Publish_The_Five_Anxiety_Articles_S449 item 3, and BRIEF__Add_A_SoMAP_Article_Kind_To_The_Gates_S450. Route followed: TO Chat/DONE__The_Eight_Resisting_Change_Quote_Pages_S195 section 5 (the change in `content_gate.py`, its cases in `content_gate_acceptance.py`, the suite read against the baseline).

**The proof, read this session.** Baseline before any change: `content_gate_acceptance.py` 459 of 463. Every new case was run against the unchanged gate first and read red (the S204a to S204e groups failed). After: 514 of 518. The four still failing are the four that failed at the baseline and at S195 (worked example article on disk, worked example landing page body on disk, help answer runs no other voice line, finding 13). New: `vault_gate/vault_gate_acceptance.py`, 11 of 11.

**Commits.** Project, 9714d68a (the gates, their tests, the standards file, the records folder), pushed. Theme, b2b9d65f (`search_gate.py` alone, a gate tool; no template touched, nothing deployed), pushed. The skill's two edited lines were taken into the project by the 14:19 autosave of 1 November before the change set's commit.

## 1. The quote page's source link (NOTE S449)

On quote-page the line is now "the source link present: the book note or the course in the Book, or a credited study". It passes on a link in the Book (the body up to its second heading) to a book note address or a course address, or on one outside link. Cases: Q06984 as drafted passes; a course link in the Book passes; a credited study passes; no link of either kind fails; a book note link outside the Book does not stand in, and fails. Every other type keeps "external link to the source present" unchanged. The 104 round one drafts were not re-gated here.

## 2. The closing question (RULING S450)

`closing_question_chars` [79, 89] is removed from the quote-page entry and replaced by `closing_question_required`, so the body must still end on its question and no length is read. In the paragraph rule, the last paragraph under "A Question That Deserves an Honest Answer" (or the S356 wording), ending on a question mark, is outside the rule; the context paragraph above it stays inside. **The owed gate run on `vault_gate/briefs/quotes_r1_helping/rewrite/hand/Q06984__helping-is-about-the-person.md`:** "paragraphs of 3 to 6 sentences" PASS (its p2 printed as excused, "(S450) the closing question line"), and no character band line is printed. The record went from 6 fails to 3, and the 3 left are the record's own, in section 7.

## 3. The gate faults (NOTE S448 items 2 and 3)

- **Item 2.** The gate now finds `000__THE_ACHOLOGY_CONTENT_STANDARD.md` by its own name: beside the gate first, else by walking three levels down from the folder above the gate, never taking a copy under an Archive or the Data Labs Handover folder. This replaces the two written routes, the pack's folder 03 and the Newsroom's Working Papers. Cases: a Standard moved to a folder no route names is found, one beside the gate wins, an archive or pack copy is never taken. **Not proved on the iMac Pro**, because this session runs on iMac 4. The line to read there is "stances field present and valid".
- **Item 3.** The course-named-once label now reads "quote page: the course named once only (S429)". `FIXED_FORM_PROVENANCE` is renamed `RETIRED_PROVENANCE_FORMULA`, and its paragraph-floor excuse now holds only on a record dated before 27 October 2026, the retirement. A newer one-sentence formula paragraph fails. The S357 case that proved the excuse is now dated 20 October so it proves the same thing. The full course name in link text is S446's and was not touched.

## 4. The article bar is 86 (RULING S449 item 3)

`search_gate.py` (`score_bar_for`) now holds post types article, book_note and quote to 86, and its printout names contentHasAssets and lengthContent as out of scope. The old 88 (book notes, quotes, instructor articles), 89 (field authority) and the site-wide 90 no longer reach any article kind. The `rank-math-90` skill's success test now reads 86, names the two tests and the article kinds, and keeps a page's own bar for anything that is not an article; the DSRD 6 pointer line names the S449 bar beside it. The skill file is copied to Kain's Desktop under its own name. Cases: each article kind reads 86, a page reads 90, a Help answer 81, and the skill text carries both tests.

## 5. The somap-article kind (BRIEF S450)

- **Records:** `Content Records/somap-article/`, holding only its `000__WHAT_IS_IN_HERE.md` (the gate's corpus skips 000__ files).
- **Content gate:** a `somap-article` entry. It has the four shapes in `shapes`, carried in the record's `somap_shape`: the shape must be one of the four, and its band is the printed guide (a NOTE, as on every article). It uses the shared banned, flagged and watched lists. It adds five FAILs on this kind only: no sentence over 40 words, no course link, no price, student count or rating, no helper or helpers outside "The Skilled Helper" (body, title, search title, description, excerpt), and no practitioner referring anyone on. The word "referral" alone prints a NOTE for the checker. Stances are one to three SoMAP stances, read live from the pack's Stances folder. The pack is found by its own file name, never a route. Cases: a short record of each of the four shapes passes the whole gate, and its guide is that shape's own. Each rule fails on its planted fault (helper in the body, helpers in the title, refer the client on, 41 words, a course link, a price, a student count, a rating, no shape, an unknown shape, an Achology stance, four stances). The Skilled Helper passes, and an Achology quote page is not read by the helper line.
- **Vault gate:** kind `somap-article`, with no table in 00 THE MAP. Its brief opens with The Shared Road and then the SoMAP Article Pack, read from the SoMAP project folder and checksummed by path; Achology's article pack is not in it. Each page brief carries its SoMAP stances from the pack's folder, and `check` reads them at their own paths. Cases: `build --kind somap-article` builds a brief for a test pages file (in a temporary briefs folder, deleted, so no real batch or titles file is touched). The pack's words and both named stances are in it, `check` is clean, a changed stance makes it stale, and an Achology stance holds the page.
- **Red for the vault gate is read, not replayed.** `vault_gate.py` had never been under git, because the ignore rule takes only the Machine's top-level scripts. So its earlier state cannot be run again. The red is the code as read this session before the change: KINDS had no somap-article and build refused any unknown kind. Both vault gate files are now tracked, added by name.

## 6. Six calls Code made, each overturnable in a line

1. SoMAP required fields: the hub question article's list less kh_category, kh_tag, kh_tag_order, lead_tag, destination_course_name and destination_course_url, article_type and source_type, plus somap_shape and stances.
2. The SoMAP byline key is `somap` (the pack: "The byline is SoMAP itself").
3. SoMAP takes the full eight-part Search and Citation Brief.
4. The word bands are guides, a NOTE, as on every article; only the shape itself fails.
5. Seven Beliefs pages share the article post type, so they read 86 too; author biographies keep 89 (the ruling does not name them).
6. The retired formula's excuse is dated by the record date against 27 October 2026.

## 7. Found, not changed (outside this job)

- `content_gate_fixtures.py` cannot run. Its pilot path still points at Content Records inside The Machine, which was moved at S434. And two of its word list checks are broken against the Standard: `banned_always` carries "structured training", which Part 16 does not, and `machine_tells_always` parses the S450 "holds" sentence as three items. Both were there before this change; this session edited no word list.
- Q06984's three remaining fails are the record's own: it is not signed, "Empathy" is not a stance in the map, and one seven-word run is shared with CQ018-087-1 ("be honest with yourself for a moment").
- The API worker's quote prompts (`api_worker.py`, `fix_quote_pages.py`) still tell writers the course goes "in the formula sentence". They are writing instructions, not gate labels, and the worker stands down (NOTE S438), so they were left.
- A folder was added (`somap-article`). The folder map generator was not run, since it writes outside this job's files. It waits on the next session that runs it.

OWED BACK: nothing from Code; sessions B, C and D can import against the gate as it now stands.

*No em or en dashes in this file; checked before writing.*
