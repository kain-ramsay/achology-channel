CHAT DISPOSITION, S346, 6 September 2026: read and recorded. Shipped at v0.167.63 and v0.167.64 and struck from the theme queue by Code in the sitting that shipped it. Chat ruled the same opener fix runs across the other three dialogs, which remains an open theme queue line. No DSRD change owed. Board card: accessibility and the dialogs.

# SHIP: the policy document reader joins the shared modal, and the page behind it is inert at last

**DOCUMENT TYPE:** ship brief. Not a page spec.

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Shipped:** theme v0.167.63 and v0.167.64, each deployed with its three proofs.
**Answers:** the second of the two accessibility fixes your S344 ruling unblocked.
**Board card:** the Codex theme audit.

---

## What changed

The reader's inline script in `template-policy.php` no longer runs its own dialog behaviour. It calls `window.achologyModal`, which owns the focus trap, Escape, the opener restore, the scroll lock, and `inert` with its `aria-hidden` fallback on everything outside the box. What stays local is the part that is genuinely this reader's: turning pages, the desktop spreads, and flipping its lazy images to eager on first open.

## Why I did more than add the attribute

Your line asked for `inert` on the reader, and I could have added six lines to its own open and close. I did not, because this was the fifth hand-rolled focus trap in the theme and the last one outside the controller built at S103 precisely to stop that. The rule the workbench key taught in the same session applies: when the same behaviour is written in five places, a fix applied to four of them looks finished and is not. If you would rather it had stayed local, say so and I will change it back.

## The one thing that made it more than a swap

`modal.js` is enqueued in the footer and the reader's script is printed in the page body, so at parse time `window.achologyModal` did not yet exist. The block is now held to `DOMContentLoaded`. It binds handlers a fraction later and nothing else.

## v0.167.64, which was mine to catch and I nearly did not

`modal.js` remembers the opener by reading `document.activeElement` when a dialog opens. **Safari on the Mac does not focus a button when it is clicked.** So on Safari, and only on Safari, every one of these dialogs returned the visitor to the top of the document instead of to the button they pressed, which is most of what the opener restore exists to prevent. The reader now hands its button in.

**The other three dialogs still read `activeElement` and still carry this.** The member story, testimonial and About dialogs need the same, and the durable form is `modal.js` taking the opener off the click event itself rather than each caller remembering to pass it. That is a shared-file change reaching three pages, so it is a sweep, and it is on the theme queue rather than done. Tell me if you want it as one.

## Your test, met

Measured on `/about/code-of-ethics/` after the deploy, which carries two readers. On open: eleven of the twelve siblings outside the box take `inert` and `aria-hidden`, focus enters at the close button, the page behind stops scrolling. On close by Escape: all eleven restore, including the two that carried `aria-hidden` for their own reasons before the reader opened and keep it after, no `data-ach-modal-was` markers left behind, and focus back on the button pressed. No console errors. Text content and appearance unchanged.

## What I found while verifying, which is not mine to fix

**axe on `/about/code-of-ethics/` returns one violation and it is colour contrast on `cite`**, on a record dating from 14 August. It predates this change and reaches the whole policy family, so it wants measuring across all ten pages before anything is chosen. On the queue as an open line, next to the same shape of problem on the testimonials page.

---

OWED BACK: your word on whether the shared controller was the right depth for this, and whether the opener sweep across the other three dialogs should run.

*No em or en dashes in this file; checked before writing.*
