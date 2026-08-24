# BRIEF: the four content templates are yours with Kain. Here is exactly what each one has to build to.

**From:** Claude Chat, Session 303. **Date:** 24 August 2026.
**Approved by Kain in session**, at the close of a design session he stopped because designing these pages in the Chat panel was not working.

---

## The split, ruled by Kain

**Yours with Kain: the four content templates.** Article, book note, workbook, quote. You build each one to the specifications named below, deploy it, and Kain rules whatever is genuinely open on the real page in Safari.

**Mine with Kain: the components, and the pages that list rather than read.** The category hubs, the listing pages, the tag landing pages, the Knowledge Hub homepage.

**Why he split it this way, and it is worth you knowing.** Standing rule 16 divides work by one question: does the built theme already hold the thing? That branch works, and it worked twice this morning on the header. The branch that has never worked is a page template that does not exist in the theme yet, which falls to Chat, in a panel, drawing a page from documents nothing forces it to open. All eleven Knowledge Hub templates fall down that branch, because not one of them is built. Today it produced three quote card options that broke DSRD 7 section 15.2, and Kain caught it with one question.

**So the rule this brief establishes: the first version of a page template that does not exist is built by you, from the specifications that already exist, with no design decisions taken.** The moment it exists, everything afterwards runs the branch that already works.

**Build to spec. Where a spec is silent, leave the slot honestly empty and name it in your report. Do not fill a gap with judgement, and do not invent.** That is the whole discipline here: a page built to what exists, with its holes visible, is exactly what Kain needs in front of him.

---

## 1. The article page

**Fully specified and signed. Build it and nothing else.**

`SIGNED_SPEC__The_Individual_Article_Page_S302`, already in FROM Chat. Thirteen blocks in order, one template for all six article types, two switches both keyed off `article_type`. It carries four rulings Kain took on renders at S302 and it names its own single open item, the featured banner, which stays a placeholder.

**Three corrections from my S303 reply that the sheet does not yet carry:** Related Further Reading is three cards, two on a phone; Explore Related Learning Paths is two at every width, not three at desktop; and author biographies publish as articles on this template, so it serves six types and not five plus an exception.

**Two faults to fix in the same pass, both already briefed:** delete the hardcoded Tasha Eurich fallback book, and stop the featured image's alt text being overridden by the article title.

## 2. The book note page

**Fully specified. DSRD 9 section 32, the go-live spec written across S249 to S251.**

Its travelling shelf panel is DSRD 8 section 20 and is locked, with every value written. Kain approved this page by eye across two sessions.

**One thing to know before you touch the shelf:** the quote page now adopts a horizontal form of it (see 4 below), which under DSRD 8 section 20 triggers the section 12.3 promotion procedure. That runs before either page ships the variant.

## 3. The quote page

**Content specified, layout not. DSRD 2 section 1.1 lists what the page holds. DSRD 9 has no quote page section at all.**

**Build it to what exists, which is more than it sounds:**

- The featured image is the quote card, fully specified at **DSRD 7 section 15.2**: warm cream #FDFAF8, large quote mark top left at eight per cent brand orange, quote in the heading font **never truncated**, author beneath it smaller, the Achology Wise Quotes logo bottom left, three pixel orange bar along the base edge. **Your S301 prototype breaks three of those** and they are named at the foot of this file.
- The Listen player is the one already live on 249 help articles: DSRD 7 sections 5.1 and 5.2, behaviour at DSRD 2 section 2.24. A quote takes the single clip with no follow-along, per DSRD 2 section 1.1.
- Breadcrumb, hero, hairlines, reading column: same as the article page.
- Related Further Reading and Explore Related Learning Paths: same components, same counts as the article page.
- The closing Where next panel: DSRD 8 section 13, copy approved S282.

**Two blocks were ruled by Kain at S303 on tabbed renders.** Both are written in full in `RULINGS__The_Quote_Page_S303.md`, in the Quote Page folder under Knowledge Hub Design Prototypes. Read it there; this file does not copy it.

1. The self-reflection question takes the cream card.
2. The source book block takes the travelling shelf panel laid horizontally.

**Five things are open and they are Kain's to rule on your rendered page, not mine to draw:**

1. The quote written out beneath the card: the registered Pull Quote style (DSRD 7 section 3) or a larger step of its own.
2. The Listen player's attribution row: on a help article it carries Declan Fitzpatrick's photograph because he reads them; a quote is in Kain's voice.
3. Tag pills: DSRD 2 section 1.1 asks for them, DSRD 9 section 22.11 removed them from the article page entirely.
4. The share row: DSRD 2 asks for it, no page on the site has one, and DSRD 3 section 6.2 registers a `content_share` event describing exactly that control.
5. The Where next panel's second row, whose approved copy reads "Explore this article's topics".

**And one that is explicitly yours with him, by the specification's own words.** DSRD 7 section 15.2: the quote card's type step sizes "are not ruled: Kain settles them with Claude Code on the real page with real quotes in Safari". Six of the first twenty five quotes drafted run 121 to 150 characters, so bring long ones.

## 4. The workbook page

**The thinnest of the four, and I am saying so rather than dressing it up.**

DSRD 2 section 1.7 specifies what the landing page holds, including the free-tier download mechanic through Kit. **DSRD 9 has no workbook page section.** The workbook card and the featured workbook card are both approved with prototypes and build sheets in the Card System folder, but they are cards for listings, not this page.

**Build what section 1.7 names, leave everything it does not name visibly empty, and report the gaps.** Expect this page to need the most ruling in Safari of the four.

---

## What comes back, and in what order

**One page at a time, deployed, with its DSRD 6 record.** Take them in the order above: the article page is signed and needs no ruling to start, so it is first and it unblocks the pattern for the rest.

**On each return, name in your report:** every slot you left empty and the specification that is silent on it, and every value you had to read from somewhere other than a specification.

**Do not design any of the four in your own head, and do not ask me to design them.** Kain's ruling: he wants to see real pages in Safari and rule there.

---

## Three breaches in your S301 quote prototype, for correction not criticism

`PROTOTYPE__quote_page_v1.html`, built in a morning to give Kain something to look at, which it did.

1. **The quote card** carries an orange spine down the left edge instead of the three pixel bar along the base edge.
2. **It has no Achology Wise Quotes logo** bottom left. DSRD 7 section 16.2 specifies the mark.
3. **The quote mark sits at thirty five per cent opacity.** Section 15.2 says eight.

And the quote beneath it is set in Como 28px weight 500, which is not a state any document holds. That is open decision 1 above.

*No em or en dashes in this file; checked before writing.*
