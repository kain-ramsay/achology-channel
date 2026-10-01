# Job 7: failure triage of the content gate report

Read-only. Built only from `cloud-reports/job6-content-gate.md` on branch `cloud-report/job6-content-gate` of `kain-ramsay/achology-record` (commit `8041f4c`). The gate was not re-run, the gate's code and standards were not opened, no record was opened, and no replacement words are written. The only changes are this new file on a new branch.

## How the groups were decided

The report holds, for each failing line, a label (the gate's own wording), a detail text per record, and a flag where the file's name starts with a working-file prefix (`REPORT__`, `Batch_Report`, `SKIPPED__`, `SUPERSEDED__`, `HELD__`, `MEASURED__`, `_`, `000__`). Groups are judged from those three things only.

- **A. A script could fix it with no change of meaning.** The right value is stated in the report line itself and nothing is being rewritten. Four line types qualify: `keyword in address slug`, `article_type is the register value`, `source_type is a value the ACF field offers`, `no em or en dashes`. Caveats are in the table.
- **B. Needs a person to rewrite words, or to choose.** Length, rhythm, reading ease, keyword placement, banned or tell-tale words, headings, missing links, missing words, tag choices.
- **C. Looks like a gate or standard problem, not a record problem.** Two tests, both stated so they can be argued with: (1) the failing file is one the report marks as a working file by its name prefix, so the gate is being asked about a document that is not a drafted record; or the line is `unexpected section`, which in the report fires only on such files; (2) the rule fails at least half of one content type that has 10 or more records (three cases: book-note `'actually'`, help-answer `keyword in a subheading`, seven-beliefs-series `outcome or problem tags`). A rule failing most of a type can mean the rule is newer than the records or that the rule is wrong; which one: **cannot tell from the report**.
- **U. Cannot tell from the report.** Used where the report does not show whether the fix is mechanical, a person's choice, or a rule problem.
- **Left open.** The one `keyword unique in register` failure (`field-authority-article/the-importance-of-self-awareness.md`) is not put in any group, and nothing is said about which article should give up the keyword `self-awareness`.

Group is assigned to each failing instance (one line on one record), not only to the line type, because a line type can mix groups. An instance on a working-file name is always C, whatever its line. The counts below are instances unless a column says records.

The working-file test is by name only. Files the report does not flag but whose detail text suggests a note rather than a record exist (for example `RESEARCH__Course_Buying_Questions_Candidates_S356.md` and `KAREN_SOURCE_LESSONS_S344.md`, each failing with `no '## Page fields' table found`); they are left in the group their line gives, and whether they are records: **cannot tell**.

## Every failing line type: records failed, and group

Records failed = number of records the line printed FAIL on (from the report). The group columns split those instances. Order: most records first.

| Line type | Records failed | A | B | C | U | Open | Why |
|---|---|---|---|---|---|---|---|
| 'actually' at most once (Kain, S381) | 286 | 0 | 176 | 110 | 0 | 0 | Words to cut or reword. In book-note it fails 100 of 153 records (65%), so that cell is C (the rule's own label dates it S381; whether the book notes pre-date it: cannot tell). 11 of the 286 are on working-file names (C). |
| keyword in a subheading | 213 | 0 | 1 | 212 | 0 | 0 | A heading has to be reworded. In help-answer it fails 212 of 341 records, so that cell is C: whether the help-answer standard or the records are out of step: cannot tell. |
| unexpected section | 206 | 0 | 0 | 206 | 0 | 0 | All 206 failures are on working-file names (186 quote-page, 20 book-note): headings in batch reports and notes that are not record sections. |
| keyword in address slug | 156 | 156 | 0 | 0 | 0 | 0 | A: the report names the slug, and a script can rewrite it. Caveats: whether the slug or the keyword should move, and whether any of these addresses is already live (changing a live address is a redirect decision), cannot be told from the report. It fails 153 of 341 help-answers (45%), just under the half-of-a-type test; that is worth a person checking whether the rule or the slug scheme is at fault. |
| machine-written tells | 110 | 0 | 99 | 11 | 0 | 0 | Words to reword (the detail names the word, for example plainly, truly). A script could delete or swap them, but that changes the wording, so it is B. 11 of the 110 are on working-file names (C). |
| reading ease (Flesch, approximate) | 64 | 0 | 37 | 27 | 0 | 0 | Rewrite to shorten sentences and words. 27 of the 64 are on working-file names (C). |
| paragraphs of 3 to 4 sentences, or 50+ words | 50 | 0 | 21 | 29 | 0 | 0 | Paragraph rhythm: needs rewriting. 29 of the 50 are on working-file names (C). |
| keyword density | 45 | 0 | 44 | 1 | 0 | 0 | Keyword count too low or too high: rewrite. |
| record field block present | 33 | 0 | 0 | 30 | 3 | 0 | Every failing file has no `## Page fields` table. 30 of the 33 are on working-file names (C). The other 3 are U (whether they are meant to be records: cannot tell): `help-answer/RESEARCH__Course_Buying_Questions_Candidates_S356.md`; `hub-question-article/EXEMPLAR__can-i-practise-cbt-on-my-own__APPROVED_S374.md`; `instructor-article/KAREN_SOURCE_LESSONS_S344.md`. |
| voice: the quoted person is not narrated | 33 | 0 | 11 | 22 | 0 | 0 | 22 are `the record carries no quote_author` on working-file names (C). The other 11 name a narrating phrase (for example 'Kain describes'): rewrite (B). |
| total body words | 31 | 0 | 3 | 28 | 0 | 0 | Too short or too long: words to add or cut. 28 of the 31 are on working-file names (C). |
| contractions: at least one in the body | 29 | 0 | 29 | 0 | 0 | 0 | Needs contractions put in: rewording. |
| section headings, verbatim and in order | 26 | 0 | 0 | 26 | 0 | 0 | Headings must be reworded or reordered. All 26 are on working-file names (C). |
| keyword verbatim in first 10% of body | 25 | 0 | 25 | 0 | 0 | 0 | Rewrite the opening. |
| a 'Put this into practice' block (Kain, S356) | 22 | 0 | 0 | 22 | 0 | 0 | The practice field is empty: words needed. All 22 are quote-page working-file names. |
| the body ends on the reflection question | 22 | 0 | 0 | 22 | 0 | 0 | Last sentence has to be rewritten as a question. All 22 are quote-page working-file names; 3 end with `*` and 1 with a backtick, which may be markup rather than words (cannot tell). |
| outcome or problem tags, 2 to 4 | 14 | 0 | 4 | 10 | 0 | 0 | A person has to choose tags (not a rewrite, but not mechanical). In seven-beliefs-series it fails 9 of 12 records, so that cell is C: cannot tell whether those records or the rule are at fault. |
| no paragraph over 60 words or 3 sentences | 14 | 0 | 14 | 0 | 0 | 0 | Split or cut paragraphs: rewrite. |
| voice: opens speaking to the reader | 8 | 0 | 4 | 4 | 0 | 0 | The opening must be rewritten. 4 of the 8 are on working-file names (C). Their detail text is a note header (for example `**From:** Claude Cowork`). |
| voice: no paragraph describing the article | 5 | 0 | 5 | 0 | 0 | 0 | Remove a paragraph that talks about the article: rewrite. |
| keyword in first 50 chars of SEO title | 4 | 0 | 4 | 0 | 0 | 0 | Title rewrite (the detail shows 51 to 53 characters, near misses). |
| description length | 4 | 0 | 4 | 0 | 0 | 0 | Shorten the description: rewrite (158 to 168 against a maximum of 155). |
| no paragraph over 120 words | 4 | 0 | 4 | 0 | 0 | 0 | Split or cut paragraphs. |
| external link to the source present | 3 | 0 | 2 | 1 | 0 | 0 | A person must supply the source link and the words around it. |
| headed sections, counted not named | 3 | 0 | 0 | 3 | 0 | 0 | Structure: sections to add or merge. |
| stage 0 demand evidence recorded | 3 | 0 | 3 | 0 | 0 | 0 | A person must record the demand evidence; the report gives no detail. |
| banned brand words | 3 | 0 | 1 | 2 | 0 | 0 | Replace a banned word (the detail shows `empowerment`). |
| practice block within 40 to 60 words | 3 | 0 | 3 | 0 | 0 | 0 | Practice block 21 to 30 words: words to add. |
| every tag is one of the 36 locked slugs | 2 | 0 | 1 | 1 | 0 | 0 | field-authority-article: on a working-file name (C); 3 tags outside the register, and whether record or register is wrong cannot be told. workbook (B): a placeholder, `To be confirmed at commission`, that a person must replace. |
| no em or en dashes | 2 | 0 | 0 | 2 | 0 | 0 | Mechanical in method: a script could replace the dashes. All 2 are on working-file names (C). Caveat: the replacement punctuation is an editorial choice, so whether it is 'no change of meaning': cannot tell. |
| keyword in first 120 chars of description | 2 | 0 | 2 | 0 | 0 | 0 | Description rewrite. |
| no one-sentence paragraph (Kain, S361) | 2 | 0 | 2 | 0 | 0 | 0 | Merge or reword paragraphs. |
| article_type is the register value | 1 | 0 | 0 | 1 | 0 | 0 | Mechanical in method (the field holds `field-authority-article`; the report states the standard is `field-authority`). All 1 are on working-file names (C). |
| keyword unique in register | 1 | 0 | 0 | 0 | 0 | 1 | Left open, as instructed. |
| source_type is a value the ACF field offers | 1 | 0 | 0 | 1 | 0 | 0 | Mechanical in method (the field holds `salvage`; the report states the only value offered is `legacy-page`). All 1 are on working-file names (C). A person should confirm `salvage` means the same: cannot tell. |
| voice: first heading does not repeat the title What is counselling? | 1 | 0 | 1 | 0 | 0 | 0 | Heading to reword. |
| SEO title length | 1 | 0 | 1 | 0 | 0 | 0 | Title rewrite (65 against a maximum of 60). |
| author is a key the people registry holds | 1 | 0 | 0 | 0 | 1 | 0 | workbook: the author field reads `Base voice, no pen name; assigned at commission per the workbook field group's own key`, so U: cannot tell whether the rule applies to workbooks yet. |
| landing page body present | 1 | 0 | 1 | 0 | 0 | 0 | Words needed: the record carries no `landing_page_body`. |
| required fields present (22) | 1 | 0 | 1 | 0 | 0 | 0 | workbook: 2 missing, `landing_page_body` and `whats_inside`, both need words. |
| **All 40 line types** | **1,435 instances** | **156** | **503** | **771** | **4** | **1** | |

## Counts per group per content type

Instances = failing lines. Records = records with at least one failing line in that group (a record can be in several groups). Open (1 instance, field-authority-article) is not counted in any group.

| Content type | Records run | Records failing | Instances A | B | C | U | Records with A | B | C | U |
|---|---|---|---|---|---|---|---|---|---|---|
| author-biography | 52 | 2 | 1 | 0 | 5 | 0 | 1 | 0 | 1 | 0 |
| book-note | 153 | 106 | 2 | 13 | 136 | 0 | 2 | 12 | 102 | 0 |
| field-authority-article | 121 | 15 | 0 | 19 | 18 | 0 | 0 | 11 | 3 | 0 |
| help-answer | 341 | 228 | 153 | 174 | 212 | 1 | 153 | 91 | 212 | 1 |
| hub-guide | 29 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| hub-question-article | 58 | 1 | 0 | 4 | 0 | 1 | 0 | 1 | 0 | 1 |
| instructor-article | 139 | 45 | 0 | 56 | 0 | 1 | 0 | 45 | 0 | 1 |
| quote-page | 457 | 182 | 0 | 222 | 374 | 0 | 0 | 160 | 22 | 0 |
| seven-beliefs-series | 12 | 12 | 0 | 5 | 26 | 0 | 0 | 3 | 12 | 0 |
| workbook | 1 | 1 | 0 | 10 | 0 | 1 | 0 | 1 | 0 | 1 |
| **All** | 1363 | 592 | 156 | 503 | 771 | 4 | 156 | 324 | 352 | 4 |

### Which line types sit in each group, per content type

**author-biography**
- A: keyword in address slug 1
- C: paragraphs of 3 to 4 sentences, or 50+ words 1; reading ease (Flesch, approximate) 1; record field block present 1; section headings, verbatim and in order 1; total body words 1

**book-note**
- A: keyword in address slug 2
- B: machine-written tells 10; total body words 1; keyword density 1; keyword in first 50 chars of SEO title 1
- C: 'actually' at most once (Kain, S381) 100; unexpected section 20; total body words 3; paragraphs of 3 to 4 sentences, or 50+ words 3; reading ease (Flesch, approximate) 3; record field block present 3; section headings, verbatim and in order 3; machine-written tells 1

**field-authority-article**
- B: 'actually' at most once (Kain, S381) 10; paragraphs of 3 to 4 sentences, or 50+ words 3; voice: no paragraph describing the article 2; external link to the source present 1; description length 1; no paragraph over 120 words 1; voice: first heading does not repeat the title What is counselling? 1
- C: paragraphs of 3 to 4 sentences, or 50+ words 3; total body words 2; voice: opens speaking to the reader 2; 'actually' at most once (Kain, S381) 1; external link to the source present 1; article_type is the register value 1; every tag is one of the 36 locked slugs 1; headed sections, counted not named 1; keyword density 1; no em or en dashes 1; outcome or problem tags, 2 to 4 1; reading ease (Flesch, approximate) 1; record field block present 1; source_type is a value the ACF field offers 1
- Open: keyword unique in register 1

**help-answer**
- A: keyword in address slug 153
- B: keyword density 42; reading ease (Flesch, approximate) 32; contractions: at least one in the body 29; keyword verbatim in first 10% of body 24; no paragraph over 60 words or 3 sentences 14; 'actually' at most once (Kain, S381) 13; description length 3; outcome or problem tags, 2 to 4 3; stage 0 demand evidence recorded 3; keyword in first 120 chars of description 2; no one-sentence paragraph (Kain, S361) 2; no paragraph over 120 words 2; SEO title length 1; keyword in first 50 chars of SEO title 1; machine-written tells 1; total body words 1; voice: no paragraph describing the article 1
- C: keyword in a subheading 212
- U: record field block present 1

**hub-guide**: no failing lines.

**hub-question-article**
- B: paragraphs of 3 to 4 sentences, or 50+ words 1; reading ease (Flesch, approximate) 1; voice: no paragraph describing the article 1; voice: opens speaking to the reader 1
- U: record field block present 1

**instructor-article**
- B: machine-written tells 31; 'actually' at most once (Kain, S381) 18; paragraphs of 3 to 4 sentences, or 50+ words 2; reading ease (Flesch, approximate) 2; banned brand words 1; total body words 1; voice: opens speaking to the reader 1
- U: record field block present 1

**quote-page**
- B: 'actually' at most once (Kain, S381) 134; machine-written tells 56; paragraphs of 3 to 4 sentences, or 50+ words 14; voice: the quoted person is not narrated 11; practice block within 40 to 60 words 3; keyword in first 50 chars of SEO title 2; reading ease (Flesch, approximate) 1; voice: no paragraph describing the article 1
- C: unexpected section 186; paragraphs of 3 to 4 sentences, or 50+ words 22; voice: the quoted person is not narrated 22; a 'Put this into practice' block (Kain, S356) 22; record field block present 22; section headings, verbatim and in order 22; the body ends on the reflection question 22; reading ease (Flesch, approximate) 21; total body words 20; machine-written tells 7; 'actually' at most once (Kain, S381) 6; banned brand words 1; no em or en dashes 1

**seven-beliefs-series**
- B: voice: opens speaking to the reader 2; machine-written tells 1; reading ease (Flesch, approximate) 1; no paragraph over 120 words 1
- C: outcome or problem tags, 2 to 4 9; machine-written tells 3; 'actually' at most once (Kain, S381) 3; record field block present 3; voice: opens speaking to the reader 2; headed sections, counted not named 2; total body words 2; reading ease (Flesch, approximate) 1; banned brand words 1

**workbook**
- B: 'actually' at most once (Kain, S381) 1; every tag is one of the 36 locked slugs 1; external link to the source present 1; keyword density 1; keyword in a subheading 1; keyword verbatim in first 10% of body 1; landing page body present 1; outcome or problem tags, 2 to 4 1; paragraphs of 3 to 4 sentences, or 50+ words 1; required fields present (22) 1
- U: author is a key the people registry holds 1

## The ten worst records per content type, by number of failing lines

Ties are broken by file name. The split is that record's own failing lines by group (A, B, C, U). Two lists per type: first every file, then with the working-file names left out (so the second list is the one most likely to be actual records; the report's own flag is by name only). hub-guide has no failing lines. The `keyword unique in register` line is left open and not counted, so `the-importance-of-self-awareness.md` shows no failing lines.

### author-biography

**All files** (2 failing files in all; showing 2)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `_scratch_peterson.md` *(working-file name)* | 5 | 0 | 0 | 5 | 0 |
| 2 | `Author_Biography_Brene_Brown_S304.md` | 1 | 1 | 0 | 0 | 0 |

**Working-file names left out** (1 failing files in all; showing 1)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `Author_Biography_Brene_Brown_S304.md` | 1 | 1 | 0 | 0 | 0 |

### book-note

**All files** (106 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `REPORT__The_Forty_Six_Book_Notes_Turned_Out_To_Be_Twenty_Five_S349.md` *(working-file name)* | 15 | 0 | 0 | 15 | 0 |
| 2 | `REPORT__Second_Qualitative_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md` *(working-file name)* | 11 | 0 | 0 | 11 | 0 |
| 3 | `REPORT__The_Seventeen_Book_Notes_Keyword_And_Demand_Backfill_Sixteen_Blocked_On_Body_Gaps_S349.md` *(working-file name)* | 11 | 0 | 0 | 11 | 0 |
| 4 | `a-way-of-being.md` | 3 | 0 | 2 | 1 | 0 |
| 5 | `awakenings.md` | 2 | 0 | 1 | 1 | 0 |
| 6 | `coming-to-our-senses.md` | 2 | 0 | 1 | 1 | 0 |
| 7 | `creating-minds.md` | 2 | 0 | 1 | 1 | 0 |
| 8 | `how-the-mighty-fall.md` | 2 | 0 | 1 | 1 | 0 |
| 9 | `noise.md` | 2 | 0 | 1 | 1 | 0 |
| 10 | `the-brains-way-of-healing.md` | 2 | 0 | 1 | 1 | 0 |

**Working-file names left out** (103 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `a-way-of-being.md` | 3 | 0 | 2 | 1 | 0 |
| 2 | `awakenings.md` | 2 | 0 | 1 | 1 | 0 |
| 3 | `coming-to-our-senses.md` | 2 | 0 | 1 | 1 | 0 |
| 4 | `creating-minds.md` | 2 | 0 | 1 | 1 | 0 |
| 5 | `how-the-mighty-fall.md` | 2 | 0 | 1 | 1 | 0 |
| 6 | `noise.md` | 2 | 0 | 1 | 1 | 0 |
| 7 | `the-brains-way-of-healing.md` | 2 | 0 | 1 | 1 | 0 |
| 8 | `the-open-society-and-its-enemies.md` | 2 | 0 | 1 | 1 | 0 |
| 9 | `the-relationship-cure.md` | 2 | 0 | 1 | 1 | 0 |
| 10 | `time-and-free-will.md` | 2 | 0 | 1 | 1 | 0 |

### field-authority-article

**All files** (14 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `REPORT__Exemplar_Gate_Fixed_And_Row_152_Trim_Confirmed_S344.md` *(working-file name)* | 6 | 0 | 0 | 6 | 0 |
| 2 | `SUPERSEDED__how-psychological-thinking-has-transformed-over-the-years.md` *(working-file name)* | 6 | 0 | 0 | 6 | 0 |
| 3 | `_to_delete/EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md` | 6 | 0 | 6 | 0 | 0 |
| 4 | `_to_delete/SKIPPED__unlock-personal-empowerment-with-the-empowerment-dynamic.md` *(working-file name)* | 6 | 0 | 0 | 6 | 0 |
| 5 | `EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S344.md` | 3 | 0 | 3 | 0 | 0 |
| 6 | `helping-people-help-themselves.md` | 2 | 0 | 2 | 0 | 0 |
| 7 | `a-guide-to-building-inner-resilience.md` | 1 | 0 | 1 | 0 | 0 |
| 8 | `balanced-lifestyle-seven-practical-steps-to-achieve-life-balance.md` | 1 | 0 | 1 | 0 | 0 |
| 9 | `learn-about-the-psychologist-dr-albert-ellis.md` | 1 | 0 | 1 | 0 | 0 |
| 10 | `learned-helplessness-experiment-the-psychology-of-helplessness.md` | 1 | 0 | 1 | 0 | 0 |

**Working-file names left out** (11 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `_to_delete/EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S319.md` | 6 | 0 | 6 | 0 | 0 |
| 2 | `EXEMPLAR__the-seven-levels-of-human-awareness__FROZEN_S344.md` | 3 | 0 | 3 | 0 | 0 |
| 3 | `helping-people-help-themselves.md` | 2 | 0 | 2 | 0 | 0 |
| 4 | `a-guide-to-building-inner-resilience.md` | 1 | 0 | 1 | 0 | 0 |
| 5 | `balanced-lifestyle-seven-practical-steps-to-achieve-life-balance.md` | 1 | 0 | 1 | 0 | 0 |
| 6 | `learn-about-the-psychologist-dr-albert-ellis.md` | 1 | 0 | 1 | 0 | 0 |
| 7 | `learned-helplessness-experiment-the-psychology-of-helplessness.md` | 1 | 0 | 1 | 0 | 0 |
| 8 | `maslows-hierarchy-of-needs.md` | 1 | 0 | 1 | 0 | 0 |
| 9 | `psychology-history-timeline.md` | 1 | 0 | 1 | 0 | 0 |
| 10 | `the-impact-of-the-invisible-gorilla-experiment-explained.md` | 1 | 0 | 1 | 0 | 0 |

### help-answer

**All files** (228 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `HELP__where-can-i-learn-the-johari-window.md` | 11 | 1 | 9 | 1 | 0 |
| 2 | `HELP__where-can-i-learn-about-carl-rogers.md` | 9 | 1 | 7 | 1 | 0 |
| 3 | `RESEARCH__Course_Buying_Questions_Candidates_S356.md` | 8 | 0 | 7 | 0 | 1 |
| 4 | `HELP__key-milestones-achology-s-history.md` | 7 | 1 | 5 | 1 | 0 |
| 5 | `HELP__achology-certificates-recognised-internationally.md` | 6 | 0 | 5 | 1 | 0 |
| 6 | `HELP__what-is-achology.md` | 6 | 1 | 4 | 1 | 0 |
| 7 | `HELP__achology-certificates-vs-university-degrees.md` | 5 | 1 | 3 | 1 | 0 |
| 8 | `HELP__have-each-year-keep-master-achologist.md` | 5 | 1 | 3 | 1 | 0 |
| 9 | `HELP__manage-achology-community-notifications.md` | 5 | 1 | 3 | 1 | 0 |
| 10 | `HELP__mentoring-opportunities-achology-membership.md` | 5 | 1 | 3 | 1 | 0 |

**Working-file names left out** (228 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `HELP__where-can-i-learn-the-johari-window.md` | 11 | 1 | 9 | 1 | 0 |
| 2 | `HELP__where-can-i-learn-about-carl-rogers.md` | 9 | 1 | 7 | 1 | 0 |
| 3 | `RESEARCH__Course_Buying_Questions_Candidates_S356.md` | 8 | 0 | 7 | 0 | 1 |
| 4 | `HELP__key-milestones-achology-s-history.md` | 7 | 1 | 5 | 1 | 0 |
| 5 | `HELP__achology-certificates-recognised-internationally.md` | 6 | 0 | 5 | 1 | 0 |
| 6 | `HELP__what-is-achology.md` | 6 | 1 | 4 | 1 | 0 |
| 7 | `HELP__achology-certificates-vs-university-degrees.md` | 5 | 1 | 3 | 1 | 0 |
| 8 | `HELP__have-each-year-keep-master-achologist.md` | 5 | 1 | 3 | 1 | 0 |
| 9 | `HELP__manage-achology-community-notifications.md` | 5 | 1 | 3 | 1 | 0 |
| 10 | `HELP__mentoring-opportunities-achology-membership.md` | 5 | 1 | 3 | 1 | 0 |

### hub-guide

No failing lines.

### hub-question-article

**All files** (1 failing files in all; showing 1)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `EXEMPLAR__can-i-practise-cbt-on-my-own__APPROVED_S374.md` | 5 | 0 | 4 | 0 | 1 |

**Working-file names left out** (1 failing files in all; showing 1)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `EXEMPLAR__can-i-practise-cbt-on-my-own__APPROVED_S374.md` | 5 | 0 | 4 | 0 | 1 |

### instructor-article

**All files** (45 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `KAREN_SOURCE_LESSONS_S344.md` | 8 | 0 | 7 | 0 | 1 |
| 2 | `feeling-stuck-in-life.md` | 3 | 0 | 3 | 0 | 0 |
| 3 | `happiness-is-a-delusion-fulfilment-is-not.md` | 2 | 0 | 2 | 0 | 0 |
| 4 | `positive-vs-negative-motivation.md` | 2 | 0 | 2 | 0 | 0 |
| 5 | `thoughts-and-emotions-connection.md` | 2 | 0 | 2 | 0 | 0 |
| 6 | `I14__meaningful-life-versus-busy-life.md` | 1 | 0 | 1 | 0 | 0 |
| 7 | `I18__persuade-someone-who-disagrees.md` | 1 | 0 | 1 | 0 | 0 |
| 8 | `K10__growth-mindset-at-work.md` | 1 | 0 | 1 | 0 | 0 |
| 9 | `all-progression-is-impossible-without-change.md` | 1 | 0 | 1 | 0 | 0 |
| 10 | `assumptions-damage-relationships.md` | 1 | 0 | 1 | 0 | 0 |

**Working-file names left out** (45 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `KAREN_SOURCE_LESSONS_S344.md` | 8 | 0 | 7 | 0 | 1 |
| 2 | `feeling-stuck-in-life.md` | 3 | 0 | 3 | 0 | 0 |
| 3 | `happiness-is-a-delusion-fulfilment-is-not.md` | 2 | 0 | 2 | 0 | 0 |
| 4 | `positive-vs-negative-motivation.md` | 2 | 0 | 2 | 0 | 0 |
| 5 | `thoughts-and-emotions-connection.md` | 2 | 0 | 2 | 0 | 0 |
| 6 | `I14__meaningful-life-versus-busy-life.md` | 1 | 0 | 1 | 0 | 0 |
| 7 | `I18__persuade-someone-who-disagrees.md` | 1 | 0 | 1 | 0 | 0 |
| 8 | `K10__growth-mindset-at-work.md` | 1 | 0 | 1 | 0 | 0 |
| 9 | `all-progression-is-impossible-without-change.md` | 1 | 0 | 1 | 0 | 0 |
| 10 | `assumptions-damage-relationships.md` | 1 | 0 | 1 | 0 | 0 |

### quote-page

**All files** (182 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `Batch_Report__Six_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fifteen_200_Of_200.md` *(working-file name)* | 22 | 0 | 0 | 22 | 0 |
| 2 | `Batch_Report__Fourteen_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Fourteen.md` *(working-file name)* | 20 | 0 | 0 | 20 | 0 |
| 3 | `Batch_Report__Ten_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Two_S356.md` *(working-file name)* | 20 | 0 | 0 | 20 | 0 |
| 4 | `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Five_S357.md` *(working-file name)* | 18 | 0 | 0 | 18 | 0 |
| 5 | `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Four_S357.md` *(working-file name)* | 18 | 0 | 0 | 18 | 0 |
| 6 | `Batch_Report__Seven_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Six_S357.md` *(working-file name)* | 18 | 0 | 0 | 18 | 0 |
| 7 | `Batch_Report__Twenty_Six_Course_018_Quotes_Corrected_To_S356_Shape_Batch_Six_S356.md` *(working-file name)* | 18 | 0 | 0 | 18 | 0 |
| 8 | `Batch_Report__Eight_Course_001_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Three_S357.md` *(working-file name)* | 17 | 0 | 0 | 17 | 0 |
| 9 | `Batch_Report__Forty_Nine_Course_018_Quotes_Drafted_Corrected_And_Gate_Verified_Batch_Seven.md` *(working-file name)* | 17 | 0 | 0 | 17 | 0 |
| 10 | `Batch_Report__Nine_Instructor_Quotes_Corrected_To_S356_Shape_Batch_Five_S356.md` *(working-file name)* | 17 | 0 | 0 | 17 | 0 |

**Working-file names left out** (160 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `CQ001-007-1__why-being-reflective-beats-being-a-great-thinker.md` | 4 | 0 | 4 | 0 | 0 |
| 2 | `_to_delete/CQ001-044-1__why-knowing-yourself-shapes-how-you-influence-others.md` | 4 | 0 | 4 | 0 | 0 |
| 3 | `_to_delete/CQ001-094-1__why-unsolicited-advice-always-comes-across-as-patronizing.md` | 4 | 0 | 4 | 0 | 0 |
| 4 | `CQ001-002-2__why-every-effect-in-your-life-has-a-cause.md` | 3 | 0 | 3 | 0 | 0 |
| 5 | `CQ001-006-2__why-being-a-contributor-beats-being-a-consumer.md` | 3 | 0 | 3 | 0 | 0 |
| 6 | `CQ001-054-1__why-growth-in-life-depends-on-your-awareness.md` | 3 | 0 | 3 | 0 | 0 |
| 7 | `CQ001-090-2__how-to-understand-behavior-without-endorsing-it.md` | 3 | 0 | 3 | 0 | 0 |
| 8 | `CQ001-170-1__why-your-family-shaped-whether-you-feel-at-peace.md` | 3 | 0 | 3 | 0 | 0 |
| 9 | `CQ001-002-1__why-you-dont-know-it-all-yet.md` | 2 | 0 | 2 | 0 | 0 |
| 10 | `CQ001-005-1__why-what-you-think-is-true-might-not-be.md` | 2 | 0 | 2 | 0 | 0 |

### seven-beliefs-series

**All files** (12 failing files in all; showing 10)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `Batch_Report__Seven_Beliefs_Parts_3_To_9_S387.md` *(working-file name)* | 7 | 0 | 0 | 7 | 0 |
| 2 | `Batch_Report__Seven_Beliefs_Back_Links_S387.md` *(working-file name)* | 5 | 0 | 0 | 5 | 0 |
| 3 | `Batch_Report__Seven_Beliefs_Parts_1_And_2_S387.md` *(working-file name)* | 5 | 0 | 0 | 5 | 0 |
| 4 | `PART_01__the-seven-beliefs-achology-is-built-on.md` | 4 | 0 | 3 | 1 | 0 |
| 5 | `PART_02__can-people-change.md` | 2 | 0 | 1 | 1 | 0 |
| 6 | `PART_09__philosophy-of-life.md` | 2 | 0 | 1 | 1 | 0 |
| 7 | `PART_03__know-thyself.md` | 1 | 0 | 0 | 1 | 0 |
| 8 | `PART_04__thinking-errors.md` | 1 | 0 | 0 | 1 | 0 |
| 9 | `PART_05__understanding-and-managing-emotions.md` | 1 | 0 | 0 | 1 | 0 |
| 10 | `PART_06__emotional-responsibility.md` | 1 | 0 | 0 | 1 | 0 |

**Working-file names left out** (9 failing files in all; showing 9)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `PART_01__the-seven-beliefs-achology-is-built-on.md` | 4 | 0 | 3 | 1 | 0 |
| 2 | `PART_02__can-people-change.md` | 2 | 0 | 1 | 1 | 0 |
| 3 | `PART_09__philosophy-of-life.md` | 2 | 0 | 1 | 1 | 0 |
| 4 | `PART_03__know-thyself.md` | 1 | 0 | 0 | 1 | 0 |
| 5 | `PART_04__thinking-errors.md` | 1 | 0 | 0 | 1 | 0 |
| 6 | `PART_05__understanding-and-managing-emotions.md` | 1 | 0 | 0 | 1 | 0 |
| 7 | `PART_06__emotional-responsibility.md` | 1 | 0 | 0 | 1 | 0 |
| 8 | `PART_07__change-your-life-from-the-inside-out.md` | 1 | 0 | 0 | 1 | 0 |
| 9 | `PART_08__sense-of-purpose.md` | 1 | 0 | 0 | 1 | 0 |

### workbook

**All files** (1 failing files in all; showing 1)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` | 11 | 0 | 10 | 0 | 1 |

**Working-file names left out** (1 failing files in all; showing 1)

| # | File | Failing lines | A | B | C | U |
|---|---|---|---|---|---|---|
| 1 | `DRAFT__The_Karpman_Drama_Triangle_Workbook.md` | 11 | 0 | 10 | 0 | 1 |

## Left open

`field-authority-article/the-importance-of-self-awareness.md` fails `keyword unique in register` (claimed by `self-awareness`). Which article gives up the keyword is being decided elsewhere. Nothing here counts it, recommends on it, or changes it.

## What cannot be told from the report

- Whether any of the 156 `keyword in address slug` failures concerns an address that is already live. If so, a script fix is a redirect decision, not a mechanical one.
- For each of the three C cells that fail at least half of a type, whether the records or the rule are out of date. The report shows the rate, not the history of the rule.
- Whether the files with working-file names, and the files that look like notes without such a name, were meant to be gated at all. Files inside a `_to_delete/` folder (listed with that path) are not flagged by the report's name rule, so they stay in the group their line gives; whether they should be treated as working files: cannot tell.
- Whether punctuation replacement for dashes, or `salvage` for `legacy-page`, changes meaning.
- Whether the register-clash line (left open) behaves the same on the project machine, where the real keyword register may hold rows the rebuilt one lacked (stated in the job 6 report).