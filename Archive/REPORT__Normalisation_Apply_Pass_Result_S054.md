# REPORT: the normalisation apply pass has run

**From:** Claude Code, Session 054. **Date:** 2026-08-11.
**Answers:** `RULING__Normalisation_Apply_Pass_Authorised_S263.md` section 4, which names three things to report back.
**Status:** complete. Applied to the live WordPress data, verified by query, and fully reversible.

## 1. The count actually changed: 897

Exactly the ruled number, and it was verified against the data rather than against the script's own log. The query compares each review's live text to its untouched copy:

| | Rows |
|---|---|
| `review_text` | 4,517 |
| `review_text_raw`, the untouched copy | 4,517 |
| Where the two now differ | **897** |
| Where the two are identical | 3,620 |

3,620 is the 3,038 that were already correct plus the 582 flagged, which is the arithmetic the dry run predicted.

## 2. Reviews the pass skipped that the dry run predicted it would change: none

Zero. The apply script does not restate the rules; it **imports `normalise_dryrun.py` and calls its own `flags()` and `normalise()` functions**, so there is one definition of "the corrected rules" and not two that could drift. A flagged review cannot reach an UPDATE by construction rather than by a second copy of the flag list. The script reported 582 flagged and skipped, and 897 statements written, before a single row was touched.

## 3. Both reversal mechanisms were in place before the first write

Confirmed, and the run was sequenced so it could not have been otherwise: the script aborts on any error before reaching the apply step.

1. **`review_text_raw`, 4,517 rows**, one per review, holding the untouched text on the same post. Written and counted before the apply step ran. This is the durable reversal: restoring the whole archive, or a single review, is one copy back.
2. **A full `qbk_postmeta` dump**, 7,800,283 bytes, at `/tmp/qbk_postmeta_before_normalisation_S054.sql` on the server. Belt and braces beneath the raw copy.

**One caution worth recording rather than leaving implied.** The dump sits in `/tmp` and will not survive indefinitely. The reversal that matters is `review_text_raw` in the database, which survives everything and is what a restore would actually use. If Chat wants the dump kept somewhere durable, say so and it moves.

## 4. The bounds, each confirmed

- **Corrected rules only.** The pass ran against the rules that produce 897, with the emoticon, bracket and sign-off cases flagged. The 1,035 version was never on the server.
- **WordPress only.** `qbk_postmeta`, `review_text`, the `review` post type. The Notion bank was not touched and no export of it was made.
- **Reversal before the first write.** Section 3.
- **The 582 flagged were not revisited**, individually or in groups.

## 5. Verified on the page, not only in the database

The Reviews page renders after the change: 366,558 bytes, no fatal, the first batch of 50 cards present. The dynamic cache was purged after the run. One spot check on the record Kain saw in the samples, post 29044: live text now opens "Very innovative course", the raw copy still opens "very innovative course".

## 6. What is not done, and is not mine

The paragraph spacing. It is carried to Kain's Safari sitting, per section 3 of the ruling, and nothing about it has been built or changed. The 622 reviews carrying newlines still render as unbroken blocks, exactly as they did before this pass.

*No em or en dashes in this file; checked before writing.*
