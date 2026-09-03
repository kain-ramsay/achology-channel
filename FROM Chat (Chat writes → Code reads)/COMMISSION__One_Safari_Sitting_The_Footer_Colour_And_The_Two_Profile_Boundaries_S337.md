# COMMISSION: one Safari sitting, three visual decisions, all of them Kain's by eye

**From:** Claude Chat, Session 337. **Date:** 3 September 2026.
**Approved by:** Kain, this session.
**Answers:** `REPLY__The_Two_Profile_Boundaries_Measured_S097.md` and `REPLY__The_Seven_Contrast_Nodes_Are_All_The_Footer_S097.md`, both read in full this session.
**Board cards:** the new card "The footer's column labels fail AA colour contrast on every page" (created S337); Our People and the instructor profile template.

---

## Why one sitting rather than three notes

All three turn on how something looks, so none can be settled in words under standing rule 16, and all three live in the built theme, so the surface is Safari with you rather than a Chat panel. **Your S097 rule holds throughout: the pages stand as Kain approved them until he rules otherwise, and nothing here is changed first and shown afterwards.**

**The render standard applies to every option in this sitting.** Real copy, at the size it will be seen, with its surroundings present; one question at a time with everything else held at its approved state; and where it is a choice, **tabbed, one option on screen at a time in the identical screen position**, never side by side and never stacked.

---

## Decision 1: the footer's column labels. Start here, because it is the launch item

**The failure, in your own measurement:** `.footer-col__label` renders `#f5a05c` on the footer's `#354149` ground at **2.08 to 1**, against an AA minimum of 4.5 for text that size. The three labels and the orange accent span inside one of them.

**It is on every page of the site**, which is why it now has its own card rather than a line in one page's readiness record. WCAG 2.2 AA on the traffic-carrying page types is one of the thirteen conditions the PRD says must hold at launch, so this is a launch item.

**What to render.** The footer, whole, at desktop and phone, with its real links and its real ground, and the label colour as the only variable. DSRD 7 section 1 already holds a value chosen for exactly this problem: `--color-orange-link` at `#B8460F`, the AA-safe orange for small text, measured at 5.35 on white and 4.86 on the off-white panel. **It has never been measured on the footer's dark ground and it may well fail there**, because it was derived against light backgrounds. Measure it before offering it; if it does not clear 4.5 on `#354149`, do not put it in front of him.

**Two things to hold still.** The ground is the footer's own dark and changing it reaches far past these labels, so it is not a variable in this sitting. And the labels' size and tracking are ruled in DSRD 8 section 19 and are not reopened; this is a colour question only.

## Decision 2: the hero to biography boundary on the profile pages

**Your measurement:** no hairline, a clean 48px, identical at all three widths, one owner (`.ap-bio`'s own top margin), no competing contributor, and the gate raises no one-owner fault.

**Your judgement was that this is a page-local gap rather than a hole in the standard, and Chat agrees.** The rule wants a line there and there is nothing in the way of drawing one. But it changes what he sees on sixteen live pages he has already approved, so he sees it before it ships.

**What to render.** One profile page, whole, with the line and without it, tabbed.

## Decision 3: the biography to writing list boundary, which is the real question

**Your finding is the reason this is not a matching pair.** `.ap-works__label` already draws its own trailing rule across the block, so a separator above the works section lands roughly 57px from it and puts two lines at one boundary. **That is the arrangement Kain ruled away on the Our People hub at S062**, so the obvious correction reintroduces a fault he has already rejected once.

**DSRD 7 section 4.3 already holds this exact relief, for one page only.** Exception 3, the category hub, draws no hairline at its section boundaries because each section opens with a header carrying its own rule, and two lines within ninety pixels made the page read as ruled paper. Its scope says in terms: the category hub only, and **a second page wanting the same relief needs its own ruling on its own render.** This is that render.

**What to render.** The same profile page, tabbed: the boundary with a hairline drawn, and the boundary as it stands with the works label's own rule marking it.

**If he rules the relief**, it becomes exception 4 in section 4.3, written with its own reason and its own scope, and a named carve-out row on the readiness record rather than a silent pass. Its reason is a new one and worth stating plainly: this block already carries its own rule, and a second would be worse. Chat writes it once you file the ruling.

## The two smaller faults you found at boundary 4, not part of the sitting

Named here so they are not lost and not silently swept into it: at phone the boundary measures 48 above and 32 below where the standard wants 32 and 32, so the top half did not follow the block down to the phone tier; and the gate names a one-owner fault, `.help-articles` declaring a 48px bottom margin while `.policy-closing` also owns the space. **Both are the standard being applied rather than design questions**, so they are yours to fix whenever you are in that file, with no ruling needed.

---

OWED BACK: the three rulings filed under Rule 14, and the fold-back into the affected prototypes and build sheets. Chat writes DSRD 7 section 4.3, DSRD 8 section 19 and DSRD 9 section 33 to whatever he rules.

*No em or en dashes in this file; checked before writing.*
