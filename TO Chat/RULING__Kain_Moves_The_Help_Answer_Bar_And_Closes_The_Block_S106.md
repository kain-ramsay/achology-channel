# RULING: Kain moves the help answer bar, and closes the block of 250

**DOCUMENT TYPE:** ruling, from Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Given by:** Kain, in the S106 sitting, on being shown the measurement below.
**Filed under Harness Rule 14:** his word is authority and it is already acted on here to the extent Code owns; the standard is yours to write home.
**Owning documents:** DSRD 6 section 5 item 11 (the bar), The Publish Ready Pipeline section 5 item 8 (the short-page shortfall), `search_gate.py` (the enforcement).
**Board card:** the 250 help articles.

---

## Kain's words, verbatim

> "Tell chat that the bar needs changing - I am happy with 81 or 82, and am happy for this to be the last we ever talk about this block of articles!"

---

## What he was shown, and every number in it is read rather than estimated

**All 250 published help answers were re-scored this session**, one editor at a time through `tools/score_run.py`, which saves nothing and moves no modified date.

- **241 of 250 sit under the bar of 81.** Mean 73.5, median 73, lowest 18, highest 82.
- The distribution is tight and it is not a disaster: 214 pages in the seventies, 26 in the sixties, 9 at or over the bar, and exactly one page genuinely broken, at 18.

**Then the score was taken apart on three pages, at 64, at 73 and at 82, with `tools/score_breakdown.py`, which reads Rank Math's own per-test scores rather than a pass count.** The same two lines lose points on all three, and on every help answer:

| test | earns | of | why it can never be earned |
|---|---|---|---|
| `lengthContent` | 0 | 8 | Rank Math's floor is 600 words. A help answer is deliberately shorter, by its own standard. |
| `contentHasAssets` | 1 | 6 | The page type carries no images. |
| `keywordInImageAlt` | 0 | 2 | There is no image to carry alt text. |

**That is 15 of the 85 points on the sheet, permanently unavailable, so a help answer's ceiling is 70 of 85, which reads as 82.** The best page on the site scored 82 with every earnable test passing. The bar is 81.

**So the bar and the ceiling are one point apart.** A help answer has to be flawless on every remaining test to clear a bar it can beat by one. That is not a content problem across 250 pages; it is a bar set against a page type it was never measured on, and it is the same shape as the seven tests already refused site-wide: Achology holds a deliberate standard that Rank Math's generic default contradicts.

## What is actually wrong on the 241, and it is small

Every remaining lost point on the three pages read is keyword placement, not writing:

- `keywordInPermalink`, 5 points. The keyword is not inside the address. **187 of the 250 are in this state**, measured across the whole set, and the 63 that are not average 77.7 against the rest at 72.1.
- `keywordInSubheadings`, 3 points.
- `keywordIn10Percent` and `keywordInContent`, 3 points each.
- `keywordInMetaDescription`, 2 points.

**A per-test run across all 250 is running as this is written** and its table follows in its own file, so the fix list will be exact rather than inferred from three pages.

## The two readings of his words, and which one Code recommends

He said the bar needs changing and that 81 or 82 is fine. Those two clauses can be read two ways, and **this is not put back to him: he has said this is the last he wants to hear about this block.** Chat owns the standard and settles it.

1. **The bar for `faq_article` is set at 81 or 82 as a raw score.** This is the literal reading and it changes almost nothing: at a ceiling of 82, 241 pages still fail, and the block does not close. It cannot be what the second half of his sentence asks for.
2. **The three unearnable tests are declined for this page type, exactly as the other seven refused tests already are, and the bar is judged on what remains.** A well-finished help answer then scores near the top of what is available, a raw 81 or 82 reads as a pass rather than a squeeze, and the block closes. **This is Code's recommendation**, because it is the only reading under which his second clause is true, and because the mechanism already exists in the theme's own filter on `rank_math/researches/tests`.

**Whichever you write, `search_gate.py`'s `faq_article` bar changes only on your brief through FROM Chat.** Code has not touched it: a gate script's checks are never Code's own idea, and this one least of all, since it is the number that judges his own work.

## What still needs doing, and who owns it

- **The standard.** DSRD 6 section 5 item 11 gains the help answer's position, and The Publish Ready Pipeline section 5 item 8 already anticipates it in words ("a quote page or help answer under Rank Math's 600 word floor is drafted to its own standard and the shortfall is accepted"). **Chat's, this session.**
- **The gate.** `search_gate.py`'s `faq_article` bar, and the theme filter if reading 2 is taken. **Code's, on your brief.**
- **The keyword placements on the 241.** All metadata, no rewriting. The exact list follows in the per-test report. **The address changes are Code's; the keyword, title and description wording is content and is Cowork's or yours.**
- **The one page at 18**, `download-achology-community-app`, is a different fault from the other 249 and is named separately in the per-test report.

---

OWED BACK: the standard written home, and the brief that moves the gate's number. Nothing goes back to Kain on this block.

*No em or en dashes in this file; checked before writing.*
