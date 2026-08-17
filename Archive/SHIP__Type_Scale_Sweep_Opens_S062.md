**DISPOSITION (S280, Chat):** read and answered at S279 via REPLY__The_Four_S062_Files_Answered_S279 in the new FROM Chat. Recorded at S279 in DSRD 7 section 3.0: the tie correction (the override's 13-down-to-12 governs over the S056 wording), the token naming disagreement and which document governed, the measured 318 declarations against the brief's 167, and the site-wide 33px h1 consequence. Archived.

# SHIP: v0.64.0, the type scale sweep opens with the tokens, the foundation and the policy family

**DOCUMENT TYPE:** ship brief. Not a page spec, not a commission.
**From:** Claude Code, Session 062. **Date:** 17 August 2026.
**Executes:** `BRIEF__Type_Scale_Sweep_S270.md`, signed by Kain at S270 and never started until today.
**Board card:** the typography card.

---

## What shipped

**The nine tokens exist**, in `base.css`, named by value per brief section 6: `--text-12` through `--text-42`. Brief section 6's naming is what was built, not the role naming that `GUIDANCE__Standardising_The_Type_Across_The_Site_S269.md` section 4 argued for. The guidance is explicitly not a ruling and the brief is signed, so the signed document governed. Worth a line in whichever document ends up owning this, because the two disagree in writing and a later reader will find both.

**Two bodies of work moved onto them:**

| Body of work | Declarations now on the scale | Left literal |
|---|---|---|
| `base.css`, the shared foundation | 17, every one a token | none |
| `policies.css`, the policy family | 17, every one a token | the 9 watermark sizes, the named exception |

**Sizes that actually moved**, all of them inside the render Kain already approved: the page h1 32 to 33, the policy lead 19 to 18, h3 20 to 21, the index card name 17 to 16, the meta line 13 to 12, the overline 11 to 12, the table 15 to 14, the stacked table label 11 to 12, and in the foundation h4 17 to 16, the overline 11 to 12, nav 13 to 12, caption 13 to 12.

**The fold-in from brief section 4 is done:** the policy pull quote takes brand dark, the S226 ruling `policies.css` never received.

**Nothing else was touched.** No `font-weight` and no `line-height`, per brief section 2.

## Why this shipped without a new sitting

Brief section 5 names the policy family as **already approved**, and it is: the page Kain ruled on at S056 was the privacy policy page rendered twice, and his words were "I think the right-hand one reads better (on your proposed scale)". So the representative page for this page design has been through his eye, and asking again would spend a sitting on a decision he has already given.

**The foundation shipped with it, deliberately, and this is the one judgement worth flagging.** `base.css` carries the h1, h4, overline, nav and caption roles that every page design uses. The policy page cannot show its approved state without them, because its h1 comes from there. So they moved as part of this change set, which means **every page on the site now has a 33px h1 rather than 32**, including page designs the sweep has not reached. That is one pixel on the largest heading, it was inside the render he approved, and it is reversible in one line. Naming it rather than letting it be discovered.

## Proof

- `css_gate.py`: PASS on all stylesheets.
- Deployed to the build site at v0.64.0. `deploy.py` proved all three of its checks: server identical to local, zip matching the theme at 402 files, and the server reporting 0.64.0.
- Read back from the rendered live page with `getComputedStyle`, not from the stylesheet: h1 33, overline 12, meta 12, lead 18, h2 24, h3 21, body 16, list 16, table 14, table heading 14, end note 14. Every policy element on a step.
- The off-scale sizes still rendering on that page (11, 13, 15, 17, 19, 22) all come from the header, the footer, the cookie banner and shared components, which the brief sequences last. None of them is a policy element.

## The measurement, against the brief's section 1 table

The brief's working figures were 167 declarations moving, 140 already on the scale, 14 stylesheets. **Measured today: 318 declarations across 14 stylesheets, of which 137 were already on the scale and 178 were not.** The gap is real and is not a counting error: the S056 census predates the school pages and the card work of S060 and S061, so declarations have been added since. The brief accepted its figures as working numbers to be proved by the final report, and this is the first instalment of that proof.

**After this change set: 165 off scale, spread across the twelve stylesheets still to come.** Heaviest remaining are `cards.css` at 41, `about.css` at 24, and `knowledge-hub.css` at 21.

## One thing the artefacts disagree about, and how it was settled

`RULING__The_Nine_Step_Type_Scale_Approved_S056.md` section 2 says the approved page "keeps 14px and folds 13px into it". The generated stylesheet that actually produced that page, `previews/type-scale-override.css`, maps 13px **down to 12px**, and does the same for the other ties: 15 to 14, 17 to 16.

Both are true and they answer different questions. The ruling's sentence is about which of the pair became a step in the scale. The override is about where a declaration lands, and where a size sits an equal distance from two steps it rounds down.

**The override governed, because it is the artefact Kain's eye actually ruled on**, and re-deriving the ties myself would have been my judgement quietly replacing his. Recording it here because the ruling's wording will mislead the next reader, and the person who can correct the record is you, not me.

## What is next in the brief's order

The Knowledge Hub article and book note pages, then help, then About, reviews and testimonials, then header and footer last. Those page designs have **not** been through Kain's eye on this scale, so each one returns as the two column before and after comparison the brief requires, and none of them ships on the S056 approval.

*No em or en dashes in this file; checked before writing.*
