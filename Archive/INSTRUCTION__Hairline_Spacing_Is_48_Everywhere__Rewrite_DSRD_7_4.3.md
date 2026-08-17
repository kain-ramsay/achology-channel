# INSTRUCTION: hairline spacing is 48 everywhere. Rewrite DSRD 7 §4.3.

**From:** Claude Code · **Date:** 2026-07-27 · **Priority: do this before any
other DSRD work.**

## The decision

Kain settled this previously and restated it on 2026-07-27, in his words:

> "There will always be forty eight above and beneath every single hairline
> through the entire website as a matter of standard."

**One value. 48px above every hairline, 48px below every hairline. Every page,
every width, no exceptions, no tiers, no per-page judgement.**

## Why this is urgent

This decision has now been missed on multiple occasions, because it was agreed
in conversation and **never written into the DSRDs**. DSRD 7 §4.3 as it stands
says the opposite in two places, so every session that reads it in good faith
applies the wrong rule. That happened again today and cost hours.

Until §4.3 is rewritten, the spec actively contradicts the standard. This is
not a tidy-up. It is the fix for a repeat failure.

## What §4.3 currently says that must go

1. **The dense-page tier.** §4.3 currently states: *"Where a page separates
   every section with a hairline, both measurements are 32px instead, at every
   width."* **Delete this entirely.** Do not soften it, do not keep it as an
   exception, do not leave it as a historical note. Any surviving mention of a
   32px tier will be read and applied.
2. **The counting test.** §4.3 currently instructs the reader to *"count the
   section boundaries on the page, and count the hairlines"* to choose a tier.
   **Delete this too.** There is no tier to choose, so there is nothing to
   count. This test is what produced today's wrong answer.
3. **The mobile reduction, for hairlines only.** §4.3 currently says both
   measurements *"become 32px below 768px"*. Kain's standard is 48 at every
   width. **Delete the reduction for hairline spacing.** Note carefully: the
   general spacing scale in §4 keeps its `2xl → 32px below 768px` mobile
   reduction for everything else; only the hairline rule is exempted from it.
   Say that explicitly so the two are not confused.
4. **The S216 provenance line.** §4.3 cites *"Settled S216 on the rendered Code
   of Ethics page … 18 July 2026"* as the authority for the 32px tier. Replace
   it with Kain's decision, so the document's own audit trail points at the
   right ruling.

## What §4.3 must say instead

Write it so a reader cannot construct a second answer. It needs to state, in
one short unambiguous block:

- Content edge to line: **48px**. Line to content edge: **48px**. At every
  width, on every page. Use `var(--sp-2xl)`.
- **No page may set its own value.** Where a page or template currently
  declares its own hairline spacing, that declaration is deleted so the page
  inherits the standard. A page-local override is a defect, not a variant.
- **Scope.** This governs section hairlines: a 1px rule separating one page
  section from another. It does **not** govern rules inside a DSRD 8
  component — a card footer, a card's stats row, a pricing divider — which
  keep their own specified values. (§4.3 already draws this line and it should
  survive the rewrite unchanged, because Kain confirmed it on 2026-07-27.)
- **The element carrying the line supplies all the space.** Keep the existing
  paragraph on this, and keep *"everything touching the line supplies zero"*.
  Both are correct and both still apply.
- **Verification.** Keep the existing instruction to measure in the browser at
  desktop and phone, but change the expected reading to 48 at both.

## Also check and reconcile, do not assume

This missed decision may have propagated. Please search every DSRD and fix or
flag each hit, rather than assuming §4.3 is the only home:

- Any other reference to a 32px hairline, a dense page, a densely ruled page,
  or a hairline tier, anywhere in DSRD 6, 7, 8 or 9.
- **DSRD 6 §10**, which §4.3 names as the page gate enforcing this. The gate's
  wording must check for 48, not for "the page's tier".
- **DSRD 9 §26** (Header-to-Content Spacing, LOCKED). This is a separate rule
  and stays as it is, but confirm its wording cannot be misread as licensing a
  32px hairline on mobile.
- **DSRD 8 §12.4**, the Related Questions block, which §4.3 currently names as
  a block arriving with its own 48px standard. That is now simply the standard,
  so the sentence granting it an exception should go.
- Any page-layout spec in DSRD 9 that states a hairline value for a specific
  page.

## Where the rule must live so this cannot recur

Kain's point is that this has been missed repeatedly. So beyond the rewrite:

- Put the single sentence at the **top of §4.3**, not buried after the
  discussion, so a skim-read lands on it.
- Make sure the **page readiness gate (DSRD 6)** would fail a page that used
  any other value, so it is caught mechanically rather than by memory.
- If there is a design-foundations summary or quick-reference anywhere in the
  DSRD set, put the one sentence there too.

## What I am doing on the build side

I am sweeping the theme now: every section hairline and the breadcrumb gap to
48 above and below, at every width, with page-local overrides deleted rather
than edited so nothing can drift again. I will file a ship brief when it lands.

**Known non-conforming before the sweep:** the breadcrumb sets 32 below itself,
so the gap under it is 32 while the hairline below the header is 48 — which is
the visible inconsistency Kain spotted on /testimonials/. The About page and
the whole policy family run 32/32 at the doc header. /testimonials/ already ran
48/48 and was correct.

I do not edit DSRDs, which is why this is coming to you rather than being done
directly. Please confirm back when §4.3 is rewritten.
