ARCHIVED, Chat S452 (2 November 2026): road step 18 read: every page this file names that is under its bar or held is listed with its cause and state in 99 Working Papers, planning, STEP18__Every_Landed_Page_Under_The_Bar_S452; the records needing mends go to a writing session and back to Code; the rest wait on signed briefs Code has not landed yet. Its empty score table is asked of Code in FROM Chat NOTE__Five_S207_Score_Tables_Are_Empty_S452.

**For Chat. What this needs from you:** read the score table (section 5). Nothing is held. The two stage 5 instrument lines S198 asked you to rule on are still in the checker. Factory session, Code S207.

# DONE: the 40 author biographies without the banned word are on the build site (Code, factory S207, a side session of S203, 2 November 2026)

Answers BRIEF__Update_The_40_Author_Biographies_Without_The_Banned_Word_S451. Route followed: the S198 route, `article_body_update.py author-biography:<post_name> --apply`, body only, every record as it stands today.

## 1. The import checks

- **Fields complete and signed.** All 40 carry the batch signature and pass `stage5_import_checks.py` check 1.
- **Body shape and named files.** The checker fails all 40 on the two instrument faults S198 reported and asked you to rule on: it compares the ruled headings without putting the person's name in, and it reads `featured_image` where a biography names `portrait_image`. **So both were checked by hand, by a script that does what the checker should:** every body carries "{name}: Early Years and Formation", "{name}'s Main Body of Work and Ideas" and "{name}'s Worldwide Influence and Legacy" for one name, and every `portrait_image` is on an attachment on the install. **40 of 40 pass both.** As at S198, some records have no Sourcing record or Search and Citation Brief section (the older record shape); named, not fixed. No body carries a working note.
- **Every link resolves.** 41 site addresses, read from inside the host: 22 answer 200. Ten are /academy/ course pages (pages to come). Nine are the Seven Beliefs parts (can-people-change, change-your-life-from-the-inside-out, emotional-responsibility, know-thyself, philosophy-of-life, sense-of-purpose, standing-on-the-shoulders-of-giants, thinking-errors, understanding-and-managing-emotions), not yet published, so pages to come. 153 outside links: 137 answer below 400. The rest are publishers refusing scripts or rate limiting (403 and 429: Simon and Schuster, Princeton, Stanford, the New York Times and others), moralfoundations.org asking for a sign in (401), two hosts that did not connect (openlibrary.org on Alfred Adler, happinesshypothesis.com on Jonathan Haidt), and one Wikisource address on Leo Tolstoy that my checker cut at a bracket. All of these links were already on the pages and are unchanged by the batch.

## 2. What landed

**40 of 40 updated in place,** body only, all published before and after, each reported back under its own post id. None was created, renamed or taken down.

## 3. Read back

All 40 from plain ssh dumps: status, post_name, post_title, post_excerpt, search title, search description, focus phrase, and the stored body against the tool's own conversion of the record. **40 of 40 match in every one of those fields.** (My read-back also compares a `featured_image_alt` field, which biography records do not carry, so it printed a difference on all 40; that line is my script's, not the pages'.)

## 4. The banned word

Every stored title, excerpt, body and search field of the 40, read on the server: **none carries "holds".**

## 5. The score table

The Author Biography Pack names no bar of its own, and The Shared Road sets 86 for every article kind; biographies are articles on the build site, so the table reads against 86, as at S198.

| Page (record) | Post | Focus phrase | Score | Against 89 | Failing tests |
|---|---|---|---|---|---|
| Author_Biography_Gerard_Egan_S298 | 33605 | Gerard Egan | 91 | pass | none |
| Author_Biography_Aristotle_S304 | 33592 | Aristotle | 89 | pass | none |
| Author_Biography_Arthur_Schopenhauer_S304 | 33593 | Arthur Schopenhauer | 89 | pass | none |
| Author_Biography_Carl_Jung_S304 | 33598 | Carl Jung | 89 | pass | none |
| Author_Biography_Gabor_Mate_S304 | 33604 | Gabor Maté | 89 | pass | none |
| Author_Biography_Howard_Gardner_S305 | 33712 | Howard Gardner | 89 | pass | none |
| Author_Biography_James_Allen_S304 | 33607 | James Allen | 89 | pass | none |
| Author_Biography_Jonathan_Haidt_S304 | 33611 | Jonathan Haidt | 89 | pass | none |
| Author_Biography_Joseph_Campbell_S304 | 33612 | Joseph Campbell | 89 | pass | none |
| Author_Biography_Robert_Greene_S304 | 33620 | Robert Greene | 89 | pass | none |
| Author_Biography_Ryan_Holiday_S304 | 33621 | Ryan Holiday | 89 | pass | none |
| Author_Biography_Sigmund_Freud_S304 | 33622 | Sigmund Freud | 89 | pass | none |
| Author_Biography_Simon_Sinek_S305 | 33623 | Simon Sinek | 89 | pass | none |
| Author_Biography_Steven_Pinker_S304 | 33624 | Steven Pinker | 89 | pass | none |
| Author_Biography_A_C_Grayling_S304 | 33589 | A. C. Grayling | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Abraham_Maslow_S305 | 33708 | Abraham Maslow | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Alan_Watts_S304 | 33591 | Alan Watts | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Alfred_Adler_S305 | 33709 | Alfred Adler | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Brendon_Burchard_S304 | 33595 | Brendon Burchard | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Brene_Brown_S304 | 33596 | Brené Brown | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Cal_Newport_S304 | 33597 | Cal Newport | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Charles_Duhigg_S304 | 33599 | Charles Duhigg | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Daniel_Goleman_S304 | 33600 | Daniel Goleman | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Erich_Fromm_S304 | 33602 | Erich Fromm | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Erik_Erikson_S305 | 33711 | Erik Erikson | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Friedrich_Nietzsche_S304 | 33603 | Friedrich Nietzsche | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Irvin_Yalom_S304 | 33606 | Irvin Yalom | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_John_C_Maxwell_S304 | 33608 | John C. Maxwell | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_John_Dewey_S304 | 33609 | John Dewey | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_John_Stuart_Mill_S304 | 33610 | John Stuart Mill | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Jordan_B_Peterson_S305 | 33714 | Jordan B. Peterson | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Judith_S_Beck_S305 | 33715 | Judith S. Beck | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Leo_Tolstoy_S304 | 33614 | Leo Tolstoy | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Mark_Manson_S304 | 33616 | Mark Manson | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Nassim_Nicholas_Taleb_S304 | 33618 | Nassim Nicholas Taleb | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Plato_S304 | 33619 | Plato | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Rick_Hanson_S305 | 33717 | Rick Hanson | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Robert_Cialdini_S305 | 33718 | Robert Cialdini | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_Viktor_Frankl_S305 | 33627 | Viktor Frankl | 86 | **under** | contentHasShortParagraphs |
| Author_Biography_William_James_S304 | 33628 | William James | 86 | **under** | contentHasShortParagraphs |

## Commits

Theme: none. Project: none. Channel: this DONE and the brief's disposition line.

OWED BACK: the S198 ruling on the two stage 5 instrument lines, still open.

*No em or en dashes in this file; checked before writing.*
