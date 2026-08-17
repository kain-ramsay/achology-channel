# SHIP: v0.38.17, the ICO credential and three acronyms, plus the eight-page alt sweep

**From:** Claude Code, S047. **Date:** 2026-08-05. **Version:** v0.38.17, committed and deployed.
**Executes:** `ANSWER__S047_Walk_Batch_All_Items_S245.md` items 1, 3 and 4. All three are done, live, and read back off the rendered pages.

## What changed

**Item 4, the sub-footer ICO credential (signed sweep, `footer.php`).** The visible link text was "ICO Registered". It now reads the string DSRD 8 s19 registers:

> Registered with the ICO · ZB662679

Read back off the live page:

```
class="footer-ico" href="https://ico.org.uk/ESDWebPages/Entry/ZB662679" target="_blank"
rel="noopener" aria-label="Achology's ICO data protection register entry (opens in a new tab)"
>Registered with the ICO &middot; ZB662679</a>
```

Nothing else moved: the href, the middot, the `aria-hidden` on the separator, the `aria-label` and the new-tab behaviour were already correct and are untouched, exactly as the finding proposed.

**Item 1, three acronyms on the Privacy Policy (`policies-content/privacy-policy.php`).** The copy you approved, placed verbatim into its existing sentences with nothing else changed. Read back off the live page this turn:

- "submit a curriculum vitae (CV) or application materials; or"
- "marketing support, information technology (IT) services, business administration, and technical support"
- "regulatory bodies (such as His Majesty's Revenue and Customs (HMRC)), where disclosure is required"

Worth flagging one thing about where this copy lives, since it bears on the Rank Math score problem: **the policy pages carry no editor content at all.** `wp post get 126 --field=post_content` returns one byte. The copy is in the theme at `policies-content/privacy-policy.php`. That is the same condition recorded against the theme-built pages generally, and it is why the scorer cannot see them.

**Item 3, the eight-page OG alt sweep (WordPress media library, no theme file).** Eight attachment alt texts, the em dash replaced by a colon, which is DSRD 2 s3.0's own first-named substitute. All eight read back off the live pages:

| Page | `og:image:alt` now |
|---|---|
| /policies/privacy-policy/ | Achology's privacy policy: an ancient handwritten scroll lit in amber against a dark background |
| /policies/terms-and-conditions/ | Achology's terms and conditions: an ancient handwritten scroll... |
| /policies/refund-policy/ | Achology's refund policy: an ancient handwritten scroll... |
| /policies/cookie-policy/ | Achology's cookie policy: an ancient handwritten scroll... |
| /policies/trust-statement/ | Achology's trust statement: an ancient handwritten scroll... |
| /policies/disclaimers/ | Achology's disclaimers: an ancient handwritten scroll... |
| /policies/accessibility-statement/ | Achology's accessibility statement: an ancient handwritten scroll... |
| /policies/ | Achology's policies: an ancient handwritten scroll... |

Eight of eight, zero remaining. **Two more attachments carry the same defect and were deliberately left alone**, because your brief named eight pages and Rule 3 means eight. Filed as `FINDING__Two_More_OG_Alt_Texts_Carry_The_Em_Dash.md`.

## The gates after the ship

`page_gate` v5, all three walked pages, cache purged before measurement:

```
page                                                       result
------------------------------------------------------------------------------
/policies/privacy-policy/                                  PASS  28 pass  0 FAIL  0 review
/policies/terms-and-conditions/                            PASS  28 pass  0 FAIL  0 review
/policies/refund-policy/                                   PASS  28 pass  0 FAIL  0 review
------------------------------------------------------------------------------
0 of 3 pages fail
```

`css_gate`: `policies.css` and `footer.css` both PASS, along with about, base, components, fonts, header, help and knowledge-hub. Three files still fail and none was touched by this ship: `cards.css` 7, `people.css` 3, and `testimonials.css` 24, the last held deliberately for the Testimonials pass under your S245 item 6.

## Deployment

Committed as v0.38.17, deployed over SSH under Rule 12, cache purged, and the deployed version confirmed on the server as 0.38.17 before anything was measured. Kain uploaded nothing.

## What this closes

Pages 1, 2 and 3 of the walk now have no open defect of their own. What remains against all three is the footer contrast, which you have deferred to the mega menu and footer design session and which I record by reference from here on, and two approved phrases still needed for page 3 (the first use of UK and the single use of US on the Refund Policy).

Page 4, the Cookie Policy, is next.

*No em or en dashes in this file; checked before writing.*
