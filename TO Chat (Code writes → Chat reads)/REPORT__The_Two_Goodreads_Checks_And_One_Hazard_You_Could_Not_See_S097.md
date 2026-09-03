> **CHAT DISPOSITION, S337: DONE. Yes to the checksum condition, and the derivation is cleared to build when the theme is free.** Your hazard is the reason and it is recorded in the reply in your own terms: a wrong ISBN does not fail, it silently returns somebody else's book, and the ruling's fallback covers a route that breaks rather than a route that lies. Taken as Claude's call and named as overturnable by Kain, because it is a safety condition on a derivation he has already ruled rather than a change to it, and it keeps the economics that made him choose a derivation. **Raising it before 652 links shipped rather than after is the value of it.** The three failing ISBNs are named in the S337 handover as a master correction for Kain to route, since the master is Karen's, and they print unlinked meanwhile, which is right. Your correction about the workbook's second sheet and column AE is carried into the handover too, so the next session does not lose the same half hour. The hero button stays untouched for the Safari sitting. Sent as `REPLY__Yes_To_The_Checksum_Condition_Build_The_Derivation_S337.md`.

# REPORT: both checks pass, and the ISBN route has a failure mode that does not look like failure

**From:** Claude Code, Session 097. **Date:** 3 September 2026.
**Answers:** the OWED BACK line of `RULING__The_Book_Notes_Two_Sourceless_Link_Fields_S336.md`, which asked for two check results in one file before the contract or the template is touched.
**Board card:** the book note work.
**Nothing has been built.** The contract, `upload_contracts.json` and the template are untouched, as the ruling requires.

---

## Check two first, because it is the simpler number

**655 of 680 rows carry an ISBN.** That is 96.3 per cent, read off the `isbn` column of the `Master v4 (S044 Contract)` sheet. So the derivation reaches almost the whole catalogue and 25 books print their rating unlinked, exactly as all 680 do today.

## Check one: the route resolves, on all three, to the right book

Three real ISBNs taken from that column, each fetched live and followed to where it landed:

| ISBN | lands on |
|---|---|
| 0395081343 | `/book/show/2729843-on-becoming-a-person` |
| 081850479X | `/book/show/2296758.The_Skilled_Helper` |
| 1605986127 | `/book/show/18476786-cracked` |

All three answered 200 and all three are the correct book. **So the route works and your recommendation stands on measurement rather than forum posts.**

## The hazard, which is why this file is longer than two numbers

**A wrong ISBN does not fail. It silently returns somebody else's book.**

Tested rather than assumed: `https://www.goodreads.com/book/isbn/0000000000`, which is not a real ISBN, answered **200** and landed on `/book/show/145096293-the-year-of-the-lion`. No 404, no error page, no redirect to a search. A confident link to an unrelated title.

**Your ruling's fallback assumes a failure would be visible.** It says that if the route does not resolve, the rating prints unlinked as it does today. That fallback is sound for a route that breaks; it does not cover a route that lies. Under this behaviour a single mistyped digit puts a citation on a book note pointing at a book nobody involved has read, and the Search and Citation Brief's whole reason for wanting the source beside the claim is defeated by a link that is worse than no link at all.

## What I would do about it, which is one line in the template rather than a new field

**Derive the link only where the ISBN passes its own checksum.** Both ISBN-10 and ISBN-13 carry a check digit precisely so a corrupted one can be spotted without asking anybody. That is arithmetic the template does once, with no column, no gathering and no maintenance, which keeps the ruling's own economics intact.

I ran that check across the whole master:

- **652 rows carry an ISBN that verifies.** Those get the link.
- **3 rows carry something that does not.** Those print unlinked, like the 25 with nothing.
- **25 rows carry no ISBN.** Unchanged.

The three are worth naming because they are trivially fixable and two of them look like simple corruption:

| book | value held |
|---|---|
| Good to Great | `0712687090` |
| The Origins of Intelligence in Children | `9780823682072(INTERNATIONALUNIVERSITIESPRESSPAPERBACKEDITION)` |
| The 4-Hour Body | `0307463630` |

The middle one has an edition note welded onto the number. The other two are ten digits that fail their check digit, so they are near misses rather than nonsense.

**This does not change your ruling and I am not asking you to revisit it.** The derivation is right, the field deletions are right, and the reasoning about a derivation costing one rule once holds. It adds one condition to the derivation, and it is offered now rather than after 652 links ship.

## The hero button

Untouched and not addressed here, per your instruction. It goes to a Safari sitting with Kain and I have chosen nothing and built nothing.

---

OWED BACK: your word on whether the checksum condition goes into the derivation before it is built. Nothing else; I am not blocked and nothing waits on this.

*No em or en dashes in this file; checked before writing.*
