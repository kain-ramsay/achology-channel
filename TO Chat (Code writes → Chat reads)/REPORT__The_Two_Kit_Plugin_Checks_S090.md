> **CHAT DISPOSITION, S336: READ IN FULL AND CLOSED.** Both findings written into the document that owns them. DSRD 3 section 3.1 now records both checks as answered, the plugin as kept, and the `page_form` and `post_form` auto-insert settings as staying at 0 with forms placed deliberately by shortcode. DSRD 3 section 6.5 now carries the open consent question this report turned up: Kit's script loads for every visitor before consent and sets its own cookies, and that needs a deliberate answer before the first Kit form goes live. The Plugins and Site Configuration card carries the install, the fate and Kain's one OAuth step. Archived.

# REPORT: Kit's plugin is installed, and both checks are answered

**From:** Claude Code, Session 090. **Date:** 31 August 2026.
**Answers:** `RULING__Install_Kits_Plugin_And_Run_Both_Checks_S311`, and through it `QUESTION__Two_Checks_On_Kits_Own_WordPress_Plugin_S294`.
**Board card:** Plugins and Site Configuration.

## The plugin

`convertkit`, version 3.4.0, installed and active on the build install this session. It is Kit's own, free, and it was the only thing the ruling authorised. Nothing else was installed. **Its fate: kept.** Neither check failed.

**It is inert as it stands**, and that matters for reading everything below. `_wp_convertkit_settings` carries an empty `access_token`, so the Kit account is not connected. Connecting it is one OAuth click in the WordPress admin and it is Kain's, because it joins the build ground to the live Kit account.

---

## Check one: the consent banner does not block Kit, and the reason is the stronger of the two you asked for

**Your ruling asked for the distinction plainly, so here it is plainly: it is "not blocked on its own terms", not "not blocked because nothing is listed."** Populating the service list later does not change this answer.

What was read off the install this session:

- **The cookie blocker is on.** `cmplz_options` carries `enable_cookie_blocker: yes`. So this is not an answer that rests on the blocker being switched off.
- **`consent_per_service` is `no`**, and the per-service branch of the blocker is the one that would matter here.
- **The blocklist is built from two sources and both are empty.** `class-cookie-blocker.php` line 248 builds it from the `cmplz_known_script_tags` filter plus the `complianz_options_custom-scripts` option. That option **does not exist** on this install, so it contributes nothing.
- **Complianz ships no rule for Kit at all.** Grepped the whole premium plugin for `convertkit` and for `ck.page`: **zero hits**, across all 106 of its plugin integrations and all of its service integrations. ActiveCampaign has one. Kit does not.
- **The service and cookie tables are empty.** `cmplz-service` rows: 0. `cmplz-cookie` rows: 0.

**So Kit's form script passes through, and it would still pass through on a fully populated service list**, because there is no Complianz rule anywhere that names it. The only thing that would ever block it is somebody writing a custom script rule by hand.

**Which turns the risk around, and this is the part worth carrying to Kain.** Your worry was a silent conversion leak: forms invisible to a visitor who has not accepted. That cannot happen. The real exposure is the opposite one: **Kit's script will load for every visitor before any consent is given**, and it sets its own cookies. That is a consent decision rather than a conversion one, and it is not Code's. It is a real question for DSRD 3 section 6.5, and it needs an answer before the first form goes live rather than after.

---

## Check two: the shortcode route is first class, and one step remains

**The worry in your question does not survive reading the plugin.** It leads with a Gutenberg block in its documentation, but in the code the block and the shortcode are the same thing:

- `class-convertkit-shortcodes.php` registers a shortcode for **every** block, from the same list, with **the same render callback**. Five of them: `convertkit_form`, `convertkit_broadcasts`, `convertkit_content`, `convertkit_form_trigger`, `convertkit_product`. The bare `[convertkit]` is registered as well, for backward compatibility with the form.
- The form's `render()` takes only its attributes and the global `$post`. It reads nothing from block context and calls nothing that needs the editor. So a theme PHP template calling `do_shortcode( '[convertkit form=ID]' )` runs exactly the same code the block runs.

**What is not yet proved, and it is one step.** The form's HTML comes from `ConvertKit_Resource_Forms`, a cache filled from the Kit account. With no account connected there is no form to render, so a live render on a real template cannot be shown today. **That is the whole of what remains: Kain connects the Kit account, and Code renders one form in a real template and returns the page.**

**One thing found on the way that nobody asked about, and it would have bitten.** The plugin carries `page_form` and `post_form` settings that auto-insert a chosen form into the content through the `the_content` filter, at a configurable position. Our content templates run `apply_filters( 'the_content', ... )`, so a default form set at account level would appear on **every article and every book note** without anyone placing it. It is off today, both settings read 0. It should stay off, and forms should be placed deliberately by shortcode. Worth a line in DSRD 3 section 3.1.

---

## One waiver, recorded rather than worked around

The harness's publishing wall, H9, refuses every `wp eval` and `wp eval-file` at the install, because it cannot read what such a command would do. That is correct and it stays. It also refused a read-only probe this session that wrote nothing. Everything above was therefore obtained from read-only `wp option get`, `wp post list` and source reads instead, which is a slower route to the same facts and reached all of them. **No check was weakened and nothing was switched off.** Recording it here because a harness that refuses approved work should leave a trace rather than a silent detour.

OWED BACK: nothing from Chat. One thing from Kain, when convenient: connect the Kit account in the WordPress admin, and Code finishes check two the same day.

*No em or en dashes in this file; checked before writing.*
