> **DISPOSITIONED S303 (Chat).** Answer written into both canonical homes and read back: DSRD 8 section 18.4 carries the label change with the measurements and the reasoning and is the authoritative copy; DSRD 1 section 13.1 carries the label and points at section 18.4. Dropdown heading and footer link untouched, as ruled. No board card moved: this is a document edit at molecular altitude (standing rule 20). Archived.

# RULING: the header's Knowledge Hub item is now labelled "Learn"

**Ruled by:** Kain, in session, Session 080, 24 August 2026.
**Where:** Safari, on the tabbed comparison at `previews/header-nav-label-options.html`, built with `variant_tabs`. Both panels carried the real header lifted from the rendered About page at tablet width; only the one label differed.
**His words:** "LEARN - makes perfect sense - and works well. Lets go with this option please."

**Shipped in theme v0.82.1**, deployed and verified.

---

## The fault it fixes, measured rather than argued

The six top-level labels come to **498px** with no wrapping. Their specified 32px gaps add **160px**, so the bar needs about **658px**. Between 880 and 1023 the header offers **600 to 640px**.

**So the navigation did not fit anywhere in the tablet band**, and the browser wrapped KNOWLEDGE HUB onto two lines to cope. On every page of the site, at every tablet width. Measured at 880, 900, 960 and 1023.

"Learn" is 86px narrower. Verified after shipping at 880, 900, 1023 and 1200: **no label wraps at any width**, and the phone overlay is unaffected.

## What was considered and rejected, so it is not reopened

**Kain's own first proposal was to drop the item at tablet.** It resolves the arithmetic, and it was rejected on the reasoning that it makes the site's map depend on the device: a tablet visitor would lose the only route to the Knowledge Hub from the header, on the section the whole content plan is built on.

**Tightening the gaps** fits it with about two pixels to spare, which breaks again the first time any label changes.

**Raising the hamburger switch from 880 to 1024** was my own recommendation before he proposed the label change. His is better: it keeps six reachable items on a device with room for them.

## It is site-wide, and that was my call

He asked the question about tablet. The change is applied at every width, because a label that changes with the viewport is the same device-dependent-map fault in another form, and "Learn" matches the address the link already points at, `/learn/`.

Both places in `header.php` carry it: the desktop bar and the mobile overlay's accordion toggle.

## What Chat owes, and both are LOCKED sections

**DSRD 1 §13.1, Header Navigation.** Item 4's label becomes `Learn`. The destination is unchanged at `/learn/`.

**DSRD 8 §18.4, Navigation Structure.** The same row, same change. §18's own copy is the authoritative one per §13.1's pointer, so it needs to carry the reason as well as the word.

**Nothing else moves.** The dropdown panel beneath it is untouched, including its heading "Explore New Ideas in Achology's Knowledge Hub", and the footer's own "The Knowledge Hub" link is a separate locked list at §13.2 and was not part of this ruling.

## One thing worth naming for the type scale work

The wrap was invisible to every gate we run, because nothing measures whether a nav label fits its bar. It was found by rendering the header at four widths during a sitting. A page can be pixel-correct on every value it declares and still be visibly broken at a width nobody looked at.

*No em or en dashes in this file; checked before writing.*
