> **CODE DISPOSITION, S097: WAITS ON one file existing, a per-book-note earnings table in the Search Console exports folder.** Arrived mid-session and read in full at H6's block. Nothing in it cancels the work in hand: it is read-only, it commissions nothing, and it says so. **Two facts measured before this line was written, so the next session starts from a known state rather than rediscovering it.** Row 2's join has no field behind it: not one of the 114 records under `Content Records/book-note` carries `old_address`, so the old-site address has to come from the S087 LIST file and the live URL export instead. And the API route does not exist: `tools/url_inspection.py` holds the signed JWT machinery but calls `urlInspection` only and has no `searchAnalytics.query`, so row 3 is a build before it is a read. Both are small and neither needs anybody. First item of the next factory session.

# ASK: for each of the 65 published book notes, what does its old page already earn in Search Console?

**From:** Claude Chat, Session 334. **Date:** 3 September 2026. **For:** a factory session.
**Answers nothing; this is a read-only request.** Nothing is commissioned here and no writing, no import and no edit follows from it. The commission that depends on the answer is not written until Kain has read it.
**Board card:** Book Notes: the psychologist expansion.

---

## Why this is being asked

Your `REPORT__The_Sixty_Five_Book_Notes_Already_Had_Their_Words_S097.md` closed the question Chat thought it was asking. The 65 keywords exist, they are distinct, they are on the install, and the honest job is not writing 65 but reading 65 and replacing the ones that do not survive stage 0. That is right as far as it goes.

Kain and Chat then took it one step further at S334, and the ruling behind this ASK is his. **A keyword and a body are one thing on these pages, so no keyword can be replaced on its own.** Change `{book title} book summary` to a real question and the page now claims to answer something its own words do not answer: the keyword leaves the first paragraph, leaves the subheadings, leaves the density band, and the page fails its own score for a reason nobody introduced by writing badly. So every keyword we change drags a body pass behind it, 65 times.

That is too much work to spend on a guess, and it does not have to be a guess. **Most of these 65 replace a page that is already live on the old site and already earns.** Google can say, page by page, which questions those pages actually win today and in whose words. That is better evidence than any fresh demand harvest could produce for the same books, it costs nothing to read, and it doubles as the thing the redirect map needs at cutover: a page's real earning question is what its redirect has to protect.

So the order Kain ruled is: evidence first, then each keyword decided against what its own old page already earns, then a fresh stage 0 demand check only on the books with no old page behind them, and the body pass done in the same turn as any keyword that changes.

## What is being asked for

One table, one row per published book note, with as many of these as you can read without a new build:

1. **The book note's slug and its current focus keyword**, as they now stand on the install after tonight's push.
2. **The old-site address it replaces**, where one exists. Your S087 LIST file and the `old_address` field are the two sources already in hand; where a note replaces nothing, say so rather than leaving the cell blank, because "no old page" is itself the answer that routes that book to a fresh demand check.
3. **What that old address earns in Search Console**, over whatever window gives an honest read (twelve months is the usual, but take what the data supports and name the window you used): its clicks and impressions, and the queries it actually ranks for, with the top few by impressions and their positions.
4. **Whether the query Google reports and the keyword we have written are the same thing**, in your own reading, one of three: they agree, they disagree, or the page earns too little for the question to be answerable from data.

Row three is the one that matters. Rows one and two are the join.

## What is not being asked

Do not change a keyword, a body, a record or a page. Do not run a demand harvest: stage 0 belongs to Cowork under the pipeline and only on the books this table says have no evidence. Do not re-score anything. If the table shows something that looks like an obvious fix, name it in the report and leave it alone, which is what you did with the stray backslash on `chasing-the-scream` and it was the right call.

## What happens with the answer

Chat reads the table with Kain, and each of the 65 lands in one of three piles: the keyword stands and nothing is touched; the keyword changes and its body is rewritten to match in the same pass; or the book has no old page and goes to a normal stage 0 demand check before anything is drafted. Only then is a Cowork commission written, and it will be sized from the table rather than from the number 65.

---

OWED BACK: the table, in whatever form is cheapest for you to produce, with the Search Console window named. No deadline; it gates a commission that is not yet written.

*No em or en dashes in this file; checked before writing.*
