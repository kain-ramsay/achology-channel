**For Chat. What this needs from you:** three record mends: two book notes with the old fifth heading and one hub guide with no outside link (section 2). Also one quote article, Q07042, at 85 (section 4). Factory side session of Code S203, 2 November 2026.

# DONE: the 15 pages, resisting change links, two quote articles and three book notes (Code, factory, 2 November 2026)

Answers BRIEF__Update_15_Pages_Resisting_Change_Links_Two_Quote_Articles_Three_Book_Notes_S451.

## 1. Counts

- **12 of 15 updated in place and read back**, each body character for character against its record. All stay published.
  - Seven of the ten linking records went with the 87 instructor brief that ran first, sent from the current records, as this brief asks. Those seven are change-is-the-only-constant, I17 (change-vs-transition), personal-growth-requires-discomfort (why-does-personal-growth-feel-so-painful), step-outside-your-comfort-zone (why-is-stepping-out-of-your-comfort-zone-so-hard), growing-or-standing-still (growing-as-a-person), fixed-or-growth-mindset and all-progression-is-impossible-without-change.
  - The other five were sent body only: the-stages-of-change-model, the-ultimate-life-coaching-handbook, Q07016 and Q07042 (by quote_id, posts 36267 and 38503) and yes-50-scientifically-proven-ways-to-be-persuasive.
- **3 held** (section 2).
- **The 23 inbound links:** all 23 are in the ten records, exactly as the brief's table lists them, counted record by record. 21 are on the build site and read back. The other 2 sit in the held hub guide.
- **Scores:** 2 of 3 at 86 or over (section 4). Two of the five pages the brief asks to score are held, so they are not scored.
- free-will-by-sam-harris (its address and redirect from the S190 report) was not part of this run.

## 2. The three import checks, and the three held

- **Check 1, fields complete and signed.** All 15 carry the 2 November S451 signature, and none carries a form of hold. Quote pages were checked by `import_quote_pages.py`, 2 of 2 pass. The generic checker asks a quote page for a featured picture, which quote pages do not carry.
- **Check 2, body shape.** `body_guard.py --signed` is clean. Two book notes fail `stage5_import_checks.py`, and are **held**:
  - atomic-habits-clear and civilization-and-its-discontents still carry the fifth heading "What Might Your Next Learning Steps Be?".
  - DSRD 9 section 32.7 replaced it on 22 October with "A Question That Deserves an Honest Answer" (Kain, Session 440), and the gate's book note standard reads only the new heading.
  - Only three book note records in The Stock still carry the old one.
  - The two records need that heading changed, and then a fresh signature.
- **Check 3, links.**
  - Every site address resolves. One is a page to come: the coaching handbook links to Seven Beliefs part 7 (change-your-life-from-the-inside-out), which is signed and not on the build site yet.
  - Every outside link resolves, apart from publishers that refuse scripts.
  - **human-nature-and-behaviour (hub guide) is held:** `article_body_update.py` refuses it for carrying no outside link (DSRD 6 section 5 item 11 move 6), as factory S205 found for seven other hub guides.

## 3. Read back

The 12 bodies match their records. The fields this brief does not send were not compared. On the book notes those are the search fields, which are stored under their prod_ names. On the quote pages it is the picture, which is the baked card.

## 4. Rank Math scores against 86

Read one editor at a time, 12 seconds apart, nothing saved, in turns agreed with the other factory sessions.

| Record | Post | Address | Focus phrase | Score | Against 86 |
|---|---|---|---|---|---|
| Q07016__ready-to-change | 36267 | /learn/helping-people/quotes/why-we-resist-change-even-when-its-positive/ | resist change even when it's positive | 88 | pass |
| yes-50-scientifically-proven-ways-to-be-persuasive | 36218 | /learn/psychology/book-notes/yes-50-scientifically-proven-ways-to-be-persuasive/ | Yes! 50 Scientifically Proven Ways to Be Persuasive | 88 | pass |
| Q07042__why-change-never-happens-overnight | 38503 | /learn/helping-people/quotes/why-is-change-so-hard/ | why is change so hard | 85 | **under** |

**Q07042, 85:**
- Measured on the record, the phrase "why is change so hard" sits in no section between the first and last heading (keywordInSubheadings).
- It does sit in the first tenth, the content, the title, the description and the address.
- The 113 page brief notes that Rank Math's subheading test matches the phrase anywhere between the first section heading and the last. One sentence carrying the phrase in the Book, Look or Took would lift it, as it did the 92 round one pages.

Not scored: atomic-habits-clear and civilization-and-its-discontents, which are held.

## 5. Not run, said plainly

Google's Rich Results test was not run. No score line went into a DSRD 6 record.

OWED BACK: the two book note headings, the hub guide's outside link and the Q07042 sentence, each in its record and signed. Then Code sends the four and scores them.

*No em or en dashes in this file; checked before writing.*
