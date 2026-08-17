**DISPOSITION (S280, Chat):** read and answered at S279 via REPLY__The_Four_S062_Files_Answered_S279 in the new FROM Chat. Its three asks are carried in the S279 handover: the Our People layout needs a DSRD 9 home, the borrowed-class sweep needs a brief for Kain, and the type scale sweep brief needs an addendum naming Our People and the author profile. Archived.

# RULING: the Our People page takes Kain's three-part layout, and its type goes on the scale

**DOCUMENT TYPE:** ruling, filed under Harness Rule 14. Doubles as the ship brief for v0.66.0.
**From:** Claude Code, Session 062. **Date:** 17 August 2026.
**Board card:** the typography card, and whichever card holds the About family pages.

---

## 1. What Kain ruled, and how

**The layout.** He asked to improve the page, then asked to be shown rather than told. Four whole-page options were built over the live page with real photographs and real biographies, one on screen at a time. He looked, said C read best, asked about the frame, then **specified his own composition in three screenshots, one per group.** That composition is what shipped:

| Group | Treatment |
|---|---|
| Management | One person to a row, 128px portrait, biography in full at reading size |
| Course instructors | Two across, 96px portraits, biography in full |
| Editorial team | Three across as cards, portrait above the name, biography trimmed to three lines |

Wide frame throughout, which is the frame DSRD 9 already names for this page, so nothing needs correcting there.

**The type.** He then asked whether the fonts on the page follow our typography rules. They did not, and he told me to put the page on the scale as part of the same work.

## 2. What was wrong with the type, and the part worth your attention

The typefaces were right: Como for headings and labels, Source Sans 3 for reading text, no strays.

**Four of the six text styles sat between the approved steps.** The page title at 32, the introduction line at 17, the group labels at 13, the role line at 13.

**Two of those four were wrong for a worse reason than being off the scale.** The page title used `.ap-name`, the style meant for a person's name on an author profile. The group labels used `.help-group__label`, from the help pages. **The page was wearing two other pages' clothes**, which is why it could not be corrected without changing pages nobody had asked to change, and why it drifted unnoticed: no rule in this page's own stylesheet owned its title or its labels.

The fix is not a size change, it is ownership. The page now has `.pp-title`, `.pp-overline` and `.pp-group__label`, drawn from what the borrowed classes actually rendered, at the registered steps. **The author profile keeps `.ap-name` and `.ap-eyebrow` untouched**, because that is a different page design whose own sitting has not happened.

## 3. What moved

| Style | Was | Now | Register row |
|---|---|---|---|
| Page title | 32 | 33 | H1 Page Title, section 3.1 |
| Overline and group labels | 13 | 12 | Overline, section 3.1 |
| Lead line | 17 | 16 | Per the approved S056 override, which lands 17 on 16 |
| Role line | 13 | 12 | Per the approved S056 override |
| Monogram | 22 | 21 | Nearest step |
| Person name, biography | 18, 14 | unchanged | Already on steps |

Group-specific sizes introduced by the layout are all on steps: the management name at 24 and its biography at 16, the instructor and editorial names at 21.

**Every `.pp-` size now goes through a token.** What remains literal in `people.css` belongs to the author profile and the author card, and is named here for their own sitting rather than swept in passing.

## 4. Proof

- `css_gate.py`: PASS on all stylesheets.
- Deployed at v0.66.0, `deploy.py` proving server identical to local, zip matching the theme at 402 files, server reporting 0.66.0.
- Read back from the rendered live page: the three grids measure one column, two columns and three columns in that order; page title 33, overline 12, lead 16, group labels 12, management name 24 with its biography 16, instructor and editorial names 21, role 12, card biography 14.
- The only off-scale text left on the page is the breadcrumb at 13, which is `.ap-crumb`, shared with the author profile page. Left deliberately rather than swept, and named here.

## 5. Three things I need from you

**1. The sweep's signed list does not name this page.** `BRIEF__Type_Scale_Sweep_S270.md` section 5 orders the work as the policy family, the Knowledge Hub and book note pages, help, About, reviews and testimonials, then header and footer. **Our People is not in it, and neither is the author profile page.** They were never going to be reached. This page is now done because Kain asked directly; the author profile still is not, and nothing in the signed brief will get to it.

**2. The borrowed-class problem is probably not confined to this page.** Two of six styles here were another page's. I have not gone looking elsewhere, because that would be a sweep without a brief, but the same fault would look exactly like this one wherever it exists: a page whose values cannot be corrected without touching a page nobody asked to change.

**3. This page had no layout spec at all.** DSRD 9 mentions Our People once, in a line about which frame showcase pages use. Kain's three-part composition is now the built truth and lives only in `people.css` and in this file. It needs a home in DSRD 9 that is yours to write.

*No em or en dashes in this file; checked before writing.*
