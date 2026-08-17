# SHIP: v0.38.52, the three signed S248 briefs, all live and read back

**From:** Claude Code, S048. **Date:** 2026-08-06.
**Closes:** `BRIEF__Link_Orange_Darkened_And_1px_Underline_S248.md`,
`BRIEF__Footer_Headings_Light_Orange_F5A05C_S248.md`,
`BRIEF__Accessibility_Statement_Space_Sentence_S248.md`.
**Live:** https://achologytest.com, theme reports `?ver=0.38.52`. Pushed to
GitHub, `e1c3cfa..b76c174`. Cache purged before every measurement below.

## 1. Link orange darkened to #B8460F

`--color-orange-link` is now #B8460F in base.css, with the companion
`--color-orange-link-rgb` at 184, 70, 15. One value, everywhere the token is
used.

Three hand-typed values that were not tracking the token are now tracking it:
`rgba(198, 78, 20, 0.32)` underline colours in knowledge-hub.css and help.css,
and a literal `#C64E14` on the help page's helpful-strip thanks line. Stale
comment quotes of the superseded DSRD 7 section 1 sentence were restated in
about.css and components.css.

**Measured on the rendered live page, cache purged**, the six Disclaimers
section 12 cross-reference links that failed the S047 walk:

| Link | Contrast |
|------|----------|
| Terms & Conditions | 5.36:1 |
| Refunds Policy | 4.86:1 |
| Privacy Policy | 5.36:1 |
| Cookie Policy | 4.86:1 |
| Trust Statement | 5.36:1 |
| Accessibility Statement | 4.86:1 |

All six clear the 4.5:1 that 15px text requires. The three at 5.36 sit on
white, the three at 4.86 on the off-white panel, matching the two numbers
DSRD 7 section 1 now names.

**One item of the brief needed no change, reported so the record is accurate.**
The 1px underline was already in place site-wide before this session:
policies.css (three rules), knowledge-hub.css and help.css all carried
`text-decoration-thickness: 1px` on every body-copy link. Verified on the
rendered page at desktop, tablet and phone. Nothing was changed to satisfy
that half of the brief, and nothing needed to be.

## 2. Footer headings and CTA overline to light orange #F5A05C

A new token `--color-orange-footer: #F5A05C` in base.css, annotated per
DSRD 7 section 4.5. The three footer column headings (and their mobile
accordion form, which is the same element) and the CTA card overline take it.

Measured on the rendered live page: the headings at **5.02:1** on #354149,
against the 3.32:1 that brand orange measured. The CTA overline sits on the
card's `linear-gradient(160deg, rgba(237,105,34,0.08), rgba(237,105,34,0.03))`
tint over the same footer ground, so it was measured across the gradient
rather than at one point: **4.65:1 at the strongest orange stop and 4.89:1 at
the weakest**. It clears 4.5 across the whole card, as the brief asked me to
confirm.

No other footer element changed. The Start Your Trial button is untouched.

The section 19.6 comment in footer.css about the Achology span was restated:
it quoted the pre-S248 DSRD sentence naming brand orange and #C64E14, and that
sentence has been replaced. The span still inherits, so the heading renders
identically whether the word is wrapped or not.

## 3. Accessibility Statement, "or Space" removed

The rendered live page now carries the approved sentence word for word:

> "**Full keyboard access.** Site navigation, including dropdown menus, can be
> operated entirely by keyboard: menus open and close with Enter, Tab moves
> through the links, and Escape closes a menu and returns focus to where you
> were."

Read back off https://achologytest.com/policies/accessibility-statement/ after
the cache purge. "Enter or Space" appears nowhere on the page. Nothing else on
the page changed.

## Gates

`css_gate` PASS on all seven touched files: base.css, footer.css, help.css,
knowledge-hub.css, about.css, components.css, style.css.

Three files still FAIL `css_gate` and were **not** touched by this work, so
they are reported rather than hidden: cards.css (7 issues), people.css (3),
testimonials.css (24). All pre-existing. Raising them as a job is a separate
question and I have not acted on them.

Dash check clean on the touched copy.

## What Chat can now restate

- Every walk record that referenced the link-orange finding can close its
  section 7 item.
- Every walk record's section 7 chrome item on the footer headings can close.
- The Accessibility Statement walk record's section 11 item 2 can close on the
  keyboard claim.
- The Accessibility Statement's own sentence, "all body-length text uses a
  colour combination that passes WCAG AA", is true again as of this ship.

*No em or en dashes in this file; checked before writing.*
