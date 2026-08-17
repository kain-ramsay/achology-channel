# COMMISSION: build one card sheet that renders every registered card from the live components

**From:** Claude Chat, S255. **Date:** 2026-08-10.
**Approved by Kain in session.** This is a build commission, not a question.
**Why it exists:** Kain is taking every card in the design system through one objective review with fresh eyes, so the whole card family is consistent and improved before the remaining Knowledge Hub pages are designed. Cards are the shared unit of those pages, so settling them once is the difference between ruling on the same card four times and assembling four pages from settled parts.

## What to build

**One page, at one URL, rendering every registered card type in the theme.**

It is a build-site page for us to look at, not a public one. Noindex, off the navigation, no sitemap entry. Name it whatever fits the theme's conventions.

## The one rule that makes it worth building

**Every card on the sheet renders from its live component, never re-authored.** Same PHP renderer, same stylesheet, same markup the real pages emit. If a card cannot be rendered from its one home, it does not go on the sheet: it gets named in your report as a card with no single home, which is itself a finding worth having.

This is the whole point. A hand-built sheet would show us your reading of the specification. We need the actual thing, because the specification and the build have drifted before and we are reviewing the build.

## What goes on it

Read DSRD 8 and include every registered card. From Chat's read this session that is at least:

- §6.1 Article card
- §6.2 Book note card, **both** layouts: vertical and horizontal
- §6.3 Quote card
- §6.4 Workbook card
- §6.5 Featured article card
- §6.6 Featured quote card
- §6.7 Featured workbook card
- §6.8 Featured book note card
- §6.9 Compact/mini cards, all four variants: article, book note, quote, workbook
- §7 Course card
- §14 Review card
- §13A Member card
- The bundle card, the Access All Areas card, and the membership cards

**If DSRD 8 registers a card not in that list, include it and say so.** The list is Chat's read, not a boundary. Equally, if something in that list has no live component behind it, say that rather than building one.

Return the sheet's card list in your report so we can confirm nothing is missing before Kain sits down with it.

## How it is laid out

Grouped by family, in DSRD 8's own order, with each card labelled by its section number and name so Kain and I can point at things unambiguously.

Give each family a heading and set the cards in the grid they actually appear in on a real page: the standard Knowledge Hub cards three across, the featured cards spanning their two columns, the compact cards in their row. A card seen alone reads differently from a card seen beside its siblings, and the inconsistencies we are hunting only show up in the second case.

## Three breakpoints

The sheet must be readable at desktop, tablet and phone, since responsive behaviour is where card families usually break apart. Kain will look at all three in Safari.

Whatever the sheet's own container is, each card must sit at the width it occupies on its real page at that breakpoint. A card rendered wider or narrower than its true width would have us ruling on padding and clamping that no reader will ever see.

**Responsive behaviour is part of what is being reviewed, not a backdrop to it.** The card family's responsive rules were set one card at a time as each was built, which is why they currently live as a mobile subsection for the featured family, a separate line for the bundle card, and per-card notes elsewhere. Kain is settling one family rule with recorded exceptions, so the sheet needs to show honestly what each card does at each tier, including where two cards in the same family disagree.

## The build facts we need per card, reported alongside the sheet

These are read off the built component, not judged. They decide things at the review that cannot be decided by looking, and finding them out mid-session would stop it dead.

**1. Is the card a real link?** For each card type, say whether the destination is an `<a href>` in the markup, and what that anchor wraps: the whole shell, the title, or only the footer CTA. If any card is made clickable by a JavaScript handler on a non-anchor element, say so plainly. A card whose route exists only in JavaScript is invisible to a crawler, and on a listing page carrying twenty-four of them that is twenty-four internal links the site does not actually have.

**2. What is the link's accessible name?** The text a screen reader announces and a crawler reads as the link. If it is the footer CTA wording, then a listing page offers two dozen links all named "Read this Article". Report what it is today per card type, and whether the card title is inside the anchor.

**3. What heading element does the card title emit?** `h2`, `h3`, `h4`, or a `div` or `span` styled as a title. DSRD 8 specifies the title's typography and never its element, so this has never been written down. Report it per card type, and say whether the element is fixed in the component or passed in by the calling page.

**4. Do card images carry width and height attributes?** Per card type, for the banner, the cover panel, the thumbnail and the portrait: whether intrinsic dimensions are set in the markup, and whether `loading="lazy"` is applied. The site's CLS target is 0.05, which is tight, and an image with no dimensions reserved is the ordinary cause of a shift.

**5. What is in the alt attribute?** Per card type and per image: the actual value or the pattern it is built from, including whether decorative images (the bookshelf backdrop, the watermark, the faded portrait) are correctly marked as decorative rather than described.

**Report these as facts, not fixes.** Do not correct any of them while building the sheet.

**One thing that is already settled, so it is not reopened:** cards carry no schema markup of their own. DSRD 3 section 5.3 assigns listing pages `CollectionPage` from Rank Math with nothing custom needed. No `ItemList` or per-card structured data is to be added or proposed.

## Real content, not lorem

Use real posts and real course data. Real book covers, real portraits, real titles, real excerpts of their true length.

**Include the awkward ones deliberately.** The longest real title you can find, the shortest, a quote that runs past the clamp, a book with a long subtitle, a course name that wraps. Cards look consistent on tidy content and fall apart on real content, and real content is what the site will carry.

## The course card, which is why this is urgent

The course card has been unsettled since S252: Kain is not certain the built card matches what he approved, because the Book Note prototype carried a prototype rendition rather than the real component, so the two have never been put side by side. Nothing new has been built on it since, correctly.

The sheet resolves that by simply showing the real one. **Render the live course card from its component and nothing else.** Do not reconcile it, correct it, or improve it on the way. If you know of a second rendition of the course card anywhere in the theme or in a prototype, name it in your report rather than choosing between them.

## What you do not do

**No design judgement anywhere in this job.** Do not tidy a card, align two cards that disagree, fix a value that looks wrong, or standardise anything while building the sheet. Every inconsistency you can see is exactly what Kain needs to see, and a card corrected on the way to the sheet is a finding deleted.

Where something looks wrong to you, write it in your report as an observation. That is genuinely useful and it is the right place for it.

## What comes back

The live URL through TO Chat, with:

1. The list of every card on the sheet, by section number and name.
2. Any registered card you could not render, and why.
3. Any card you found authored in more than one place.
4. Your observations, kept separate from the sheet itself.

Kain then reviews it card by card with Chat, rules on the render, and Chat writes each ruling into DSRD 8. Anything he changes comes back to you as its own brief afterwards. Nothing in the theme changes on the strength of this commission except the sheet itself.

*No em or en dashes in this file; checked before writing.*
