# REPORT: the S357 paragraph gate is patched, and the four sets are re-measured

**Filed by Claude Code, Session 118. Date:** 15 September 2026.
**Answers:** `BRIEF__Patch_The_Paragraph_Check_To_The_S357_Ruling_Then_Re_Run_The_77_Records_S361.md`.

---

## 1. The patch

`content_gate.py`'s paragraph-rhythm check now reads all four `shared` keys in `content_gate_standards.json` as written, nothing hardcoded: `paragraph_sentences [3, 4]`, `paragraph_floor_words 50`, `single_sentence_paragraph "once_per_section"`, `short_paragraph_allowance_per_section 1`. A paragraph passes on 3 to 4 sentences OR 50 or more words; one paragraph under both floors is allowed per section, the unheaded opening counted as its own section exactly as the ruling says; a second short paragraph in the same section fails; a paragraph over 4 sentences still fails outright regardless of word count. `help-answer` is excluded and keeps only its own S356 cap (`paragraph_words_max` / `paragraph_sentences_max`). The pre-S357 literal `"allowed"` still works exactly as before, since the acceptance file's own BASE standard depends on it.

Three acceptance cases added, one per branch the brief named: the word-floor pass, the once-per-section allowance, the second short paragraph in a section failing. **106 of 106 cases pass**, the 103 pre-existing ones unmoved.

Committed and pushed: `ed16460`.

## 2. The re-measure, four sets

**I04, I14, I18: 3 of 3 now pass whole.** Confirmed false failures of the same bug, exactly as the brief expected. Nothing in these three bodies needs rewriting.

**Unpublished book notes: 9 of 51 now pass whole.** One correction to the brief's own count: measuring fresh against the install tonight (99 live `book_note` posts, per `wp post list`), 51 records have no matching post, not 50. Of the 42 still failing:

| failing on | records |
|---|---|
| paragraph rhythm (still genuinely short, beyond the one-per-section allowance) | 30 |
| machine-written tells (the word "plainly") | 28 |
| outcome-or-problem tag count | 9 |
| reading ease (Flesch) | 4 |
| total body words | 4 |
| keyword verbatim in first 10% of body | 1 |
| external link to the source | 1 |

(Most records fail on more than one line, so these do not sum to 42.)

**24 DSM records: 0 of 24 pass. All 24 fail, all on paragraph rhythm alone**, and this is not the bug: several carry 20 to 30 short paragraphs against a one-per-section allowance, a genuinely staccato style the S357 floor is built to catch. None fail on any other line.

## 3. Routing, and what is still owed before "publish" happens

**The 9 passing book notes are not yet imported.** `book_note_import.py --plan` on the nine found a pre-existing, unrelated gap: the importer carries 21 of a record's fields nowhere, five of them the S329 fields (`search_intent`, `reviewed_by`, `update_cadence`, `query_variants`, `schema_type`) that DSRD 2 and this gate both treat as required. This is not new and not caused by tonight's patch; it looks old and unnoticed. Importing the nine now would silently drop those five fields from the published pages. Flagging rather than deciding: is dropping them acceptable for this batch (matching what every prior book-note import has apparently done), or does the importer need those five columns before anything else goes through it?

**I04, I14, I18 still need their "finish pass" pushed** through proper clearance (H9 blocks a raw `wp post update`); I have not yet identified and run the correct route for these three this session.

**The 42 still-failing book notes and all 24 DSM records** are ready for the same paragraph-split job Cowork is already doing for I04/I14/I18, now that the counts above are real rather than gate noise.

---

OWED BACK: your word on the 21-field question, so the nine can import; and confirmation of the route for pushing I04/I14/I18's finish pass.
