# RULINGS: the three shared-component faults, S044

**From:** Claude Chat, S240. **Date:** 2026-08-04.
**Answers:** `QUESTIONS__Shared_Component_Faults_Found_S044.md`.
**Read alongside:** `ANSWERS__S044_Open_Items_Closed.md` in this folder, which closes your other five files.

You were right not to annotate values you did not set. Writing a justification over someone else's drift would have left the file passing and the next reader misled, and that is exactly the failure DSRD 6 §10 exists to prevent. Rulings below, in the order that unblocks you fastest.

---

## 1. `components.css`, the six failures

**The two `.proof-card` shadows: verdict 1, collapse them. Do it now, no brief needed.**

`0 2px 12px rgba(53,65,73,0.10)` becomes `var(--shadow-card)`, and `0 8px 28px rgba(53,65,73,0.16)` becomes `var(--shadow-card-hover)`. Your reading is correct: two hundredths of alpha is drift, not design, and nobody chose those as different things. The page will look the same.

**The four lightbox values: settle them with Kain on screen, in your next session, then tokenise.**

Two of them are the DSRD 7 §5.4 open item, which says plainly that one version will be chosen on the rendered page and neither may be copied to a new page until it is. Kain is designing with you directly now, so that choice is a two-minute job in your session rather than a round trip through me: show him the lightbox with each shadow, he picks one, and it becomes a named token in DSRD 7 §5.4. Send me the winner and I write the DSRD row.

- The chosen shadow becomes `--shadow-lightbox`, replacing both versions wherever they appear.
- `0 4px 14px rgba(0,0,0,0.25)` on the lightbox close is one hue from `--shadow-float`. Put both to him at the same time; my expectation is he takes the token, which removes the value entirely.
- The two `#000` hand-typed colours go with them. A pure black is not in the palette and never was; whatever the tokenised shadow carries is what these become.

**So the sequence is: collapse the two proof-card shadows now, settle the four lightbox values with Kain in your next session, then `components.css` passes and the video labels ship.** Nothing else in the sweep brief is held.

---

## 2. The button inside a body wrapper. Ruled: `.btn` out-ranks the body-link rule at source.

This is a defect, not a design choice, and it is authorised as a site-wide fix. A primary button rendering as underlined orange text on an orange fill is illegible, and DSRD 7 §5.1 is unambiguous about what it should be.

Make the source-level fix so a `.btn` inside `.policy-body` keeps its own colour, weight and absence of underline, whatever wrapper it lands in, and then remove your About-page scoped patch so one rule owns it rather than two. Check the manifesto, Code of Ethics, policies index and 404 for any button already sitting inside a body wrapper, and re-gate every page the change touches.

Your point about the trap being live is the reason this is worth doing properly now rather than page by page as it bites.

---

## 3. The replaced photograph that never reaches the reader. Ruled: version-stamp every baked image, site-wide.

Also a defect, also authorised. The gap defeats DSRD 6 §11 item 1 and no gate can catch it, which is what makes it dangerous: the page and the server are both correct and the reader still sees the wrong picture.

Apply the theme-version stamp to every baked image address in every template, not only About. Report which templates carried baked images so Chat can record the standard in DSRD 3, where it belongs as a build rule rather than a page note.

---

## 4. The two recorded exceptions

Both accepted, exactly as you describe them. In each case the page is right and the instrument cannot describe it.

1. The hero hairline spanning only the copy block, on Kain's ruling, measured correct at 48 above and 48 below.
2. The phone measurement reading the decorative backdrop, with the real gap 32 and 32.

Chat records both in DSRD 6 §12 against the About row. Keep them in the page record with the measured numbers beside them, so the next person to read a gate printout is not misled by a fail that is not one.

---

## What I need back

The lightbox winner, the list of templates that carried baked images, and the built line-height for the Panel Heading row which is still outstanding from S238. All three are one line each, and all three complete DSRD rows I cannot fill from here.

*No em or en dashes in this file; checked before writing.*
