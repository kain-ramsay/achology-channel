# RULING: the boundary above the enquiries panel is restored, and the S083 move is finished

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory, and that is part of what this file reports.
**Ruled by:** Kain, in the S097 sitting, having found the fault by eye on the rendered page and been shown the diagnosis and the two ways to fix it.
**His words:** *"yes, that makes perfect sense, thank you Claude - please go ahead"*, on the recommendation that the wrapper's styling move to sit beside the panel rather than the page being put back on the about.css list.
**Filed under Harness Rule 14.**
**Board card:** the Our People page card.

---

## What was wrong

The Our People page has had no line above its closing enquiries panel since S083, and nobody caught it until Kain looked at the page.

`template-our-people.php` wraps the panel in `<div class="policy-closing">` and its own comment says that class "carries the boundary above it". `.policy-closing` was defined in exactly one place, `about.css`, and **Our People stopped loading `about.css` at S083**, when `'instructors'` was taken off the enqueue list on the reasoning that the panel "now carries its own stylesheet and enqueues it itself".

**That reasoning was right about the panel and wrong by one class.** `.warm-room*` did move into `warm-room.css` and does self-enqueue, which is why the panel itself has rendered perfectly throughout. The wrapper that draws the line above it stayed behind. Every page taken off the list kept a perfect panel and silently lost its boundary.

**It is the S096 class of fault in its purest form: a change that looks like it worked.** The markup is right, the class is present, the template comment asserts the line is carried, nothing errors, and no gate measures a 1px line.

## What was done, v0.141.0

`.policy-closing` now lives in `warm-room.css` beside the panel it belongs to, moved verbatim with its comment. Nothing was retuned. `.policy-related` stays in `about.css`: it is the policy pages' block, those pages load that stylesheet for their own reasons, and the two only ever shared a selector.

**The same trap was checked for before the move, because this fix could have caused the fault it was fixing.** A page carrying the wrapper without the rule would lose its line. All three uses of `.policy-closing` (Our People, Testimonials, the Founders' Letter) call `achology_warm_room()` immediately inside the wrapper, and that function enqueues `warm-room.css` itself, so no page can hold the wrapper without the rule. There is no list to keep up to date.

## Proof

`css_gate` passes on every stylesheet. Deployed, cache purged, and all three of the deploy check's proofs green: server identical to local, zip matching the theme at 487 files, and the server reporting 0.141.0.

**Read off the live element in a browser, not off the file:** `border-top: 1px solid rgb(238, 237, 237)`, `margin-top: 48px`, `padding-top: 48px`, across the 880 column, served from `warm-room.css?ver=0.141.0`. That is the hairline standard exactly, 48 above and 48 below.

**The page for Kain's eye:** `https://achologytest.com/about/instructors/`

## One correction, made to Kain in the sitting

I told him this would repair the article page too. **It does not.** The article page closes with `achology_content_foot()` and carries no `.policy-closing` wrapper at all, so it has never had a boundary above its panel rather than having lost one. Giving it one is a change to that page's foot, which is not the page he was looking at, so it is named for the theme sitting rather than reached into here.

## No prototype version, and the reason

Rule 14's fold-back writes the approved state into the component's design folder as the prototype's next version **where the ruling approves how a component looks**. It does not apply here. Kain did not approve a new appearance; he ruled that a documented standard, already written and already ruled, should render again after eight sessions of not rendering. The prototype does not move because nothing about the design moved.

---

OWED BACK: nothing on the fix. The article page's own boundary is item three of the theme queue.

*No em or en dashes in this file; checked before writing.*
