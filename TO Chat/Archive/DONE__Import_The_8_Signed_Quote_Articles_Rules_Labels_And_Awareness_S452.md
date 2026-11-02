> CHAT DISPOSITION, S453 (2 November 2026): Answered: BRIEF__Update_The_103_Round_Two_Quote_Articles_Mended_To_The_Bar_S453.
**For Chat. What this needs from you:** record mends on seven of the eight (section 5), and the 24 inbound sentences as an attachment (section 4). All eight are on the build site; one is at 86, seven are under and left as they are. Factory side session of Code, 2 November 2026.

# DONE: the 8 signed quote articles on rules, labels and awareness (Code, factory, 2 November 2026)

Answers BRIEF__Import_The_8_Signed_Quote_Articles_Rules_Labels_And_Awareness_S452.

## 1. The counts

- **Imported:** 8 of 8. 5 updated in place, matched by quote_id, still published. 3 created as drafts (no post carried their quote_id).
- **Redirects:** 8 written and proved at 301 by `publish_gate.py --write-redirect`.
- **Inbound links:** 0 of 24 placed (section 4).
- **Link up:** 8 of 8 named articles answer 200. The link up itself is on no page (section 3).
- **Scores:** 8 read, 1 at 86 or more (section 5).
- The 89 held round two pages were not touched.

## 2. The three import checks

- **Fields present and signed.** All 8 carry Kain's 2 November signature word for word. post_name, quote_id, focus phrase, address and redirect_from match the brief. Title, headline and search title are the same on all 8.
- **Body.** `body_guard.py --signed`: 8 records, 0 working notes, exit 0. The importer's body shape check passed all 8.
- **Named files.** Course quote covers 001 and 018 are in the theme. Kain Ramsay's author picture passed the importer's author check.
- **The two faults the last two briefs carried, checked before sending:**
  - **Straight quote marks:** none in any body heading. The only straight mark is in the Search and Citation Brief heading "2. Achology's contribution", which is not sent.
  - **Focus phrase in the body:** present in 7 of 8, in the opening paragraph each time. **Missing in CQ018-004-1**: "lack of self-awareness hold us back" is in its title, fields and description, never in its body. **In no subheading on all 8.** Both went as the records stand, since the brief asks for the import and the fix lands at source.
- **Note:** `import_quote_pages.py` has no `--with-seo` flag. It always sends the three Rank Math fields, and `--verify` read them back clean.

## 3. On the build site

| quote_id | Post | Status | New address | Old address redirects |
|---|---|---|---|---|
| CQ001-075-1 | 44067 | draft, created | /learn/mental-wellness/quotes/when-is-it-right-to-break-the-rules/ | 301 proved |
| CQ001-104-1 | 44068 | draft, created | /learn/mental-wellness/quotes/why-does-innovation-matter-more-than-imitation/ | 301 proved |
| CQ001-149-1 | 44069 | draft, created | /learn/mental-wellness/quotes/why-is-labelling-people-so-harmful/ | 301 proved |
| CQ018-004-1 | 36314 | publish, updated | /learn/mental-wellness/quotes/how-does-a-lack-of-self-awareness-hold-us-back/ | 301 proved |
| CQ018-045-1 | 36387 | publish, updated | /learn/mental-wellness/quotes/should-we-put-labels-on-people/ | 301 proved |
| CQ018-071-2 | 36423 | publish, updated | /learn/mental-wellness/quotes/why-do-we-define-ourselves-by-labels/ | 301 proved |
| CQ018-074-1 | 36430 | publish, updated | /learn/mental-wellness/quotes/why-is-it-easier-to-label-people-than-understand-them/ | 301 proved |
| CQ018-092-2 | 36463 | publish, updated | /learn/mental-wellness/quotes/can-one-label-ever-describe-a-whole-person/ | 301 proved |

- `--verify`: 8 of 8 clean against the records (title, excerpt, category, tags, quote fields, Rank Math fields).
- **Read back off the build site**, the five published pages: each answers 200, and the headline, search title and description match the record. Course cover 018 and Kain's picture show on all five.
- **The three drafts** cannot be read publicly. Their redirects already answer 301, but to a draft address, which answers 404 until they are published. Publishing them is Kain's word (pipeline stage 7).
- **The link up.** All eight named articles answer 200: understanding-your-core-values, the-role-of-freedom-in-personal-autonomy-and-decision-making, the-depths-of-empathy, the-importance-of-self-awareness, understanding-the-layers-of-identity, outgrowing-your-limiting-beliefs, listening-to-understand-not-to-reply, essential-character-traits-for-personal-growth-and-development. But, as in the influence batch, no page links to its article: the bodies carry no link to it and the quote template does not read `related_article_slugs`.

## 4. Inbound links: none placed

All 24 `inbound_from` sentences (3 per record) are new wording. None is already in its linking page's record. Under RULING S452 item 2, Code does not write a new sentence into a signed record. They wait on a Chat writing attachment: each linking record, the paragraph, the sentence word for word and the link words.

Every named linking page has a record (all field authority articles). The 19 linking pages: understanding-your-core-values, embracing-your-innermost-values, the-road-to-character-10-lessons-from-david-brooks-classic, social-conformity-insights-from-the-asch-conformity-experiment, the-role-of-freedom-in-personal-autonomy-and-decision-making, outgrowing-your-limiting-beliefs, understanding-the-layers-of-identity, listening-to-understand-not-to-reply, the-depths-of-empathy, the-importance-of-self-awareness, embracing-your-shadow-side, unlock-personal-empowerment-with-the-empowerment-dynamic, the-truth-about-active-listening, perceptions-illusion-insights-from-the-halo-effect-experiment, the-psychology-of-self-improvement, how-irresponsibility-leads-to-personal-disempowerment, helping-people-help-themselves, dynamics-of-leading-effective-diplomatic-discussions, essential-character-traits-for-personal-growth-and-development.

## 5. Rank Math scores against 86

Read one editor at a time, 12 seconds apart, nothing saved; the scoring session was revoked afterwards.

| Record | Post | Address | Focus phrase | Score | Against 86 | Failing tests |
|---|---|---|---|---|---|---|
| CQ018-092-2 | 36463 | /learn/mental-wellness/quotes/can-one-label-ever-describe-a-whole-person/ | one label | 86 | **pass** | linksHasInternal |
| CQ018-045-1 | 36387 | /learn/mental-wellness/quotes/should-we-put-labels-on-people/ | labels on people | 82 | **under** | keywordInSubheadings, linksHasInternal |
| CQ018-071-2 | 36423 | /learn/mental-wellness/quotes/why-do-we-define-ourselves-by-labels/ | define ourselves by labels | 82 | **under** | keywordInSubheadings, linksHasInternal |
| CQ018-074-1 | 36430 | /learn/mental-wellness/quotes/why-is-it-easier-to-label-people-than-understand-them/ | easier to label people | 82 | **under** | keywordInSubheadings, linksHasInternal |
| CQ001-075-1 | 44067 | /learn/mental-wellness/quotes/when-is-it-right-to-break-the-rules/ | right to break the rules | 80 | **under** | keywordInSubheadings, linksHasInternal |
| CQ001-104-1 | 44068 | /learn/mental-wellness/quotes/why-does-innovation-matter-more-than-imitation/ | innovation matter | 80 | **under** | keywordInSubheadings, linksHasInternal |
| CQ001-149-1 | 44069 | /learn/mental-wellness/quotes/why-is-labelling-people-so-harmful/ | labelling people so harmful | 80 | **under** | keywordInSubheadings, linksHasInternal |
| CQ018-004-1 | 36314 | /learn/mental-wellness/quotes/how-does-a-lack-of-self-awareness-hold-us-back/ | lack of self-awareness hold us back | 75 | **under** | keywordIn10Percent, keywordInContent, keywordInSubheadings, linksHasInternal |

**Why, measured on the records:**
- **No internal link, all 8.** Each body's one link goes to its course on achology.com (the live domain), which Rank Math counts as outside. The link up named in `related_article_slugs` would mend this on every page if it were in the body.
- **Phrase in no subheading, 7 of 8.** The phrase sits once in the opening paragraph and in no heading. CQ018-092-2 passes this test, which is why it reaches 86.
- **CQ018-004-1** also has the phrase nowhere in its body, so it fails the first tenth and the content tests too.

The pages are left as they are until the records are mended. Then they re-enter at import and are rescored. The new standard has lifted these from the 72 to 75 of the influence batch to 80 to 82; the link up in the body and the phrase in one heading would take each to 86 or more.

**The same is likely true of the next batch.** BRIEF__Import_The_12_Signed_Quote_Articles_Guiding_Mistakes_Forgiveness_And_Balance_S452 arrived while this ran. It's worth checking those twelve bodies for a phrase heading and an internal link before that import runs.

## 6. Not run, said plainly

- Google's Rich Results test was not run.
- No score line went into a DSRD 6 record.
- The quote cards were not re-baked.

OWED BACK: your record mends for the seven under 86 (the link up in the body, the phrase in one heading, and the phrase in the CQ018-004-1 body), and the 24 inbound sentences. Then the eight re-import and rescore.

*No em or en dashes in this file; checked before writing.*
