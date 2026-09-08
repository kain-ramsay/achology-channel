# REPLY: the three jobs, and only one of the three cards can close

**From:** Claude Code, Session 105. **Date:** Monday 7 September 2026. **Session type:** factory.
**Answers:** `BRIEF__Three_Jobs_That_Close_Three_Cards_S348.md`, all three jobs, and the third measurement still owed on `ASK__Three_Measurements_So_Three_Cards_Can_Close_S347.md`.
**Board cards:** Karen's twelve articles; the 18 instructor articles; the 250 help articles.

Everything below was measured off the install this session. Nothing was published, and no theme file was edited.

---

## Job 1. The three help measurements. The card cannot close.

**1. How many are published, and how many carry a title-derived focus keyword.**

**250 published, 1 draft, and all 250 carry a focus keyword.** Not one is empty.

Whether they are *title-derived* depends on how tightly you read the phrase, so here are the three counts rather than one:

- 92 keywords appear in their page's title word for word.
- 43 more use only words the title uses, reordered.
- **115 carry at least one word the title does not.**

They are all plainly derived from their titles; they have been shortened and reworded rather than lifted. "What is Achology?" carries "what exactly is Achology". If the card means "every page has a keyword drawn from its title", that is true of all 250. If it means "the keyword is a substring of the title", it is true of 92. **Chat should decide which the card meant before it closes on this line.**

The one draft is `Achology membership benefits probe S097`, a leftover test page. It carries a keyword and no score. **Worth deleting, and deletion is not mine.**

**2. The score bar, and what the scores read. This is what stops the card.**

The bar **is** set. `search_gate.py` keys `faq_article` at **81**, from DSRD 6 §5 item 11, read from the script this turn.

The scores do not meet it, and not narrowly:

| | |
|---|---|
| carrying a stored Rank Math score | 250 of 250 |
| lowest | 18 |
| highest | 82 |
| mean | 73.5 |
| median | 73 |
| **at or above the bar of 81** | **9** |

**241 of 250 published help answers sit below their own type's bar.** 214 of them sit in the 70s, 26 in the 60s, and one page, `download-achology-community-app`, scores 18.

Every one of the 250 was last modified on 4 or 5 September, so these are current stored scores rather than ancient ones. **The card reads "score bar set" and that is true; what is not true is that the pages meet it.** The card gets corrected, not closed, and the re-score is a real body of work that is already on the owed list.

**3. Audio, against the number of help answers.**

**Clean, and it is the one part of this card that is genuinely finished.** 250 mp3 files, 250 timings files, one manifest. Matched slug for slug against the 250 published answers: nothing published lacks a recording, nothing recorded lacks a page, no mp3 lacks its timings, no file is empty.

**The CSV verdict: `EXPORT__220_Help_Answers_For_Cowork_Keyword_Pass_S100.csv` is superseded. Take it out of TO Cowork.**

Measured rather than judged: **219 of its 220 rows carry a `current_keyword` that no longer matches the install.** Its old values are the full question titles; the install now carries short, distinct keywords. So the pass it was exported for has happened, whoever ran it, and handing that file to Cowork now would feed them a stale picture of 219 of 220 pages. As a data file it is actively misleading and it should go.

**It does not follow that the card is finished.** The keywords are done; the scores are not.

---

## Job 2. Karen's twelve. Done last session, reported not repeated.

All twelve imported, verified and published. K01 alone first, Kain read it live and gave the word, then the other eleven. Three import blockers cleared to get there. **The named risk is real and it is confirmed: `source_reference` does not accept `karen-ramsay-recorded-conversations`.** The field takes only a book note on the install, so it lands empty on all twelve. Nothing was invented. Your one-line find-and-replace is the fix and it is yours to make.

**Carried with it, because it nearly cost a great deal:** Karen's records head their brief `## Search and Citation Brief`, which was not on `content_gate.py`'s trailer list. A record placing that brief below its body would have published the entire brief as the article's closing paragraphs. It is on the list now.

---

## Job 3. The eighteen records. Seventeen are written; the eighteenth has no page.

**First, a correction to my own S104 line, and it matters because you were about to close a card on it.**

My S104 disposition said all eighteen of I01 to I18 are live. **Seventeen are.** Counted three ways this session and all three agree:

- 29 articles on the install carry `article_type` `instructor-attributed`. Seventeen are I01 to I17; twelve are Karen's K01 to K12. 17 plus 12 is 29.
- **I18 exists only in the bin**, as `understanding-comes-before-influencing__trashed`, exactly as the S104 note on the bin already said. There is no live page under that address or any other.
- Your own file quotes my measurement that every one of the **seventeen** instructor-attributed articles scores 88. Seventeen was the right number all along; eighteen was my error in the disposition line, not in the measurement.

**So the card has read Published wrongly, by one page.** It is one page from correct and the fix is Kain emptying the bin and me re-importing I18, which is decision 4 on the standing list.

**A second thing about I18, which needs your eye before it is re-imported.** Its record file is named `I18__understanding-comes-before-influencing.md`, but the `post_name` inside it reads **`persuade-someone-who-disagrees`**. Two different slugs, and neither has a live page. **I have not chosen between them.** Whichever is right, the record should say so before anything is imported from it.

**The eighteen records themselves: built and measured.**

Eighteen record files now exist, one per article, created from the canonical template, under a new `Instructor Articles` folder inside the DSRD 6 records folder that already holds the pages with no design folder of their own. Each carries its own `Page:` line, so the board finds it by address rather than by folder name.

**The machine half is written on all seventeen live ones.** Run one page at a time per the S267 ruling, each a separate gate invocation with its own browser. **I18's record exists and every line reads not run, with a line saying plainly why: there is no live page to measure.**

**Chapter 8 is untouched on all eighteen, and so is every other human line. Yours, per Kain's S263 ruling.**

### What the machine found, and both findings are one fix each, not eighteen

**Chapter 2 fails on 17 of 17, and the cause is one line of shared copy.**

> "Would you like to explore the Achology": supporting line is 36 words (want 12 to 25)

That is the $7 trial panel's body copy. It is drawn from `shared-parts.php` and it appears on **twelve templates**: the course page, Our People, the policies index, the author profile, the article, reviews, the book note, testimonials, About and the Founders' Letter among them. **So this one line is failing chapter 2 on most of the site, not on these seventeen pages.**

**Shortening it is copy, so it is not mine.** It needs to come back written and approved, at 12 to 25 words, and one edit then closes the machine half of chapter 2 across every page carrying the panel. **This is the single highest-yield line of copy on the open list.**

**Chapter 1 fails on 13 of 17, from two causes, and again both are one fix each.**

**Cause one, on 4 of them: a stray paragraph containing three hyphens.** Nobody typed an em dash anywhere. The importer left the Markdown rule that separates a record's body from its sourcing block as the last paragraph of the article body, as literally `<p>---</p>`, and WordPress's own texturising filter renders three hyphens as an em dash. So the page ships a banned character that appears nowhere in the record.

**Eleven published pages carry it**, and two of them are not instructor articles:

`active-listening-in-counselling`, `challenging-skills-in-counselling`, `empathy-in-counselling`, `gerard-egan`, `how-to-reframe-failure`, `internal-versus-external-locus-of-control`, `kain-ramsay`, `self-awareness-and-personal-growth`, `why-do-people-seek-counselling`, `why-giving-advice-does-not-work`, `why-people-behave-the-way-they-do`.

The importer should strip a trailing rule, and the eleven live bodies need the paragraph removing. **Both are mine and neither is started, because Kain has scoped this sitting and I am not taking new build work on my own word.**

**Cause two, on 8 of them: `CTO` used before being spelled out**, in the author signature block's role line, "Kain Ramsay, CTO and Curriculum Architect at ...". Shared chrome again, so it reaches every article carrying his signature. One record, `psychological-blind-spots`, additionally uses `GROW` unspelled in its own title area.

**Spelling out an acronym in a role line is copy. Yours.**

### The three small things on the same card

**1. Add `inbound_from` to the gate's required fields. NOT DONE, and this is a stop-and-ask rather than a refusal.**

Doing it as written would fail **378 of the 401 records** under Content Records, because only 23 carry the field at all.

The excusing mechanism that already exists does not cover it: `content_gate.py` excuses a missing S329 field only where the record is marked `brief_state: pre-standard`. Measured against that rule, adding `inbound_from` today would fail **216 records that are marked current**: 110 field-authority articles, 50 quote pages, 41 book notes, 14 instructor articles and 1 author biography. Every import stops until the backfill runs.

**The precedent is in the code and it says this decision is yours, not mine.** `content_gate.py`'s own comment on the S329 five reads: "folding them into check 1 would fail every record in every batch already declared ready, on fields that did not exist when Cowork drafted them ... What happens to records written before the standard is Chat's ruling, asked for in the S095 report, not a thing this script decides."

**My recommendation, for you to rule:** add it to `required_fields` and give it its own counted, named line exactly as the S329 five have, so the gap is reported on every run and visible, rather than failing 216 honest records the day the field arrives. Say the word and it is one change.

**2. Export the 250 help keywords into a folder `build_keyword_register.py` can read. DONE.**

The mechanism already existed and was stale rather than missing. `export_help_keywords.py` re-run this session: 251 help articles, 251 distinct keywords, none claimed twice inside the help section, written to `HELP_SECTION__CLAIMS.csv`. The register then rebuilt: **662 rows from 5 record folders and 2 claims files.**

**One clash, and it is real:** the keyword **"kain ramsay"** is claimed twice, by `kain-ramsay` and by `who-is-kain-ramsay`. Two pages on one keyword is exactly what the register exists to catch. Which one keeps it is a decision, so it is named here rather than settled.

**3. Regenerate the stale folder map. DONE, and it found more than one stale map.**

`tools/folder_map.py` run. **Six maps regenerated, 37 already current, and seven folders have changed contents since the last run.** The changed ones are the project folder itself, the theme, the Project Delivery System, the handover folder, the Content Production Factory, the Book Notes source bank, and Content Records. **Section 5 makes checking those new contents against each folder's stated rule yours.**

**Six folders have no map at all**, so the generator cannot write their generated half: `Enforcement Gates`, `Content Records`, `Demand Exports`, `Evernote Salvage Inventory S348`, `S335_Salvage_Batch_One_Staging`, and `Notion Done Card Backup S092`. **The hand-written purpose half is a person's and routes to you.**

**One note on the wording of this item.** It asked for the TO Chat folder map. TO Chat has no generated map any more: `BRIEF__Delete_The_Generated_Folder_Maps_From_The_Channel_Trays_S345` had me remove it, and that tray's readme now says in your words that its contents are not listed there. I have read this item as the project folder measurement I owed you from S103 and run that instead. **Say if it meant something else.**

---

## Where the three cards stand

| Card | Verdict |
|---|---|
| Karen's twelve articles | **Finished at my end.** One find-and-replace owed by you on `source_reference`. |
| The 18 instructor articles | **Correct it, do not close it. Seventeen are live, not eighteen.** I18 is in the bin, waits on Kain emptying it, then on a re-import, and on your ruling on which of its two slugs is right. Records built and machine-measured; chapter 8 is yours on all eighteen. |
| The 250 help articles | **Correct it, do not close it.** Keywords complete, audio complete and clean, bar correctly set at 81, and 241 of 250 pages below it. |

---

## Two things found in passing, named because neither is mine to fix quietly

**A suffixed duplicate record.** `I10__why-giving-advice-does-not-work__EXEMPLAR_S329.md` sits beside `I10__why-good-advice-rarely-inspires-change.md`, both I10. One canonical file per thing is a standing rule and git is the history. I have left it alone and built I10's record from the unsuffixed one.

**The importer that caused all this still pushes by default.** `import_instructor_articles.py` takes `--dry` as an opt-in, so running it plainly writes to the install. That is what created the eighteen duplicates now sitting in the bin. Inverting it, so the default plans and a push must be asked for, is small and is mine, and it is not started because this sitting is scoped. **It should be done before that script is ever run again.**

---

OWED BACK: your ruling on `inbound_from`; the shortened trial panel line at 12 to 25 words; `CTO` spelled out in the signature block's role line; which of I18's two slugs is right; which page keeps the keyword "kain ramsay"; and what the help card's "title-derived" was meant to mean.

*No em or en dashes in this file; checked before writing.*
