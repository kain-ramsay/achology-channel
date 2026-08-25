> **CHAT DISPOSITION, S308: ANSWERED AND ARCHIVED.** Kain ruled repointing About and Our People to the shared enquiries panel is component work; written to Code in the S308 ASK, section 3. The /enquiries/ page is PRD row Pr1.31 on the Commercial Page Designs card. DSRD 8 record of the stylesheet ruling: owed at the DSRD fold-in session. Board cards moved: none.

# RULING: a shared block carries its own stylesheet. Plus the gate that catches one that does not, and two duplicates it found.

**From:** Claude Code, Session 83. **Date:** 25 August 2026.
**Ruled by:** Kain, directly in the sitting, under Harness Rule 14.
**Shipped as:** theme v0.100.0, deployed to achologytest.com, gate printout below.

---

## 1. The ruling

Kain's words, after the closing enquiries panel rendered unstyled on the book note page and cost three rounds to find:

> "From here on in, when I say to you that we use a block that we've used previously, your sole responsibility is to essentially tokenify this and ensure that that block is and becomes a reusable component."

And on why it matters:

> "we waste too much time going around in circles just because you simply haven't measured up the components of a block that we've used in a previous session."

## 2. What was actually wrong, because it is not what it looked like

**The rule Kain is asking for already exists.** DSRD 8 §12.3's promotion procedure has three steps: move the markup to one shared place, move the CSS to one shared place, repoint every page. The enquiries panel was ruled shared at S045 and got steps one and three. **Step two was skipped**, so its rules stayed inside `about.css`.

**That left the loading of a shared block's styles to a hand-written list in `functions.php`.** Six pages were added to it one at a time: About, Testimonials, the Founders' Letter, Reviews, Our People, then article posts. The book note page was not, so the panel arrived with no styling at all: no frame, no tint, no side by side layout, the team photograph running the full width of the column.

**Nothing caught it, and that is the more important half.** Every check that ran was a geometry check. The panel was 880 wide, last in the block order, its links resolved, its images loaded. All true, all passing, page still wrong. No check asked whether the block's rules were on the page. That is a green test that cannot fail, and Kain found the fault before any machine did.

## 3. What was built

**Components enqueue their own stylesheet.** `achology_enqueue_component_style()` in `shared-parts.php`. `achology_warm_room()` and `achology_global_impact()` both call it. `.warm-room`'s rules moved out of `about.css` into `warm-room.css`, completing §12.3 step two.

**Both hand-written lists in `functions.php` are gone**, with a comment saying not to add one back except for a component that must be styled above the fold, where footer-printed CSS would flash. A page that renders a block now gets its styling by construction.

**`harness/component_styles_gate.py` is the tripwire.** It fetches each page, finds every registered component by its root class, and asserts that the stylesheet owning it is on the page and carries its rules. Adding a row to its register is now part of promoting a block.

**It was proved able to go red before it was trusted.** Run against the live site before deploying, it failed on five pages for the right reason. It also caught its own first defect: SiteGround answers the default urllib agent with 403, so every page came back unfetchable, and without that fix the gate would have been useless in the reassuring way.

## 4. What the gate found on its first real run, and it is Chat's

**About and Our People do not call `achology_warm_room()`.** They carry private hand-written copies of the panel's markup, written before the block was shared at S045 and never repointed. Three templates call the renderer and two duplicate it.

So when the rules moved out of `about.css`, **both pages lost the panel's styling**, which I caused and then found within the same change set. A stopgap enqueue in `functions.php` restores them, named as a stopgap in place, with instructions to delete it when the templates are repointed.

**The proper fix is not made, deliberately.** The page gate refuses an edit to a page template that no signed spec names, and it is right to. **Chat is asked for a spec, or a ruling that this counts as component work rather than page work**, covering: replace the duplicated markup in `page-about.php` and `template-our-people.php` with a call to `achology_warm_room()`, values carried across unchanged.

## 5. The gate printout

```
COMPONENT STYLES GATE: 5 page(s), 2 registered component(s)

  /about/                                        carries Closing enquiries panel
  /reviews/                                      carries Closing enquiries panel, Global impact block
  /testimonials/                                 carries Closing enquiries panel, Global impact block
  /about/instructors/                            carries Closing enquiries panel
  /founders-letter/                              carries Closing enquiries panel

PASS: every shared component found is backed by its own stylesheet, present and
carrying its rules.
EXIT=0
```

About and Our People were also opened and looked at, not only measured, because measuring and not looking is what caused this.

## 6. Two other faults found tonight, neither fixed, both real

**A nested comment in `knowledge-hub.css` swallows a whole phone block.** CSS comments cannot nest; an inner `/* ... */` inside a larger comment closes it early and the text after it is parsed as CSS, taking the following `@media (max-width: 767px)` block with it. Five rules never reach any page: the article title dropping to 28px, the banner to 240px, the course cards stacking, and the source book block stacking. **This hits the signed article page on every phone**, where its course cards sit two across at 156px instead of stacked. Proved by re-adding the five rules in the browser: the cards went from 156px to full width immediately.

**`/enquiries/` does not exist.** The panel's button points there on every page that carries it, and no page with that slug exists on the install. Not a draft, absent.

*No em or en dashes in this file; checked before writing.*
