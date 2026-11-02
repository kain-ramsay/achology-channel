ARCHIVED, Chat S452 (2 November 2026): R2 done; Page readiness card updated.

# SHIP 0.707.677: a focused link is no longer hidden under the pinned subject bar (theme, S203, S448 R2)

First line: nothing needed from Chat beyond marking R2 done on its card.

What changed: `kh-subject.css`, one rule beside the pin rule: `html.subj-stick{scroll-padding-top:152px}`. The bar pins under the header and ends at 144 at every width (measured live at 1280 and 375 by pinning it as its script does), plus the 8 gap base.css keeps, the same reasoning as the tag page's 153 (T10).

Proof, read on the build site at 0.707.677: scroll padding 152 on /learn/psychology/, /learn/articles/, /learn/quotes/ and /?s=confidence, each carrying the pinned bar. Not walked live: the Shift and Tab walk itself, because the browser pane used could not scroll the page; the clearance is measured, not walked. Verified by measurement on 4 of 4 pages.

Gate: the edit adds no css_gate line (checked against the committed copy). Theme commit 78f49a55; only the R2 lines went into it, because the small fixes session's R11 lines were in the same file, uncommitted.

For Chat's record, found in passing: a deploy from the shared theme folder sends a stray `.git 2` folder and a `.claude` folder into the server's theme directory, and a deploy from a clean copy deletes them again. Both are refused by the web server's runtime list, but a copy of the repository has no place there. Code will check what `.git 2` is and remove it from the theme folder in the next theme session.

Also for Chat: the S451 instructor brief (87 articles) and the two banned word briefs (27 hub guides, 95 field authority) are passed to the running factory import session, after Kain's seven items, with a note to import any of the eleven course-sentence articles that are among the 87 once, from the current records.

OWED BACK: nothing.
