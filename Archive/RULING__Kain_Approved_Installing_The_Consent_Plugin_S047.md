# RULING: Kain approved installing the cookie consent plugin (S047, in session)

**From:** Claude Code, S047. **Date:** 2026-08-05.
**Filed under harness Rule 14:** a ruling Kain gives in a Code session is authority, is acted on, and is filed to TO Chat the same session quoting his words, so Chat writes it into the owning document.
**Owning document:** DSRD 3 section 6.5, and section 3's plugin list.

## What he ruled

Asked whether to build the cookie consent mechanism the Cookie Policy promises, Kain said:

> "Yes. Let's build it. Let's go and work that out, Claude."

Then, presented with the scoping and the Rule 11 question (that installing it means putting outside code onto a site taking card payments, which is his decision and not mine), he said:

> "Yes, install it and set it up"

## What I put to him before he ruled

Stated plainly, so the record shows what he was agreeing to:

1. **This was never a new decision.** DSRD 3 section 6.5 already specifies the whole mechanism and assigns it to me: "Configured and verified by Claude Code as part of the policy-suite build." The Cookie Policy's promises are an accurate restatement of that standard. The standard was simply never built.
2. **The tool was already chosen** in the same section: "Implementation uses Complianz GDPR/CCPA, already in the plugin list (section 3), configured to block GTM4WP until consent."
3. **Rule 11's check, in one line as the rule requires:** the specification already names a maintained public project rather than anything built from scratch, and it is what I proposed using. I verified its health before recommending it: version 7.5.2, last updated 2026-08-03, two days before this session, rated 94 percent across 1,650 ratings, and tested against exactly the WordPress version this site runs.
4. **The site's own versions match its requirements:** WordPress 7.0.2 against a tested-to of 7.0.2, and PHP 8.2.33 against a required 7.4.
5. **Cost:** a few hours of my time and, as far as I can see, no money. I told him I would confirm that before installing and return to him if it changed.
6. **What still comes back to him:** how the banner looks, shown in Safari, because that is a visual decision and his.

## Why this matters to the record

Chat should note that this is not a gap in the documents. Everything needed was written down. What failed is that a specified, assigned piece of the policy suite was never built, and nothing noticed for months, because the page that promises it passes every gate we own. The S047 walk found it by reading what the page says and then checking whether it was true.

That is worth writing into DSRD 3 section 6.5 as a status line, so the next reader can tell a specification from a built thing. My suggestion, offered not decided: the section gains a built-and-verified date once I have finished, and until then says plainly that it is specified and not yet built.

## What is missing from the documents, and needs writing

One genuine gap, small: the "Cookie settings" footer link that DSRD 3 section 6.5 requires is **not registered in DSRD 8 section 19**, which is where footer chrome strings live and which DSRD 6 section 1's chrome carve-out tests labels against. The label itself is specified by DSRD 3 ("a 'Cookie settings' link in the site footer reopens the banner"), so I am building it to that wording rather than inventing one, but section 19's registered set needs the row adding.

*No em or en dashes in this file; checked before writing.*
