**Needs from Chat:** nothing to act on; record it on the policy pages sweep card. Part of `BRIEF__The_Policy_Pages_Sweep_S386`, done ahead of the rest on Kain's direct instruction.

# REPORT: every policy page carries its own image, and all score above 80

**From:** Claude Code, S135 (theme), Monday 28 September 2026. Theme 0.668.0.

Kain, in the sitting: raise every policy page above 80 in Rank Math by baking a unique image into each, with proper alt text and SEO practice; "you decide, you source the images, bake them in, implement, job done."

## What was built

- **One image per policy page with no art of its own** (Privacy, Terms, Cookies, Refunds, Trust, Disclaimers, Accessibility, How We Write; the Code of Ethics, Manifesto and Founders' Letter already carry art). Each is the page's word from the Policies index ghost words, in Como Bold, faint brand orange, on a transparent ground. No stock images, so nothing to license.
- **SEO and image standard:** keyword file names (`images/policies/achology-{slug}.webp`), alt text naming the page, width and height declared, a 600 and 1200 `srcset`, WebP under 17KB. Placed as a real `<img>` behind the right of the header in `template-policy.php`, hidden below 1024px like every watermark. Made by `tools/policy_header_images.py`, rerun for any new policy page.

## Rank Math, read fresh from the install into the score table

Privacy 94 to 95; Terms 94 to 95; Cookies 88 to 89; Refunds 88 to 89; Trust 88 to 89; Disclaimers 89 to 91; Accessibility 87 to 88; How We Write 79 to 82.

## OWED BACK

Nothing.

*No em or en dashes in this file; checked before writing.*

## Later the same sitting

Kain chose option 2 of five rendered positions, "slightly smaller": the word now sits behind the page title, trimmed to its own edges, at 60 per cent of its 2x master. Theme 0.668.1.
