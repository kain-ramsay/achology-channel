# QUESTIONS: three shared-component faults found at S044, one of them blocking

**From:** Claude Code, S044. **Date:** 2026-08-04.
**Context:** Kain worked the About page directly with me this session rather than through spec files, which is his ruling on process. Everything he asked for is built and live except item 1 below, which is stopped and marked **waiting on ruling**. Items 2 and 3 are fixed on the About page and are reported because the cause is site-wide, not page-local.

---

## 1. WAITING ON RULING, and it is blocking the last item of your shared-parts sweep brief

**`components.css` does not pass its own gate, and has not for some time.** Six failures, none of them introduced this session. Confirmed rather than assumed: I stashed my change, re-ran the gate against the committed file, and got the same six with only the line numbers moved.

```
line 465: HAND-TYPED SHADOW '0 2px 12px rgba(53,65,73,0.10)'    .proof-card, resting
line 469: HAND-TYPED SHADOW '0 8px 28px rgba(53,65,73,0.16)'    .proof-card, hover
line 482: HAND-TYPED COLOUR #000                                the video lightbox
line 482: HAND-TYPED SHADOW '0 24px 64px rgba(0,0,0,0.4)'       the video lightbox
line 484: HAND-TYPED SHADOW '0 4px 14px rgba(0,0,0,0.25)'       the lightbox close
line 526: HAND-TYPED COLOUR #000                                a second lightbox rule
```

**What it blocks.** Item 4 of `BRIEF__Sweep_Shared_Parts_About_And_Testimonials.md`, the visible question label under each of the five member videos. It is built and ready: the poster and its caption become one figure and the grid spans move from the button to that figure. The rule that carries it belongs in `components.css`, which is the block's one home under DSRD 3 §2.6, and H4 will not let that file ship while it fails. Every other item of the brief is live on both pages.

**Why I have not annotated them to pass.** The gate accepts an annotation, and I could have written one in a minute. But four of these are values I did not set, and I do not know whether anyone chose them deliberately. Writing "deliberate one-off" over someone else's drift is inventing a justification, and it would leave the file passing while telling the next reader something untrue.

**What I would do, for what it is worth.** Two of the four shadows sit within two hundredths of an existing token: `--shadow-card` is `0 2px 12px rgba(53,65,73,0.08)` against the card's `0.10`, and `--shadow-card-hover` is `0 8px 28px rgba(53,65,73,0.14)` against its `0.16`. Nobody chose those as different things, and DSRD 6 §10's first verdict is written for exactly this: "Collapse it. The value sits close enough to a named one that using the named one leaves the page looking the same. Change the page. Two values a hair apart are drift, not design."

The two blacks and the `0 24px 64px` are already yours: DSRD 7 §5.4 records them as an open item, "the lightbox shadow exists in two versions ... both stand as found inconsistencies, and neither may be copied to a new page." The `0 4px 14px rgba(0,0,0,0.25)` is one hue away from the `--shadow-float` token you created this session.

**The ask:** a ruling, and if it needs a sweep brief because it touches shared components on every page, then that brief. The video labels ship the moment it lands.

## 2. FIXED on About, but the cause is site-wide: a button inside a body wrapper renders as an underlined orange link

Kain said the closing panel's button was "not following any rules whatsoever". He was right, and it was worse than styling: it rendered **orange text, underlined, on the orange fill**, which is close to illegible.

The cause is specificity. `policies.css`'s `.policy-body a` is one point more specific than `.btn-primary`, so a button that happens to be an `<a>` inside a body wrapper loses its own colour and gains a body-link underline. DSRD 7 §5.1 is unambiguous about what it should be: "Primary (solid): Background #ED6922, white text."

I fixed it scoped to the About page, because that button and the founders letter button are currently the only ones on the site sitting inside a body wrapper, and widening the fix would have been a sweep. **But the trap is live for every page:** the next person who puts a button inside `.policy-body` anywhere will get an underlined orange link and may well not notice, because it still looks like *something*.

Worth a ruling on whether `.btn` should simply out-rank the body-link rule at source.

## 3. FIXED on About, and worth knowing everywhere: a replaced photograph never reaches the reader

Kain asked me twice to replace the customer support photograph. Both times I had already done it. The file was converted, deployed, and verified byte-identical on the server, and he still saw the old picture.

**Stylesheets and scripts get a version stamp from WordPress; images baked into a template do not.** The filename had not changed, so the address had not changed, so no browser had any reason to fetch it again. Nothing in any gate catches this, because the page and the server are both correct.

Both About portraits now carry the theme version in their address. Every other template with a baked image has the same gap, and DSRD 6 §11 item 1 is the line it defeats: everything loads on the page as a visitor meets it.

## Also, two recorded exceptions the About page now needs

Both are consequences of Kain's own S044 rulings, and both are the instrument failing to describe the page rather than the page being wrong.

1. **The hero hairline reads as absent to `page_gate`.** It now spans only the copy block, on his ruling, so it sits on a child element rather than at the block boundary. The gate has no way to express a part-width hairline. Measured on the live page it is correct: 48 above from the button, 48 below to the next block.
2. **At phone the gate measures 1px above the hero line.** It is reading the decorative backdrop, which fills the hero by design under his phone ruling. The real gap from the text is 32, and 32 below.

*No em or en dashes in this file; checked before writing.*
