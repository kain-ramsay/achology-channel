# BEFORE STATE: the consent configuration exactly as it stands, before anything is touched

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Answers:** `APPROVED__Move_Onto_The_Paid_Consent_Plugin_S267.md`, step one.
**Purpose:** Kain's instruction is that the paid plugin ends up "configured exactly the same way". This file is the thing that sentence gets checked against. Nothing in it is written from memory; every value was read off the live build site this session by an instrument, and the instruments were tested before their answers were trusted.

**Nothing has been changed on the site. This is a read only record.**

---

## 1. What is running right now

| Fact | Value |
|---|---|
| Plugin | Complianz GDPR/CCPA Cookie Consent (the free edition) |
| Plugin file | `complianz-gdpr/complianz-gpdr.php` |
| Version | 7.5.2 |
| Status | active |
| Licence | none, this is the free edition |
| First installed version recorded | 7.5.2 |
| Activation timestamp recorded | 1785961812 |
| Site | achologytest.com, the build ground |
| WordPress | 7.0.3 |
| PHP | 8.2.33 |
| Theme | achology 0.60.17 |
| Database table prefix | `qbk_` |

Complianz owns four database tables here: `qbk_cmplz_cookiebanners` (1 row), `qbk_cmplz_cookies` (0 rows), `qbk_cmplz_services` (0 rows), `qbk_cmplz_dnsmpd` (0 rows). The three empty ones are empty because no cookie scan has ever been stored and no third party services are declared; that is a fact about this site, not a fault.

---

## 2. How this record was taken, and why it can be trusted

Three instruments, all read only, all kept in the session scratchpad:

- **`cmplz_dump.php`** reads every Complianz option, every row of every Complianz table, and **every one of the 209 registered settings resolved through the plugin's own API**.
- **`cmplz_frontend_probe.php`** fetches 303 live URLs from the server itself and records, per URL, whether the banner is in the markup, the theme's footer control markup in full, which banner id it binds to, how many scripts the cookie blocker is holding, and whether any tracker is present.
- **`cmplz_diff.py`** compares two dumps and prints a two column before and after table.

**Why the resolved settings matter more than the stored ones.** Complianz stores only the values that differ from its own defaults: the whole of `cmplz_options` is seven keys. So a default could move between the free and paid editions and the site's behaviour would change while no stored row moved at all. Reading all 209 registered settings through the plugin's own resolver closes that hole. This is the single most important thing in this file, because a comparison of stored options alone would have read clean over exactly the change we are most exposed to.

**The instruments were made to fail before they were believed.** Two tests, on Kain's standing requirement:

1. **Same answer twice on the same input.** The configuration dump was run twice with the site untouched: byte identical. The front end probe was run twice across all 303 URLs: byte identical. The first attempt at the configuration dump **failed** this test, differing on `_transient_timeout_cmplz_cookies`, a cache expiry clock. Transients are caches rather than settings, so they are now excluded, and that exclusion is written in the script beside the reason.
2. **A no on a case already known.** The comparison instrument was given the real dump against a copy with one known value altered (the banner position) and reported exactly that one line and nothing else. The front end probe was pointed at `robots.txt` and `wp-login.php`, two addresses that genuinely carry no banner, and reported the banner absent on both while reporting it present on the home page in the same run.

---

## 3. Region, consent model and documents

| Setting | Value |
|---|---|
| Regions configured | `uk` (United Kingdom only) |
| Company country | `GB` |
| Consent type for region `uk` | **optin** |
| Consent type for country `GB` | **optin** |
| Behaviour for visitors outside the region | `none` |
| Region redirect | `no` |
| EU consent regions | `no` |
| UK consent regions | `no` |
| Consent cookie lifetime | **365 days** |
| Cookie domain | not set |
| Set cookies on root | not set |

Opt-in is the model PECR requires and the model the Cookie Policy promises. It is evidenced twice over: by the resolver above, and by the generated stylesheet on disk being named `banner-1-optin.css`.

**The two statement links, pinned rather than left to resolve.** This is the S051 fix recorded in DSRD 3 section 6.5, and it is still in place:

| Document | Mode | Points at | Live address | Status |
|---|---|---|---|---|
| cookie-statement | `custom` | post 130, "Cookie Policy" | https://achologytest.com/policies/cookie-policy/ | publish |
| privacy-statement | `custom` | post 126, "Privacy Policy" | https://achologytest.com/policies/privacy-policy/ | publish |

Disclaimer, impressum and dnsmpd are unset on purpose, per that same section.

---

## 4. The banner, setting by setting

One banner exists, id **1**, titled **"Achology consent bar"**, marked as the default, banner version 11.

### 4.1 Behaviour

| Setting | Value |
|---|---|
| Banner disabled | no |
| Position | `bottom-right` |
| Banner width | 526 |
| Animation | `none` |
| Box shadow | on |
| Header and footer shadow | off |
| Close button | off |
| Soft cookie wall | off |
| Dismiss on scroll | off |
| Dismiss on timeout | off |
| Dismiss timeout value | 10 |
| Categories shown | `view-preferences` |
| Checkbox style | `slider` |
| Manage consent control | `hover-hide-mobile` |
| Legal document links shown | yes |
| Logo used | no (attachment id 0) |
| Custom banner CSS enabled | **no** (the field holds Complianz's commented scaffold with every rule empty, so it does nothing) |
| Width correction disabled | no |
| Preview hidden | no |

### 4.2 Every word on the banner

| Slot | Text | Shown |
|---|---|---|
| Header | We use Cookies to Improve Your Experience | yes |
| Message (opt-in) | Here's our cookies policy (as required by law). Cookies are both biscuits and safety features. Some cookies keep our website working. The rest tell us which pages are worth improving. Say no to our cookies policy, and nothing breaks, for you or us. | shown in opt-in mode |
| Message (opt-out) | To provide the best experiences, we use technologies like cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as browsing behavior or unique IDs on this site. Not consenting or withdrawing consent, may adversely affect certain features and functions. | not used at opt-in |
| Accept button | Accept All | yes |
| Deny button | Reject All | yes |
| Save preferences button | Save preferences | n/a |
| View preferences button | See Preferences | n/a |
| Informational accept | Accept | yes |
| Manage consent control label | Cookie settings | n/a |
| Category, functional | Functional | n/a |
| Category, statistics | Statistics | yes |
| Category, preferences | Preferences | yes |
| Category, marketing | Marketing | yes |

The four category description paragraphs (functional, statistics, statistics anonymous, preferences, marketing) are all Complianz's own stock wording, all set to show. They are recorded verbatim in the machine dump; they are not reproduced here because none of them is Achology's writing and none has been edited.

**The message and the header are Kain's own words and are the highest risk item in this whole swap.** If the paid edition re-runs its wizard or re-seeds the banner row, that copy is what gets lost.

### 4.3 Colour, type and geometry

| Setting | Value |
|---|---|
| Background | `#354149`, border `#354149` |
| Text | `#FFFFFF`, hyperlinks `#FFFFFF` |
| Toggles | background `#5E6B75`, active `#ED6922`, inactive `#8A9199`, bullet `#ffffff` |
| Accept button | background `#354149`, border `#FFFFFF`, text `#FFFFFF` |
| Deny button | background `#354149`, border `#FFFFFF`, text `#FFFFFF` |
| Settings button | background `#354149`, border `#FFFFFF`, text `#FFFFFF` |
| Banner corner radius | 12px on all four corners |
| Button corner radius | 10px on all four corners |
| Border width | 0 on all four sides |
| Font size | 14 |

The three buttons carry identical colours, which is what makes Accept and Reject equally prominent. That is the button parity carve out DSRD 7 section 5.1 registers as a consent exception, and it is the thing DSRD 3 section 6.5's first check is actually testing.

**A note on where the banner's look really comes from.** Most of the visible design is not in these fields. It is in the theme's own `footer.css`, which styles `.cmplz-cookiebanner.achology-consent-bar` directly. The generated plugin stylesheet on disk is `wp-content/uploads/complianz/css/banner-1-optin.css`, 17,297 bytes, md5 `5768040df2d1b687873f08309f0b1162`. If that file regenerates with different selectors after the swap, the theme's styling is what breaks, not these settings.

---

## 5. What is blocked before consent, measured rather than assumed

**Across all 303 public URLs: zero scripts are being held by the cookie blocker, and zero trackers appear in any page.**

| Measured across 303 URLs | Result |
|---|---|
| Pages carrying the banner markup | 303 of 303 |
| Scripts held as `text/plain` by the blocker | 0 |
| `data-category` blocking attributes | none |
| `data-service` blocking attributes | none |
| Google Tag Manager, GA4, `gtag(`, Facebook, Hotjar, Clarity references | **none, on any page** |

**This is a finding Kain and Chat need, and it changes what one of the DSRD 3 checks can prove.**

DSRD 3 section 6.5 records, from the S047 build, that "GTM does not load and no GA4 cookie is set until acceptance". **There is no tag manager on this site today.** The full plugin list is Advanced Custom Fields Pro, Complianz, Rank Math, Rank Math Pro, SG Security, SG Optimizer, WordPress Starter, WP All Import and the Rank Math import helper. GTM4WP is not installed and not present in the plugins directory at all, active or inactive. There is no mu-plugins directory. Rank Math holds an unconnected GA4 property that belongs to the live achology.com and has no property linked here.

So after the swap I can honestly re-run that check as "no tracker loads before consent", and it will pass, but **its passing will prove less than it proved at S047**, because there is now nothing installed for the blocker to hold back. The blocking configuration itself is recorded above and can be compared setting by setting; what cannot be reproduced today is a live demonstration of a real tag being held. I am not going to install a tag manager to manufacture one. This is named here rather than discovered later, and it is Chat's to decide whether DSRD 3 section 6.5's status line needs re-wording.

**Blocking related settings as they stand:**

| Setting | Value |
|---|---|
| Block WordPress comment cookies | `yes` |
| Block HubSpot service | `no` |
| Block reCAPTCHA service | `no` |
| Consent per service | `no` |
| Consent for anonymous statistics | `yes` |
| Placeholder style | `minimal` |
| Blocked content text | Click to accept {category} cookies and enable this content |
| Blocked content text, per service | Click 'I agree' to enable {service} |
| Per service agree text | I agree |
| Google consent mode | `no` |
| Google basic consent mode | `no` |
| Ads data redaction | `no` |
| URL passthrough | `no` |
| Microsoft Clarity consent mode | `yes` |
| Amazon consent signal | `no` |
| Uses ad cookies | `no` |
| Uses personalised ad cookies | `no` |
| Uses first party marketing cookies | `no` |
| Uses social media | `no` |
| Uses third party services | `no` |
| Active integrations flag | 1 |

---

## 6. Consent record keeping

| Setting | Value |
|---|---|
| Records of consent | **`no`** |
| Proof of consent | not enabled |
| Notifications email | manager@achology.com |
| Send notification emails | on |
| Website scan email | manager@achology.com |
| Website scan signup status | `pending` |
| Website scan status | `pending` |
| Cookie database API sync | `yes` |
| Automatic cookie scan | not disabled |
| Clear data on uninstall | not enabled |

Two administrator consents are stored from the plugin's own onboarding, both dated 2026-08-06, one for its newsletter and one for its website scan terms. They are records of Karen's or Kain's clicks inside the plugin's dashboard, not visitor consent records, and they carry the account email manager@achology.com.

**The website scan is stuck.** The error log on the plugin holds one entry, timestamped 2026-08-12 12:57:21: "cannot retrieve token, email or client id or secret not found". The signup never completed. This is a free edition service and it may simply start working once a licence is present; it is recorded so that if it is still failing afterwards, nobody thinks the swap caused it.

---

## 7. The footer control, and the trap behind it

This is the item DSRD 10 section 16 item 7 warns about, and it is the most likely thing to break.

**What the theme emits**, from `footer.php` lines 179 to 190, unchanged across all 303 pages measured:

```html
<div id="cmplz-manage-consent" class="footer-cookie-settings"><button class="cmplz-manage-consent manage-consent-1">Cookie settings</button></div>
```

The banner id in that class name is **not hardcoded**. It comes from `cmplz_get_default_banner_id()`, which returns 1 today, and the whole control is wrapped in a `function_exists` guard so the footer never renders a control that cannot work.

**The three ways the swap can break this, in order of how quietly they would happen:**

1. **`cmplz_get_default_banner_id()` is renamed or removed in the paid edition.** The `function_exists` guard then evaluates false, the control disappears from the footer entirely, and **nothing errors**. The page still renders, the banner still appears, and the only symptom is a missing line in the footer. DSRD 3 section 6.5's fourth check catches this only if it is actually run.
2. **The paid edition seeds a second banner row and makes it the default.** The control then renders as `manage-consent-2` while the visible banner is still 1, or the reverse. It looks correct and does nothing when clicked. Clicking it is the only way to find out.
3. **`complianz.min.js` changes the selector it binds its reopen handler to.** Same symptom as 2: present, correct looking, dead.

**And the trap the comment in `footer.php` exists to record:** this control is deliberately not the `[cmplz-manage-consent]` shortcode. That shortcode renders `#cmplz-manage-consent-container`, which the plugin's script reads as "a consent management page is open, suppress the banner". Placed in a footer it appears on every page, and the banner would then never show anywhere on the site, silently. If any part of the swap tempts anyone toward the shortcode, the answer is no.

**One pre-existing observation, named and left alone per the brief's scope.** Complianz's own hover tab also renders with `id="cmplz-manage-consent"` on every page, so each page currently carries that id twice. It is a duplicate id in the HTML and an accessibility defect, it exists today before any swap, and it is not mine to fix inside this job. Recorded so the after comparison does not read it as something the swap introduced.

---

## 8. The four checks DSRD 3 section 6.5 records as verified

Quoted from that section, read from the canonical file this session:

> "the banner appears on first visit with equal-prominence Accept and Decline (button parity per DSRD 7 §5.1's registered consent exception); GTM does not load and no GA4 cookie is set until acceptance; Decline leaves the site fully functional; the choice persists across pages and visits; the footer "Cookie settings" link reopens the banner."

Their before state, and what each will be worth after:

| Check | Before the swap | What re-running it after will prove |
|---|---|---|
| Banner appears on first visit, Accept and Decline equally prominent | Banner markup on 303 of 303 URLs; the three buttons carry identical colours | Fully reproducible |
| Tag manager blocked, no GA4 cookie until acceptance | No tag manager installed; no tracker on any of 303 pages | Reproducible only as "no tracker loads", see section 5 |
| Decline leaves the site fully functional | Nothing is blocked, so nothing can break on decline | Fully reproducible |
| Choice persists across pages and visits | Consent cookie lifetime 365 days | Fully reproducible |
| Footer control reopens the banner | Control present and identical on 303 of 303 URLs, bound to banner 1 | Fully reproducible, and must be clicked, not read |

---

## 9. The machine record

The full machine readable dump sits beside this file's instruments in the session scratchpad: 32 option rows, 209 resolved settings, the complete banner row, and the 303 URL front end probe. The after state will be produced by the same three scripts, unchanged, and the comparison will be the two column table this brief asks for.

*No em or en dashes in this file; checked before writing.*
