> CHAT DISPOSITION, S357: read. Recorded in DSRD 7 section 15.2 and DSRD 8 section 30. Nothing owed. Archived.

# RULING AND SHIP: the quote card's share picture is stamped with the design it was baked against, and a stale one cannot publish

**From Code, S110. Date: Thursday 10 September 2026. Theme 0.259.0.**
**Found by Kain**, live, by pressing Download on a quote page. His words:

> "the upgraded quote card image still isnt downloading - an older version is
> still locked in"

**He was right, and it was three faults stacked, not one.**
**Answers:** the proposal in `RULING__The_Quote_Card_Is_Settled_S109.md`, the
stale share picture section.
**Board cards:** Quote page template; Quote verification.

---

## The three faults, because only the first was known

**One, the baker could not reach the site at all.** SiteGround's Antibot answers
an automated browser with a challenge screen, so every run of the card baker
refused with "no card on the page". That reads as a template fault rather than a
network one, which is why it sat. It now loads through the mirror `page_gate.py`
already built, which fetches from inside the host over the SSH line where the
challenge does not apply.

**Two, the address never changed, so his browser served him his own copy.** Even
a successful re-bake wrote to the same filename, and a file replaced at an
unchanged address is uploaded, not shipped. This project already holds that rule
and it was written for stylesheets; it is just as true of a picture. Every card
is now named for the design it was baked against, so a card baked against a
different design is a different address and cannot come out of anybody's cache.

**Three, the page itself was cached.** Measured immediately after a successful
attach: the install carried the new attachment and the new stamp, and the live
page still handed out the old picture's address. The baker now purges after it
attaches, and where the purge fails it says so and says what the consequence is.

## What is stamped, and what the check actually compares

Three values land on each quote when its card is attached: the design id, the
theme version, and the moment.

**Kain asked for the theme version and the check does not use it. That is a
substitution, so it is named rather than slipped in.** The theme takes a new
version several times in a working day for work that never touches this card. A
check that refuses every quote after every unrelated release is a check that gets
switched off inside a week, and this project's own lesson is that a check nobody
trusts is worse than none. So the version is stamped, because it is what a human
reads and dates; the CHECK compares the card's own design id.

**The design id is a fingerprint of the three things the picture is made of:**
the drawing, every stylesheet rule that names the card, and the lockup file
printed into it. Move any of those and every baked card is stale and says so.
Move anything else in the theme and it stays quiet. `quote_card_design.py` holds
the reasoning in full.

## The refusal

`publish_gate.py` now refuses to clear a quote page whose share picture is
missing, unstamped, or stamped against an older design. It is never a quality row
and is never waived by `--update`, and the reason is the one thing that makes
this artefact different from everything else on the site: **a picture that has
already left the site cannot be corrected by a later edit.** A stale stylesheet
is fixed by a reload. A stale card is on somebody's Instagram.

**It is proved able to refuse**, which is this project's standing rule about
green tests. `publish_gate_card_acceptance.py` runs eleven cases: four refusals,
two passes, and five on the id itself, including that it moves when the drawing,
the styles or the lockup move and does not move when only spacing does. **One of
them failed on its first run and found a real weakness:** the whitespace
guarantee lived in the readers rather than at the point the hash is taken, so any
future caller could have lost it. Fixed at the hashing boundary, and the id moved
once as a result, which re-baked the one card that existed.

## What is yours

Nothing, except one thing for the record. **The production filename in DSRD 7
section 15.2** wants the quote's number within its book, which lives in the
master spreadsheet and is still owed. The design id in the filename is additive
and is Code's, taken because it is what makes the address change. It does not
settle the naming question and does not conflict with it.

---

OWED BACK: nothing. It is a record.

*No em or en dashes in this file; checked before writing.*
