**Needs from Chat: read the proof below and close the card "Site search: built and working". Two things still wait on others: your words for three labels (TO Chat/ASK__Site_Search_Words_The_Brief_Does_Not_Give_S203.md), and Kain's eye on the as-you-type preview round. Theme (side), S203.**

# SHIP: one search for the whole site, theme 0.707.681 to 0.707.683 (S203)

**From:** Claude Code, theme side session, S203, 1 November 2026. **To:** Claude Chat.
**Built:** BRIEF__Site_Search_One_Search_For_The_Whole_Site_S448, RULING__The_Search_Synonym_List_S448, R9 of BRIEF__Page_Readiness_Reader_Halves_Fixes_For_Code_S448, and the S202 review's search row 9 on the theme queue.
**Deployed by the theme main session:** 0.707.681 (the search), 0.707.682 (the front page box's shortcut) and 0.707.683 (Did you mean on longer words). Local copy, server and zip agree. Every result below was read from the build site over SSH, one page at a time, 10 seconds apart.

## The five builds (brief items 1 to 5)

1. **One index for the whole site.** SearchWP's default engine, the one the header search uses, now covers the four Knowledge Hub kinds, the 375 Help answers and every published page. A page built later joins on its own. Titles weigh 80 and focus keywords 60, against 5 for body text. An exact title is moved to first place by the theme. Readers never see the component sheet (/cards/), the thank-you page, or any page Rank Math keeps out of search engines. The Help engine is untouched, so the /help/ search works as before. Proof: "refund" finds 40 results (37 Help answers, 1 page, 1 article, 1 quote), with the Refund Policy page first. "Kain Ramsay" finds his own page first.
2. **The results page.** It is headed "Search Achology". Help and Pages appear as their own kinds in the band, with the DSRD 9 section 38.4 tiles: off-white, with a question-mark glyph or a page glyph in orange (rgb 184 70 15 on rgb 243 244 244). Nothing else on the signed page changed. Course pages will show as Pages until a course template exists to tell them apart.
3. **The Knowledge Hub shortcut.** The front page box carries `ach_in=hub`, read from /learn/. Its results show the four Knowledge Hub kinds only. One line under the count reads "Showing Knowledge Hub results only. Search all of Achology", with the second sentence as the link to the whole-site search. Code drafted these words under the brief for Kain's eye. Proof: "anxiety" through the shortcut finds 103 (47 Articles, 35 Book Notes, 21 Quotes).
4. **The preview as you type: held.** The licence includes SearchWP's Live Ajax Search, but how the dropdown looks is not signed. It becomes a four-option round in the Change Viewer, and goes to the theme main session for Kain when built. The plugin is not installed on the build site yet.
5. **Spelling help.** Where SearchWP supplies a correction, the no-results line opens with "Did you mean" and the corrected word as a link that runs that search. Proof: "pyschologgy" shows "Did you mean psychology? Check the spelling, or try one of these popular searches." SearchWP only finds candidates that share a sound code, so "procrastinashun" gets no suggestion and shows the plain line. Everyday misspellings still find their pieces with no line at all: "anxeity" finds 106 anxiety pieces.

## R9 and queue row 9

- **R9, done.** /?s=zzqxv answers 200 with "No results for "zzqxv"", the popular searches, the subjects and the ask line, and shows no Best Match and no result card. The cause: SearchWP's "did you mean" setting swaps any word it cannot find for the nearest word in its index, however far off. The theme now keeps that swap only for a near misspelling (two edits at most, and no more than a third of the word). A swap up to a third of the word becomes the "Did you mean" line, and anything further finds nothing.
- **Row 9, done.** /page/99/?s=anxiety answers 404, /page/2/?s=anxiety answers 200, and /page/2/?s=zzqxv answers 404. The check is made against the search's own page count (achology_kh_search_page). Row 9 is struck on the theme queue.

## The synonym ruling: five tests (result counts)

- "can't stop worrying": 21 results, led by "Can You Use Anxiety to Your Advantage?" and "Why Do I Get Anxiety for No Reason?".
- "EQ": 63, led by "Emotional Intelligence: Summary and Key Ideas".
- "DiMAP": 1,137, led by "What does an applied psychology course cover?". The count is high because SearchWP splits a long synonym into single words, so "Diploma Course in Modern Applied Psychology" matches nearly every page. The top results are right. There is no Diploma course page yet for it to find.
- "counseling": 199, led by "What Is Counselling, and Is It the Same as Therapy?".
- "money back": 23, the Help answers on refunds first.

The ruling says 37 lines; DSRD 1 section 7.6 holds 39 since Kain's S448 renames, and the 39 are set, word for word, replace off. Two S178 lines that the list does not cover are kept: "self esteem" finds "self-esteem", and "behavior" finds "behaviour".

## Measured in WebKit at 1280, 834 and 390

Four pages: "refund", "zzqxv", "anxiety" through the shortcut, and "pyschologgy". None scrolls sideways at any width. The phone kinds bar swipes within itself, as Kain chose at S178. The heading, the count, the shortcut line and the hint are read from the rendered page.

## The answers owed (brief items 6 and 7)

6. **The licence:** SearchWP Standard, valid to 26 August 2027. By SearchWP's own plan table, Standard includes Live Ajax Search Results. Metrics and Statistics, Related Content and Conditional Redirects are in Pro only, so none of the three is included.
7. **The no-results log:** without Metrics, SearchWP's built-in Statistics and its no-results list serve. The log holds 2,835 searches from 31 August to 1 November 2026, 124 of them with no results. Most are test searches. Clear the log at launch, not before, as the brief says.

## The older briefs

- BRIEF__Build_The_Site_Search_Results_Page_To_DSRD_9_Section_38_S375: closed by this ship. Its one open item was the scope question, which DSRD 1 section 7.1 settled at S448 and 0.707.681 builds. Its header control and dropdown part had already passed to the S321 sitting.
- BRIEF__Render_The_Header_With_A_Search_Control_For_Kains_Eye_S321: already closed at S179, and in the Archive. The dropdown preview it held is the round named in item 4.

## Reach

The same field and the same results page serve the header, the /learn/ banner and the 404 page, so all three now search the whole site. /learn/ alone opens on the shortcut. The /help/ box keeps its own engine, as the brief asks.

## The SearchWP options, before and after

**searchwp_engines, before:**

```json
{"default":{"label":"Default","settings":{"stemming":true,"adminengine":false},"sources":{"post.article":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"taxonomy":{"kh_tag":50,"kh_category":20},"meta":{"quote_author":40,"quote_text":20,"source_book_author":40,"source_book_title":40,"subject_name":40,"whats_inside":10,"rank_math_focus_keyword":60}},"rules":[],"options":[]},"post.book_note":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"taxonomy":{"kh_tag":50,"kh_category":20},"meta":{"quote_author":40,"quote_text":20,"source_book_author":40,"source_book_title":40,"subject_name":40,"whats_inside":10,"rank_math_focus_keyword":60}},"rules":[],"options":[]},"post.quote":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"taxonomy":{"kh_tag":50,"kh_category":20},"meta":{"quote_author":40,"quote_text":20,"source_book_author":40,"source_book_title":40,"subject_name":40,"whats_inside":10,"rank_math_focus_keyword":60}},"rules":[],"options":[]},"post.workbook":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"taxonomy":{"kh_tag":50,"kh_category":20},"meta":{"quote_author":40,"quote_text":20,"source_book_author":40,"source_book_title":40,"subject_name":40,"whats_inside":10,"rank_math_focus_keyword":60}},"rules":[],"options":[]}}},"help":{"label":"Help","settings":{"stemming":true,"adminengine":false},"sources":{"post.faq_article":{"attributes":{"title":300,"content":1,"slug":300,"excerpt":1,"author":300,"meta":{"*":1}},"rules":[],"options":[]}}}}

```

**searchwp_engines, after (read back):**

```json
{"default":{"label":"Default","settings":{"stemming":true,"adminengine":false},"sources":{"post.article":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"taxonomy":{"kh_tag":50,"kh_category":20},"meta":{"quote_author":40,"quote_text":20,"source_book_author":40,"source_book_title":40,"subject_name":40,"whats_inside":10,"rank_math_focus_keyword":60}},"rules":[],"options":[]},"post.book_note":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"taxonomy":{"kh_tag":50,"kh_category":20},"meta":{"quote_author":40,"quote_text":20,"source_book_author":40,"source_book_title":40,"subject_name":40,"whats_inside":10,"rank_math_focus_keyword":60}},"rules":[],"options":[]},"post.quote":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"taxonomy":{"kh_tag":50,"kh_category":20},"meta":{"quote_author":40,"quote_text":20,"source_book_author":40,"source_book_title":40,"subject_name":40,"whats_inside":10,"rank_math_focus_keyword":60}},"rules":[],"options":[]},"post.workbook":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"taxonomy":{"kh_tag":50,"kh_category":20},"meta":{"quote_author":40,"quote_text":20,"source_book_author":40,"source_book_title":40,"subject_name":40,"whats_inside":10,"rank_math_focus_keyword":60}},"rules":[],"options":[]},"post.faq_article":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"meta":{"rank_math_focus_keyword":60,"*":1}},"rules":[],"options":[]},"post.page":{"attributes":{"title":80,"slug":60,"excerpt":40,"content":5,"meta":{"rank_math_focus_keyword":60,"rank_math_description":20}},"rules":[],"options":[]}}},"help":{"label":"Help","settings":{"stemming":true,"adminengine":false},"sources":{"post.faq_article":{"attributes":{"title":300,"content":1,"slug":300,"excerpt":1,"author":300,"meta":{"*":1}},"rules":[],"options":[]}}}}

```

**searchwp_synonyms, before:**

```json
[{"sources":"cbt","synonyms":"cognitive behavioural therapy","replace":false},{"sources":"nlp","synonyms":"neuro-linguistic programming","replace":false},{"sources":"eq","synonyms":"emotional intelligence","replace":false},{"sources":"self worth","synonyms":"self-esteem","replace":false},{"sources":"self esteem","synonyms":"self-esteem","replace":false},{"sources":"behavior","synonyms":"behaviour","replace":false},{"sources":"counseling","synonyms":"counselling","replace":false},{"sources":"counselor","synonyms":"counsellor","replace":false},{"sources":"behavioral","synonyms":"behavioural","replace":false}]

```

**searchwp_synonyms, after (read back, 41 lines):**

```json
[{"sources":"CBT","synonyms":"cognitive behavioural therapy","replace":false},{"sources":"cognitive behavioural therapy","synonyms":"CBT","replace":false},{"sources":"NLP","synonyms":"neuro-linguistic programming, neuro linguistic programming","replace":false},{"sources":"neuro-linguistic programming, neuro linguistic programming","synonyms":"NLP","replace":false},{"sources":"EQ, EI, emotional IQ","synonyms":"emotional intelligence","replace":false},{"sources":"emotional intelligence","synonyms":"EQ, emotional IQ","replace":false},{"sources":"DiMAP","synonyms":"Diploma Course in Modern Applied Psychology, modern applied psychology","replace":false},{"sources":"modern applied psychology","synonyms":"DiMAP","replace":false},{"sources":"CPD","synonyms":"continuing professional development","replace":false},{"sources":"VALTS","synonyms":"Virtual Achologist Led Training Sessions","replace":false},{"sources":"PALS","synonyms":"Peer-Peer Applied Learning Sessions","replace":false},{"sources":"CIPS","synonyms":"Competency Improvement Practice Sessions","replace":false},{"sources":"SoMAP","synonyms":"Society of Modern Applied Psychology","replace":false},{"sources":"UKRLP","synonyms":"UK Register of Learning Providers","replace":false},{"sources":"MIW","synonyms":"Mindfulness, Applied Insight and Wisdom","replace":false},{"sources":"counseling","synonyms":"counselling","replace":false},{"sources":"counselor, counselors","synonyms":"counsellor, counsellors","replace":false},{"sources":"behavioral","synonyms":"behavioural","replace":false},{"sources":"judgment","synonyms":"judgement","replace":false},{"sources":"practicing","synonyms":"practising","replace":false},{"sources":"worry, worrying, can't stop worrying, overthinking, panic, nervous","synonyms":"anxiety","replace":false},{"sources":"stressed, overwhelmed, burnout, burned out, burnt out","synonyms":"stress","replace":false},{"sources":"low mood, feeling down, feeling low, sad","synonyms":"depression","replace":false},{"sources":"insecure, insecurity, not good enough, self worth","synonyms":"self-esteem, confidence","replace":false},{"sources":"imposter syndrome, impostor syndrome, doubting myself","synonyms":"self-doubt","replace":false},{"sources":"procrastinate, procrastinating, can't get motivated, lazy","synonyms":"procrastination, motivation, self-discipline","replace":false},{"sources":"stuck, feel stuck, lost in life, no direction","synonyms":"purpose, direction","replace":false},{"sources":"shy, shyness, awkward, social anxiety","synonyms":"social confidence","replace":false},{"sources":"people pleaser, people pleasing, can't say no","synonyms":"boundaries, assertiveness","replace":false},{"sources":"bereavement, loss, losing someone","synonyms":"grief","replace":false},{"sources":"meditation, meditate","synonyms":"mindfulness","replace":false},{"sources":"hypnosis","synonyms":"hypnotherapy","replace":false},{"sources":"personal agency","synonyms":"empowerment, empowered, empower","replace":false},{"sources":"long reads, long read","synonyms":"in-depth, deep dive","replace":false},{"sources":"life coach, become a coach","synonyms":"life coaching","replace":false},{"sources":"talking therapy","synonyms":"counselling","replace":false},{"sources":"certification, accredited, accreditation","synonyms":"certificate","replace":false},{"sources":"money back, cancel","synonyms":"refund","replace":false},{"sources":"cost, price, how much","synonyms":"pricing","replace":false},{"sources":"self esteem","synonyms":"self-esteem","replace":false},{"sources":"behavior","synonyms":"behaviour","replace":false}]

```

OWED BACK: nothing from this file. The ASK carries the three questions.

*No em or en dashes in this file; checked before writing.*
