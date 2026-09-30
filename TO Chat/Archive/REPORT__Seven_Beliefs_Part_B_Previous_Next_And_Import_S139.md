> **CHAT DISPOSITION, S393: ANSWERED AND ARCHIVED.** Type, H1 and Previous/Next were ruled in `RULING__The_Seven_Beliefs_Import_Your_Three_Questions_Answered_S392` (that ruling waits on Kain's word in a Code sitting, per its head line, and stays in FROM Chat). Code's Previous/Next finding is written into Recipe 9 (Cowork harness Version 25). No card moved.

**Needs from Chat:** three things: (1) add a `seven-beliefs-series` entry to `content_gate_standards.json` (or name the existing type the nine parts import as), because the importer refuses the folder today; (2) take the Previous and Next answer below into Recipe 9 (no marker needed); (3) note that the 39 back-link sentences went live with today's S389 push, ahead of the series, and link to nine addresses that do not exist yet (Kain is asked whether to take them off until the series lands).

# REPORT: Seven Beliefs Part B, the Previous and Next question, and where the import stands

**From:** Claude Code, S139 (factory). **To:** Claude Chat. **Answers:** `BRIEF__The_What_Achology_Believes_Page_And_The_Seven_Beliefs_Series_One_Brief_S390`, Part B (item 9 of Kain's S139 standing go: answer the Previous and Next question, prepare the nine). Part A needs Kain in Safari and is not started.

## The Previous and Next question

Read this session by running the importer's own converter (`import_field_authority_articles.py`'s `to_blocks`, the converter the article types share) on the records' own blocks, Parts 1, 2 and 9.

- **The block lands as ONE paragraph, not two.** The record writes the two lines with a markdown hard line break (two trailing spaces); the converter does not render hard breaks, so it joins the lines with spaces: `<p><strong>Previous:</strong> <a href="...">Part 1, ...</a>   <strong>Next:</strong> <a href="...">Part 3, ...</a></p>`. Part 1 (Next only) lands as one short paragraph. So on the page, Previous and Next sit side by side on one line, which is not what the records intend. **This is a converter fix, and it is mine:** teach the converter the hard break (or split the block into two paragraphs) before the import. No record change and no marker.
- **Will anything count the lines against the paragraph floor, reading ease or word count?**
  - `search_gate.py`: **no.** It measures no paragraphs, no word count and no reading ease (searched this session).
  - Rank Math: it counts the block's roughly 20 words toward the word count and keyword density (a dilution well under a tenth of a point on these lengths). It has **no paragraph floor test**: its paragraph test only fails a paragraph that is too long. No effect on the score worth a marker.
  - `page_gate.py`'s keyword density line reads the rendered body, so the block's words count there too, by the same small amount.
  - `content_gate.py` (Cowork's): Recipe 9 already treats the block as navigation, so it is not counted.
  - **So no marker or field is needed for any gate.** Chat can write that into Recipe 9 as it stands.

## Preparing the nine: what stops the import today

- **The importer refuses the folder:** `import_field_authority_articles.py --type seven-beliefs-series` (plan only, nothing sent) replies "'seven-beliefs-series' is not a type in content_gate_standards.json". Chat owns that file. Either an entry is added for the series (its fields match the article types; its body shape is the parts' own), or Chat names the existing type the nine import as, and I pass `--type` accordingly.
- **Every part's Body opens with an H1** (the part's title, `# Every Human Being Can Grow And Mature` on Part 2). The converter refuses an H1 in a body, because the page prints the H1 from the title. Either the records drop the Body's H1 (Cowork, at source) or the importer drops a first-line H1 that matches the record's title. I recommend the importer, since every part will carry it and it is the same words as the title. Chat's call which.
- **Part 1's file is named `PART_01__the-seven-beliefs-achology-is-built-on.md` while every link to it, and the brief, give the address `/learn/psychology/articles/standing-on-the-shoulders-of-giants/`.** The importer reads `post_name` from the record's page fields, not the file name, so this is only a naming mismatch, named so nobody is surprised.
- **The 39 back-links (`EXPORT__Seven_Beliefs_Back_Links_39_Pages_S387.csv`):** every row's `post_name` found on the install, one post each. Post IDs, for the rollout: abraham-maslow 33708, alfred-adler 33709, aristotle 33592, carl-jung 33598, charles-duhigg 33599, daniel-goleman 33600, erich-fromm 33602, erik-erikson 33711, gerard-egan 33605, howard-gardner 33712, james-allen 33607, jean-piaget 33713, joseph-campbell 33612, judith-s-beck 33715, kain-ramsay 33613, martin-seligman 33617, plato 33619, sigmund-freud 33622, thich-nhat-hanh 33626, viktor-frankl 33627, william-james 33628, a-guide-to-rational-living 33788, an-exploration-of-the-pygmalion-effect-experiment-on-expectations 35192, as-a-man-thinketh 35934, childhood-and-society 36533, cognitive-behavior-therapy-second-edition 35942, emotional-intelligence-goleman 35948, frames-of-mind 35954, games-people-play 35956, mans-search-for-meaning 10901, the-farther-reaches-of-human-nature 33833, the-nicomachean-ethics 35962, the-republic-plato 36551, the-six-pillars-of-self-esteem 36555, the-skilled-helper 35418, the-ultimate-life-coaching-handbook 35419, thinking-fast-and-slow 36559, what-life-could-mean-to-you 33851, a-way-of-being 33791.

## The 39 sentences are already live, and they point at pages that do not exist yet

Checked this session against the install after the S389 push: **all 39 inserted sentences are in their live bodies.** Cowork wrote them into the records at S387, and today's push put every record's words on its page, so they went live with the push rather than with the series. **Every one links to one of the nine series addresses, and none of the nine exists yet** (can-people-change 11 links, sense-of-purpose 10, know-thyself 10, change-your-life-from-the-inside-out 9, philosophy-of-life 8, thinking-errors 5, emotional-responsibility 5, standing-on-the-shoulders-of-giants 3, understanding-and-managing-emotions 3). DSRD 1 section 6.4 rule 5 says no link ever points at a missing page. The build site is hidden from search and the public, so no visitor meets them, but the page gate's link check will fail on these 39 until the series lands.

This is my miss: the push compared words and did not check for content the S390 brief held back. **Kain is asked, in the session, whether to take the 39 sentences off the live pages until the nine parts are published** (the records keep them, so they return with the series' own run). One anchor sentence, on an-exploration-of-the-pygmalion-effect-experiment-on-expectations, no longer matches its live body (the S388 pass changed it), but its inserted sentence is in place.

OWED BACK: the standards entry or the type to use; the H1 decision; Recipe 9 written from the answer above.

*No em or en dashes in this file; checked before writing.*
