> **CODE DISPOSITION, S117: DONE.** `REPLY__Real_Amazon_Completions_For_Six_Seed_Terms_Category_Read_Not_Reachable_S117.md`, TO Chat, carries the real completions for all six seed terms (three returned real phrases, three returned genuinely empty, both are results) and names the category-competitiveness half as tried and not reachable (Amazon's best-seller pages refused with a 503; the completion endpoint used for the rest did not).
>
> **Two things noted while reading, so the factory session does not rediscover them.** Section 7 says it is not urgent and not blocking, which is why it waits rather than interrupting. And section 5 is honest that both repos work by calling Amazon's own suggestion feed directly, "outside what Amazon's terms of service intend": the brief records that as Kain's call, already made by commissioning it, so it travels as authorised rather than as an open question. **Testable: archived when the completions for the six seed terms are filed to TO Chat.**

# BRIEF: get real Amazon search data for TULCH's seven keywords and three categories

**DOCUMENT TYPE:** brief, filed by Claude Chat, Session 359, commissioned live by Kain. **Date:** Monday 14 September 2026.
**Commissioned by:** Kain, live, this session: "Code will have no problem getting this data for us. Draft him an instruction to review the two GitHub repos, tell him what we need to achieve."
**What this replaces:** four failed attempts by Chat to reach Amazon's live data this session (browser extension timing out on both the Amazon homepage and a search-results page, a direct fetch to Amazon's suggestion API rejected as an unseen domain, then the same API blocked again on retry through the browser). None of those routes are worth Code repeating; this brief exists because Chat's environment cannot reach this data and Code's may.

## 1. What we're trying to achieve

The Ultimate Life Coaching Handbook (Kindle ASIN B0CGVSWS44, paperback ISBN 9781544544809) is live on KDP. Kain is in his KDP dashboard now, editing its keywords and categories. He wants both built from real Amazon search demand, not from guessed phrasing. Chat guessed twice this session and was rightly called out both times, so this now needs actual data.

**Two things needed back:**

1. **Real Amazon autosuggest completions** for these seed terms (and any close variants you judge worth trying): "life coach", "life coaching book", "how to become a life coach", "self help coaching", "personal development coach", "coaching book for beginners". What we want is the exact list of completions Amazon's own search box offers for each, in order.
2. **Category competitiveness**, if it's reachable the same way or by any other free route you have: for the book's three current live KDP categories (below), whether the #1 book in each category is realistically outranked by a single Handbook, versus buried behind titles selling at a much higher volume.

## 2. What's already fixed and must not change

Book title and subtitle are locked, never touch them: "The Ultimate Life Coaching Handbook: A Comprehensive Guide to the Methodology, Principles, and Practice of Life Coaching."

## 3. Current live state, read off Kain's KDP dashboard this session (screenshot, not guessed)

**Categories (3, live now):**
- Kindle Books > Education & Teaching > Higher & Continuing Education > Adult & Continuing Education
- Kindle Books > Self-Help > Personal Transformation
- Kindle Books > Self-Help > Communication & Social Skills

**Keywords (7, live now, to be replaced):**
- How to Be a Life Coach
- Holistic Life Coaching Book
- How to Become a Life Coach
- Book on Life Coaching
- Life Coaching Books
- Coaching Skills
- Coaching Books

## 4. The one rule already confirmed this session, multi-sourced, so you don't need to re-derive it

Amazon's own stated guidance, quoted directly in one of the sources Chat checked: keywords should not repeat words already in the title, subtitle, or category, because Amazon indexes those already. A word repeated there is a wasted keyword slot. Whatever you bring back, the final seven Chat builds from it will be checked against this rule before they go to Kain.

## 5. The two GitHub repos Kain wants reviewed

- `github.com/joshleitzel/amazon_scraper` — free, pulls Amazon autosuggest data from a query, has a "snowball" mode that expands a seed term into further real suggestions.
- `github.com/drawrowfly/amazon-keyword-scraper-ts` — MIT licensed, free, returns keywords plus the number of active competing products per keyword.

Use whichever gets you real data fastest, or both if that's useful. One honest flag already given to Kain and repeated here: both work by calling Amazon's own suggestion feed directly, which sits outside what Amazon's terms of service intend, and the feed can change or get blocked without notice. That's Kain's call to accept, already made by commissioning this.

## 6. What to send back

The real completions for each seed term, in the order Amazon returns them, plus whatever category-competitiveness read you can get. Send it as a plain list, not built into finished keyword boxes; Chat will build the final seven from your real data and the redundancy rule above, then bring them to Kain to paste in.

## 7. Not urgent, not blocking

Kain is mid-session in KDP right now on other fields while this runs. No rush that breaks anything if this takes a normal turnaround.
