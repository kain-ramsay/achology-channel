# SHIP and ASK: one modal controller, and a close button nobody could see

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Shipped:** theme v0.167.30, v0.167.31 and v0.167.32, each deployed with its three proofs.
**Closes:** most of the theme queue's modal line, the Codex audit's sixth item, DSRD 6 chapter 7.
**Board card:** the Codex theme audit.

---

## What shipped

`modal.js` is new and holds, once, what four dialogs were each half implementing: the focus trap wrapping at both ends, Escape, focus returning to whatever was clicked, `inert` plus `aria-hidden` on everything outside the dialog with any prior `aria-hidden` remembered and put back, and the scroll lock.

The member story lightbox, the testimonial lightbox and the About lightbox all call it now. Both video iframes carry a title, so a screen reader announces whose video it is rather than reading out a player address and a number.

The two lightboxes the audit named both declared `role="dialog" aria-modal="true"`, which promises a screen reader that the rest of the page is unavailable, and neither kept it. Tab walked straight out into a page that was still fully readable and clickable. The testimonial one did not return focus to the card that opened it either.

Measured after the deploy, on the live pages: focus lands inside the dialog, Tab and Shift Tab wrap at both ends, focus dragged outside is pulled back, the header is `inert` and `aria-hidden` while a dialog is open and freed on close, focus returns to the exact card that was clicked, the video is torn down, and the console is clean.

## The thing that was found on the way, and it is the part worth your attention

**The member story lightbox's close button has been rendering off the screen.**

It sat as a sibling of the panel rather than inside it, so its containing block was the lightbox layer, which is `position: fixed; inset: 0`. The shared rule puts the button eighteen pixels outside the top right corner of whatever contains it. Outside the corner of the panel it was written for; outside the corner of the **window** here. Measured at 1440 by 900 it rendered at x 1418, y minus 18: half above the top of the screen, the rest past the right edge.

It is on every page carrying the member story strip, which is /reviews/, the course pages and /cards/. Nothing reported it because Escape and a click on the backdrop both close the dialog, so the only person who would ever find it is somebody looking for the button. It was styled, it was announced to a screen reader, and it could not be seen or clicked.

It is now inside the panel, exactly as the identical lightbox on /about/ already has it, so two instances of one component stop disagreeing. That also brings it inside the element carrying `role="dialog"`, which is what lets the focus trap reach the control that closes the dialog.

**The ASK.** Both instances now show the button as a quarter circle, because the panel clips it (`overflow: hidden` against `top: -18px; right: -18px`). That is the appearance /about/ has shipped with, so it is what these two now share rather than anything chosen here. It is not good, and moving it fully inside the corner is a visual decision. Put to Kain on a render this session.

## Two parts of the queue line did NOT ship, and both are with you

**The testimonial filter buttons.** They carry `role="tablist"` and `role="tab"` with `aria-selected`, and implement none of the tab pattern: no arrow-key roving focus, no single tab stop for the set, no `tabpanel`. A screen reader announces "tab, 1 of 5" and then meets an ordinary button, which is worse than no role at all. The fix is `role="group"` and `aria-pressed`, in `page-testimonials.php`.

**The policy document reader**, the fourth dialog, whose script is inline in `template-policy.php`. It already has a trap, Escape and focus restore; it is missing only the `inert` half, so the page behind still takes clicks while the reader is open.

**Both were refused by the scope wall, for the same reason: neither page has a signed spec carrying a page gate line.** Harness Rule 5 says that is a stop and ask rather than an edit, so I stopped. The JS deliberately still writes `aria-selected` on the filters, because a button reading `role="tab"` with `aria-pressed` on it would be worse than either alone.

**What I need from you:** either a signed spec with its page gate line for those two pages, or your word that an accessibility correction that changes no wording and no appearance does not need one, in which case say so and I will put it in the harness as a rule rather than treating each case on its own.

---

OWED BACK: the route for those two pages, and Kain's word on the close button's corner if you would rather it came through you than through the sitting.

*No em or en dashes in this file; checked before writing.*
