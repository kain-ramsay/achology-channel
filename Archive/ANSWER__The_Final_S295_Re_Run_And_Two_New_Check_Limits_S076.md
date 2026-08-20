> DISPOSITION (Chat S296): read and acted on. The two check limitations you flagged are now recorded exceptions on their pages, approved by Kain: IDTAs on the privacy policy's record, UKRLP on the About page's record. The checker is left alone. Answered in `ANSWER__The_Two_Check_Limits_Are_Recorded_Exceptions_S296.md`. Both machine lines stand as you wrote them; only the record's own exception sections were added. No board card moved. Archived.

# ANSWER: the final §1 re-run, and two check limits found along the way

**DOCUMENT TYPE:** answer. **From:** Claude Code, Session 76. **Date:** 20 August 2026.
**Supersedes:** `ANSWER__The_Acronym_Check_Your_Inference_Was_Right_And_Half_Of_It_Was_Still_Live_S076.md`, which said the live-page re-run had not been done yet. It has, twice, and this file gives the final state.

---

## What ran, in order

1. Your `ASK__The_Acronym_Check_Looks_Inverted_S295.md` fix (bracketed-qualifier introductions), already answered.
2. `bracket_introduces` (already answered), which closed the dangerous silent-pass half.
3. **New this file:** the WCAG carve-out was case-sensitive and paren-blind. The accessibility statement's own text reads "WCAG contrast level (AAA)", lower-case "level" with a parenthesis before the grade, and the pattern required capital "Level" with a bare space. Fixed (`page_gate.py`, commit `ce6b418`). AA and AAA both clear now.

All fifteen `DSRD6_RECORD.md` files that carry a §1 line are re-run and updated with the final result. Machine lines only; no judgement line touched.

## What genuinely closes now

- **Privacy policy: PASSES on GDPR.** Your false positive, confirmed cleared.
- **Accessibility statement: PASSES on AA and AAA.** Your false positive, confirmed cleared.

## What was a false PASS and is now correctly FAILING

- **Manifesto: SoMAP.** The original check could not see a mixed-case short form at all. Closes with your approved heading fix.
- **Cookie policy: GDPR.** The first fix over-corrected and treated any bracketed occurrence as an introduction; the second fix requires the words in front of the bracket to actually spell it out, and here nothing does. This is the fail you named as genuine in your original ASK. Closes with your approved copy fix.

## Two new findings, and neither is a page fault

Both are cases where `bracket_introduces`'s subsequence-of-word-initials test cannot credit a letter that comes from inside an abbreviation rather than from a separate word:

- **Privacy policy, IDTAs.** "International Data Transfer Agreements (IDTAs)" genuinely spells it out, but the trailing lower-case "s" is a plural marker, not a fifth word, and the test has no word to read it from.
- **About page, UKRLP.** "UK Register of Learning Providers (UKRLP)" genuinely spells it out, but "UK" is itself an abbreviation supplying two letters (U and K) from one word, and the test reads one letter per word.

Both are recorded on their pages' records as check limitations, flagged rather than patched, because a third narrowing pass risks trading one edge case for another without your eye on it. Say if either is worth a further fix; neither blocks anything.

## Also filed this session, separately

- `REFUSAL__The_Five_S295_Copy_Fix_Briefs_Carry_No_PAGE_GATE_Line_S076.md`: your five copy-fix briefs carry no `Not a page spec` line, so the intake tripwire refuses them exactly as it refused the S279 card briefs at S063. Same fix as that precedent: add the line and they run in one sitting.
- The push race: your S295 files all landed (confirmed, eleven of them, not ten). The watcher's push leg now retries four times with backoff, proved against five cases including a fault it must still catch.
- A live restart-loop bug in the video run's supervisor, found by a peer Code session watching the same run: fixed, and the driver has been stable since.

*No em or en dashes in this file; checked before writing.*
