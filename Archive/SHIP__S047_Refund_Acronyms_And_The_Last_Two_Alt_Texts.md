# SHIP: v0.38.18, the two Refund Policy acronyms and the last two alt texts

**From:** Claude Code, S047. **Date:** 2026-08-05. **Version:** v0.38.18, committed and deployed.
**Executes:** `BRIEF__Refund_Acronyms_And_Two_Extra_OG_Alts_S246.md`, both items, in full.

## Item 1: the two approved phrases, live on the Refund Policy

Placed verbatim into their existing sentences, first appearance only, nothing else on the page touched. Read back off the rendered live page this turn:

> "Nothing here reduces your statutory rights under **United Kingdom (UK)** consumer law."

> "Refunds are made in **United States (US)** dollars, the currency in which you paid."

The three later bare uses of UK stay exactly as they are, per the rule and per your instruction. Dash check on the rendered page after the edit: 0 em, 0 en.

## Item 2: attachments 911 and 908

Both done, identical transformation:

| Attachment | Alt text now |
|---|---|
| 911 | The Achology Manifesto: an ancient handwritten scroll lit in amber against a dark background |
| 908 | The Achology Code of Ethics: an ancient handwritten scroll lit in amber against a dark background |

**Then I checked the whole library rather than just the two.** A scan of every attachment in the media library for either banned character now returns nothing:

```
scan complete
```

So it is ten of ten on the policy family and, more usefully, zero remaining anywhere in the library. Whenever the site-wide OG imagery work wires the Manifesto and Code of Ethics images up, the alt text is already clean and the dash cannot ship.

## The gates after the ship

`page_gate` v5, cache purged before measurement:

```
page                                                       result
------------------------------------------------------------------------------
/policies/refund-policy/                                   PASS  28 pass  0 FAIL  0 review
/policies/cookie-policy/                                   PASS  28 pass  0 FAIL  0 review
------------------------------------------------------------------------------
0 of 2 pages fail
```

`css_gate`: unchanged by this ship. `policies.css` PASS; the three known failures (`cards.css`, `people.css`, `testimonials.css`) are untouched and still stand where they were.

Deployed over SSH under Rule 12, server version confirmed as 0.38.18 before measuring, cache purged. Kain uploaded nothing.

## Where the four walked pages now stand

| Page | Its own defects | What still stands against it |
|---|---|---|
| 1 Privacy Policy | none | footer contrast only (deferred to the design session) |
| 2 Terms and Conditions | none | footer contrast only |
| 3 Refund Policy | none | footer contrast only |
| 4 Cookie Policy | **two acronyms, and the consent mechanism** | footer contrast, plus its own finding |

Three of the four are now clean on their own account, which is the walk doing its job. The fourth is the one that matters: `FINDING__The_Cookie_Policy_Describes_A_Consent_Mechanism_That_Does_Not_Exist.md` is waiting on a decision that is not mine and not yours, and it is the only thing found in this session with consequences beyond the build ground.

Page 5, the Trust Statement, is next.

*No em or en dashes in this file; checked before writing.*
