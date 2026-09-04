**DISPOSITIONED S339 (Chat): read, closed loop.** A live ruling made and acted on entirely inside Code's own S101 sitting; nothing owed from here. No card change needed.

# RULING: Kain reworded the UKRLP line and enlarged the hero image, in the S101 sitting

**From:** Claude Code, Session 101. **Date:** 4 September 2026. **Session type:** factory.
**Under:** Harness Rule 14. Kain's word in this sitting, filed the same session.
**Follows:** `RULING__The_UKRLP_Line_Placement_And_Styling_Chosen_By_Kain_S100.md`, which this partially supersedes.

---

## What was shown

The pilot page, `/help/achology-basics-and-identity/what-is-achology/`, opened in Kain's own Safari.

## Kain's word, quoted

On the UKRLP line's wording: "Please change: 'Achology is listed on the UK Register of Learning Providers (UKRLP) with the UK Provider Reference Number (UKPRN: 10099815).' with 'Achology is listed on the UK Register of Learning Providers (UKRLP) with the UK Provider Number UKRLP 10099815'."

On the hero image: "i think the image could maybe benefit from being a little bit larger."

## What this means, in full

**The UKRLP line's wording changes; its link and placement do not.** The number stays the live link to the UKRLP search page (`https://ukrlp.education.gov.uk/search/provider/10099815?query=Achology&page=1&ukprnStatus=active`), which is what makes the line count as a genuine external link for Rank Math's own check. Only the surrounding words change, to Kain's new sentence exactly as given. This is the line's second wording; the first (S100's, "UK Provider Reference Number (UKPRN: ...)") is superseded.

**The hero image grows from 200px to 240px on desktop, 130px to 155px on mobile**, the same proportion both tiers, since "a little bit larger" was given as a direction rather than a number and both sizes needed to move together.

## What is built and proved, this session

- `help.css` updated (`.help-hero-image` width/height at both tiers) and deployed, theme version 0.167.7 to 0.167.8.
- Post 218's live `post_content` updated under a `publish_gate.py --clear ... --update` clearance: only the UKRLP paragraph's wording changed; the hero image and the rest of the body are untouched.
- Both re-verified on the live pilot page before this file was written: the image measures 240px, the line reads exactly as Kain gave it.

---

OWED BACK: nothing. This is the record of a ruling already acted on.

*No em or en dashes in this file; checked before writing.*
