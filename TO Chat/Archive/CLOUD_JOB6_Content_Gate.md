# Job 6: content gate run over every file under Content Records

Read-only run. Nothing in the record repository was changed; the gate only reads. This report is the one new file, on branch `cloud-report/job6-content-gate` of `kain-ramsay/achology-record`. It replaces the first two versions of the report on this branch (git history holds them); the results below are from the third and final run.

## How it was run

- Repository: `kain-ramsay/achology-record`, shallow clone of `main` at commit `10b2ec1eb6db77af9341f966ea351b092bf09301`.
- Gate: `content_gate.py` in `Claude Code (Projects)/0001. Achology Website Upgrade 2026/04. Content Production Factory + COWORK/`, run as `python3 content_gate.py "Content Records/<type>/<file>.md" <type>` from that folder, once per Markdown file, with the file's own folder name as the content type. Standards were read from `content_gate_standards.json` in the same folder.
- Content type: taken from the folder the file sits in. The folder names match the gate's type keys exactly (`author-biography`, `book-note`, `field-authority-article`, `help-answer`, `hub-guide`, `hub-question-article`, `instructor-article`, `quote-page`, `seven-beliefs-series`, `workbook`). Whether a record's own fields name a different type: **cannot tell from this run**.
- A "failing line" is a line of the gate's printout that begins `FAIL`. Lines beginning `..` (flags and `NOT RUN` notes) are not failures and are not counted. For every record the number of `FAIL` lines equals the count in the gate's own `GATE: FAIL (n)` line.
- Files under Content Records: **1395**. Gate run on **1363** (every `.md` file in a type folder). **32** were not run (see the last section).

## The three runs, and what the environment supplied

The gate reads three things that are not in the repository. Each was missing from the first run.

1. **Run 1, as cloned.** 772 pass, 591 fail, 1,434 failing lines. The gate printed `course links, NOT CHECKED` on 824 records, and skipped the keyword-clash test silently.
2. **Run 2, with the theme's `courses-setup.php` and `people-setup.php` in place.** Copies from the `achology-theme` repository `main` at `8556d96` were placed at the path the gate looks for (`.../01. www.achology.com | All Website Assets/01. The Achology WordPress Theme/achology/`) for the run, not committed, and removed afterwards. No failing line changed on any record. Whether `main`'s `courses-setup.php` is the version the records were written against: **cannot tell**.
3. **Run 3 (this report), also with `KEYWORD_REGISTER.csv` present.** No copy exists anywhere in the repository, its history or the session (searched). The file is untracked on purpose (`.gitignore`). The project's own `build_keyword_register.py` rebuilds it from the records, so it was rebuilt that way: 1,326 rows from the 11 record folders, no `__CLAIMS.csv` file present. The builder itself exits 1 and prints one clash: keyword `self-awareness`, claimed by `the-importance-of-self-awareness` and by `self-awareness`. **One record changed result**: `field-authority-article/the-importance-of-self-awareness.md` now fails `keyword unique in register` (claimed by `self-awareness`). Every other record keeps its result. The register file was removed afterwards and is not in the commit.

Limits that remain, so the numbers are not claimed as the project machine's:

- The rebuilt register is made from these same records, so it can only show clashes between two records. Any keyword claim held only in the real register (for example rows pasted in by hand, or help-section claims the builder's comments say live outside the records) is not in it. Whether the project machine's register has rows this one lacks: **cannot tell**.
- The other claimant in the clash is a retired record. The builder reads the `hub-guide-retired` folder too; its one file, `self-awareness__superseded_by_grow-self-awareness.md`, carries `post_name` `self-awareness`, `rm_focus_keyword` `self-awareness` and address `/learn/helping-people/articles/self-awareness/` in its own fields (register row from `hub-guide-retired`, slug `self-awareness`). Whether a retired record's keyword should still count as claimed, so that the live article fails: **cannot tell from the code**.
- **265 records had checks marked `NOT RUN` by the gate itself** because the record is dated before a line existed (for example the outcome-tags line, 2026-09-04, and the stage 0 demand line, 2026-08-26) or its brief state is pre-standard. Those are exemptions the gate applies, not failures.

## Summary by content type

| Content type | Files run | Pass | Fail | Failing lines in all |
|---|---|---|---|---|
| author-biography | 52 | 50 | 2 | 6 |
| book-note | 153 | 47 | 106 | 151 |
| field-authority-article | 121 | 106 | 15 | 38 |
| help-answer | 341 | 113 | 228 | 540 |
| hub-guide | 29 | 29 | 0 | 0 |
| hub-question-article | 58 | 57 | 1 | 5 |
| instructor-article | 139 | 94 | 45 | 57 |
| quote-page | 457 | 275 | 182 | 596 |
| seven-beliefs-series | 12 | 0 | 12 | 31 |
| workbook | 1 | 0 | 1 | 11 |
| **All** | **1363** | **771** | **592** | **1435** |

Of the 592 failing files, 32 have names that start with a working-file prefix (`REPORT__`, `Batch_Report`, `SKIPPED__`, `SUPERSEDED__`, `HELD__`, `MEASURED__`, `_` or `000__`); 33 files with such names were run in all. They are marked in the lists below with *(name prefix suggests a working file, not a drafted record)*, and their failures are included in every count. Whether each is a record that should pass the gate: **cannot tell from the code**. Counts with those files left out are not given.

Exit codes seen: 0 (pass) on 771 files, 1 (fail) on 592 files. No file ended with exit code 2 or an error on stderr.

## Failing lines grouped by line, all types, with a count for each

Count is the number of records on which that line printed FAIL.

| Count | Failing line |
|---|---|
| 286 | 'actually' at most once (Kain, S381) |
| 213 | keyword in a subheading |
| 206 | unexpected section |
| 156 | keyword in address slug |
| 110 | machine-written tells |
| 64 | reading ease (Flesch, approximate) |
| 50 | paragraphs of 3 to 4 sentences, or 50+ words |
| 45 | keyword density |
| 33 | record field block present |
| 33 | voice: the quoted person is not narrated |
| 31 | total body words |
| 29 | contractions: at least one in the body |
| 26 | section headings, verbatim and in order |
| 25 | keyword verbatim in first 10% of body |
| 22 | the body ends on the reflection question |
| 22 | a 'Put this into practice' block (Kain, S356) |
| 14 | outcome or problem tags, 2 to 4 |
| 14 | no paragraph over 60 words or 3 sentences |
| 8 | voice: opens speaking to the reader |
| 5 | voice: no paragraph describing the article |
| 4 | keyword in first 50 chars of SEO title |
| 4 | description length |
| 4 | no paragraph over 120 words |
| 3 | headed sections, counted not named |
| 3 | external link to the source present |
| 3 | stage 0 demand evidence recorded |
| 3 | banned brand words |
| 3 | practice block within 40 to 60 words |
| 2 | every tag is one of the 36 locked slugs |
| 2 | no em or en dashes |
| 2 | no one-sentence paragraph (Kain, S361) |
| 2 | keyword in first 120 chars of description |
| 1 | article_type is the register value |
| 1 | source_type is a value the ACF field offers |
| 1 | keyword unique in register |
| 1 | voice: first heading does not repeat the title What is counselling? |
| 1 | SEO title length |
| 1 | required fields present (22) |
| 1 | author is a key the people registry holds |
| 1 | landing page body present |

## Failing lines grouped by line, within each content type

Each line shows the count, then every record that failed it with the gate's own detail text (whitespace collapsed; detail over 240 characters is cut and marked).

### author-biography (2 of 52 records fail)

**keyword in address slug: 1**

- `Author_Biography_Brene_Brown_S304.md` — brene-brown

**paragraphs of 3 to 4 sentences, or 50+ words: 1**

- `_scratch_peterson.md` *(name prefix suggests a working file, not a drafted record)* — 1 breach: (opening) p1=1sent/32w

**reading ease (Flesch, approximate): 1**

- `_scratch_peterson.md` *(name prefix suggests a working file, not a drafted record)* — 18.4 (band 60 to 70)

**record field block present: 1**

- `_scratch_peterson.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found

**section headings, verbatim and in order: 1**

- `_scratch_peterson.md` *(name prefix suggests a working file, not a drafted record)* — found 0

**total body words: 1**

- `_scratch_peterson.md` *(name prefix suggests a working file, not a drafted record)* — 32 (standard 1600 to 2000)

### book-note (106 of 153 records fail)

**'actually' at most once (Kain, S381): 100**

- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — 4 found
- `a-guide-to-rational-living.md` — 4 found
- `a-path-through-the-jungle.md` — 3 found
- `a-way-of-being.md` — 11 found
- `atomic-habits-clear.md` — 6 found
- `authentic-happiness-seligman.md` — 5 found
- `awakenings.md` — 3 found
- `before-happiness.md` — 2 found
- `best-self-be-you-only-better.md` — 4 found
- `boundaries-cloud.md` — 2 found
- `brainstorm-the-power-and-purpose-of-the-teenage-brain.md` — 5 found
- `chasing-the-scream.md` — 3 found
- `coaching-with-the-brain-in-mind.md` — 2 found
- `coming-to-our-senses.md` — 8 found
- `creating-minds.md` — 8 found
- `daring-to-trust.md` — 10 found
- `decisive.md` — 8 found
- `difficult-conversations-patton.md` — 8 found
- `embracing-uncertainty.md` — 4 found
- `feeling-good-burns.md` — 4 found
- `finding-flow.md` — 5 found
- `frames-of-mind.md` — 2 found
- `further-along-the-road-less-travelled.md` — 7 found
- `games-people-play.md` — 6 found
- `getting-past-no.md` — 5 found
- `have-a-little-faith.md` — 4 found
- `homage-to-catalonia.md` — 5 found
- `how-the-mighty-fall.md` — 5 found
- `how-to-fix-a-broken-heart.md` — 5 found
- `how-to-know-a-person.md` — 5 found
- `humble-inquiry.md` — 3 found
- `identity-youth-and-crisis.md` — 4 found
- `journey-to-the-heart.md` — 6 found
- `keeping-the-love-you-find.md` — 3 found
- `leader-effectiveness-training.md` — 3 found
- `linchpin.md` — 4 found
- `mans-search-for-meaning.md` — 5 found
- `maps-of-meaning.md` — 3 found
- `mental-efficiency.md` — 3 found
- `money-master-the-game.md` — 3 found
- `multiple-intelligences-new-horizons.md` — 2 found
- `necessary-endings.md` — 3 found
- `noise.md` — 2 found
- `open-when.md` — 7 found
- `quit.md` — 2 found
- `radical-compassion.md` — 6 found
- `recovering-from-emotionally-immature-parents.md` — 5 found
- `resilient.md` — 4 found
- `shift.md` — 3 found
- `shyness-what-it-is-what-to-do-about-it.md` — 3 found
- `speak-peace-in-a-world-of-conflict.md` — 6 found
- `stillness-speaks.md` — 6 found
- `stoicism-and-the-art-of-happiness.md` — 3 found
- `surrounded-by-psychopaths.md` — 2 found
- `teacher-and-child.md` — 4 found
- `the-4-hour-body.md` — 5 found
- `the-8th-habit.md` — 10 found
- `the-advantage.md` — 9 found
- `the-advice-trap.md` — 2 found
- `the-beck-diet-solution.md` — 4 found
- `the-brains-way-of-healing.md` — 3 found
- `the-bridge-across-forever.md` — 3 found
- `the-confidence-gap.md` — 4 found
- `the-diet-trap-solution.md` — 2 found
- `the-doors-of-perception.md` — 5 found
- `the-farther-reaches-of-human-nature.md` — 3 found
- `the-feeling-good-handbook.md` — 3 found
- `the-gap-and-the-gain.md` — 4 found
- `the-happiness-project.md` — 9 found
- `the-high-5-habit.md` — 6 found
- `the-history-of-philosophy.md` — 2 found
- `the-honest-truth-about-dishonesty.md` — 5 found
- `the-jealousy-cure.md` — 2 found
- `the-life-cycle-completed.md` — 4 found
- `the-maine-woods.md` — 7 found
- `the-open-society-and-its-enemies.md` — 2 found
- `the-origins-of-intelligence-in-children.md` — 3 found
- `the-perennial-philosophy.md` — 2 found
- `the-places-that-scare-you.md` — 2 found
- `the-power-of-truth.md` — 3 found
- `the-psychology-of-self-esteem.md` — 3 found
- `the-relationship-cure.md` — 6 found
- `the-republic-plato.md` — 4 found
- `the-science-of-being-well.md` — 3 found
- `the-six-pillars-of-self-esteem.md` — 8 found
- `the-skilled-helper.md` — 5 found
- `the-stoic-challenge.md` — 5 found
- `the-time-paradox.md` — 5 found
- `the-ultimate-life-coaching-handbook.md` — 5 found
- `the-way-to-love.md` — 5 found
- `thrift.md` — 2 found
- `time-and-free-will.md` — 7 found
- `toward-a-psychology-of-being.md` — 2 found
- `truth-and-repair.md` — 8 found
- `tusculan-disputations.md` — 6 found
- `utilitarianism.md` — 3 found
- `what-do-you-say-after-you-say-hello.md` — 6 found
- `what-life-could-mean-to-you.md` — 2 found
- `why-zebras-dont-get-ulcers.md` — 4 found
- `words-that-work.md` — 4 found

**unexpected section: 20**

- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — The four read with a harder eye, as the brief asked
- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — The result, stated plainly first
- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — The seventeen, one by one
- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — What this leaves for Code and for Kain
- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — What this read did
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — Addendum: Kain's ruling on stoicism and the art of happiness
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — Fixed in the same pass, small and mechanical
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — Logged, not fixed: the same body and link gap as the seventeen, plus one more
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — One finding that is not like the others: stoicism and the art of happiness
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — Results, all 25
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — The scope correction, found before any file was touched
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — What comes next
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — What this means for the board card
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — What was done on the 25
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — Addendum: Kain's ruling on the three open points, so the same three are not re-asked forty-six times
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — The seventeen, one line each
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — What comes next
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — What this means for the board card
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — What was done, on every one of the seventeen
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — Why sixteen of the seventeen still show GATE: FAIL

**machine-written tells: 11**

- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — plainly
- `a-way-of-being.md` — truly
- `awakenings.md` — truly
- `coming-to-our-senses.md` — truly
- `creating-minds.md` — truly
- `how-the-mighty-fall.md` — truly
- `noise.md` — truly
- `the-brains-way-of-healing.md` — truly
- `the-open-society-and-its-enemies.md` — truly
- `the-relationship-cure.md` — truly
- `time-and-free-will.md` — truly

**total body words: 4**

- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — 1776 (standard 1100 to 1400)
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — 2186 (standard 1100 to 1400)
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — 1086 (standard 1100 to 1400)
- `a-way-of-being.md` — 1440 (standard 1100 to 1400)

**paragraphs of 3 to 4 sentences, or 50+ words: 3**

- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — 6 breach: The seventeen, one by one p3=2sent/47w, The seventeen, one by one p4=2sent/44w, The four read with a harder eye, as the brief asked p1=1sent/21w, The four read with a harder eye, as the brief asked p3=6, The four read with a harde [truncated, 323 chars in all]
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — 14 breach: The scope correction, found before any file was touched p3=6, The scope correction, found before any file was touched p5=5, What was done on the 25 p1=2sent/23w, What was done on the 25 p2=5, What was done on the 25 p3=2sent/48w, [truncated, 787 chars in all]
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — 13 breach: What was done, on every one of the seventeen p1=2sent/34w, What was done, on every one of the seventeen p3=2sent/47w, What was done, on every one of the seventeen p4=2sent/37w, What was done, on every one of the seventeen p5=2sen [truncated, 836 chars in all]

**reading ease (Flesch, approximate): 3**

- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — 53.7 (band 60 to 70)
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — 49.6 (band 60 to 70)
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — 45.9 (band 60 to 70)

**record field block present: 3**

- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found

**section headings, verbatim and in order: 3**

- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* — found 5
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* — found 9
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* — found 6

**keyword in address slug: 2**

- `free-will-sam-harris.md` — free-will-sam-harris
- `nature-emerson.md` — nature-emerson

**keyword density: 1**

- `emotional-leonard-mlodinow.md` — 0.79% (11 hits, band 1.0 to 1.5)

**keyword in first 50 chars of SEO title: 1**

- `yes-50-scientifically-proven-ways-to-be-persuasive.md` — 51 chars

### field-authority-article (15 of 121 records fail)

**'actually' at most once (Kain, S381): 11**

- `EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S344.md` — 3 found
- `_to_delete/EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md` — 3 found
- `_to_delete/SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic.md` *(name prefix suggests a working file, not a drafted record)* — 2 found
- `a-guide-to-building-inner-resilience.md` — 2 found
- `balanced-lifestyle-seven-practical-steps-to-achieve-life-balance.md` — 2 found
- `helping-people-help-themselves.md` — 12 found
- `learn-about-the-psychologist-dr-albert-ellis.md` — 3 found
- `learned-helplessness-experiment-the-psychology-of-helplessness.md` — 7 found
- `maslows-hierarchy-of-needs.md` — 2 found
- `psychology-history-timeline.md` — 3 found
- `the-impact-of-the-invisible-gorilla-experiment-explained.md` — 2 found

**paragraphs of 3 to 4 sentences, or 50+ words: 6**

- `EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S344.md` — 10 breach: (opening) p2=2sent/44w, (opening) p4=2sent/39w, What the seven levels of human awareness are p1=2sent/26w, What the seven levels of human awareness are p10=2sent/46w, Why it matters which level is running your week p2=2sent/28w,  [truncated, 609 chars in all]
- `REPORT__Exemplar_Gate_Fixed_And_Row_152_Trim_Confirmed_S344.md` *(name prefix suggests a working file, not a drafted record)* — 10 breach: Item 1: the frozen exemplar, gate-fixed and re-frozen as FROZEN_S344 p1=1sent/38w, Item 1: the frozen exemplar, gate-fixed and re-frozen as FROZEN_S344 p2=1sent/42w, Item 1: the frozen exemplar, gate-fixed and re-frozen as FROZEN [truncated, 837 chars in all]
- `SUPERSEDED__how-psychological-thinking-has-transformed-over-the-years.md` *(name prefix suggests a working file, not a drafted record)* — 9 breach: (opening) p1=2sent/22w, (opening) p3=2sent/32w, How Psychological Thinking Has Transformed Since 1879 p5=2sent/12w, Why it matters p5=2sent/28w, Going deeper p8=2sent/31w, Putting it into practice p6=2sent/33w, Putting it into pra [truncated, 338 chars in all]
- `_to_delete/EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md` — 10 breach: (opening) p1=5, (opening) p2=5, What the seven levels of human awareness are p1=5, What the seven levels of human awareness are p9=2sent/46w, Why it matters which level is running your week p2=7, Why it matters which level is run [truncated, 569 chars in all]
- `_to_delete/SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic.md` *(name prefix suggests a working file, not a drafted record)* — 3 breach: (opening) p1=6, Putting the empowerment dynamic into practice p1=1sent/17w, Putting the empowerment dynamic into practice p5=2sent/43w
- `helping-people-help-themselves.md` — 18 breach: (opening) p4=1sent/26w, Helping people help themselves was Egan's real point p1=2sent/31w, Helping people help themselves was Egan's real point p9=2sent/28w, Why this distinction actually matters p1=2sent/35w, Why this distinctio [truncated, 901 chars in all]

**external link to the source present: 2**

- `_to_delete/EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md` — 0 found
- `_to_delete/SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic.md` *(name prefix suggests a working file, not a drafted record)* — 0 found

**total body words: 2**

- `REPORT__Exemplar_Gate_Fixed_And_Row_152_Trim_Confirmed_S344.md` *(name prefix suggests a working file, not a drafted record)* — 856 (standard 1600 to 2400)
- `_to_delete/SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic.md` *(name prefix suggests a working file, not a drafted record)* — 864 (standard 1600 to 2400)

**voice: no paragraph describing the article: 2**

- `EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S344.md` — 1, opening 'You started this article inside a question you had not heard'
- `_to_delete/EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md` — 1, opening 'You started this article inside a question you had not heard'

**voice: opens speaking to the reader: 2**

- `REPORT__Exemplar_Gate_Fixed_And_Row_152_Trim_Confirmed_S344.md` *(name prefix suggests a working file, not a drafted record)* — **From:** Claude Cowork. **Date:** 8 September 2026.
- `SUPERSEDED__how-psychological-thinking-has-transformed-over-the-years.md` *(name prefix suggests a working file, not a drafted record)* — Ask someone what psychology is. They will probably describe

**article_type is the register value: 1**

- `SUPERSEDED__how-psychological-thinking-has-transformed-over-the-years.md` *(name prefix suggests a working file, not a drafted record)* — 'field-authority-article' (standard 'field-authority')

**description length: 1**

- `_to_delete/EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md` — 158 (max 155)

**every tag is one of the 36 locked slugs: 1**

- `SUPERSEDED__how-psychological-thinking-has-transformed-over-the-years.md` *(name prefix suggests a working file, not a drafted record)* — 3 outside the register: history-of-psychology, applied-psychology, cognitive-behavioural-psychology

**headed sections, counted not named: 1**

- `REPORT__Exemplar_Gate_Fixed_And_Row_152_Trim_Confirmed_S344.md` *(name prefix suggests a working file, not a drafted record)* — 3 found (standard 4)

**keyword density: 1**

- `_to_delete/SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic.md` *(name prefix suggests a working file, not a drafted record)* — 3.82% (11 hits, band 1.0 to 1.5)

**keyword unique in register: 1**

- `the-importance-of-self-awareness.md` — claimed by self-awareness

**no em or en dashes: 1**

- `_to_delete/SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic.md` *(name prefix suggests a working file, not a drafted record)* — 2 found

**no paragraph over 120 words: 1**

- `_to_delete/EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md` — p18=122

**outcome or problem tags, 2 to 4: 1**

- `SUPERSEDED__how-psychological-thinking-has-transformed-over-the-years.md` *(name prefix suggests a working file, not a drafted record)* — 0 found (attribute and modality tags not counted)

**reading ease (Flesch, approximate): 1**

- `REPORT__Exemplar_Gate_Fixed_And_Row_152_Trim_Confirmed_S344.md` *(name prefix suggests a working file, not a drafted record)* — 56.2 (band 60 to 70)

**record field block present: 1**

- `REPORT__Exemplar_Gate_Fixed_And_Row_152_Trim_Confirmed_S344.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found

**source_type is a value the ACF field offers: 1**

- `SUPERSEDED__how-psychological-thinking-has-transformed-over-the-years.md` *(name prefix suggests a working file, not a drafted record)* — 'salvage' (offered: legacy-page)

**voice: first heading does not repeat the title What is counselling?: 1**

- `what-is-counselling.md`

### help-answer (228 of 341 records fail)

**keyword in a subheading: 212**

- `HELP__achologist-adept.md` — 3 headings read
- `HELP__achologist-led-tutorials-alts.md` — 4 headings read
- `HELP__achologist-title-without-membership.md` — 4 headings read
- `HELP__achology-access-all-areas-pass.md` — 2 headings read
- `HELP__achology-accessibility-requirements.md` — 2 headings read
- `HELP__achology-automated-decision-making-profiling.md` — 4 headings read
- `HELP__achology-career-change-coaching-mentoring.md` — 3 headings read
- `HELP__achology-case-study-discussion-groups.md` — 4 headings read
- `HELP__achology-certificates-recognised-internationally.md` — 5 headings read
- `HELP__achology-certificates-vs-university-degrees.md` — 4 headings read
- `HELP__achology-certification-practice-competence.md` — 3 headings read
- `HELP__achology-change-mind-after-14-day-guarantee.md` — 2 headings read
- `HELP__achology-character-development.md` — 3 headings read
- `HELP__achology-coaching-competency-review-sessions.md` — 4 headings read
- `HELP__achology-code-character-conduct-ccac.md` — 3 headings read
- `HELP__achology-code-ethics.md` — 3 headings read
- `HELP__achology-community-rules-moderation.md` — 4 headings read
- `HELP__achology-content-offensive-emotionally-challenging.md` — 2 headings read
- `HELP__achology-copyright-sharing-course-content.md` — 3 headings read
- `HELP__achology-course-order-sequence.md` — 4 headings read
- `HELP__achology-course-outcomes.md` — 3 headings read
- `HELP__achology-course-piracy-copyright.md` — 3 headings read
- `HELP__achology-course-prerequisites-requirements.md` — 4 headings read
- `HELP__achology-course-required-attend-workshops.md` — 3 headings read
- `HELP__achology-courses-cpd-hours.md` — 2 headings read
- `HELP__achology-courses-other-languages.md` — 3 headings read
- `HELP__achology-customer-legal-rights-uk-consumer-law.md` — 3 headings read
- `HELP__achology-disagreement-open-discussion.md` — 4 headings read
- `HELP__achology-discounts-sales-promotions.md` — 3 headings read
- `HELP__achology-discussion-boundary-feels-unsafe.md` — 3 headings read
- `HELP__achology-discussion-spaces-groups-events.md` — 4 headings read
- `HELP__achology-evidence-based-humanistic-psychology.md` — 3 headings read
- `HELP__achology-free-trial-introductory-offer.md` — 4 headings read
- `HELP__achology-invite-link-not-working.md` — 3 headings read
- `HELP__achology-knowledge-hub-free-read.md` — 4 headings read
- `HELP__achology-knowledge-hub.md` — 5 headings read
- `HELP__achology-live-events-types.md` — 3 headings read
- `HELP__achology-live-practice-session-etiquette.md` — 4 headings read
- `HELP__achology-media-press-interview-requests.md` — 4 headings read
- `HELP__achology-members-host-workshops-events.md` — 3 headings read
- `HELP__achology-membership-free-coaching-included.md` — 4 headings read
- `HELP__achology-membership-refund.md` — 2 headings read
- `HELP__achology-multiple-psychology-traditions.md` — 3 headings read
- `HELP__achology-no-transformation-promises.md` — 3 headings read
- `HELP__achology-on-udemy-should-i-join-achology.md` — 3 headings read
- `HELP__achology-password-reset-email-not-arriving.md` — 4 headings read
- `HELP__achology-payment-methods.md` — 3 headings read
- `HELP__achology-peer-learning-community-teaches.md` — 3 headings read
- `HELP__achology-peer-learning-culture.md` — 4 headings read
- `HELP__achology-professional-indemnity-insurance.md` — 3 headings read
- `HELP__achology-recommended-practice-pathway.md` — 3 headings read
- `HELP__achology-refund-disagree-course-content.md` — 2 headings read
- `HELP__achology-refund-policy-explained.md` — 3 headings read
- `HELP__achology-refund-technical-issues.md` — 2 headings read
- `HELP__achology-responsible-community-member-advice.md` — 4 headings read
- `HELP__achology-s-character-code-based-aristotle.md` — 4 headings read
- `HELP__achology-s-five-community-principles.md` — 4 headings read
- `HELP__achology-s-nine-value-based-principles.md` — 4 headings read
- `HELP__achology-s-registered-company-details.md` — 4 headings read
- `HELP__achology-s-ten-value-commitments.md` — 4 headings read
- `HELP__achology-s-three-learning-paths.md` — 3 headings read
- `HELP__achology-success-stories-do-courses-work.md` — 3 headings read
- `HELP__achology-trust-legal-policies-work-together.md` — 3 headings read
- `HELP__achology-uk-register-learning-providers.md` — 3 headings read
- `HELP__achology-updates-course-already-purchased.md` — 4 headings read
- `HELP__achology-vs-icf-coaching-certification.md` — 3 headings read
- `HELP__achology-vs-linkedin-learning-comparison.md` — 3 headings read
- `HELP__achology-vs-school-of-life-comparison.md` — 3 headings read
- `HELP__achology-vs-tony-robbins-comparison.md` — 3 headings read
- `HELP__achology-vs-udemy-psychology-courses.md` — 2 headings read
- `HELP__any-achology-courses-appear-more-than.md` — 4 headings read
- `HELP__ask-questions-achology-community.md` — 4 headings read
- `HELP__become-a-master-achologist.md` — 3 headings read
- `HELP__become-an-achology-affiliate.md` — 3 headings read
- `HELP__become-instructor-contribute-content-achology.md` — 4 headings read
- `HELP__best-browsers-devices-achology-community.md` — 4 headings read
- `HELP__build-real-competence-achology.md` — 3 headings read
- `HELP__call-myself-certified-achology-credentials.md` — 3 headings read
- `HELP__call-myself-therapist-achology-courses.md` — 2 headings read
- `HELP__can-achology-suspend-terminate-access.md` — 4 headings read
- `HELP__cancel-achology-membership-anytime.md` — 3 headings read
- `HELP__cant-log-in-achology-community.md` — 3 headings read
- `HELP__cant-send-receive-messages-achology-community.md` — 4 headings read
- `HELP__ccac-green-red-status-mean.md` — 4 headings read
- `HELP__character-traits-define-achologist.md` — 4 headings read
- `HELP__choose-right-achology-event-level.md` — 4 headings read
- `HELP__cips-when-need-them.md` — 3 headings read
- `HELP__coaching-hot-seat.md` — 4 headings read
- `HELP__commit-practising-achologist.md` — 4 headings read
- `HELP__completed-achology-course-nothing-changed.md` — 3 headings read
- `HELP__course-completion-vs-competence.md` — 2 headings read
- `HELP__course-included-free-membership-happens-when.md` — 4 headings read
- `HELP__create-posts-achology-community.md` — 4 headings read
- `HELP__delete-achology-account-and-data.md` — 5 headings read
- `HELP__difference-between-code-ethics-ccac-community.md` — 4 headings read
- `HELP__dimap-course-upgrade.md` — 3 headings read
- `HELP__do-achology-courses-get-updated.md` — 3 headings read
- `HELP__does-achology-offer-a-money-back-guarantee.md` — 4 headings read
- `HELP__does-achology-offer-partnerships-collaborations.md` — 4 headings read
- `HELP__does-achology-sell-personal-data.md` — 4 headings read
- `HELP__does-achology-supervise-peer-coaching.md` — 3 headings read
- `HELP__download-achology-community-app.md` — 3 headings read
- `HELP__download-achology-course-materials.md` — 4 headings read
- `HELP__downloading-achology-content.md` — 3 headings read
- `HELP__earn-cpd-credit-hosting-session-only.md` — 4 headings read
- `HELP__evidence-cpd-learning-progression-achology.md` — 2 headings read
- `HELP__explain-achology-qualifications-to-clients.md` — 4 headings read
- `HELP__find-achology-course-resources.md` — 4 headings read
- `HELP__find-achology-members-similar-interests.md` — 4 headings read
- `HELP__fix-achology-community-notification-problems.md` — 3 headings read
- `HELP__fix-audio-video-achology-live-sessions.md` — 3 headings read
- `HELP__get-value-achology-mentorship-sessions.md` — 4 headings read
- `HELP__have-each-year-keep-master-achologist.md` — 4 headings read
- `HELP__have-retake-code-ethics-training-every.md` — 4 headings read
- `HELP__hidden-fees-additional-costs-achology.md` — 3 headings read
- `HELP__homework-assessment-achology-courses.md` — 3 headings read
- `HELP__host-own-achology-event.md` — 2 headings read
- `HELP__how-achology-courses-work-self-paced.md` — 4 headings read
- `HELP__how-long-achology-courses-take-timelines.md` — 4 headings read
- `HELP__how-long-achology-keeps-personal-data.md` — 4 headings read
- `HELP__how-long-achology-operating.md` — 3 headings read
- `HELP__how-long-achology-refund-process.md` — 3 headings read
- `HELP__how-much-does-achology-cost.md` — 5 headings read
- `HELP__how-psychology-became-institutionalised.md` — 3 headings read
- `HELP__how-to-contact-achology-support.md` — 4 headings read
- `HELP__how-to-join-live-achology-community-event.md` — 3 headings read
- `HELP__how-to-participate-achology-discussions-events.md` — 4 headings read
- `HELP__how-to-request-achology-refund.md` — 3 headings read
- `HELP__inside-achology-course-modules-breakdown.md` — 4 headings read
- `HELP__insurance-coverage-achology-qualifications.md` — 2 headings read
- `HELP__is-achology-a-university.md` — 3 headings read
- `HELP__is-achology-accredited-somap.md` — 3 headings read
- `HELP__is-achology-content-scientific-or-ideological.md` — 4 headings read
- `HELP__is-achology-educational-provider-or-professional-body.md` — 2 headings read
- `HELP__is-achology-global-platform.md` — 3 headings read
- `HELP__is-achology-right-emotionally-vulnerable.md` — 2 headings read
- `HELP__is-achology-suitable-for-beginners.md` — 4 headings read
- `HELP__is-achology-therapy-counselling-or-coaching.md` — 3 headings read
- `HELP__is-achology-worth-the-money.md` — 3 headings read
- `HELP__join-professional-body-after-achology.md` — 3 headings read
- `HELP__kain-ramsay-udemy-vs-achology-courses.md` — 3 headings read
- `HELP__key-milestones-achology-s-history.md` — 2 headings read
- `HELP__long-achology-valts-session.md` — 5 headings read
- `HELP__manage-achology-community-notifications.md` — 4 headings read
- `HELP__manipulative-pricing-tactics-achology-avoids.md` — 2 headings read
- `HELP__many-ccac-sessions-need-complete-often.md` — 4 headings read
- `HELP__many-courses-achology-offer-total.md` — 3 headings read
- `HELP__many-times-coach-same-person-cips.md` — 4 headings read
- `HELP__masterclasses-vs-practitioner-courses-differences.md` — 2 headings read
- `HELP__membership-first-or-course-first.md` — 4 headings read
- `HELP__membership-payment-fails-achology.md` — 2 headings read
- `HELP__mentoring-opportunities-achology-membership.md` — 4 headings read
- `HELP__mentorship-sessions-recorded-achology.md` — 3 headings read
- `HELP__navigate-achology-community-guide.md` — 3 headings read
- `HELP__nine-ccac-virtues.md` — 4 headings read
- `HELP__offer-free-coaching-someone-outside-achology.md` — 4 headings read
- `HELP__overwhelmed-by-achology-options.md` — 4 headings read
- `HELP__personal-progress-checklist-count-official-cpd.md` — 4 headings read
- `HELP__personal-responsibility-achology-learning.md` — 3 headings read
- `HELP__platform-changes-course-access-achology.md` — 3 headings read
- `HELP__post-nominal-letters-achology-certificates.md` — 2 headings read
- `HELP__principle-based-reflective-discussion.md` — 5 headings read
- `HELP__prior-qualifications-needed-achology.md` — 4 headings read
- `HELP__progress-member-achologist.md` — 3 headings read
- `HELP__psychology-as-practical-wisdom.md` — 3 headings read
- `HELP__realistic-outcomes-with-achology.md` — 3 headings read
- `HELP__revisit-achology-courses-after-completion.md` — 3 headings read
- `HELP__rsvp-join-achology-live-events.md` — 4 headings read
- `HELP__see-real-results-how-long-achology-takes.md` — 2 headings read
- `HELP__self-study-books-vs-achology-courses.md` — 4 headings read
- `HELP__senior-achologist-two-levels.md` — 2 headings read
- `HELP__share-achology-account-courses.md` — 3 headings read
- `HELP__share-my-achology-account-login.md` — 3 headings read
- `HELP__six-achology-cpd-statuses.md` — 4 headings read
- `HELP__slow-deep-learning-rejects-fast-certification.md` — 3 headings read
- `HELP__society-lost-gatekeeping-psychology.md` — 2 headings read
- `HELP__standards-apply-trainee-achologists.md` — 4 headings read
- `HELP__study-multiple-achology-courses-simultaneously.md` — 4 headings read
- `HELP__submit-cpd-credit-claim-hosting-attending.md` — 4 headings read
- `HELP__supervision-after-achology-training.md` — 3 headings read
- `HELP__transfer-kain-ramsay-udemy-courses-achology.md` — 3 headings read
- `HELP__upgrade-courses-bundle-access-pass.md` — 3 headings read
- `HELP__using-achology-content-branding-materials.md` — 3 headings read
- `HELP__valts-achology.md` — 4 headings read
- `HELP__verify-achology-certificate.md` — 3 headings read
- `HELP__what-achology-certificate-proves.md` — 2 headings read
- `HELP__what-does-achology-certification-qualify.md` — 2 headings read
- `HELP__what-does-achology-mean-becoming-wiser.md` — 3 headings read
- `HELP__what-does-achology-membership-include.md` — 3 headings read
- `HELP__what-if-achology-courses-dont-work.md` — 2 headings read
- `HELP__what-is-achology.md` — 5 headings read
- `HELP__what-is-applied-psychology-achology.md` — 3 headings read
- `HELP__what-is-circle-achology-community.md` — 4 headings read
- `HELP__what-makes-achology-different.md` — 3 headings read
- `HELP__what-personal-data-achology-collects.md` — 3 headings read
- `HELP__what-to-include-achology-support-request.md` — 5 headings read
- `HELP__where-can-i-learn-about-carl-rogers.md` — 5 headings read
- `HELP__where-can-i-learn-the-johari-window.md` — 6 headings read
- `HELP__where-is-achology-based.md` — 3 headings read
- `HELP__which-achology-company-am-actually-contracting.md` — 4 headings read
- `HELP__which-achology-events-earn-accreditation-credit.md` — 4 headings read
- `HELP__who-is-achology-designed-for.md` — 3 headings read
- `HELP__who-is-achology-not-for.md` — 4 headings read
- `HELP__who-is-kain-ramsay.md` — 3 headings read
- `HELP__who-runs-achology.md` — 3 headings read
- `HELP__who-verifies-achology-cpd-claims.md` — 4 headings read
- `HELP__why-achology-avoids-diagnostic-labels.md` — 2 headings read
- `HELP__why-achology-criticizes-psychology-teaching.md` — 2 headings read
- `HELP__why-achology-includes-community-course-prices.md` — 4 headings read
- `HELP__why-pay-achology-when-free-content-exists.md` — 3 headings read
- `HELP__will-clients-take-achology-certificate-seriously.md` — 3 headings read
- `HELP__will-employers-recognise-achology-certificate.md` — 3 headings read

**keyword in address slug: 153**

- `HELP__achologist-adept.md` — achologist-adept
- `HELP__achologist-title-without-membership.md` — achologist-title-without-membership
- `HELP__achology-access-all-areas-pass.md` — achology-access-all-areas-pass
- `HELP__achology-accessibility-requirements.md` — achology-accessibility-requirements
- `HELP__achology-automated-decision-making-profiling.md` — achology-automated-decision-making-profiling
- `HELP__achology-career-change-coaching-mentoring.md` — achology-career-change-coaching-mentoring
- `HELP__achology-certificates-vs-university-degrees.md` — achology-certificates-vs-university-degrees
- `HELP__achology-certification-practice-competence.md` — achology-certification-practice-competence
- `HELP__achology-change-mind-after-14-day-guarantee.md` — achology-change-mind-after-14-day-guarantee
- `HELP__achology-coaching-competency-review-sessions.md` — achology-coaching-competency-review-sessions
- `HELP__achology-code-character-conduct-ccac.md` — achology-code-character-conduct-ccac
- `HELP__achology-code-ethics.md` — achology-code-ethics
- `HELP__achology-community-rules-moderation.md` — achology-community-rules-moderation
- `HELP__achology-content-offensive-emotionally-challenging.md` — achology-content-offensive-emotionally-challenging
- `HELP__achology-copyright-sharing-course-content.md` — achology-copyright-sharing-course-content
- `HELP__achology-course-outcomes.md` — achology-course-outcomes
- `HELP__achology-course-piracy-copyright.md` — achology-course-piracy-copyright
- `HELP__achology-course-prerequisites-requirements.md` — achology-course-prerequisites-requirements
- `HELP__achology-course-required-attend-workshops.md` — achology-course-required-attend-workshops
- `HELP__achology-courses-cpd-hours.md` — achology-courses-cpd-hours
- `HELP__achology-courses-other-languages.md` — achology-courses-other-languages
- `HELP__achology-disagreement-open-discussion.md` — achology-disagreement-open-discussion
- `HELP__achology-discounts-sales-promotions.md` — achology-discounts-sales-promotions
- `HELP__achology-discussion-boundary-feels-unsafe.md` — achology-discussion-boundary-feels-unsafe
- `HELP__achology-discussion-spaces-groups-events.md` — achology-discussion-spaces-groups-events
- `HELP__achology-evidence-based-humanistic-psychology.md` — achology-evidence-based-humanistic-psychology
- `HELP__achology-knowledge-hub-free-read.md` — achology-knowledge-hub-free-read
- `HELP__achology-live-events-types.md` — achology-live-events-types
- `HELP__achology-media-press-interview-requests.md` — achology-media-press-interview-requests
- `HELP__achology-members-host-workshops-events.md` — achology-members-host-workshops-events
- `HELP__achology-membership-free-coaching-included.md` — achology-membership-free-coaching-included
- `HELP__achology-membership-refund.md` — achology-membership-refund
- `HELP__achology-multiple-psychology-traditions.md` — achology-multiple-psychology-traditions
- `HELP__achology-no-transformation-promises.md` — achology-no-transformation-promises
- `HELP__achology-on-udemy-should-i-join-achology.md` — achology-on-udemy-should-i-join-achology
- `HELP__achology-payment-methods.md` — achology-payment-methods
- `HELP__achology-professional-indemnity-insurance.md` — achology-professional-indemnity-insurance
- `HELP__achology-recommended-practice-pathway.md` — achology-recommended-practice-pathway
- `HELP__achology-refund-disagree-course-content.md` — achology-refund-disagree-course-content
- `HELP__achology-refund-policy-explained.md` — achology-refund-policy-explained
- `HELP__achology-refund-technical-issues.md` — achology-refund-technical-issues
- `HELP__achology-responsible-community-member-advice.md` — achology-responsible-community-member-advice
- `HELP__achology-s-character-code-based-aristotle.md` — achology-s-character-code-based-aristotle
- `HELP__achology-s-five-community-principles.md` — achology-s-five-community-principles
- `HELP__achology-s-nine-value-based-principles.md` — achology-s-nine-value-based-principles
- `HELP__achology-s-registered-company-details.md` — achology-s-registered-company-details
- `HELP__achology-s-three-learning-paths.md` — achology-s-three-learning-paths
- `HELP__achology-skill-development-workshops.md` — achology-skill-development-workshops
- `HELP__achology-success-stories-do-courses-work.md` — achology-success-stories-do-courses-work
- `HELP__achology-teaching-philosophy.md` — achology-teaching-philosophy
- `HELP__achology-trust-legal-policies-work-together.md` — achology-trust-legal-policies-work-together
- `HELP__achology-uk-register-learning-providers.md` — achology-uk-register-learning-providers
- `HELP__achology-updates-course-already-purchased.md` — achology-updates-course-already-purchased
- `HELP__any-achology-courses-appear-more-than.md` — any-achology-courses-appear-more-than
- `HELP__ask-questions-achology-community.md` — ask-questions-achology-community
- `HELP__become-an-achology-affiliate.md` — become-an-achology-affiliate
- `HELP__become-instructor-contribute-content-achology.md` — become-instructor-contribute-content-achology
- `HELP__best-browsers-devices-achology-community.md` — best-browsers-devices-achology-community
- `HELP__build-real-competence-achology.md` — build-real-competence-achology
- `HELP__call-myself-certified-achology-credentials.md` — call-myself-certified-achology-credentials
- `HELP__call-myself-therapist-achology-courses.md` — call-myself-therapist-achology-courses
- `HELP__can-achology-suspend-terminate-access.md` — can-achology-suspend-terminate-access
- `HELP__cant-log-in-achology-community.md` — cant-log-in-achology-community
- `HELP__cant-send-receive-messages-achology-community.md` — cant-send-receive-messages-achology-community
- `HELP__ccac-green-red-status-mean.md` — ccac-green-red-status-mean
- `HELP__choose-right-achology-event-level.md` — choose-right-achology-event-level
- `HELP__cips-when-need-them.md` — cips-when-need-them
- `HELP__commit-practising-achologist.md` — commit-practising-achologist
- `HELP__completed-achology-course-nothing-changed.md` — completed-achology-course-nothing-changed
- `HELP__course-included-free-membership-happens-when.md` — course-included-free-membership-happens-when
- `HELP__create-posts-achology-community.md` — create-posts-achology-community
- `HELP__difference-between-certificate-completion-certificate-achievement.md` — difference-between-certificate-completion-certificate-achievement
- `HELP__difference-between-code-ethics-ccac-community.md` — difference-between-code-ethics-ccac-community
- `HELP__does-achology-offer-partnerships-collaborations.md` — does-achology-offer-partnerships-collaborations
- `HELP__downloading-achology-content.md` — downloading-achology-content
- `HELP__earn-cpd-credit-hosting-session-only.md` — earn-cpd-credit-hosting-session-only
- `HELP__evidence-cpd-learning-progression-achology.md` — evidence-cpd-learning-progression-achology
- `HELP__find-achology-course-resources.md` — find-achology-course-resources
- `HELP__find-achology-members-similar-interests.md` — find-achology-members-similar-interests
- `HELP__fix-achology-community-notification-problems.md` — fix-achology-community-notification-problems
- `HELP__fix-audio-video-achology-live-sessions.md` — fix-audio-video-achology-live-sessions
- `HELP__get-value-achology-mentorship-sessions.md` — get-value-achology-mentorship-sessions
- `HELP__guest-speakers-policy.md` — guest-speakers-policy
- `HELP__have-each-year-keep-master-achologist.md` — have-each-year-keep-master-achologist
- `HELP__have-retake-code-ethics-training-every.md` — have-retake-code-ethics-training-every
- `HELP__hidden-fees-additional-costs-achology.md` — hidden-fees-additional-costs-achology
- `HELP__homework-assessment-achology-courses.md` — homework-assessment-achology-courses
- `HELP__host-own-achology-event.md` — host-own-achology-event
- `HELP__how-long-achology-operating.md` — how-long-achology-operating
- `HELP__how-long-achology-refund-process.md` — how-long-achology-refund-process
- `HELP__how-psychology-became-institutionalised.md` — how-psychology-became-institutionalised
- `HELP__how-to-contact-achology-support.md` — how-to-contact-achology-support
- `HELP__how-to-join-live-achology-community-event.md` — how-to-join-live-achology-community-event
- `HELP__how-to-participate-achology-discussions-events.md` — how-to-participate-achology-discussions-events
- `HELP__how-to-request-achology-refund.md` — how-to-request-achology-refund
- `HELP__inside-achology-course-modules-breakdown.md` — inside-achology-course-modules-breakdown
- `HELP__insurance-coverage-achology-qualifications.md` — insurance-coverage-achology-qualifications
- `HELP__is-achology-a-university.md` — is-achology-a-university
- `HELP__is-achology-content-scientific-or-ideological.md` — is-achology-content-scientific-or-ideological
- `HELP__is-achology-educational-provider-or-professional-body.md` — is-achology-educational-provider-or-professional-body
- `HELP__is-achology-global-platform.md` — is-achology-global-platform
- `HELP__is-achology-right-emotionally-vulnerable.md` — is-achology-right-emotionally-vulnerable
- `HELP__join-professional-body-after-achology.md` — join-professional-body-after-achology
- `HELP__key-milestones-achology-s-history.md` — key-milestones-achology-s-history
- `HELP__long-achology-valts-session.md` — long-achology-valts-session
- `HELP__manage-achology-community-notifications.md` — manage-achology-community-notifications
- `HELP__many-courses-achology-offer-total.md` — many-courses-achology-offer-total
- `HELP__many-times-coach-same-person-cips.md` — many-times-coach-same-person-cips
- `HELP__membership-payment-fails-achology.md` — membership-payment-fails-achology
- `HELP__mentoring-opportunities-achology-membership.md` — mentoring-opportunities-achology-membership
- `HELP__mentorship-sessions-recorded-achology.md` — mentorship-sessions-recorded-achology
- `HELP__navigate-achology-community-guide.md` — navigate-achology-community-guide
- `HELP__nine-ccac-virtues.md` — nine-ccac-virtues
- `HELP__overwhelmed-by-achology-options.md` — overwhelmed-by-achology-options
- `HELP__pals-earn-them.md` — pals-earn-them
- `HELP__personal-responsibility-achology-learning.md` — personal-responsibility-achology-learning
- `HELP__platform-changes-course-access-achology.md` — platform-changes-course-access-achology
- `HELP__post-nominal-letters-achology-certificates.md` — post-nominal-letters-achology-certificates
- `HELP__prior-qualifications-needed-achology.md` — prior-qualifications-needed-achology
- `HELP__progress-member-achologist.md` — progress-member-achologist
- `HELP__psychology-as-practical-wisdom.md` — psychology-as-practical-wisdom
- `HELP__rsvp-join-achology-live-events.md` — rsvp-join-achology-live-events
- `HELP__see-real-results-how-long-achology-takes.md` — see-real-results-how-long-achology-takes
- `HELP__senior-achologist-two-levels.md` — senior-achologist-two-levels
- `HELP__seven-marks-maturity-achology-teaches.md` — seven-marks-maturity-achology-teaches
- `HELP__share-achology-account-courses.md` — share-achology-account-courses
- `HELP__share-my-achology-account-login.md` — share-my-achology-account-login
- `HELP__six-achology-cpd-statuses.md` — six-achology-cpd-statuses
- `HELP__slow-deep-learning-rejects-fast-certification.md` — slow-deep-learning-rejects-fast-certification
- `HELP__society-lost-gatekeeping-psychology.md` — society-lost-gatekeeping-psychology
- `HELP__standards-apply-trainee-achologists.md` — standards-apply-trainee-achologists
- `HELP__transfer-kain-ramsay-udemy-courses-achology.md` — transfer-kain-ramsay-udemy-courses-achology
- `HELP__upgrade-courses-bundle-access-pass.md` — upgrade-courses-bundle-access-pass
- `HELP__using-achology-content-branding-materials.md` — using-achology-content-branding-materials
- `HELP__valts-achology.md` — valts-achology
- `HELP__verify-achology-certificate.md` — verify-achology-certificate
- `HELP__what-achology-certificate-proves.md` — what-achology-certificate-proves
- `HELP__what-does-achology-certification-qualify.md` — what-does-achology-certification-qualify
- `HELP__what-does-achology-mean-becoming-wiser.md` — what-does-achology-mean-becoming-wiser
- `HELP__what-if-achology-courses-dont-work.md` — what-if-achology-courses-dont-work
- `HELP__what-is-achology.md` — what-is-achology
- `HELP__what-is-applied-psychology-achology.md` — what-is-applied-psychology-achology
- `HELP__what-is-circle-achology-community.md` — what-is-circle-achology-community
- `HELP__what-personal-data-achology-collects.md` — what-personal-data-achology-collects
- `HELP__what-to-include-achology-support-request.md` — what-to-include-achology-support-request
- `HELP__where-can-i-learn-about-carl-rogers.md` — where-can-i-learn-about-carl-rogers
- `HELP__where-can-i-learn-the-johari-window.md` — where-can-i-learn-the-johari-window
- `HELP__who-is-achology-not-for.md` — who-is-achology-not-for
- `HELP__who-runs-achology.md` — who-runs-achology
- `HELP__why-achology-includes-community-course-prices.md` — why-achology-includes-community-course-prices
- `HELP__why-pay-achology-when-free-content-exists.md` — why-pay-achology-when-free-content-exists
- `HELP__will-clients-take-achology-certificate-seriously.md` — will-clients-take-achology-certificate-seriously
- `HELP__will-employers-recognise-achology-certificate.md` — will-employers-recognise-achology-certificate

**keyword density: 42**

- `HELP__achologist-led-tutorials-alts.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__achology-access-all-areas-pass.md` — 1.54% (1 hits, band 1.0 to 1.5)
- `HELP__achology-accessibility-requirements.md` — 1.60% (1 hits, band 1.0 to 1.5)
- `HELP__achology-certificates-recognised-internationally.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__achology-code-character-conduct-ccac.md` — 0.54% (1 hits, band 1.0 to 1.5)
- `HELP__achology-free-trial-introductory-offer.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__achology-invite-link-not-working.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__achology-password-reset-email-not-arriving.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__achology-payment-methods.md` — 1.59% (1 hits, band 1.0 to 1.5)
- `HELP__achology-skill-development-workshops.md` — 2.48% (2 hits, band 1.0 to 1.5)
- `HELP__achology-success-stories-do-courses-work.md` — 0.97% (1 hits, band 1.0 to 1.5)
- `HELP__achology-uk-register-learning-providers.md` — 2.36% (2 hits, band 1.0 to 1.5)
- `HELP__achology-vs-icf-coaching-certification.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__achology-vs-school-of-life-comparison.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__coaching-hot-seat.md` — 0.77% (1 hits, band 1.0 to 1.5)
- `HELP__course-completion-vs-competence.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__delete-achology-account-and-data.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__dimap-course-upgrade.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__do-achology-courses-get-updated.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__does-achology-offer-a-money-back-guarantee.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__does-achology-sell-personal-data.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__download-achology-community-app.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__how-much-does-achology-cost.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__is-achology-accredited-somap.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__is-achology-therapy-counselling-or-coaching.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__is-achology-worth-the-money.md` — 0.88% (1 hits, band 1.0 to 1.5)
- `HELP__kain-ramsay-udemy-vs-achology-courses.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__key-milestones-achology-s-history.md` — 0.99% (1 hits, band 1.0 to 1.5)
- `HELP__manipulative-pricing-tactics-achology-avoids.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__membership-first-or-course-first.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__pals-earn-them.md` — 1.94% (4 hits, band 1.0 to 1.5)
- `HELP__seven-marks-maturity-achology-teaches.md` — 1.89% (3 hits, band 1.0 to 1.5)
- `HELP__what-does-achology-membership-include.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__what-is-achology.md` — 0.81% (1 hits, band 1.0 to 1.5)
- `HELP__where-can-i-learn-about-carl-rogers.md` — 0.47% (1 hits, band 1.0 to 1.5)
- `HELP__where-can-i-learn-the-johari-window.md` — 0.41% (1 hits, band 1.0 to 1.5)
- `HELP__where-is-achology-based.md` — 0.54% (1 hits, band 1.0 to 1.5)
- `HELP__which-achology-company-am-actually-contracting.md` — 0.77% (1 hits, band 1.0 to 1.5)
- `HELP__who-is-achology-designed-for.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__who-is-kain-ramsay.md` — 0.84% (1 hits, band 1.0 to 1.5)
- `HELP__why-achology-criticizes-psychology-teaching.md` — 0.00% (0 hits, band 1.0 to 1.5)
- `HELP__will-life-coaches-be-replaced-by-ai.md` — 2.27% (2 hits, band 1.0 to 1.5)

**reading ease (Flesch, approximate): 32**

- `HELP__achology-case-study-discussion-groups.md` — 59.8 (band 60 to 70)
- `HELP__achology-certificates-recognised-internationally.md` — 38.4 (band 60 to 70)
- `HELP__achology-certificates-vs-university-degrees.md` — 36.2 (band 60 to 70)
- `HELP__achology-community-rules-moderation.md` — 50.0 (band 60 to 70)
- `HELP__achology-course-outcomes.md` — 51.8 (band 60 to 70)
- `HELP__achology-disagreement-open-discussion.md` — 52.4 (band 60 to 70)
- `HELP__achology-discussion-spaces-groups-events.md` — 70.7 (band 60 to 70)
- `HELP__achology-live-practice-session-etiquette.md` — 57.2 (band 60 to 70)
- `HELP__achology-media-press-interview-requests.md` — 46.5 (band 60 to 70)
- `HELP__achology-peer-learning-culture.md` — 43.1 (band 60 to 70)
- `HELP__achology-s-ten-value-commitments.md` — 46.0 (band 60 to 70)
- `HELP__achology-skill-development-workshops.md` — 57.1 (band 60 to 70)
- `HELP__become-instructor-contribute-content-achology.md` — 44.7 (band 60 to 70)
- `HELP__cant-send-receive-messages-achology-community.md` — 55.2 (band 60 to 70)
- `HELP__character-traits-define-achologist.md` — 45.9 (band 60 to 70)
- `HELP__find-achology-members-similar-interests.md` — 57.6 (band 60 to 70)
- `HELP__fix-audio-video-achology-live-sessions.md` — 59.1 (band 60 to 70)
- `HELP__have-each-year-keep-master-achologist.md` — 57.6 (band 60 to 70)
- `HELP__key-milestones-achology-s-history.md` — 56.6 (band 60 to 70)
- `HELP__long-achology-valts-session.md` — 56.1 (band 60 to 70)
- `HELP__manage-achology-community-notifications.md` — 55.9 (band 60 to 70)
- `HELP__mentoring-opportunities-achology-membership.md` — 44.4 (band 60 to 70)
- `HELP__nine-ccac-virtues.md` — 57.2 (band 60 to 70)
- `HELP__self-study-books-vs-achology-courses.md` — 58.3 (band 60 to 70)
- `HELP__senior-achologist-two-levels.md` — 58.4 (band 60 to 70)
- `HELP__what-is-achology.md` — 49.0 (band 60 to 70)
- `HELP__what-is-circle-achology-community.md` — 50.8 (band 60 to 70)
- `HELP__where-can-i-learn-about-carl-rogers.md` — 55.1 (band 60 to 70)
- `HELP__where-can-i-learn-the-johari-window.md` — 59.3 (band 60 to 70)
- `HELP__why-pay-achology-when-free-content-exists.md` — 51.1 (band 60 to 70)
- `HELP__will-employers-recognise-achology-certificate.md` — 33.0 (band 60 to 70)
- `RESEARCH__Course_Buying_Questions_Candidates_S356.md` — 50.8 (band 60 to 70)

**contractions: at least one in the body: 29**

- `HELP__achology-certificates-recognised-internationally.md` — 0 contractions, 5 uncontracted forms
- `HELP__achology-disagreement-open-discussion.md` — 0 contractions, 6 uncontracted forms
- `HELP__achology-discussion-spaces-groups-events.md` — 0 contractions, 5 uncontracted forms
- `HELP__achology-media-press-interview-requests.md` — 0 contractions, 5 uncontracted forms
- `HELP__achology-refund-technical-issues.md` — 0 contractions, 5 uncontracted forms
- `HELP__ask-questions-achology-community.md` — 0 contractions, 6 uncontracted forms
- `HELP__character-traits-define-achologist.md` — 0 contractions, 3 uncontracted forms
- `HELP__coaching-hot-seat.md` — 0 contractions, 4 uncontracted forms
- `HELP__download-achology-course-materials.md` — 0 contractions, 1 uncontracted forms
- `HELP__fix-audio-video-achology-live-sessions.md` — 0 contractions, 2 uncontracted forms
- `HELP__have-each-year-keep-master-achologist.md` — 0 contractions, 3 uncontracted forms
- `HELP__hidden-fees-additional-costs-achology.md` — 0 contractions, 3 uncontracted forms
- `HELP__how-long-achology-refund-process.md` — 0 contractions, 5 uncontracted forms
- `HELP__how-to-join-live-achology-community-event.md` — 0 contractions, 5 uncontracted forms
- `HELP__key-milestones-achology-s-history.md` — 0 contractions, 1 uncontracted forms
- `HELP__manage-achology-community-notifications.md` — 0 contractions, 4 uncontracted forms
- `HELP__navigate-achology-community-guide.md` — 0 contractions, 6 uncontracted forms
- `HELP__nine-ccac-virtues.md` — 0 contractions, 7 uncontracted forms
- `HELP__overwhelmed-by-achology-options.md` — 0 contractions, 9 uncontracted forms
- `HELP__revisit-achology-courses-after-completion.md` — 0 contractions, 1 uncontracted forms
- `HELP__senior-achologist-two-levels.md` — 0 contractions, 1 uncontracted forms
- `HELP__upgrade-courses-bundle-access-pass.md` — 0 contractions, 4 uncontracted forms
- `HELP__what-is-achology.md` — 0 contractions, 5 uncontracted forms
- `HELP__what-is-circle-achology-community.md` — 0 contractions, 5 uncontracted forms
- `HELP__where-can-i-learn-about-carl-rogers.md` — 0 contractions, 1 uncontracted forms
- `HELP__where-can-i-learn-the-johari-window.md` — 0 contractions, 7 uncontracted forms
- `HELP__why-pay-achology-when-free-content-exists.md` — 0 contractions, 15 uncontracted forms
- `HELP__will-employers-recognise-achology-certificate.md` — 0 contractions, 5 uncontracted forms
- `RESEARCH__Course_Buying_Questions_Candidates_S356.md` — 0 contractions, 12 uncontracted forms

**keyword verbatim in first 10% of body: 24**

- `HELP__achologist-led-tutorials-alts.md`
- `HELP__achology-certificates-recognised-internationally.md`
- `HELP__achology-free-trial-introductory-offer.md`
- `HELP__achology-invite-link-not-working.md`
- `HELP__achology-password-reset-email-not-arriving.md`
- `HELP__achology-vs-icf-coaching-certification.md`
- `HELP__achology-vs-school-of-life-comparison.md`
- `HELP__course-completion-vs-competence.md`
- `HELP__delete-achology-account-and-data.md`
- `HELP__dimap-course-upgrade.md`
- `HELP__do-achology-courses-get-updated.md`
- `HELP__does-achology-offer-a-money-back-guarantee.md`
- `HELP__does-achology-sell-personal-data.md`
- `HELP__download-achology-community-app.md`
- `HELP__guest-speakers-policy.md`
- `HELP__how-much-does-achology-cost.md`
- `HELP__is-achology-accredited-somap.md`
- `HELP__is-achology-therapy-counselling-or-coaching.md`
- `HELP__kain-ramsay-udemy-vs-achology-courses.md`
- `HELP__manipulative-pricing-tactics-achology-avoids.md`
- `HELP__membership-first-or-course-first.md`
- `HELP__what-does-achology-membership-include.md`
- `HELP__who-is-achology-designed-for.md`
- `HELP__why-achology-criticizes-psychology-teaching.md`

**no paragraph over 60 words or 3 sentences: 14**

- `HELP__achologist-adept.md` — longest 77 words, 7 sentences; 1 over: p3=77w/7s
- `HELP__achology-certificates-vs-university-degrees.md` — longest 49 words, 4 sentences; 1 over: p13=30w/4s
- `HELP__become-a-life-coach.md` — longest 57 words, 4 sentences; 1 over: p11=54w/4s
- `HELP__cbt-practitioner-vs-cbt-therapist.md` — longest 75 words, 4 sentences; 3 over: p12=40w/4s, p16=75w/4s, p17=54w/4s
- `HELP__have-each-year-keep-master-achologist.md` — longest 73 words, 5 sentences; 1 over: p2=73w/5s
- `HELP__how-long-achology-courses-take-timelines.md` — longest 57 words, 5 sentences; 1 over: p11=40w/5s
- `HELP__key-milestones-achology-s-history.md` — longest 203 words, 14 sentences; 1 over: p3=203w/14s
- `HELP__mentoring-opportunities-achology-membership.md` — longest 45 words, 4 sentences; 1 over: p14=31w/4s
- `HELP__overwhelmed-by-achology-options.md` — longest 60 words, 4 sentences; 1 over: p3=30w/4s
- `HELP__what-does-an-nlp-course-cover.md` — longest 60 words, 4 sentences; 1 over: p31=51w/4s
- `HELP__what-makes-a-good-nlp-course.md` — longest 58 words, 4 sentences; 1 over: p20=52w/4s
- `HELP__where-can-i-learn-about-carl-rogers.md` — longest 113 words, 5 sentences; 1 over: p7=113w/5s
- `HELP__where-can-i-learn-the-johari-window.md` — longest 154 words, 9 sentences; 3 over: p4=51w/4s, p8=154w/9s, p12=35w/4s
- `RESEARCH__Course_Buying_Questions_Candidates_S356.md` — longest 357 words, 13 sentences; 12 over: p2=75w/3s, p3=105w/3s, p4=110w/6s, p5=212w/9s, p6=357w/13s, p7=107w/3s

**'actually' at most once (Kain, S381): 13**

- `HELP__achology-certificates-vs-university-degrees.md` — 2 found
- `HELP__achology-s-ten-value-commitments.md` — 2 found
- `HELP__best-cbt-course-or-certification.md` — 5 found
- `HELP__coaching-hot-seat.md` — 2 found
- `HELP__how-to-start-learning-cbt.md` — 4 found
- `HELP__is-a-cbt-certification-worth-it.md` — 10 found
- `HELP__manage-achology-community-notifications.md` — 2 found
- `HELP__membership-first-or-course-first.md` — 2 found
- `HELP__mentoring-opportunities-achology-membership.md` — 2 found
- `HELP__realistic-outcomes-with-achology.md` — 2 found
- `HELP__what-does-a-cbt-course-cover.md` — 6 found
- `HELP__where-can-i-learn-the-johari-window.md` — 2 found
- `RESEARCH__Course_Buying_Questions_Candidates_S356.md` — 2 found

**description length: 3**

- `HELP__achology-teaching-philosophy.md` — 157 (max 155)
- `HELP__where-can-i-learn-about-carl-rogers.md` — 168 (max 155)
- `HELP__where-can-i-learn-the-johari-window.md` — 177 (max 155)

**outcome or problem tags, 2 to 4: 3**

- `HELP__cbt-practitioner-vs-cbt-therapist.md` — 0 found (attribute and modality tags not counted)
- `HELP__where-can-i-learn-about-carl-rogers.md` — 0 found (attribute and modality tags not counted)
- `HELP__where-can-i-learn-the-johari-window.md` — 0 found (attribute and modality tags not counted)

**stage 0 demand evidence recorded: 3**

- `HELP__cbt-practitioner-vs-cbt-therapist.md`
- `HELP__where-can-i-learn-about-carl-rogers.md`
- `HELP__where-can-i-learn-the-johari-window.md`

**keyword in first 120 chars of description: 2**

- `HELP__where-is-achology-based.md` — 145 chars
- `HELP__who-is-kain-ramsay.md` — 149 chars

**no one-sentence paragraph (Kain, S361): 2**

- `HELP__what-is-achology.md` — 2: p3, p12
- `RESEARCH__Course_Buying_Questions_Candidates_S356.md` — 20: p1, p11, p12, p13, p14, p15, p17, p19

**no paragraph over 120 words: 2**

- `HELP__key-milestones-achology-s-history.md` — p3=203
- `HELP__where-can-i-learn-the-johari-window.md` — p8=154

**SEO title length: 1**

- `HELP__download-achology-community-app.md` — 65 (max 60)

**keyword in first 50 chars of SEO title: 1**

- `HELP__achology-certificates-recognised-internationally.md` — 53 chars

**machine-written tells: 1**

- `RESEARCH__Course_Buying_Questions_Candidates_S356.md` — plainly

**record field block present: 1**

- `RESEARCH__Course_Buying_Questions_Candidates_S356.md` — no '## Page fields' table found

**total body words: 1**

- `RESEARCH__Course_Buying_Questions_Candidates_S356.md` — 2030 (standard 320 to 1500)

**voice: no paragraph describing the article: 1**

- `HELP__what-does-an-nlp-course-cover.md` — 1, e.g. 'It closes with'

### hub-guide

No failing lines (29 of 29 records pass).

### hub-question-article (1 of 58 records fail)

**paragraphs of 3 to 4 sentences, or 50+ words: 1**

- `EXEMPLAR__can-i-practise-cbt-on-my-own__APPROVED_S374.md` — 7 breach: (opening) p2=7, (opening) p3=2sent/36w, What it looks like in real life p1=5, What it looks like in real life p2=8, What it looks like in real life p3=6, Where it gets hard p2=5, Open items, before this could publish p1=11

**reading ease (Flesch, approximate): 1**

- `EXEMPLAR__can-i-practise-cbt-on-my-own__APPROVED_S374.md` — 77.1 (band 60 to 70)

**record field block present: 1**

- `EXEMPLAR__can-i-practise-cbt-on-my-own__APPROVED_S374.md` — no '## Page fields' table found

**voice: no paragraph describing the article: 1**

- `EXEMPLAR__can-i-practise-cbt-on-my-own__APPROVED_S374.md` — 1, opening '- Not run: content_gate.py, the Search and Citation Brief, h'

**voice: opens speaking to the reader: 1**

- `EXEMPLAR__can-i-practise-cbt-on-my-own__APPROVED_S374.md` — **KAIN'S RULING, S374, Monday 21 September 2026, after readi

### instructor-article (45 of 139 records fail)

**machine-written tells: 31**

- `KAREN_SOURCE_LESSONS_S344.md` — paradigm, to summarise, truly
- `all-progression-is-impossible-without-change.md` — truly
- `balance-the-main-areas-of-life.md` — truly
- `can-you-be-too-self-aware.md` — truly
- `can-you-choose-to-be-more-introverted-or-extroverted.md` — truly
- `change-is-the-only-constant.md` — truly
- `confuse-opinions-with-facts.md` — truly
- `connected-to-your-future-self.md` — truly
- `cover-up-incompetence-with-head-knowledge.md` — truly
- `disagreement-vs-division.md` — truly
- `every-decision-is-a-trade-off.md` — truly
- `everyone-experiences-reality-differently.md` — truly
- `feeling-stuck-in-life.md` — truly
- `fixed-or-growth-mindset.md` — truly
- `forget-your-mistakes-but-remember-their-lessons.md` — truly
- `fountain-or-a-drain.md` — truly
- `freedom-vs-security.md` — truly
- `happiness-is-a-delusion-fulfilment-is-not.md` — truly
- `living-according-to-your-values.md` — truly
- `pattern-recognition-superpower.md` — truly
- `positive-vs-negative-motivation.md` — truly
- `rational-or-emotional-thinker.md` — truly
- `remembered-for.md` — truly
- `saying-less-more-influential.md` — truly
- `self-acceptance-vs-self-improvement.md` — truly
- `taking-responsibility-creates-personal-growth.md` — truly
- `think-objectively.md` — truly
- `thoughts-and-emotions-connection.md` — truly
- `types-of-listening.md` — truly
- `whats-the-key-to-winning-hearts-and-minds.md` — truly
- `your-relationship-with-money-tells-a-story.md` — truly

**'actually' at most once (Kain, S381): 18**

- `I14__meaningful-life-versus-busy-life.md` — 5 found
- `I18__persuade-someone-who-disagrees.md` — 2 found
- `K10__growth-mindset-at-work.md` — 12 found
- `KAREN_SOURCE_LESSONS_S344.md` — 2 found
- `assumptions-damage-relationships.md` — 20 found
- `doctors-have-only-minutes-to-diagnose.md` — 2 found
- `feeling-stuck-in-life.md` — 13 found
- `growing-or-standing-still.md` — 13 found
- `happiness-is-a-delusion-fulfilment-is-not.md` — 2 found
- `labels-vs-true-identity.md` — 13 found
- `personal-growth-requires-discomfort.md` — 10 found
- `positive-vs-negative-motivation.md` — 13 found
- `stages-of-building-strong-relationships.md` — 10 found
- `stages-of-human-development-and-maturity.md` — 15 found
- `step-outside-your-comfort-zone.md` — 19 found
- `thoughts-and-emotions-connection.md` — 2 found
- `time-perspective.md` — 10 found
- `turn-a-vision-into-a-goal.md` — 19 found

**paragraphs of 3 to 4 sentences, or 50+ words: 2**

- `KAREN_SOURCE_LESSONS_S344.md` — 1 breach: (opening) p1=2sent/21w
- `does-a-diagnosis-do-to-the-person.md` — 1 breach: (opening) p5=5

**reading ease (Flesch, approximate): 2**

- `KAREN_SOURCE_LESSONS_S344.md` — -503.2 (band 60 to 70)
- `feeling-stuck-in-life.md` — 59.8 (band 60 to 70)

**banned brand words: 1**

- `KAREN_SOURCE_LESSONS_S344.md` — empowerment

**record field block present: 1**

- `KAREN_SOURCE_LESSONS_S344.md` — no '## Page fields' table found

**total body words: 1**

- `KAREN_SOURCE_LESSONS_S344.md` — 9598 (standard 1200 to 2200)

**voice: opens speaking to the reader: 1**

- `KAREN_SOURCE_LESSONS_S344.md` — **Written by:** Claude Cowork, S344, 6 September 2026.

### quote-page (182 of 457 records fail)

**unexpected section: 186**

- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — Gate result, every piece, from the real script run on the real files
- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — Judgment calls, named rather than silently taken
- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — Pieces drafted (5 of 33)
- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — Status line
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — Content-safety exclusions
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — Corpus collision checks
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — Production and register notes
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing and attribution
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — Verification table
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — What this batch does not close
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — What this batch is
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was drafted
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was found drafting each record
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was screened and set aside
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — Content-safety exclusions
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — Corpus collision checks
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — Production and register notes
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing and attribution
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — Verification table
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — What this batch does not close
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — What this batch is
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was drafted
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was found drafting each record
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was screened and set aside
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — Continuing
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — Corpus collision checks
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing and attribution
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — Verification table
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — What this batch does not close
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was drafted
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was found drafting each record
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — Why eight, not a fixed number
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — Corpus collision checks
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — Pieces drafted (8)
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing and attribution: course 001 is a mixed monologue and dialogue course
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — The production rule this batch confirms: keyword length and occurrence count, against the density band
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — What this batch does not close
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was found, drafting each record
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — Corpus collision checks
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — Pieces drafted
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing and attribution
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — What this batch does not close
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was found drafting each record
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — Why five, not a fixed number
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — Next
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — Not advanced this pass, seen but not actioned
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — State of the register and the board
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — The one decision put to Kain, and what it settled
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — What this batch is
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — What this pass found and fixed, batch-wide
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — Lecture 051: three candidates, three thematic-proximity drops, no exact collision among them
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — Lecture 122: dropped for a fault not named before this batch, a collision with the session's own new output
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — Lecture 123, and half of lecture 115: dropped for an over-mined rhetorical template
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — Selection and collision checks run before drafting
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing: every record in this batch came from a wholly unused lecture number
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — Support files synced to the device
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — The keyword and closing-question constraints, applied by pre-verification
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — The remaining pool, recomputed against the live corpus after this batch
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — What was found, drafting each record
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — A drafting note worth carrying forward
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — H1 and closing question, by record
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — Pieces corrected
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — Verbatim gate output, all nine
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — What changed on every record
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — What is left
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — Word count, density, and reading ease, by record
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — Content-safety exclusions
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — Corpus collision checks
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — Production and register notes
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing and attribution
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — Verification table
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — What this batch does not close
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — What this batch is
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was drafted
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was found drafting each record
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — What was screened and set aside
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — A same-transcript misattribution risk, found and excluded: the Machiavelli line in lectures 052 and 053
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — Lecture 058: one candidate considered, dropped for failing to stand alone
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — Lecture 129: dropped entirely as structurally unsuitable
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — Selection and attribution checks run before drafting
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing: all six records came from the last six genuinely unread lecture numbers
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — Support files synced to the device
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — The keyword and closing-question constraints, applied by pre-verification
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — The lecture 059 collision investigation, resolved
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — The pool, closed
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — Two further candidates dropped inside lectures 052 and 053, for a collision already found in batch fourteen's own investigation
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — What this batch does not close
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — What was found, drafting each record
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — A process change worth naming
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — H1 and closing question, by record
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — Pieces corrected
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — Verbatim gate output, all ten
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — What changed on every record
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — What is left, and a scope conflict worth naming (unchanged this batch)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — Word count, density, and reading ease, by record
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — A gap in the skill's own description, worth flagging
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — H1 and closing question, by record
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — Pieces corrected
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — Verbatim gate output, all ten
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — What changed on every record
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — What is left, and a scope conflict worth naming
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — Word count, density, and reading ease, by record
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — Gate result, every piece, from the real script, run fresh against the live files
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — H1 and closing question, one line per record
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — One thing outside this batch's scope, worth flagging: the quote-page skill's worked example is stale
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — Pieces corrected (10 of 10)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — Scope: this batch is ten records, not twenty-six, and that is a call Cowork made, not Kain
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — Status
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — The character count, counted by script on every record, not by eye
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — The density-pattern exception: not needed on any of the ten
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — What is left, named and not started
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — Why this batch needed more than opener and closing question, unlike batch one
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — Correction, S356: the opening line rewritten fresh on all ten, per Kain's ruling
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — Gate result, every piece, from the real script, run fresh against the live files
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — H1 and closing question, one line per record
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — Open items, named rather than silently closed
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — Pieces corrected (10 of 10)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — Status line
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — Status line (supersedes the one above)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — The character count, counted by script on every record, not by eye
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — The density-pattern exception: not needed on any of the ten
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — Named, not fixed this batch, and what it means for the records still needed
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — Selection and collision checks run before drafting
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing: why this batch is smaller, and what was found reaching it
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — Support files synced to the device
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — The keyword and closing-question constraints, applied by pre-verification
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — Two candidates dropped for a verbatim sentence-boundary fault, not a collision
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — What was found, drafting each record
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — How the 30 were fixed
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — Named, not fixed this batch
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — The reflection question field, checked and closed
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — The thirteen fixed in this session's visible working history
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — What was found
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — Named, not fixed this batch
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — Selection and collision checks run before drafting
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing: a new transcript location found this batch
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — Support files synced to the device
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — The collisions checked and avoided
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — The keyword-length rule, applied and extended
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — What was found, drafting each record
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — Named, not fixed this batch
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — Selection and collision checks run before drafting
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — Sourcing: lecture selection this batch
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — Support files synced to the device
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — The collisions checked and avoided
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — The keyword and closing-question constraints, applied by pre-verification
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — What was found, drafting each record
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — A standing question closed, not carried forward
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — How the 25 were fixed
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — Named, not fixed this batch
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — The collision found and fixed
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — What was found
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — How the 15 were fixed
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — Named, not fixed this batch
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — Production and register
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — Support files synced to the device
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — The collision found and fixed
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — What was found
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — Full gate printout, all 26 records
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — One further observation, not fixed here
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — The internal-link defect found and fixed on all 26
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — The one expected, permanent exception
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — Verification
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — What changed, on every one of the 26
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — Working files

**'actually' at most once (Kain, S381): 140**

- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — 9 found
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — 4 found
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — 16 found
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — 3 found
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — 2 found
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — 5 found
- `CQ001-002-1__why-you-dont-know-it-all-yet.md` — 2 found
- `CQ001-002-2__why-every-effect-in-your-life-has-a-cause.md` — 4 found
- `CQ001-005-1__why-what-you-think-is-true-might-not-be.md` — 4 found
- `CQ001-006-1__why-simple-ideas-are-always-harder-to-explain.md` — 2 found
- `CQ001-006-2__why-being-a-contributor-beats-being-a-consumer.md` — 4 found
- `CQ001-007-1__why-being-reflective-beats-being-a-great-thinker.md` — 6 found
- `CQ001-008-1__why-simple-ideas-alone-drive-real-behavior-change.md` — 4 found
- `CQ001-009-1__why-your-perspective-shapes-the-questions-you-ask.md` — 4 found
- `CQ001-009-2__why-the-way-you-see-things-differs-from-reality.md` — 5 found
- `CQ001-011-3__what-it-actually-means-to-live-a-virtuous-life.md` — 5 found
- `CQ001-012-1__why-you-have-beliefs-even-without-knowing-it.md` — 6 found
- `CQ001-015-1__why-we-talk-ourselves-out-of-what-we-want.md` — 2 found
- `CQ001-017-1__why-we-feel-uncomfortable-in-our-own-skin.md` — 5 found
- `CQ001-018-1__why-the-philosophy-you-live-by-actually-matters.md` — 9 found
- `CQ001-019-1__why-we-can-only-find-meaning-in-our-past.md` — 5 found
- `CQ001-021-1__why-your-brain-can-only-focus-on-one-thing.md` — 3 found
- `CQ001-025-1__why-we-keep-following-rules-we-never-question.md` — 2 found
- `CQ001-026-1__why-we-become-like-the-people-we-try-to-avoid.md` — 8 found
- `CQ001-030-1__why-we-only-remember-what-matters-to-us.md` — 4 found
- `CQ001-034-1__why-how-we-treat-others-is-always-a-choice.md` — 4 found
- `CQ001-035-1__why-you-are-always-choosing-connection-or-not.md` — 3 found
- `CQ001-036-1__why-you-cannot-grow-beyond-what-you-are-exposed-to.md` — 3 found
- `CQ001-037-1__why-our-beliefs-are-just-glorified-ideas-we-hold.md` — 7 found
- `CQ001-039-1__why-your-core-values-shape-every-decision-you-make.md` — 5 found
- `CQ001-040-1__why-you-do-not-need-to-be-miles-ahead.md` — 2 found
- `CQ001-042-1__why-looking-back-should-never-mean-living-there.md` — 2 found
- `CQ001-043-1__why-people-only-change-when-they-want-to.md` — 7 found
- `CQ001-044-1__why-being-more-self-aware-shapes-your-influence.md` — 4 found
- `CQ001-047-1__why-we-stop-trying-to-break-free-from-limits.md` — 5 found
- `CQ001-048-1__why-the-relationships-you-keep-shape-your-life.md` — 6 found
- `CQ001-049-1__why-self-awareness-comes-before-personal-growth.md` — 7 found
- `CQ001-050-1__why-you-can-only-teach-what-you-have-lived.md` — 3 found
- `CQ001-051-1__why-personal-growth-is-a-choice-not-an-accident.md` — 2 found
- `CQ001-052-1__why-reflective-conversation-cannot-be-rushed.md` — 2 found
- `CQ001-053-1__why-your-public-self-hides-your-private-one.md` — 4 found
- `CQ001-054-1__why-growth-in-life-depends-on-your-awareness.md` — 9 found
- `CQ001-055-1__why-self-awareness-should-be-your-top-priority.md` — 4 found
- `CQ001-056-1__why-faith-is-an-outlook-on-life.md` — 5 found
- `CQ001-058-1__why-holding-onto-the-past-holds-you-back.md` — 5 found
- `CQ001-059-1__why-frustration-lands-on-the-wrong-target.md` — 8 found
- `CQ001-061-1__why-we-transfer-old-feelings-onto-new-people.md` — 5 found
- `CQ001-062-1__why-that-weight-isnt-yours-to-carry.md` — 4 found
- `CQ001-063-1__why-we-fight-to-be-understood-instead-of-listening.md` — 4 found
- `CQ001-064-1__why-only-you-decide-how-deep-to-grow.md` — 7 found
- `CQ001-065-1__why-being-yourself-is-the-biggest-risk.md` — 6 found
- `CQ001-070-1__why-reflection-is-the-real-engine-of-growth.md` — 4 found
- `CQ001-079-1__why-feeling-broken-does-not-mean-you-are-broken.md` — 4 found
- `CQ001-082-1__why-identity-and-personality-are-not-the-same.md` — 3 found
- `CQ001-082-2__why-you-need-a-vision-for-who-you-become.md` — 4 found
- `CQ001-085-1__why-we-all-miscommunicate-even-when-we-care.md` — 4 found
- `CQ001-086-1__why-getting-people-is-easier-than-keeping-them.md` — 4 found
- `CQ001-088-1__why-you-can-choose-how-long-you-carry-it.md` — 3 found
- `CQ001-090-1__why-your-beliefs-put-a-cap-on-your-potential.md` — 6 found
- `CQ001-090-2__how-to-understand-behavior-without-endorsing-it.md` — 4 found
- `CQ001-091-1__why-you-should-build-your-life-on-principles.md` — 4 found
- `CQ001-094-1__why-unsolicited-advice-feels-patronizing.md` — 10 found
- `CQ001-098-1__why-your-response-determines-your-inner-experience.md` — 7 found
- `CQ001-101-1__why-forgiving-someone-is-about-freeing-you-too.md` — 7 found
- `CQ001-109-1__why-the-truth-confronts-who-we-really-are.md` — 6 found
- `CQ001-115-1__why-a-theory-is-not-the-same-as-truth.md` — 6 found
- `CQ001-119-1__why-simple-ideas-matter-more-than-complex-ones.md` — 9 found
- `CQ001-123-1__why-inner-conflict-means-you-do-not-know-yourself.md` — 2 found
- `CQ001-137-1__why-being-humble-makes-a-person-more-attractive.md` — 2 found
- `CQ001-138-1__why-your-fear-is-always-about-the-future.md` — 6 found
- `CQ001-154-1__why-trying-to-prove-yourself-wrong-helps-you-grow.md` — 6 found
- `CQ001-157-1__why-judging-others-is-really-a-defense-mechanism.md` — 6 found
- `CQ001-170-1__why-your-family-shaped-whether-you-feel-at-peace.md` — 3 found
- `CQ001-172-1__why-realising-you-have-a-choice-changes-everything.md` — 7 found
- `CQ001-173-1__why-you-should-not-keep-your-growth-to-yourself.md` — 9 found
- `CQ001-175-1__why-people-are-only-honest-once-they-trust-you.md` — 4 found
- `CQ018-001-1__why-we-take-courses-to-be-challenged-not-soothed.md` — 3 found
- `CQ018-002-2__why-wanting-what-you-lack-can-lead-to-sadness.md` — 2 found
- `CQ018-002-3__why-maturity-means-severing-our-dependency-on-other-people.md` — 2 found
- `CQ018-005-1__why-thinking-like-a-winner-is-where-it-starts.md` — 3 found
- `CQ018-017-2__why-most-of-your-thoughts-are-not-true.md` — 3 found
- `CQ018-022-1__why-applying-what-you-learn-is-what-learning-means.md` — 11 found
- `CQ018-050-1__why-personal-growth-is-rarely-a-joyous-process.md` — 3 found
- `CQ018-053-1__why-your-character-shows-most-when-no-one-watches.md` — 5 found
- `CQ018-054-1__why-what-simmers-beneath-the-surface-undermines-us.md` — 3 found
- `CQ018-059-1__why-managing-your-emotions-is-work-that-never-ends.md` — 6 found
- `CQ018-060-1__why-your-life-runs-on-fumes-without-giving-back.md` — 6 found
- `CQ018-061-1__why-staying-angry-at-others-costs-you-so-much.md` — 5 found
- `CQ018-063-1__why-our-beliefs-are-just-guesses-or-ideas-at-best.md` — 5 found
- `CQ018-063-2__why-so-few-of-us-actually-know-what-we-believe.md` — 8 found
- `CQ018-064-1__why-we-assume-that-what-we-think-is-true.md` — 6 found
- `CQ018-069-2__why-life-eventually-becomes-about-other-people.md` — 2 found
- `CQ018-071-2__living-life-defined-by-labels-that-they-assign.md` — 7 found
- `CQ018-074-1__why-its-easier-to-diagnose-people-than-to-understand-them.md` — 5 found
- `CQ018-076-1__why-people-pleasing-is-false-friendliness.md` — 2 found
- `CQ018-077-1__why-peace-must-be-the-umpire-of-every-decision.md` — 5 found
- `CQ018-077-2__why-self-control-has-to-precede-our-own-growth.md` — 3 found
- `CQ018-078-2__why-youre-not-determined-by-anyone-else.md` — 4 found
- `CQ018-079-1__why-what-you-do-always-outweighs-what-you-say.md` — 5 found
- `CQ018-081-1__why-belief-drives-your-wellbeing.md` — 2 found
- `CQ018-082-1__why-you-are-your-own-harshest-critic.md` — 4 found
- `CQ018-082-2__choosing-to-be-part-of-the-solution.md` — 5 found
- `CQ018-083-1__why-not-every-thought-is-a-universal-truth.md` — 6 found
- `CQ018-084-1__why-maturity-is-not-associated-with-age.md` — 4 found
- `CQ018-086-2__why-you-cant-trust-a-scared-person.md` — 3 found
- `CQ018-087-1__why-trust-is-the-foundation-of-every-relationship.md` — 5 found
- `CQ018-087-2__how-learning-from-mistakes-makes-you-more-valuable.md` — 3 found
- `CQ018-088-1__why-assumptions-are-the-killer-of-human-connectedness.md` — 9 found
- `CQ018-088-2__what-happens-when-dialogue-becomes-disrespectful.md` — 2 found
- `CQ018-090-1__what-is-the-real-mark-of-maturity.md` — 4 found
- `CQ018-090-2__what-it-means-to-let-dead-things-stay-dead.md` — 5 found
- `CQ018-091-2__why-we-compromise-our-integrity-to-keep-the-peace.md` — 8 found
- `CQ018-093-1__why-being-right-is-not-the-point-at-all.md` — 7 found
- `CQ018-094-1__why-needing-to-be-a-hero-hides-your-insecurity.md` — 4 found
- `CQ018-095-1__what-one-shift-in-perspective-can-actually-change.md` — 5 found
- `CQ018-095-2__why-you-are-more-than-your-past.md` — 3 found
- `CQ018-096-1__why-we-become-the-relationships-that-we-keep.md` — 6 found
- `CQ018-096-2__why-experience-gives-us-authority-in-life.md` — 5 found
- `CQ018-097-2__why-no-teacher-can-make-you-learn.md` — 4 found
- `CQ018-100-1__why-a-blamer-hides-loneliness-behind-a-tough-mask.md` — 3 found
- `CQ018-101-1__why-no-mountain-gives-you-the-fulfillment-you-seek.md` — 11 found
- `CQ018-103-1__why-telling-the-truth-is-what-leads-to-trust.md` — 11 found
- `CQ018-104-1__why-real-peace-begins-once-you-accept-each-other.md` — 7 found
- `CQ018-105-1__why-hardship-produces-growth-when-nothing-else-does.md` — 4 found
- `CQ018-105-2__why-trust-plus-time-is-the-real-intimacy-formula.md` — 7 found
- `CQ018-108-2__why-how-you-respond-matters-more-than-what-occurs.md` — 8 found
- `CQ018-110-2__why-knowing-facts-is-not-the-same-as-understanding.md` — 5 found
- `CQ018-111-1__why-youre-not-entitled-to-peoples-trust.md` — 2 found
- `CQ018-116-1__why-how-you-use-today-must-always-be-purposeful.md` — 6 found
- `CQ018-117-1__why-you-get-distressed-by-what-you-focus-on.md` — 4 found
- `CQ018-118-1__why-freedom-is-always-simply-a-choice-you-make.md` — 3 found
- `CQ018-119-1__why-real-understanding-ends-all-tension-in-a-bond.md` — 3 found
- `CQ018-120-1__why-simplicity-is-key-to-a-highly-effective-life.md` — 8 found
- `CQ018-124-1__why-practice-does-not-make-perfect.md` — 3 found
- `CQ018-125-1__why-how-people-feel-is-always-their-real-problem.md` — 5 found
- `CQ018-126-1__why-discipline-is-what-turns-a-plan-into-action.md` — 8 found
- `CQ018-128-1__the-relief-in-not-having-it-all-together.md` — 3 found
- `_to_delete/CQ001-044-1__why-knowing-yourself-shapes-how-you-influence-others.md` — 4 found
- `_to_delete/CQ001-094-1__why-unsolicited-advice-always-comes-across-as-patronizing.md` — 9 found
- `_to_delete/CQ001-101-1__why-owning-your-choices-makes-you-feel-empowered.md` — 4 found

**machine-written tells: 63**

- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — plainly
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — plainly
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — truly
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — truly
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — plainly, truly
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — plainly
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — plainly, truly
- `CQ001-002-2__why-every-effect-in-your-life-has-a-cause.md` — truly
- `CQ001-007-1__why-being-reflective-beats-being-a-great-thinker.md` — truly
- `CQ001-016-1__why-not-every-idea-is-true.md` — truly
- `CQ001-019-1__why-we-can-only-find-meaning-in-our-past.md` — truly
- `CQ001-021-1__why-your-brain-can-only-focus-on-one-thing.md` — truly
- `CQ001-025-1__why-we-keep-following-rules-we-never-question.md` — truly
- `CQ001-027-1__why-family-is-your-first-culture.md` — truly
- `CQ001-030-1__why-we-only-remember-what-matters-to-us.md` — truly
- `CQ001-031-1__why-you-overreact-to-things-that-seem-small.md` — truly
- `CQ001-034-1__why-how-we-treat-others-is-always-a-choice.md` — truly
- `CQ001-039-1__why-your-core-values-shape-every-decision-you-make.md` — truly
- `CQ001-043-1__why-people-only-change-when-they-want-to.md` — truly
- `CQ001-047-1__why-we-stop-trying-to-break-free-from-limits.md` — truly
- `CQ001-050-1__why-you-can-only-teach-what-you-have-lived.md` — truly
- `CQ001-055-1__why-self-awareness-should-be-your-top-priority.md` — truly
- `CQ001-060-1__why-we-channel-conflict-into-something-productive.md` — truly
- `CQ001-062-1__why-that-weight-isnt-yours-to-carry.md` — truly
- `CQ001-063-1__why-we-fight-to-be-understood-instead-of-listening.md` — truly
- `CQ001-066-1__why-you-feel-out-of-sync-with-yourself.md` — truly
- `CQ001-074-1__why-you-react-to-traits-and-not-people.md` — truly
- `CQ001-085-1__why-we-all-miscommunicate-even-when-we-care.md` — truly
- `CQ001-090-2__how-to-understand-behavior-without-endorsing-it.md` — truly
- `CQ001-094-1__why-unsolicited-advice-feels-patronizing.md` — truly
- `CQ001-104-1__why-innovators-get-more-respect-than-imitators-do.md` — truly
- `CQ001-108-1__why-you-are-always-for-or-against-yourself.md` — truly
- `CQ001-115-1__why-a-theory-is-not-the-same-as-truth.md` — truly
- `CQ001-117-1__why-real-growth-happens-outside-your-comfort-zone.md` — truly
- `CQ001-118-1__why-a-value-drives-every-choice-we-make.md` — truly
- `CQ001-122-1__why-excitement-is-not-the-same-as-motivation.md` — truly
- `CQ001-123-1__why-inner-conflict-means-you-do-not-know-yourself.md` — truly
- `CQ001-124-1__why-we-so-often-confuse-confidence-with-arrogance.md` — truly
- `CQ001-127-1__why-defending-our-beliefs-too-rigidly-isolates-us.md` — truly
- `CQ001-128-1__why-empathy-holds-relationships-together.md` — truly
- `CQ001-129-1__why-no-one-wakes-up-wanting-to-hurt-you.md` — truly
- `CQ001-135-1__why-accepting-disorder-costs-you-peace.md` — truly
- `CQ001-137-1__why-being-humble-makes-a-person-more-attractive.md` — truly
- `CQ001-138-1__why-your-fear-is-always-about-the-future.md` — truly
- `CQ001-141-1__why-good-depends-on-values.md` — truly
- `CQ001-145-1__why-connection-determines-your-peace.md` — truly
- `CQ001-150-1__why-normal-is-different-for-everyone.md` — truly
- `CQ001-155-1__why-we-judge-others.md` — truly
- `CQ001-157-1__why-judging-others-is-really-a-defense-mechanism.md` — truly
- `CQ001-160-1__why-we-feel-threatened-by-others.md` — truly
- `CQ001-169-1__why-some-people-overcome-hardship.md` — truly
- `CQ001-170-1__why-your-family-shaped-whether-you-feel-at-peace.md` — truly
- `CQ001-173-1__why-you-should-not-keep-your-growth-to-yourself.md` — truly
- `CQ018-022-1__why-applying-what-you-learn-is-what-learning-means.md` — truly
- `CQ018-074-1__why-its-easier-to-diagnose-people-than-to-understand-them.md` — truly
- `CQ018-093-1__why-being-right-is-not-the-point-at-all.md` — truly
- `CQ018-095-2__why-you-are-more-than-your-past.md` — truly
- `CQ018-096-2__why-experience-gives-us-authority-in-life.md` — truly
- `CQ018-097-2__why-no-teacher-can-make-you-learn.md` — truly
- `CQ018-100-1__why-a-blamer-hides-loneliness-behind-a-tough-mask.md` — truly
- `CQ018-110-2__why-knowing-facts-is-not-the-same-as-understanding.md` — truly
- `CQ018-120-1__why-simplicity-is-key-to-a-highly-effective-life.md` — truly
- `_to_delete/CQ001-094-1__why-unsolicited-advice-always-comes-across-as-patronizing.md` — truly

**paragraphs of 3 to 4 sentences, or 50+ words: 36**

- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — 5 breach: Pieces drafted (5 of 33) p1=5, Pieces drafted (5 of 33) p2=2sent/27w, Judgment calls, named rather than silently taken p3=5, Status line p1=1sent/42w, Status line p2=2sent/43w
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — 11 breach: What was drafted p1=16, Sourcing and attribution p1=1sent/48w, Sourcing and attribution p2=1sent/6w, Content-safety exclusions p1=1sent/23w, Content-safety exclusions p2=10, Corpus collision checks p1=2sent/25w, Corpus collision  [truncated, 422 chars in all]
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — 8 breach: What was drafted p1=16, Sourcing and attribution p1=1sent/48w, Sourcing and attribution p2=1sent/16w, Content-safety exclusions p1=1sent/21w, Corpus collision checks p1=2sent/23w, Corpus collision checks p2=5, What was found draft [truncated, 305 chars in all]
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — 5 breach: What was drafted p2=16, Sourcing and attribution p1=1sent/41w, Sourcing and attribution p3=1sent/36w, What was found drafting each record p1=6, Verification table p1=1sent/46w
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — 6 breach: Pieces drafted (8) p1=8, Pieces drafted (8) p2=2sent/26w, The production rule this batch confirms: keyword length and occurrence count, against the density band p2=5, What was found, drafting each record p1=1sent/8w, What was foun [truncated, 305 chars in all]
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — 10 breach: (opening) p1=2sent/39w, Pieces drafted p1=1sent/17w, Pieces drafted p2=5, Sourcing and attribution p1=1sent/18w, Corpus collision checks p1=1sent/30w, Corpus collision checks p2=5, What was found drafting each record p1=1sent/28w [truncated, 371 chars in all]
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — 5 breach: What this pass found and fixed, batch-wide p1=19, The one decision put to Kain, and what it settled p3=5, Verification p1=2sent/38w, State of the register and the board p2=1sent/40w, Next p1=2sent/14w
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — 7 breach: (opening) p2=1sent/15w, Lecture 051: three candidates, three thematic-proximity drops, no exact collision among them p1=8, Selection and collision checks run before drafting p3=1sent/34w, What was found, drafting each record p1=2s [truncated, 387 chars in all]
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — 19 breach: Pieces corrected p2=1sent/12w, Verbatim gate output, all nine p2=6, Verbatim gate output, all nine p3=1sent/2w, Verbatim gate output, all nine p5=6, Verbatim gate output, all nine p6=1sent/2w, Verbatim gate output, all nine p8=6, [truncated, 781 chars in all]
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — 11 breach: What was drafted p1=14, What was drafted p2=1sent/29w, Sourcing and attribution p1=1sent/46w, Sourcing and attribution p2=1sent/6w, Content-safety exclusions p1=1sent/22w, Content-safety exclusions p2=8, What was screened and set [truncated, 429 chars in all]
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — 8 breach: Sourcing: all six records came from the last six genuinely unread lecture numbers p1=5, Lecture 058: one candidate considered, dropped for failing to stand alone p1=5, Selection and attribution checks run before drafting p3=7, Wha [truncated, 463 chars in all]
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — 23 breach: Pieces corrected p2=1sent/12w, A process change worth naming p1=5, Verbatim gate output, all ten p2=7, Verbatim gate output, all ten p3=1sent/2w, Verbatim gate output, all ten p5=6, Verbatim gate output, all ten p6=1sent/2w, Verb [truncated, 965 chars in all]
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — 24 breach: Pieces corrected p2=1sent/36w, A gap in the skill's own description, worth flagging p1=8, Verbatim gate output, all ten p2=7, Verbatim gate output, all ten p3=1sent/2w, Verbatim gate output, all ten p5=6, Verbatim gate output, al [truncated, 1019 chars in all]
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — 29 breach: Scope: this batch is ten records, not twenty-six, and that is a call Cowork made, not Kain p2=5, Pieces corrected (10 of 10) p1=10, Why this batch needed more than opener and closing question, unlike batch one p2=1sent/11w, Why t [truncated, 2583 chars in all]
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — 72 breach: Pieces corrected (10 of 10) p1=10, The character count, counted by script on every record, not by eye p2=1sent/9w, The density-pattern exception: not needed on any of the ten p1=6, Gate result, every piece, from the real script,  [truncated, 6445 chars in all]
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — 6 breach: (opening) p2=1sent/31w, Two candidates dropped for a verbatim sentence-boundary fault, not a collision p2=6, Two candidates dropped for a verbatim sentence-boundary fault, not a collision p3=5, Selection and collision checks run b [truncated, 356 chars in all]
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — 8 breach: (opening) p1=1sent/36w, The thirteen fixed in this session's visible working history p1=2sent/41w, Verification p1=1sent/25w, Verification p2=2sent/29w, Production and register p1=2sent/40w, Named, not fixed this batch p1=2sent/28 [truncated, 325 chars in all]
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — 2 breach: Selection and collision checks run before drafting p2=5, Selection and collision checks run before drafting p3=1sent/36w
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — 4 breach: Selection and collision checks run before drafting p2=5, Selection and collision checks run before drafting p3=1sent/35w, What was found, drafting each record p5=5, Production and register p1=2sent/39w
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — 4 breach: (opening) p1=1sent/34w, How the 25 were fixed p4=1sent/43w, How the 25 were fixed p6=1sent/32w, Verification p1=1sent/30w
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — 8 breach: What was found p5=1sent/24w, What was found p6=1sent/49w, What was found p7=1sent/45w, How the 15 were fixed p2=6, How the 15 were fixed p5=1sent/44w, How the 15 were fixed p6=8, The collision found and fixed p1=2sent/32w, Product [truncated, 269 chars in all]
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — 82 breach: (opening) p1=1sent/12w, (opening) p2=6, The internal-link defect found and fixed on all 26 p1=5, Verification p2=1sent/14w, Full gate printout, all 26 records p1=1sent/1w, Full gate printout, all 26 records p3=7, Full gate printo [truncated, 3770 chars in all]
- `CQ001-002-1__why-you-dont-know-it-all-yet.md` — 8 breach: (opening) p1=2sent/45w, (opening) p3=1sent/39w, What the Quote Might Be Saying p6=2sent/33w, What Can We Take Away From It? p1=2sent/47w, What Can We Take Away From It? p2=2sent/35w, What Can We Take Away From It? p4=2sent/36w, Wh [truncated, 333 chars in all]
- `CQ001-002-2__why-every-effect-in-your-life-has-a-cause.md` — 9 breach: (opening) p1=2sent/49w, (opening) p3=1sent/29w, What the Quote Might Be Saying p3=2sent/37w, What the Quote Might Be Saying p6=2sent/40w, What Can We Take Away From It? p1=2sent/37w, What Can We Take Away From It? p2=2sent/33w, Wh [truncated, 385 chars in all]
- `CQ001-005-1__why-what-you-think-is-true-might-not-be.md` — 10 breach: (opening) p1=2sent/47w, (opening) p3=1sent/25w, What the Quote Might Be Saying p3=2sent/28w, What the Quote Might Be Saying p4=2sent/43w, What the Quote Might Be Saying p6=2sent/21w, What the Quote Might Be Saying p8=2sent/46w, W [truncated, 424 chars in all]
- `CQ001-006-1__why-simple-ideas-are-always-harder-to-explain.md` — 6 breach: (opening) p3=1sent/28w, What the Quote Might Be Saying p2=2sent/36w, What Can We Take Away From It? p1=2sent/30w, What Can We Take Away From It? p5=2sent/37w, What Can We Take Away From It? p6=2sent/26w, A Question Worthy of an Ho [truncated, 264 chars in all]
- `CQ001-006-2__why-being-a-contributor-beats-being-a-consumer.md` — 9 breach: (opening) p3=2sent/26w, What the Quote Might Be Saying p2=2sent/35w, What the Quote Might Be Saying p6=2sent/37w, What the Quote Might Be Saying p7=2sent/37w, What the Quote Might Be Saying p8=2sent/33w, What Can We Take Away From [truncated, 399 chars in all]
- `CQ001-007-1__why-being-reflective-beats-being-a-great-thinker.md` — 7 breach: (opening) p1=2sent/40w, (opening) p3=1sent/31w, What the Quote Might Be Saying p1=2sent/24w, What Can We Take Away From It? p2=2sent/25w, What Can We Take Away From It? p3=2sent/38w, What Can We Take Away From It? p5=2sent/37w, A  [truncated, 288 chars in all]
- `CQ001-008-1__why-simple-ideas-alone-drive-real-behavior-change.md` — 7 breach: (opening) p3=1sent/29w, What the Quote Might Be Saying p2=2sent/37w, What the Quote Might Be Saying p7=2sent/24w, What Can We Take Away From It? p1=2sent/35w, What Can We Take Away From It? p5=2sent/34w, What Can We Take Away From [truncated, 309 chars in all]
- `CQ001-011-3__what-it-actually-means-to-live-a-virtuous-life.md` — 10 breach: (opening) p1=2sent/48w, (opening) p3=2sent/24w, What the Quote Might Be Saying p1=2sent/30w, What Can We Take Away From It? p1=2sent/38w, What Can We Take Away From It? p2=1sent/31w, What Can We Take Away From It? p3=2sent/29w, W [truncated, 431 chars in all]
- `CQ001-013-1__how-a-persistent-thought-can-become-your-reality.md` — 6 breach: (opening) p1=2sent/42w, (opening) p3=1sent/26w, What the Quote Might Be Saying p7=2sent/22w, What the Quote Might Be Saying p8=2sent/45w, What Can We Take Away From It? p5=2sent/37w, A Question Worthy of an Honest Answer p2=1sent/ [truncated, 243 chars in all]
- `CQ001-017-1__why-we-feel-uncomfortable-in-our-own-skin.md` — 8 breach: (opening) p3=1sent/29w, What the Quote Might Be Saying p1=2sent/33w, What the Quote Might Be Saying p4=2sent/35w, What Can We Take Away From It? p1=2sent/36w, What Can We Take Away From It? p5=2sent/14w, What Can We Take Away From [truncated, 361 chars in all]
- `CQ001-054-1__why-growth-in-life-depends-on-your-awareness.md` — 5 breach: (opening) p1=2sent/39w, (opening) p3=1sent/37w, What the Quote Might Be Saying p1=2sent/28w, What Can We Take Away From It? p1=2sent/34w, A Question Worthy of an Honest Answer p2=1sent/12w
- `CQ001-090-1__why-your-beliefs-put-a-cap-on-your-potential.md` — 8 breach: (opening) p3=1sent/36w, What the Quote Might Be Saying p1=2sent/27w, What the Quote Might Be Saying p3=2sent/48w, What the Quote Might Be Saying p7=2sent/24w, What Can We Take Away From It? p1=2sent/30w, What Can We Take Away From [truncated, 354 chars in all]
- `CQ001-090-2__how-to-understand-behavior-without-endorsing-it.md` — 7 breach: (opening) p1=2sent/33w, (opening) p3=1sent/31w, What the Quote Might Be Saying p1=2sent/25w, What the Quote Might Be Saying p5=2sent/25w, What the Quote Might Be Saying p6=2sent/35w, What Can We Take Away From It? p5=2sent/32w, A  [truncated, 288 chars in all]
- `CQ018-088-2__what-happens-when-dialogue-becomes-disrespectful.md` — 1 breach: What the Quote Might Be Saying p3=2sent/33w

**voice: the quoted person is not narrated: 33**

- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — the record carries no quote_author
- `CQ001-007-1__why-being-reflective-beats-being-a-great-thinker.md` — 1, e.g. 'Kain says'
- `CQ001-016-1__why-not-every-idea-is-true.md` — 2, e.g. 'Kain Ramsay said'
- `CQ001-051-1__why-personal-growth-is-a-choice-not-an-accident.md` — 1, e.g. 'Kain Ramsay puts it'
- `CQ001-052-1__why-reflective-conversation-cannot-be-rushed.md` — 1, e.g. 'Kain Ramsay says'
- `CQ001-054-1__why-growth-in-life-depends-on-your-awareness.md` — 1, e.g. 'Kain describes'
- `CQ001-060-1__why-we-channel-conflict-into-something-productive.md` — 1, e.g. 'Kain describes'
- `CQ001-110-1__why-it-is-possible-to-see-yourself-objectively.md` — 1, e.g. 'Kain describes'
- `CQ001-148-1__why-you-can-manage-prejudice.md` — 1, e.g. 'Kain says'
- `CQ001-150-1__why-normal-is-different-for-everyone.md` — 1, e.g. 'Kain Ramsay said'
- `CQ001-170-1__why-your-family-shaped-whether-you-feel-at-peace.md` — 1, e.g. 'Kain describes'
- `CQ001-171-1__why-you-dont-need-anything-from-society.md` — 1, e.g. 'Kain Ramsay describes'

**a 'Put this into practice' block (Kain, S356): 22**

- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — the practice field is empty

**reading ease (Flesch, approximate): 22**

- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — 58.2 (band 60 to 70)
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — 55.3 (band 60 to 70)
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — 52.3 (band 60 to 70)
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — 53.9 (band 60 to 70)
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — 53.8 (band 60 to 70)
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — 55.3 (band 60 to 70)
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — 53.4 (band 60 to 70)
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — 53.0 (band 60 to 70)
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — 43.0 (band 60 to 70)
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — 44.1 (band 60 to 70)
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — 49.2 (band 60 to 70)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — 43.7 (band 60 to 70)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — 46.7 (band 60 to 70)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — 51.9 (band 60 to 70)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — 53.3 (band 60 to 70)
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — 40.3 (band 60 to 70)
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — 50.8 (band 60 to 70)
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — 49.2 (band 60 to 70)
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — 38.5 (band 60 to 70)
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — 45.6 (band 60 to 70)
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — 48.3 (band 60 to 70)
- `_to_delete/CQ001-044-1__why-knowing-yourself-shapes-how-you-influence-others.md` — 57.2 (band 60 to 70)

**record field block present: 22**

- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found

**section headings, verbatim and in order: 22**

- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — found 4
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — found 10
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — found 10
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — found 9
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — found 8
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — found 8
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — found 7
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — found 11
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — found 7
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — found 10
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — found 14
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — found 7
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — found 7
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — found 10
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — found 9
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — found 9
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — found 7
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — found 9
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — found 9
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — found 7
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — found 7
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — found 7

**the body ends on the reflection question: 22**

- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '*', not a question mark
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '*', not a question mark
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '*', not a question mark
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '.', not a question mark
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — the last sentence ends '`', not a question mark

**total body words: 20**

- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* — 1964 (standard 650 to 825)
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* — 1697 (standard 650 to 825)
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* — 1230 (standard 650 to 825)
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* — 1284 (standard 650 to 825)
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* — 1075 (standard 650 to 825)
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — 1182 (standard 650 to 825)
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* — 1552 (standard 650 to 825)
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* — 5641 (standard 650 to 825)
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* — 1846 (standard 650 to 825)
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* — 2071 (standard 650 to 825)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* — 6187 (standard 650 to 825)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* — 6355 (standard 650 to 825)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* — 6819 (standard 650 to 825)
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* — 11542 (standard 650 to 825)
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* — 1914 (standard 650 to 825)
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* — 1665 (standard 650 to 825)
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* — 1821 (standard 650 to 825)
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* — 1371 (standard 650 to 825)
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* — 1701 (standard 650 to 825)
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — 14685 (standard 650 to 825)

**practice block within 40 to 60 words: 3**

- `_to_delete/CQ001-044-1__why-knowing-yourself-shapes-how-you-influence-others.md` — 30 words
- `_to_delete/CQ001-094-1__why-unsolicited-advice-always-comes-across-as-patronizing.md` — 21 words
- `_to_delete/CQ001-101-1__why-owning-your-choices-makes-you-feel-empowered.md` — 23 words

**keyword in first 50 chars of SEO title: 2**

- `_to_delete/CQ001-044-1__why-knowing-yourself-shapes-how-you-influence-others.md` — 52 chars
- `_to_delete/CQ001-094-1__why-unsolicited-advice-always-comes-across-as-patronizing.md` — 57 chars

**banned brand words: 1**

- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* — empowerment

**no em or en dashes: 1**

- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* — 3 found

**voice: no paragraph describing the article: 1**

- `CQ001-006-2__why-being-a-contributor-beats-being-a-consumer.md` — 1, e.g. 'this article'

### seven-beliefs-series (12 of 12 records fail)

**outcome or problem tags, 2 to 4: 9**

- `PART_01__the-seven-beliefs-achology-is-built-on.md` — 0 found (attribute and modality tags not counted)
- `PART_02__can-people-change.md` — 0 found (attribute and modality tags not counted)
- `PART_03__know-thyself.md` — 0 found (attribute and modality tags not counted)
- `PART_04__thinking-errors.md` — 0 found (attribute and modality tags not counted)
- `PART_05__understanding-and-managing-emotions.md` — 0 found (attribute and modality tags not counted)
- `PART_06__emotional-responsibility.md` — 0 found (attribute and modality tags not counted)
- `PART_07__change-your-life-from-the-inside-out.md` — 0 found (attribute and modality tags not counted)
- `PART_08__sense-of-purpose.md` — 0 found (attribute and modality tags not counted)
- `PART_09__philosophy-of-life.md` — 0 found (attribute and modality tags not counted)

**machine-written tells: 4**

- `Batch_Report__Seven_Beliefs_Back_Links_S387.md` *(name prefix suggests a working file, not a drafted record)* — truly
- `Batch_Report__Seven_Beliefs_Parts_1_And_2_S387.md` *(name prefix suggests a working file, not a drafted record)* — truly
- `Batch_Report__Seven_Beliefs_Parts_3_To_9_S387.md` *(name prefix suggests a working file, not a drafted record)* — truly
- `PART_02__can-people-change.md` — truly

**voice: opens speaking to the reader: 4**

- `Batch_Report__Seven_Beliefs_Back_Links_S387.md` *(name prefix suggests a working file, not a drafted record)* — **From:** Claude Cowork, Monday 28 September 2026. **Answers
- `Batch_Report__Seven_Beliefs_Parts_1_And_2_S387.md` *(name prefix suggests a working file, not a drafted record)* — **From:** Claude Cowork, run of Monday 28 September 2026. **
- `PART_01__the-seven-beliefs-achology-is-built-on.md` — *Part 1 of 9: Introduction, standing on the shoulders of gia
- `PART_09__philosophy-of-life.md` — *Part 9 of 9: How the seven beliefs fit together.*

**'actually' at most once (Kain, S381): 3**

- `Batch_Report__Seven_Beliefs_Back_Links_S387.md` *(name prefix suggests a working file, not a drafted record)* — 75 found
- `Batch_Report__Seven_Beliefs_Parts_1_And_2_S387.md` *(name prefix suggests a working file, not a drafted record)* — 2 found
- `Batch_Report__Seven_Beliefs_Parts_3_To_9_S387.md` *(name prefix suggests a working file, not a drafted record)* — 9 found

**record field block present: 3**

- `Batch_Report__Seven_Beliefs_Back_Links_S387.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Seven_Beliefs_Parts_1_And_2_S387.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found
- `Batch_Report__Seven_Beliefs_Parts_3_To_9_S387.md` *(name prefix suggests a working file, not a drafted record)* — no '## Page fields' table found

**headed sections, counted not named: 2**

- `Batch_Report__Seven_Beliefs_Parts_1_And_2_S387.md` *(name prefix suggests a working file, not a drafted record)* — 12 found (standard 6 to 11)
- `Batch_Report__Seven_Beliefs_Parts_3_To_9_S387.md` *(name prefix suggests a working file, not a drafted record)* — 5 found (standard 6 to 11)

**reading ease (Flesch, approximate): 2**

- `Batch_Report__Seven_Beliefs_Parts_3_To_9_S387.md` *(name prefix suggests a working file, not a drafted record)* — 48.5 (band 60 to 70)
- `PART_01__the-seven-beliefs-achology-is-built-on.md` — 73.1 (band 60 to 70)

**total body words: 2**

- `Batch_Report__Seven_Beliefs_Back_Links_S387.md` *(name prefix suggests a working file, not a drafted record)* — 27214 (standard 2500 to 3700)
- `Batch_Report__Seven_Beliefs_Parts_3_To_9_S387.md` *(name prefix suggests a working file, not a drafted record)* — 4726 (standard 2500 to 3700)

**banned brand words: 1**

- `Batch_Report__Seven_Beliefs_Parts_3_To_9_S387.md` *(name prefix suggests a working file, not a drafted record)* — empowerment

**no paragraph over 120 words: 1**

- `PART_01__the-seven-beliefs-achology-is-built-on.md` — p12=153, p14=124, p25=123, p27=138, p28=123

### workbook (1 of 1 records fail)

**'actually' at most once (Kain, S381): 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — 2 found

**author is a key the people registry holds: 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — Base voice, no pen name; assigned at commission per the workbook field group's own key

**every tag is one of the 36 locked slugs: 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — 1 outside the register: To be confirmed at commission

**external link to the source present: 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — 0 found

**keyword density: 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — 0.00% (0 hits, band 1.0 to 1.5)

**keyword in a subheading: 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — 4 headings read

**keyword verbatim in first 10% of body: 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md`

**landing page body present: 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — the record carries no landing_page_body

**outcome or problem tags, 2 to 4: 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — 0 found (attribute and modality tags not counted)

**paragraphs of 3 to 4 sentences, or 50+ words: 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — 26 breach: (opening) p1=1sent/4w, (opening) p3=2sent/29w, (opening) p4=1sent/8w, (opening) p5=1sent/43w, (opening) p6=1sent/22w, (opening) p7=1sent/12w, Part One: The teaching p6=2sent/27w, Part One: The teaching p7=2sent/31w, Part Two: The [truncated, 901 chars in all]

**required fields present (22): 1**

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` — 2 missing: landing_page_body, whats_inside

## Failing lines per record

Every record with at least one FAIL, with the names of its failing lines. The detail for each is in the section above.

### author-biography

- `Author_Biography_Brene_Brown_S304.md` (1): keyword in address slug
- `_scratch_peterson.md` *(name prefix suggests a working file, not a drafted record)* (5): total body words; section headings, verbatim and in order; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present

### book-note

- `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(name prefix suggests a working file, not a drafted record)* (11): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; machine-written tells; reading ease (Flesch, approximate); record field block present
- `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(name prefix suggests a working file, not a drafted record)* (15): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present
- `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(name prefix suggests a working file, not a drafted record)* (11): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present
- `a-guide-to-rational-living.md` (1): 'actually' at most once (Kain, S381)
- `a-path-through-the-jungle.md` (1): 'actually' at most once (Kain, S381)
- `a-way-of-being.md` (3): total body words; machine-written tells; 'actually' at most once (Kain, S381)
- `atomic-habits-clear.md` (1): 'actually' at most once (Kain, S381)
- `authentic-happiness-seligman.md` (1): 'actually' at most once (Kain, S381)
- `awakenings.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `before-happiness.md` (1): 'actually' at most once (Kain, S381)
- `best-self-be-you-only-better.md` (1): 'actually' at most once (Kain, S381)
- `boundaries-cloud.md` (1): 'actually' at most once (Kain, S381)
- `brainstorm-the-power-and-purpose-of-the-teenage-brain.md` (1): 'actually' at most once (Kain, S381)
- `chasing-the-scream.md` (1): 'actually' at most once (Kain, S381)
- `coaching-with-the-brain-in-mind.md` (1): 'actually' at most once (Kain, S381)
- `coming-to-our-senses.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `creating-minds.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `daring-to-trust.md` (1): 'actually' at most once (Kain, S381)
- `decisive.md` (1): 'actually' at most once (Kain, S381)
- `difficult-conversations-patton.md` (1): 'actually' at most once (Kain, S381)
- `embracing-uncertainty.md` (1): 'actually' at most once (Kain, S381)
- `emotional-leonard-mlodinow.md` (1): keyword density
- `feeling-good-burns.md` (1): 'actually' at most once (Kain, S381)
- `finding-flow.md` (1): 'actually' at most once (Kain, S381)
- `frames-of-mind.md` (1): 'actually' at most once (Kain, S381)
- `free-will-sam-harris.md` (1): keyword in address slug
- `further-along-the-road-less-travelled.md` (1): 'actually' at most once (Kain, S381)
- `games-people-play.md` (1): 'actually' at most once (Kain, S381)
- `getting-past-no.md` (1): 'actually' at most once (Kain, S381)
- `have-a-little-faith.md` (1): 'actually' at most once (Kain, S381)
- `homage-to-catalonia.md` (1): 'actually' at most once (Kain, S381)
- `how-the-mighty-fall.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `how-to-fix-a-broken-heart.md` (1): 'actually' at most once (Kain, S381)
- `how-to-know-a-person.md` (1): 'actually' at most once (Kain, S381)
- `humble-inquiry.md` (1): 'actually' at most once (Kain, S381)
- `identity-youth-and-crisis.md` (1): 'actually' at most once (Kain, S381)
- `journey-to-the-heart.md` (1): 'actually' at most once (Kain, S381)
- `keeping-the-love-you-find.md` (1): 'actually' at most once (Kain, S381)
- `leader-effectiveness-training.md` (1): 'actually' at most once (Kain, S381)
- `linchpin.md` (1): 'actually' at most once (Kain, S381)
- `mans-search-for-meaning.md` (1): 'actually' at most once (Kain, S381)
- `maps-of-meaning.md` (1): 'actually' at most once (Kain, S381)
- `mental-efficiency.md` (1): 'actually' at most once (Kain, S381)
- `money-master-the-game.md` (1): 'actually' at most once (Kain, S381)
- `multiple-intelligences-new-horizons.md` (1): 'actually' at most once (Kain, S381)
- `nature-emerson.md` (1): keyword in address slug
- `necessary-endings.md` (1): 'actually' at most once (Kain, S381)
- `noise.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `open-when.md` (1): 'actually' at most once (Kain, S381)
- `quit.md` (1): 'actually' at most once (Kain, S381)
- `radical-compassion.md` (1): 'actually' at most once (Kain, S381)
- `recovering-from-emotionally-immature-parents.md` (1): 'actually' at most once (Kain, S381)
- `resilient.md` (1): 'actually' at most once (Kain, S381)
- `shift.md` (1): 'actually' at most once (Kain, S381)
- `shyness-what-it-is-what-to-do-about-it.md` (1): 'actually' at most once (Kain, S381)
- `speak-peace-in-a-world-of-conflict.md` (1): 'actually' at most once (Kain, S381)
- `stillness-speaks.md` (1): 'actually' at most once (Kain, S381)
- `stoicism-and-the-art-of-happiness.md` (1): 'actually' at most once (Kain, S381)
- `surrounded-by-psychopaths.md` (1): 'actually' at most once (Kain, S381)
- `teacher-and-child.md` (1): 'actually' at most once (Kain, S381)
- `the-4-hour-body.md` (1): 'actually' at most once (Kain, S381)
- `the-8th-habit.md` (1): 'actually' at most once (Kain, S381)
- `the-advantage.md` (1): 'actually' at most once (Kain, S381)
- `the-advice-trap.md` (1): 'actually' at most once (Kain, S381)
- `the-beck-diet-solution.md` (1): 'actually' at most once (Kain, S381)
- `the-brains-way-of-healing.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `the-bridge-across-forever.md` (1): 'actually' at most once (Kain, S381)
- `the-confidence-gap.md` (1): 'actually' at most once (Kain, S381)
- `the-diet-trap-solution.md` (1): 'actually' at most once (Kain, S381)
- `the-doors-of-perception.md` (1): 'actually' at most once (Kain, S381)
- `the-farther-reaches-of-human-nature.md` (1): 'actually' at most once (Kain, S381)
- `the-feeling-good-handbook.md` (1): 'actually' at most once (Kain, S381)
- `the-gap-and-the-gain.md` (1): 'actually' at most once (Kain, S381)
- `the-happiness-project.md` (1): 'actually' at most once (Kain, S381)
- `the-high-5-habit.md` (1): 'actually' at most once (Kain, S381)
- `the-history-of-philosophy.md` (1): 'actually' at most once (Kain, S381)
- `the-honest-truth-about-dishonesty.md` (1): 'actually' at most once (Kain, S381)
- `the-jealousy-cure.md` (1): 'actually' at most once (Kain, S381)
- `the-life-cycle-completed.md` (1): 'actually' at most once (Kain, S381)
- `the-maine-woods.md` (1): 'actually' at most once (Kain, S381)
- `the-open-society-and-its-enemies.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `the-origins-of-intelligence-in-children.md` (1): 'actually' at most once (Kain, S381)
- `the-perennial-philosophy.md` (1): 'actually' at most once (Kain, S381)
- `the-places-that-scare-you.md` (1): 'actually' at most once (Kain, S381)
- `the-power-of-truth.md` (1): 'actually' at most once (Kain, S381)
- `the-psychology-of-self-esteem.md` (1): 'actually' at most once (Kain, S381)
- `the-relationship-cure.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `the-republic-plato.md` (1): 'actually' at most once (Kain, S381)
- `the-science-of-being-well.md` (1): 'actually' at most once (Kain, S381)
- `the-six-pillars-of-self-esteem.md` (1): 'actually' at most once (Kain, S381)
- `the-skilled-helper.md` (1): 'actually' at most once (Kain, S381)
- `the-stoic-challenge.md` (1): 'actually' at most once (Kain, S381)
- `the-time-paradox.md` (1): 'actually' at most once (Kain, S381)
- `the-ultimate-life-coaching-handbook.md` (1): 'actually' at most once (Kain, S381)
- `the-way-to-love.md` (1): 'actually' at most once (Kain, S381)
- `thrift.md` (1): 'actually' at most once (Kain, S381)
- `time-and-free-will.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `toward-a-psychology-of-being.md` (1): 'actually' at most once (Kain, S381)
- `truth-and-repair.md` (1): 'actually' at most once (Kain, S381)
- `tusculan-disputations.md` (1): 'actually' at most once (Kain, S381)
- `utilitarianism.md` (1): 'actually' at most once (Kain, S381)
- `what-do-you-say-after-you-say-hello.md` (1): 'actually' at most once (Kain, S381)
- `what-life-could-mean-to-you.md` (1): 'actually' at most once (Kain, S381)
- `why-zebras-dont-get-ulcers.md` (1): 'actually' at most once (Kain, S381)
- `words-that-work.md` (1): 'actually' at most once (Kain, S381)
- `yes-50-scientifically-proven-ways-to-be-persuasive.md` (1): keyword in first 50 chars of SEO title

### field-authority-article

- `EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S344.md` (3): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381); voice: no paragraph describing the article
- `REPORT__Exemplar_Gate_Fixed_And_Row_152_Trim_Confirmed_S344.md` *(name prefix suggests a working file, not a drafted record)* (6): total body words; headed sections, counted not named; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; voice: opens speaking to the reader
- `SUPERSEDED__how-psychological-thinking-has-transformed-over-the-years.md` *(name prefix suggests a working file, not a drafted record)* (6): paragraphs of 3 to 4 sentences, or 50+ words; every tag is one of the 36 locked slugs; outcome or problem tags, 2 to 4; article_type is the register value; source_type is a value the ACF field offers; voice: opens speaking to the reader
- `_to_delete/EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md` (6): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381); description length; external link to the source present; no paragraph over 120 words; voice: no paragraph describing the article
- `_to_delete/SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic.md` *(name prefix suggests a working file, not a drafted record)* (6): total body words; paragraphs of 3 to 4 sentences, or 50+ words; no em or en dashes; 'actually' at most once (Kain, S381); keyword density; external link to the source present
- `a-guide-to-building-inner-resilience.md` (1): 'actually' at most once (Kain, S381)
- `balanced-lifestyle-seven-practical-steps-to-achieve-life-balance.md` (1): 'actually' at most once (Kain, S381)
- `helping-people-help-themselves.md` (2): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381)
- `learn-about-the-psychologist-dr-albert-ellis.md` (1): 'actually' at most once (Kain, S381)
- `learned-helplessness-experiment-the-psychology-of-helplessness.md` (1): 'actually' at most once (Kain, S381)
- `maslows-hierarchy-of-needs.md` (1): 'actually' at most once (Kain, S381)
- `psychology-history-timeline.md` (1): 'actually' at most once (Kain, S381)
- `the-impact-of-the-invisible-gorilla-experiment-explained.md` (1): 'actually' at most once (Kain, S381)
- `the-importance-of-self-awareness.md` (1): keyword unique in register
- `what-is-counselling.md` (1): voice: first heading does not repeat the title What is counselling?

### help-answer

- `HELP__achologist-adept.md` (3): no paragraph over 60 words or 3 sentences; keyword in address slug; keyword in a subheading
- `HELP__achologist-led-tutorials-alts.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__achologist-title-without-membership.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-access-all-areas-pass.md` (3): keyword in address slug; keyword in a subheading; keyword density
- `HELP__achology-accessibility-requirements.md` (3): keyword in address slug; keyword in a subheading; keyword density
- `HELP__achology-automated-decision-making-profiling.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-career-change-coaching-mentoring.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-case-study-discussion-groups.md` (2): reading ease (Flesch, approximate); keyword in a subheading
- `HELP__achology-certificates-recognised-internationally.md` (6): reading ease (Flesch, approximate); keyword in first 50 chars of SEO title; keyword verbatim in first 10% of body; keyword in a subheading; keyword density; contractions: at least one in the body
- `HELP__achology-certificates-vs-university-degrees.md` (5): no paragraph over 60 words or 3 sentences; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading
- `HELP__achology-certification-practice-competence.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-change-mind-after-14-day-guarantee.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-character-development.md` (1): keyword in a subheading
- `HELP__achology-coaching-competency-review-sessions.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-code-character-conduct-ccac.md` (3): keyword in address slug; keyword in a subheading; keyword density
- `HELP__achology-code-ethics.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-community-rules-moderation.md` (3): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading
- `HELP__achology-content-offensive-emotionally-challenging.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-copyright-sharing-course-content.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-course-order-sequence.md` (1): keyword in a subheading
- `HELP__achology-course-outcomes.md` (3): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading
- `HELP__achology-course-piracy-copyright.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-course-prerequisites-requirements.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-course-required-attend-workshops.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-courses-cpd-hours.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-courses-other-languages.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-customer-legal-rights-uk-consumer-law.md` (1): keyword in a subheading
- `HELP__achology-disagreement-open-discussion.md` (4): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__achology-discounts-sales-promotions.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-discussion-boundary-feels-unsafe.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-discussion-spaces-groups-events.md` (4): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__achology-evidence-based-humanistic-psychology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-free-trial-introductory-offer.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__achology-invite-link-not-working.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__achology-knowledge-hub-free-read.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-knowledge-hub.md` (1): keyword in a subheading
- `HELP__achology-live-events-types.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-live-practice-session-etiquette.md` (2): reading ease (Flesch, approximate); keyword in a subheading
- `HELP__achology-media-press-interview-requests.md` (4): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__achology-members-host-workshops-events.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-membership-free-coaching-included.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-membership-refund.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-multiple-psychology-traditions.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-no-transformation-promises.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-on-udemy-should-i-join-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-password-reset-email-not-arriving.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__achology-payment-methods.md` (3): keyword in address slug; keyword in a subheading; keyword density
- `HELP__achology-peer-learning-community-teaches.md` (1): keyword in a subheading
- `HELP__achology-peer-learning-culture.md` (2): reading ease (Flesch, approximate); keyword in a subheading
- `HELP__achology-professional-indemnity-insurance.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-recommended-practice-pathway.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-refund-disagree-course-content.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-refund-policy-explained.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-refund-technical-issues.md` (3): keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__achology-responsible-community-member-advice.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-s-character-code-based-aristotle.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-s-five-community-principles.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-s-nine-value-based-principles.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-s-registered-company-details.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-s-ten-value-commitments.md` (3): 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); keyword in a subheading
- `HELP__achology-s-three-learning-paths.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-skill-development-workshops.md` (3): reading ease (Flesch, approximate); keyword in address slug; keyword density
- `HELP__achology-success-stories-do-courses-work.md` (3): keyword in address slug; keyword in a subheading; keyword density
- `HELP__achology-teaching-philosophy.md` (2): description length; keyword in address slug
- `HELP__achology-trust-legal-policies-work-together.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-uk-register-learning-providers.md` (3): keyword in address slug; keyword in a subheading; keyword density
- `HELP__achology-updates-course-already-purchased.md` (2): keyword in address slug; keyword in a subheading
- `HELP__achology-vs-icf-coaching-certification.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__achology-vs-linkedin-learning-comparison.md` (1): keyword in a subheading
- `HELP__achology-vs-school-of-life-comparison.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__achology-vs-tony-robbins-comparison.md` (1): keyword in a subheading
- `HELP__achology-vs-udemy-psychology-courses.md` (1): keyword in a subheading
- `HELP__any-achology-courses-appear-more-than.md` (2): keyword in address slug; keyword in a subheading
- `HELP__ask-questions-achology-community.md` (3): keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__become-a-life-coach.md` (1): no paragraph over 60 words or 3 sentences
- `HELP__become-a-master-achologist.md` (1): keyword in a subheading
- `HELP__become-an-achology-affiliate.md` (2): keyword in address slug; keyword in a subheading
- `HELP__become-instructor-contribute-content-achology.md` (3): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading
- `HELP__best-browsers-devices-achology-community.md` (2): keyword in address slug; keyword in a subheading
- `HELP__best-cbt-course-or-certification.md` (1): 'actually' at most once (Kain, S381)
- `HELP__build-real-competence-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__call-myself-certified-achology-credentials.md` (2): keyword in address slug; keyword in a subheading
- `HELP__call-myself-therapist-achology-courses.md` (2): keyword in address slug; keyword in a subheading
- `HELP__can-achology-suspend-terminate-access.md` (2): keyword in address slug; keyword in a subheading
- `HELP__cancel-achology-membership-anytime.md` (1): keyword in a subheading
- `HELP__cant-log-in-achology-community.md` (2): keyword in address slug; keyword in a subheading
- `HELP__cant-send-receive-messages-achology-community.md` (3): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading
- `HELP__cbt-practitioner-vs-cbt-therapist.md` (3): no paragraph over 60 words or 3 sentences; outcome or problem tags, 2 to 4; stage 0 demand evidence recorded
- `HELP__ccac-green-red-status-mean.md` (2): keyword in address slug; keyword in a subheading
- `HELP__character-traits-define-achologist.md` (3): reading ease (Flesch, approximate); keyword in a subheading; contractions: at least one in the body
- `HELP__choose-right-achology-event-level.md` (2): keyword in address slug; keyword in a subheading
- `HELP__cips-when-need-them.md` (2): keyword in address slug; keyword in a subheading
- `HELP__coaching-hot-seat.md` (4): 'actually' at most once (Kain, S381); keyword in a subheading; keyword density; contractions: at least one in the body
- `HELP__commit-practising-achologist.md` (2): keyword in address slug; keyword in a subheading
- `HELP__completed-achology-course-nothing-changed.md` (2): keyword in address slug; keyword in a subheading
- `HELP__course-completion-vs-competence.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__course-included-free-membership-happens-when.md` (2): keyword in address slug; keyword in a subheading
- `HELP__create-posts-achology-community.md` (2): keyword in address slug; keyword in a subheading
- `HELP__delete-achology-account-and-data.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__difference-between-certificate-completion-certificate-achievement.md` (1): keyword in address slug
- `HELP__difference-between-code-ethics-ccac-community.md` (2): keyword in address slug; keyword in a subheading
- `HELP__dimap-course-upgrade.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__do-achology-courses-get-updated.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__does-achology-offer-a-money-back-guarantee.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__does-achology-offer-partnerships-collaborations.md` (2): keyword in address slug; keyword in a subheading
- `HELP__does-achology-sell-personal-data.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__does-achology-supervise-peer-coaching.md` (1): keyword in a subheading
- `HELP__download-achology-community-app.md` (4): SEO title length; keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__download-achology-course-materials.md` (2): keyword in a subheading; contractions: at least one in the body
- `HELP__downloading-achology-content.md` (2): keyword in address slug; keyword in a subheading
- `HELP__earn-cpd-credit-hosting-session-only.md` (2): keyword in address slug; keyword in a subheading
- `HELP__evidence-cpd-learning-progression-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__explain-achology-qualifications-to-clients.md` (1): keyword in a subheading
- `HELP__find-achology-course-resources.md` (2): keyword in address slug; keyword in a subheading
- `HELP__find-achology-members-similar-interests.md` (3): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading
- `HELP__fix-achology-community-notification-problems.md` (2): keyword in address slug; keyword in a subheading
- `HELP__fix-audio-video-achology-live-sessions.md` (4): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__get-value-achology-mentorship-sessions.md` (2): keyword in address slug; keyword in a subheading
- `HELP__guest-speakers-policy.md` (2): keyword in address slug; keyword verbatim in first 10% of body
- `HELP__have-each-year-keep-master-achologist.md` (5): no paragraph over 60 words or 3 sentences; reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__have-retake-code-ethics-training-every.md` (2): keyword in address slug; keyword in a subheading
- `HELP__hidden-fees-additional-costs-achology.md` (3): keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__homework-assessment-achology-courses.md` (2): keyword in address slug; keyword in a subheading
- `HELP__host-own-achology-event.md` (2): keyword in address slug; keyword in a subheading
- `HELP__how-achology-courses-work-self-paced.md` (1): keyword in a subheading
- `HELP__how-long-achology-courses-take-timelines.md` (2): no paragraph over 60 words or 3 sentences; keyword in a subheading
- `HELP__how-long-achology-keeps-personal-data.md` (1): keyword in a subheading
- `HELP__how-long-achology-operating.md` (2): keyword in address slug; keyword in a subheading
- `HELP__how-long-achology-refund-process.md` (3): keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__how-much-does-achology-cost.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__how-psychology-became-institutionalised.md` (2): keyword in address slug; keyword in a subheading
- `HELP__how-to-contact-achology-support.md` (2): keyword in address slug; keyword in a subheading
- `HELP__how-to-join-live-achology-community-event.md` (3): keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__how-to-participate-achology-discussions-events.md` (2): keyword in address slug; keyword in a subheading
- `HELP__how-to-request-achology-refund.md` (2): keyword in address slug; keyword in a subheading
- `HELP__how-to-start-learning-cbt.md` (1): 'actually' at most once (Kain, S381)
- `HELP__inside-achology-course-modules-breakdown.md` (2): keyword in address slug; keyword in a subheading
- `HELP__insurance-coverage-achology-qualifications.md` (2): keyword in address slug; keyword in a subheading
- `HELP__is-a-cbt-certification-worth-it.md` (1): 'actually' at most once (Kain, S381)
- `HELP__is-achology-a-university.md` (2): keyword in address slug; keyword in a subheading
- `HELP__is-achology-accredited-somap.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__is-achology-content-scientific-or-ideological.md` (2): keyword in address slug; keyword in a subheading
- `HELP__is-achology-educational-provider-or-professional-body.md` (2): keyword in address slug; keyword in a subheading
- `HELP__is-achology-global-platform.md` (2): keyword in address slug; keyword in a subheading
- `HELP__is-achology-right-emotionally-vulnerable.md` (2): keyword in address slug; keyword in a subheading
- `HELP__is-achology-suitable-for-beginners.md` (1): keyword in a subheading
- `HELP__is-achology-therapy-counselling-or-coaching.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__is-achology-worth-the-money.md` (2): keyword in a subheading; keyword density
- `HELP__join-professional-body-after-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__kain-ramsay-udemy-vs-achology-courses.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__key-milestones-achology-s-history.md` (7): no paragraph over 60 words or 3 sentences; reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; keyword density; no paragraph over 120 words; contractions: at least one in the body
- `HELP__long-achology-valts-session.md` (3): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading
- `HELP__manage-achology-community-notifications.md` (5): 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__manipulative-pricing-tactics-achology-avoids.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__many-ccac-sessions-need-complete-often.md` (1): keyword in a subheading
- `HELP__many-courses-achology-offer-total.md` (2): keyword in address slug; keyword in a subheading
- `HELP__many-times-coach-same-person-cips.md` (2): keyword in address slug; keyword in a subheading
- `HELP__masterclasses-vs-practitioner-courses-differences.md` (1): keyword in a subheading
- `HELP__membership-first-or-course-first.md` (4): 'actually' at most once (Kain, S381); keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__membership-payment-fails-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__mentoring-opportunities-achology-membership.md` (5): no paragraph over 60 words or 3 sentences; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading
- `HELP__mentorship-sessions-recorded-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__navigate-achology-community-guide.md` (3): keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__nine-ccac-virtues.md` (4): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__offer-free-coaching-someone-outside-achology.md` (1): keyword in a subheading
- `HELP__overwhelmed-by-achology-options.md` (4): no paragraph over 60 words or 3 sentences; keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__pals-earn-them.md` (2): keyword in address slug; keyword density
- `HELP__personal-progress-checklist-count-official-cpd.md` (1): keyword in a subheading
- `HELP__personal-responsibility-achology-learning.md` (2): keyword in address slug; keyword in a subheading
- `HELP__platform-changes-course-access-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__post-nominal-letters-achology-certificates.md` (2): keyword in address slug; keyword in a subheading
- `HELP__principle-based-reflective-discussion.md` (1): keyword in a subheading
- `HELP__prior-qualifications-needed-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__progress-member-achologist.md` (2): keyword in address slug; keyword in a subheading
- `HELP__psychology-as-practical-wisdom.md` (2): keyword in address slug; keyword in a subheading
- `HELP__realistic-outcomes-with-achology.md` (2): 'actually' at most once (Kain, S381); keyword in a subheading
- `HELP__revisit-achology-courses-after-completion.md` (2): keyword in a subheading; contractions: at least one in the body
- `HELP__rsvp-join-achology-live-events.md` (2): keyword in address slug; keyword in a subheading
- `HELP__see-real-results-how-long-achology-takes.md` (2): keyword in address slug; keyword in a subheading
- `HELP__self-study-books-vs-achology-courses.md` (2): reading ease (Flesch, approximate); keyword in a subheading
- `HELP__senior-achologist-two-levels.md` (4): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__seven-marks-maturity-achology-teaches.md` (2): keyword in address slug; keyword density
- `HELP__share-achology-account-courses.md` (2): keyword in address slug; keyword in a subheading
- `HELP__share-my-achology-account-login.md` (2): keyword in address slug; keyword in a subheading
- `HELP__six-achology-cpd-statuses.md` (2): keyword in address slug; keyword in a subheading
- `HELP__slow-deep-learning-rejects-fast-certification.md` (2): keyword in address slug; keyword in a subheading
- `HELP__society-lost-gatekeeping-psychology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__standards-apply-trainee-achologists.md` (2): keyword in address slug; keyword in a subheading
- `HELP__study-multiple-achology-courses-simultaneously.md` (1): keyword in a subheading
- `HELP__submit-cpd-credit-claim-hosting-attending.md` (1): keyword in a subheading
- `HELP__supervision-after-achology-training.md` (1): keyword in a subheading
- `HELP__transfer-kain-ramsay-udemy-courses-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__upgrade-courses-bundle-access-pass.md` (3): keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__using-achology-content-branding-materials.md` (2): keyword in address slug; keyword in a subheading
- `HELP__valts-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__verify-achology-certificate.md` (2): keyword in address slug; keyword in a subheading
- `HELP__what-achology-certificate-proves.md` (2): keyword in address slug; keyword in a subheading
- `HELP__what-does-a-cbt-course-cover.md` (1): 'actually' at most once (Kain, S381)
- `HELP__what-does-achology-certification-qualify.md` (2): keyword in address slug; keyword in a subheading
- `HELP__what-does-achology-mean-becoming-wiser.md` (2): keyword in address slug; keyword in a subheading
- `HELP__what-does-achology-membership-include.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__what-does-an-nlp-course-cover.md` (2): no paragraph over 60 words or 3 sentences; voice: no paragraph describing the article
- `HELP__what-if-achology-courses-dont-work.md` (2): keyword in address slug; keyword in a subheading
- `HELP__what-is-achology.md` (6): no one-sentence paragraph (Kain, S361); reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; keyword density; contractions: at least one in the body
- `HELP__what-is-applied-psychology-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__what-is-circle-achology-community.md` (4): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__what-makes-a-good-nlp-course.md` (1): no paragraph over 60 words or 3 sentences
- `HELP__what-makes-achology-different.md` (1): keyword in a subheading
- `HELP__what-personal-data-achology-collects.md` (2): keyword in address slug; keyword in a subheading
- `HELP__what-to-include-achology-support-request.md` (2): keyword in address slug; keyword in a subheading
- `HELP__where-can-i-learn-about-carl-rogers.md` (9): no paragraph over 60 words or 3 sentences; reading ease (Flesch, approximate); outcome or problem tags, 2 to 4; description length; keyword in address slug; keyword in a subheading; keyword density; stage 0 demand evidence recorded; contractions: at least one in the body
- `HELP__where-can-i-learn-the-johari-window.md` (11): no paragraph over 60 words or 3 sentences; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); outcome or problem tags, 2 to 4; description length; keyword in address slug; keyword in a subheading; keyword density; no paragraph over 120 words; stage 0 demand evidence recorded; contractions: at least one in the body
- `HELP__where-is-achology-based.md` (3): keyword in first 120 chars of description; keyword in a subheading; keyword density
- `HELP__which-achology-company-am-actually-contracting.md` (2): keyword in a subheading; keyword density
- `HELP__which-achology-events-earn-accreditation-credit.md` (1): keyword in a subheading
- `HELP__who-is-achology-designed-for.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__who-is-achology-not-for.md` (2): keyword in address slug; keyword in a subheading
- `HELP__who-is-kain-ramsay.md` (3): keyword in first 120 chars of description; keyword in a subheading; keyword density
- `HELP__who-runs-achology.md` (2): keyword in address slug; keyword in a subheading
- `HELP__who-verifies-achology-cpd-claims.md` (1): keyword in a subheading
- `HELP__why-achology-avoids-diagnostic-labels.md` (1): keyword in a subheading
- `HELP__why-achology-criticizes-psychology-teaching.md` (3): keyword verbatim in first 10% of body; keyword in a subheading; keyword density
- `HELP__why-achology-includes-community-course-prices.md` (2): keyword in address slug; keyword in a subheading
- `HELP__why-pay-achology-when-free-content-exists.md` (4): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__will-clients-take-achology-certificate-seriously.md` (2): keyword in address slug; keyword in a subheading
- `HELP__will-employers-recognise-achology-certificate.md` (4): reading ease (Flesch, approximate); keyword in address slug; keyword in a subheading; contractions: at least one in the body
- `HELP__will-life-coaches-be-replaced-by-ai.md` (1): keyword density
- `RESEARCH__Course_Buying_Questions_Candidates_S356.md` (8): total body words; no one-sentence paragraph (Kain, S361); no paragraph over 60 words or 3 sentences; machine-written tells; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present; contractions: at least one in the body

### hub-question-article

- `EXEMPLAR__can-i-practise-cbt-on-my-own__APPROVED_S374.md` (5): paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; voice: no paragraph describing the article; voice: opens speaking to the reader

### instructor-article

- `I14__meaningful-life-versus-busy-life.md` (1): 'actually' at most once (Kain, S381)
- `I18__persuade-someone-who-disagrees.md` (1): 'actually' at most once (Kain, S381)
- `K10__growth-mindset-at-work.md` (1): 'actually' at most once (Kain, S381)
- `KAREN_SOURCE_LESSONS_S344.md` (8): total body words; paragraphs of 3 to 4 sentences, or 50+ words; banned brand words; machine-written tells; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present; voice: opens speaking to the reader
- `all-progression-is-impossible-without-change.md` (1): machine-written tells
- `assumptions-damage-relationships.md` (1): 'actually' at most once (Kain, S381)
- `balance-the-main-areas-of-life.md` (1): machine-written tells
- `can-you-be-too-self-aware.md` (1): machine-written tells
- `can-you-choose-to-be-more-introverted-or-extroverted.md` (1): machine-written tells
- `change-is-the-only-constant.md` (1): machine-written tells
- `confuse-opinions-with-facts.md` (1): machine-written tells
- `connected-to-your-future-self.md` (1): machine-written tells
- `cover-up-incompetence-with-head-knowledge.md` (1): machine-written tells
- `disagreement-vs-division.md` (1): machine-written tells
- `doctors-have-only-minutes-to-diagnose.md` (1): 'actually' at most once (Kain, S381)
- `does-a-diagnosis-do-to-the-person.md` (1): paragraphs of 3 to 4 sentences, or 50+ words
- `every-decision-is-a-trade-off.md` (1): machine-written tells
- `everyone-experiences-reality-differently.md` (1): machine-written tells
- `feeling-stuck-in-life.md` (3): machine-written tells; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate)
- `fixed-or-growth-mindset.md` (1): machine-written tells
- `forget-your-mistakes-but-remember-their-lessons.md` (1): machine-written tells
- `fountain-or-a-drain.md` (1): machine-written tells
- `freedom-vs-security.md` (1): machine-written tells
- `growing-or-standing-still.md` (1): 'actually' at most once (Kain, S381)
- `happiness-is-a-delusion-fulfilment-is-not.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `labels-vs-true-identity.md` (1): 'actually' at most once (Kain, S381)
- `living-according-to-your-values.md` (1): machine-written tells
- `pattern-recognition-superpower.md` (1): machine-written tells
- `personal-growth-requires-discomfort.md` (1): 'actually' at most once (Kain, S381)
- `positive-vs-negative-motivation.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `rational-or-emotional-thinker.md` (1): machine-written tells
- `remembered-for.md` (1): machine-written tells
- `saying-less-more-influential.md` (1): machine-written tells
- `self-acceptance-vs-self-improvement.md` (1): machine-written tells
- `stages-of-building-strong-relationships.md` (1): 'actually' at most once (Kain, S381)
- `stages-of-human-development-and-maturity.md` (1): 'actually' at most once (Kain, S381)
- `step-outside-your-comfort-zone.md` (1): 'actually' at most once (Kain, S381)
- `taking-responsibility-creates-personal-growth.md` (1): machine-written tells
- `think-objectively.md` (1): machine-written tells
- `thoughts-and-emotions-connection.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `time-perspective.md` (1): 'actually' at most once (Kain, S381)
- `turn-a-vision-into-a-goal.md` (1): 'actually' at most once (Kain, S381)
- `types-of-listening.md` (1): machine-written tells
- `whats-the-key-to-winning-hearts-and-minds.md` (1): machine-written tells
- `your-relationship-with-money-tells-a-story.md` (1): machine-written tells

### quote-page

- `Batch_Report__Course_018_Quotes_Batch_1_of_33_S354.md` *(name prefix suggests a working file, not a drafted record)* (11): section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(name prefix suggests a working file, not a drafted record)* (18): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(name prefix suggests a working file, not a drafted record)* (18): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(name prefix suggests a working file, not a drafted record)* (17): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Proving_Batch_S357.md` *(name prefix suggests a working file, not a drafted record)* (16): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Five_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Two_S357.md` *(name prefix suggests a working file, not a drafted record)* (16): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(name prefix suggests a working file, not a drafted record)* (17): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; no em or en dashes; machine-written tells; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(name prefix suggests a working file, not a drafted record)* (20): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; machine-written tells; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(name prefix suggests a working file, not a drafted record)* (17): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; machine-written tells; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(name prefix suggests a working file, not a drafted record)* (18): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(name prefix suggests a working file, not a drafted record)* (22): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Four_S356.md` *(name prefix suggests a working file, not a drafted record)* (17): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; machine-written tells; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Three_S356.md` *(name prefix suggests a working file, not a drafted record)* (17): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; machine-written tells; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(name prefix suggests a working file, not a drafted record)* (20): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; machine-written tells; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_S356.md` *(name prefix suggests a working file, not a drafted record)* (17): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Thirteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Thirteen.md` *(name prefix suggests a working file, not a drafted record)* (17): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Thirty_Six_Course_018_Quotes_Flesch_Remediated_And_Gate_Verified_Batch_Eight.md` *(name prefix suggests a working file, not a drafted record)* (13): section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Eleven.md` *(name prefix suggests a working file, not a drafted record)* (17): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Twelve_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Twelve.md` *(name prefix suggests a working file, not a drafted record)* (17): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Twenty_Five_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Nine.md` *(name prefix suggests a working file, not a drafted record)* (16): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Twenty_Four_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Ten.md` *(name prefix suggests a working file, not a drafted record)* (15): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(name prefix suggests a working file, not a drafted record)* (18): total body words; section headings, verbatim and in order; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; unexpected section; paragraphs of 3 to 4 sentences, or 50+ words; banned brand words; machine-written tells; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present; the body ends on the reflection question; a 'Put this into practice' block (Kain, S356); voice: the quoted person is not narrated
- `CQ001-002-1__why-you-dont-know-it-all-yet.md` (2): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381)
- `CQ001-002-2__why-every-effect-in-your-life-has-a-cause.md` (3): paragraphs of 3 to 4 sentences, or 50+ words; machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-005-1__why-what-you-think-is-true-might-not-be.md` (2): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381)
- `CQ001-006-1__why-simple-ideas-are-always-harder-to-explain.md` (2): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381)
- `CQ001-006-2__why-being-a-contributor-beats-being-a-consumer.md` (3): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381); voice: no paragraph describing the article
- `CQ001-007-1__why-being-reflective-beats-being-a-great-thinker.md` (4): paragraphs of 3 to 4 sentences, or 50+ words; machine-written tells; 'actually' at most once (Kain, S381); voice: the quoted person is not narrated
- `CQ001-008-1__why-simple-ideas-alone-drive-real-behavior-change.md` (2): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381)
- `CQ001-009-1__why-your-perspective-shapes-the-questions-you-ask.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-009-2__why-the-way-you-see-things-differs-from-reality.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-011-3__what-it-actually-means-to-live-a-virtuous-life.md` (2): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381)
- `CQ001-012-1__why-you-have-beliefs-even-without-knowing-it.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-013-1__how-a-persistent-thought-can-become-your-reality.md` (1): paragraphs of 3 to 4 sentences, or 50+ words
- `CQ001-015-1__why-we-talk-ourselves-out-of-what-we-want.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-016-1__why-not-every-idea-is-true.md` (2): machine-written tells; voice: the quoted person is not narrated
- `CQ001-017-1__why-we-feel-uncomfortable-in-our-own-skin.md` (2): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381)
- `CQ001-018-1__why-the-philosophy-you-live-by-actually-matters.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-019-1__why-we-can-only-find-meaning-in-our-past.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-021-1__why-your-brain-can-only-focus-on-one-thing.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-025-1__why-we-keep-following-rules-we-never-question.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-026-1__why-we-become-like-the-people-we-try-to-avoid.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-027-1__why-family-is-your-first-culture.md` (1): machine-written tells
- `CQ001-030-1__why-we-only-remember-what-matters-to-us.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-031-1__why-you-overreact-to-things-that-seem-small.md` (1): machine-written tells
- `CQ001-034-1__why-how-we-treat-others-is-always-a-choice.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-035-1__why-you-are-always-choosing-connection-or-not.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-036-1__why-you-cannot-grow-beyond-what-you-are-exposed-to.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-037-1__why-our-beliefs-are-just-glorified-ideas-we-hold.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-039-1__why-your-core-values-shape-every-decision-you-make.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-040-1__why-you-do-not-need-to-be-miles-ahead.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-042-1__why-looking-back-should-never-mean-living-there.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-043-1__why-people-only-change-when-they-want-to.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-044-1__why-being-more-self-aware-shapes-your-influence.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-047-1__why-we-stop-trying-to-break-free-from-limits.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-048-1__why-the-relationships-you-keep-shape-your-life.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-049-1__why-self-awareness-comes-before-personal-growth.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-050-1__why-you-can-only-teach-what-you-have-lived.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-051-1__why-personal-growth-is-a-choice-not-an-accident.md` (2): 'actually' at most once (Kain, S381); voice: the quoted person is not narrated
- `CQ001-052-1__why-reflective-conversation-cannot-be-rushed.md` (2): 'actually' at most once (Kain, S381); voice: the quoted person is not narrated
- `CQ001-053-1__why-your-public-self-hides-your-private-one.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-054-1__why-growth-in-life-depends-on-your-awareness.md` (3): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381); voice: the quoted person is not narrated
- `CQ001-055-1__why-self-awareness-should-be-your-top-priority.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-056-1__why-faith-is-an-outlook-on-life.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-058-1__why-holding-onto-the-past-holds-you-back.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-059-1__why-frustration-lands-on-the-wrong-target.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-060-1__why-we-channel-conflict-into-something-productive.md` (2): machine-written tells; voice: the quoted person is not narrated
- `CQ001-061-1__why-we-transfer-old-feelings-onto-new-people.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-062-1__why-that-weight-isnt-yours-to-carry.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-063-1__why-we-fight-to-be-understood-instead-of-listening.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-064-1__why-only-you-decide-how-deep-to-grow.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-065-1__why-being-yourself-is-the-biggest-risk.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-066-1__why-you-feel-out-of-sync-with-yourself.md` (1): machine-written tells
- `CQ001-070-1__why-reflection-is-the-real-engine-of-growth.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-074-1__why-you-react-to-traits-and-not-people.md` (1): machine-written tells
- `CQ001-079-1__why-feeling-broken-does-not-mean-you-are-broken.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-082-1__why-identity-and-personality-are-not-the-same.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-082-2__why-you-need-a-vision-for-who-you-become.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-085-1__why-we-all-miscommunicate-even-when-we-care.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-086-1__why-getting-people-is-easier-than-keeping-them.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-088-1__why-you-can-choose-how-long-you-carry-it.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-090-1__why-your-beliefs-put-a-cap-on-your-potential.md` (2): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381)
- `CQ001-090-2__how-to-understand-behavior-without-endorsing-it.md` (3): paragraphs of 3 to 4 sentences, or 50+ words; machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-091-1__why-you-should-build-your-life-on-principles.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-094-1__why-unsolicited-advice-feels-patronizing.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-098-1__why-your-response-determines-your-inner-experience.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-101-1__why-forgiving-someone-is-about-freeing-you-too.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-104-1__why-innovators-get-more-respect-than-imitators-do.md` (1): machine-written tells
- `CQ001-108-1__why-you-are-always-for-or-against-yourself.md` (1): machine-written tells
- `CQ001-109-1__why-the-truth-confronts-who-we-really-are.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-110-1__why-it-is-possible-to-see-yourself-objectively.md` (1): voice: the quoted person is not narrated
- `CQ001-115-1__why-a-theory-is-not-the-same-as-truth.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-117-1__why-real-growth-happens-outside-your-comfort-zone.md` (1): machine-written tells
- `CQ001-118-1__why-a-value-drives-every-choice-we-make.md` (1): machine-written tells
- `CQ001-119-1__why-simple-ideas-matter-more-than-complex-ones.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-122-1__why-excitement-is-not-the-same-as-motivation.md` (1): machine-written tells
- `CQ001-123-1__why-inner-conflict-means-you-do-not-know-yourself.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-124-1__why-we-so-often-confuse-confidence-with-arrogance.md` (1): machine-written tells
- `CQ001-127-1__why-defending-our-beliefs-too-rigidly-isolates-us.md` (1): machine-written tells
- `CQ001-128-1__why-empathy-holds-relationships-together.md` (1): machine-written tells
- `CQ001-129-1__why-no-one-wakes-up-wanting-to-hurt-you.md` (1): machine-written tells
- `CQ001-135-1__why-accepting-disorder-costs-you-peace.md` (1): machine-written tells
- `CQ001-137-1__why-being-humble-makes-a-person-more-attractive.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-138-1__why-your-fear-is-always-about-the-future.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-141-1__why-good-depends-on-values.md` (1): machine-written tells
- `CQ001-145-1__why-connection-determines-your-peace.md` (1): machine-written tells
- `CQ001-148-1__why-you-can-manage-prejudice.md` (1): voice: the quoted person is not narrated
- `CQ001-150-1__why-normal-is-different-for-everyone.md` (2): machine-written tells; voice: the quoted person is not narrated
- `CQ001-154-1__why-trying-to-prove-yourself-wrong-helps-you-grow.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-155-1__why-we-judge-others.md` (1): machine-written tells
- `CQ001-157-1__why-judging-others-is-really-a-defense-mechanism.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-160-1__why-we-feel-threatened-by-others.md` (1): machine-written tells
- `CQ001-169-1__why-some-people-overcome-hardship.md` (1): machine-written tells
- `CQ001-170-1__why-your-family-shaped-whether-you-feel-at-peace.md` (3): machine-written tells; 'actually' at most once (Kain, S381); voice: the quoted person is not narrated
- `CQ001-171-1__why-you-dont-need-anything-from-society.md` (1): voice: the quoted person is not narrated
- `CQ001-172-1__why-realising-you-have-a-choice-changes-everything.md` (1): 'actually' at most once (Kain, S381)
- `CQ001-173-1__why-you-should-not-keep-your-growth-to-yourself.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ001-175-1__why-people-are-only-honest-once-they-trust-you.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-001-1__why-we-take-courses-to-be-challenged-not-soothed.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-002-2__why-wanting-what-you-lack-can-lead-to-sadness.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-002-3__why-maturity-means-severing-our-dependency-on-other-people.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-005-1__why-thinking-like-a-winner-is-where-it-starts.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-017-2__why-most-of-your-thoughts-are-not-true.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-022-1__why-applying-what-you-learn-is-what-learning-means.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ018-050-1__why-personal-growth-is-rarely-a-joyous-process.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-053-1__why-your-character-shows-most-when-no-one-watches.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-054-1__why-what-simmers-beneath-the-surface-undermines-us.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-059-1__why-managing-your-emotions-is-work-that-never-ends.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-060-1__why-your-life-runs-on-fumes-without-giving-back.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-061-1__why-staying-angry-at-others-costs-you-so-much.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-063-1__why-our-beliefs-are-just-guesses-or-ideas-at-best.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-063-2__why-so-few-of-us-actually-know-what-we-believe.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-064-1__why-we-assume-that-what-we-think-is-true.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-069-2__why-life-eventually-becomes-about-other-people.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-071-2__living-life-defined-by-labels-that-they-assign.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-074-1__why-its-easier-to-diagnose-people-than-to-understand-them.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ018-076-1__why-people-pleasing-is-false-friendliness.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-077-1__why-peace-must-be-the-umpire-of-every-decision.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-077-2__why-self-control-has-to-precede-our-own-growth.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-078-2__why-youre-not-determined-by-anyone-else.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-079-1__why-what-you-do-always-outweighs-what-you-say.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-081-1__why-belief-drives-your-wellbeing.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-082-1__why-you-are-your-own-harshest-critic.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-082-2__choosing-to-be-part-of-the-solution.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-083-1__why-not-every-thought-is-a-universal-truth.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-084-1__why-maturity-is-not-associated-with-age.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-086-2__why-you-cant-trust-a-scared-person.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-087-1__why-trust-is-the-foundation-of-every-relationship.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-087-2__how-learning-from-mistakes-makes-you-more-valuable.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-088-1__why-assumptions-are-the-killer-of-human-connectedness.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-088-2__what-happens-when-dialogue-becomes-disrespectful.md` (2): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381)
- `CQ018-090-1__what-is-the-real-mark-of-maturity.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-090-2__what-it-means-to-let-dead-things-stay-dead.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-091-2__why-we-compromise-our-integrity-to-keep-the-peace.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-093-1__why-being-right-is-not-the-point-at-all.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ018-094-1__why-needing-to-be-a-hero-hides-your-insecurity.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-095-1__what-one-shift-in-perspective-can-actually-change.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-095-2__why-you-are-more-than-your-past.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ018-096-1__why-we-become-the-relationships-that-we-keep.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-096-2__why-experience-gives-us-authority-in-life.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ018-097-2__why-no-teacher-can-make-you-learn.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ018-100-1__why-a-blamer-hides-loneliness-behind-a-tough-mask.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ018-101-1__why-no-mountain-gives-you-the-fulfillment-you-seek.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-103-1__why-telling-the-truth-is-what-leads-to-trust.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-104-1__why-real-peace-begins-once-you-accept-each-other.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-105-1__why-hardship-produces-growth-when-nothing-else-does.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-105-2__why-trust-plus-time-is-the-real-intimacy-formula.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-108-2__why-how-you-respond-matters-more-than-what-occurs.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-110-2__why-knowing-facts-is-not-the-same-as-understanding.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ018-111-1__why-youre-not-entitled-to-peoples-trust.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-116-1__why-how-you-use-today-must-always-be-purposeful.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-117-1__why-you-get-distressed-by-what-you-focus-on.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-118-1__why-freedom-is-always-simply-a-choice-you-make.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-119-1__why-real-understanding-ends-all-tension-in-a-bond.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-120-1__why-simplicity-is-key-to-a-highly-effective-life.md` (2): machine-written tells; 'actually' at most once (Kain, S381)
- `CQ018-124-1__why-practice-does-not-make-perfect.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-125-1__why-how-people-feel-is-always-their-real-problem.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-126-1__why-discipline-is-what-turns-a-plan-into-action.md` (1): 'actually' at most once (Kain, S381)
- `CQ018-128-1__the-relief-in-not-having-it-all-together.md` (1): 'actually' at most once (Kain, S381)
- `_to_delete/CQ001-044-1__why-knowing-yourself-shapes-how-you-influence-others.md` (4): 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); keyword in first 50 chars of SEO title; practice block within 40 to 60 words
- `_to_delete/CQ001-094-1__why-unsolicited-advice-always-comes-across-as-patronizing.md` (4): machine-written tells; 'actually' at most once (Kain, S381); keyword in first 50 chars of SEO title; practice block within 40 to 60 words
- `_to_delete/CQ001-101-1__why-owning-your-choices-makes-you-feel-empowered.md` (2): 'actually' at most once (Kain, S381); practice block within 40 to 60 words

### seven-beliefs-series

- `Batch_Report__Seven_Beliefs_Back_Links_S387.md` *(name prefix suggests a working file, not a drafted record)* (5): total body words; machine-written tells; 'actually' at most once (Kain, S381); record field block present; voice: opens speaking to the reader
- `Batch_Report__Seven_Beliefs_Parts_1_And_2_S387.md` *(name prefix suggests a working file, not a drafted record)* (5): headed sections, counted not named; machine-written tells; 'actually' at most once (Kain, S381); record field block present; voice: opens speaking to the reader
- `Batch_Report__Seven_Beliefs_Parts_3_To_9_S387.md` *(name prefix suggests a working file, not a drafted record)* (7): total body words; headed sections, counted not named; banned brand words; machine-written tells; 'actually' at most once (Kain, S381); reading ease (Flesch, approximate); record field block present
- `PART_01__the-seven-beliefs-achology-is-built-on.md` (4): reading ease (Flesch, approximate); outcome or problem tags, 2 to 4; no paragraph over 120 words; voice: opens speaking to the reader
- `PART_02__can-people-change.md` (2): machine-written tells; outcome or problem tags, 2 to 4
- `PART_03__know-thyself.md` (1): outcome or problem tags, 2 to 4
- `PART_04__thinking-errors.md` (1): outcome or problem tags, 2 to 4
- `PART_05__understanding-and-managing-emotions.md` (1): outcome or problem tags, 2 to 4
- `PART_06__emotional-responsibility.md` (1): outcome or problem tags, 2 to 4
- `PART_07__change-your-life-from-the-inside-out.md` (1): outcome or problem tags, 2 to 4
- `PART_08__sense-of-purpose.md` (1): outcome or problem tags, 2 to 4
- `PART_09__philosophy-of-life.md` (2): outcome or problem tags, 2 to 4; voice: opens speaking to the reader

### workbook

- `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` (11): paragraphs of 3 to 4 sentences, or 50+ words; 'actually' at most once (Kain, S381); required fields present (22); every tag is one of the 36 locked slugs; outcome or problem tags, 2 to 4; author is a key the people registry holds; keyword verbatim in first 10% of body; keyword in a subheading; keyword density; external link to the source present; landing page body present

## Course links flagged by the gate (not a failure)

The gate prints `course links, flagged not gated N named and unlinked` and does not fail on it. It means a course is named in the body without a link. Counts from runs 2 and 3:

| Content type | Records with the line | Records with 1 or more named-and-unlinked | Named-and-unlinked phrases in all |
|---|---|---|---|
| book-note | 153 | 1 | 1 |
| field-authority-article | 121 | 1 | 1 |
| help-answer | 341 | 2 | 14 |
| hub-question-article | 58 | 1 | 1 |
| instructor-article | 139 | 2 | 3 |
| seven-beliefs-series | 12 | 2 | 8 |
| **All** | **824** | **9** | **28** |

The course-link line is absent from the printout on 539 records: all 457 `quote-page`, all 52 `author-biography`, all 29 `hub-guide` and the 1 `workbook` record. Whether the gate skips the check for those types by design, or for another reason: **cannot tell from this run**.

## Files not run

**folder guide, directly under Content Records, not in a type folder (1)**

- `000__WHAT_IS_IN_HERE.md`

**not a Markdown file (30)**

- `book-note/.tmp_originals_copy.md.bak`
- `book-note/CORRECTION__65_Book_Notes_Stage_0_Results_S341.csv`
- `book-note/_new_body.txt`
- `book-note/_new_body2.txt`
- `book-note/_to_delete/the-doors-of-perception.md.b64`
- `book-note/_to_delete/tusculan-disputations.md.b64`
- `book-note/_to_delete/tusculan2.b64`
- `field-authority-article/ARTICLE_HERO_IMAGE_MAP_S340.csv`
- `field-authority-article/_s341_fix.py`
- `field-authority-article/_s341_fix2.py`
- `field-authority-article/body_before.txt`
- `help-answer/MEASURED__All_250_Help_Answers_S117.csv`
- `help-answer/_batch6_slugs.txt`
- `quote-page/CQ001-027-1.b64`
- `quote-page/CQ001-027-1_v2.b64`
- `quote-page/_batch4_data.json`
- `quote-page/_batch4_transform.py`
- `quote-page/_batch5_data.json`
- `quote-page/_batch5_transform.py`
- `quote-page/_stale_Q06995__rules-we-make-up.md.bak`
- `quote-page/_stale_Q07023__sensible-goals-wise-decisions.md.bak`
- `quote-page/_stale_Q07024__communication-is-the-dna.md.bak`
- `quote-page/_stale_Q07025__doubting-character-and-ability.md.bak`
- `quote-page/_stale_Q07027__not-responsible-for-answers.md.bak`
- `quote-page/_stale_Q07028__more-than-techniques.md.bak`
- `quote-page/_stale_Q07030__encouraging-people-to-live-well.md.bak`
- `quote-page/_stale_Q07031__decisions-that-align.md.bak`
- `quote-page/_stale_Q07032__self-awareness-like-oxygen.md.bak`
- `seven-beliefs-series/_cowork_shared_bar_S387.py`
- `seven-beliefs-series/check_no_repeats.py`

**folder name is not a content type in content_gate_standards.json: cannot tell which type applies (1)**

- `hub-guide-retired/self-awareness__superseded_by_grow-self-awareness.md`

The one `.md` file in a folder with no gate type is `hub-guide-retired/self-awareness__superseded_by_grow-self-awareness.md`. Which type it should be gated as: **cannot tell**. `000__WHAT_IS_IN_HERE.md` sits directly under Content Records and is the folder's own guide, not a record.
