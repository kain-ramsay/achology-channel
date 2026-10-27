**For Chat. What this needs from you:** read the score table and the findings in section 4; mend the 34 records at source (already your job by RULING__Gate_Lines_On_Signed_Words_..._S449); rule on the three pages in section 3. Factory session.

# DONE: 113 of the 147 signed book notes are on the build site; the 34 wait on their publisher link (Code, S190 factory session, 27 October 2026)

Answers BRIEF__Import_The_147_Signed_Book_Notes_S446 for 113 pages, with RULING__Kain_Lands_The_147_Book_Notes_S190 (Kain, in the sitting: "yes, please go ahead and do this claude") and RULING__Gate_Lines_On_Signed_Words_The_73_Help_Answers_The_147_Book_Notes_And_The_Five_Anxiety_Articles_S449, which confirms that reading. Every record was read as it stands today.

## 1. What reached the build site
- **113 book notes updated in place**, all still published; none created, none unpublished. Through the theme's `article_body_update.py --apply --with-seo`, after the theme deployed the S440 template at 0.707.637 (contents list and badge on "A Question That Deserves an Honest Answer"; the S190 theme queue line struck by that session).
- Body for all 113. Excerpt for all 113. Search title and description for the 32 records that carry `rm_seo_title` and `rm_seo_description`; the other 81 carry only `prod_rm_*` and the tool reads `rm_*`, so their stored search title and description were left as they were. The read back below found them already equal to the record's `prod_rm_*` values.
- No course link was written into any record by the autolinker this run; no record changed.

## 2. Checks
- **Lock 4:** `body_guard.py --signed` exit 0 before the dry run and again before the landing (1,014 records, 0 with a working note).
- **The three import checks** (`stage5_import_checks.py` with the build site's attachment file names): 146 of 147 pass all three. fierce-self-compassion fails check 3: its record names `fierce-self-compassion.jpg`, on no attachment; its page keeps the `self-compassion.jpg` cover it already shows, as your S449 ruling says.
- **The page check:** `article_body_update.py --verify` (publish_gate.rendered_faults) on a-liberated-mind: clean. Its served page carries the five headings, the practice block and Sources (as a list), and all five contents links resolve to an id in the body.
- **Read back of all 113** against their records (post_title, post_excerpt, search title, search description, focus keyword, the five headings in order, no old headline): **110 match.** Three do not, in section 3.
- **Content gate:** each page's lines that judge Kain's signed words are recorded as `exception, 2026-10-27, signed prose not reworded (Kain S190 sitting), approved by Kain`. Every line by record is in `GATE_LINES__The_147_Book_Notes_S190.csv` beside the records.
- **Lock 5:** LOCK5_PENDING

## 3. Three pages whose title or keyword on the build site is older than the record
The body tool writes neither, and the publishing wall refuses a hand `wp post update` without a clearance, so Code left them:
- free-will-sam-harris (33802): title "Free Will: Summary and Key Ideas" against the record's "Free Will by Sam Harris: Summary and Key Ideas"; focus keyword "Free Will" against "free will by sam harris".
- thinking-fast-and-slow (36559): title "Thinking Fast and Slow: Summary and Key Ideas" against "Thinking, Fast and Slow: Summary and Key Ideas".
- mans-search-for-meaning (10901): focus keyword "search for meaning" against "man's search for meaning".
**Ask:** may Code write these three through `publish_gate.py --clear` and the cleared update, or does a theme or Kain route take them?

## 4. Findings for Chat
- **71 records link their course to the full address `https://achology.com/academy/...`** rather than `/academy/...`. On the build site Rank Math counts that as an outside link, so 56 pages fail "internal link" and lose points they would keep on achology.com. A record mend (the address without the host) or nothing until go-live; your call.
- **Three records link their course to a checkout address** (`community.achology.com/checkout/...`), boundaries-cloud among them.
- **The book note ceiling is 88**, as the theme queue's S103 line says (`contentHasAssets` scores 1 of 6 for a body with no picture): 34 pages reach it with no test failing.
- `rank_math_title` on the pages stores the title without " | Achology", as it did before this import; the served title is the same.

## 5. The title ruling (owed line)
On every book note landed this session the body's first-line headline was dropped and the page title is `post_title`; no page was refused for it.

## 6. The 34 not landed
Refused by the body tool, before any write, for no outside link (DSRD 6 section 5 item 11 move 6); have-a-little-faith also has no internal link. They land the moment their records change, with no further word: a-guide-to-rational-living, a-new-guide-to-rational-living, a-path-through-the-jungle, bittersweet, brainstorm-the-power-and-purpose-of-the-teenage-brain, coming-to-our-senses, creating-minds, critique-of-practical-reason, crucial-conversations-mcmillan, emotional-leonard-mlodinow, finding-flow, getting-past-no, have-a-little-faith, keeping-the-love-you-find, linchpin, maps-of-meaning, money-master-the-game, multiple-intelligences-new-horizons, nature-emerson, noise, originals, quit, shyness-what-it-is-what-to-do-about-it, stillness-speaks, talking-to-crazy, teacher-and-child, the-brains-way-of-healing, the-happiness-project, the-maine-woods, the-origins-of-intelligence-in-children, the-republic-plato, the-way-to-love, time-and-free-will, toward-a-psychology-of-being. Until then their pages keep the S150 bodies, whose fifth contents link now points at nothing on the new template.

## 7. Tools changed (committed and pushed; no rule loosened)
- Theme d8eaf70e: `tools/book_note_import.py` repointed and reading the S440 shape; its H9 entry re-hashed after reading the whole diff.
- Project aa0dfaa9 (Kain's S190 yes): `content_gate_standards.json` book note shape to S440; `content_gate_acceptance.py` change 2 turned to the S440 fifth (the same four cases fail as before); `stage5_import_checks.py` reads a book note's cover and leaves the foot out of the body shape.

## 8. The score table: 113 pages
Read from each page's editor with score_run.py's session under `block_every_write`, nothing saved, by Rank Math's own analyser on the primary keyword (its result manager's score). 0 at 90 or above (the ceiling is 88), 34 at 88, 79 under; median 82. Every page under 90, with its failing tests and primary keyword, is in `RANK_MATH_FAILURES__Book_Notes_S190.csv` beside the records, keyed by post id. Tests failing: internal link 56 (section 4), short paragraphs 38, keyword in subheadings 4, title starts with keyword 2, keyword in title 2, keyword in first 10% 2, keyword in image alt 1, keyword in content 1.

SCORE_TABLE

OWED BACK: the ask in section 3; the 34 mended at source; your word on section 4's course address.

*No em or en dashes in this file; checked before writing.*
