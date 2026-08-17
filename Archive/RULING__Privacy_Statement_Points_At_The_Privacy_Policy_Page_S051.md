# RULING: the privacy statement link points at the Privacy Policy page

**From:** Claude Code, S051. **Date:** 2026-08-08.
**Filed under Harness Rule 14.** Companion to
`RULING__Cookie_Statement_Points_At_The_Cookie_Policy_Page_S051.md`, same
session, same fault, same fix.
**Owning document:** the same one that takes the cookie statement ruling.

## What was put to him

Reported as found during the cookie statement fix: the privacy statement link
had the same fault and resolved to nothing. Asked, in one question:

> "shall I point the privacy statement link at the Privacy Policy page, the
> same as I did with the cookie one?"

## Kain's ruling, his word in full

> "yes"

## What was done, the same turn

`cmplz_privacy-statement_custom_page` set to `126`, the Privacy Policy page. The
`privacy-statement` setting was already `custom`; it simply had no page behind
it, which is why it resolved to `#`.

Transients and both caches purged after. **All five document types read back:**

| Type | Setting | Resolves to |
|---|---|---|
| cookie-statement | custom | https://achologytest.com/policies/cookie-policy/ |
| privacy-statement | custom | https://achologytest.com/policies/privacy-policy/ |
| disclaimer | none | `#`, switched off on purpose |
| impressum | none | `#`, switched off on purpose |
| dnsmpd | unset | `#`, US only, the region is UK |

The cookie statement was re-checked on three page types after this second purge
and is unchanged, so the two settings do not disturb each other.

**Both were latent rather than visible.** No privacy statement link renders on
any page measured today, so nothing was broken on screen. It would have been
the moment anything linked to it.

## The two left at `#`, and why they are not a defect

`disclaimer` and `impressum` are set to `none`, which is a deliberate setting
meaning the site does not publish that document, not an empty one. `dnsmpd` is
the US do-not-sell notice and the configured region is UK. Nothing to do on any
of the three unless the region set changes, and that would be a decision, not a
fix.

*No em or en dashes in this file; checked before writing.*
