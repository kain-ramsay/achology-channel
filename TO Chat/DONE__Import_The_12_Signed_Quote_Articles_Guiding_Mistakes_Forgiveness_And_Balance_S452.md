**For Chat. What this needs from you:** record mends on all twelve (section 5). These records name no inbound links and no link up (section 4), so that part of the brief had nothing to act on. All twelve are on the build site, all under 86, left as they are. Factory side session of Code, 2 November 2026.

# DONE: the 12 signed quote articles on guiding others, mistakes, forgiveness, balance and life skills (Code, factory, 2 November 2026)

Answers BRIEF__Import_The_12_Signed_Quote_Articles_Guiding_Mistakes_Forgiveness_And_Balance_S452.

## 1. The counts

- **Imported:** 12 of 12. 8 updated in place, matched by quote_id, still published. 4 created as drafts (no post carried their quote_id).
- **Redirects:** 12 written and proved at 301 by `publish_gate.py --write-redirect`.
- **Inbound links:** none to place; no record has an `inbound_from` field (section 4).
- **Link up:** none to check; no record has a `related_article_slugs` field (section 4).
- **Scores:** 12 read, 0 at 86 or more (section 5).
- The 91 held round two pages were not touched.

## 2. The three import checks

- **Fields present and signed.** All 12 carry Kain's 2 November signature word for word. post_name, quote_id, focus phrase, address and redirect_from match the brief, and title, headline and search title are the same.
- **Body.** `body_guard.py --signed`: 12 records, 0 working notes, exit 0. The body shape check passed all 12, and every ruled heading uses curly marks.
- **Named files.** Course quote covers 001 and 018 are in the theme. Kain Ramsay's author picture passed the importer's author check. The four book quotes (Q07015, Q07020, Q07021, Q07026) carry The Ultimate Life Coaching Handbook cover.
- **Focus phrase:** once in the body on all 12, in the opening paragraph, and in no subheading.

## 3. On the build site

| quote_id | Post | Status | New address | Old address redirects |
|---|---|---|---|---|
| CQ001-066-1 | 44075 | draft, created | /learn/mental-wellness/quotes/what-happens-when-your-life-is-out-of-balance/ | 301 proved |
| CQ001-088-1 | 44076 | draft, created | /learn/mental-wellness/quotes/how-do-you-let-go-of-resentment/ | 301 proved |
| CQ001-101-1 | 44077 | draft, created | /learn/motivation/quotes/who-does-forgiveness-really-set-free/ | 301 proved |
| CQ001-125-1 | 44078 | draft, created | /learn/mental-wellness/quotes/is-a-good-life-really-about-balance/ | 301 proved |
| CQ018-025-4 | 36359 | publish, updated | /learn/mental-wellness/quotes/what-does-it-mean-to-learn-from-your-mistakes/ | 301 proved |
| CQ018-049-1 | 36395 | publish, updated | /learn/mental-wellness/quotes/can-you-guide-someone-further-than-youve-gone-yourself/ | 301 proved |
| CQ018-061-1 | 36408 | publish, updated | /learn/mental-wellness/quotes/why-let-go-of-resentment/ | 301 proved |
| CQ018-087-2 | 36452 | publish, updated | /learn/mental-wellness/quotes/what-are-the-benefits-of-learning-from-mistakes/ | 301 proved |
| Q07015 | 36266 | publish, updated | /learn/helping-people/quotes/why-do-we-struggle-with-the-things-school-never-taught-us/ | 301 proved |
| Q07020 | 35454 | publish, updated | /learn/helping-people/quotes/can-you-help-someone-make-wiser-choices-than-your-own/ | 301 proved |
| Q07021 | 36272 | publish, updated | /learn/helping-people/quotes/does-how-you-handle-hard-times-affect-how-you-help-others/ | 301 proved |
| Q07026 | 35460 | publish, updated | /learn/helping-people/quotes/can-life-skills-be-taught-when-life-has-no-rulebook/ | 301 proved |

- `--verify`: 12 of 12 clean against the records (title, excerpt, category, tags, quote fields, Rank Math fields).
- **Read back off the build site**, the eight published pages: each answers 200, and the headline, search title and description match the record. The course quotes show course cover 018 and Kain's picture. The four book quotes show the handbook cover and Kain's picture.
- **The four drafts** cannot be read publicly. Their redirects answer 301 to a draft address, which answers 404 until they are published. Publishing them is Kain's word (pipeline stage 7).

## 4. Inbound links and the link up: nothing named

Unlike the 8 and 10 batches, these 12 records carry neither `inbound_from` nor `related_article_slugs`. Each record's Planned links section reads "Inbound: theme-built and automatic, per DSRD 1 section 6.1". The internal link it plans is "the source course, linked once in the Book", which is on achology.com. So no inbound link was placed and no link up was checked. If these should carry the same fields as the earlier batches, that's a record mend.

## 5. Rank Math scores against 86

Read one editor at a time, 12 seconds apart, nothing saved; the scoring session was revoked afterwards.

| Record | Post | Address | Focus phrase | Score | Against 86 | Failing tests |
|---|---|---|---|---|---|---|
| CQ018-049-1 | 36395 | /learn/mental-wellness/quotes/can-you-guide-someone-further-than-youve-gone-yourself/ | guide someone further | 82 | **under** | keywordInSubheadings, linksHasInternal |
| CQ018-061-1 | 36408 | /learn/mental-wellness/quotes/why-let-go-of-resentment/ | why let go of resentment | 82 | **under** | keywordInSubheadings, linksHasInternal |
| CQ018-087-2 | 36452 | /learn/mental-wellness/quotes/what-are-the-benefits-of-learning-from-mistakes/ | benefits of learning from mistakes | 82 | **under** | keywordInSubheadings, linksHasInternal |
| CQ018-025-4 | 36359 | /learn/mental-wellness/quotes/what-does-it-mean-to-learn-from-your-mistakes/ | learn from your mistakes | 81 | **under** | keywordInSubheadings, linksHasInternal |
| CQ001-088-1 | 44076 | /learn/mental-wellness/quotes/how-do-you-let-go-of-resentment/ | let go of resentment | 80 | **under** | keywordInSubheadings, linksHasInternal |
| CQ001-101-1 | 44077 | /learn/motivation/quotes/who-does-forgiveness-really-set-free/ | forgiveness really set free | 80 | **under** | keywordInSubheadings, linksHasInternal |
| CQ001-125-1 | 44078 | /learn/mental-wellness/quotes/is-a-good-life-really-about-balance/ | life really about balance | 80 | **under** | keywordInSubheadings, linksHasInternal |
| Q07021 | 36272 | /learn/helping-people/quotes/does-how-you-handle-hard-times-affect-how-you-help-others/ | handle hard times | 79 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| Q07026 | 35460 | /learn/helping-people/quotes/can-life-skills-be-taught-when-life-has-no-rulebook/ | life skills be taught | 79 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals |
| CQ001-066-1 | 44075 | /learn/mental-wellness/quotes/what-happens-when-your-life-is-out-of-balance/ | life is out of balance | 76 | **under** | keywordInSubheadings, linksHasInternal, titleStartWithKeyword |
| Q07015 | 36266 | /learn/helping-people/quotes/why-do-we-struggle-with-the-things-school-never-taught-us/ | school never taught us | 75 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals, titleStartWithKeyword |
| Q07020 | 35454 | /learn/helping-people/quotes/can-you-help-someone-make-wiser-choices-than-your-own/ | wiser choices | 74 | **under** | keywordInSubheadings, linksHasExternals, linksNotAllExternals, titleStartWithKeyword |

**Why, measured on the records:**
- **Phrase in no subheading, all 12.**
- **The eight course quotes have no internal link.** Their one body link goes to the course on achology.com, which Rank Math counts as outside.
- **The four book quotes have no outside link.** Their one body link is the internal handbook book note.
- **Three titles do not open with the phrase:** CQ001-066-1, Q07015 and Q07020.

The pages are left as they are until the records are mended. Then they re-enter at import and are rescored.

## 6. Not run, said plainly

- Google's Rich Results test was not run.
- No score line went into a DSRD 6 record.
- The quote cards were not re-baked.

OWED BACK: your record mends for the twelve (the phrase in one heading; one internal link on the course quotes and one outside link on the book quotes; the inbound and link up fields if they are wanted). Then the twelve re-import and rescore.

*No em or en dashes in this file; checked before writing.*
