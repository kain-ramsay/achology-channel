# REPORT: the typography census, part 1. The theme declares 122 type styles where DSRD 7 registers 50.

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Answers:** `COMMISSION__The_Typography_Census_And_Its_Specimen_Page_S267.md`, part 1.
**Part 2, the specimen page, is built and is section 9 of this file.** Kain rules from that page, not from these numbers.

**Harvested from the theme's own stylesheets, never from a document**, exactly as the component census was. Sixteen stylesheets, 11,504 lines.

---

## 1. The count

| | |
|---|---|
| Registered in DSRD 7 section 3 | **50** (26 Como, 24 Source Sans 3) |
| **Distinct whole type styles actually declared** | **122** |
| Of those, matching a registered style | **55** |
| **Of those, NOT registered** | **67** |

A whole style means size, weight and line height together, as the commission requires: a registered 17px at weight 600 and an unregistered 17px at weight 500 are two rows here, never one.

**The shape is the same as the component census, and milder.** That found 304 class families against 42 named. This finds 122 styles against 50 registered. Two and a half times over, rather than seven.

### The three properties separately

| | Distinct values | Declarations |
|---|---|---|
| font-size | **33** | 322 |
| font-weight | **5** | 229 |
| line-height | **18** | 132 |

**Every size in use, largest first, with its declaration count:**

115.85(2) 105.85(2) 105.26(1) 104.97(1) 104.4(1) 104(2) 85.11(1) 83.79(1) 56(2) 42(2) 40(1) 36(2) 34(4) 32(7) 28(7) 26(5) 24(16) 22(4) 20(14) 19(5) 18(8) 17(24) 16(30) 15(20) 14(47) 13(45) 12.5(8) 12(30) 11(24) 10.5(3) 10(1), plus one `inherit` and one `0`.

**The five weights, and what each carries:**

| Weight | Declarations | Sizes it appears at | Class families |
|---|---|---|---|
| 400 | 48 | 9 | 32 |
| 500 | 30 | 9 | 20 |
| **600** | **97** | **14** | **59** |
| 700 | 35 | 16 | 25 |
| 800 | 4 | 3 | 4 |
| **not set at all** | **108** | 24 | 65 |

**The most useful line in this report is the last one.** In 108 declarations the weight is not stated, so the type inherits whatever it lands in. That is nearly half of all sizing declarations carrying no weight decision at all, which is worth knowing before any rule about what a weight means is written.

---

## 2. The seven sizes nobody would guess, and they are all one component

The largest type on the site is not a heading. Seven of the eight largest sizes belong to a single decorative watermark on the policies index:

`115.85px`, `105.85px`, `105.26px`, `104.97px`, `104.4px`, `85.11px`, `83.79px`

Every one is a `.policy-index__row[data-word="..."]::before`, a per-word watermark tuned individually so each policy name fills the same visual space. Eight bespoke sizes to two decimal places, none registered, none reusable.

**Named, not judged.** The commission says if a style is plainly wrong I name it and leave it, and this may be exactly right for what it does. But it is the clearest example of what the census is for: nobody reading DSRD 7 would know these exist.

---

## 3. Where the scale collapses

**The register's own sizes run in an unbroken chain from 20px down to 10px with no gap wider than 1px**, and the code follows it:

20 and 19, 19 and 18, 18 and 17, 17 and 16, 16 and 15, 15 and 14, 14 and 13, 13 and 12.5, 12.5 and 12, 12 and 11, 11 and 10.5, 10.5 and 10.

**Twelve consecutive pairs one step apart.** Between 20px and 10px there are eleven distinct sizes carrying 232 declarations. That is not a scale, it is a continuum, and it is why the commission expects the specimen page to put near neighbours side by side.

The heaviest concentration is in the middle: 14px (47 declarations), 13px (45), 16px (30), 12px (30), 17px (24), 11px (24).

The odometer sizes cluster the same way at the top: 104, 104.4, 104.97, 105.26, 105.85 are five distinct sizes within two pixels of each other.

---

## 4. The responsive gap, measured

| | |
|---|---|
| Styles declared outside any media query | 117 |
| Styles that exist only inside one | 5 |
| **Distinct sizes with no responsive variant anywhere** | **28 of 32** |

**So 28 of the 32 real sizes on this site are the same on a phone as on a desktop.** The five media-query-only styles are the phone variants of the book note hero, the help hero, the article heading, the Knowledge Hub hub and listing headings, and the consent counter.

The register itself only states responsive behaviour for four styles: the Odometer Digit, the Featured Testimonial Quote, the Chapter Question and the Counter Caption. The code matches that. **This is a gap in both, not a drift between them**, which makes it a design decision for Kain rather than a correction.

---

## 5. Four registered styles that are not in the code at all

These are named in DSRD 7 section 3 but no stylesheet declares a matching size, weight and line height:

1. **AAA/Membership Header Title** (26px / 700 / 1.3)
2. **Chapter Numeral** (46px / 800 / 1)
3. **Chapter Question** (26px / 600 / 1.3)
4. **Pull Quote** (18px / 400 italic / 1.6)

**Reported as found, not diagnosed.** There are innocent explanations for each: the AAA and membership cards are among the five commerce components not yet reviewed, and the Chapter Numeral and Chapter Question were built for Member Testimonials, whose stylesheet may express them differently than the register records. The Pull Quote is registered for the quiet text-led pages. **I have not chased any of them, because the commission is a measurement and chasing four specifications is a different job.** They are listed so Chat can decide whether they are stale register rows or genuinely missing builds.

---

## 6. Traceability and tokens, both as the commission asked

**Traceability: 121 of 122 styles trace to a class family.** The single exception is `input, textarea, select { line-height: inherit }` in the base stylesheet, which is a form reset rather than a type style. Printed as untraceable rather than left looking complete.

**Tokens: only three type values on this whole site are written through a custom property**, and all three belong to one component:

- `--said-size = 24px`
- `--said-weight = 500`
- `--said-leading = 1.5`

That is the said block, DSRD 8 section 15. **Everything else is a literal number typed into a rule.** Worth stating plainly, because a scale cannot be enforced through tokens that do not exist, and the mechanical check the commission looks forward to would need them.

**No type is set inline in any PHP template.** Zero declarations across all templates, so the stylesheets are the whole truth.

---

## 7. How the instrument was proved before its answers were used

The parser was made to fail before it was believed, on Kain's standing requirement. Twelve checks against a sample stylesheet with known contents, including four negative controls:

- finds a plain declaration, and one inside a media query
- resolves `var(--x)` and reports the token beside its resolved value
- marks a media-query-only style as such, and does not mark others
- traces `.beta__title` to the family `beta`
- **does not count a commented-out value**
- **does not count a weight inside `@font-face`**
- **ignores a rule with no type properties**
- **strips `!important` without eating the value, and keeps `inherit` whole**

**The last check exists because the first run got it wrong.** `str.rstrip("!important")` strips a character set rather than a suffix, so it silently turned `inherit` into `inhe`. It appeared in the first output as a size called `inhe` and was caught by reading the result rather than by any test. The test now exists so it cannot come back, and the fault is recorded here rather than quietly fixed, because a parser that corrupts values ending in those letters would have been wrong in ways nobody would have questioned.

---

## 8. What is not in this report

**No judgement on which styles should go.** The commission is explicit that I measure and render, and Kain decides.

**Nothing changed.** No value corrected, removed or unified. The theme is exactly as it was.

---

## 9. Part 2: the specimen page, built and open in Kain's Safari

**The link:** `https://achologytest.com/wp-content/themes/achology/previews/type-specimen.html`

All 122 styles, each shown once, split into the 55 registered and the 67 not, ordered largest first inside each so near neighbours land beside each other, at desktop, tablet and phone width simultaneously.

**The words are real and none are invented.** They were harvested from the live site this session by walking ten pages, including the key-protected card workbench, and reading the actual text each selector renders. Where no live rendering could be found, **the row says so in red and shows nothing**, rather than filling the gap with sample text nobody decided. That is 43 of the 122.

**The type is real, not a reproduction.** The page loads the theme's own stylesheets from the live site and rebuilds each style's real class chain, including the base class behind every BEM modifier, so the genuine rules and the genuine media queries apply. Nothing about the type is hand-written into the specimen.

### It was proved rather than assumed, and the first two attempts were wrong

**Measured, not eyeballed:** every row's rendered font size was read back with `getComputedStyle` and compared against the size the census says it should be. **73 of the 78 measurable rows match exactly.**

**The five that did not match are the proof the page works.** They are all responsive styles, and at desktop width they correctly showed their desktop size while their label named a phone size. Re-measured at 375px, every one renders at its phone value: the book note title reads 42px at desktop, 34px at tablet and 28px at phone, in the three columns side by side. **A style with no responsive behaviour is identical in all three columns, which is what makes the responsive gap visible at a glance rather than as a number.**

**Two faults were caught and fixed by that checking, neither of which would have been visible by looking:**

1. **The first measurement pass read the wrong element**, taking the outermost node of each reproduced chain rather than the styled innermost one. It reported 28 mismatches, all of them false. Fixed by walking to the deepest element and, for the watermark rows, measuring the pseudo-element.
2. **Several specimens floated over the page.** The consent banner, its manage-consent tab and the policy index watermark are fixed or absolutely positioned on the live site, and they inherited that here, covering the rows beneath. Position is now neutralised inside a specimen only. **No type property is touched**, which matters because type is the only thing this page measures.

A build stamp now travels on the three column URLs, because a rebuilt specimen was once served from cache and showed the previous version.

### One finding the page surfaces that the count alone did not

**Eight of the 122 styles are carried only by classes Kain already ruled dead at S266** and which are awaiting deletion: the `fa-`, `fam-`, `x5-` and `sd-note` families. They are flagged in red on the page.

**This is worth knowing before he rules**, because those eight will disappear on their own when `COMMISSION__Delete_All_35_About_CSS_Dead_Classes_S266` runs. Ruling on whether they earn a place would be ruling on something already deleted.

### Where it lives, and why it is not on localhost

The previews README records the ruled route as serving locally over `python3 -m http.server`. **That would not bind in this environment**, and a localhost link would die with my session in any case, leaving Kain with a dead address.

So the two files sit on the build site under the theme's `previews/` folder. That folder is on `deploy.py`'s exclude list, which means rsync neither sends it nor deletes it, so what is there now survives every future deploy and is not disturbed by one. **The files are also in the theme repository**, so they are version controlled like everything else.

**Chat may want to correct the previews README** on that point: its localhost instruction is the only route it names, and a live path under the excluded folder is both more durable and reachable by Kain without me running anything.

### What Kain rules from it

The four questions the commission names, in the order the page makes them answerable: which unregistered styles earn a place, which registered ones are duplicates of each other pretending to be different jobs, what each weight means on this site, and what happens on a phone.

**Nothing on that page changes anything.** No value corrected, removed or unified, and the theme is exactly as it was.

*No em or en dashes in this file; checked before writing.*
