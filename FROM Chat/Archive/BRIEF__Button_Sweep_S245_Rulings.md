# BRIEF: the button sweep, built to Kain's S245 rulings

**From:** Claude Chat, S245. **Date:** 2026-08-05.
**Closes:** your `AUDIT__Every_Button_On_The_Site.md` and `REQUEST__Button_Standard_Needs_A_Design_Session_With_Kain.md` (both now archived). The design session you asked for happened this session: every option was rendered at real size in real context, and Kain ruled on each by eye.

## The rulings, now written into the documents

1. **DSRD 7 §5.1 is the button authority and carries its missing padding line.** Standard button padding: 12px 24px, every button in page content.
2. **One compact chrome variant exists:** Como 13px/600, 9px 22px, 10px radius, only inside fixed-height site chrome. Sole use: the header Sign In (§18.6). Sign In does not change.
3. **The nudge CTA is a registered exception** (written into DSRD 8 §18.12): keeps 8px 16px and the 8px corner, reason recorded. Does not change.
4. **The footer CTA button joins the standard:** DSRD 8 §19.7 amended from 12px 28px to 12px 24px.
5. **The typed chevron is replaced by the registered arrow:** §19.7's label becomes 'Start Your Trial' followed by Lucide `ArrowRight`, 15px, white, 6px gap, static (no hover nudge). Registered in DSRD 7 §5.2.
6. **The Listen button keeps 9px 16px, now specified** as a registered exception in DSRD 7 §5.1. Does not change.

## The one code pass

Only the footer CTA button changes:

- `.cta-card__btn`: padding 12px 28px becomes 12px 24px.
- Its label: remove the typed › character; append the registered Lucide `ArrowRight` at 15px, white, 6px gap, static.

Everything else the audit measured now conforms to an explicit specification and stands as built. Do not touch Sign In, the nudge CTA, or the Listen button.

## Acceptance criteria

- The rendered footer button matches DSRD 8 §19.7 as amended (read the canonical file before building; the change register rows for DSRD 7 and 8 are dated S245).
- `css_gate.py` PASS pasted in the ship note.
- The footer is site-wide chrome, so confirm the change renders correctly on at least the About page, one help article, and the 404, and return the result through TO Chat with your status line.

*No em or en dashes in this file; checked before writing.*
