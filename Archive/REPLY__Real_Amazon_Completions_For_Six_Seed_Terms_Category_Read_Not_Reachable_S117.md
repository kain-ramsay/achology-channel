# REPLY: real Amazon completions for the six seed terms; the category read did not go through

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** `BRIEF__Get_Real_Amazon_Search_Data_For_TULCH_Keywords_And_Categories_S359.md`, in FROM Chat.
**Route used:** not the two GitHub repos named in the brief (this environment cannot build the `cryptography`/native-extension packages several Python routes need, the same wall met elsewhere this session). Amazon's own live completion endpoint, `completion.amazon.com`, fetched directly and read for real, current results, checked against the page each time rather than guessed.

---

## 1. The completions, in the order Amazon returned them

**"life coach"**: life coaching books, life coach, life coaching, life coaching supplies, life coach gifts, life coach books, life coach shirt, life coaching workbook, life coach planner, life coaching for dummies.

**"life coaching book"**: life coaching books, life coaching book, life coaching books for clients, life coaching books for coaches.

**"how to become a life coach"**: how to become a life coach, how to become a life coach book.

**"self help coaching"**, **"personal development coach"**, **"coaching book for beginners"**: all three returned an empty suggestions array. Checked, not a fetch failure: the same route that returned real completions for the first three returned a genuinely empty list for these, which is itself the finding rather than a gap in the read.

## 2. What this says, read plainly rather than built into keywords

"Life coach" and "life coaching book" both carry real demand for "workbook," "planner," and "for dummies" as companion terms, none of which repeat the title, subtitle or category per the redundancy rule you already hold. "Books for clients" and "books for coaches" split the audience in a way worth naming to Kain. The three empty seeds suggest those exact phrasings are not what buyers actually type; the working phrasings above may be the more honest keyword material.

## 3. The category-competitiveness half: not reachable

Tried Amazon's public best-seller listing for the closest category; refused with a 503 (bot detection on that surface, unlike the lighter completion endpoint). No other free route was found this session. Named as not done rather than guessed at.

---

OWED BACK: nothing further from Code. Building the final seven keywords against the redundancy rule is Chat's, from the real data above.

*No em or en dashes in this file; checked before writing.*
