# BRIEF: retag the 82 rescued articles against the 36 locked tags, and fix their keys, in one correction run

**From:** Claude Chat, Session 341. **Date:** 5 September 2026.
**Authority:** Kain, in Chat this session. His word: "yes" to the route named below.
**Run under:** the Cowork Production Harness (Version 16), Rule 5 (never open the master file) and Rule 7 (your outbound tray is FROM Cowork and nothing else). This is a metadata correction run, not a drafting run: no body copy changes anywhere, in any record, for any reason.
**Output folder:** `Content Records/field-authority-article/` and `Content Records/quote-page/` in the Content Production Factory folder. You write into those two folders and into FROM Cowork, nowhere else.

---

## 1. Why this run exists

Code built the field-authority-article importer this session and ran it in plan mode against every record in the folder. **All 82 refused.** Not one can be imported as it stands. The faults are in the records' metadata, not in the writing, and every class below was counted by Code off the install (`REPORT__The_Two_Missing_Importers_Are_Built_And_Registered_S102.md`, channel Archive after this session):

| Records | Fault |
|---|---|
| 82 of 82 | `kh_tag` carries free-text topic words ("harry harlow", "research ethics", "history of psychology") instead of the 36 locked tag slugs. WordPress would mint about 200 new terms, and the course cards at the foot of every page would render empty, because the theme fills them from the lead tag's course mapping and an unregistered tag maps to nothing. |
| 82 of 82 | `lead_tag` outside the register, for the same reason. |
| 72 of 82 | `author` is not a key the people registry holds. Seventy carry `charlotte-avery`; the registry key is `charlotte-j-avery`. The byline resolves by exact key, so the page would show no author at all. |
| 80 of 82 | `source_type` carries one of ten invented values (`study`, `framework`, `salvage`, `legacy-page`, `historical-overview`, and so on). |
| 23 of 82 | `article_type` is `field-authority-article`, `school-authority` or `salvage-rewrite`. The register value is `field-authority`. |
| 2 of 82 | `lead_tag` is not among the record's own `kh_tag` values. |

The frozen exemplar carried the first three faults too, so the pattern came from Chat's side, not yours. **Chat has already corrected the exemplar's metadata and it is the pattern for this run** (`EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md`, its header carries the S341 correction note).

**The gate now catches all of this.** `content_gate.py` (edited S341, beside these records) reads `kh_tag`, `lead_tag`, `kh_tag_order`, `author`, `article_type` and `source_type` for their values against the standards file. Run it on the exemplar and you will see the new lines passing; run it on any other record in the folder and you will see them failing. Your run is finished when every record passes those lines.

## 2. The 36 locked tags, copied from DSRD 1 section 5.6 at S341

**Outcome and problem tags (25). Each record carries two to four of these, and only these count toward the two-to-four.**

understand-your-mind, build-confidence, develop-emotional-intelligence, improve-relationships, find-purpose-and-direction, achieve-your-goals, lead-with-impact, build-mental-resilience, practice-mindfulness, help-others-grow, support-mental-health, communicate-effectively, grow-self-awareness, master-your-mindset, increase-productivity, unlock-personal-growth, overcome-self-doubt, manage-stress-and-anxiety, break-negative-thinking, navigate-life-changes, build-self-discipline, strengthen-your-partnership, start-and-grow-a-business, overcome-feeling-stuck, improve-social-confidence

**Attribute tags (5). Additional, uncounted, added only where honestly true. Never the lead tag.**

research-based (the piece rests on named studies or experiments), practical-exercise (the reader is given something to do), deep-dive (long and comprehensive on one subject), beginner-friendly, professional-practice (written for practitioners)

**Modality tags (6). Additional, uncounted. May be the lead tag where the piece is plainly about that discipline.**

learn-nlp, learn-cbt, learn-life-coaching, learn-counselling, learn-hypnotherapy, learn-mindfulness

No other value exists. A tag not in these three lists is a fault.

## 3. How to choose a record's tags

Read the record's title, excerpt and `kh_category`. Then ask one question: **what does a reader gain from this article?** Tag the gain, never the topic. An article about the Milgram experiment is not tagged "milgram" or "obedience"; a reader gains understanding of their own mind and a warning about authority, so it carries `understand-your-mind` and `master-your-mindset`, with `research-based` as an attribute because it rests on a named experiment.

**The lead tag is the gain the reader most wants, written first.** The theme reads it to fill the three course cards at the foot of the page (DSRD 1 section 5.7), so the lead tag decides which courses the page recommends. Pick the one whose course mapping fits the article's `destination_course_name`, the school the article points to. The mapping tables are DSRD 1 sections 5.2, 5.3 and 5.5; you do not need to open them, because every outcome tag maps to at least three courses and the fit is usually plain from the tag's name.

Three worked examples, all real records in the folder:

- **The Seven Levels of Human Awareness** (personal-growth, the exemplar, already corrected by Chat): `grow-self-awareness, unlock-personal-growth, master-your-mindset, deep-dive`. Lead `grow-self-awareness`.
- **Obedience to Authority: Stanley Milgram** (a study): `understand-your-mind, master-your-mindset, research-based`. Lead `understand-your-mind`.
- **Gerard Egan's Skilled Helper Model** (counselling practice): `help-others-grow, communicate-effectively, learn-counselling, professional-practice`. Lead `help-others-grow`.

## 4. The edit on every field-authority record, and nothing else

For each of the 81 records (every `.md` file in the folder except the exemplar, the batch reports, `ARTICLE_HERO_IMAGE_MAP_S340.csv`, `body_before.txt` and the one file named `SUPERSEDED__`, which is retired and is not touched):

1. `kh_tag`: replace the value with the chosen tags, comma separated, lead tag first.
2. `kh_tag_order`: the same list, in the same order.
3. `lead_tag`: the first tag in `kh_tag`.
4. `author`: `charlotte-j-avery` where it reads `charlotte-avery`. Where it reads anything else, map it to the registry key by name: the eleven keys are amelia-a-sinclair, benjamin-lockwood, charlotte-j-avery, declan-fitzpatrick, evelyn-montgomery, frederick-s-martin, isabella-s-whitmore, jackson-p-hartley, kain-ramsay, gerard-egan, karen-ramsay. A value that maps to none of these is skipped and logged as waiting on ruling, per Rule 3.
5. `article_type`: `field-authority`, on every record.
6. `source_type`: `legacy-page`, on every record. (Kain added this value to the theme's choice list at S341; Code's theme edit travels separately. Until it lands, the gate passes it and Code's importer refuses it, and that order is correct.)
7. Nothing else in the field table moves, and the body is not opened for editing.

Then run `python3 content_gate.py <record> field-authority-article` on each record. The seven lines this run owns are: `every tag is one of the 36 locked slugs`, `outcome or problem tags, 2 to 4`, `lead_tag is one of the record's own tags, not an attribute`, `kh_tag_order carries the same tags as kh_tag`, `author is a key the people registry holds`, `article_type is the register value`, `source_type is a value the ACF field offers`. All seven must read PASS on every record. Other lines on the printout that read FAIL are pre-existing and are not this run's to fix; note their count per record in the report and leave them.

## 5. The two mechanical edits on the quote records

For each of the 25 records in `Content Records/quote-page/`:

1. `author`: `frederick-s-martin` where it reads `frederick-martin`.
2. `image_quote_text`: where it differs from `quote_text` in any character, replace it with `quote_text` exactly. The rule is the S300 no-cap ruling: the two are always identical. Code counted five that differ.

Nothing else on the quote records moves. **Two faults on them are known and are deliberately not this run's:** every quote record lacks `demand_evidence` (a stage 0 job, its own brief), and the S341 gate shows each carries one outcome tag where the standard says two to four (a finding Chat is taking to Kain, not a fix for tonight). Log both as seen, touch neither.

## 6. The report, in the shape Code asked for at S101

One `Batch_Report__Retag_And_Keys_S341.md` in the field-authority-article folder and one `Batch_Report__Quote_Keys_S341.md` in the quote-page folder, each carrying:

- At its head, in one sentence each: which records this run touched, and which records in the folder it did not touch and why (the exemplar, the superseded record, the batch reports, the CSV). Nothing left to be inferred by set difference.
- One row per record: record slug (there is no post ID before import, so the slug is the key), the tags chosen with the lead tag first, the author key written, the count of other gate lines still reading FAIL.
- The gate printout for every record, attached, per Rule 6. A record you edited but did not gate is "edited, not verified", in those words.

Then one file into FROM Cowork: `DONE__Retag_And_Keys_Run_S341.md`, naming the two reports and the two counts (records touched, records passing all seven lines).

## 7. What this run is not

Not a rewrite, not a re-gate of the body, not a keyword pass, not a source check. Where a record's tags cannot be chosen with confidence from its title and excerpt, skip it, log it as waiting on ruling with the two tags you were choosing between, and carry on.

---

OWED BACK: the two batch reports in their folders and the DONE file in FROM Cowork. Chat re-reads the gate printouts against the reports, then relays "records ready" to Code so the importer runs the moment the pictures and the theme edit have landed.

*No em or en dashes in this file; checked before writing.*
