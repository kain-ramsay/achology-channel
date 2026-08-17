# REPORT: the cookie banner's "cookie statement" link points at a help article

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Found while:** diffing eleven policy pages before and after an unrelated theme
change. It is not caused by that change, and it appears on `/policies/` too,
which that change cannot touch.

## What it is

Complianz prints its configuration inline on every page. Its cookie statement
link is the one the banner sends readers to. On every page measured it now
reads:

```
"cookie-statement":{"title":"","url":"https://achologytest.com/help/comparisons-and-alternatives/society-lost-gatekeeping-psychology/"}
```

It should be the cookie policy. Stable across three separate fetches, so it is
the stored value, not a flap.

## What it was, an hour earlier

The same field on the same pages, captured before I flushed the cache:

```
"cookie-statement":{"title":"","url":"https://achologytest.com/policies/"}
```

So the correct value was the one sitting in the cache, and the flush replaced
it with the wrong one. The stored setting has been wrong for some time and the
cache was hiding it. It is a plugin setting resolving to a post id, and the
help import almost certainly moved what that id points at.

## Why it comes to you rather than being fixed

It is a plugin setting, not theme code, and it is a compliance-facing link, so
it is not mine to change on my own judgement. It also touches a page, and pages
are Kain's. Someone needs to point Complianz's cookie statement back at the
cookie policy and confirm which page it should be, `/policies/cookie-policy/`
or `/policies/`.

Flagging one thing for whoever picks it up: if a plugin's stored page id has
drifted, the same drift may sit in its other stored ids (privacy statement,
impressum). Worth checking the set rather than the one field.

Nothing of mine is blocked by this.

*No em or en dashes in this file; checked before writing.*
