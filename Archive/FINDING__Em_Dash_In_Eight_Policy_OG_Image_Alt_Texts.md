# FINDING: an em dash sits in the OG image alt text of all eight policy-family pages

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.16.
**Found on:** page 1 of the S047 walk, then confirmed by reading all eight live pages.
**Needs:** replacement strings from Chat, or Kain's word that the punctuation is mine to change mechanically.

## The standard

DSRD 2 section 3.0, quoted from the canonical document read this turn:

> "**The dash ban (Kain, S222).** No em dash (U+2014) and no en dash (U+2013) appears anywhere in Achology copy: page copy, articles, headings, metadata, captions, CSV fields and emails alike, across every page and content type this document specifies, with no exception. Use a colon, a comma, brackets or a full stop instead. The check is mechanical: a piece containing either character is not ready."

Metadata is named explicitly.

## What is there

Every one of these carries a literal U+2014. Read off the live pages this turn:

| Page | `og:image:alt` |
|---|---|
| /policies/privacy-policy/ | Achology's privacy policy [EM DASH] an ancient handwritten scroll lit in amber against a dark background |
| /policies/terms-and-conditions/ | Achology's terms and conditions [EM DASH] an ancient handwritten scroll lit in amber against a dark background |
| /policies/refund-policy/ | Achology's refund policy [EM DASH] an ancient handwritten scroll lit in amber against a dark background |
| /policies/cookie-policy/ | Achology's cookie policy [EM DASH] an ancient handwritten scroll lit in amber against a dark background |
| /policies/trust-statement/ | Achology's trust statement [EM DASH] an ancient handwritten scroll lit in amber against a dark background |
| /policies/disclaimers/ | Achology's disclaimers [EM DASH] an ancient handwritten scroll lit in amber against a dark background |
| /policies/accessibility-statement/ | Achology's accessibility statement [EM DASH] an ancient handwritten scroll lit in amber against a dark background |
| /policies/ | Achology's policies [EM DASH] an ancient handwritten scroll lit in amber against a dark background |

The dash character is written out in words above so this file does not itself breach the ban.

The strings live in the WordPress media library as each attachment's alt text, which Rank Math reads into `og:image:alt`. They are not in the theme.

## Why no gate caught it

`page_gate`'s dash check reads the rendered visible text of the page, and these strings never render: they are attribute values in the head. The dash sweeps that cleaned the site's copy swept content, not media library fields. Nothing we own has ever read this surface.

Worth Chat noting for the standard: this is the second defect found on page 1 that lives in a surface no instrument reads. The first is the footer contrast, filed separately.

## What I propose, and what I am not doing

Rule 8 puts every published word with Chat, metadata text included, so I am not rewriting these. The mechanical fix is one character each: the em dash becomes a colon, which is the first substitute DSRD 2 section 3.0 itself names, giving for example:

> Achology's privacy policy: an ancient handwritten scroll lit in amber against a dark background

If Chat confirms that reading, or Kain says the substitution is mine to make, it is eight WP-CLI updates and a re-read of all eight pages to prove it. Under Rule 3 that is a sweep across eight pages and needs a signed brief naming them, so a line in the reply authorising it is what unblocks it.

Two related observations, offered as information and not raised as gaps, since OG imagery is handled site-wide:

1. /manifesto/ , /code-of-ethics/ and /instructors/ emit no `og:image` at all.
2. /help/ and the ten people profiles fall back to `Achology-OG-Default-Image.png`.
3. /about/ , /about/founders-letter/ and /testimonials/ carry alt text that names the page rather than describing the image ("About", "Founders' Letter", "testimonials").

*No em or en dashes in this file; checked before writing.*
