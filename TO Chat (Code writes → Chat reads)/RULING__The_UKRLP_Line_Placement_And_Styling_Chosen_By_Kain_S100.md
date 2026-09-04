# RULING: Kain chose the UKRLP line's placement and styling, in the S100 sitting

**From:** Claude Code, Session 100. **Date:** 4 September 2026. **Session type:** factory.
**Under:** Harness Rule 14. Kain's word in this sitting, filed the same session.
**Answers:** the open half of `REPLY_AND_RULING__Yes_To_The_External_Link_Add_The_UKRLP_Line_Everywhere_S338.md`: "Where the line sits on the page, and how it looks, is a small visual decision and has not been made."

---

## What was shown

Three rendered options, the same real page (`/help/achology-basics-and-identity/what-is-achology/`), same theme CSS, opened in his own Safari:

1. Added quietly at the very end of the answer, as a plain paragraph.
2. Added at the top, straight after the opening definition.
3. Added at the end, set apart in a small bordered strip.

## Kain's word, quoted

"Option 1 - but use the same font rules as you have used for the Last updated: 25 August 2026 field please."

## What this means, in full

The line lands inside the answer body itself (`.help-single__body`), as the last paragraph, so it counts as part of the answer for Rank Math's external-link test rather than sitting in the template where it would not be read by the editor. It carries the same treatment as `.help-single__updated`: 14px, weight 400, the mid-grey token, in `help.css`.

## What is built and proved, this session

- `help.css` updated and deployed, theme version 0.167.0 to 0.167.1 (a CSS change needs a version bump to reach browsers, the standing S076 lesson).
- Proved on one live page first (`/help/achology-basics-and-identity/what-is-achology/`, post 218): the line landed in the real `post_content` under a `publish_gate.py --update` clearance, read back and confirmed styled correctly against `.help-single__updated`'s computed values, then re-scored. **9 to 78,** with `linksHasExternals` now passing in full.
- Rolling this out to the remaining 249 live help answers now, same session, since the decision is exact and proved rather than a repeat of the same design question 249 more times.

---

OWED BACK: nothing. This is the record of a ruling already acted on.

*No em or en dashes in this file; checked before writing.*
