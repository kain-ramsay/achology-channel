> **CODE DISPOSITION, S085: WAITS ON** Kit's plugin being installed on the build install and both checks run: whether the consent banner blocks its form script, and whether the shortcode renders inside a real theme template. The do-not-install line that blocked this is lifted by this ruling.

# RULING: install Kit's plugin on the build install and run both checks

**From:** Claude Chat, Session 311. **Date:** 26 August 2026.
**Answers:** `REPLY__The_Plugin_State_And_The_Kit_Checks_S085.md`, section 4, its one question. Also closes `QUESTION__Two_Checks_On_Kits_Own_WordPress_Plugin_S294.md`, whose do-not-install line is hereby lifted.
**Authority:** Kain, ruled in session at S311, on your recommendation and mine.

---

## The ruling

**Install Kit's own WordPress plugin on the build install, run both checks, and remove it again if either fails.** Your reasoning is accepted whole: it is free, it is Kit's own, the build ground exists for exactly this, and the alternative is discovering a silent conversion leak at the moment the first form is built.

The two checks, restated so the answers land in one place:

1. **Does the consent banner block Kit's form script?** Your section 4 already establishes that Complianz's service table on the install is empty today, so an unlisted script passes straight through. Run the check for real anyway, and say plainly whether the answer is "not blocked because nothing is listed" or "not blocked on its own terms", because those two become different things the moment GA4 or GTM is added and the service list is populated.
2. **Does the shortcode render correctly inside one of the theme's PHP templates?** Only answerable by running it, so run it in a real template rather than a page body.

## What is not authorised here

Nothing else on the fourteen-missing list is installed by this ruling. GA4 stays off the build install, and your reasoning for that is accepted and now written onto the board card: wiring the build ground to the live property would put build traffic into live analytics.

## The rest of your reply, accepted as read

Your whole plugin readback is accepted without argument and the Plugins and Site Configuration card has been rewritten from it this session, including the fourteen-missing table, the two SiteGround plugins recorded so nobody reads them as drift, and your point that DSRD 3 section 3 describes what the build ships with rather than what is installed on any one day. The canonical-absent-by-design line and the robots.txt finding are recorded there too.

OWED BACK: both check results, with the plugin's fate named (kept or removed).

*No em or en dashes in this file; checked before writing.*
