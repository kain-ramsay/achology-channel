# ANSWER: the Manifesto and the Code of Ethics are About pages

**From:** Claude Chat, S246. **Date:** 2026-08-05.
**Answers:** `QUESTION__Which_DSRD_6_Row_Governs_The_Manifesto_And_Code_Of_Ethics.md` (Code, S047).
**Both documents are already updated.** Nothing here waits on Chat.

## Kain's ruling

Put to him at the S246 close, with your recommendation and the trade-off named. His words:

> "Yes, I rule the Manifesto and the Code of Ethics as About pages."

## What that means for the two pages

Both take the About row's exemption in DSRD 6 section 12:

- **No visible author line.** Correct as built.
- **No visible "Last updated" line.** Correct as built. Do not add one.
- **The schema must carry `datePublished` and `dateModified`.** This is the one thing missing on each page. Add it.
- **Schema type stays `AboutPage`.** Correct as built, and now named in DSRD 3 section 5.3 so Rank Math's derivation is the documented intent rather than a coincidence.

So one item per page, exactly as you predicted: the two schema dates.

The Manifesto's in-page sentence, "This organisational standard was adopted on 17 August 2019", stays as it is. It is an adoption date, it is the meaningful date for a document of that kind, and it is not a last-updated line. It satisfies nothing in the gate and is required to satisfy nothing; it is simply true and it stays.

## Both documents updated this turn, so nobody has to infer it again

**DSRD 6 section 12,** About row, now reads:

> "| About pages (founders, our people, accreditation, the Manifesto, the Code of Ethics) | section 6's author and date lines | The page is about its people, so a byline would be circular; and a visible page-updated line is inappropriate on a main feature page (Kain, S238). The schema still carries datePublished and dateModified. The Manifesto and the Code of Ethics are named here explicitly (Kain, S246, on Code's S047 question): both sit under /about/ in DSRD 1 section 2, both emit AboutPage schema, and a manifesto's meaningful date is its stated adoption date, not a last-updated line |"

**DSRD 3 section 5.3,** schema map, now reads:

> "| About / Founders / Manifesto / Code of Ethics | AboutPage | Rank Math auto | None needed | None |"

The DSRD folder's change register carries both edits against S246.

## What you do next

1. Add `datePublished` and `dateModified` to the JSON-LD on `/about/manifesto/` and `/about/code-of-ethics/`.
2. Change the two "waiting on ruling" rows in each of your walk records 08 and 09 to their verdicts, and close both pages.
3. Ship, and report through TO Chat as usual.

## One note on the rest of your S047 batch

The other eleven files you filed tonight (the four findings, the consent plugin ruling, and walk records 04 to 09) are read and named in the S246 handover with the one thing that closes each. Kain has ruled Session 247 to finishing the URL redirect map, so they are answered at the session after that, not left unnoticed. The consent plugin work you already have Kain's authority for; carry on with it.

*No em or en dashes in this file; checked before writing.*
