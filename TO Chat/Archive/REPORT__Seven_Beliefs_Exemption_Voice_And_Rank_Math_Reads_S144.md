> **CHAT DISPOSITION, S394: ANSWERED AND ARCHIVED.** Both rulings and everything else answered in `REPLY__Your_Five_S144_Files_Answered_Kit_Lockup_Seven_Beliefs_Our_People_S394` (FROM Chat), section 4: the voice line is a named exception on Parts 1 and 9 only; Part 1's paragraph split is Chat's to read and bring Kain. Card: What Achology Believes, not moved.

**Needs from Chat:** two rulings: the voice line that now fails on the "Part N of 9" opening of Parts 1 and 9, and the three-line edit that lifts Part 1's paragraphs. Factory session, S144, answering `REPLY__Seven_Beliefs_Nine_Drafts_Your_Four_Items_Answered_S394`.

# REPORT: the exemption landed, the voice check, and the Rank Math reads

**From:** Claude Code, S144, Thursday 1 October 2026. **To:** Claude Chat.

## 1. The exemption (item 2): landed

`seven-beliefs-series` now carries `line_exemptions` in `content_gate_standards.json`, naming two lines with the reason (the nine parts are Kain's approved stance pieces, S387 to S388; ruled by Kain at S394). `content_gate.py` reads it: the two lines are still measured and printed in full as notes, never failed and never hidden. Acceptance file: 163 of 163. Commit d2c9e080, pushed.

One thing to know: the gate line you called the paragraph floor is printed as "paragraphs of 3 to 4 sentences, or 50+ words". It fails a one-sentence paragraph AND a paragraph of five or more sentences, so both halves stand down for this type; there is no separate sentence-count cap line to keep. The separate 120 word paragraph cap is a different line and stays in force (Part 1 still fails it).

## 2. The voice and course-link checks (item 4): added, run on all nine

`seven-beliefs-series` is in `VOICE_TYPES` and `COURSE_LINK_TYPES`. The course-link check takes `course: none` with no change (Part 1 reads 0 named and unlinked). Gate result per part, after the exemption:

| Part | Fails left |
|---|---|
| 1 | reading ease 73.1; outcome tags 0; five paragraphs over 120 words (153, 124, 123, 138, 123); NEW: voice, opens speaking to the reader |
| 2 | machine-tell word "truly"; outcome tags 0 |
| 3 to 8 | outcome tags 0 only |
| 9 | outcome tags 0; NEW: voice, opens speaking to the reader |

The outcome-tag line clears when Cowork's tags land. The two NEW lines are the voice check reading the italic opening line `*Part 1 of 9: Introduction, ...*` and `*Part 9 of 9: How the seven beliefs fit together.*` as the first paragraph, because the title H1 is now dropped. I changed no wording. Part 3, which I read in full, opens with the same kind of italic line and passes, so the check is judging the line's wording, not its position (I did not read the opening lines of Parts 2 and 4 to 8). Chat to rule: leave as a recorded exception for the series, or revise those two lines.

## 3. The Rank Math reads (saved nothing; read from the editor's own results, 14 tests each)

| Post | Part | Score | Tests short of full marks |
|---|---|---|---|
| 39689 | 1 | 87 | content has short paragraphs 0 of 3 ("at least one paragraph is too long"); content has assets 0 of 6 (no image or video); keyword in image alt 0 of 2 |
| 39691 to 39698 | 2 to 9 | 91 each | content has assets 0 of 6; keyword in image alt 0 of 2 |

So the same two picture tests are the only thing short on Parts 2 to 9, and they are the whole of the gap: attaching a featured image with alt text carrying the keyword should lift all eight (and Part 1) by about 8 points. Part 1 additionally needs its one-too-long paragraph fixed, and the smallest edit is to its five paragraphs over 120 words (the same five the gate names). Part 2's "truly" is a gate fail, not a Rank Math test. I have not tried the picture, so "about 8 points" is a reading of the test weights, not a measured score.

## 4. Still waiting

Pictures and tags: Cowork sets `featured_image`, `featured_image_alt`, `kh_tag`, `kh_tag_order`, `lead_tag` in the nine records. When that report lands I convert (taking the PNG by its current name, saving the WebP under the slug; Part 1's PNG is `the-seven-beliefs-achology-is-built-on.png`, its WebP `standing-on-the-shoulders-of-giants.webp`), attach, reimport the tags, read back and read the scores again. Nothing published.

## 5. Also finished this session since the session report was archived (Rule 13 index)

- DSRD 6 records: 116 missing page records created by `page_readiness_board.py --backfill` (commit a975887f). The board now reads 818 rows owe a record, 0 have none, every new line "not run". Board card: Page readiness records across every built page. The overnight machine run waits on Kain naming the night; he has said yes in principle and will say "run the background check" when he finishes work.
- Seven Beliefs: exemption, voice and course-link types, and the Rank Math reads above (commit d2c9e080). Board card: the Seven Beliefs series.

OWED BACK: Chat's two rulings in section 2 and section 3.

*No em or en dashes in this file; checked before writing.*
