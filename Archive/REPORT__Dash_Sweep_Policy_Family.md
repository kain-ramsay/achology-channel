# REPORT: the dash ban applied to the policy family, 94 replacements, punctuation only

**From:** Claude Code, S230. **Date:** 2026-07-29. **Ships as:** theme v0.36.31, zip rebuilt, awaiting Kain's upload.
**Authority:** Kain's direct instruction, recorded verbatim in `NOTE__Kains_Words_On_The_Dash_Sweep.md`.

## The standard, quoted

DSRD 2 section 3.0: "No em dash (U+2014) and no en dash (U+2013) appears anywhere in Achology copy: page copy, articles, headings, metadata, captions, CSV fields and emails alike, across every page and content type this document specifies, with no exception. Use a colon, a comma, brackets or a full stop instead. The check is mechanical: a piece containing either character is not ready."

## What changed

| Page | Replacements |
|---|---|
| Privacy Policy | 43 |
| Cookie Policy | 17 |
| Terms and Conditions | 12 |
| Trust Statement | 10 |
| Disclaimers | 7 (4 em, 3 en) |
| Accessibility Statement | 5 |
| **Total** | **94** |

The Refund Policy carried none and was not touched. Zero dashes now remain in any of the seven pages' copy.

**Punctuation only. No word was added, removed or reordered anywhere.** The rules I fixed in advance, so the choice was never made sentence by sentence:

1. A pair of dashes inside a sentence becomes a pair of commas: "tools we use, such as Google Analytics, are third-party".
2. A dash straight after a bold label becomes a colon: "To understand how the site is used: anonymous-style analytics".
3. Every other dash becomes a comma where what follows hangs off the sentence ("including people who use a keyboard"), and a colon where what follows stands as its own clause ("built with semantic HTML" against "operated entirely by keyboard: menus open and close with Enter or Space"). A comma in that second case would splice two sentences together, which is a different fault from the one being fixed.

The copy is Kain's and yours. If any one of these reads better another way, it is a one-line change.

## Two things found while in there, neither fixed

**1. The dash count in a file search is not the dash count on the page.** Most of these were written as `&mdash;` rather than as the character. A grep of the theme for the character alone found 5 in the privacy policy; the rendered page carried 42. Anything that certifies the ban by searching source files is under-reporting, and the page gate, which reads the rendered text, is the instrument to trust.

**2. `policies-content/policies.php` is a dead file, and it carries the old index copy.** It holds seven em dashes and a full set of policy row descriptions. Nothing references it: the Policies index is rendered by `template-policies-index.php` from its own row data, which is why the live page is clean and this file is not. It is a duplicate of a block that has one home elsewhere, so it belongs to your `BRIEF__Collapse_Every_Duplicated_Block_Into_Its_One_Home.md`, not to this sweep. **I have not deleted it.** Recommend it goes in that pass.

Three other files carry dashes inside HTML build comments (`code-of-ethics.php`, `manifesto.php`, and one line in `policies.php`). Those are not copy, they never render, and they are untouched.

## Deployed, and verified on the live pages

Kain asked me to deploy it myself rather than upload a zip, so the changed files went straight to the build site over the existing SSH access and the dynamic cache was purged. **All seven policy pages now pass every check the page gate carries except the site wide canonical**, which you have already ruled out of page work. Terms and Conditions and the Trust Statement read 27 pass, 1 fail; so do the other five.

**Two dashes survived the first pass, and the gate caught both.** The reason is worth recording, because it is the same class of fault as the spacing drift reported earlier today: my comment mask treated the `//` in `https://` as the start of a line comment, so any dash later on a line carrying a link was skipped as though it sat in a comment. The two that survived were both immediately after a link. Fixed, re-swept, redeployed, re-checked.

The lesson is the one the harness already states: the file check is not the verification. The sweep reported itself clean on the files and was not clean on the pages, and only the rendered check knew that.

## One thing for the register, not fixed

**The dash ban is broken in metadata as well as in copy, and nothing checks it.** Terms and Conditions carries an og:image:alt of "Achology's terms and conditions [em dash] an ancient handwritten scroll lit in amber against a dark background". DSRD 2 section 3.0 covers metadata explicitly. The page gate reads rendered body text and does not look at meta fields, so this is invisible to it. That is a checker gap and a content defect, and both belong with you rather than in this sweep.

## What is verified, and what is not

**Verified:** zero dashes remain in the copy of all six changed files, checked with comments stripped so the count is of copy only. The theme committed at v0.36.31 and the zip rebuilt.

**Verified on the live pages:** all seven, after deployment, zero dashes in the rendered text of any of them.

**Not yet done:** the seven DSRD 6 records. Structure and copy both pass now, but a page has no verdict until every chapter of DSRD 6 has one, and several chapters need instruments I have not run on these pages yet (the accessibility walk, the speed test, the schema check). The records follow; the pages are not being called done before then.

*No em or en dashes in this file; checked before writing.*
