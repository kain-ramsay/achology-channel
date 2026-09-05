# SHIP: the small hardening line is closed, and the seven Codex items with it

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Shipped:** theme v0.167.36 and v0.167.37, each deployed with its three proofs.
**Closes:** the theme queue's small hardening line. **With it, all seven Codex audit items are shipped.**
**Board card:** the Codex theme audit.

---

## The three parts

**The analyser feed's half** shipped earlier this session at v0.167.27, riding with the book note cover as the queue line said it should: certificate verification on, the timeout down from ten seconds to five, and a DOM parse in place of the regular expression.

**The buttons and the book cover, v0.167.36.** A button with no type defaults to submit, so each of these would have submitted any form it ever found itself inside instead of doing its own job: the header burger, the mobile navigation's close, and the cookie settings button in the footer. The source book cover in the article callout now declares width and height from ACF's own numbers, so the browser reserves room for it and the callout stops moving under the reader's eye.

**One correction to the audit's count.** It said four untyped buttons. There are three. The fourth, the copy-link button in `knowledge-hub-parts.php`, already carries `type="button"` on the line below its opening tag, which is why a line-by-line read missed it. Five untyped buttons remain on every page and all five belong to the Complianz cookie plugin, not the theme.

**The fallback template and the README, v0.167.37.**

`index.php` was a hard-coded proof page from the first day of the build: a heading reading "The Achology design system is live", a paragraph explaining that if the heading was in Como the stylesheet had loaded, and a button whose address was `#`. It said on its own face that it was temporary, and it was still there two hundred sessions later. It is the template WordPress reaches for whenever nothing more specific matches, so the one page a visitor could land on by accident was a developer's note to himself.

It now lists what the query found, each result's own title linked to itself with its own excerpt, so every word on the page comes from the content rather than from copy Code would have had to write. Where the query finds nothing it hands over to `404.php`, the site's approved answer to arriving somewhere that does not exist. That page's own header says the theme has no search template and that a search would land here, on "a worse dead end than this page". That sentence is now acted on.

**Measured live:** a search matching nothing renders the wayfinding page, its approved heading and its seven doors, at status 200, because an empty archive is not a missing address. A search matching content lists twelve results. No `href="#"` from the theme remains on either.

## The README was wrong in the way documentation goes wrong

It said Kain zips the theme and uploads it through Appearance, Themes, which Harness Rule 12 made a break. It said every file in the folder ships to the website, which the allowlist ended this morning. It carried eleven em dashes against the dash ban.

All corrected, and the correction is dated in the file rather than quietly applied. It now also says the theme is English only, with the evidence rather than the assertion: the text domain is declared in `style.css`, no string is passed through a translation function, and there are no translation files.

## Where the seven items stand

All seven shipped this session: the runtime-only deploy, the reviews dataset off the server, the workbench key, the modal controller, the reviews search bounds, the self-hosted fonts, and this line.

Three things they raised are open and named on the queue: the cutover gate must see the workbench key refused on the live host; the testimonial filter buttons' tab roles; and the policy document reader's missing `inert`. The last two are blocked on the scope wall, waiting on your answer in `SHIP_AND_ASK__One_Modal_Controller_And_A_Close_Button_That_Was_Off_Screen_S103.md`.

---

OWED BACK: nothing on this file.

*No em or en dashes in this file; checked before writing.*
