# REPLY: the plugin state, one line each, read off the install

**From:** Claude Code, Session 85. **Date:** 26 August 2026.
**Answers:** `ASK__The_Plugin_State_One_Line_Each_S307.md` in full, and as much of `QUESTION__Two_Checks_On_Kits_Own_WordPress_Plugin_S294.md` as can be answered without installing anything.
**Board card:** Plugins and Site Configuration.
**Read at:** theme v0.102.1, WordPress on achologytest.com, 26 August 2026. Every line below was read off the install with WP-CLI over SSH. Nothing is from recall.

---

## 1. Everything installed, in full

Nine plugins are active. There are no inactive plugins and no must-use plugins.

| Plugin | Version | Installed | Configured | Verified |
|---|---|---|---|---|
| advanced-custom-fields-pro | 6.8.8 | yes | yes | yes, the article field group is live and read by the templates |
| seo-by-rank-math | 1.0.276 | yes | partly | see section 3 |
| seo-by-rank-math-pro | 3.0.119 | yes | partly | see section 3 |
| complianz-gdpr-premium | 7.6.4 | yes | partly | banner renders; its service list is empty, see section 4 |
| wp-all-import | 4.1.1 | yes | yes | yes, it imported the 250 help answers, the 51 biographies and the 18 instructor articles |
| import-xml-csv-settings-to-rank-math-seo | 1.2 | yes | yes | yes, the SEO columns land on import |
| sg-cachepress | 7.8.2 | yes | yes | yes, the deploy purges through it every ship |
| sg-security | 1.6.5 | yes | default | not verified against any requirement; it is SiteGround's, not on DSRD 3's list |
| wordpress-starter | 3.4.8 | yes | default | SiteGround's own, not on DSRD 3's list |

## 2. DSRD 3 section 3's list, against what is actually there

**On the list and installed:** ACF PRO, Rank Math SEO (and Pro), WP All Import and its Rank Math companion, SiteGround Speed Optimizer, Complianz.

**On the list and NOT installed, fourteen of them:** SearchWP, Kit's own WordPress plugin, the one lightweight contact form plugin for the enquiries form, EWWW Image Optimizer, WP Offload Media, Index WP MySQL For Speed, Wordfence Security, Zero Spam, WP Mail SMTP Pro, GTM4WP, FileBird Pro, WPCode Lite, Members, WP Crontrol.

**Installed and not on the list, two:** sg-security and wordpress-starter, both SiteGround's own and both arriving with the hosting rather than being chosen. Worth a row on the card so nobody treats them as drift.

**The document is not wrong and neither is the install.** Section 3 describes what the build installs and keeps by launch, and most of that set has nothing to do until the pages that need it exist. What the card should carry is the difference, which is the table above, rather than a state line measured on one day in August.

## 3. The card's open items, one line each

**GA4.** Not on the site. Rank Math's analytics option holds an account, a property and the measurement ID `G-HJ29S4Z0R8` for `achology.com`, the LIVE site, but its install code field is empty and no `gtag` or `googletagmanager` appears anywhere in a rendered page, checked on a help answer today. **That is the right state and it should stay that way.** achologytest.com is the build ground; wiring it to the live property would put build traffic into live analytics.

**Google Tag Manager and the ten named events (DSRD 10 section 10).** GTM4WP is not installed, no container is on the site, and none of the ten events is emitted. Nothing on this has started.

**SearchWP and its index.** Not installed. There is no index across the four Knowledge Hub types or the help answers, so the search results page has nothing to read when it is built.

**The SMTP plugin.** WP Mail SMTP Pro is not installed. Nothing on the site sends mail today; the enquiries form does not exist yet, so nothing is broken by its absence.

**Kit's own forms plugin.** Not installed, and its two checks cannot be run. See section 4.

**Image optimisation.** EWWW is not installed and neither is WP Offload Media. The 127 attachments on the install are unoptimised. This is the same ground `COMMISSION__The_Image_And_Icon_Machinery_Both_Halves_S294` covers, and that commission is the better home for it than a plugin row: the standard is DSRD 7 sections 12.3 and 12.4, and a plugin cannot enforce a slot's stated display width.

**Rank Math site-wide configuration.** Schema is configured: knowledge graph type company, organisation name Achology Transactions Ltd, local business type EducationalOrganization, website name Achology, Twitter card summary_large_image. Sitemap is on, 200 items a page, images included, featured images excluded, attachments excluded, author sitemap on. Author archives are disabled and set to noindex. Breadcrumbs are off in Rank Math, correctly, because the theme draws its own. **Search Console is not reconnected**, and that is the same key work as the redirect card.

**The site-wide canonical tag.** Absent by design and correct. `blog_public` is 0, so every page carries `noindex, nofollow` and Rank Math deliberately withholds the canonical. Verified on a rendered help answer today. This is not a defect and it flips at cutover, where `cutover_gate.py --golive` proves it landed.

**Crawler access.** `robots.txt` reads the WordPress default: `Disallow: /wp-admin/` with admin-ajax allowed, and the sitemap named. It does **not** carry a blanket disallow. The noindex meta tag is what is holding the site out of the index, and it is doing it on every page. Worth knowing rather than assuming the robots file is the guard, because at cutover the meta tag is what changes and the robots file already reads as it should.

## 4. The two Kit checks, and why neither can be run

`QUESTION__Two_Checks_On_Kits_Own_WordPress_Plugin_S294` asks two things and, in the same file, says do not install anything. Kit's plugin is not on the install. So both checks are blocked on a decision rather than on work, and that file stays live in FROM Chat head-lined exactly that way.

**Check one, partly answerable and worth having.** Complianz's own service table on the install is **empty**: zero rows. DSRD 3 section 6.5 records the blocker as holding only the services its configuration names, and today it names none. So as things stand an unlisted script passes straight through, and Kit's form script would not be blocked. **That is a fact about today, not a ruling**, and it stops being true the moment GA4 or GTM is added and the service list is populated. The check still has to be run for real once the plugin is on.

**Check two cannot be approximated at all.** Whether the shortcode renders correctly inside one of the theme's PHP templates is answerable only by running it.

**What Code recommends, and it is one question for Kain.** Install Kit's plugin on the build install, run both checks, and remove it again if either fails. It is free, published by Kit, and the build ground exists precisely so that things can be tried without consequence. The alternative is that this question sits unanswered until the first form is built, which is the worst moment to discover a silent conversion leak.

OWED BACK: nothing. The two Kit checks are owed once Kain rules on installing the plugin.

*No em or en dashes in this file; checked before writing.*
