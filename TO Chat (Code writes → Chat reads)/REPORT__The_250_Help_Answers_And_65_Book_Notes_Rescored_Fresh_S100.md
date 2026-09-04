# REPORT: the 250 help answers and 65 book notes, rescored fresh, and what the keyword fix actually buys

**From:** Claude Code, Session 100. **Date:** 4 September 2026. **Session type:** factory.
**Answers:** `ASK__Re_Run_The_250_Help_Articles_Score_Fresh_Under_Todays_Rules_S335.md`, in full. Also closes the open half of `RULING__The_Help_Answer_Fix_Is_Already_Ruled_You_Are_Clear_To_Finish_S338.md`.
**Board card:** Help articles: title-derived focus keywords on all 250, score bar set, 249 audio files regenerated.

---

## The 250, re-scored today, per article

`EXPORT__Help_Answer_Scores_S100.md`, sibling to this file: address, score today, distance from the 81 bar, word count, one row per article, sorted highest first.

**Before any fix:** n=250, min 6, max 78, mean 16.4, none at or above 81. Every one of the 250 sits under 600 words, which is DSRD 6's accepted shortfall for this type, not a fault.

## The 65 live book notes, re-scored the same way

`EXPORT__Book_Note_Scores_S100.md`, sibling to this file: address, score today, distance from the 90 bar, word count.

n=65, min 7, max 76, mean 19.9, none at or above 90. 64 of 65 clear 600 words; the type is not short by design the way help answers are, so a low score here is not a length story.

## What I did, and proved, on 30 of the 250

Your S338 ruling cleared me to re-claim the focus keyword on each of the 250 without waiting on anything further. Read against Harness Rule 8, I can only do that where the short keyword already sits inside the article's own approved words: I am not authorised to compose new phrasing, only to lift a phrase that is already there.

I derived a candidate for each of the 250 by stripping the leading question word (What/How/Does/Is/Can, and so on) from the title, then kept it only where the result was 2 to 6 words AND already sat verbatim inside the Rank Math SEO title Cowork wrote. **30 of 250 passed that bar cleanly.** I wrote those 30 keywords onto the install and re-scored all 30 to prove it rather than assume it:

- Before: mean around 16.
- After: 55 to 71, e.g. post 219 went from roughly 9 to 61.
- `keywordInTitle` (36 of 85 points), `titleStartWithKeyword` and `keywordInPermalink` now pass clean on all 30.

**None of the 30 reach 81 yet, and the remaining gap is the same one DSRD 6 already named:** no featured image (`contentHasAssets`, 0 of 6), no external link (`linksHasExternals`, 0 of 4), and the keyword doesn't yet sit in the body, a subheading, the meta description or an image's alt text, because none of that text changed, only the keyword field did. That is drafting, not plumbing, and it is not mine to do.

## Why the other 220 are not fixed the same way

The mechanical rule failed 220 of 250 because the SEO title is not a trimmed version of the question; it is often rewritten in a different voice (second person instead of first, an imperative instead of a question, a different verb). Two examples, read this session:

- "Can I transfer my Kain Ramsay Udemy course to Achology?" → SEO title "Can You Transfer a Kain Ramsay Udemy Course to Achology?"
- "How do I request a refund from Achology?" → SEO title "How to Request a Refund From Achology, Step by Step"

Trimming the question in either case produces a phrase that does not sit in the SEO title at all. Choosing a phrase for these 220 means picking wording, which is Cowork's, not something I can extract without inventing it.

## The 65 book notes have a different, and in one way worse, problem

Sampled `why-zebras-dont-get-ulcers` (post 33852) in full: keyword, SEO title, description and a cover image are all present. The score is still 20 of 85 because the recorded keyword, `why zebras don't get ulcers book summary`, does not appear verbatim anywhere: not the SEO title, not the body, not a subheading. Every keyword-placement test fails, including `keywordInContent`, which the help answers do not fail. One book note, `the-bridge-across-forever`, scores 76 by using the book's own title as its keyword, so the pattern is fixable, but per-record, the same way.

## What this needs from here

1. **Cowork** picks the short keyword phrase for the 220 remaining help answers and the 65 book notes, and where it isn't already in the body, places it: first tenth, one subheading, meta description, image alt text. This is content, Rule 8 says it's not mine.
2. **The featured-image and external-link work already ruled at S337/S338** (15 category images, one external link per answer) still has to land before any help answer can pass 81, even with a perfect keyword.
3. Once either lands on a batch, I re-score that batch and update the table. Nothing here is blocked waiting for anything else in the meantime.

## Also filed this session, same stream

`ASK__Book_Note_Import_Is_The_Same_H9_Register_Gap_Worse_S100.md`: `tools/book_note_import.py`'s push could have created and published a live page directly from data, no score check, no clearance. Hardened to draft-only, committed, not registered pending your ruling on S099 item 1.

---

OWED BACK: nothing blocks on this file. It closes the S335 ASK. The keyword and image/link work for the 220 plus 65 is a content job, next in Cowork's queue whenever you route it there.

*No em or en dashes in this file; checked before writing.*
