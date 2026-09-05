# RULING: the video dialog's close button shows whole, inside the corner

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Given by:** Kain, directly in the sitting, on the rendered page in Safari.
**Shipped on his word:** theme v0.167.33.
**Board card:** the Codex theme audit.

---

## What he was shown

The reviews page, opened in Safari as a new tab, with the member story video dialog open. He was told what to press and what he would see: the white close button in the video's top right corner with only a quarter of it showing, because the video's rounded corner cuts the rest away, and that the About page had been like that all along.

## The question, and his words

Asked whether the whole button should move just inside the corner so all of it shows:

> "yes, please do claude!"

## What shipped on it

`components.css`: the shared rule for `.about-video-lightbox__close` and `.shared-video-lightbox__close` moves from `top: -18px; right: -18px` to `top: 8px; right: 8px`.

**8px is not a number chosen in the moment.** The same rule already used it below 768px, where the negative offsets would have pushed the button off a phone screen. The component held the right answer and applied it at one width only. That phone override is deleted with this change, because it now repeats the rule above it.

Measured on the rendered pages after the deploy: at 1440 the whole button sits inside the panel, at 390 the whole button sits inside the panel, on both the reviews page and About.

## The fold-back Rule 14 asks for cannot be written, and that is a finding

Rule 14 says a ruling approving how a component looks is exported into that component's design folder as the prototype's next version, with the build sheet updated to match.

**The shared video lightbox has neither.** `COMPONENT_REGISTRY.md` carries it as a row reading NOT RECORDED for prototype, build sheet and disposition. It is one of the six families the S266 harvest found that DSRD 8 had never named.

So the Rule 4 chain has no top for this component: prototype beats sheet beats code, and here there is only code. I have not invented a prototype to satisfy the rule, because a prototype written from the code is exactly the inversion that chain exists to prevent.

**What I need from you:** whether this component gets a prototype and a sheet now that Kain has ruled on its appearance, or whether its registry row records a different disposition. Either way the row should stop reading NOT RECORDED in all three columns while the component is live on four page families.

---

OWED BACK: the disposition for the shared video lightbox's registry row.

*No em or en dashes in this file; checked before writing.*
