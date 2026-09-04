# COMMISSION: redo stage 0 properly on all 65 Salvage articles, then run it right on every batch after this one

**From:** Claude Chat, Session 339. **Date:** 4 September 2026.
**Authority:** Kain Ramsay, ruled in session.
**Under:** The Publish Ready Pipeline, Version 7 (this session), rule 6, and the `rank-math-90` skill, Part A step 1.

---

## What happened

All 65 field-authority-article Salvage records in `Content Records/field-authority-article/` carry real, honest demand evidence: `demand_evidence` and `query_variants` are filled in on every one, from a genuine live check at drafting. That much was done properly.

What did not happen: the title itself was not set to the actual proven question. 63 of the 65 read as a topic label ("10 Ethically Dubious Experiments in Psychology") rather than the question the record's own evidence points to ("What Are the Most Unethical Experiments in Psychology?"). Rule 6 said "a question people are actually asking" and that was read loosely enough to mean "matches the topic," which is not what it means. Rule 6 is now corrected in the pipeline document, with an example built into the rule itself so it cannot be read loosely again.

## What is commissioned

**Part 1. Redo stage 0 on all 65 existing records**, in `Content Records/field-authority-article/`, the Salvage batch (rows 1 to 70 plus the S338 wave). For each one:

1. Run the real stage 0 check again, live: autocomplete on the seed phrase, the People Also Ask questions on the results page, one AI assistant asked the seed question. Do not reuse the old evidence unread; confirm it or correct it.
2. Where the evidence genuinely supports a question, set `post_title` to that question, word for word, not a paraphrase. Update `rm_seo_title` to the same question or a faithful shortened form that still carries the keyword in its first 50 characters and stays under 60 total. Update `rm_seo_description`, the address slug, and any query_variants that need to change to match.
3. **Where the live evidence does not actually support a question** for that topic, a real list or topic search rather than a question, name that plainly in the record's notes rather than forcing a question onto it. That is a genuine finding, not a shortcut, and it comes back to Chat named as one, for Kain's ruling, rather than decided in the batch.
4. Re-run `content_gate.py` on every touched record and write the printout in, per the standing rule.
5. Write one batch report to FROM Cowork: every record, its old title, its new title (or the reason it stays a topic label), and the live evidence for each, so Chat's stage 3 spot check has something real to check against.

**Part 2. Apply the corrected rule 6 to every Salvage record still to be drafted.** Nothing changes about the recipe, the voice, or the six-section shape. Stage 0 for every remaining row proves the actual question live, before drafting, and the title set is that question, not a label built to match it.

## What this does not touch

The bodies, the sourcing, the voice, the six-section structure, the destination course routing: none of that is reopened. This is a title-and-metadata correction, run through the same stage 0 the pipeline already specifies.

---

OWED BACK: one batch report per part, in FROM Cowork, in the shape stage 0 and this commission both name.

*No em or en dashes in this file; checked before writing.*
