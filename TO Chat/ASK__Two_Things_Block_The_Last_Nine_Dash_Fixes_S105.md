# ASK: two things block the last nine dash fixes, and neither is mine to decide

**From:** Claude Code, Session 105. **Date:** Monday 7 September 2026. **Session type:** factory.
**Board card:** the 18 instructor articles.
**Commissioned by Kain in this sitting**, on the fault reported in `REPLY__Three_Jobs_Three_Cards_S105.md`: **"yes, fix both please"**, meaning the eleven live pages and the tool that caused them.

---

## What is done

**The cause is fixed and proved.** `import_instructor_articles.py` and `import_author_biographies.py` both turned a record's body-to-notes separator into a paragraph, and WordPress renders three hyphens as an em dash. Both now drop a thematic break instead. Proved in both directions on both scripts: the rule goes, output is otherwise byte-identical to the same body without it, hyphenated prose survives untouched, and with the fix disabled the leak returns, so the test can go red.

**Worth knowing why the fix that already existed did not reach them.** `content_gate.strip_file_footer` has stripped a closing rule since S104, on every return path. These two importers are **the only two that never call `extract_body`**: both read a CSV rather than the record. **So there is one rule with three implementations of it**, and this is the second time that has cost a live page. Naming it rather than fixing it in passing; it deserves its own job.

**Two of the eleven live pages are corrected**, through `article_body_update.py`, which writes `post_content` and never a status. `gerard-egan` and `kain-ramsay`, both read back clean, both confirmed off the install. **Nine still carry it.**

---

## Blocker 1: the instructor records write H4 headings, and the standard does not have an H4

`article_body_update.py` refuses eight of the nine with "body carries a heading deeper than H3, which the converter does not render". The refusal is real: every instructor-article record heads its body sections with `####`.

**Checked on the rendered live page rather than assumed:** those H4s render as **H2** on the published article, because `import_instructor_articles.py`'s own converter maps anything from H2 to H6 onto H2.

**DSRD 9 section 22.6, read from the canonical file this turn, defines two heading styles and no more:**

> H2, Como 24px/600, brand dark, margin-top 32px, margin-bottom 16px
> H3, Como 20px/600, brand dark, margin-top 24px, margin-bottom 12px

**There is no H4 in the standard.** So a record writing `####` is outside it, and the two tools disagree about what to do: one refuses, the other silently flattens. The pages happen to be right; the records are not.

**I have not touched the refusal.** Loosening a check on a tool that writes to live pages, so that my own work can pass, is the same move I declined on the publishing wall an hour ago, and my judgement is not neutral here.

**My recommendation, for you to rule:** the seventeen instructor-article records change their body headings from `####` to `##`, matching section 22.6 and every other content type. It changes no words and no rendered page, because the live pages already show H2. Once the records match the standard the refusal disappears on its own, and the nine pages can be corrected with nothing loosened anywhere. **Say the word and I will make that change to the records; it is structural rather than drafting, so I have not assumed it.**

---

## Withdrawn from this file: the I18 slug question, which I should not have asked

An earlier version of this session's reply asked which of two slugs was right for I18. **That question is answered by the record itself and I withdraw it.** Its `post_title`, `post_name` and `address` all read `persuade-someone-who-disagrees` and agree with each other. Only its FILENAME reads `understanding-comes-before-influencing`, and every one of the eighteen is like that: I01's file is named `why-people-seek-help` and its `post_name` is `why-do-people-seek-counselling`. A stale filename is the whole of decision 5, not a competing claim.

**So I18 is imported and verified, now that Kain has emptied the bin.** Post 35920, drafted, six H2s, image attached with its alt text. **All eighteen of I01 to I18 now exist.** It stays a draft: publishing it needs the instructor type's bar written into DSRD 6, which you hold, and Kain's per-article approval per the S309 re-conditioning.

**One thing this exposed, and it is the real half of decision 5.** The sheet the instructor importer reads by default still carries the pre-S309 slugs, so running it plainly would create eighteen duplicates again. It is not the importer's memory, it is the CSV. I built a one-row sheet from I18's record with `build_upload_csv.py` and imported from that. **The default sheet should be regenerated from the records or deleted; while it exists it is a loaded gun.**

## Blocker 2: the I10 duplicate record, which is now costing something real

The ninth page, `why-giving-advice-does-not-work`, is refused for a different reason: **two records claim that `post_name`.**

- `I10__why-good-advice-rarely-inspires-change.md`, 2,318 words
- `I10__why-giving-advice-does-not-work__EXEMPLAR_S329.md`, 3,550 words

The tool refuses rather than guess which one is the article, and it is right to. **This is the suffixed-copy rule earning its keep:** one canonical file, one canonical name, git for the history. Flagged in this session's earlier reply as a filing untidiness; it has since blocked a live fix, so it is no longer untidiness.

**Which of the two is the record is yours, because they differ by 1,232 words and that is a content question, not a filing one.** I have changed neither and deleted neither.

---

## What happens on your two answers

Both answered, the nine pages take one command and one read-back, and chapter 1 closes its machine half on every one of them.

---

OWED BACK: your ruling on the instructor records' heading level, and which of the two I10 files is the record.

*No em or en dashes in this file; checked before writing.*
