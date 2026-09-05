# QUESTION: what does the article page template actually look like today?

**DOCUMENT TYPE:** not a page spec. A read-only question. Nothing here commissions any change.
**From:** Claude Chat, Session 268. **Date:** 2026-08-12.
**Why it is being asked:** Session 268 is designing the Knowledge Hub page set, one page per session, in the numbered order on the board. Page 1 is the article page. Its layout is already LOCKED in the page layout specification document at section 22, and the project record says you built the template complete to that section back in July, with its stylesheet alongside. Your S055 measurement confirms one article post is published and public. So this is a reconciliation, not a fresh design: Kain has ruled that I write the signed spec from section 22 plus everything ruled since, and it is then compared against what is genuinely in the theme.

**What this is for:** the answer becomes the reconciliation column of the article page's signed spec. Where the build and the spec agree, the spec records it. Where they differ, the difference goes to Kain as a ruling rather than being fixed by either of us. Nothing is changed on the strength of this answer until he has seen it.

**Ask for the answer only.** Do not change the template, the stylesheet or any record because of this file. If something in it looks like a defect to you, name it and leave it.

---

## 1. Does it render, and where

- The address of the one published article post, in full.
- Whether that address resolves today at the current deployed theme version, tested rather than assumed.
- The template file and stylesheet that render it, and whether the stylesheet is enqueued conditionally or globally.
- Whether the page carries a readiness record, and if so what its verdict and open lines are.

## 2. The eleven blocks, present or absent

Section 22 lists this order, top to bottom. For each one, say whether the template emits it, and if it does, whether it emits real data or a declared placeholder:

1. sticky header
2. breadcrumb
3. hero, being the category pill, the article title and the meta line
4. featured image
5. article body
6. author signature block
7. hairline
8. Related Further Reading
9. Source Book Callout
10. hairline
11. Explore Related Learning Paths, then rainbow stripe and footer

## 3. The two card rows, which is the part I most need

Section 22 says Related Further Reading uses compact cards and Explore Related Learning Paths uses full course cards, two of them, in a two column grid.

**Kain has never approved either card by eye.** Both are in the seven cards still unruled, so whatever is rendering there today was not signed by him.

- What class families does each of those two rows actually emit right now?
- Is either row a live query, and if so what is it querying on: which taxonomy, which field, what ordering, what fallback when it finds nothing?
- If either is a placeholder, say plainly that it is one.
- Does the further reading row scroll horizontally as the section describes, or has it become a grid?

## 4. What data each slot reads

For every slot on the page that is not fixed template text, name the field, taxonomy or query that fills it, and what renders when it is empty. In particular: the author name in the meta line and in the signature block, the author avatar and bio line, the reading time, the date, the featured image, and the source book callout's cover, title, author and description.

## 5. Everything ruled since July that may or may not have reached this template

Each of these was ruled after the template was built. For each, say whether the article template carries it today:

- the block heading standard ruled at S263, and the seven block heading rewrites you shipped this week
- the icon registry, being whether every glyph on this page comes through the registry function or whether any are still inline
- the ruling that an article shows its category, its school and its courses
- the author attribution key ruling, being the author slug and the people registry rather than WordPress user accounts
- the in body link ceiling and the first mention only register rule, if either applies to Knowledge Hub articles as it does to help articles
- any external link on the page, and whether it carries the four requirements the design foundations document sets

## 6. Two straight questions

- **Was this page ever approved by Kain's eye?** The July record mentions a third round review workflow and a sign off that was still pending. If you can tell from your own records whether that sign off happened, say so. If you cannot, say you cannot rather than reasoning it out.
- **What on this page do you already know is wrong or unfinished?** Your own list, in your own order.

*No em or en dashes in this file; checked before writing.*
