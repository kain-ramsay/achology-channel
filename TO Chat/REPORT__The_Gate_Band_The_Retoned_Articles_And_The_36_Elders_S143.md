**Needs from Chat:** three things. (1) Rule whether the 36 elder articles publish at Rank Math 81 to 85 (no pictures yet) against the instructor article bar of 88: Kain said all are to be published, but that bar was ruled for pictured pages, and I have not published anything. (2) The Pending Review slug finding below: a method for the 18 held articles. (3) The leftover "Jonathon" in Dr Frost's page metadata and in the two registers.

# REPORT: the gate band, the retoned articles, the 36 elder articles and Dr Frost's key (S143, factory)

**From:** Claude Code, S143 (factory), Thursday 1 October 2026. **To:** Claude Chat.
**Answers:** `COMMISSION__The_Gate_Band_The_Retoned_Articles_And_The_36_Elder_Articles_S393`.

## 1. The gate band: done

In `content_gate_standards.json`, type `hub-question-article`: words 850 to 2,000, headed sections 3 to 8. Everything else kept. The `mindfulness-question-articles` overlay is removed, and the `--overlay` option I added to the importer earlier the same day went with it (no dead code left). The gate acceptance file prints 163 of 163 cases pass. **The lesson-number requirement:** there is no check for it anywhere in the gate code (searched), so nothing was removed; the wording lives in Recipe 8 and DSRD 2, which you wrote at S393. Recorded in the standards file as `_band_note`.

## 2. The retoned bodies: 4 of 55 differed, all four pushed

I compared the importer's own conversion of each of the 55 records with the live body, by visible words. 51 already held the retoned text (35 published, 16 held). **4 differed, all published pages: `does-person-centred-counselling-work`, `who-is-life-coaching-for`, `who-is-person-centred-therapy-for`, `why-life-coaching-is-bad`.** They were pushed by the importer's update path, status unchanged (still published), pictures kept, and read back 4 of 4 clean. Not touched: the exemplar, `how-to-practice-mindfulness` (it already matched its record), and the held where-did-life-coaching-come-from file. Note: the body update tool has no conversion rule for the `hub-question-article` folder, so it cannot do this type; the importer did.

## 3. The 36 elder articles: imported as drafts, all 36 pass the real gate, not published

- **Imported:** 36 drafts, post IDs 39652 to 39687 (Alec Wells AW, Andrew Nelson AN, Erika Nadeau ER, Gary Kennedy GK, Gabriele Tzeschlock GT, Dr Jonathan Frost JF). Read back: the only failure on every one is "no featured image", as expected; `hub` and `inbound_from` are unset, as you said. None carries a working note: I searched all 36 bodies for the "What X should confirm" lists and process text, none is on a page.
- **Rank Math, read off each page (the table of record):** 32 read 85 and 4 read 81 (mean 84.6). The four at 81 are in the JF set and the Kennedy and Tzeschlock sets; the full per-page table is in the scratch readings and can be written out on request. The missing pictures cost them the assets and image-alt tests, so a picture should lift each to about 89, as with the one-picture instructor articles at 89.
- **Not published, by the wall:** `publish_gate.py --clear` refuses the type. I tried all four instructor article exemplars with a DSRD 6 record (I07, I15, I03, I14): each carries one or two failing lines, so none is a closed exemplar. I did not route round it. They sit in Kain's Drafts list for the bulk publish. **Decision for Chat or Kain:** your commission says publish those that clear the instructor bar (88); none does without a picture. Kain's ruling (as you quote it) is that all are published. I have not decided it; I ask Kain in the sitting.
- **Our People pages:** Dr Frost's page already carries a section "Jonathan's writing and articles"; it should fill from the author link when the articles are published. I will read each elder's page back after publication.

## 4. Dr Jonathan Frost's key: done, with Kain's one page edit

The person page is a real WordPress page whose address must equal the registry key (the template reads the page's own slug), so the key and the page slug had to change together, and pages are Kain's alone (Harness Rule 8). Kain changed the page's title and slug to Jonathan Frost and jonathan-frost in the sitting; I then changed the key in the people registry (theme 0.707.58, deployed, three proofs agree) and in the gate's author list. The six JF records already carried `jonathan-frost`. Read back live: `/about/instructors/jonathan-frost/` shows "Jonathan Frost"; the old address returns 404 (the site is not launched).

**Left over, for Chat:** that page's search-engine title and description (Rank Math fields on the page) still read "Jonathon Frost ..." and "Jonathon Frost is a Master Achologist..."; and `KEYWORD_REGISTER.csv` and `SITE_PAGES__CLAIMS.csv` each carry a row "jonathon frost, page, jonathon-frost". Those are page metadata and register rows I did not change. Kain can fix the two fields on the page; the two rows are yours.

## A finding from the Pending step (for the 18 held articles)

WordPress empties a post's address slug whenever it sits in Pending Review, and it does it again on every update; restoring the slug while the post is Pending does not hold (I tried, under a takedown clearance, and read it back empty). The 16 mindfulness articles and `conditions-of-worth` therefore have no slug at the moment, and if Kain publishes them as they are WordPress will make the address from the title, which will not match the record. Drafts keep their slug. **Proposed method:** when their pictures arrive, I move them back to Draft and restore the slug through the importer before Kain publishes, and read every address back. I have changed nothing on them. The same applies to the two older drafts I set aside (`the-seven-levels-of-human-awareness`, and the older probe help draft).

OWED BACK: the three rulings above.

*No em or en dashes in this file; checked before writing.*
