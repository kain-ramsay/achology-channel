# BUILD BRIEF — Consolidate the "Where next?" panel as a library component (S219)

**From:** Claude Chat · **To:** Claude Code · **Date:** 24 July 2026 · **Status:** approved by Kain

## Why you're getting this

The "Where next?" panel (`.policy-next*`) ran on three pages — the manifesto, the Code of Ethics, and the 404 — so it passed §12's reuse threshold in DSRD 8. It has now been **promoted from a policy-family page-local block to a locked library component**, specified in full at **DSRD 8 §13 ("Where next?" Panel)**. DSRD 8 §12.4 no longer lists it; its row there now points to §13, and the family's block count dropped from six to five.

The spec is done. This brief is the build half of the promotion procedure (DSRD 8 §12.3, step 3): move the CSS to the shared layer so future pages adopt one component rather than copying a second version. **No visual change** — the panel must render pixel-identical afterwards.

## What to build

1. **Move the `.policy-next*` rules out of `policies.css` §9 into the shared components stylesheet (`components.css`).** That is where site-wide components live per DSRD 10 §6 (alongside breadcrumbs and school accent colours). Take the whole `.policy-next*` block, including the `--pair` variant, the `button.policy-next__row` variant, the in-prose `.policy-body .policy-next*` overrides, the ruled-page rhythm rules, and the `.policy-page--404 .policy-next` zeroing.
2. **Leave the panel's markup and class names exactly as they are.** The three pages already use `.policy-next*`; they "point at the component" by class, so nothing in the templates changes — this is a stylesheet move, not a markup change.
3. **Do not fold in the icon-tint work.** The `.policy-next__icon` tint is the raw value `rgba(237,105,34,0.07)` and its selector is ungrouped — both are owned by the **Icon Standardisation** card, not this brief. Move the rule as-is; don't tokenise it here.

## Acceptance criteria

- `.policy-next*` (all rules named above) live in `components.css`; `policies.css` no longer defines them.
- The manifesto, Code of Ethics and 404 pages render pixel-identical to before at desktop, tablet and phone — including the pair variant on the manifesto, the button-row variant, and the 404's zeroed top margin.
- No other page gains or loses styling from the move.
- The panel matches DSRD 8 §13 exactly.

## Definition of done

The three affected pages pass the **DSRD 6 page gate** with the per-chapter record returned. Confirm back on this channel (`TO Chat`) that the move is done and nothing regressed.
