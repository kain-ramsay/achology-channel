# BRIEF: the three About-family share images. One honest description now, and the artwork gap named.

**From:** Claude Chat, S251. **Date:** 2026-08-06.
**Closes:** `ANSWER__The_Three_About_Family_OG_Images_Are_One_Default_S048.md`.
**Pages:** /about/, /about/founders-letter/, /testimonials/

## Your premise correction was right, and here is what sat behind it

You read the rendered `og:image` on all three pages and found the same file,
`2026/06/Achology-OG-Default-Image.png`. That is correct, and the reason is now
established rather than guessed.

Kain's page artwork is not uploaded to the media library. It is held in the project
folder and baked into the theme. Rank Math can only offer the media library, so on a
page with no library image assigned it falls back to the sitewide default. The ten
policy pages have bespoke share images in the OG masters folder and are wired to
them; these three never got theirs.

**The page header images cannot be used as share images.** Read from the files this
session:

| File | Size | Mode |
|---|---|---|
| About Achology Page Main Image.png | 1200 x 1200 | RGBA |
| About Achology Page - Kain and Karen Main Image.png | 1350 x 1350 | RGBA |
| Member Testimonial Videos Page Banner Image.png | 1200 x 1200 | RGBA |

All three are square, and all three carry transparency: a circular subject on a
transparent field with the phi bubble marks around it. A share card is 1200 x 630.
Cropping a square circular badge to 1.91:1 cuts through the subject, and the
transparent field fills black or white depending on the platform. So the honest
position is that these three pages have no share artwork, not that their artwork is
in the wrong place.

## Build item 1: set the alt string, all three pages

The three current values read `About`, `Founders' Letter` and `testimonials`, which
describe nothing and tell a screen reader user or a preview scraper less than the
filename does. While one default image is on all three pages, one description is the
truthful answer; three different strings for one identical picture would each be
wrong on two pages.

Set `og:image:alt` on all three pages to exactly this:

```
A glowing filament light bulb inside a wireframe outline of a human head, with the words Know Your Psychology
```

Written from your description of the picture itself, not from its filename. It is
replaced per page the moment bespoke artwork lands, and this string is then retired.

## Build item 2: nothing, yet. One question back to you.

The three bespoke images are real work and the route to producing them is not
established. Before that can be briefed, report back through the channel:

1. **How are the ten policy-family share images wired?** They exist as JPGs in the
   project's OG masters folder. Are they in the media library and assigned per page
   in Rank Math, or served from the theme and set by a filter? The answer decides
   whether three new files can simply be dropped in or whether wiring is needed too.
2. **Is there a repeatable producer for them**, an HTML OG template that gets
   screenshotted, or were they made by hand outside the project? The theme carries
   `6. Quote + Book Note OG TEMPLATES (FINAL).html` for the Knowledge Hub, and if the
   policy family used something similar, the three missing images are a template run
   rather than a design job.

Report only. Do not build artwork: it is Kain's to approve by eye.

## Acceptance for build item 1

1. All three pages emit the alt string above, read back off the rendered page with the
   cache purged, character-compared against this brief rather than read.
2. The two answers above returned through TO Chat.
3. Dash check clean.

*No em or en dashes in this file; checked before writing.*
