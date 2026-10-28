**For Chat. What this needs from you:** one decision on the four book notes still at 81 to 85 (section 3): the fix is a link that wraps the whole book title in each opening line, which is a change to the signed body, so it is yours to make in the records (and Kain's to re-sign if you judge it needs it); then Code updates and rescores the four.

# DONE: 54 book notes updated, mended and rescored (Code, factory session, S196, 28 October 2026)

Answers NOTE__48_Book_Notes_Long_Paragraphs_Split_Update_And_Rescore_S450, against the article bar of 86 (RULING__The_Article_Publish_Bar_Is_86_Publish_The_Five_Anxiety_Articles_S449).

## 1. Result in one line
50 of the 54 now score 88 with no test failing. Four sit at 81 to 85, all on one cause the brief did not foresee (section 3).

## 2. What was done
- **Checks first.** `body_guard.py --signed`: 1,014 records read, 0 with a working note in the body. `stage5_import_checks.py --type book-note` on the 48: 48 of 48 pass checks 1 and 2; check 3 not run (no picture changed). Before sending, each of the 48 bodies was converted through the book note converter and read: every one carries paragraph tags and the longest paragraph on any page is 120 words.
- **The 48, updated.** `article_body_update.py book-note:<slug> --apply --with-seo`: 48 bodies sent, 0 refused or failed. Five read back through the publish gate (the-social-animal-aronson, free-will-by-sam-harris, mental-efficiency, how-to-fix-a-broken-heart, cognitive-behavior-therapy-second-edition): all clean.
- **the-social-animal-aronson's four fields.** `--with-seo` sends only `post_excerpt` for a book note, because it reads `rm_seo_title` and `rm_seo_description` and book note records spell them `prod_rm_*` (a gap in the tool, noted for whoever next owns it; the five other fields of the 47 did not change, so nothing else was missed). The four signed values were written directly from the record and read back: focus phrase "the social animal", the new search title, the new description, and the cover's alt text. Score 88, nothing failing.
- **free-will-sam-harris, new address.** The page is now /learn/psychology/book-notes/free-will-by-sam-harris/. The 301 was written through `publish_gate.py --write-redirect` and proved by the server: /learn/psychology/book-notes/free-will-sam-harris/ answers 301 to the new address. The record's `post_name` and `address` now carry the new address, and a `redirect_from` line names the old one. keywordInPermalink now passes (79 to 85).
- **a-guide-to-rational-living and a-path-through-the-jungle (42).** Both already read 88 before anything was touched here, with keywordInTitle and titleStartWithKeyword passing: the built title field had been mended since the S190 DONE. Nothing changed; rescored at 88.
- **The three search phrases.** Not changed, for the reason in section 3.

## 3. Why four are still under 86, and the fix
The brief read the subheading test as matching the signed page heading. It does not. Read from the editor, Rank Math's keywordInSubheadings pattern is `<h[2-6]...>`, then any text, then the phrase's words joined by spaces or punctuation, then any text, then `</h[2-6]>`. The "any text" runs across headings, so the test passes when the phrase appears anywhere in the body between the first section heading and the last. The page title is never read.

On all four the phrase is in the opening line, but the publisher link wraps only the first word or two of the book's title, so the link's closing tag breaks the phrase:
- free-will-by-sam-harris: link on "Free Will", then " by Sam Harris".
- best-self-be-you-only-better: link on "Best Self", then ": Be You, Only Better".
- identity-youth-and-crisis: link on "Identity", then ": Youth and Crisis".
- yes-50-scientifically-proven-ways-to-be-persuasive: link on "Yes!" only, and the full title is spelled out only in Sources, which is after the last heading (so keywordIn10Percent fails too).

The passing page proves it: a-guide-to-rational-living links its whole title, "A Guide to Rational Living", and passes. Punctuation in the phrase is not the cause: the test treats any run of spaces and punctuation as one gap. So no spelling of the three phrases can pass, and the only phrase forms that would pass ("free will", "best self", "identity") are not the claimed searches, so Code did not set them.

**The fix (yours, in the records):** in each opening line, let the publisher link carry the book's whole title (for free will, the sentence's "Free Will by Sam Harris" or the link on "Free Will" with "by Sam Harris" moved inside it). No word changes. For yes-50, the opening line also needs the full title once inside its first tenth. Expected: each of the four to 88.

## 4. The score table (54 pages, read by `score_run.py`; failing tests by the S187 per-test reader)
| Address | Score | Failing tests |
|---|---|---|
| /learn/mental-wellness/book-notes/a-liberated-mind/ | 88 | none |
| /learn/psychology/book-notes/childhood-and-society/ | 88 | none |
| /learn/helping-people/book-notes/cognitive-behavior-therapy-second-edition/ | 88 | none |
| /learn/personal-growth/book-notes/come-together/ | 88 | none |
| /learn/psychology/book-notes/decisive/ | 88 | none |
| /learn/helping-people/book-notes/difficult-conversations-patton/ | 88 | none |
| /learn/motivation/book-notes/extreme-ownership-willink/ | 88 | none |
| /learn/psychology/book-notes/frames-of-mind/ | 88 | none |
| /learn/personal-growth/book-notes/further-along-the-road-less-travelled/ | 88 | none |
| /learn/helping-people/book-notes/getting-past-no/ | 88 | none |
| /learn/wisdom-for-life/book-notes/homage-to-catalonia/ | 88 | none |
| /learn/motivation/book-notes/how-the-mighty-fall/ | 88 | none |
| /learn/mental-wellness/book-notes/how-to-fix-a-broken-heart/ | 88 | none |
| /learn/personal-growth/book-notes/keeping-the-love-you-find/ | 88 | none |
| /learn/motivation/book-notes/linchpin/ | 88 | none |
| /learn/wisdom-for-life/book-notes/meditations-for-mortals/ | 88 | none |
| /learn/personal-growth/book-notes/mental-efficiency/ | 88 | none |
| /learn/psychology/book-notes/multiple-intelligences-new-horizons/ | 88 | none |
| /learn/wisdom-for-life/book-notes/nature-emerson/ | 88 | none |
| /learn/mental-wellness/book-notes/notes-on-a-nervous-planet/ | 88 | none |
| /learn/wisdom-for-life/book-notes/on-the-tranquility-of-mind/ | 88 | none |
| /learn/personal-growth/book-notes/peace-power-and-plenty/ | 88 | none |
| /learn/mental-wellness/book-notes/shift/ | 88 | none |
| /learn/mental-wellness/book-notes/shyness-what-it-is-what-to-do-about-it/ | 88 | none |
| /learn/psychology/book-notes/surrounded-by-psychopaths/ | 88 | none |
| /learn/helping-people/book-notes/talking-to-crazy/ | 88 | none |
| /learn/helping-people/book-notes/teacher-and-child/ | 88 | none |
| /learn/personal-growth/book-notes/the-8th-habit/ | 88 | none |
| /learn/wisdom-for-life/book-notes/the-art-of-the-good-life/ | 88 | none |
| /learn/mental-wellness/book-notes/the-beck-diet-solution/ | 88 | none |
| /learn/psychology/book-notes/the-doors-of-perception/ | 88 | none |
| /learn/mental-wellness/book-notes/the-feeling-good-handbook/ | 88 | none |
| /learn/motivation/book-notes/the-gap-and-the-gain/ | 88 | none |
| /learn/psychology/book-notes/the-honest-truth-about-dishonesty/ | 88 | none |
| /learn/wisdom-for-life/book-notes/the-perennial-philosophy/ | 88 | none |
| /learn/general-interest/book-notes/the-quick-and-easy-way-to-effective-speaking/ | 88 | none |
| /learn/personal-growth/book-notes/the-relationship-cure/ | 88 | none |
| /learn/mental-wellness/book-notes/the-six-pillars-of-self-esteem/ | 88 | none |
| /learn/helping-people/book-notes/the-skilled-helper/ | 88 | none |
| /learn/mental-wellness/book-notes/the-tao-of-fully-feeling/ | 88 | none |
| /learn/wisdom-for-life/book-notes/the-tao-te-ching/ | 88 | none |
| /learn/helping-people/book-notes/the-ultimate-life-coaching-handbook/ | 88 | none |
| /learn/personal-growth/book-notes/thrift/ | 88 | none |
| /learn/wisdom-for-life/book-notes/time-and-free-will/ | 88 | none |
| /learn/mental-wellness/book-notes/tusculan-disputations/ | 88 | none |
| /learn/psychology/book-notes/what-do-you-say-after-you-say-hello/ | 88 | none |
| /learn/psychology/book-notes/what-life-could-mean-to-you/ | 88 | none |
| /learn/psychology/book-notes/the-social-animal-aronson/ | 88 | none |
| /learn/psychology/book-notes/free-will-by-sam-harris/ | 85 | keywordInSubheadings |
| /learn/mental-wellness/book-notes/best-self-be-you-only-better/ | 85 | keywordInSubheadings |
| /learn/psychology/book-notes/identity-youth-and-crisis/ | 85 | keywordInSubheadings |
| /learn/psychology/book-notes/yes-50-scientifically-proven-ways-to-be-persuasive/ | 81 | keywordIn10Percent, keywordInSubheadings |
| /learn/mental-wellness/book-notes/a-guide-to-rational-living/ | 88 | none |
| /learn/mental-wellness/book-notes/a-path-through-the-jungle/ | 88 | none |

The 88 ceiling on every page is contentHasAssets (1 of 6) and lengthContent (3 of 8), both earning short rather than failing, as on every book note since S190.

## 5. Two things worth knowing
- The same split-link pattern may sit on other book notes that pass only because their phrase appears again later in the body. It is worth a check whenever a book note fails keywordInSubheadings.
- `book_note_import.py` stops at start-up: it reads `Batch_Report__S310_Fourth_Expansion_And_Reverification.md` from the book-note records folder, and that file is no longer there. It was not needed for this job.

OWED BACK: Chat's fix to the four records' opening links (section 3), then Code updates and rescores those four.

*No em or en dashes in this file; checked before writing.*
