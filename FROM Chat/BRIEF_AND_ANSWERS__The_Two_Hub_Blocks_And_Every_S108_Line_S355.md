# BRIEF AND ANSWERS: the two hub blocks to build and render, and every S108 line answered

**From:** Claude Chat, Session 355. **Date:** Wednesday 9 September 2026.
**Answers:** `RULING__The_Quote_Card_Is_Settled_S108`, `RULING__The_Quote_Page_Carries_The_Course_Slot_S108`, `RULING__The_Quote_Page_Is_Two_Zones_And_Seven_More_S108`, `SHIP__Quote_Page_Source_Card_Fixed_And_Filled_S108`. All four are archived; every correction they asked for is written home.
**Board cards:** Quote page template; the keyword cluster plan, 29 hubs; Author Biography Articles; Book notes.
**Read this cold.**

---

## PART ONE: YOUR FOUR S108 FILES, ANSWERED

### 1.1 The reflection question gains its own field. Kain ruled it.

**The record gains a field. The body does not gain a marker.** The field name is `reflection_question`, which is the name your template already reads first.

His reasoning, recorded: the gate can check a field, a field cannot be lost, and with roughly 7,500 quote pages coming, a guess is wrong on some of them.

Written home at DSRD 10's quote field table and DSRD 2 section 1.1 item 11. **Two consequences, both named there.** The twenty five records already drafted carry the question as their last paragraph and each needs it lifted into the field, which is Cowork's job and is not yours. And **your fallback stays in the template until every record carries the field, then goes.** Do not remove it yet.

**The column contract is yours.** `upload_contracts.json` lives with the importer, so adding `reflection_question` to the quote type's contract is your edit, not Chat's.

### 1.2 Source Sans 3 is corrected out of both documents

DSRD 8 section 20.6 and `RULINGS__The_Quote_Page_S303.md` in the Quote Page folder both now read the site's own body face, with your S103 finding named as the reason. Correction three in that section.

### 1.3 The stale cap: yes, sweep it

**Please do the sweep you offered.** The 120-character cap was a live example of a ruling recorded in a document and never chased into the thing that enforces it, and it cut real quotes for nine sessions.

**One more instance found this session by Chat, in a document rather than in code:** DSRD 10 still described `image_quote_text` as "a 120-character version for image templates". Corrected at S355. So the stale value had spread to two places, not one.

Report what the sweep finds, including nothing, which is a real result.

### 1.4 The four open slots

Recorded at DSRD 8 section 20.6: three of the five closed at your S108 sitting (the four type bands, the share controls, the listen bar) and two stay open, the tag pills on the render and the Wise Quotes lockup, which is an asset nobody has made.

### 1.5 The listen bar has a registry row, and its prefixes are yours

Added to `COMPONENT_REGISTRY.md` at S355. It is a component rather than a token, which answers what Kain asked you in the sitting: it has markup and behaviour, not a value.

**Its class prefixes read TO CONFIRM. Please send them**, so the gate reads its membership correctly and treats its internal spacing as component-internal.

### 1.6 The source card's controls

DSRD 8 section 20.6 now carries the full-width span and the phone stack as part of the ruled definition, with your measurements and your reason. The excerpt sentence is recorded there too: read raw, never through `get_the_excerpt()`, and a missing sentence draws nothing.

### 1.7 One question back to you

**DSRD 7 section 15.2 still lists Canva Bulk Create CSV columns for the quote card.** You have since built a generator. **Which one makes the file now?** Chat left the line alone rather than guess. If the generator has replaced Canva for this template, say so and the line is rewritten.

---

## PART TWO: THREE PUSHES OWED, FROM COWORK'S S354 REPORTS

1. **The twelve biography records.** Cowork found that an earlier pass fixed 27 of 39 and silently missed twelve: Maslow, Schopenhauer, Burchard, Newport, Ariely, Goleman, Fromm, Haidt, Jordan B. Peterson, Tolstoy, Gladwell, Cialdini. All twelve are fixed in the record now, all 51 confirmed at H2. **If `article_body_update.py` already ran against these twelve believing them corrected, the live page carries the broken H3 structure. They need a fresh push, not a skip.**

2. **One sentence onto a live page.** `a-guide-to-rational-living` gains one sentence at the end of its "fair correction" paragraph, cross-linking to the new A New Guide to Rational Living record. Nothing else on that page changed. The record and its master row already agree.

3. **Not a push, a check:** the achologytest.com live page check from S354 (the Shyness title fix, the new cross link) is still unverified. The site approval prompt went unanswered in that session.

---

## PART THREE: THE COMMISSION. TWO NEW ARTICLE BLOCKS, AND THE RENDER

**Authority:** `PLAN__The_Keyword_Cluster_Plan_S351.md`, approved whole by Kain at S351; act 4 of its section 9.

### 3.1 What this is for, in one paragraph

The Knowledge Hub becomes 29 clusters. Each cluster has one long guide at its centre, a hub, and every other piece on that subject is a spoke pointing up to it. A hub is not a new page type: it is an article with a contents list at the top and a gathering block at the foot. Two blocks make the whole thing work, and they are both on the article template.

### 3.2 Block one: the "Part of" line

**Renders on every Knowledge Hub page that is not itself a hub guide. No exceptions.**

One line, reading `Part of the Achology guide to {subject}`, with the subject phrase carrying the link to the hub guide. The subject and its address come from the record's own hub field, never typed per page.

Specified at DSRD 2 section 1.5 item 3a and DSRD 1 sections 3.4 and 6.1.

### 3.3 Block two: the gathering block

**Renders only where the record is a hub guide** (`article_type` `hub-guide`) and draws nothing on any other page, in the same way a missing cover draws nothing rather than a fallback.

Every spoke of the hub, listed by group, at the foot of the page, above the course cards block. Built from the hub field by reverse lookup.

Specified at DSRD 2 section 1.5 item 9a and DSRD 1 sections 3.4 and 6.1.

### 3.4 The hub field on the article post type

Both blocks read it. Its assignment rule is DSRD 2 section 0.0. **A hub guide carries its own hub value**, which is how its gathering block finds its spokes, and it does not render the "Part of" line, because a page does not link to itself.

### 3.5 The render, and why it is yours rather than Chat's

**Kain has one visual decision to make on these blocks: where the "Part of" line sits near the top of an article page.** DSRD 2 section 1.5 records the placement as open and his.

**Chat is not rendering it, and the reason is the two-surfaces rule (standing rule 16, ruled S258).** The dividing question is whether the built theme already holds the thing. The two blocks are new, but **everything they have to be judged against is built**: the breadcrumb, the hero, the meta line, the featured image and the opening of the body. Reconstructing all of that in the Chat panel to place one line inside it is exactly the wrong-surface failure the rule names. So the render is yours, live in Safari, on a real article.

**Chat's call, named here so Kain can overturn it in a line.**

The render standard applies in full: real copy, at the size it will be seen, with what surrounds it present, at desktop, tablet and phone in one look, and **the options tabbed, one on screen at a time in the identical screen position, never side by side and never stacked** (Kain's standing instruction, S277).

### 3.6 The rest of the build, and its order

1. The hub field on the article post type.
2. The two blocks.
3. The render for Kain, and his ruling on the placement.
4. Pillar Content set at import, keyed off the `hub-guide` label.
5. The one line at the end of the course page, when the course page build sitting runs. It is recorded as an amendment in that page's signed spec, section 3a. **It is one line and nothing else on that page moves.**

### 3.7 What is not yours yet

**The hub value on existing records.** Kain ruled at S355 that a record which is not a lecture takes its hub from its `lead_tag`, through a tag-to-hub map. **That map does not exist yet.** Chat writes it, Kain approves it, and only then does the assignment pass run. Do not write hub values onto published records before that.

---

OWED BACK: the class prefixes for the listen bar; your answer on the Canva line; the sweep result; the three pushes; and the two blocks with the render for Kain.

*No em or en dashes in this file; checked before writing.*
