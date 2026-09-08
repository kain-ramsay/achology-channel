# DONE: the fifteen help-answer keyword placements are drafted, tested, and gate-clean

**From:** Claude Cowork. **Date:** 8 September 2026.
**Runs:** `ADDENDUM__The_Keyword_Now_Moves_To_Fit_The_Address_S350.md`, Job 2.
**Deliverable:** `KEYWORD_PLACEMENTS__Fifteen_Help_Answers_S351.csv`, sibling to this file.

---

All fifteen named posts (231, 227, 245, 253, 256, 261, 273, 274, 277, 346, 352, 353, 395, 412, 10036) now pass all four placement tests: keyword verbatim in a subheading, keyword verbatim in the opening tenth of the body, keyword verbatim again elsewhere in the body, keyword in the meta description at 155 characters or under. Post 375 was left alone, as instructed.

Each post's already-assigned focus keyword is unchanged. Nothing else about any answer changed: no fact, no claim, no link, no other heading, no other sentence. Every edit is two body-text swaps (the opening restatement sentence, and one existing heading reworded to carry the keyword) plus a new meta description. Word counts moved by no more than ten words either way, all of it from the keyword now sitting inside sentences that previously paraphrased around it.

**How each was verified, not just drafted.** Every old sentence and heading was matched against the live page's actual current text with an exact, single-occurrence check before being replaced, both in the plain body text and in the live rendered HTML pulled fresh from the WordPress REST API today, so the CSV's `new_body_html` is the real current markup with only the named spans swapped, not a reconstruction from a stale file. The four tests then ran against the result using the same pass logic throughout: total keyword occurrences, position in the first tenth, and meta length are all counted mechanically, not eyeballed. The CSV was written, then re-read from disk and re-checked, to catch anything a CSV escaping quirk might have broken.

**Zero placements left out.** Every one of the fifteen took its keyword naturally; none needed forcing, so there is nothing to list under the brief's "leave it and name it" clause this time.

**One thing worth knowing.** Six of the fifteen (227, 231, 245, 253, 352, 353) needed their first meta description draft trimmed, once or twice, to land at or under 155 characters. The final versions in the CSV are the ones that passed. Post 346's opening sentence keeps its existing internal link to the membership page; post 10036 (the only keyword with an apostrophe) matches the surrounding page's own curly-quote convention in the HTML column, and uses a plain apostrophe in the meta description and plain-text column, matching how meta descriptions and body text are already stored on this site.

**What the CSV carries.** One row per post: id, slug, title, the unchanged keyword, the old and new opening sentence, the old and new heading, the new meta description with its length, old and new word counts, all four test verdicts, and both the full new body text and full new body HTML, ready to apply against the live post by id. This is a correction to live pages, the same shape as the S338 precedent, not a fresh import.

OWED BACK: nothing further needed from you on this batch. It is ready for whoever applies corrections to live help pages to action and, per the standing practice, for a real Rank Math re-score after it lands, since Cowork's checks are thorough but not the executable gate.

*No em or en dashes in this file; checked before writing.*
