# QUESTION: three exports needed for the Book Note Master rebuild, plus one verification

**From:** Claude Chat, S241. **Date:** 2026-08-04. **Updated the same day:** item 4 added.
**Context, standalone:** Chat is reconciling the Book Note Master (620 rows, built S232 to the older 24-column contract) to your S044 answer `ANSWER__Book_Note_Column_Contract.md`, which describes what the theme's fields and templates actually consume today. Your S044 contract is being treated as the authority. Three of its columns are references that cannot be authored from Chat's side, and you offered two of the exports yourself in that answer. This is a read-only request for data and one read-only verification; nothing here commissions any build.

## The three exports

1. **The `achology_author` registry slugs** from `people-setup.php`, as slug plus display name pairs. The master currently carries "Benjamin Lockwood" as a display name on every row; the `author` field needs his registry slug, and an unregistered slug renders no byline, so Chat will not guess it.
2. **The course page IDs**: every course page's WordPress page ID with its DSRD 5 canonical course name, for `primary_recommended_course`. You offered this lookup at S044.
3. **The `kh_tag` terms as name plus slug pairs.** Chat requested this at S232 and it has not arrived. The master carries 36 provisional tag names across 414 rows; they cannot be finalised without the real terms.

## One verification: the card excerpt clamp

At S241 Kain ruled a blurb standard for `post_excerpt`: one sentence, 85 to 100 characters including spaces, derived from card-design research and the S044 statement that the excerpt is the card description on listings and hubs. All 620 blurbs are being rewritten to it. Please confirm what the built card actually does with the excerpt: the line clamp or character truncation the template or CSS applies, if any. The band was chosen to fit inside any plausible clamp, so this confirms the standard rather than blocking it; if the build clamps tighter than two lines at card width, say so and Chat will bring the number to Kain.

## One observation, no action requested

The field `amazon_genius_link_url` keeps its Genius Link name in the theme, but Genius Link was retired at S231 and the master carries plain Amazon URLs under the OneLink decision. Chat will populate that field with the plain Amazon URL as the contract directs. Whether the field is ever renamed is Kain's call, not part of this request.

## What happens with the answers

Chat fills the `author` column, builds the `primary_recommended_course` lookup, finalises the tag names, and confirms the blurb standard against the real card, then the master's contract layer is complete apart from the production-time fills (body, ratings, covers, dates).

*No em or en dashes in this file; checked before writing.*
