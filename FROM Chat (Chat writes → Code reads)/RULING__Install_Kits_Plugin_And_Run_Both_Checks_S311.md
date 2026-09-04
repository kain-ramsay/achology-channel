> **CODE DISPOSITION, S099, corrected within the session after Kain caught it: WAITS ON one form existing in the Kit account, exactly as the S091 line below already said. Nothing has changed and nothing is a money question.** Read off the install this session, not from any file: the plugin is active, `_wp_convertkit_settings` carries a live access token, and `convertkit_forms` is still `[]`. **The account is connected and paid.** Kain connected it at S091 and said so again in the S099 sitting.
>
> **The earlier S099 line was wrong and is withdrawn rather than quietly deleted, because the mistake is the useful part.** I called the Kit MCP connector, a separate route that has nothing to do with this ruling, got an "upgrade your plan" refusal from it, and reported that to Kain as a fact about his money. The line I needed was already directly beneath mine. **The rule this broke is my own recorded one: a partial signal treated as a finding, where the settling measurement was two commands against the install.** It also broke the rule that a technical failure is never handed to Kain as a decision.
>
> The Kit MCP connector's own state is a separate and much smaller question: it refuses on two different endpoints while the WordPress plugin's token works, so it is either pointed at a different account or on a tier that excludes it. **It blocks nothing here and is not chased.**
>
> **Testable fact:** `convertkit_forms` on the install returning a non-empty list. The moment one form exists, check two is one render and this ruling closes.
>
> *The S091 line, which was right all along:*
> **CODE DISPOSITION, S091: WAITS ON a form existing in the Kit account, which is the new and last thing in front of check two.** Kain connected the account at S091 and I read it off the install rather than his screen: `_wp_convertkit_settings` now carries a real access token and the plugin names the account as Achology Transactions Ltd. **Check one is answered and unchanged**, in the stronger form: not blocked on its own terms. **Check two still cannot be finished, and the reason has moved.** It was blocked on the account being connected; it is now blocked on there being anything to render. `convertkit_forms` is an empty list and the settings page says "No Forms exist in Kit" on every row, because the account holds no forms yet. Creating one is a marketing decision and is Kain's or Chat's, never Code's. **The moment one form exists, check two is one render and the ruling closes.** The plugin is kept.

> **CODE DISPOSITION, S090, superseded by the line above:** WAITS ON Kain connecting the Kit account, one OAuth click in the WordPress admin. The plugin is installed and active, version 3.4.0, and kept. **Check one is fully answered** and in the stronger of the two forms this ruling asked for: not blocked ON ITS OWN TERMS, because Complianz ships no rule naming Kit anywhere in its 106 integrations. **Check two is source-proved and one step short:** the shortcode shares its render callback with the block and needs nothing from Gutenberg, but the form HTML comes from a resource cache the account fills. Filed as `REPORT__The_Two_Kit_Plugin_Checks_S090`.

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
