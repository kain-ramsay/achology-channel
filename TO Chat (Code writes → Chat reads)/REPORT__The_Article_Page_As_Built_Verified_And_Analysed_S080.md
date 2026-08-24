# REPORT: the article page, step 1 verified and step 2 analysed

**From:** Claude Code, Session 080. **Date:** 24 August 2026.
**Under:** `BRIEF__The_Eleven_Knowledge_Hub_Templates_And_The_Redirects_That_Fall_Out_S301`. First of the eleven, taken in Kain's order.
**Steps 3 and 4 have not run.** Nothing has been amended and Kain has not seen a render. Two of the findings below need his ruling before anything is built.

---

## Step 1. What the theme actually holds today

**`single-article.php`, 435 lines**, serving `/learn/{category}/articles/{slug}/`. One template for all Knowledge Hub articles. Read in full this session; nothing below is from a spec or from memory.

Also read: `knowledge-hub-setup.php` for the post type and its fields, `acf-json/group_article_fields.json` for the field contract, and `courses-setup.php` for the course selection the page depends on.

**What it renders, in order:** breadcrumb, hero with category pill and meta line, featured image, article body, author signature card, hairline, Related Further Reading, Source Book Callout, hairline, Explore Related Learning Paths, and then it ends.

**What DSRD 9 §22.1 says it should render:** the same list, plus item 12, the closing "Where next?" panel.

---

## Step 2. Six findings. Four are defects and two are gaps in the specification.

### 1. The closing "Where next?" panel is not built at all

**Kain ruled it onto this page at S272**, on two rendered options of the whole page foot. **He approved its copy word for word at S282**, rendered at 1200, 768 and 390. An approved prototype was filed in the Article Page folder in the same session.

**None of it is in the template.** The page ends on the course card grid, which is exactly the ending he looked at and rejected.

There is a second cost, and §22.10a names it: Row 1 of that panel "closes the source-author back link DSRD 1 §6 requires of every article, quote and book note, **which this page had nowhere else**". So its absence is not only a missing block, it leaves a site-wide cross-linking rule unmet on every article.

### 2. The Source Block has one variant where the ruling gives it two

**§22.9 ruled two variants at S268**, on a four-state comparison Kain judged in the side panel. The book variant and the school variant. The school variant is for "an article with no source book: the 105 school authority articles and the instructor-attributed articles", and the ruling is explicit that it is "not a cosmetic fallback: without it a school authority article carries no link to its own school anywhere on the page."

**The template has only the book variant.** The school variant does not exist in the code.

### 3. When the source book does not resolve, the page presents somebody else's book as though it were the source

This is the one I would fix first if only one could be fixed.

The template falls back to a hardcoded example: **Tasha Eurich's *Insight***, with her name, a written description of her book, and a dead link. It carries the same styling as a real callout and nothing marks it as a placeholder.

So the eighteen instructor articles imported this session, every one of them Gerard Egan's, would each render a source book callout crediting a different author's book. **It would look entirely deliberate.**

A placeholder that announces itself is fine. One that impersonates real content is the fault Kain ruled on at S252, in his own words: "why are you making up course names when you don't need to?"

### 4. The same invented-content fault survives in Related Further Reading

Where the tag and category queries return nothing, the block renders **four hardcoded cards** with invented titles and `href="#"`: *Emotional Intelligence: Why It Can Matter More Than IQ*, *Understanding Emotional Regulation Through Self-Observation*, and two more.

The S252 correction was applied to the course block on this same page and the course block now renders nothing rather than inventing. **This block was left as it was.** The course block's own approach is the answer already agreed on this page.

### 5. The featured image's alt text is discarded at render

The template passes the article's own title as the image's alt, which **overrides whatever alt the image actually carries**.

Two things wrong with it. The authored alt text is thrown away: the eighteen alt descriptions written into `IMAGE_MAP__Eighteen_Instructor_Articles_S298` and verified onto the attachments this session never reach a reader. And a screen reader now hears the article's title twice in a row, once as the H1 and once as the image, which is the redundancy the accessibility chapter exists to remove.

This is the same failure the S300 ASK was worried about, arriving from the opposite direction: the alt did land, and the page throws it away.

### 6. A live contradiction between two DSRDs, on this exact block

**DSRD 9 §22.9 says:** "The school variant takes the brand palette only, never the school colour, per DSRD 7 §2: school colours are exclusive to /academy/ and the Knowledge Hub uses the brand palette."

**DSRD 7 §2 no longer says that.** It was rewritten at S282 on Kain's ruling, recorded in `RULING__The_School_Lockup_Is_A_Site_Wide_Device_S282`: "That rule is superseded. School colour now appears wherever a school is named on a fixed element the reader learns: the school lockup, **the school block on a Knowledge Hub content page**, the school segment of a breadcrumb..."

The school block on a Knowledge Hub content page is this block. **One document forbids the colour and the other requires it**, and this is the block about to be built. It cannot be settled by preference; it is Kain's.

---

## The gap Kain found himself, which the specification does not cover

He asked in session whether the article page needs versions per article type. The answer from DSRD 1 §3.2 is that there are **six** article types, not three, and that they differ in exactly one thing: what the article points at.

| Article type | Points at | Source block variant |
|---|---|---|
| Book-derived | Book note page | book, built |
| Field-authority | School page | school, ruled, **not built** |
| Instructor-attributed | Instructor profile | school, per the S268 ruling |
| Buyer-intent | Course page | **none specified** |
| Video-derived | Course page | **none specified** |
| Author biography | Author hub | not applicable, it is the hub's body |

**Two of the six types point at a course page and no course variant exists**, in the specification or the code. That is a real hole and it is Kain's to fill by eye, not mine to invent.

His instinct that the types differ is right and is already written down. His instinct that this needs several page designs is not what he himself ruled: at S268 he rejected a per-type variant explicitly, because an instructor variant repeated the byline sitting a few centimetres above it. **One page, one block that changes.** That has been put back to him.

---

## What I propose to do, and what I will not touch

**Straightforward, no judgement needed:** stop the alt text being overridden; remove the four invented cards and let the block render nothing when there is nothing real, matching the course block on the same page; build the "Where next?" panel to its approved copy and filed prototype.

**Needs Kain first:** the course variant of the source block, which nobody has designed, and the school-colour contradiction above. Until those two are settled the source block cannot be finished, and the placeholder book stays as the ugliest thing on the page.

**Not mine at all:** the heading shape of the eighteen imported articles, which carry five to seven headed sections against §22.6's ruled four plus an unheaded close. Content, and yours.

*No em or en dashes in this file; checked before writing.*
