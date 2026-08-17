# Note for Claude Chat — video schema needs a spec

**From:** Claude Code, 2026-07-22
**For:** the DSRD set (DSRD 10 §9 schema map, and DSRD 3 §5's schema section)
**This is a request for a spec, not a spec. Claude Code writes no DSRD.**

## The gap
The site is about to carry a lot of video — five testimonial videos on the
About page today, and more coming on course pages, the membership page and the
testimonials page. None of it is described to search engines. DSRD 10 §9's
schema-per-page-type table has no `VideoObject` row for any page type, so there
is nothing for the theme to build against.

## Why the Rank Math Video Sitemap module does not solve it
Rank Math Pro has a Video Sitemap module that auto-detects videos and emits
video schema. It detects videos by finding a `<video>` tag or a provider
`<iframe>` in the served HTML. Achology's videos are none of those: they are
buttons (`<button data-video-open="{vimeoID}">`) with a poster image, and the
Vimeo `<iframe>` is only injected into a lightbox on click. So the module would
find zero videos and build an empty video sitemap. The module was left OFF for
this reason (Rank Math config session, 2026-07-22).

The mechanism that works is `VideoObject` JSON-LD emitted by the theme, which
already holds each video's Vimeo ID.

## What chat needs to decide (so Claude Code can build)
1. **Which page types carry video schema** — add the `VideoObject` rows to
   DSRD 10 §9. About page today; presumably course, membership and testimonials
   pages later.
2. **Where the required fields come from.** Google requires `name`,
   `description`, `thumbnailUrl` and `uploadDate` on every `VideoObject`, and
   wants `contentUrl` or `embedUrl` and `duration`. For the About testimonials
   the theme currently holds only the Vimeo ID and a poster image. It does NOT
   hold a per-video title, description, upload date or duration. Decide the
   source of each: hardcoded in the template, an ACF field group, or pulled from
   Vimeo's oEmbed/API at build time. (The testimonial thumbnails do carry a
   printed question each — e.g. "What would you say to anyone thinking of
   studying with Achology?" — which could serve as `name`.)
3. **Sitemap or not.** Once the schema exists, decide whether a video sitemap is
   also wanted. With Pro it can be turned on, but Google treats schema and
   sitemap as two routes to the same end; the schema is the one that earns the
   result. A sitemap is optional belt-and-braces.

## Suggested shape (chat's call, not decided here)
An ACF field group on whatever post types carry video (title, description,
upload date, duration, Vimeo ID, poster), with the theme emitting one
`VideoObject` per video from those fields — mirroring how the FAQ audio and the
Person schema are already handled. But the field source in point 2 is the real
decision, and it is chat's.
