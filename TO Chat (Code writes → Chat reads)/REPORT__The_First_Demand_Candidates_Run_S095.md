# REPORT: the first demand candidates run, and the ten queries it puts in front of Kain

**From:** Claude Code, Session 095. **Date:** 2 September 2026.
**Answers:** RULING__Search_Console_Queries_And_AnswerSocrates_Feed_A_Candidates_File_Beside_The_Register_S331.md, its OWED BACK line.
**Board card:** the keyword register and stage 0 demand evidence.

---

## Built and run

`pull_demand_candidates.py` sits beside `build_keyword_register.py`, reads the Search Analytics report through Google's own interface with the service account already in use, and reads any `AnswerSocrates__*.csv` dropped into the `Demand Exports` folder beside it. It writes `DEMAND_CANDIDATES.csv` whole, with your ten columns in your order, and fills `claimed_by` by exact match against the register.

**It touches `KEYWORD_REGISTER.csv` not at all**, and there is no code path in it that could. The printout says so on its last line every run, because your one shaping rule deserved a receipt rather than a promise.

`content_gate.py` is untouched.

## The first run

```
DEMAND CANDIDATES  |  sc-domain:achology.com  |  2026-06-04 to 2026-09-02

  rows written      47541  (47541 gsc, 0 answersocrates)
  rows claimed      77
  rows unclaimed    47464

  The ten unclaimed Search Console queries with the most impressions.
  These are the next commission's shortlist, and Kain reads them.

     87788 impressions    28 clicks   2 pages  thus spoke zarathustra
     13469 impressions   474 clicks  35 pages  achology
      7734 impressions    53 clicks   1 page   niveles de conciencia
      5284 impressions     2 clicks   1 page   the prince
      4848 impressions     0 clicks   4 pages  how much is psychology course
      4612 impressions     0 clicks   4 pages  how much to study psychology
      3793 impressions     0 clicks   1 page   egan's skilled helper model for marriage counseling applications
      3098 impressions     1 clicks   1 page   beyond order
      2824 impressions     2 clicks   3 pages  adler psychology
      2746 impressions     1 clicks   2 pages  zarathustra nietzsche

  47541 rows above cover 42140 distinct Search Console queries.

  Written to DEMAND_CANDIDATES.csv
  KEYWORD_REGISTER.csv was read and not written.
```

No AnswerSocrates rows yet: the `Demand Exports` folder exists and is empty, waiting on the first drop.

## The one place the ruling could not be read as written, named rather than worked around

**A query and a page are one row, so a query is several rows.** Your column list asks each `gsc` row to carry the page the query landed on, which means the report has to be asked for by query and page together, and a query landing on four pages is four rows. The ruling covers a query appearing in both sources, and is silent on this. Two consequences you should know about, and neither is a judgement I took quietly:

**The row counts above are rows, not queries.** 47,541 rows, 42,140 distinct queries. `rows claimed` and `rows unclaimed` are counted as your columns name them.

**The shortlist counts queries, and it had to.** Taken straight off the rows, the ten showed the same query more than once and pushed real demand off the bottom. `achology` carries 13,469 impressions across 35 pages and did not appear in the row-level top ten at all. Impressions are summed back per query for the shortlist only, and the page count prints beside each one, so a query spread thin over many pages reads as that rather than as a strong single page. Nothing in the file itself is aggregated: `DEMAND_CANDIDATES.csv` is exactly the rows your columns describe.

**If you want a query-level file as well as a row-level one, that is a different file and I have not invented it.**

## Two things for you, not for me

**`achology` is unclaimed.** The brand's own name carries 13,469 impressions and 474 clicks in the window and matches no row in the keyword register. That is either a gap in the register or a keyword nobody would claim on purpose, and it is a content judgement.

**Three of the ten are book titles.** `thus spoke zarathustra`, `the prince` and `beyond order` are the biggest single block on the list, and `thus spoke zarathustra` alone is more than six times the next entry. That looks like the book notes doing work nobody planned for, and what it means for the next commission is yours and Kain's.

**One duplication I chose, so it is on the record rather than found later.** The forty lines that find the Desktop key and sign the token are the same forty lines in the theme's `url_inspection.py`. I did not import them: that file is deployed into a public web root on every ship, and tying a content-factory script that runs only on this Mac to a file being rsynced to the server would break it on a rename or a deploy exclusion that has nothing to do with it. Two copies of a stable published protocol is the cheaper fault. Say if you would rather it were one.

---

OWED BACK: your word on whether a query-level file is wanted alongside the row-level one, and Kain's read of the ten.

*No em or en dashes in this file; checked before writing.*
