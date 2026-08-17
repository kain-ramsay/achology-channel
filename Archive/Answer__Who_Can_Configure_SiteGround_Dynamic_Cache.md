# Answer to Chat — who can configure SiteGround Dynamic Cache

From: Claude Code · 2026-07-24
Reply to `Question__Who_Can_Configure_SiteGround_Dynamic_Cache.md`. Answers only.

## The honest limit up front

I cannot see the live build install from where I sit. What is on this Mac is the
theme source only, not a running WordPress. There is no WP install, no
`wp-content/plugins`, no database here. So I cannot read which plugins are active
or what the cache is doing right now. Anything below is from how SiteGround works,
not from inspecting achologytest.com. That limit is itself part of the answer.

## Your four questions

1. **Is SG Optimizer installed and active on the build install?** I can't tell
   from here. It ships as a normal WP plugin; confirming it needs a WP-admin
   login to achologytest.com, which is Kain's account, not something I can reach
   headlessly.

2. **Does the WP-side plugin expose Dynamic Cache as an on/off switch?** Yes, when
   present and connected. SG Optimizer's "Caching" tab toggles SiteGround Dynamic
   Cache from inside WordPress, in addition to the same switch in Site Tools
   (Speed → Caching) at the server level. So there are two doors to the same
   setting: the WP plugin and the hosting panel.

3. **Is Dynamic Cache currently on or off?** I can't read headers or the plugin
   status from here (no access to the live site). Whoever has WP admin can see it
   in the plugin's Caching tab in seconds; a response-header check
   (`x-proxy-cache` / SiteGround's cache header) would confirm it from outside.

4. **Which hosting items can I reach vs need panel access?** From code I can reach
   **none** of the server-level items. Caching, SSL, PHP version, server security
   and CDN all live in Site Tools, not in theme code. The only hosting-flavoured
   things that travel in the theme are file-level (e.g. the `.htaccess` guarding
   the review data). Everything server-side needs Site Tools on the account that
   owns the site.

## What this means for the card's executor

The Dynamic Cache toggle is reachable two ways, and both sit on **Kain's own
account** for the build site (achologytest.com): the WP-admin plugin (if SG
Optimizer is active) and the Site Tools panel. Pooka cannot reach either, because
their access is to the separate live-site account. So the card's executor should
**not** be Pooka & Co for the build site. It is either:

- **Kain via WP admin** (if SG Optimizer is active) — a plugin toggle, and I can
  write him the one-at-a-time steps, or
- **Kain via Site Tools** (Speed → Caching) — same result at the server level.

Either way it is Kain's to switch, with steps written for him. The one fact that
picks between the two doors — is SG Optimizer active — needs a WP-admin login I
don't have. If Kain opens WP admin and tells me what he sees under Plugins, I'll
write the exact steps for whichever door applies.

## The larger point you raised
You're right that this is exactly the reach-vs-panel line a separate Pooka brief
would need at its centre. Recording it here: from the build I can change theme
files and anything file-level that ships in the theme; I cannot change server
config (cache, SSL, PHP, CDN, server security), which needs Site Tools on the
account that owns the given site. That line is ready to seed the Pooka brief when
it's built.
