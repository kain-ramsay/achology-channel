# BRIEF: correct the book note keyword on 63 records, and backfill the demand evidence we already hold

**From:** Claude Chat, Session 349. **Date:** Tuesday 8 September 2026, 12:05.
**Harness:** the Cowork Production Harness at the root of the Content Production Factory folder. Read it first, then The Shared Rules, then this file.
**Board cards:** the 65 published book notes; book notes, redraft the 17.
**Runs before:** `BRIEF__The_Second_Read_On_The_Seventeen_Redrafted_Book_Notes_S349.md`, filed earlier today. Do this first; the second read is worth more once the records are clean.

---

## What Code's gate run found, and why it is not what anyone expected

He ran `content_gate.py` across **all 149 book note records**, not just the seventeen Chat redrafted. **86 pass, 63 fail.** The seventeen are seventeen of the sixty-three, and every one of them fails the identical eight lines.

**Not one failure is about the writing.** No record fails on words, paragraphs, reading ease, dashes or vocabulary. Every failing line is a field: a missing `demand_evidence`, and five keyword placement checks.

## Job 1: the keyword takes the book's title

**Ruled by Chat at S349, and it is the standard being applied rather than a new rule.** DSRD 6 section 5 item 11's by-type list already says the book note's focus keyword is **the book's title**. The records carry `{book} book summary`, which sits in neither the address, nor the SEO title, nor the cover alt, nor the opening, which is why five checks fail on each one.

**On every failing record, set:**

- `prod_rm_focus_keyword` (or `rm_focus_keyword` where the record uses that name) to **the book's title exactly as `post_title` carries it**, including its apostrophe character. `Born for Love`. `Why Zebras Don't Get Ulcers` with the curly apostrophe the title uses, which also closes the alt-text point Code named at S103.
- **Nothing else.** Not the title, not the address, not the body, not the excerpt, not the cover. The pages are live and Kain ruled their title pattern at S102.

**Where the title alone is genuinely ambiguous** (two books sharing a title, or a one-word title like `Originals` that means something else), name it in the report rather than inventing a longer phrase. Code rebuilds the register afterwards and any clash surfaces there.

## Job 2: backfill the demand evidence from the file we already hold

`demand_evidence` is absent on all sixty-three. **The evidence exists and does not need re-researching:** your stage 0 run covered all 67 published notes and its results CSV is in `Content Records/book-note`, with the confirmed keyword and its evidence per row.

**Copy it in, row by row, into each record's `demand_evidence` field**, in the form the other content types use. **Where the CSV's confirmed keyword and this brief's rule disagree** (it will, because the CSV confirmed the `book summary` form), the evidence line still stands as the demand check that was run: record it as evidence for the book's demand, and note in the row that the keyword form was corrected at S349 to the standard's own by-type rule.

**Where a record is not in the CSV** (the unpublished ones among the 149), run the stage 0 check on it as normal.

## Job 3: one real record fault

`have-a-little-faith` carries the tag `find-purpose-direction`. **DSRD 1 section 5.6's register does not hold that slug.** Replace it with the nearest registered tag the record's own content earns, read from section 5.6 this session, and say in the report which you chose and why.

## Four records also carry a length fault, and these are copy

Correct them in the same pass, they are small:

- `the-origins-of-intelligence-in-children`: SEO title 66 characters, maximum 60.
- `yes-50-scientifically-proven-ways-to-be-persuasive`: SEO title 63 characters.
- `meditations-for-mortals`: description 159 characters, maximum 155.
- `multiple-intelligences-new-horizons`: description 172 characters.

## Order, because two cards are waiting

**The seventeen first** (the slugs are in the second-read brief), so that card can close. **Then the other forty-six.** Report after the seventeen rather than holding everything to the end.

**Re-run the gate on each record as you finish it** and put the passing printout in. A record leaves this run with a PASS printout or it is named in the report with its failing line.

---

OWED BACK: the seventeen, gate-clean, with their printouts, then the forty-six. Name any title that is ambiguous as a keyword.

*No em or en dashes in this file; checked before writing.*
