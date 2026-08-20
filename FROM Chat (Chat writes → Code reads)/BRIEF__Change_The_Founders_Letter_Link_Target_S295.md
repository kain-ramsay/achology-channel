# BRIEF: change one link target on the Founders' Letter

**DOCUMENT TYPE:** approved brief. **From:** Claude Chat, Session 295. **Date:** 20 August 2026.
**Approved by Kain, S295.** One attribute changes. No word of the letter is touched.

**This reverses Kain's own S245 ruling, deliberately.** The Wikipedia target was his call then,
filed under Harness Rule 14 and recorded in DSRD 2 §2.13. He reopened and reversed it this
session on the DSRD 6 §6 finding below. **DSRD 2 §2.13 has already been corrected**, so the
specification and this brief agree; if you find any other document still naming Wikipedia as
this link's target, it is stale and the corrected §2.13 governs.

---

## Why

Chat ran DSRD 6 §6's human half on `/about/founders-letter/` this session and failed it on
item 3. That item requires a cited source to be linked "directly (the book's own page, the
study itself), not a middleman summary", and names linking to originals as itself a trust
signal.

The letter's central claim rests on the manual's growth from roughly a hundred categories in
its first edition to roughly three hundred in the current one. **Sending a reader to
Wikipedia to check the page's strongest claim is the weakest support available for it**,
and it is the letter's only outward link.

## The change

`policies-content/founders-letter.php`, in the paragraph beginning "The American Psychiatric
Association began publishing that list in 1952".

**Current href:** `https://en.wikipedia.org/wiki/Diagnostic_and_Statistical_Manual_of_Mental_Disorders`

**New href:** `https://www.psychiatry.org/patients-families/what-is-the-dsm`

**Everything else about the link is unchanged**: the same anchor text ("Diagnostic and
Statistical Manual of Mental Disorders", the words already in the sentence, per DSRD 1
§6.4), the same `target="_blank"` and `rel="noopener"` per DSRD 3's external-link standard.
**The href attribute is the only thing that moves.**

## Why that page, and not the other one

The American Psychiatric Association holds two pages for the manual, and both are the
publisher's own, so both satisfy item 3:

- `https://www.psychiatry.org/psychiatrists/practice/dsm`, the practitioner-facing DSM home.
- `https://www.psychiatry.org/patients-families/what-is-the-dsm`, written for a general reader.

**The reader-facing page is chosen** because it carries the exact fact the letter's sentence
rests on, that the association has published and updated the manual since 1952, and because
a reader of a founders' letter is a general reader rather than a clinician.

**Both were fetched and confirmed live this session**, so neither is a guessed address.

## What NOT to do

- **Do not edit a word of the letter.** The anchor text stays exactly as it is.
- **Do not add a second outward link.** This remains the letter's only one.
- **Do not fill any judgement line in `DSRD6_RECORD.md`.** Chat writes those.

## What to return

The rendered page through TO Chat, with the link followed once to confirm it resolves.

*No em or en dashes in this file; checked before writing.*
