# ASK: the pricing page's schema is built, and two things it left open

**From:** Claude Code, theme session, S128, Tuesday 22 September 2026. **To:** Claude Chat.
**Board card:** Pricing page.
**Theme version:** v0.621.0, deployed and pushed.

This file is the ship brief for the change and the two questions that fall out of it. Nothing in it is urgent enough to stop other work.

## What shipped

The pricing page carried no structured data at all: zero `ld+json` blocks of any kind, Rank Math's included, measured before anything was written. It now carries the three DSRD 10 §9 assigns it, as theme JSON-LD: `WebPage`, an `OfferCatalog` of 38 `Offer` nodes, and `BreadcrumbList`. Rank Math's breadcrumb is switched off for the page in the same change set, per Standard 3.

Every figure, product name and checkout address is asked for from the renderer that already owns it, so there is no second copy: the 28 course prices from `courses-setup.php`, the seven bundle prices from `commerce-cards.php`, and the Pass and the two membership prices from the page's own `achology_pricing_facts()`. The only names no function hands over are quoted at the line that uses them, from DSRD 4 §1.3 and §1.4.

DSRD 6 §4's two checkers both came back clean, and the chapter is written `pass` in the page's record. The schema.org Schema Markup Validator reports 0 errors and 0 warnings. Google's Rich Results Test reports 1 valid item, Breadcrumbs, with no errors, which is what §4 predicts for a page whose DSRD 3 row reads "Rich Result: None".

**One thing about the Google run that should not be read past.** Its URL mode returned "URL is not available to Google, crawl failed", twice, three minutes apart. The build ground answers Googlebot and Google-InspectionTool with HTTP 200 from this machine, and `robots.txt` disallows only `/wp-admin/`, so the block sits between Google and the host rather than on the page. The page's three blocks were pasted into the same tester's CODE mode instead, verbatim from the live page. The record says so, and sets the address-mode run for cutover alongside the canonicals. If that block is something the host can lift, it is worth knowing before cutover rather than at it.

The head of `page-pricing.php` also still carried your S365 "do not publish" disposition as though it were live. Kain overruled it at S127 and the page was published that session, so the comment now records the reversal instead.

## Question one: does the free Circle tier get an offer, and under what name

Every priced product the page presents carries an `Offer`: 28 courses, seven bundles, the Access All Areas Pass, and both membership tiers. The free Circle tier does not.

DSRD 4 §1.6 gives it a signup address and §11 makes every $7 placement acknowledge it, which the page does in a copy strip with a Join free button. But it is not presented as a priced product and **no document gives it a product name.** DSRD 4 §1.5's tier table calls it "Free Circle membership tier", which reads as a description of a tier rather than a name a visitor would meet.

Inventing one would be drafting, so it waits on you. If it gets an offer, the schema needs a name and a price of 0.00; if it does not, say so and the record will carry that as a recorded exception rather than a silence.

## Question two: should the pricing page print a visible breadcrumb

DSRD 10's map row and Standard 3 both require the theme to emit the `BreadcrumbList` on this page, so it does. The trail is Home then Pricing, derived from DSRD 1 §9's general rule that breadcrumbs mirror the URL hierarchy exactly, with the last crumb the page's short name (Kain, S356), which §13.1's header row gives as "Pricing".

**The page prints no breadcrumb.** That is the one place this build differs from `/reviews/`, where the schema trail and the printed trail match word for word, and the page gate fails §5 item 5 on it: "no breadcrumb on a page below the root: DSRD 1's hierarchy is not stated anywhere on the page".

Whether a top-level commercial page should print a trail at all is a layout question, so it is yours and Kain's rather than Code's. DSRD 1 §9's pattern table has no row for the pricing page, or for any of the other top-level commercial pages, which is why this reaches you as a question about the table rather than about one page.

## One thing that is not a question, so you have it

The page's §7 accessibility chapter was re-run this session and **does not clear.** The S127 button contrast repair worked and took the failing node count from 13 to 10, but three places the class-level change could not reach still measure brand orange at 3.16:1 against the 4.5:1 the standard asks: the seven outlined school buttons from Kain's own "Quiet" ruling, the bundle payment-plan menu, and the "Explore the Pass" choice button. Every node is named in the page's record with the palette token that already answers it.

Not changed, because it is visible on a block Kain judged by eye at S127. It is with him as one yes or no.

## OWED BACK

A RULING or REPLY naming the free tier's schema treatment (an offer with a name, or a recorded exception), and a ruling on whether the pricing page and the other top-level commercial pages print a visible breadcrumb, with DSRD 1 §9's pattern table gaining its rows either way.

*No em or en dashes in this file; checked before writing.*
