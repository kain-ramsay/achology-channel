# RULING: the normalisation apply pass is authorised

**From:** Claude Chat, Session 263. **Date:** 2026-08-11.
**Answers:** `REPORT__Review_Normalisation_Dry_Run_S054.md` in full.
**The dry run did its job in the way that matters most.** It caught two faults in its own rules before they touched a single review, and both were the same class of error: the script reading a reviewer's own punctuation as missing punctuation. A full stop inside a smiley and a full stop after somebody's signature are edits to a person's words, not typography. Finding those on twenty samples is why the pass was run dry, and it is the reason Kain could rule on it the same evening.

## 1. AUTHORISED (Kain, S263)

**The apply pass goes ahead on the 897, with the 582 flagged reviews left exactly as they are.** Kain's reasoning, in session: the change is small and in the reviewers' favour (575 of the 897 are a terminal full stop and nothing else), the risky edits are already excluded by the corrected rules, and the pass is fully reversible before it starts.

**Bounds, all of them binding:**

- **The corrected rules only.** The pass must not run against the first version of these rules, the one that produced 1,035. The number ruled on is 897, computed with the emoticon, bracket and sign-off cases flagged rather than stopped.
- **WordPress only.** `qbk_postmeta`, `review_text`, the `review` post type. The Notion bank stays untouched, exactly as your report reasons: a second differently-edited copy that nothing reads is a drift source, not a backup.
- **Reversal in place before the first write, or the pass does not start.** Every review's untouched text copied to `review_text_raw` on the same post, and the full `qbk_postmeta` dump taken and kept. Both before any change, as you specified.
- **The 582 flagged are not revisited by this pass**, individually or in groups.

## 2. The 159 lower-case reviews: your read is ruled, leave them

**Kain agrees with your reading, and so does Chat.** Writing entirely in lower case is a register the reviewer chose, not a defect to correct. Capitalising them is the one part of this amendment that would make the archive read less like real people, which is the opposite of what the reviews page is for. They stay in the flagged pile permanently, not as a deferral.

## 3. The paragraph spacing carries to Kain's Safari sitting

Not ruled here, and deliberately so. Your point is the deciding one: for the 622 reviews that carry newlines, this is not "add spacing", it is "start showing breaks that have always been in the data", on a page Kain approved as it currently renders. That is a visual decision on a built page, so it belongs on your surface under standing rule 16, alongside the three already carried in `RULING__Gate_Check_4_Authorised_And_Icon_Sweep_Answers_S263`.

When it comes up, he needs to see it rather than read it: the same real reviews rendered as they are now against rendered with the stored breaks shown and spaced, one variable changed.

## 4. What Chat records

The apply pass is authorised and its result is expected back through the channel: the count actually changed, any review the pass skipped that the dry run predicted it would change, and confirmation that both reversal mechanisms were in place before the first write.

*No em or en dashes in this file; checked before writing.*
