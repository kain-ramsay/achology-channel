> **CODE DISPOSITION, S090: DONE.** Superseded by `RULING__Install_Kits_Plugin_And_Run_Both_Checks_S311`, which lifted its do-not-install line, and answered by `REPORT__The_Two_Kit_Plugin_Checks_S090` in TO Chat. Its check one is settled in the stronger of the two forms it asked for. Its check two's remaining step is carried on the ruling, which stays.

# QUESTION: two checks on Kit's own WordPress plugin before we build forms on it

**From:** Claude Chat, Session 294, 20 August 2026
**To:** Claude Code
**Read-only. Two checks and an answer. Nothing to build here.**
**Governing standard:** DSRD 3 **section 3.1**, written this session. Read it from the canonical file; it is the ruling these checks sit under.
**Board card:** the plugins and site configuration card.

---

## The ruling this sits under

Kain ruled at S294 that **every email capture on the site runs through Kit's own WordPress plugin**, the one Kit publishes and maintains itself, free, source public on their GitHub organisation. It replaces the previous unruled working choice of Fluent Forms. Nothing was bought.

His reasoning, plainly: Achology is committed to Kit and pays for Kit, so a Kit-built plugin adds no vendor, no licence and no second system.

**One exception it creates.** The enquiries form is not a subscription: somebody writes a message and it has to arrive at support@achology.com. Kit captures subscribers; it does not deliver a message to an inbox. So the enquiries page carries one small contact form, and that is the only form on the site that is not a Kit form. Choosing it is a separate, smaller decision and is not part of this file.

## Check one: does the consent banner block Kit's form script?

**Why this matters more than it looks.** DSRD 3 section 6.5 has the consent banner holding non-essential scripts until a visitor accepts. If Kit's form script is caught by that blocker, then a visitor who has not yet clicked accept sees **no signup form at all**, on every page carrying one. That is not a visible fault anyone would report. It is a silent conversion leak, and it would run from launch day until somebody happened to notice.

Section 6.5 also records that the blocker only blocks the services its configuration names, currently one entry, so an unlisted script passes straight through. That cuts both ways here and is part of what needs establishing.

**What I need to know.** Whether Kit's form script is caught by the blocker as things stand. If it is, whether it should be classed strictly necessary or stay blocked, and what a non-consenting visitor actually sees where the form should be.

## Check two: does it deliver into a PHP template?

This site is PHP templates, not the block editor. Kit's plugin leads with a Gutenberg block. A shortcode route exists and should serve, but it has never been run on one of our templates.

**What I need to know.** Whether the shortcode renders a Kit form correctly inside one of the theme's own PHP templates, confirmed on a real page rather than reasoned from the documentation.

## What happens with the answers

Both go into DSRD 3 section 3.1, which currently names them as owed. Neither is a reason to choose differently, and neither blocks anything you are working on.

**The fallback if either fails**, so it is on record rather than re-derived: the free WPForms Lite plus Kit's own open-source WPForms integration, which is maintained by Kit and works on a free Kit account. Its one shortfall is that Lite keeps no local copy of a submission, which matters for the enquiries form and not for a signup.

## What this does not ask for

**Do not install anything and do not build a form.** The full list of every place on the site where somebody can give an email address has not been written yet; it is the first task on the Launch Email Set card and it is Chat's. Building before that list exists means building the wrong number of forms.

*No em or en dashes in this file; checked before writing.*
