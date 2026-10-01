**Needs from Chat:** four things; the first is Kain's request, made in the sitting and urgent because he is ready to make the pictures now: (0) set up the Canva design project and the image map for the 36 elder article pictures (section "The picture project" below). (1) Rule whether the 36 elder articles publish at Rank Math 81 to 85 (no pictures yet) against the instructor article bar of 88: Kain said all are to be published, but that bar was ruled for pictured pages, and I have not published anything. (2) The Pending Review slug finding below: a method for the 18 held articles. (3) The leftover "Jonathon" in Dr Frost's page metadata and in the two registers.

# REPORT: the gate band, the retoned articles, the 36 elder articles and Dr Frost's key (S143, factory)

**From:** Claude Code, S143 (factory), Thursday 1 October 2026. **To:** Claude Chat.
**Answers:** `COMMISSION__The_Gate_Band_The_Retoned_Articles_And_The_36_Elder_Articles_S393`.

## 1. The gate band: done

In `content_gate_standards.json`, type `hub-question-article`: words 850 to 2,000, headed sections 3 to 8. Everything else kept. The `mindfulness-question-articles` overlay is removed, and the `--overlay` option I added to the importer earlier the same day went with it (no dead code left). The gate acceptance file prints 163 of 163 cases pass. **The lesson-number requirement:** there is no check for it anywhere in the gate code (searched), so nothing was removed; the wording lives in Recipe 8 and DSRD 2, which you wrote at S393. Recorded in the standards file as `_band_note`.

## 2. The retoned bodies: 4 of 55 differed, all four pushed

I compared the importer's own conversion of each of the 55 records with the live body, by visible words. 51 already held the retoned text (35 published, 16 held). **4 differed, all published pages: `does-person-centred-counselling-work`, `who-is-life-coaching-for`, `who-is-person-centred-therapy-for`, `why-life-coaching-is-bad`.** They were pushed by the importer's update path, status unchanged (still published), pictures kept, and read back 4 of 4 clean. Not touched: the exemplar, `how-to-practice-mindfulness` (it already matched its record), and the held where-did-life-coaching-come-from file. Note: the body update tool has no conversion rule for the `hub-question-article` folder, so it cannot do this type; the importer did.

## 3. The 36 elder articles: imported as drafts, all 36 pass the real gate, not published

- **Imported:** 36 drafts, post IDs 39652 to 39687 (Alec Wells AW, Andrew Nelson AN, Erika Nadeau ER, Gary Kennedy GK, Gabriele Tzeschlock GT, Dr Jonathan Frost JF). Read back: the only failure on every one is "no featured image", as expected; `hub` and `inbound_from` are unset, as you said. None carries a working note: I searched all 36 bodies for the "What X should confirm" lists and process text, none is on a page.
- **Rank Math, read off each page (the table of record):** 32 read 85 and 4 read 81 (mean 84.6). The four at 81 are `how-do-you-keep-going-when-youve-lost-motivation` (39673) and `what-does-it-mean-to-listen-without-fixing` (39674), both Gary Kennedy; `what-does-it-mean-to-mean-what-you-say` (39680), Gabriele Tzeschlock; and `how-can-one-person-make-a-positive-difference` (39687), Dr Jonathan Frost. I did not read the failing tests per page. The missing picture is the likely cause of the gap to the one-picture instructor articles that read 89 (DSRD 6 section 5 item 11); that is an expectation until a pictured one is read.
- **Not published, by the wall:** `publish_gate.py --clear` refuses the type. I tried all four instructor article exemplars with a DSRD 6 record (I07, I15, I03, I14): each carries one or two failing lines, so none is a closed exemplar. I did not route round it. They sit in Kain's Drafts list for the bulk publish. **Decision for Chat or Kain:** your commission says publish those that clear the instructor bar (88); none does without a picture. Kain's ruling (as you quote it) is that all are published. I have not decided it; I ask Kain in the sitting.
- **Our People pages:** Dr Frost's page already carries a section "Jonathan's writing and articles"; it should fill from the author link when the articles are published. I will read each elder's page back after publication.

## 4. Dr Jonathan Frost's key: done, with Kain's one page edit

The person page is a real WordPress page whose address must equal the registry key (the template reads the page's own slug), so the key and the page slug had to change together, and pages are Kain's alone (Harness Rule 8). Kain changed the page's title and slug to Jonathan Frost and jonathan-frost in the sitting; I then changed the key in the people registry (theme 0.707.58, deployed, three proofs agree) and in the gate's author list. The six JF records already carried `jonathan-frost`. Read back live: `/about/instructors/jonathan-frost/` shows "Jonathan Frost"; the old address returns 404 (the site is not launched).

**Left over, for Chat:** that page's search-engine title and description (Rank Math fields on the page) still read "Jonathon Frost ..." and "Jonathon Frost is a Master Achologist..."; and `KEYWORD_REGISTER.csv` and `SITE_PAGES__CLAIMS.csv` each carry a row "jonathon frost, page, jonathon-frost". Those are page metadata and register rows I did not change. Kain can fix the two fields on the page; the two rows are yours.

## A finding from the Pending step (for the 18 held articles)

WordPress empties a post's address slug whenever it sits in Pending Review, and it does it again on every update; restoring the slug while the post is Pending does not hold (I tried, under a takedown clearance, and read it back empty). The 16 mindfulness articles and `conditions-of-worth` therefore have no slug at the moment, and if Kain publishes them as they are WordPress will make the address from the title, which will not match the record. Drafts keep their slug. **Proposed method:** when their pictures arrive, I move them back to Draft and restore the slug through the importer before Kain publishes, and read every address back. I have changed nothing on them. The same applies to the two older drafts I set aside (`the-seven-levels-of-human-awareness`, and the older probe help draft).

## The picture project for the 36 elder articles (Kain's request, S143, in the sitting)

Kain has no picture ideas for these 36 and asked for suggestions. Code suggested the house style already ruled for the type, from DSRD 7 section 12.1 as quoted at S143: Kain's Magic Media long-exposure style, the same recipe as the 15 help-category images and the 18 instructor article images, the key term for each piece, orange, cream, taupe, black, grey and white only, on a plain background, landscape, no words on the picture, no portraits of the elders (their portrait and course cover already show in the article). Kain said yes, and is ready to make them now.

**Kain's words, verbatim:** "Yes, please do. Claude, um, I'm happy to do them right now. Um, and I think what would also be helpful is if when you ask chat to do this, you just ask chat, to set up the design project for me in Canva name all of the name all of the, the images so they're all kind of named and titled correctly and also just define the actual dimensions of the image because we're just going to want the dimensions to be the same size as every other image at that point you know the, the, the, the we build into the articles does this make sense".

**What Chat is asked to do, so Kain can start:**

1. **Set up the Canva design project** in Kain's Canva: one file, 36 pages, one named page per article, as for the 78. **Page size 1760 by 840 pixels**, the size of the 78 article pictures (the S392 note records them as PNG, 1760 by 840) and of the 18 instructor pictures; Code converts the export to WebP at the width the article renders (DSRD 7 section 12.3) and attaches it.
2. **Name every page** with the article's slug, and put the title and its key words on the page's name or notes so Kain sees what each picture is for. The save-as filename for each export is the slug followed by `.png`, matching the record's own `featured_image` field once it is set.
3. **Write the image map** into the record folder, one row per article (Canva page number, slug, save-as filename, title, key words), per Pipeline stage 2A. The 36 slugs and titles are in the instructor article folder of the content records (files AN01 to AN06, AW01 to AW06, ER01 to ER06, GK01 to GK06, GT01 to GT06, JF01 to JF06).
4. **Name the folder** Kain exports into, as for the 78 (a subfolder of the Article Page's Page Images), and tell Code in the channel when the set is there.
5. **Ask Cowork to set `featured_image` and `featured_image_alt` in the 36 records** (the alt text carries each record's own focus keyword), because the importer attaches a picture only from the record's own fields and the records are Cowork's. Code then converts, attaches and reads the scores again; no article's status changes.

**Not blocking:** the 36 drafts are on the install already. They can be published without pictures and the pictures added afterwards, since the importer's update path never changes a status.

OWED BACK: the picture project set up and the image map written (item 0), and the three rulings above.

*No em or en dashes in this file; checked before writing.*
