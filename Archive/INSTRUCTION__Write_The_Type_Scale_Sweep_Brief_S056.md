> **DISPOSITION, S270 (Chat), 12 Aug 2026.** The signed brief this asked for, BRIEF__Type_Scale_Sweep_S270.md, is written and signed in FROM Chat. Every decision this note left to Chat is settled inside it: representative page route, token names --text-12 through --text-42, the colour fold-in, the dead class deletion sequenced first, the gate check commissioned after. Archived.

# INSTRUCTION: please write the signed sweep brief for the type scale rollout

**From:** Claude Code, session S056. **Date:** 2026-08-12.
**Asked for by Kain, in session:** "write the brief for claude so we can get the sweep started please."
**Reads with:** `RULING__The_Nine_Step_Type_Scale_Approved_S056.md`, `PROPOSAL__The_Type_Scale_S056.md`, `REPORT__The_Typography_Census_S056.md`.

**One thing to read first, because it overtakes your S269 reply.** That reply says Kain rules from the specimen page in a session not yet scheduled. **He has already ruled, this session.** He was shown a before-and-after of the privacy policy page and approved the scale in his own words. The ruling file above carries them. So the design session that was pending is closed, and what is needed now is the brief.

**Why this is an instruction note and not the brief itself.** Harness Rule 3 gives exactly one route to a sweep: a signed brief from Kain arriving through FROM Chat. A brief I wrote and then acted on would be me signing my own permission, which is the failure that rule exists to prevent and would be worth nothing as a control. So everything the brief needs is below, in the order it needs saying, for Chat to write and Kain to sign.

---

## 1. What the sweep is

Move every font size declared in the theme onto the nine step scale Kain approved: **12, 14, 16, 18, 21, 24, 28, 33, 42**.

Measured, not estimated: **167 declarations move, 140 are already on the scale, 13 are exempt.** Fourteen stylesheets are touched.

| Stylesheet | font-size declarations |
|---|---|
| cards.css | 134 |
| help.css | 128 |
| knowledge-hub.css | 120 |
| policies.css | 103 |
| about.css | 95 |
| components.css | 90 |
| base.css | 89 |
| book-note.css | 80 |
| reviews.css | 80 |
| header.css | 66 |
| people.css | 55 |
| global-impact.css | 43 |
| testimonials.css | 43 |
| footer.css | 34 |

## 2. The boundary that matters most: size only

**The sweep moves `font-size` and nothing else.**

`font-weight` and `line-height` are **not** ruled and must not be touched. The census found five weights in use, **108 declarations that set no weight at all**, and 18 distinct line heights, and Kain has ruled on none of it. A sweep that tidied those in passing would be changing things nobody approved, on the back of an approval for something else.

Please make that a sentence in the brief rather than an assumption, because it is the most likely thing to drift.

## 3. The two exception sets, already approved on the render

Everything **above 48px** stays off the scale, by name:

- The **odometer digits**, 104px desktop and 56px phone. A moving graphic, not a heading.
- The **eight policy index watermark sizes**, from 83.79px to 115.85px, hand tuned per word so each policy name fills the same space. Snapping them would break the thing they exist to do.

## 4. How it should run, and this is the part Kain cares about

**One page at a time, never a single pass over the theme.** Each page returns the same two column before-and-after comparison he ruled from, and ships only after he has looked. He has now seen that format and approved from it, so it is a known instrument rather than a new one.

Each comparison is generated the same way: the live page, and the live page with a generated override appended, with **nothing but type size differing between them**.

**A sensible order, heaviest first**, so the risky pages are seen while attention is freshest. A suggestion, not a requirement: the policy family (already rendered and approved), the Knowledge Hub article and book note pages, the help pages, About, reviews and testimonials, then the header and footer last, because they appear on every page and a fault there is visible everywhere.

**Please have the brief settle whether Kain wants to see every page or one representative page per page design.** Twelve or thirteen sittings against four or five. I would recommend the representative route, because 96 percent of declarations move by a pixel or less and he has already seen what that looks like, but it is his time and his call.

## 5. The token work, which is what stops it coming back

**Only three type values in the whole theme go through a named token**, all three on the said block. Every other size is a loose number typed into a rule. That is the actual root cause of the sprawl: there was nothing to reuse, so each new card invented its own.

So the sweep should not write nine literal numbers 307 times. It should **name the nine steps as custom properties and reference them**, which is what makes the scale enforceable afterwards rather than merely true on the day it lands.

The token names are Chat's to choose, since they become part of the design vocabulary and will be read by everyone who works on the theme afterwards.

## 6. The gate, and its timing

Once the sweep is complete, the stylesheet gate gains a check: **every font size declared in the theme must be one of the nine steps or a named exception, and anything else fails.**

**It must be commissioned after the sweep, not with it.** A gate against the current state fails on 167 declarations, which is the mistake the typography gate was deliberately held back from in the first place.

## 7. What is explicitly not in this sweep

- **The weight rule.** It does not exist, Kain asked for it by name, and it needs its own render and its own ruling.
- **The responsive rule.** 28 of the 32 real sizes are identical on a phone and a desktop. Your S269 reply already frames this correctly as a design decision rather than a drift.
- **DSRD 7 section 3 itself.** Rebuilding it around the scale is Chat's, and Code never edits a DSRD.
- **The 67 unregistered styles.** The sweep makes their sizes legal; it does not decide whether they should exist.
- **The four registered styles with no matching declaration**, which your S269 reply takes as Chat's.

**One sequencing note.** Eight styles are carried only by classes Kain ruled dead at S266. If `COMMISSION__Delete_All_35_About_CSS_Dead_Classes_S266` runs before the sweep, the sweep has eight fewer things in it and nothing is swept that is about to be deleted. Worth putting that commission first if it is otherwise ready.

## 8. Definition of done, suggested

1. Every font size in the theme is one of the nine steps or a recorded exception.
2. The nine steps exist as named tokens and are referenced rather than repeated.
3. Every page design has had its before-and-after seen and approved by Kain.
4. `css_gate.py` passes on all stylesheets, printout in the ship brief.
5. A rendered check that nothing broke: the same instrument used for the consent sweep this session, all 303 public URLs compared before and after.
6. The report names the count moved per stylesheet, so the numbers in section 1 can be checked against what actually happened.

## 9. One line to write into the brief for Kain rather than for me

He said this session, plainly, that he has no experience of this and is relying on being steered. So the brief should say in one line **what he will actually be asked to do**: look at pairs of pages and say better, worse or the same. Nothing else. He does not need to read a stylesheet or approve a number, and a brief that reads as though he might is a brief that will sit unread.

*No em or en dashes in this file; checked before writing.*
