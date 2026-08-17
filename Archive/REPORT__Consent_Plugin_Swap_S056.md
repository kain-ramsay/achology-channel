# REPORT: the consent plugin is swapped, verified against the before state, and one real fault was caught by the swap itself

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Answers:** `APPROVED__Move_Onto_The_Paid_Consent_Plugin_S267.md` and `AMENDMENT__The_Consent_Plugin_And_Key_Are_On_The_Mac_S268.md`.
**Companion file:** `BEFORE_STATE__Consent_Plugin_Configuration_S056.md`, which is the column this whole report is measured against.

**Status: swapped, licensed and verified. Nothing is outstanding on this brief.** The site is running Complianz Privacy Suite premium 7.6.2, licence entered by Kain in session and reading **valid**. Section 8 records the licence step and its verification.

---

## 1. What is running now

| Fact | Before | After |
|---|---|---|
| Plugin | Complianz GDPR/CCPA (free) | Complianz Privacy Suite (GDPR/CCPA) premium |
| Plugin file | `complianz-gdpr/complianz-gpdr.php` | `complianz-gdpr-premium/complianz-gpdr-premium.php` |
| Version | 7.5.2 | **7.6.2** |
| Licence status | not applicable | **`error`, no key entered yet** |

**The answer to the question the brief asked me to establish rather than assume:** the premium edition **replaces** the free one. It is a separate plugin with its own folder, installed alongside, and on activation its own code deactivates and then **deletes** the free plugin. It does not unlock the free plugin in place and it does not run beside it.

I read that behaviour out of the premium plugin's source before installing anything, in `pro/functions.php` and `pro/filters-actions.php`, and then watched it happen. I had deliberately left the free plugin's folder on disk as an instant rollback, and the premium plugin removed it anyway on the next load. That is its designed behaviour, not a fault, and rollback now runs from the backup instead.

**Deleting the free plugin runs the free plugin's own uninstaller**, which wipes the entire configuration if `clear_data_on_uninstall` is set. The before state file records that setting as unset, which I had checked in the plugin's `uninstall.php` before the swap began. Had it been set, the swap would have destroyed the configuration at that moment. That is worth recording as a general rule: check that flag before ever removing this plugin.

---

## 2. The order it ran in

1. The before state recorded, setting by setting, into `BEFORE_STATE__Consent_Plugin_Configuration_S056.md`.
2. **Backup taken** to `~/backups/consent-swap-S056` on the server: the full database, all plugins, all themes, and the generated Complianz assets. Verified rather than assumed: every archive tested for integrity, and the database dump searched for the banner row, Kain's banner copy, the banner title and both statement page pins, all found. The same search was then run against an archive that does not contain them and returned zero, so the test can say no.
3. **The restore route, in one line:** restore `database.sql.gz` with `wp db import`, unpack `plugins.tar.gz` over `wp-content`, then deactivate premium and activate `complianz-gdpr`. It is one command and I hold it.
4. Premium 7.6.2 installed from the archive on the Mac, checksum matched across the transfer.
5. Free deactivated, premium activated.
6. Compared, corrected, re-checked, swept.

---

## 3. The comparison, which is the point of the whole exercise

**Final result: of the 209 settings that exist in both editions, zero have moved.** The banner's 54 columns are identical except one, and the front end is identical across all 303 pages except the plugin folder name in the asset paths.

| What was compared | Result |
|---|---|
| Registered settings present in both editions | 209 |
| Of those, values that differ from the before state | **0** |
| Banner row columns | 54 |
| Of those, columns that differ | **1**, `banner_version` 11 to 12 |
| Public URLs swept | 303 |
| URLs where the banner markup differs | **0** |
| URLs where the theme's footer control differs | **0** |
| URLs where anything else consent related differs | **0** |
| Settings the paid edition adds | 138, all at their defaults |

`banner_version` is Complianz's own internal counter, bumped when it regenerates the banner. The generated stylesheet it regenerates, `banner-1-optin.css`, came out **byte identical, same md5 as before the swap**, so nothing visible moved with it.

**Kain's banner copy, the header, the three button labels, the colours, the corner radii, the font size, the position and the width all survived untouched.** That was the thing most at risk and it is intact.

---

## 4. Three things moved on their own, and one of them took the banner off the entire site

This is the part that matters, and none of it would have been visible without the written before state.

### 4.1 The one that broke the site: `regions`

The premium plugin's upgrade-from-free routine rewrites the `regions` setting from the scalar `"uk"` into the map `{"uk": 1}`. It does this deliberately, in `pro/filters-actions.php`, to support selecting several regions at once.

**The plugin's own `cmplz_has_region()` cannot read the value it just wrote.** That function calls `cmplz_get_regions()`, which returns the option as it stands, and then tests with `in_array( $code, $regions )`, which matches on the array's **values**. The rewritten map holds `uk` as a **key** and `1` as its only value, so `cmplz_has_region('uk')` returned false.

The consequence was total and silent: **the cookie banner disappeared from every one of the 303 pages.** No error, no warning, no admin notice. The page still rendered, the footer control still rendered, the markup simply no longer contained a banner and the banner script was no longer enqueued. A visual spot check of one page would have caught it; a check of the settings screen would not, because the setting looked correct.

Fixed by restoring the before state value, the scalar `"uk"`. `cmplz_has_region('uk')` returns true again and the banner is back on all 303 pages.

**This is a live trap and it needs recording somewhere permanent.** The regions control in the Complianz settings screen is the thing that writes the map form. If Kain or Karen ever opens the region setting and saves it, the banner may vanish site-wide again with no visible symptom in the admin. I have not established which combinations of that screen produce the bad shape, only that the shape produced by the upgrade routine does. **Chat should decide where this belongs, and my suggestion is DSRD 10 section 16 as a second item beside the shortcode trap, because it is the same class of fault: a silent site-wide suppression of the banner.**

### 4.2 GeoIP region detection was switched on

The same install routine sets `use_country` to true and downloads a GeoIP database. Before the swap it was false.

With GeoIP on and only the UK region configured, a visitor detected as outside the UK is served **no banner at all**. Before the swap every visitor got the banner regardless of location. Given the project's requirement that the site be compliant for UK **and EU** visitors from day one, that would have been a compliance regression rather than an improvement, so I restored it to false to match the before state.

**It is worth Kain looking at properly, as an improvement rather than a fault.** The right configuration is probably GeoIP on with both UK and EU regions configured, which is a paid feature doing real work. That is his decision and it is in section 7 below, not acted on.

### 4.3 The privacy statement link came unpinned

`privacy-statement` resolved as `custom` before the swap and as `generated` after it, which would have pointed the banner's privacy link away from the Privacy Policy page.

This is the exact fault DSRD 3 section 6.5 records the S051 fix as having closed: "a statement type with no page set falls through to whatever post happens to be current". The S051 fix stored `cookie-statement` explicitly, and `cookie-statement` survived the swap untouched. **`privacy-statement` was never actually stored.** Its page id was pinned in `cmplz_privacy-statement_custom_page`, but the mode itself was left to resolve, and it happened to resolve to `custom` under the free plugin. So the pin was half applied for months and nobody could have known.

I have now stored the mode explicitly, so both statements are pinned the same way and neither can fall through again. **I did not fully establish why it resolved differently under the paid edition.** The field's default is `custom` in both editions, which I checked, so the flip was not a default change; the install regenerated the documents at that moment and that is the likely cause, but I am not going to state a mechanism I did not prove.

**Chat may want to correct DSRD 3 section 6.5**, which currently reads as though both statements were pinned at S051. Only one of them was.

---

## 5. The DSRD 3 section 6.5 checks, all re-run

Quoted from that section, read from the canonical file this session:

> "the banner appears on first visit with equal-prominence Accept and Decline (button parity per DSRD 7 §5.1's registered consent exception); GTM does not load and no GA4 cookie is set until acceptance; Decline leaves the site fully functional; the choice persists across pages and visits; the footer "Cookie settings" link reopens the banner."

| Check | Result | How |
|---|---|---|
| Banner appears on first visit, Accept and Decline equally prominent | **pass** | Opened the site in a browser. Banner appears bottom right with Kain's copy and three identically styled buttons: Accept All, Reject All, See Preferences |
| No tracker loads before consent | **pass, but see below** | 303 pages swept, zero tracker references and zero scripts held by the blocker |
| Decline leaves the site fully functional | **pass** | Clicked Reject All. Marketing, statistics and preferences all set to deny, functional to allow, page continued to work |
| The choice persists across pages and visits | **pass** | Navigated to another page; banner stayed dismissed and the deny cookies persisted |
| The footer control reopens the banner | **pass** | **Clicked it, did not read it.** The banner reopened and the status cookie went back to `show` |

**The honesty note on check 2, carried forward from the before state file.** There is no tag manager on this site, so the check passes but proves less than it did at S047, when there was something to hold back. I did not install a tag manager to manufacture a demonstration.

**One thing I nearly reported as a regression and was wrong about.** The footer control measured as hidden, and it looked exactly like the failure DSRD 10 section 16 item 7 warns about. It was not. Complianz hides that control below 768px because the banner's `hover-hide-mobile` setting says to, and the browser pane was at a narrow width. At desktop width the control is visible, 100 by 50, and works. The setting is unchanged before and after. Recording it because a careless check would have filed a false alarm here, and because the control renders as a fixed tab at the bottom right of the window rather than as a text link inside the footer, which may or may not be what Kain thinks he specified. **That is a design observation for him, not a defect, and I have not touched it.**

---

## 6. The instruments, and the two tests they had to pass

Three scripts, all read only. All are kept and the after state was produced by the same scripts, unchanged, so the two columns are genuinely comparable.

Every one of them had to do two things before its answers were used, per Kain's standing requirement:

1. **Say the same thing twice on the same input.** The configuration dump and the 303 page probe were each run twice with nothing changed between: byte identical, every time, before and after the swap. The configuration dump **failed this first time**, differing on a cache expiry clock, and transients are now excluded with the reason written beside the exclusion.
2. **Say no on a case already known.** The comparison instrument was given the real dump against a copy with the banner position altered and reported exactly that one line. The page probe was pointed at `robots.txt` and `wp-login.php`, which genuinely carry no banner, and reported it absent on both while reporting it present on the home page in the same run. The backup verification was run against an archive that does not contain the banner copy and returned zero.

**The single most valuable design decision was reading all 209 registered settings through the plugin's own resolver rather than only the stored options.** Complianz stores only what differs from its defaults; the whole of `cmplz_options` was seven keys. A comparison of stored options alone would have shown the privacy statement pin as unchanged, because nothing was stored for it either side. It moved anyway, and only the resolved reading saw it.

---

## 7. What the paid version adds, and what is worth switching on. Answer only, nothing acted on.

Read from the plugin itself rather than from a feature list: 138 new settings and fourteen new code modules. Nothing below has been enabled.

### Worth having, in my order

**1. Records of consent.** Premium logs each visitor's consent as a dated record. The site currently keeps none: `records_of_consent` is `no` and there is nowhere to look if a visitor or a regulator ever asks what a person consented to and when. Under UK GDPR the ability to demonstrate consent is the obligation, not merely obtaining it. **This is the one I would switch on first and the only one I would call close to necessary.**

**2. GeoIP region detection, with the EU added as a second region.** This is section 4.2 turned into a decision. Right now the site targets the UK only and shows every visitor the UK banner, which is safe but blunt. With GeoIP on and both UK and EU configured, each visitor gets the banner and the document set for their own jurisdiction. Given the launch requirement covers EU visitors as well as UK, **the site is arguably under-configured today whether or not GeoIP is used**, because the EU is not a configured region at all. That is worth Kain's attention on its own.

**3. The full site cookie scan.** The free scan covers 50 posts. This site has 303 public addresses. The scan is what keeps the Cookie Policy's cookie table honest as the site changes, and the Cookie Policy makes public claims about cookies that ought to stay true after launch.

**4. Data subject request handling.** A structured route for access and erasure requests, with a form and a register. Achology will get these once it is selling to the public. Not urgent before launch; genuinely useful after.

### Not worth switching on

**Automatic document translation.** The site is English only.

**The German imprint fields, 18 of them.** Only relevant to a German-established business.

**US state privacy law and the children/COPPA set, 14 settings.** The configured region is the UK and the site is not aimed at children. Answering these questions would generate document sections about laws that do not apply, which makes the policies longer and less true, not more compliant.

**IAB TCF.** This is the advertising industry consent framework. The site runs no advertising, and `uses_ad_cookies` is `no`. Switching it on would be actively wrong.

**The processor and data breach registers.** Real obligations, but they are documents about how Achology operates rather than anything the website does, and they belong wherever the company's other operational records live rather than inside a WordPress plugin. Worth a decision by Kain, not a default yes.

**WCAG banner colour checking.** The banner's colours were ruled by Kain's eye and are already recorded. An automated colour checker would only produce an opinion he has already overruled.

### The honest summary

**Two of the additions do real work here: consent records, and proper regional configuration. The rest is either for other jurisdictions, other business models, or work this project already does better by hand.** A small verified configuration beats a large unchecked one, and the swap has just demonstrated exactly why.

---

## 8. The licence: entered by Kain, verified by me

**Done in session, S056.** Kain entered the key himself in WordPress admin, Complianz, Settings, License. Neither Chat nor I handled it at any point, and I never opened the file that holds it.

| Check | Result |
|---|---|
| Key stored on the site | yes, 32 characters |
| Licence status | **`valid`** |
| Plugin version | 7.6.2 premium |

**The status was read with the cached result deleted first.** Complianz caches its licence verdict in a transient, so reading it straight would have returned whatever it last decided rather than what is true now. Deleting the cache and forcing a live check is the difference between asking the plugin and asking the plugin's memory, and this project has been caught by that distinction before.

**Everything was re-verified after the licence went in**, because a licence changes which code paths run:

- The 209 settings shared with the free edition: **still zero moved** from the before state.
- The banner row: still one column moved, `banner_version`, the internal counter.
- All 303 pages swept again: **zero differences** from the before state on the banner markup, the footer control, the manage-consent binding, the blocker, or trackers.
- In a browser, on a cleared session: banner appeared on first visit; Accept All set marketing, statistics and preferences to allow and dismissed it; the footer control reopened it. Clicked, not read.

**Two facts recorded from the earlier unlicensed period, because they matter to the honesty of section 5.** The banner behaved identically before and after the key was entered, so nothing in the verification above depended on the licence. And the key was entered on the second attempt: the first check found no key stored at all, which was reported as a plain negative rather than smoothed over.

**The account question, answered by Kain in session, S056:** the Complianz account is under **manager@achology.com**, which matches the address already registered with the plugin on this site, and he confirms the licence key is in a file in the same folder as the plugin archive. No separate account is involved and nothing here needs Karen.

**One practical obstacle, on his machine rather than the site.** The key file in that folder is `Complianz GDPR premium Key.md`, and on this Mac it exists only as an iCloud placeholder, 179 bytes, never downloaded. It has to be opened once in Finder to pull the real file down before it can be read at all. I have not opened it and will not: a licence key is a credential, and the standing boundary in both the brief and the amendment keeps it out of my hands and out of Chat's regardless of how convenient it would be. Kain enters it himself.

## 9. What I would like from Chat

1. **The regions trap needs a permanent home**, per section 4.1. My suggestion is DSRD 10 section 16, beside the shortcode trap it resembles.
2. **DSRD 3 section 6.5 needs two corrections**, per sections 4.3 and 5: only the cookie statement was actually pinned at S051, not both; and the tag manager clause now describes a check that cannot be demonstrated on this site because no tag manager is installed.
3. **Section 6.5's status line should record 7.6.2 premium**, not 7.5.2 free.

*No em or en dashes in this file; checked before writing.*
