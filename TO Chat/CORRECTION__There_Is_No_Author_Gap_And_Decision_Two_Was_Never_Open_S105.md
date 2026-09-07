# CORRECTION: there is no author gap, decision 2 was never open, and I put a settled standard to Kain as a question

**From:** Claude Code, Session 105. **Date:** Monday 7 September 2026. **Session type:** factory.
**Board card:** the Knowledge Hub article set.
**Replaces:** a RULING file written earlier this session and deleted within the hour, before Chat read it. It said Kain had ruled the WordPress author should be filled in. **It was wrong at its root and nothing in it should be acted on.** It is named here rather than quietly removed.

---

## 1. What happened

Decision 2 of the standing five reads: "192 of 196 published articles have no WordPress author at all (author zero). Every importer creates that way. Bylines are unaffected, since they come from the record's pen name, but schema will notice. Whose name is on an article is a decision, so nothing was changed."

**I put that to Kain as an open decision this session and recommended filling the author in.** He said yes, on the strength of my description. On measuring what that would take, I found it needed five new WordPress accounts, went back to him, and he answered:

**Kain, in this sitting: "no, leave the pen names without accounts - we actually agreed this a few months ago"**

**He was right, and it is stronger than an agreement.** DSRD 10 section 5.4, quoted word for word from the canonical file, read this turn:

> "Authorship on Knowledge Hub content ... is an **ACF author slug resolved against the theme's people registry** (roles, biographies, photos, and the author signature card, held in the theme's setup code). There are **no WordPress author accounts** ... Author profile pages render from the registry via a page template."

And, in the same sentence, the reason author zero appears at all: "the Hub CPTs deliberately carry no `author` support."

---

## 2. So decision 2 is not a decision, and both halves of its premise were wrong

**"Author zero" is not a defect. It is the design working.** The Hub post types are registered without author support, so WordPress has nowhere to put an author and writes zero. Every importer "creates that way" because that is the only way it can create.

**"Schema will notice" was unfounded, and I had already disproved it this session without noticing.** Checked on the rendered live page just now, the Article schema on `/learn/helping-people/articles/empathy-in-counselling/` carries:

```
"author": { "@type": "Person",
            "name": "Prof. Gerard Egan",
            "url": "https://achologytest.com/about/instructors/gerard-egan/" }
```

A full Person with a name and a resolvable URL, built from the registry exactly as section 5.4 says. **Search engines and AI systems are already getting the author.** I had read the same registry-built Person schema off the six elder pages earlier in this very session and did not connect it.

**Nothing was changed on the install at any point.** The wall refused the write, which turned out to be the right outcome for the wrong reason.

---

## 3. What I did wrong, so the fix lands in the right place

**The standard was findable and I did not look.** The Shared Rules, section 3: "Look first: the DSRDs, the project files, the vault, the theme, the unread files in your inbox. A question that a file could have answered is a break." One grep of DSRD 10 would have closed it. I took a line from a memory note as the state of the world and put it to Kain instead, which is section 2's rule broken as well: memory is never a source.

**The cost was his time on a question that had been settled, and he had to be the one to remember it.** That is the failure this instruction system exists to prevent, and it happened in the middle of a session that had already quoted DSRD 6 correctly three times.

**Where the fix belongs.** Not in a new rule: the rules that would have caught this both already exist and were simply not kept. The fix is in the standing decisions list itself, which is the artefact that carried a settled standard as an open question and would have gone on doing so every session. **Decision 2 comes off it, replaced by one line pointing at DSRD 10 section 5.4**, so the next reader meets the answer rather than the question. I have struck it from the memory note this session.

**One thing for you to consider, and it is yours rather than mine.** If that list carried one settled thing as open, it is worth asking what else on it is settled. I have not audited the other four; I have measured three of them this session and they are all genuinely open.

---

## 4. Withdrawn with it

The deleted file also asked you to rule on narrowing `H9` so that a `wp post update` setting no status stops counting as a publishing verb. **That request is withdrawn too.** It existed only to unblock work that should never have been done, and a harness change with no live need behind it is exactly what the growth governor forbids. The observation stands if a genuine case ever arrives; it is not one today.

---

OWED BACK: nothing. This file corrects the record and closes decision 2. Kain's ruling needs no writing into a document, because the document already said it.

*No em or en dashes in this file; checked before writing.*
