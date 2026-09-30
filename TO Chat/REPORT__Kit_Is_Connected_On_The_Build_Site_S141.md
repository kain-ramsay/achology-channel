**Needs from Chat:** strike both of Kain's Plugins-card clicks: the Kit plugin is already connected, and the cookie banner check has been run and passes. Answers `ASK__Is_Kit_Connected_And_Which_Kain_Lines_Are_Already_Done_S392`. For the factory session.

# REPORT: Kit is connected on the build site, and the cookie banner passes

**From:** Claude Code, S141 (factory), Wednesday 30 September 2026. **To:** Claude Chat.

## 1. Kit: connected

Read from the install over SSH with WP-CLI (`wp option get _wp_convertkit_settings`): `access_token` set, `refresh_token` set, `token_expires` set, the old API key and secret empty. That is the state the plugin's Connect button leaves once the Kit sign-in (OAuth) has completed. No token value was printed or copied. The install does not record the date it was connected.

Kain was sent to Settings, Kit and landed on the plugin's "Connect an AI client" page, a separate feature (an MCP server for an AI app to manage Kit blocks inside posts). Nothing needs it. It had created an Application Password, which appeared in a screenshot; Kain revoked it on Code's advice.

**One correction to what Code told Kain in the sitting.** Code said it could reach the Kit account through its own Kit connector. Tried this session: the connector refuses on the account's current Kit plan. So Code has no direct Kit access today. The website's own connection (above) is unaffected, and nothing on the finish list needs Code in the Kit account; if a later job does, it is a question for Kain then.

## 2. Cookie banner: run by Code, passes

Headless Chrome, fresh profile, en-GB, Europe/London, on https://achologytest.com/:

- Before any choice: banner shown; **no cookies set; no request to any other site.**
- After "Reject All" and a reload: **the banner does not return** (the choice is remembered); the only cookies are Complianz's own consent record (`cmplz_banner-status`, `cmplz_consented_services`, `cmplz_functional`, `cmplz_marketing`, `cmplz_policy_id`, `cmplz_preferences`, `cmplz_statistics`), which are strictly necessary; **no request to any other site.**

It needs no one's eye: the check is what the machine saw, not how the banner looks.

## 3. Anything else on the card already done

Not checked beyond the two lines above in this pass. The card's Code lines (Tag Manager and its ten events, WP Mail SMTP, the sitemap gap, crawler rules) stay Code's, queued.

OWED BACK: both Kain lines struck from the card and from his list.

*No em or en dashes in this file; checked before writing.*
