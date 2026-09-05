# SWEEP BRIEF: phone-tier conformance on the shared block separators

**From:** Claude Chat, S238. **Date:** 2026-08-04. **Signed by Kain:** S238.
**Answers:** your request in RECORD__Policy_index.md and RECORD__Page_about.md ("a sweep brief for phone-tier conformance across the shared separators"). This is the signed sweep brief; it authorises the change set below and nothing beyond it.

## The rule this sweep enforces

DSRD 7 §4.3, ruling 4: "The measurements are 48px on desktop and tablet, 32px on phones. Nothing else, at any width, on any page." The full §4.3 standard applies: one owner supplies the space (the element carrying the hairline owns the full measurement through its padding and margin), the deepest last child before the line and the deepest first child after it carry zero, and no page sets its own spacing values (ruling 2).

## The change set: two shared separators

1. **`.policy-body--ruled + .policy-body--ruled`** (components.css). Currently no phone tier, so the boundary reads 48/48 at phone. Add the phone tier so it reads 32/32 below 768px.
2. **`.help-popular`**. Same defect, same fix: 32/32 below 768px.

For both selectors, bring the separator to full §4.3 conformance at every width. Where either currently renders unevenly at desktop or tablet (48 above the line and 32 below), correct it to 48/48 there too, per ruling 4. Apply the fix on the shared component's own rule, in the pattern the conforming pages already use: a hand-written phone tier. Do not redefine the `--sp-2xl` token in base.css; a token-level change touches every page and is not authorised by this brief.

Also in scope: the components.css comment claiming no other template stacks the ruled wrapper is false (the Testimonials template stacks two adjacently). Correct or remove that comment so the code stops asserting something untrue.

## Out of scope

The About-page-local separators `.pfq` and `.tw-wrap` are excluded from this sweep. They are single-page changes and ride the About build change set to its signed spec (SPEC__About_Page_Locked_Structure_And_Copy.md, in FROM Chat).

## The pages this sweep touches

- Via the ruled pair: the Policies index, About, Testimonials.
- Via `.help-popular`: the help articles, the 404 page, the Policies index.

## Definition of done

1. Both selectors conform to DSRD 7 §4.3 at desktop, tablet and phone.
2. Each affected page re-gated with page_gate v3 on the hairline-spacing chapter (DSRD 6 §10), printouts filed through TO Chat.
3. The DSRD 6 records for the Policies index, About and Testimonials refreshed on that row.
4. No page-local spacing declarations added anywhere (§4.3 ruling 2).
5. The false components.css comment corrected.

*No em or en dashes in this file; checked before writing.*
