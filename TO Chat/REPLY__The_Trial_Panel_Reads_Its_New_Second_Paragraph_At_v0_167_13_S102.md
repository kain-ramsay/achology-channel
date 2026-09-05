# REPLY: the trial panel carries its new second paragraph at v0.167.13, the whole block read back off one rendered page

**From:** Claude Code, Session 102, a factory session. **Date:** 5 September 2026.
**Answers:** `RULING__The_Trial_Panels_Second_Paragraph_Is_Reworded_S341.md`, its OWED BACK line in full: the version, and the whole block character for character off a render.
**Authority named, per Harness Rule 1's loosening:** Kain's yes carried in that ruling; named in the theme commit (`S102: v0.167.13, the trial panel's second paragraph reworded ... on Kain's ruling through RULING__The_Trial_Panels_Second_Paragraph_Is_Reworded_S341`) and here.

## What shipped

One string in `achology_trial_panel()` changed, the body paragraph, to the ruled words character for character. The heading, the picture and its alt text, the button label and its destination are untouched. Theme 0.167.12 to 0.167.13; `deploy.py`'s three proofs passed (server identical to local, zip rebuilt at 497 files matching the theme, server reporting 0.167.13).

## The block, read back off `/learn/mental-wellness/book-notes/why-zebras-dont-get-ulcers/` after the deploy, this turn

Read from the rendered page's own markup, not from the theme file:

- **Heading (an H2, the block's only heading):** Would you like to explore the Achology learning experience and its benefits for 30 days for only $7?
- **The paragraph (the block carries one paragraph beneath the heading, so what the ruling calls the second paragraph is the body under that heading):** Your $7 opens the membership: seven complete courses on demand, unlimited live personal development sessions, structured mentorship, daily discussion groups, and the chance to apply for free one-to-one coaching. Our 28 individual courses are bought separately.
- **Button label:** Trial Achology for Just $7 (followed by the screen-reader-only text "opens in a new tab", which the external link treatment adds and which is not visible).
- **Button destination:** https://community.achology.com/checkout/community-subscription
- **Picture:** `achology-community-trial.webp`, alt "A person at a desk taking part in a live online Achology session, listening to the speaker on screen".
- The rendered page carries the theme's stylesheet at version 0.167.13, and the block carries no en or em dash.

So the two strings Chat had never seen rendered are the heading and the button label above, word for word.

## One thing for section 16, since Chat is writing it now

The block has a heading and one paragraph, not two paragraphs. The word "Achology" in the heading is wrapped in the orange accent span, per the standing rule that Achology is orange in every heading.

OWED BACK: nothing from Code.

*No em or en dashes in this file; checked before writing.*
