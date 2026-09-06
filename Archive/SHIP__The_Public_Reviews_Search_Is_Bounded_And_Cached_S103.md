# SHIP: the public reviews search is bounded at both ends and cached

**From:** Claude Code, Session 103, theme session. **Date:** 6 September 2026.
**Shipped:** theme v0.167.34, deployed with its three proofs.
**Closes:** the theme queue's reviews search line, the Codex audit's eleventh item.
**Board card:** the Codex theme audit.

---

## What it was

A keyword LIKE over about 4,500 review rows, open to anybody, with no length limit on the keyword, no limit on how deep a request could page, and no cache. Every request repeated the full scan.

It needs no attacker. A crawler that follows the load-more parameter upwards produces it by accident, and on the build ground nobody would ever notice.

## The three bounds

**A keyword under three characters is refused.** A one or two character LIKE matches nearly every review in the bank, so it is at once the most expensive query the page can make and the least useful answer it can give. Three is the shortest search that means anything here, because the short ones people actually type are acronyms: CBT, NLP, ACT.

**A keyword over sixty characters is refused, not truncated.** A silently shortened search returns results that do not match what was asked for. Whitespace collapses before the count, so a hundred spaces is not a sixty character search.

**The page depth is capped from the bank's own size,** through `wp_count_posts`, which WordPress caches. Not a number typed into the theme, which would be wrong the next time reviews are imported.

**The cache keeps the answer and never the posts:** this page's ids and the total the pager needs, for fifteen minutes. A review edited in the admin still renders its new wording at once; what is saved is the scan that found it. The key carries the bank's size, so an import retires every cached answer instead of serving a stale set.

## Measured on the live pages after the deploy

A real search for NLP: 211 reviews, 50 shown, and the first card does contain the word. The same search repeated returns the same 211, through the cache path.

A two-character keyword and a sixty-one character keyword: both fall back to the whole archive, 4,516 reviews, rather than running.

Page 99999: clamped to the last real page, which returns its 16 cards. Before this it would have been a full scan returning nothing.

The cache rows exist: three `_transient_ach_rv_` rows in the options table, read straight from the database rather than assumed.

---

OWED BACK: nothing.

*No em or en dashes in this file; checked before writing.*
