# REPORT: the S226 link map is run across all 249, live and verified

**Written:** 28 July 2026, S228. **From:** Claude Code. **For:** Claude Chat.
**Authority:** `BRIEF__Internal_Links_Across_The_249_Help_Articles.md` (S226),
re-commissioned in `00__RULING__Harness_Live_249_Stand_Cleanup_Pass_Commissioned.md`
section 2 item 4.

Done, gated, published, read back from the live database, and 20 opened in Kain's
Safari for review.

## 1. The numbers

| | |
|---|---|
| Articles read | 249 |
| Articles gaining links | 187 |
| Links added | 459 |
| Links on the section before | 2,057 |
| Links on the section now | 2,516 |
| article_gate failures | 0 of 187 |
| Unterminated links after publishing | none |
| Publish result | updated 187, failed 0 |

## 2. Links added per category

| Target | Added | Target | Added |
|---|---|---|---|
| /courses/ | 111 | /academy/ (landing) | 12 |
| /membership/ | 54 | /policies/refund-policy/ | 8 |
| /certification/ | 54 | /policies/privacy-policy/ | 7 |
| /accreditation/ | 32 | /policies/cookie-policy/ | 5 |
| /academy/schools/ | 27 | /about/instructors/kain-ramsay/ | 4 |
| /pricing/ | 26 | /about/instructors/gerard-egan/ | 3 |
| /access-all-areas/ | 25 | /free-events/, /free-coaching/, /enquiries/ | 3 each |
| /about/code-of-ethics/ | 19 | /learn/ | 2 |
| the 7 school pages | 30 | /learn/workbooks/, /testimonials/, /policies/ | 1 each |
| the 28 course pages | 33 | the remaining policy pages | 5 |

The site-wide picture after the pass: 1,798 article-to-article links (unchanged,
untouched), 133 to the academy and its schools, 121 to courses, 99 to the policy
family, 94 to certification, 87 to membership, 41 to About, 34 to Access All
Areas, 32 to pricing, 27 to accreditation, 23 to enquiries.

## 3. The rules, one by one

1. **First mention only.** Enforced per target per article.
2. **Body only.** Every heading is masked before matching, so no H1, H2 or H3
   carries a new link.
3. **No self-links.** Each article's own URL is excluded from its own map.
4. **The anchor is the words already there.** The matched text is re-emitted
   character for character. No word was added, removed or reordered anywhere in
   the 249. The word counts are identical before and after.
5. **No invented anchors.** 62 articles carry no mapped phrase and were left
   untouched. They are logged in `linkmap_log.json`.
6. **Eight per article.** 8 articles hit the cap; the overflow is logged with the
   phrase and intended target in `linkmap_log.json`.
7. **Existing links untouched.** Existing anchors are masked before matching, so
   nothing was re-pointed and no link is nested inside another.
8. **Live targets only: overridden by Kain**, this session, in his words: "yes,
   write every link now". See section 5.

## 4. Rule 5 in practice: what I refused to link, and why

The brief says where a mention does not fit, link nothing and log it. Six kinds
came up, each found by reading the dry run rather than by guessing:

- **"the Academy of Modern Applied Psychology Ltd"** is the registered company.
  Linking its first two words splits a company name, so it is skipped.
- **"reviews" as a verb.** "The Society of Modern Applied Psychology then reviews
  the claim" is not the reviews page. Bare "reviews" is linked only where a
  determiner marks it as the noun, which in practice meant none of them.
- **"terms".** Almost every instance is "in terms of". 19 articles carry one and
  none is linked. Only "terms and conditions" would have been.
- **"Web Content Accessibility Guidelines"** is a published standard, not the
  accessibility statement.
- **"the Privacy Notice"** is a named document; linking one word out of its name
  splits the name.
- **"accredited" describing another profession.** "years of accredited study,
  supervised clinical hours and professional registration" is about regulated
  therapy, not Achology accreditation. Where another institution's language sits
  within 160 characters, the word is left alone. That skipped 22 candidates.

## 5. Kain's override of rule 8, on the record

Rule 8 says write a link only where the target returns 200 today. I checked, and
half your map is not built: **live** are the seven policy pages, the policies
index, About's code of ethics and manifesto, the instructors index, Kain Ramsay,
Gerard Egan and testimonials. **Not built** are /courses/, /academy/,
/academy/schools/, all seven school pages, all 28 course pages, /membership/,
/pricing/, /access-all-areas/, /accreditation/, /certification/, /reviews/,
/free-events/, /free-coaching/, /enquiries/, /learn/ and /learn/workbooks/.

That is the entire commercial half, which is the reason you wanted the pass. I put
it to Kain as one question and he ruled: write every link now. His reasons, in
his words and from the rebuild: the address structure is settled, the pages are
coming, and the section already carries hundreds of links written that way.

So there is no deferred list. Instead, **408 of the 459 new links point at pages
that do not exist yet.** They resolve the day those pages ship, and they are
listed above by target so you can see exactly what goes live with each page. The
51 that work today are the policy family, the two instructor profiles, the code of
ethics, the manifesto and testimonials.

## 6. Verification

Gate before publishing: `article_gate` clean on all 187. Read back from the live
database after publishing: 249 articles, 2,516 links, no unterminated anchor, no
article shorter or longer than before. Twenty of the edited articles are open in
Kain's Safari now, spread across all fifteen categories.

## 7. What this pass did not touch

The register pass, the Code of Character and Conduct replacement and the Wiser
People sentence are all still outstanding. Your first-mention-only ruling landed
while this pass was running (hook H6 blocked me mid-edit until I read it, its
first real firing on live work) and those three run next.

---

HARNESS | Scope: the S226 link map across all 249 help articles | Spec quoted: yes (the brief's rules 1 to 8, and DSRD 1 section 2.3 for the school and course slugs, verified against the map) | Gates: pass, article_gate clean on 187 of 187, read back live with no unterminated links | Page: 20 articles open in Safari, listed in section 6 | Outside scope: none
