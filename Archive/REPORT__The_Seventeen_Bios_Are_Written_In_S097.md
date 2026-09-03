# REPORT: all seventeen bios are written in and live. Every anchor restored, no wording touched.

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Answers:** `RULING_AND_COPY__All_Seventeen_Profile_Bios_S334.md`, its three OWED BACK items.
**Shipped as:** theme v0.148.0, deployed, all three deploy proofs green.
**Board card:** the Our People page card.

---

## What went in

**51 fields across 17 people, verbatim.** Not a word was changed, reflowed or tidied. A script placed them rather than a person retyping them, precisely so that could be true.

**17 of those fields did not exist before.** Eight people had no opening paragraph and nine had no close: Kain's intro, and both the intro and the close for Karen, Gerard and all six elders. That absence is what made every profile a different shape, and it is why a replace-only pass would have written nothing at all.

## Item one: the character counts

Against Kain's shape of about 300 in the intro, 500 in the bio, 215 in the close, and about 1,050 in total.

| | intro | bio | close | total |
|---|---|---|---|---|
| kain-ramsay | 304 | 502 | 221 | 1027 |
| karen-ramsay | 310 | 534 | 210 | 1054 |
| gerard-egan | 311 | 530 | 227 | 1068 |
| amelia-a-sinclair | 295 | 518 | 207 | 1020 |
| benjamin-lockwood | 302 | 505 | 215 | 1022 |
| charlotte-j-avery | 299 | 516 | 215 | 1030 |
| declan-fitzpatrick | 297 | 513 | 221 | 1031 |
| evelyn-montgomery | 287 | 542 | 218 | 1047 |
| frederick-s-martin | 292 | 530 | 227 | 1049 |
| isabella-s-whitmore | 284 | 550 | 213 | 1047 |
| jackson-p-hartley | 305 | 501 | 213 | 1019 |
| alec-wells | 284 | 522 | 212 | 1018 |
| andrew-nelson | 284 | 491 | 202 | 977 |
| erika-nadeau | 274 | 511 | 202 | 987 |
| gaby-tzeschlock | 287 | 536 | 206 | 1029 |
| gary-kennedy | 280 | 532 | 218 | 1030 |
| jonathon-frost | 254 | 544 | 206 | 1004 |

**The whole set spans 977 to 1068, a range of 91 characters across seventeen people.** The four shortest are elders, as your file predicted, and `jonathon-frost` has the shortest intro at 254. Counts exclude anchor markup.

## Item two: every anchor restored, none failed

**Eleven, all wrapped, none reported as missing.** The URLs were read out of the registry beforehand rather than typed, and the script verifies each title appears exactly once before wrapping it, so a title that had moved or changed would have been named instead of silently skipped.

**Kain's two Genius Links were followed before use, as your file asked.** `geni.us/eKtpPW` resolves to The Ultimate Life Coaching Handbook and `geni.us/eHBO` to Responsibility Rebellion, both on amazon.co.uk, both carrying `kainramsay01-21`. The old plain amazon.com address is gone.

## Item three: one thing for Kain, not a fault

His close describes Responsibility Rebellion as "a Practical Guide to Personal Empowerment". Amazon lists the book as "An Unconventional Approach to Personal Empowerment". **His words are in as written**, because they read as a description rather than a quoted subtitle and the copy is his. Named so he can change it if he meant the subtitle.

## Three faults caught before anything shipped

**Your headings use short slugs where the registry uses middle initials** (`amelia-sinclair` against `amelia-a-sinclair`, and the same for Charlotte, Frederick, Isabella and Jackson). Matching on them would have written five people's words nowhere and reported success. Every entry is keyed on the registry's own slug and the script refuses to start if one is missing.

**The first pass found fields with a PHP-string regex**, whose single-quoted alternative ran across the apostrophes inside the registry's own comments and pointed at the wrong text. It is line based now: every field here is one line, and a line cannot see into a comment.

**The second pass escaped the anchor quotes twice** and produced a file PHP would not parse. **It was linted on the server before deploying and never shipped.** A syntax error in this file is a white screen on every page of the site, so that lint is now the habit for it, and the working copy was reverted with git rather than patched over.

## What is unchanged, deliberately

The six elders still have no pages and `has_page` stays false on all six, exactly as `RULING__Every_Profile_Bio_Takes_One_Shape_S097.md` set out. Verified after deploying: `alec-wells` returns 404. Karen stays false as well. **The words existing was the thing that had to come first, and now it has**, so the remaining step is Kain creating the six pages, after which Code flips the six flags in one change set.

---

OWED BACK: nothing. Chat still owes the shape written into DSRD 2, after which the machine check is worth building.

*No em or en dashes in this file; checked before writing.*
