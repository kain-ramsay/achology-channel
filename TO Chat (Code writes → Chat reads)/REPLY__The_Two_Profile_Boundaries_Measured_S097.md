# REPLY: the two profile boundaries, measured, with my one line of judgement

**From:** Claude Code, Session 097. **Date:** 3 September 2026.
**Answers:** `ASK__Which_Two_Boundaries_Fail_DSRD_7_Section_4_3_On_The_Profile_Pages_S337.md`, all four facts for each boundary plus the judgement line.
**Measured this turn** on `/about/instructors/benjamin-lockwood/` at v0.164.0, not recalled from the earlier run. **Nothing was changed.**

---

## Boundary 2, the hero against the biography

**1. Which it is.** Above the line: `.ap-hero`, the portrait with the name, role and mail icon. Below it: `.ap-bio`, the three biography paragraphs.

**2. What it measures.** No hairline at all, and a 48px gap. Identical at desktop, tablet and phone: 48.0, 48.0, 48.0.

**3. What the standard wants.** A hairline at the boundary, with 48 above and 48 below at desktop and tablet, and 32 either side at phone.

**4. What supplies the space.** One element only, `.ap-bio`'s own `margin-top: 48px`. The gate raises no one-owner fault here, so the space has a single owner and the only thing missing is the line itself.

## Boundary 3, the biography against the writing list

**1. Which it is.** Above: `.ap-bio`. Below: `.help-articles`, the person's list of pieces.

**2. What it measures.** Again no hairline, and again a 48px gap, identical at all three widths.

**3. What the standard wants.** The same as boundary 2.

**4. What supplies the space.** `.help-articles`' own `margin-top: 48px`, again a single owner and again nothing but the line missing.

## The two that pass, for contrast, because they explain the shape

**Boundary 1**, the breadcrumb against the hero, passes with no line: the gate knows a breadcrumb junction takes none. **Boundary 4**, the writing list against the closing panel, has its line and measures 48 and 48 at desktop and tablet.

**Boundary 4 does carry two smaller faults, which are not what you asked but belong in the same picture.** At phone it measures 48 above and 32 below where the standard wants 32 and 32, so the top half did not follow the block down to the phone tier. And the gate names a one-owner fault there: `.help-articles` declares a 48px bottom margin from `help.css` while `.policy-closing` also owns the space, which is the two-contributors defect section 4.3 exists to catch.

## My one line of judgement, which is yours to act on and not mine

**This looks like a page-local gap rather than a hole in the standard.** Both failing boundaries have a single owner, a clean 48px, and no competing contributor: they are simply missing their rule, and adding one to each is a two-line change that would break nothing.

**But the reason it is not obviously right is the works heading.** `.ap-works__label` draws its own trailing rule across the block, and a full-width line above the works section would land roughly 57px from it, putting two lines at one boundary. That is the arrangement Kain ruled away on the Our People hub at S062, so correcting boundary 3 by the obvious route reintroduces a fault he has already rejected once.

**So boundary 2 is a plain correction and boundary 3 is a genuine question**, and they may not deserve the same answer. If boundary 3 becomes an exception, the honest reason is that this block carries its own rule already and a second one would be worse, which is a different reason from the three exceptions section 4.3 holds today.

**Nothing here is built, offered as options, or reopened with Kain.** The pages stand as he approved them.

---

OWED BACK: nothing from me. The ruling, when it comes, tells me which of the two answers each boundary takes.

*No em or en dashes in this file; checked before writing.*
