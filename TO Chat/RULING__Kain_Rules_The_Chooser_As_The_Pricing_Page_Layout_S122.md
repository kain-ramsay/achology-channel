# RULING: Kain rules The Chooser as the pricing page's layout, and the page is rebuilt phone first

**From:** Claude Code, S122, Wednesday 17 September 2026. **To:** Claude Chat.
**Board card:** Pricing page (PRD Pr1.19).
**Session type:** theme.

**DOCUMENT TYPE: not a page spec.** It files rulings and specifies no page.

## Why there were four whole layouts rather than four options on a component

Kain stopped the component-by-component work, in his own words:

> "I feel like I'm trying to brush up bricks and boulders with a broom, in a really big room. I like this page infrastructure, but you haven't given any thought to the structures. Like you took the pack that I gave you and just built it without giving any thought whatsoever to how this page actually needs to be structured ... rather than keeping on pushing on this one component, I want you to deliver me four completely separate brand new start from scratch page layouts as if you were a competent web designer offering me four paths or four directions to take this page in ... I've spent three hours on this one opening block with you ... the responsiveness on tablet and mobile is absolutely diabolical. It's not working ... I want every single one of them to be thought through from responsiveness level before you even start."

Four whole pages were built and rendered: The Chooser, The Ladder, The
Comparison and Catalogue First.

## The ruling

> "i definately prefer the Chooser option. Lets start working to improve this please."

**The Chooser** is the pricing page. The page is a decision and makes it on the
first screen: four choice cards, each carrying what it is, what it costs, what
the money buys and how long the community access lasts, in that order every
time; then each choice's own section in the same order as the cards.

**The three that lost are deleted rather than parked**, with everything that
served only them. They are in the theme's history at v0.462.0.

## Two earlier rulings from the same sitting, both now superseded by this one

Both are recorded because they were his and they were acted on, and because what
replaced them replaced them on his word, not on Code's judgement.

- **The opening band's artwork takes the words' height** ("I want the Fits the
  words option please!!!!!"), filed separately at S122 and shipped at v0.462.0.
  The Chooser has no opening band, so the band and the artwork are both gone.
- **The jump strip repeated the band.** His finding: "It seems that these two
  opening parts of the page are doing the same thing?" Read off the rendered
  page, four of its five links went to the same four places as the band's own.
  The Chooser has no jump strip.

**One thing for Kain, not for Chat to settle:** his own price-tag artwork, drawn
S365 and ruled into the band at S121, is not on The Chooser. It was on screen in
none of the four layouts he chose from, so the ruling stands as given; whether it
returns is his, and it is put to him in the sitting.

## What changed underneath, which is the part he actually asked for

The page is written **mobile first**. The plain rules are the phone and width is
added at 768 and 1024 (DSRD 7 section 4.1's own table calls the mobile tier
"default styles (mobile-first)"). The page it replaces was written the other way
round, which is why every width needed a patch. Everything below the tap-target
size was found and fixed: every button and link clears 44px on a phone, the
control bar is one column, a course row puts its two actions on their own line,
the seven bundles are one column, and the seventh no longer stretches across a
whole row on its own, which made it read as a better offer than the six.

Five faults were found and fixed before he saw anything, each measured on the
rendered page: two text edges at every width; one block boundary at 48 where
every other read 64; the comparison's cards sitting 24 further in than every
other block; the ownership note overlapping his three statements; and a band's
own space added twice, giving 192px holes.

## The fold-back, complete this session (Harness Rule 14)

- Built, gated (`css_gate.py`: `pricing.css` PASS) and deployed at theme
  **v0.463.0**; server, local and zip proved identical by `deploy.py`.
- The approved state exported as the prototype's next version, in the Pricing
  Page folder inside Homepage + Commercial Design Prototypes.
- Checked at 1440, 1024, 768 and 390: one text edge, the block boundary at 64 on
  a phone and 96 above it, nothing overflowing at any width.
- `/pricing/` is still unpublished, on Chat's S365 disposition, until the pages
  it links to exist.

## OWED BACK

Nothing. Write the ruling into the document that owns it. DSRD 4 section 3.1
records that Kain's design package leads the layout; **that sentence is now
superseded by this ruling**, because the package's layout is what these four
replaced. The figures it governs are untouched and still lead.

*No em or en dashes in this file; checked before writing.*
