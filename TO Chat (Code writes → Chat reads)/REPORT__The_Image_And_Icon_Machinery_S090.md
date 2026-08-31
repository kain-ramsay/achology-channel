> **CHAT DISPOSITION, S325:** listed at open, not read in full. Website workstream; S325 is an Educational Publishing System session. STAYS on one fact: the next website session, which opens by dispositioning this folder (S324 handover, register item 4).

# REPORT: the image and icon machinery, both halves, built and first run

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**Answers:** `COMMISSION__The_Image_And_Icon_Machinery_Both_Halves_S294`, all three things it asks to be reported back.
**Governing standard:** DSRD 7 sections 12.3, 12.4 and 5.2.6, read from the canonical file this session.
**Board card:** the image and icon optimisation card.

---

## Half one: the build-time pipeline

**`tools/image_pipeline.py` in the theme.** It takes a master and produces the WebP derivatives at 1x and 2x of the slot's specified display width, transparency preserved, each checked against that slot's budget.

```
python3 image_pipeline.py --slots
python3 image_pipeline.py --slot book-cover --width 180 --out ../images/ master.jpg
python3 image_pipeline.py --audit <folder>
```

**Four things are built in rather than remembered.**

**It refuses rather than guesses.** No slot named, no run. No display width given, no run, and the refusal quotes section 12.3's own sentence back: "A derivative is produced the day its slot's display width is specified, never before." There is no fallback size anywhere in the file, deliberately.

**The quality is one setting.** `QUALITY` at the head of the file, 82 for artwork and 75 for OG, with section 12.3's own note that these are Claude's proposal and not Kain's ruling written beside them. `--quality` overrides it, which is what the sitting where he rules it on a rendered hero will use. Changing the ruled value afterwards is one edit, not a hunt.

**Nothing is upscaled.** A master too short for its 2x derivative gets a named SHORT line and the 2x is not produced. An upscaled file reports a correct pixel count and looks soft, which is the defect the responsive rule exists to prevent.

**SVG is refused, not converted.** Section 12.3 ships line art as SVG because it is resolution independent; rasterising a logo is the defect the rule prevents, so a master handed in with an .svg extension is refused with that sentence rather than processed.

---

## Half two: the twelve checks

**`media_gate.py` beside `page_gate.py`, wired in the way `search_gate.py` already is.** They are not a new gate: every row lands in the page gate's own Result and its DSRD 6 record, so there is still one gate and one record. A failure to load the module is a FAIL row, never a silent skip, for the same reason the search block carries that guard.

All twelve are installed and all twelve are live:

| # | Check | Row name |
|---|---|---|
| 1 | ships as WebP or SVG | `image-format` |
| 2 | carries an alt attribute | `image-alt-present` |
| 3 | alt does not open "image of" and is not the filename | `image-alt-wording` |
| 4 | width and height in real intrinsic pixels | `image-dimensions` |
| 5 | carries srcset and sizes | `image-responsive` |
| 6 | inside its slot's file size budget | `image-budget` |
| 7 | filename lower case, hyphen separated, no date or version | `image-filename` |
| 8 | every image below the fold is lazy | `image-lazy-below-fold` |
| 9 | the largest above-the-fold image is not lazy and is fetchpriority high | `image-lcp-candidate` |
| 10 | renders through the registry | `icon-registry` |
| 11 | aria-hidden or an accessible name | `icon-hidden-or-named` |
| 12 | every icon-only control is labelled | `icon-only-control-labelled` |

**Checks 8 and 9 run at all three tiers**, because where the fold falls changes with the viewport, and check 9 is about the file Largest Contentful Paint is measured on, which is measured on a phone as well as a desktop. The other ten do not change with width and run once.

### The acceptance printout

`media_gate_acceptance.py`, **52 of 52 cases pass**, and every check is run in **both directions**: an input that should fail it and an input that should pass it, with both verdicts asserted. A file that only ever asserts failure proves nothing about the pass, which is the S050 and S089 lesson stated the other way round.

```
  1  ships as WebP or SVG ....... WebP passes / PNG fails / a Vimeo thumbnail is a carve-out
  2  alt attribute .............. alt="" passes / no attribute at all fails
  3  alt wording ................ ordinary passes / "Image of" fails / filename-as-alt fails
  4  width and height ........... matching passes / absent fails / a wrong shape fails
                                  / a 1x declaration beside a 2x file passes on ratio
  5  srcset and sizes ........... both pass / neither fails / an SVG needs neither
  6  budget ..................... under passes / over fails / an UNSLOTTED image is reported
                                  by name, never failed on a guessed budget
  7  filename ................... clean passes / upper case, a date, a version number, an
                                  export suffix and an editor resize suffix each fail
  8  lazy below the fold ........ lazy passes / eager fails
  9  the LCP image .............. correct passes / lazy fails / no fetchpriority fails /
                                  the LARGEST is the one judged / no image above the fold
                                  says so rather than going quiet
 10  the registry ............... the 24 grid at 1.75 passes / stroke 2 fails / the play
                                  triangle passes / Bootstrap, FAQ and the About era chart
                                  are named carve-outs
 11  hidden or named ............ either passes / neither fails
 12  icon-only controls ......... aria-label passes / hidden text passes / bare fails
 13  third-party markup ......... carved out and named, never failed, but the theme's OWN
                                  unnamed control still fails
```

### The recorded exceptions, reported by name

Section 5.2.6's exempt groups are carve-out rows, never silent passes and never fails: the footer social marks, the breadcrumb separators, the About era chart and signature, the /help/ audio control, the FAQ set's own registry, and the phi symbol.

**A page whose only inline SVGs are exceptions gets an INFO row saying so**, rather than a PASS reading "all 0 icons are correct", which is the shape of a check that cannot go red.

**One of those exceptions was written from the DSRD's words and matched nothing.** The About era chart's real class is `cons-stage__chart`, not anything containing "era chart", so the one drawing section 5.2.6 names by name was the single thing still failing check 10 on the first run. Read off the rendered page and corrected, with a case in the acceptance file so it stays corrected.

---

## The first run, and what it found

**Three pages, and it is a sample and named as one:** `/about/`, the home page, and `/help/what-is-achology/`. A full sweep runs every page through the SSH mirror with an axe scan each. Three pages is enough to show the pattern, and the pattern repeats identically on all three.

### Per check

| Check | /about/ (19 images) | home (10) | /help/what-is-achology/ (10) |
|---|---|---|---|
| 1 format | PASS | PASS | PASS |
| 2 alt present | PASS, 7 decorative | PASS, 7 decorative | PASS, 7 decorative |
| 3 alt wording | PASS | PASS | PASS |
| 4 width and height | **FAIL, 15 of 19** | **FAIL, 10 of 10** | **FAIL, 10 of 10** |
| 5 srcset and sizes | **FAIL, 19 of 19** | **FAIL, 10 of 10** | **FAIL, 10 of 10** |
| 6 budget | **FAIL, 2 over** | PASS | PASS |
| 7 filename | PASS | PASS | PASS |
| 8 lazy below fold | PASS, all tiers | no images below the fold | PASS, all tiers |
| 9 the LCP image | **FAIL, all three tiers** | **FAIL, all three tiers** | **FAIL, all three tiers** |
| 10 the registry | PASS after the chart fix | PASS, 23 icons | PASS, 42 icons |
| 11 hidden or named | **FAIL, 10 icons** | **FAIL, 3 icons** | **FAIL, 5 icons** |
| 12 icon-only controls | PASS, all 21 named | PASS, all 13 | PASS, all 14 |

### The four findings, in the order they are worth fixing

**One. Check 9 fails on every page at every tier, and it is the highest value line in this report.** Section 12.3 singles it out: "Lazy loading the hero delays the very file Largest Contentful Paint is measured on, which is the most common way a well-optimised page still fails its speed target." On /about/ the largest above-the-fold image is `about-achology-header.webp` and it is **lazy loaded and carries no `fetchpriority="high"`**. On the home page and the help page the largest above-the-fold image is the logo, which carries no fetchpriority either, and on the home page at phone width the dark logo is **lazy loaded**. Every one is a small edit.

**Two. Not one image on any of the three pages carries a srcset.** So every visitor on every device is served the same file: too heavy on a phone, or soft on a retina desktop. That is not a defect in any one image, it is the responsive half of section 12.3 not having been built yet, which is exactly what half one now makes possible.

**Three. Check 4 fails on nearly every image, in the same shape each time.** The attributes are there, so the layout does not shift, but they carry the rendered size rather than the intrinsic one: `achology-logo.webp` says 130x32 on a 405x100 file, the school squares say 44x44 on 96px files. The standard asks for real intrinsic pixels and CSS still controls the rendered size.

**Four. Check 11 fails on a small, repeating set of the theme's own icons**: the breadcrumb separator, the footer column chevrons, the stats and story-proof glyphs, the help popular badge. Ten, three and five on the three pages, and they are the same handful appearing on every page. Section 12.4's default is `aria-hidden="true"` and each of these sits beside a label that already carries the meaning, so the fix is one attribute in each of about six places.

### The number the commission asks for

**Reprocessing what already ships would save 2,496KB, which is 16.3 per cent, and that is a floor.**

- 284 image files in the theme measured, weighing **15,301KB** as they ship.
- Re-encoded at their own pixel size at WebP 82, they weigh **12,805KB**.
- 74 of the 284 are already at or under what re-encoding would produce, and are counted at their current size rather than made worse. A "saving" that would make a file bigger is not a saving.
- **97 files ship in a master format**, against section 12.3's two-format rule: 91 JPG and 6 PNG. The two worst are `manifesto-document.jpg` at 504.9KB, which would be 230.1KB, and `header-banner.png` at 399.0KB, which would be **39.3KB**, a tenth of its weight.

**Why it is a floor.** Nothing was resized, because a resize needs a slot's display width and section 12.3 forbids picking one. That rule does not stop applying because a run is only measuring. So this is the saving from **format and quality alone**, and every image served larger than its slot displays it saves more again once that slot's width is specified.

**So the answer to the question underneath the commission is yes: the built site needs a reprocessing sweep before launch**, and the 97 master-format files are where it starts. It is not urgent and it is not large: one pass of the pipeline once the slot widths are specified.

**One thing the audit found that no page check could, because those files are not on a page yet.** The testimonial background set, `Stacey-Q3-bg.jpg`, `Bea-Q1-bg.jpg` and about seventy like them, breaks the filename rule on the upper case alone. Cheap to rename now, expensive once anything links to them.

---

## One question for you, and it changed the code

**Does DSRD 7 section 12.4 govern markup this site does not write?**

The first real run failed /about/ ten times for the **consent banner's own glyphs**. Nobody here wrote that markup, it is on every page, and the only way to "fix" it would be to stop using Complianz. That is a false failure at volume, which the commission explicitly forbids, so it now takes the same treatment section 12.3 already gives a Vimeo thumbnail: **a carve-out naming the plugin, never a silent pass and never a fail.**

That is Code's judgement on a gap in the standard, taken under the commission's own instruction not to produce false failures, and it is named here rather than buried. **Section 12.4 does not say either way, and it should.** If the ruling goes the other way, one list in `media_gate.py` changes and the rows go back to failing.

---

## What is not checked, named rather than approximated

**Whether alt text describes the information rather than the picture.** The commission is explicit that this is a human judgement and must not be approximated with a heuristic. So check 3 tests the two banned openings and the filename case, both mechanical, and a separate INFO row states plainly that the wording itself was not machine judged, and how many images carry non-empty alt. It is a human line on the DSRD 6 record, not a score.

**Whether an image is in the right slot.** Where the slot cannot be named from the page, no budget is applied and the image is **reported by name** instead, so the list of things needing a slot is visible rather than a wrong budget quietly passing. Three or four per page on this run, mostly the logo.

OWED BACK: one ruling, not urgent. Whether a third-party plugin's own markup falls under DSRD 7 section 12.4.

*No em or en dashes in this file; checked before writing.*
