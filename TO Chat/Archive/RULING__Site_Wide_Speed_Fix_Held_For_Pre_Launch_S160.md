DISPOSITION, Chat S425: archived. The speed fix is a named step on the board card "Pre-Launch Verification | Browsers, Devices, Claims, Checkout End-to-End".

DISPOSITION, Chat S422: stays. Owes Chat: name the site-wide speed fix as a step on the Pre-launch verification card (not checked from here). Waits on: Chat's next board pass in Notion.

First line of need: Chat, attach the site-wide speed fix to the Pre-launch verification card as a named step, on Kain's S160 ruling.

# RULING: the site-wide speed fix is held for pre-launch (theme session, S160)

**For:** Chat. **Session:** theme. **Read from the vault first:** none fit.

## The ruling

Kain, S160 sitting, asked whether the site-wide speed fix should wait: "is this not something that we should do um, pre-launch once all of the website pages have been designed and built? Would that not be a smarter use of time and tokens?" Code agreed (pages still being built would undo the work; the build site has no visitors; DSRD 6 §9 already lets a build-ground speed miss stand until cutover), and Kain said yes to moving it.

So: the theme queue line "One site-wide page speed fix" (found S141) is marked HELD FOR PRE-LAUNCH. It is done once, after every page is designed and built, as a named step of the Pre-launch verification card, with time set aside for it. No theme session takes it before then. Every page's §9 line keeps reading the S141 exception until it is done.

## The fix, as measured on the thank-you page (PageSpeed mobile 77)

Every page loads 15 stylesheets before it can draw: 11 from the theme (830 KB uncompressed; brotli and a year's cache already on) and 4 from plugins. The plan: each page loads only its own type's stylesheet beside the shared ones; knowledge-hub.css (307 KB) split by page type; the first screen's styles inlined, the rest loaded without blocking; minify on deploy; dead CSS removed with css_deletion_proof.py; the Kit plugin's admin quicktags.css and form CSS kept off pages that do not need them; the two main fonts preloaded; PageSpeed mobile on three page families before and after, against DSRD 3 §4.3.

OWED BACK: the step named on the Pre-launch verification card.

*No em or en dashes in this file; checked before writing.*
