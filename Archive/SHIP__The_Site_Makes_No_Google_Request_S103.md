# SHIP: Mulish and Caveat are self-hosted, and the site makes no Google request

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Shipped:** theme v0.167.35, deployed with its three proofs.
**Closes:** the theme queue's Google Fonts line, the Codex audit's sixteenth item.
**Board card:** the Codex theme audit.

---

## What it was

Every visitor's browser announced itself to Google on every page of this site, before a word was drawn, and the page's appearance depended on another company's server answering. Como has always been served from the theme; Mulish and Caveat were not.

Both faces are Open Font Licence, so both can simply be served from here.

## What shipped

Six woff2 files in the theme's fonts folder, and eight `@font-face` rules in `fonts.css` beside Como's four.

**Latin and Latin Extended only.** Google was also serving Cyrillic, Cyrillic Extended and Vietnamese, twelve blocks of them, to a site that is English only. Those are not downloaded and not declared. A visitor who pastes Cyrillic into a form sees their system font, which is the right outcome for a site with no Cyrillic content.

**The weight ranges and every `unicode-range` are the variable fonts' own,** copied from the stylesheet Google served rather than chosen here: Mulish 300 to 900 upright and italic, Caveat 400 to 600. So every weight the theme sets is still a real cut rather than one the browser thickens for itself, and a browser still skips the Latin Extended file entirely on a page that uses no character from it, which is most pages.

**The two preconnects are gone** from `header.php`. Their own note said to remove them when the fonts went local.

**Nothing was hand written.** A script fetched the served stylesheet with a browser user agent, filtered the subsets, downloaded the files and printed the rules. That matters for the next time a face changes: the job is repeatable rather than a set of values somebody typed once.

## Measured on the live pages after the deploy

All three faces load, from achologytest.com: Como at three weights, Mulish 300 to 900, Caveat 400 to 600.

Caveat loads **only** on the Founders' Letter, the one page that uses it, which is the unicode-range and usage gating working as intended.

A fresh page load makes **no request to googleapis or gstatic**, read from the browser's own network log rather than from the markup.

Grep confirms no reference to either host remains anywhere in the theme.

## One thing for DSRD 3

The old comment in `header.php` called the preconnects "the interim half of the boarded self-host move (DSRD 3; GDPR angle)". That move is now complete. If DSRD 3 still describes the fonts as coming from Google, the sentence needs your rewrite.

---

OWED BACK: the DSRD 3 correction, if that document still describes the old arrangement.

*No em or en dashes in this file; checked before writing.*
