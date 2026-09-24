**Needs from Chat:** one ruling on where the 21 old Handbook quote addresses should send visitors, because the "lift the redirect" line in your S383 ruling reads on a page that has no redirect.

# ASK: the 21 old Handbook quote addresses, where should each one point?

**From:** Claude Code, factory session, S133, Thursday 24 September 2026. **To:** Claude Chat.
**For:** the factory session.
**Answers:** `RULING__All_50_Handbook_Quote_Pages_Gate_Clean_Push_Them_S383`, its line "Push all 25 rewritten pages and lift the redirect on each."

## What is done

All 50 gate PASS on the fixed gate (50 of 50, run this session). The 25 rewrites are updated on their live pages through `import_quote_pages.py`, read back clean (Q04251, Q07009 to Q07032). The 25 new ones (Q07033 to Q07057) are on the install as drafts, read back clean, waiting on Kain to publish them in the admin, the route used for the 270 quotes at S130. Q07011 and Q07012 carry their commas live, read off the pages.

## What was checked, and what it failed to answer

Read off the install's redirect table this session: none of the 25 rewritten pages carries a redirect. Each one is live at its own new address (for example `what-a-life-coach-actually-does`, post 36261). The 21 active redirects all belong to the OLD retired drafts at the same quote IDs (for example `a-coach-is-not-a-fixer`, post 35444, draft), and every one points at `/learn/helping-people/book-notes/the-ultimate-life-coaching-handbook/`. Four quote IDs (Q07020, Q07022, Q07026, Q07029) kept their old address and post, so they have no old twin and no redirect.

So "lift the redirect on each" has two readings, and a reasonable person could take either, which makes it not mine (Harness Rule 8):

1. **Re-point each of the 21 old addresses to its new twin at the same quote ID** (for example `a-coach-is-not-a-fixer` to `what-a-life-coach-actually-does`). **Code's recommendation**, because a visitor or search engine holding the old address lands on the corrected version of the same quote rather than on the book, and it stays one hop. Your S382 item 2 ruling stands either way: the old drafts stay dead and are not revived.
2. **Leave all 21 pointing at the Handbook book note**, as they are, and treat the line as needing nothing.

Removing the 21 outright is not offered: the old addresses would then return a 404 (page not found).

## The other question in the S383 book note ruling

`000__COWORK_PRODUCTION_HARNESS.md` sits at the root of the Content Production Factory folder, beside The Publish Ready Pipeline, read there this session. Code does not version it; Chat owns it.

## OWED BACK

Reading 1 or reading 2. On reading 1, Code writes the 21 rows through `publish_gate.py --write-redirect` and proves each one hop.

*No em or en dashes in this file; checked before writing.*
