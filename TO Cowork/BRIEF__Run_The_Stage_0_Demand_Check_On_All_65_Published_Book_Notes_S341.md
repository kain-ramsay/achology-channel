# BRIEF: run the stage 0 demand check on all 65 published book notes, and let each title and keyword follow what the check finds

**From:** Claude Chat, Session 341. **Date:** 5 September 2026.
**Authority:** Kain, in Chat this session. His words: "Yes to that! This is a great proposal." The proposal: retire the fixed book note title formula, run the stage 0 demand check on all 65 published notes, decide each title and keyword by what the check finds, rewrite a body only where its check fails.
**Run under:** the Cowork Production Harness (Version 16); the rank-math-90 skill, Part A, steps 1 to 3, which is the method and is not restated here; Rule 5 (never open the master file); Rule 7 (your outbound tray is FROM Cowork).
**Input:** `EXPORT__The_65_Published_Book_Notes_For_The_Stage_0_Demand_Check_S102.csv`, beside this brief. Sixty five rows read off the install by Code at his S102: slug, the focus keyword the page carries today, book title, book author. Every row's `old_address` reads "no old page", which is why every row takes a fresh check rather than a Search Console read.
**Output folder:** `Content Records/book-note/` in the Content Production Factory folder, one new file named below, and FROM Cowork for the pointer. Nothing else is written anywhere.

---

## 1. Why this run exists

The 65 published book notes were drafted at S086, before stage 0 existed. They carry the bare book title as H1 and, on 62 of 65, a focus keyword of the shape `{book title} book summary`, a pattern nobody proved anyone searches. DSRD 9 section 32.8 wanted a fixed formula instead (`Understanding {Book Title}: Key Ideas`); Kain retired that formula this session, because a title fixed in advance cannot be a question people actually ask, and standing rule 14 says a piece exists only against evidenced demand.

Code checked whether any of the 65 replaces a page on the old site, which would have given Search Console evidence to read instead. None does. So all 65 take the same route any new piece takes: prove the question, claim the keyword, set the three fields.

**These are live pages with no record on disk.** That changes two things below and nothing else: you write your results into one correction table rather than into 65 records, and slugs do not move.

## 2. The check, per row

For each of the 65 rows, run rank-math-90 Part A step 1 exactly as written: the seed phrase is the book title with the author where the title is a common phrase; read the autocomplete, read the People Also Ask questions, ask one AI assistant how it frames the question. Then decide:

- **The title:** the question real people ask about this book, in their wording, honest and without gimmick. Where the evidence shows people search the bare title with "summary" or "book summary", the existing title and keyword stand, and you record the evidence that proves them. A keyword that survives its check is a result, not a non-result.
- **The focus keyword:** the short phrase inside the question, never the whole question (rank-math-90 step 3, corrected S337). Claim it in `KEYWORD_REGISTER.csv` beside the gate (step 2): where the phrase is already claimed by another row, choose the next best evidenced phrase.
- **The SEO title and description:** to step 3's bounds (keyword inside the first 50 characters, title under 60; keyword inside the first 120 characters, description under 155, reading as a plain answer).
- **The evidence line:** one line naming the three sources checked and what each showed, with the pastes kept in your run notes, exactly as `demand_evidence` is written on every record.

**Slugs do not change.** These are 65 live addresses, and a renamed slug is a redirect. Where the evidenced keyword is one the existing slug already carries, well and good. Where the evidence points to a phrase the slug does not carry, choose the keyword the evidence supports anyway and mark the row `slug does not carry keyword`. Chat rules on those rows; you do not rename.

**Bodies are not touched in this run.** Where a row's keyword changes, the body will need the keyword laced through it (rank-math-90 step 4), and that is a second, smaller run on only the rows that changed, commissioned from your table. Mark each row `keyword unchanged` or `keyword changed, body pass owed` so the second run can be sized without re-deriving anything.

## 3. The table, in the shape Code asked for at S101

One file, `CORRECTION__65_Book_Notes_Stage_0_Results_S341.csv`, in `Content Records/book-note/`. Its head, as a first commented line or a companion `.md` of the same name, states in one sentence which population it covers: the 65 book notes published on the install as listed in Code's S102 export, all of them, none skipped. Then one row per note, one column one meaning:

`book_note_slug, current_focus_keyword, current_title, demand_evidence, new_title, new_focus_keyword, new_seo_title, new_seo_description, keyword_state, slug_state`

where `keyword_state` is `unchanged` or `changed, body pass owed`, and `slug_state` is `carries keyword` or `does not carry keyword`. Code's export carries no post ID, so the slug is the key; Code resolves slug to ID when he applies the table, as he did for the 220 help rows.

Then one file into FROM Cowork: `DONE__65_Book_Notes_Stage_0_S341.md`, naming the table and three counts: rows checked, keywords unchanged, keywords changed.

## 4. Two things this run is not

It is not a rewrite of any body, and it is not a judgement of the notes' quality; the 17 that failed real review are a separate card and a separate brief. Where a check cannot be completed for a row (the web search allowance runs out, the book is too obscure for any source to show demand), leave the row's new fields empty, write what happened in `demand_evidence`, and carry on. Rows left empty are reported as empty, never quietly dropped.

---

OWED BACK: the table in its folder and the DONE file in FROM Cowork. Chat reads the table, rules the `does not carry keyword` rows with Kain, sizes the body pass from the `changed` rows, and hands the table to Code to apply on the install.

*No em or en dashes in this file; checked before writing.*
