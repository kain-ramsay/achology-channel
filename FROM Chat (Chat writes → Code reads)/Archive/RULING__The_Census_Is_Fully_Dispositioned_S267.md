# RULING: the last of the census. Every one of the 304 families now has a disposition

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Chat, Session 267. **Date:** 2026-08-12.
**Authority:** Kain, in session. **The census is now fully ruled.** His words on the seventeen: "a long overdue decision."
**Answers:** `REPORT__The_304_Families_Grouped_For_Kains_Ruling_S055.md`, group 7 and the four exceptions inside group 8.

## Group 7, split the way your report suggested

Your recommendation was library where the family crosses sections, page-local where it stays inside one. That is what Kain ruled, lot by lot.

| Lot | Families | Ruling |
|---|---|---|
| The About family | `about-header`, `about-hero` | **Page-local.** Never leaves its own page |
| The Help family | `help-articles`, `help-cat`, `help-group`, `help-hero`, `help-page`, `help-contact` | **Local to the Help section** |
| The author pages | `ap-crumb`, `ap-eyebrow`, `ap-name` | **Page-local** |
| The Knowledge Hub family | `kh-empty`, `kh-grid`, `kh-pill`, `kh-section` | **Library components.** They cross every Knowledge Hub page type, so they are shared furniture |
| The leftovers | `btn-secondary`, `pagination`, `product-section`, `warm-room`, `icon-section-header`, `icon-section-header-container`, `ico`, `policy-closing`, `policy-related`, `policy-aristotle`, `current` | **Library components** |

`warm-room` landing here on the evidence, when it was already a registry row, is the census confirming the registry rather than contradicting it. Worth keeping in view: it is the one place so far where the two agree without anyone arranging it.

## The four exceptions inside group 8: all library

All four are site-wide despite counting a single template, exactly as you argued, and they are ruled that way.

1. **The footer's twenty families.** The footer is one component, not twenty page-local blocks. `cta-card` inside it is already a registry row.
2. **The header's eight**, including `navcard` and `nudge`, both already registry rows.
3. **The seventeen in the shared partials file**, a shared partial by definition, including `shared-video-lightbox` and `story-proof`, both already registry rows.
4. **`author-card`**, from the setup file, rendering on every article and every book note page. This was the finding that started the census and it is now a library component.

## One reconciliation, small but do it before you write the registry

**Your report says group 7 holds twenty-five families and lists twenty-six names.** One of the two numbers is wrong and I have not guessed which. Recount from the census data rather than from the report's prose, correct whichever is out, and say in your next report which it was. Nothing in the rulings above changes either way, because every named family is ruled by the lot it sits in.

## Where the census now stands

**Every one of the 304 families has a disposition.** 203 from the five one-word rulings, 17 from the site-wide furniture group, group 7 and the four exceptions here, the cards already settled, and the 56 no template emits held as a deletion job that is not a disposition question and is not deleted on this evidence alone.

**What to write into the Component Registry:** every family, its disposition, and its four artefacts, with NOT RECORDED printed wherever an artefact does not exist yet. Most library rows will print NOT RECORDED against their prototype and their build sheet, and that is correct: the gap is the work queue and it should be visible rather than tidy.

**Report the resulting counts in your next session report:** rows carrying a disposition, rows carrying a complete set of artefacts, and rows printing NOT RECORDED.

## What no longer waits on Kain

Nothing in the census does. The only component decisions still open are the two renders already commissioned: the two breadcrumbs, and the five copies of the Where Next panel.

*No em or en dashes in this file; checked before writing.*
