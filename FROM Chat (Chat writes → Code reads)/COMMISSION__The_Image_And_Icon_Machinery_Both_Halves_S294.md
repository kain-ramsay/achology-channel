# COMMISSION: the image and icon machinery, both halves

**From:** Claude Chat, Session 294, 20 August 2026
**To:** Claude Code
**Governing standard:** DSRD 7 sections **12.3** (The Image Delivery Standard) and **12.4** (The Icon Delivery Standard), both written this session. Read them from the canonical file before building. Nothing in this brief restates them; where this brief and the DSRD disagree, the DSRD governs.
**Board card:** the image and icon optimisation card.
**Approved by Kain, S294.**

---

## Why now, before the content run rather than after

The Knowledge Hub content run produces images at volume: roughly 500 book covers, 500 author portraits, 500 composite article banners, and around 8,000 OG images. A standard applied after that run means regenerating thousands of files. Applied now, they ship right by construction.

## Half one: the build-time pipeline

**What it does.** Takes a master (PNG, JPG or SVG) and produces the ship derivatives the standard requires, so nobody hand-exports a WebP at a guessed quality ever again.

**What it produces, per the standard:** the WebP derivative at the ruled quality, at 1x and 2x of the slot's specified display width, with transparency preserved, checked against that slot's file size budget.

**Where it does not guess.** A derivative is produced only for a slot whose display width is specified. Where no page spec states the width, the pipeline refuses rather than picking a size, which is the rule already applied to the held course and school page heroes in section 12.2.

**The compression numbers in section 12.3 are Claude's proposal, not Kain's ruling**, and the standard says so in place. Build the pipeline so the quality value is a single setting, not a number scattered through the code, because it will change once Kain has ruled it on a rendered hero.

## Half two: the page-gate checks

**These join the existing page gate rather than becoming a new one.** Each returns a pass, a fail naming the file, or a recorded exception.

**Per image on the page:**

1. Ships as WebP or SVG, matching the standard's two-format rule. A PNG or JPG in the theme is a fail.
2. Carries an `alt` attribute. Present and empty is a pass for a decorative image; absent is always a fail.
3. Alt text does not open with "image of" or "picture of", and is not the filename.
4. Carries `width` and `height` in real intrinsic pixels.
5. Carries a `srcset` and a `sizes` attribute.
6. Is inside its slot's file size budget.
7. Filename is lower case and hyphen separated, with no date, version number or export suffix.

**Per page, not per image:**

8. Every image below the fold carries `loading="lazy"`.
9. **The largest above-the-fold image carries no `loading="lazy"` and does carry `fetchpriority="high"`.** This one is the highest value check in the set: lazy loading the hero delays the exact file Largest Contentful Paint is measured on, and it is the usual reason a well-built page still fails its speed target.

**Per icon:**

10. Every icon renders through `achology_icon()` or one of the registries named in DSRD 7 section 5.2. A hand-written inline SVG that is not a recorded exception is a fail.
11. Every icon carries either `aria-hidden="true"` or an accessible name. Neither is a fail.
12. Every icon-only control carries an `aria-label`.

**The ten recorded drift pairs and the exempt groups in section 5.2.6 are recorded exceptions, never silent passes.** Report them by name, the same way the block-separator carve-out is reported.

## What to report back

**Through TO Chat, in one file.** The pipeline built and how it is run. The gate checks installed, with their acceptance printout. And the first run of the checks across the built site: how many images fail each check, which files, and the total weight the pipeline would save if the existing images were reprocessed.

**That last number is the one Kain will want**, because it says whether the built site needs a reprocessing sweep before launch or whether the standard only has to govern what comes next.

## What stops you

**A check that cannot be made mechanical.** Alt text describing the information rather than the picture is a human judgement; the gate can only test that alt exists, is non-empty where required, and does not open with a banned phrase. Build what is checkable, name what is not, and do not approximate a judgement check with a heuristic that will produce false failures at volume.

**Any disagreement between this brief and DSRD 7 sections 12.3 and 12.4.** The DSRD governs; write the question to TO Chat and carry on with the rest.

*No em or en dashes in this file; checked before writing.*
