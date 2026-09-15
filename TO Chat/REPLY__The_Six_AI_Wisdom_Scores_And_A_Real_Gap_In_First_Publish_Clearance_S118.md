# REPLY: the six AI wisdom scores, and a real gap found trying to publish them

**Filed by Claude Code, Session 118. Date:** 15 September 2026.
**Answers:** `RULING__Kain_Says_Publish_The_Six_AI_Wisdom_Articles_At_The_89_Bar_S362.md`.

---

## 1. The six scores

| slug | score | verdict |
|---|---|---|
| ai-agree-with-everything-you-say | 89 | qualifies |
| ai-give-you-a-second-opinion | 89 | qualifies |
| does-ai-actually-understand | 89 | qualifies |
| trust-ai-even-when-its-wrong | 89 | qualifies |
| ai-conversations-get-worse | 88 | held |
| ai-making-us-worse-thinkers | 88 | held |

**The two held pages name no failing test.** Read both in the editor, every section expanded: Basic SEO, Additional, Title Readability and Content Readability all read "All Good" on both. Whatever the missing points are, Rank Math's own UI does not name it on this type. Not naming a cause I cannot show.

## 2. The four that qualify are not yet published, and here is why

`publish_gate.py --clear` refused all four, each on the same shape: 18 failing checks, headed by the page reading as "Page Not Found." Read the raw page myself before trusting that: `curl` on the live address returns 404, because the post is still a draft and nothing measures a draft as an anonymous visitor would see it.

**Traced to the actual cause, not assumed.** `page_gate.py`'s own fetch (`fetch_through_server`) runs a plain, cookie-less `curl` from inside the host. That is deliberate and correct for a published page: it is exactly what the theme's own Antibot-avoidance needs and exactly what a real visitor gets. But a draft returns the same 404 to that curl as it would to a stranger, so every check that reads the rendered page is reading the site's 404 template instead of the article. This is not a fault in the four articles; it is `page_gate.py` having no route to see draft content at all. `capture_page.py`, a different tool in the same folder, already solves this for screenshots by loading through an authenticated Playwright session with minted admin cookies (`score_run.load_cookies()`); `page_gate.py`'s own mirror has never carried that capability.

**Not worked around.** I did not mint a clearance any other way, and I did not touch H9. This is exactly the kind of gap Rule 5 says stops the work rather than inventing a route past it: giving `page_gate.py` a way to measure not-yet-published content is a real capability addition to a safety-critical tool, and it deserves its own theme sitting and review, not a patch improvised at the end of a factory session.

**So, held:** the four qualifying drafts are ready and scored, but not published. Publishing waits on either a way to measure a draft properly, or a named route for a first-time publish that does not depend on the public page already existing.

OWED BACK: how you want the four qualifying drafts published, given the gap above.
