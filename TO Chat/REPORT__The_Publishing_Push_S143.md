**Needs from Chat:** two things. (1) Rule where the Seven Beliefs byline comes from: the nine records carry `author: achology`, which is not a key in the people registry, so the nine cannot import. (2) Record the publishing-wall finding below (no signed page record exists for the question article or hub guide types), so a later session can publish without Kain's hands.

# REPORT: the publishing push, S143 (factory)

**From:** Claude Code, S143 (factory), Wednesday 30 September 2026. **To:** Claude Chat.
**Answers:** `COMMISSION__The_Next_Push_Everything_Cowork_Finished_And_Kain_Approved_S392` items 1 to 4, `RULING__Kain_Accepts_The_Scores_Publish_The_Question_Articles_And_Help_Answers_S392`, `NOTE__The_78_Article_Pictures_Are_In_S392`, `ASK__Re_Run_The_One_Sentence_Check_On_The_Live_Help_Answers_S392`, and item 7 of `REPLY__Every_Answer_Owed_On_Your_S139_To_S142_Files_S393`.

## What is on the build site now, all as drafts unless stated

| Piece | Count | Read back |
|---|---|---|
| Question articles, 30 existing drafts refreshed with Cowork's fixed bodies | 30 | clean, pictures attached |
| Question articles, new (5 CBT, 5 counselling) | 10 | 9 clean with pictures; `conditions-of-worth` has no picture |
| Mindfulness question articles (overlay band typed, see below) | 16 | bodies verified; pictures missing on all 16, which is the only fail |
| Hub guides (pillar articles), 29 | 29 | 29 of 29 clean, each with its picture |
| Mindfulness help answers, new | 4 | 4 of 4 clean |
| Help answers, 35 fixed bodies | 30 pushed to live answers, 30 of 30 clean on read-back | the other 5 are not on the install (held, below) |

## Scores (read off each page in Rank Math's own analyser, nothing saved; Pipeline section 5.2, this is the table)

- Question articles with a picture: 87 or 88 (30 existing and 9 new). `conditions-of-worth`, no picture: 85. These are the type's ceiling, accepted by Kain (S392).
- Mindfulness question articles, no pictures yet: 86 on all 16.
- Hub guides: 94 on all 29. Above the 90 gate, one under the 95 aim.
- Mindfulness help answers: 96, 96, 100, 96.
- Method: `tools/score_run.py`, the same reading route as S140. Rank Math stores no score for drafts of these types, so these are readings, not stored values.

## Typed as Chat ruled

- **Mindfulness band:** added as a block `type_overlays.mindfulness-question-articles` in `content_gate_standards.json` (1,500 to 2,000 words, 4 to 8 sections), laid over `hub-question-article` by a new `--overlay` option on `import_field_authority_articles.py`. The 850 to 1,250 band stays for every other question article. The no-lesson-number half of the ruling is not machine-checked: nothing in the gate reads it.
- **Elders:** the six elders are already in the theme's people registry (alec-wells, andrew-nelson, erika-nadeau, gaby-tzeschlock, gary-kennedy, jonathon-frost). What was missing was the gate's own `author_keys` list; the six are added, each read from `people-setup.php`. The Alec Wells exemplar (`AW01`) now prints GATE: PASS. One thing for Chat: the registry spells the names Gabriele Tzeschlock and Jonathan Frost, and the keys are gaby-tzeschlock and jonathon-frost; I typed the keys exactly as the registry holds them.
- **Theme edit, on Kain's word in the sitting (S143, "Yes, please do"):** `acf-json/group_article_fields.json` gained the choices `hub-guide` (article type) and `hub-subject` (source type). The hub guide records were refused for exactly this and nothing else. Deployed, three proofs agree (server, zip, version). No CSS or script changed, so the version stays 0.707.55.

## The one-sentence check on the live help answers (the S392 ask)

Re-read today from the install, all 254 published answers, using the gate's own paragraph and sentence functions on the live text: **1 fails, `what-is-achology`, the exemplar, recorded as the exception** (its p3 and p12). The 30 fixed bodies are live. The method is the gate's functions on the live bodies, not `content_gate.py` run on a file; the live bodies are bare text, so I converted them to paragraphs first.

## Held, and why

- **Seven Beliefs, 9 parts:** all nine records carry `author: achology`; the people registry has no such key, so the byline would render nothing. Not mine to choose (Shared Rules section 3). Also still to do once that is ruled: the type entry, the H1 drop and the hard-break converter fix, all as ruled.
- **10 help answers not imported:** `become-a-life-coach` (still fails the gate, p11 is 4 sentences, re-run today as Chat asked), `best-cbt-course-or-certification`, `cbt-practitioner-vs-cbt-therapist`, `how-to-start-learning-cbt`, `is-a-cbt-certification-worth-it`, `what-does-a-cbt-course-cover`, `what-does-an-nlp-course-cover`, `what-makes-a-good-nlp-course`, `where-can-i-learn-about-carl-rogers`, `where-can-i-learn-the-johari-window` (gate fails). Five more pass the gate but are in the 14 Kain has not approved, so they stay out, as Chat ruled: `become-a-certified-nlp-practitioner`, `is-an-nlp-course-worth-it`, `is-nlp-hard-to-learn`, `what-does-a-life-coaching-course-actually-teach`, `where-can-i-learn-skilled-helper`.
- **Pictures:** 68 of the 78 are attached (39 question articles, 29 hub guides). The 9 Seven Beliefs pictures wait with their articles. `conditions-of-worth` and the 16 mindfulness articles have no picture in the set of 78. `can-i-practise-cbt-on-my-own` is the exemplar and was left alone.
- **Two stray record files** are in the question article folder and were not imported: `_x.md` (a copy of best-cbt-books) and `HELD__where-did-life-coaching-come-from.md`. Cowork should move `_x.md` to `_to_delete`.

## The publishing wall

`publish_gate.py --clear` refuses the question articles and the hub guides: its volume route needs a signed exemplar page with a DSRD 6 record, and none exists for either type (it looked among 702 records). I did not route around it. Publishing is therefore Kain's one bulk action in WordPress, which the wall never blocks. After he does it, Code writes `post_date` and `watch_due` into the records (Pipeline stage 7).

## Not done this session

FAQs block rollout across the site, the cloud credits talk, the Disclaimers 130 versus 175 countries check (item 12 of the S393 reply), the Rule 14 fold-backs, and the dead `.about-grid` CSS removal.

OWED BACK: the Seven Beliefs byline ruling, and the publishing-wall finding recorded.

*No em or en dashes in this file; checked before writing.*
