# BRIEF: eight profile metadata sets are needed, and two keywords are already claimed twice

**From:** Claude Code, Session 097. **Date:** 3 September 2026.
**Signed by:** Kain, in the S097 sitting: *"Yes, hold the six unpublished until their full meta data sets exist, and ask Chat now for those six sets plus the two that have gone stale."*
**Reads with:** the `rank-math-90` skill, Part A steps 2 and 3, and DSRD 6 section 5 item 11.
**Board card:** the Our People page card.

---

## The ruling, and why it was needed

The six eldership pages were created as drafts earlier in this sitting. **Kain asked whether they had been optimised to the skill. They had not: no focus keyword, no SEO title, no description, nothing at all.** He then ruled that they stay unpublished until their full metadata exists.

Good catch on his part. Six pages would have gone live with nothing for a search engine to read, on pages whose entire job is to be found by someone searching a person's name.

## What is asked for: eight sets, each of three fields

**The six with nothing:** Alec Wells, Andrew Nelson, Erika Nadeau, Gabriele Tzeschlock, Gary Kennedy, Jonathon Frost.

**The two that have gone stale against the bios Kain rewrote tonight**, and both were read off the install this session rather than assumed:

- **Evelyn Montgomery.** Her description says she "writes book-derived articles for Achology's Knowledge Hub, translating classic psychology texts into clear everyday guidance." Her new bio says she writes the most approachable articles for readers meeting psychology for the first time. Those are close to opposite.
- **Charlotte J. Avery.** Hers says she is "turning the ideas inside catalogued psychology books into practical long-form reading." Her new bio has her working from studies, frameworks and evidence, tracing ideas back to their origins. Drifting the same way, less severely.

**The other eight descriptions still read true against the new bios**, checked one by one, so they are left alone.

## The shape each set takes

From the skill's step 3, and these are hard limits rather than guidance:

- **Focus keyword:** the exact phrase. On these pages the ten existing ones use the person's name.
- **SEO title:** carries the keyword inside the first 50 characters, under 60 in total.
- **Description:** carries the keyword inside the first 120 characters, under 155 in total, and reads as a plain statement rather than a tease.

**The pattern the existing ten already use**, so the eight match rather than diverge:

> `Benjamin Lockwood | Lead for Book Research Content`
> "Benjamin Lockwood leads Achology's book research, distilling each catalogued book into a clear and honest overview of what it offers readers."

Name, then role, in the title. In the description: name first, what they do, and what a reader gets from them. The six elders share one role line, "Community Elder, Mentor and Events host", which is Kain's own wording and is not a field to vary.

**Their words are already written.** All six bios went into `people-setup.php` tonight at v0.148.0 and can be read there; nothing needs inventing about who these people are.

## The fault: two keywords are claimed twice, and this is not new

`KEYWORD_REGISTER.csv` holds **zero rows for any `/about/instructors/` address**. But it holds these two:

```
gerard egan,author-biography,gerard-egan,/learn/helping-people/articles/gerard-egan/
kain ramsay,author-biography,kain-ramsay,/learn/helping-people/articles/kain-ramsay/
```

**And the profile pages carry the same keywords on the install:** page 187 has `Kain Ramsay`, page 189 has `gerard egan,Prof. Gerard Egan,Egan`.

So for both men, two live pages compete for one keyword. **That is precisely what the register exists to prevent and what Rank Math penalises**, and it is invisible today because the profile pages were never entered in the register at all.

**This is a decision rather than a fix, so it is not taken here.** Either the biography article owns the person's bare name and the profile takes something else, or the reverse. Whichever way it goes, the profile pages then need register rows so it cannot happen again silently.

**The mechanism for those rows already exists** and needs no new machinery: `build_keyword_register.py` reads any `*__CLAIMS.csv` beside it, and `SITE_PAGES__CLAIMS.csv` was created in this same session for the homepage's `achology` row. A profile page has no content record, exactly like the help answers, so the claims file is its route.

## One thing nobody should read as a number yet

The ten existing profile pages carry stored Rank Math scores of 81 to 85. **Those were written before the theme's filter declined seven of Rank Math's tests**, which `rank-math-feed.php` now does. Every refusal makes the score easier, so the stored numbers are almost certainly understated and nothing has re-read them since. **Treat them as unknown rather than as failing the 90 bar.** Code re-reads them when the eight sets land and the pages are scored properly.

## What happens with the answer

Code writes the eight sets onto the pages, adds the six register rows through the claims file, rebuilds the register, reads every profile page's score back off the install, and files the table. The six stay drafts throughout. **Kain publishes them, and only then does Code flip the six `has_page` flags** so the hub cards start linking on the same day the pages appear.

---

OWED BACK: the eight metadata sets, and the ruling on which page owns the bare name for Kain and for Gerard.

*No em or en dashes in this file; checked before writing.*
