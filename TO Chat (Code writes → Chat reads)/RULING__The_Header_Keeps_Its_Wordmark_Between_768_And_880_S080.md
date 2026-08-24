# RULING: the header keeps the full wordmark between 768 and 880 pixels

**Ruled by:** Kain, in session, Session 080, 24 August 2026.
**Where:** Safari, on the tabbed comparison at `previews/header-logo-options.html`, built with `variant_tabs`, both panels carrying the header's real markup lifted from the rendered About page. One option on screen at a time, in the same pixels.
**His words:** "As it is now"

---

## What was put to him

Between 768 and 880 pixels wide the header shows the full "achology" wordmark beside the hamburger menu, because the logo swaps to the mark-only file at 768 while the navigation switches at 880. The two switch points are 112 pixels apart, so the header changes twice as the window narrows rather than once.

**Option A, as it is now:** the full wordmark at that width.
**Option B:** the mark alone, moving the logo's switch to 880 to match the navigation.

**He took A.** No code changes. The two switch points stay where they are.

## Why this needed ruling at all

**Nothing in any document records the mark-only logo.** DSRD 8 §18.2 specifies one logo asset at 32px. §18.15 says only that the "logo remains visible" below 880. The `<picture>` element in `header.php` swaps to `achology-logo-mark.webp` at `max-width: 767px`, and that behaviour was in the build with no ruling behind it.

Found at S080 while preparing the header sitting, by rendering the header at four widths rather than by reading the template.

## What Chat needs to write

**DSRD 8 §18.2 gains the mark-only variant**, which it does not currently carry: below 768px the header serves `achology-logo-mark.webp`, the phi mark alone, and above 768px it serves the full wordmark. Both are existing assets in the theme.

**§18.15 or §18.16 gains the consequence**, so nobody reads the 112px band as a defect later: between 768 and 879 the header carries the full wordmark and the hamburger together, and Kain ruled that state kept at S080 on the rendered comparison.

## What is NOT closed by this

**The header component itself is not yet approved.** This ruling settles one value inside it. The sitting's first question, whether the header holds as it is, is still open, and until he answers it there is no approved prototype and no data file. Both are written the moment he does, per the S282 commission.

*No em or en dashes in this file; checked before writing.*
