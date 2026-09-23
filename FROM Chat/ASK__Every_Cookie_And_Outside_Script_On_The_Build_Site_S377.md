ASK, from Claude Chat to Claude Code, Session 377. Approved by Kain in session. A read-only question: report what the build site sets and loads; change nothing.

# Every Cookie And Outside Script On The Build Site, From The Local Scan

## Why

Kain wants the site's GDPR and cookie wording to be accurate, and a cookie list written from memory or guesswork is exactly what makes a policy wrong. The true list has to come from the install itself. It also supplies the facts for an open ruling in DSRD 3 section 6.5: Kit's form script is not caught by the Complianz blocker and loads before consent, and Kain must decide before the first Kit form goes live whether it is classed as strictly necessary or held back by a hand-written rule. He cannot rule well without knowing what Kit actually sets.

Context from this session, so you know where it lands: Kain ruled that the launch site carries one tracker only (GA4 through GTM4WP, behind Complianz), with advertising pixels added later, retargeting first, on the Advertising Launch Pack card. Rank Math Analytics is now the site's dashboard (DSRD 3 section 6.4); it reads from Google server side and should set nothing on the front end.

## What to run

Complianz's local cookie scan on achologytest.com, which Kain allowed at S056. Do not enable the external server-side scan; that ruling stands. Supplement the scan with your own look at a sample of real pages as a visitor would load them (homepage, a Knowledge Hub article, a book note, a help answer, a page with a Kit form, any page with an embedded video), before and after accepting the banner.

## What to send back

One REPORT in TO Chat with a table, one row per cookie or outside script: its name; who sets it (first party, Google, Kit, YouTube, Vimeo, Bunny, Amazon, Circle, or other); what it is for; how long it lasts; which Complianz category it currently sits in; and whether it loads before consent, after consent, or both. Then, separately:

1. What Kit's plugin sets and loads, with and without the Kit account connected if you can tell.
2. Whether the Amazon link script on book notes (OneLink or Genius Link, per DSRD 2 section 5.1) loads anything on our pages, or only acts on click.
3. How embedded videos are served (standard YouTube, youtube-nocookie, Vimeo, Bunny Stream) and whether Complianz shows a placeholder until consent.
4. Anything loading before consent that is not strictly necessary.

Change no setting. Any fix is a separate brief after Kain rules.

*No em or en dashes in this file; checked before writing.*
