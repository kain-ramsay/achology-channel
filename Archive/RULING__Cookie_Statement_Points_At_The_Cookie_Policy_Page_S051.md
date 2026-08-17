# RULING: the cookie banner's cookie statement points at the Cookie Policy page

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Filed under Harness Rule 14:** a ruling from Kain in session is authority, and
is filed the same session so Chat writes it into its owning document.
**Owning document:** whichever holds the Complianz configuration. It is a
compliance link, so DSRD 3 §3 (Plugins, Security / Compliance) is the closest
home, but it may want a line of its own rather than a mention.

## What was put to him

Reported as found: the cookie banner's cookie statement link was pointing at a
help article, `/help/comparisons-and-alternatives/society-lost-gatekeeping-psychology/`,
on every page. Asked, in one question:

> "Shall I point it at the Cookie Policy page?"

## Kain's ruling, his word in full

> "yes"

## What was done, the same turn

Complianz was never told which page its cookie statement is. With no setting
and no page carrying its shortcode, `get_page_url()` falls through to
`get_permalink( false )`, which returns whatever post happens to be current.
That is why the address moved when the cache was flushed and why it was a help
article: not a drifted post id, an unset setting resolving to an accident.

Two options on the build ground, which is the plugin's own supported route for
an existing page:

- `cmplz_options` key `cookie-statement` set to `custom`
- `cmplz_cookie-statement_custom_page` set to `130`, the Cookie Policy page

Transients and both caches purged after.

**Verified on four page types**, including the help article it was wrong on:

```
/policies/privacy-policy/     -> "Cookie Policy", https://achologytest.com/policies/cookie-policy/
/policies/                    -> "Cookie Policy", https://achologytest.com/policies/cookie-policy/
/about/manifesto/             -> "Cookie Policy", https://achologytest.com/policies/cookie-policy/
/help/.../society-lost-...    -> "Cookie Policy", https://achologytest.com/policies/cookie-policy/
```

The link now also carries its title, which it did not before.

## The sibling, checked and not touched

Checked the other document types in the same pass, as the report said someone
should:

| Type | Setting | Resolves to |
|---|---|---|
| cookie-statement | custom | the Cookie Policy page |
| privacy-statement | custom, with no page set | `#` |
| disclaimer | none | `#`, off on purpose |
| impressum | none | `#`, off on purpose |
| dnsmpd | unset | `#`, US only, region is UK |

**privacy-statement has the same fault and is not fixed**, because Kain ruled on
the cookie statement and nothing else. It is latent rather than visible: no
privacy statement link renders on any page measured. The site has a Privacy
Policy page at id 126. Put to Kain as its own question.

*No em or en dashes in this file; checked before writing.*
