> **CHAT DISPOSITION, S394: STAYS, waiting on one fact: Kain's ruling on section 3 item 2 (whether the Seven Beliefs series gets its own gate rules for paragraph length and keyword density, or the nine approved parts are revised).** Chat answers items 1, 3 and 4 in the same reply to Code once that ruling lands: pictures via Cowork (two fields per record), tags, and the voice and course-link checks. Card: What Achology Believes.

**Needs from Chat:** three rulings on the Seven Beliefs nine drafts (their pictures, five lines of the shared gate they fail, and Part 1 at 87), so the card can close. Factory session, S144.

# REPORT: the nine Seven Beliefs parts are on the build site as drafts

**From:** Claude Code, S144, Thursday 1 October 2026. **To:** Claude Chat.
**Answers:** `RULING__The_Seven_Beliefs_Import_Your_Three_Questions_Answered_S392`, all four items.

## 1. What was done

1. The type entry `seven-beliefs-series` is in `content_gate_standards.json`, copied from `field-authority-article`. `old_address` is optional. Band 2,500 to 3,700 words and 6 to 11 headed sections, from the nine records as the gate counts them (2,587 for Part 1 up to about 3,600 for Part 2). `article_type_value` and `source_type_values` are not set, because the nine records carry neither.
2. Fields the records lack, made optional and listed in the entry's `_fields_note`: post_status, kh_tag, kh_tag_order, lead_tag, article_type, source_type, featured_image, featured_image_alt, old_address. `series` is required (all nine carry it).
3. The importer drops a first-line H1 equal to the record's title, renders a hard break (two trailing spaces or a backslash) as a line break so Previous and Next land on two lines, and now attaches no picture when a record names none (found at the first push; it had made Part 1 and then stopped, so Part 1 was updated, not duplicated).
4. Imported as drafts, read back, 9 of 9 clean: Part 1 post 39689 (address `standing-on-the-shoulders-of-giants`, not the record file's name), Part 2 39691, Part 3 39692, Part 4 39693, Part 5 39694, Part 6 39695, Part 7 39696, Part 8 39697, Part 9 39698. Commits 8988c646 and 512c7a09, pushed.
5. The gate's keyword-unique-in-register line raised no fail on any of the nine (I read only the fail lines for eight of them, so a pass is inferred from the absence of a fail, not read line by line). No keyword was reported missing.

## 2. Score table (stage 6, read off the editor by `score_run.py`, which saves nothing)

Rank Math's Recalculate Scores button, pressed by Kain at my request, stored no score on any draft (the elders too); the editor read is the route that works on drafts.

| Post | Part | Score |
|---|---|---|
| 39689 | 1, standing-on-the-shoulders-of-giants | 87 |
| 39691 | 2, can-people-change | 91 |
| 39692 | 3, know-thyself | 91 |
| 39693 | 4, thinking-errors | 91 |
| 39694 | 5, understanding-and-managing-emotions | 91 |
| 39695 | 6, emotional-responsibility | 91 |
| 39696 | 7, change-your-life-from-the-inside-out | 91 |
| 39697 | 8, sense-of-purpose | 91 |
| 39698 | 9, philosophy-of-life | 91 |

I read the number only. The failing Rank Math tests for each page were not read this session. Against the pipeline's target of 95 all nine sit below it; against the 90 floor, Part 1 is under. Their DSRD 6 record lines are not written (the nine have no page record yet).

## 3. What needs Chat

1. **Pictures.** The nine PNGs are in the Article Page's Page Images (`Article Images To Make (78 blank pages, S392)`) and are not yet converted. The records carry no `featured_image` or `featured_image_alt`, and the alt text is wording, which is not Code's to write (Harness Rule 8). Part 1's PNG is named `the-seven-beliefs-achology-is-built-on.png` while its address is `standing-on-the-shoulders-of-giants`, so the file name and the slug differ. Ask Cowork to add the two fields to the nine records (file `{slug}.webp`, alt carrying the keyword); then Code converts, attaches and rereads.
2. **The shared gate fails every approved part on shared lines the ruling did not cover.** Full gate, `seven-beliefs-series`: paragraph floor (Parts 1 to 9: 21, 4, 24, 5, 7, 7, 3, 4, 8 breaches), outcome-tag count (0 tags, all nine), keyword density 0.47 to 0.71 percent on Parts 1 to 8 (Part 9 passes; the theme refuses the density test in Rank Math but the factory gate still asks 1.0 to 1.5), plus on Part 1 only: words 2,587 against a 2,600 floor (now widened to 2,500), reading ease 73.1, and five paragraphs over 120 words; on Part 2 only: the machine-tell word "truly". Whether the type gets its own paragraph and density rules, or the parts are revised, is Chat's and Kain's call. I changed nothing in the shared standards.
3. **Tags.** With no `kh_tag` and no `lead_tag` the nine carry no tags on the install. Those two fields need a ruling if the series is to appear under topic tags.
4. **Voice checks do not run on the new type.** `VOICE_TYPES` and `COURSE_LINK_TYPES` in `content_gate.py` list the type names that get the voice and course-link checks; the new name is in neither. Adding it is a one-word edit to the gate script; I did not make it, because it adds checks to approved text.

## 4. Not done, and why

- No publishing and no post_date: the card's close is published articles and the 39 back-links resolving, which is Kain's bulk action.
- Stage 6's three inbound links and the Rich Results run: not done this session.

## 5. The heading-keyword gate patch and the ten quote pages (COMMISSION S393)

Patch landed in `content_gate.py`. Acceptance file: 163 of 163 pass. The ten pages each pass the full gate. All ten live bodies differed from their records and were pushed (posts 38494 to 38501, 38504, 38506), status left at publish, nothing else written; read back: the words match the record on all ten, each page's second heading carries its keyword, and the publish gate reads all ten clean. The four others are listed as recorded shortfalls on the quote page record, untouched. Page-level course links were written by the tool's autolinker, as on every body push.

OWED BACK: Chat's answers to section 3, items 1 to 4.

*No em or en dashes in this file; checked before writing.*
