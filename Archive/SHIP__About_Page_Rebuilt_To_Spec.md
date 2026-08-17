# SHIP: the About page rebuilt to its signed spec and addenda, v0.37.0

**From:** Claude Code, S044. **Date:** 2026-08-04.
**Answers:** `SPEC__About_Page_Locked_Structure_And_Copy.md` and `ADDENDA__About_Page_Hero_Action_Founders_Block_Closing_Panel.md`, both S237.
**Status: changed, not verified.** The page is not rendered. Kain uploads the zip, and the DSRD 6 record and the page_gate printout follow from the live page.

## What is in the theme now

Files touched: `page-about.php`, `about.css`, `about.js`, `style.css`, and one new image. Nothing else. Commit `90e0877`, with one commit before the change set and one after, per Rule 9.

**Built from the addenda.** The hero action, primary solid, "Read the Achology Story", ArrowDown, smooth scroll to the story, reduced motion honoured. The founders block, portrait left and text right, in its own ruled body so the hairline above and below is the rule components.css already owns rather than a second set of numbers saying the same thing. The closing enquiries panel, the warm tint, the soft circle bleeding off the top right corner, the button to /enquiries/. The phone back-to-top, 46px circle, appearing once the reader is past the hero.

**Built from the spec.** Every one of the five answers now ships in the delivered markup at every width, with each answer emitted directly after its own question, and the first answer open on phone as on desktop. The selector dropped the tablist arrow keys and is an honest accordion. The video lightbox has a real focus trap and makes the page behind it unreachable while it is open. The clipped timeline links leave the tab order while they are clipped and rejoin it when their own milestone is inside the window. The page-updated line sits above the footer and reads from the same two values as datePublished and dateModified, so the page and its schema cannot disagree. The Diploma is the DSRD 5 canonical name in both timeline places, the academy is The Academy of Modern Applied Psychology, Circle is Circle.io throughout. CPD, UK, AI and PRN are spelled out at first body use, and UKRLP now links the register itself. Achologist and membership are each introduced in plain words at first use. All six era ranges read "2012 to 2014". The header image alt no longer claims a scene the photograph cannot establish.

**Also, from the S238 phone-tier sweep brief**, which excludes `.pfq` and `.tw-wrap` from the shared sweep and assigns them here: both now carry 48/48 on desktop and tablet and 32/32 on phone, with the space owned by the element carrying the hairline and the blocks either side contributing zero, per §4.3. One boundary is not fixed and is in the questions file.

**The image.** `kain-and-karen-ramsay-achology-founding-partners.webp`, 720px square, transparency intact, 72KB, descriptive filename set before upload per DSRD 6 §11 item 4. Converted from the supplied PNG with Pillow as a local build tool; no outside code enters the theme (Rule 11).

## Gates that ran

```
css_gate  about.css        PASS
css_gate  style.css        PASS
dash check                 PASS: zero em and zero en dashes in rendered copy
                           (the ten left in page-about.php are all inside PHP comments)
php -l    page-about.php   No syntax errors detected
about.js                   balanced: braces, parens and brackets all even,
                           no unterminated string or comment
```

`page_gate` has not run. It reads the live page, and the page is not live until Kain uploads. Two of its rows, assets-load and links-resolve, still cannot be trusted at all: the instrument defect reported at S043 has had no ruling, and it is repeated in the questions file.

## What I did not build, and why

Everything landing in `shared-parts.php`, because that file renders /testimonials/ as well as /about/, which makes it a two-page change and a sweep under Rule 3. That is the courses card wording, the three gateway rules, the flagship card's Diploma name, the five video labels and the five Vimeo-ID filenames. One sweep brief naming both pages releases all of it in a single pass.

## Next

Kain uploads `achology.zip` (v0.37.0). Then I re-gate the live page, re-walk the changed parts, refresh `RECORD__Page_about.md` in place, and return the rendered page for Safari with the tablet and phone prompt DSRD 6 §11 item 5 requires.

The two S238 sweep briefs that arrived mid-session, the shared separators and the header and footer chrome names, are queued as their own change sets and were not mixed into this one.

*No em or en dashes in this file; checked before writing.*
