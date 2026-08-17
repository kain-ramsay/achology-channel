# BRIEF: darken the AA-safe link orange to #B8460F and set body-link underlines to 1px

**From:** Claude Chat, S248. **Date:** 2026-08-06.
**Answers:** `FINDING__Link_Orange_Fails_On_The_Off_White_Panel.md` (your S047 page 6 finding, now archived).
**Authority:** Kain, S248, both decisions made on rendered options in Chat. Written into DSRD 7 section 1 and section 5.1 this session; the change register row is updated.

## Context, standalone

Your S047 walk measured the AA-safe orange #C64E14 at 4.23 to 1 on the off-white panel #F3F4F4, below the 4.5 that 15px links require. Six links inside the Disclaimers page section 12 cross-reference table fail. The colour cleared white by only 0.17, so any tint takes it under, and DSRD 7 section 1 claimed it was safe with no background named. Kain has ruled the fix.

## The two rulings

1. **The token value changes.** `--color-orange-link` becomes **#B8460F**, replacing #C64E14, in base.css. One value, everywhere the token is used. Measured (alpha composited, same method as your finding): 5.35 to 1 on white, 4.86 to 1 on #F3F4F4. Both clear 4.5. Every role the token covers (body links, overlines, breadcrumb current page, small button labels, heading accent words) takes the same slightly darker orange; Kain approved the site-wide change knowing that.
2. **Body-copy link underlines are 1px.** `text-decoration-thickness: 1px` for body-copy links, site-wide. Kain chose it against the browser default and a 0.5px hairline, on rendered options. If the built links carry a `text-underline-offset`, keep the built offset; the ruling changes thickness only.

## Acceptance criteria

- `--color-orange-link` resolves to #B8460F; no CSS file still carries #C64E14 (sweep for the literal hex in case any file hand-typed it rather than using the token).
- Body links render 1px underlines at desktop, tablet and phone.
- The six Disclaimers cross-reference links measure at or above 4.5 to 1 on the rendered page.
- `css_gate` passes on every touched file.
- Your walk records that referenced the finding can restate section 7 accordingly; the Accessibility Statement's "all body-length text passes WCAG AA" sentence becomes true again once shipped.

DSRD 7 section 1 is the canonical statement; read it before building. This brief exists so you have the ruling without waiting to re-derive it.

*No em or en dashes in this file; checked before writing.*
