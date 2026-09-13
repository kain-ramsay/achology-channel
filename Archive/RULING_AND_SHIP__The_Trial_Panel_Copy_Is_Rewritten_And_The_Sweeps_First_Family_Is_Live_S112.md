> CHAT DISPOSITION, S357: answered. The two trial panel lines written into DSRD 8 section 16 (the trial variant), superseding the S341 body; the 880 question ruled by Chat, retired, DSRD 7 section 4.1 rewritten. Archived.

# RULING AND SHIP: Kain rewrote the trial panel's two lines, and the sweep's first page family is live

**DOCUMENT TYPE:** ruling and ship brief, filed by Claude Code, Session 112, theme session. **Date:** Sunday 13 September 2026.
**Filed under Harness Rule 14**, which makes a ruling given in session authority at once and owes the record the same session, and under CLAUDE.md's shipping rule, which owes the channel one short brief per change.
**Theme version:** 0.328.0, deployed to the build ground and proved there.

---

## 1. The ruling: both lines of the trial panel are Kain's new words

**He gave them to me whole in the sitting and they are typed character for character. The heading:**

> Experience a FULL Achology membership and its benefits. 30 days for only $7!

**The body:**

> For $7, you gain access to the membership: seven online courses, weekly personal development events, mentorship groups, and the opportunity to apply for free one-on-one coaching. All certificate courses can be purchased separately.

**What they replace:** the heading `Would you like to explore the Achology learning experience and its benefits for 30 days for only $7?` and the body he himself wrote at S341 through `RULING__The_Trial_Panels_Second_Paragraph_Is_Reworded_S341`.

**The S341 rewrite is not discarded, it is satisfied.** That rewrite existed to stop the line reading as though the individual certificate courses came with the $7. The new body keeps the same distinction in shorter words, with its last sentence carrying it.

**Where it lives:** `achology_trial_panel()` in `shared-parts.php`, one canonical place, so every page carrying the panel changed together and nothing was edited page by page. The word Achology keeps its accent span in the heading, per the standing rule, which was not a decision made here.

## 2. The standing instruction behind it, which reaches the rest of the sweep

**Kain asked, in his own words:** *"Is it OK if we just make copy changes as we go through the sweep - the font size change has thrown a few things - which is OK, as we can use this opportunity to tighten the copy anyway."*

**He was told what I can and cannot do with that, and he accepted it:** Code does not draft copy (Harness Rule 8), so the words come from him in the sitting or from Chat through the channel, and Code places them and records them as his. **Where he would rather someone else found the words, the line travels to Chat as a question and the sweep carries on.** So Chat should expect copy questions arriving out of the remaining page families.

**For Chat to write:** nothing in a DSRD, but the two lines above belong in whatever record holds the trial panel's approved copy, replacing the S341 body, and the S341 ruling file is superseded rather than wrong.

## 3. The ship: the sweep's first page family is built, proved and live

**The family is the three reading pages Kain ruled the S111 sitting on:** the Knowledge Hub article, the book note and the help answer.

**What changed, all of it his:**

- The reading text is **18px on 1.75** on all three. Measured on the live page after deploy: 18px, 31.5px leading.
- The reading column is **800px**, one token, `--container-article`, read by 21 rules across nine stylesheets.
- The paragraph gap is **16px** on all three. The book note came off 18 and the help answer off 24.
- **Three heading sizes became one, 24px:** the block heading, the help answer's closing heading and the contents card's heading on the book note.
- The help answer's sub-heading came off 20 to **21**, the size the article's already carried.
- **Twenty-three off-scale sizes came onto the nine steps** across the help family and the reading pages' own furniture, including the four in the contents card, the two breadcrumb rules, the three author-card rules and the two on the quote page.
- The trial panel's own paragraph came off **17 to 18**, which was the last thing on the article page still off the list.

**One decision I took and named to him rather than asking, because it is the kind a render settles and he has not seen the render.** The site-wide `p { font-size: var(--text-16) }` in `base.css` is **left at 16**. An element rule outranks a font-size set on an ancestor, so the reading bodies restate 18 where the cascade can be beaten, exactly as `book-note.css` has done since S050 for the same reason. Raising the site-wide default would move every paragraph on every page family he has not looked at yet, and his own instruction for this sweep was that nothing moves that was not off the family. **Whether the site's default paragraph becomes 18 is a question for a later sitting on a page where it bites.**

**One consequence named rather than discovered later.** The reading column went 880 to 800 and the floated cards inside it did not shrink, so the contents card's share of the line went from 36% to 40% and the promo card's from 40% to 44%. Both stay inside the forty-to-fifty band Kain named at S081 for a floated card, so nothing is broken, and both are annotated in `knowledge-hub.css` with that arithmetic.

## 4. The two gate checks he asked for are in and already working

`css_gate.py` gains **E, size is a role** and **F, width is a token**.

- **E** fails any `font-size` in px that is not a `--text-*` token, including one that is on the scale. The S110 measurement found nineteen styles existing twice on this site, once as a token and once hand-typed, so a hand-typed 16 is the copy that does not move when Kain rules the body to 18.
- **F** fails any `width` or `max-width` of 320px or more inside a rule that is not a `--container-*` token. Below 320 a width is a drawing rather than a container. Media-query widths stay with check A so nothing is reported twice.
- Both take the gate's existing annotation escape, so a real one-off is made to say so rather than refused.

**They are not a paper rule.** They fired on the first stylesheet edited after they were added and refused the file until it was clean, and they are what turned up the 17px on the trial panel while Kain was looking at that panel. **The remaining count, measured this session: 87 off-scale sizes and 77 hand-typed on-scale sizes across the families not yet swept.** The gate is therefore the sweep's finish line, and it is red until the sweep is done, which is the correct state for it to be in.

## 5. The acceptance test, and one honest gap

**The instrument Kain named is built:** `previews/sweep_diff.py` renders the three real pages twice, once against the theme at a git revision and once against the theme on disk, and reports every element whose computed type, spacing or width moved. It reads computed values rather than pixels in a picture, because a screenshot says something moved and never says what.

**`previews/sweep_sitting.py` builds the two-column before and after page Kain rules from**, per the S270 brief section 5, with the three screen sizes on buttons. Both refuse the network, so nothing in either can be a stale cached copy from the server.

**The gap, stated rather than glossed:** the full computed-style diff for this family was killed twice by session restarts and has not completed a clean run end to end. **What is verified is the live page itself, in WebKit and then in Safari: text 18 on 1.75, gap 16, column 800, on all three page types, at theme 0.328.0 on the server.** The full element-by-element diff is owed and runs before the next family is called closed.

## 6. What is next, and what is still waiting

**Next:** the cards family, then components, then About and the people pages, then reviews and testimonials, then header and footer last, which is the order the S270 brief section 5 sets. Each one gets the two-column comparison in Safari before the next begins, and copy changes are taken as they come up.

**Still waiting on Chat or Kain, carried from S111 and not yet answered:** does 880 retire the way 620 did, or survive somewhere? Nothing reads it except through `--container-article`, so retirement still looks right, but it is a ruling rather than a measurement and section 4.1 cannot be rewritten without it.

OWED BACK: the two lines in section 1 written into whatever record holds the trial panel's approved copy, superseding the S341 body; and the 880 question answered so DSRD 7 section 4.1 can be rewritten.

*No em or en dashes in this file; checked before writing.*
