# BRIEF: footer column headings change to light orange #F5A05C

**From:** Claude Chat, S248. **Date:** 2026-08-06.
**Answers:** `FINDING__Footer_Contrast_Fails_WCAG_2_2_AA_Site_Wide.md` (your corrected S047 filing, now archived).
**Authority:** Kain, S248, re-ruled on rendered options in Chat. Written into DSRD 8 sections 19.6 and 19.9 and DSRD 7 section 1 this session; both register rows updated.

## Context, standalone

Your corrected finding stood on one item: the four footer column headings, brand orange #ED6922 at 11px/600 on the #354149 footer, measuring 3.32 to 1 against a required 4.5. The S235 ruling that kept them orange rested on the premise that brand orange was accessible on the dark footer, and your measurement contradicted that premise. Both document corrections you asked for are done, and Kain has re-ruled the colour knowing the real number.

## The ruling

The footer column headings (all four, plus the mobile accordion headings, which are the same element) and the CTA card overline 'JOIN ACHOLOGY TODAY' (same 11px/600 style on the same dark ground; Kain ruled it onto the same value on the rendered card) take **light orange #F5A05C**, replacing brand orange #ED6922. Measured on the headings: 5.0 to 1 on #354149, passing AA at 11px/600 with no exception needed. The overline sits on the CTA card's faint orange tint, so measure it on the rendered card to confirm it clears 4.5 there too; the calculation says it does comfortably. #F5A05C is now a named DSRD 7 section 1 value (it was previously the annotated About-gradient one-off); if you give it a token, name it in base.css and annotate per section 4.5.

Not in scope: the Achology-span mechanics beyond inheriting the new heading colour.

## Acceptance criteria

- The four column headings, the mobile accordion headings, and the CTA card overline render #F5A05C at desktop, tablet and phone.
- Measured contrast on the rendered footer at or above 4.5 to 1.
- No other footer element changes; the Start Your Trial button stays exactly as its DSRD 7 section 5.1 recorded exception says.
- `css_gate` passes on touched files.
- Your walk records restate the chrome item in section 7 as closed once shipped.

DSRD 8 section 19.6 is the canonical statement; read it before building.

*No em or en dashes in this file; checked before writing.*
