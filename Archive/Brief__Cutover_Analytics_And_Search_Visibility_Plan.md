# Brief for Chat — in-site analytics / search visibility, and its cutover steps

From: Claude Code · 2026-07-24
Kain wants planning items like this to live with you (the planning expert), so I'm
handing it over rather than writing a project doc myself. Please fold this into
the cutover / go-live plan you own. Everything below is decided with Kain in this
session; the actions are all cutover-time, nothing has been done to the site.

## What Kain wants
A way to see how the site performs in Google, articles and pages, all inside
WordPress, so he has context for evaluating content, making improvements, and
spotting SEO and GEO opportunities, without logging in and out of Google Search
Console and Analytics separately.

## The decision (locked)
- **Build nothing custom.** Use tools already owned or free/official.
- **Spine: Rank Math Pro's Analytics module** (already installed and active on the
  site as part of Rank Math Pro). Once connected to Google it shows Search Console
  + Analytics data tied to each individual article and page: impressions, clicks,
  ranking position, what's rising/slipping, index status. Covers most of the need.
- **Optional companion: Google Site Kit** (free, official). Embeds Search Console
  + GA4 + PageSpeed into the same WordPress dashboard for the wider traffic/speed
  picture. Add only if the Rank Math view leaves a gap.
- **GEO note:** Rank Math's AI Visibility module is already switched on, which is
  the start of the "how do we show up in AI answers" side. Google's tools don't
  cover GEO; flagging it as its own future thread.

## Why nothing was switched on now (important)
achologytest.com is the BUILD GROUND, not live. It is deliberately walled off from
Google (Discourage search engines on; every page serves noindex/nofollow, I
confirmed this live). Both tools are inert until connected to Google, and that
connection is domain-bound to the REAL achology.com. Connecting the test site
would be throwaway (a code for the test domain doesn't carry to achology.com) and
risks the real site. So we connect nothing here. Since cutover is a clone, any
on-site config travels to achology.com anyway, so there is no benefit to enabling
the empty module now, and a live "Connect Google Services" button would just be an
accidental-connection hazard. We hold it.

## Steps to record on the cutover / go-live checklist (execute on achology.com)
1. On the live achology.com (after cutover), in Rank Math → Analytics, click
   **Connect Google Services** and authorise Search Console + Analytics for the
   achology.com property. (This is the step that makes the in-site dashboard live.)
2. Confirm the Google Analytics (GA4) property and Search Console property both
   exist for achology.com; create/verify if not.
3. Set the **Google Search Console verification code** in Rank Math → General →
   Webmaster Tools for achology.com. (Kain to supply / generate at go-live.)
4. Decide then whether to also install **Google Site Kit** for the fuller GA4 +
   PageSpeed view, and connect it to the achology.com property.
5. Re-check indexing posture at go-live: the live site must have "Discourage search
   engines" OFF (blog_public = 1) so Rank Math's per-type index settings take
   effect. (On the test site this is intentionally ON.)

## What I need from you
Please log these into the cutover plan in whatever structure you and Kain are
using, so the analytics activation is a clean, ordered part of go-live rather than
an afterthought. Ping back via the channel if you want any of the on-site Rank
Math specifics verified, I have live WP-CLI access and can check state directly.
