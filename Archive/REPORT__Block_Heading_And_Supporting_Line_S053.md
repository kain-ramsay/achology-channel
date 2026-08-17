# REPORT: block headings and their supporting lines. There is no standard, and it shows

**From:** Claude Code, Session 053. **Date:** 2026-08-11. **Theme:** v0.60.0.
**Commissioned by:** Kain, in session, after spotting two pairs on the testimonials page that did not match. He asked what the permanent fix is, and approved handing you the measurement so you can write the rule.
**What this asks of you:** one written standard. The wording is yours under Rule 8; the mechanical check that enforces it is mine.

## 1. Kain's two rulings first, so the record carries them

1. **The member stories block stays on the reviews page.** I had advised against it, on the grounds that five videos across three pages thins the testimonials page. He looked and ruled: "leave it as it stands, it fits fine." My advice is declined and that is the end of it. The reviews page carries `Five Aspects of the Achology Learning Experience` under its archive.
2. **The audit comes to you** so the standard can be written.

## 2. What he saw

Two pairs on one page, which is all it took:

> **Five Aspects of the Achology Learning Experience**
> Watch testimonials videos from our past and present students on their Learning Experience with Achology.

> **Achology Reviews: What Our Learners Say**
> Since launching our first online course in 2014, we've learned from All Our Reviews. Good and bad, they teach us what to improve.

Fifteen words against twenty-three. One sentence against two. An instruction against a story. Both his own words, written months apart, and both correct against every rule that exists, because no rule exists.

## 3. The measurement

Sixty block headings across nine built pages, read from the live pages.

| | |
|---|---|
| Block headings | 60 |
| Carrying a supporting line | 49 |
| Carrying none | 11 |
| Supporting line length | **6 to 61 words**, median 30 |
| Voice | 45 narrative, 4 imperative |
| Sentence count | 21 one sentence, 28 two or more |
| Carrying capitalised words mid-sentence | 16 |

**A ten-fold spread in length is the headline.** Six words at the shortest and sixty-one at the longest, both doing the same job in the same slot.

**One carve-out you should account for before writing anything.** Twenty of those sixty are the Privacy Policy's numbered clauses, where the paragraph under each heading is the legal text itself rather than a supporting line. Lumping them in would drag every average and would make the standard unwritable. The rule should either exempt legal documents by name or address only blocks whose paragraph is a supporting line by intent. **The other forty are the real subject.**

**Eleven headings carry no supporting line at all**, and they are not errors: the policies index, the three instructor sections and two help hub headings all stand alone and read fine. So the standard has to say *when* a supporting line is required, not just what it looks like.

## 4. What I would put in the rule, as a starting point rather than a proposal

Yours to write, but these are the five things the measurement says need deciding, in the order they bite:

1. **When a supporting line is required.** Eleven headings do without one. Is that by page type, by block type, or by the writer's judgement?
2. **A length range.** The current spread is 6 to 61 words. My reading of what actually looks right on the page is somewhere near 12 to 25, but that is an eye judgement and it is Kain's, not mine.
3. **One sentence or more than one.** Currently 21 against 28, so the site has no habit either way. One sentence is the tighter rule and the easier one to hold.
4. **Voice.** 45 narrative against 4 imperative says narrative is the house voice and the imperatives are the outliers, **but one of those four is the line Kain approved an hour ago** ("Watch testimonials videos..."), so this is his call and not a matter of counting.
5. **Capitalisation inside the line.** Sixteen carry mid-sentence capitals. Some are proper nouns and correct; some are ordinary words in title case. A rule of sentence case except proper nouns would settle it, and it is the one item here that is unambiguous.

## 5. What I will build once it is written

Four of those five are mechanically checkable and I will add them to the page gate: word count, sentence count, mid-sentence capitalisation, and the first-word test for voice. "When a line is required" needs the rule to name the block types, and then it is checkable too.

That turns this from a thing somebody notices into a thing a page cannot ship past, which is the same treatment the dash ban has.

## 6. One thing about this report you should know

**Two earlier versions of the script that produced these numbers were wrong**, and both produced output that looked like data: a regex version swallowed body copy into the headings and reported one heading on pages carrying eight, and a parser version desynced on the country panel's nested markup and found three of the reviews page's eight. Kain was shown neither.

The version behind the table above verifies its own parse against a raw count of `h2` tags in the same document and refuses to report any page where the two disagree. All nine pages reconciled. I mention it because the first two would have had me writing you a confident standard on top of nonsense.

*No em or en dashes in this file; checked before writing.*
