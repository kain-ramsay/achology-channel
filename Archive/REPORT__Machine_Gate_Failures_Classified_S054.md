# REPORT: the 34 machine gate failures, classified

**From:** Claude Code, Session 054. **Date:** 2026-08-11. **Theme:** v0.60.2.
**Answers:** `COMMISSION__Machine_Gate_Failures_Examination_S262.md` in full.
**Method:** the gate was re-run tonight against the live site, cache purged before measuring, rather than classified from the S053 numbers. Every classification below was checked against the CSS rule that produces it and against the governing sentence in DSRD 7 section 4.3, both read this turn.

## First, a correction to the commission's page list

The commission names the four pages as `/testimonials/` 4, `/about/instructors/` 6, `/help/` and its articles 11, `/pricing/` 11. Two of those are wrong and one is impossible, so the list below is the measured one:

| Page | Failures tonight |
|---|---|
| `/` (the homepage) | 11 |
| `/about/instructors/` | 6 |
| `/help/` | 11 |
| `/testimonials/` | 6 |
| **Total** | **34** |

`/pricing/` returns 404 and has never been built, so it carries no failures at all; its 11 are the homepage's. `/testimonials/` is 6, not 4. The total of 34 is right.

## The headline, before the table

**Only 11 of the 34 are defects, and they are all on `/help/`.** Twelve are one gate error repeated twelve times. Eleven belong to a page nobody has built.

## Classification, one row per failing item

### The homepage: 11 items, none of them a defect in a built page

| # | Check | Item | Classification | Reasoning |
|---|---|---|---|---|
| 1 to 6 | hairline-present | boundaries 1 and 2 at all three tiers | Not a built page | The homepage is a design-system smoke test. Its whole body is an H1 reading "The Achology design system is live", one paragraph, and one button, inside an inline-styled 720px main element. There is no page here to fail a page standard. |
| 7 | boundary-owner | boundary 2, firstOfB paddingTop 12px, declared by `.btn` in base.css | Gate error | The 12px is a button's own internal padding. DSRD 7 section 4.3 says the section governs "the separators between page-level blocks", and a button is not one. The checker is reading a control's padding as boundary spacing. |
| 8 to 10 | header-to-content | 80px at all three tiers, want 48 / 48 / 32 | Not a built page | The 80px is the placeholder's own inline `padding: 80px 24px`. It goes when the page does. |
| 11 | meta-description | 0 chars, missing | Real, but not a page defect yet | The placeholder has no metadata because it has no content. It becomes a defect the moment the homepage is built, and the words are Chat's to write. |

**What Kain should take from this page:** the homepage is not a page with eleven problems. It is a page that does not exist yet, and it is the largest single thing still missing from the site.

### `/about/instructors/`: 6 items, all one gate error

All six are `boundary-owner`, at boundaries 2, 3 and 4, reporting firstOfB marginTop 48px and firstOfB paddingTop 48px, both declared by `.pp-group` in people.css.

**Classification: gate error, one cause, six rows.**

The rule the gate is failing is this, in full:

```css
.pp-group {
	border-top: 1px solid var(--color-hairline);
	margin-top: var(--sp-2xl);
	padding-top: var(--sp-2xl);
}
```

`.pp-group` carries the hairline. DSRD 7 section 4.3's one-owner paragraph requires exactly this of the element that carries it: "The element carrying the hairline owns the full measurement. If it carries `border-bottom`, its `padding-bottom` is the space above the line and its `margin-bottom` is the space below; if `border-top`, the mirror."

So the 48 and the 48 are not a foreign contribution at the boundary. They are the line owner's own required space, and the same three boundaries pass `hairline-spacing` at 48 above and 48 below on the same run. Check 4 counts firstOfB marginTop and firstOfB paddingTop without first asking whether that element is the one carrying the line.

**What the check should test:** exempt the element carrying the hairline border at that boundary, on the side it carries it. Everything else about check 4 stands.

### `/testimonials/`: 6 items, the same gate error

All six are `boundary-owner`: boundary 3 from `.gi-block--rule-above` in global-impact.css, boundaries 6 and 7 from `.policy-closing, .policy-related` in about.css, marginTop and paddingTop in each case.

**Classification: gate error, identical cause.** Both rules carry `border-top` and both zero their bottom side deliberately:

```css
.gi-block--rule-above {
  padding-top: var(--sp-2xl);
  margin-top: var(--sp-2xl);
  border-top: 1px solid var(--color-hairline);
  padding-bottom: 0;
  margin-bottom: 0;
  border-bottom: 0;
}
```

These are line owners doing precisely what section 4.3 tells a line owner to do. One fix to check 4 clears all twelve rows across these two pages.

**One thing worth recording while this is open.** The reason these classes fail while other page-local blocks pass is that check 4 decides membership by harvesting class-shaped strings out of DSRD 8's prose with a regular expression. It recognises exactly 61 names tonight. `.about-grid` and `.about-proof__strip` are among them only because DSRD 8 section 12.1's table happens to spell them; `.pp-group` and `.gi-block--rule-above` are not, even though DSRD 8 section 21 IS the global impact block. So the check is really asking "does this class name appear in DSRD 8's text", which is not the question Chat's S227 ruling asked for, and DSRD 8 section 12 explicitly blesses page-local blocks it does not name. Worth fixing at the same time; the hairline-owner exemption is the one that clears the twelve rows.

### `/help/`: 11 items, and these are the real ones

| # | Check | Item | Classification | Reasoning |
|---|---|---|---|---|
| 1 to 3 | hairline-present | boundary 2, help-hero to help-group, all three tiers, gap 48px and no line | **Defect** | DSRD 7 section 4.3 ruling 1: "A hairline separates every pair of blocks. There is no block boundary anywhere on the site without one." The air is already right; only the line is absent. Fix: give `.help-group` the same `border-top` pattern `.pp-group` uses. |
| 4 to 6 | hairline-present | boundary 3, help-group to help-group, all three tiers, gap 48px and no line | **Defect, with one judgement flagged** | Same rule, same fix. **Flagged rather than decided:** whether two adjacent category groups are two page-level blocks or one block with internal group labels is Kain's call on the rendered page. If he rules they are one block, these three become a carve-out naming the help landing's category groups. Classified as defects because ruling 1 admits no exception and DSRD 8 does not name the group as a component. |
| 7 to 9 | hairline-present | boundary 5, help-popular to help-contact, all three tiers, gap 64px and no line | **Defect** | Ruling 1 again, and here the spacing is wrong too: 64px where ruling 4 pins 48 on desktop and tablet and 32 on phone. The 64 is `.help-popular`'s own `margin-bottom: var(--sp-3xl)`. |
| 10 | hairline-spacing | mobile boundary 4, help-group to help-popular: 48 above, 32 below, want 32/32 | **Defect** | `.help-group` carries `margin: 0 0 var(--sp-2xl)`, a fixed 48 with no phone tier, and it collapses against `.help-popular`'s 32, so the larger wins. Cleared by item 11's fix, not separately. |
| 11 | boundary-owner | desktop boundary 4, lastOfA marginBottom 48px | **Defect**, and the gate misnames its source | `.help-popular` carries the line and owns the space. `.help-group`'s own 48px bottom margin is a second contributor at the same boundary, which section 4.3 calls out by name: "A block that adds its own padding at a boundary is a defect even if the rendered total looks close." It reads correct at desktop only because adjacent margins collapse, which is exactly the trap that sentence describes. Fix: `.help-group` bottom margin to 0. **Secondary gate error:** the printout names `*, ::before, ::after in base.css` as the declaring rule, which is the universal reset setting margin to 0 and cannot be the source of 48px. The checker's `declaredBy` keeps the last matching rule it walks rather than the winning one, and its own comment already warns it can do this. The number is right; the attribution is wrong. |

## What this costs, which is what Kain asked

Three things clear the whole 34.

1. **One change to `page_gate.py` check 4:** exempt the hairline-carrying element's own space on the side it carries the line. Clears 12 rows across two pages and stops the same false failure appearing on every page built from here on. It is a change to the instrument every page is judged by, so it waits on Kain's word rather than going in with the page work.
2. **One small change set on `/help/`:** the hairline pattern at three boundaries, `.help-group`'s bottom margin to 0, `.help-popular`'s bottom spacing to the standard. Clears 11. One page, so one ordinary change set.
3. **Build the homepage.** Clears the remaining 11 by making the page real. Not a fix; the biggest unbuilt thing on the site.

## What I need back

**Two rulings from Kain, and nothing else.** Whether two adjacent `/help/` category groups are one block or two, and whether the check 4 change is authorised. The help fixes and the gate change are commissioned from his rulings on this table, per this commission's own bounds. No fix has been made.

*No em or en dashes in this file; checked before writing.*
