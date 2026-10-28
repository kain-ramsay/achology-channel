**For Chat. What this needs from you:** mend 52 paragraphs over 120 words on 34 biographies (section 4) if you want those pages above 86, and rule on two import check instrument faults (section 3). The import itself is finished.

# DONE: the 51 signed author biographies are on the build site, read back and scored (Code, factory session, S198, 28 October 2026)

Answers BRIEF__Import_The_Thirty_Signed_Author_Biographies_S445, BRIEF__Import_The_Two_Signed_Biographies_Egan_And_Kain_S447, the biography rows of BRIEF__Import_The_192_Pages_Re_Signed_With_Full_Course_Names_S447 (21), BRIEF__Import_The_127_Pages_Re_Signed_With_Full_Course_Links_S447 (7) and BRIEF__Import_The_11_Pages_With_Prices_And_Counts_Removed_S447 (3), and the older NOTE__Five_Author_Biographies_Signed_Import_Them_S426 and NOTE__Fourteen_Author_Biographies_Signed_Import_Them_S428, which these supersede. Every record was taken as it stands now (Version 33 or 34).

## 1. What landed
- **51 of 51 signed records** in the author-biography folder: the thirty (S445), Egan and Kain (S447), the five (S426) and the fourteen (S428). All 51 were already on the build site as published pages, so all 51 were **updated in place** by `article_body_update.py --apply --with-seo`. None was created, so `import_author_biographies.py` and `publish_gate.py` were not needed; every page stays published, at the same address.
- **Before:** `body_guard.py --signed` read 1,118 records, 0 with a working note, exit 0 (lock 4).
- **Refused:** none. The tool's own refusals (process text, one internal and one external link, words unchanged by the conversion) passed on all 51.
- **Search fields:** excerpt, search title and description sent from each record. Afterwards all 51 match their records on title, excerpt, search title, description and focus keyword. Gabor Maté's live focus keyword was stored as the literal text `Gabor Maté`; it was written from the record as "Gabor Maté" (a mechanical correction, one meta field, one post).
- **Course links:** three records gained their course's full-name link at its first mention, written by the autolinker with no word changed (project commit 0ce89fc8): Brendon Burchard and Friedrich Nietzsche (The Clarity, Purpose and Personal Effectiveness Masterclass), Robert Cialdini (The Communication Skills and Social Intelligence Masterclass).
- **Read back live:** all 51 clean through `publish_gate.rendered_faults` (carl-jung on a second read; the first fetch timed out).

**The headline line the title ruling owes (RULING__Signed_Pages_Take_Their_Title_From_Post_Title_Drop_The_Old_Headline_S446):** the title is post_title on all 51, and every live title matches its record. 30 bodies opened on a headline, which matched post_title on all 30 and was dropped; 21 carry none. No page shows a headline in its body (0 of 51 stored bodies carry an h1), and no page was refused for one.

**Never imported:** HELD__where-did-life-coaching-come-from is not on the build site in any status, so nothing was taken down.

## 2. Scores (score_run.py, nothing saved; failing tests by the per-test reader, with contentHasAssets and lengthContent out of scope by RULING__The_Article_Publish_Bar_Is_86_..._S449)
All 51 are at or above the article bar of 86: 33 at 86, 16 at 89, 2 at 91. The only failing test on any page is contentHasShortParagraphs, on 34.

| Address | Score | Failing tests |
|---|---|---|
| /learn/general-interest/articles/a-c-grayling/ | 86 | contentHasShortParagraphs |
| /learn/general-interest/articles/joseph-campbell/ | 89 | none |
| /learn/general-interest/articles/kain-ramsay/ | 91 | none |
| /learn/general-interest/articles/nassim-nicholas-taleb/ | 86 | contentHasShortParagraphs |
| /learn/general-interest/articles/thich-nhat-hanh/ | 86 | contentHasShortParagraphs |
| /learn/general-interest/articles/viktor-frankl/ | 86 | contentHasShortParagraphs |
| /learn/helping-people/articles/brene-brown/ | 86 | contentHasShortParagraphs |
| /learn/helping-people/articles/gabor-mate/ | 89 | none |
| /learn/helping-people/articles/gerard-egan/ | 91 | contentHasShortParagraphs |
| /learn/mental-wellness/articles/judith-s-beck/ | 86 | contentHasShortParagraphs |
| /learn/mental-wellness/articles/mark-manson/ | 86 | contentHasShortParagraphs |
| /learn/mental-wellness/articles/rick-hanson/ | 86 | contentHasShortParagraphs |
| /learn/motivation/articles/brendon-burchard/ | 86 | contentHasShortParagraphs |
| /learn/motivation/articles/cal-newport/ | 86 | contentHasShortParagraphs |
| /learn/motivation/articles/robert-greene/ | 89 | none |
| /learn/motivation/articles/ryan-holiday/ | 89 | none |
| /learn/motivation/articles/simon-sinek/ | 89 | none |
| /learn/motivation/articles/steven-pressfield/ | 86 | contentHasShortParagraphs |
| /learn/personal-growth/articles/charles-duhigg/ | 86 | contentHasShortParagraphs |
| /learn/personal-growth/articles/don-miguel-ruiz/ | 86 | contentHasShortParagraphs |
| /learn/personal-growth/articles/james-allen/ | 89 | none |
| /learn/personal-growth/articles/john-c-maxwell/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/abraham-maslow/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/alfred-adler/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/carl-jung/ | 89 | none |
| /learn/psychology/articles/dan-ariely/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/daniel-goleman/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/erik-erikson/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/howard-gardner/ | 89 | none |
| /learn/psychology/articles/irvin-yalom/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/jean-piaget/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/john-dewey/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/jonathan-haidt/ | 89 | none |
| /learn/psychology/articles/jordan-b-peterson/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/malcolm-gladwell/ | 89 | none |
| /learn/psychology/articles/martin-seligman/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/philip-zimbardo/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/robert-cialdini/ | 86 | contentHasShortParagraphs |
| /learn/psychology/articles/sigmund-freud/ | 89 | none |
| /learn/psychology/articles/steven-pinker/ | 89 | none |
| /learn/psychology/articles/william-james/ | 86 | contentHasShortParagraphs |
| /learn/wisdom-for-life/articles/alain-de-botton/ | 89 | none |
| /learn/wisdom-for-life/articles/alan-watts/ | 86 | contentHasShortParagraphs |
| /learn/wisdom-for-life/articles/aristotle/ | 89 | none |
| /learn/wisdom-for-life/articles/arthur-schopenhauer/ | 89 | none |
| /learn/wisdom-for-life/articles/bertrand-russell/ | 89 | none |
| /learn/wisdom-for-life/articles/erich-fromm/ | 86 | contentHasShortParagraphs |
| /learn/wisdom-for-life/articles/friedrich-nietzsche/ | 86 | contentHasShortParagraphs |
| /learn/wisdom-for-life/articles/john-stuart-mill/ | 86 | contentHasShortParagraphs |
| /learn/wisdom-for-life/articles/leo-tolstoy/ | 86 | contentHasShortParagraphs |
| /learn/wisdom-for-life/articles/plato/ | 86 | contentHasShortParagraphs |

## 3. The three import checks (stage5_import_checks.py, author-biography, the 51)
- **Check 1, fields complete:** passes all 51.
- **Check 2, body shape:** fails all 51, on an instrument fault. The type's ruled sections are written as `{name}: Early Years and Formation`, `{name}'s Main Body of Work and Ideas` and `{name}'s Worldwide Influence and Legacy`, and the check compares them with the record's headings without putting the person's name in, so every correct heading reads as "a section the type does not rule". The locked headings are on every page. **20 of the 51 also have no `## Sourcing record` or `## Search and Citation Brief` section** (older record shape): Alain de Botton, Bertrand Russell, Brendon Burchard, Brene Brown, Cal Newport, Don Miguel Ruiz, Friedrich Nietzsche, John C Maxwell, John Dewey, Jonathan Haidt, Jordan B Peterson, Leo Tolstoy, Mark Manson, Nassim Nicholas Taleb, Philip Zimbardo, Robert Cialdini, Ryan Holiday, Simon Sinek, Steven Pinker, Steven Pressfield. Named here, not fixed by hand.
- **Check 3, named files:** not run (no attachment list given). Biography records name their picture in `portrait_image`, and the check asks for `featured_image`, so it would print "names nothing" on all 51; that is the same kind of instrument line. No picture changed: these were body and search field updates, and every page keeps the picture it had.
- 30 of the 51 are dated before the Search and Citation Brief standard; their S329 fields are owed at next edit, not counted.

**Asked of Chat:** a ruling on whether `stage5_import_checks.py` should fill `{name}` for author-biography and read `portrait_image` for check 3. Code has not touched that file.

## 4. Short paragraphs: what the test reads, and the mend list
The stored bodies carry `<p>` tags on every page, so this is not the Help answer fault. The test is reading real paragraphs: each of the 34 failing pages has one to three paragraphs over 120 words, and none of the 17 passing pages has one (their longest run 101 to 120). The 52 paragraphs, by record, with each one's word count and opening words:

- Author_Biography_A_C_Grayling_S304: 151 words, opening "In 2001 The Meaning of Things gathered short"
- Author_Biography_Abraham_Maslow_S305: 122 words, opening "Two things about this idea are commonly got"
- Author_Biography_Alan_Watts_S304: 125 words, opening "The more serious criticism is about accuracy and"
- Author_Biography_Alfred_Adler_S305: 121 words, opening "The healthy answer, in his view, wasn't to"; 129 words, opening "Achology takes a different position on one point."
- Author_Biography_Brendon_Burchard_S304: 128 words, opening "Brendon Burchard, the American author and trainer behind"; 121 words, opening "There is a limit, and it lies in"
- Author_Biography_Brene_Brown_S304: 153 words, opening "Her doctorate in social work followed at the"
- Author_Biography_Cal_Newport_S304: 129 words, opening "Deep Work , from 2016, reached the New"; 121 words, opening "Deep work and digital minimalism have slipped into"
- Author_Biography_Charles_Duhigg_S304: 158 words, opening "Duhigg's three kinds of conversation help you read"
- Author_Biography_Dan_Ariely_S305: 142 words, opening "Predictably Irrational, published in 2008, sets out the"
- Author_Biography_Daniel_Goleman_S304: 122 words, opening "Published in 2013, the book Focus turned back"; 121 words, opening "The honest limit sits inside the term's own"; 139 words, opening ""In Achology's teaching, emotional intelligence is the ability"
- Author_Biography_Don_Miguel_Ruiz_S304: 123 words, opening "Achology differs from Ruiz on one point, and"
- Author_Biography_Erich_Fromm_S304: 125 words, opening "He studied law briefly at the University of"
- Author_Biography_Erik_Erikson_S305: 126 words, opening "Later still, closeness pulls against isolation in early"
- Author_Biography_Friedrich_Nietzsche_S304: 138 words, opening "Eternal recurrence is the thought experiment at the"
- Author_Biography_Gerard_Egan_S298: 139 words, opening "He also gave helpers a simple way to"
- Author_Biography_Irvin_Yalom_S304: 122 words, opening "The honest limit sits close to the strength:"; 141 words, opening "If Yalom's blend of case narrative and existential"
- Author_Biography_Jean_Piaget_S305: 130 words, opening "That second claim, that growth takes a different"
- Author_Biography_John_C_Maxwell_S304: 133 words, opening "The 5 Levels of Leadership, from 2011, argued"; 133 words, opening "He reached the subject by way of the"
- Author_Biography_John_Dewey_S304: 145 words, opening "John Dewey was an American philosopher who rebuilt"; 121 words, opening "The limit sits inside the movement he helped"; 122 words, opening ""In Achology's teaching, character is not defined by"
- Author_Biography_John_Stuart_Mill_S304: 137 words, opening "His central case for individual freedom arrived in"; 125 words, opening "Mill's Utilitarianism was serialised in Fraser's Magazine in"; 121 words, opening "Achology takes a different position from Mill on"
- Author_Biography_Jordan_B_Peterson_S305: 123 words, opening "Jordan B. Peterson is a Canadian clinical psychologist"; 124 words, opening "In 2018 came 12 Rules for Life: An"; 166 words, opening "Achology takes a different view of personality. His"
- Author_Biography_Judith_S_Beck_S305: 136 words, opening "A thought flashes up before an important meeting,"
- Author_Biography_Leo_Tolstoy_S304: 121 words, opening "He told the story of that crisis, and"; 124 words, opening "What Is Art? took the same direct habit"
- Author_Biography_Mark_Manson_S304: 124 words, opening "Somewhere on your mental to-do list sits a"; 140 words, opening ""In Achology's teaching, to have a sense of"; 136 words, opening "Are the things you worry about most really"
- Author_Biography_Martin_Seligman_S305: 122 words, opening "Achology's Seven Beliefs series draws on this work."
- Author_Biography_Nassim_Nicholas_Taleb_S304: 130 words, opening "Nassim Nicholas Taleb is a former options trader"; 137 words, opening "If the argument about fairness appeals more than"
- Author_Biography_Philip_Zimbardo_S305: 125 words, opening "Brooklyn College gave him a combined grounding in"
- Author_Biography_Plato_S304: 121 words, opening "Out of that questioning grew Plato's most distinctive"
- Author_Biography_Rick_Hanson_S305: 122 words, opening "Hardwiring Happiness, in 2013, is where the method"
- Author_Biography_Robert_Cialdini_S305: 123 words, opening "Achology's own account of communication differs from his"
- Author_Biography_Steven_Pressfield_S305: 142 words, opening "A long run of ordinary jobs followed his"; 136 words, opening "His own books take the idea further. The"
- Author_Biography_Thich_Nhat_Hanh_S305: 126 words, opening "His teaching was tested by war. In Vietnam"
- Author_Biography_Viktor_Frankl_S305: 140 words, opening ""In Achology's teaching, to have a sense of"
- Author_Biography_William_James_S304: 134 words, opening "He then turned to religion itself, most fully"

Splitting each at a natural sentence break, with no word changed, should take these 34 from 86 to 89. They already meet the bar of 86, so no page waits on it; send a NOTE if you mend them and Code updates and rescores.

## 5. Dispositions
NOTE__Five_Author_Biographies_Signed_Import_Them_S426 and NOTE__Fourteen_Author_Biographies_Signed_Import_Them_S428: DONE, superseded by the S445 and S447 versions now landed. BRIEF__Import_The_Thirty_Signed_Author_Biographies_S445 and BRIEF__Import_The_Two_Signed_Biographies_Egan_And_Kain_S447: DONE. The 192, 127 and 11 briefs: their biography rows are done; each stays open for its other rows.

OWED BACK: Chat's ruling on the two stage 5 instrument lines (section 3); a NOTE if the 52 paragraphs are mended.

*No em or en dashes in this file; checked before writing.*
