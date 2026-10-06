**For Code: the quote page heading upgrade, your half. Kain's ruling, S407. A factory session is the right sitting; one theme edit inside it, on Kain's word, named below.**

# BRIEF: the quote page headings upgrade, the sweep and the gate (Kain, S407)

**From:** Claude Chat, S407, Tuesday 6 October 2026. **To:** Claude Code.

## The ruling

Kain, S407, in Chat, upgraded the quote page's headings. The page now carries four body headings and a renamed related block, in this order:

1. **An Idea That’s Worthy of Your Consideration** (new, fixed words; sits directly above the provenance paragraphs, the ones opening "This quote by [author] was taken from...")
2. **What the Quote Might Be Suggesting to Us** (fixed words; replaces "What the Quote Might Be Saying")
3. **What Can We Learn From the Idea That ‘[the quote’s idea]’?** (written for each page; replaces "What Can We Take Away From It?")
4. **A Question That Deserves an Honest Answer** (fixed words; replaces "A Question Worthy of an Honest Answer")
5. **Explore More Quote Articles** (the heading of the related reading block at the page's foot; DSRD 2 section 1.1 item 13 called it Related Further Reading)

The apostrophes and quote marks are the curly ones shown. "to" is small by the Content Standard Part 1 rule 9 (Chat's call, overturnable). Written into DSRD 2 sections 1.1 and 3.3, the Content Standard Part 17.5 (now Version 10, signed by Kain at S407) and the defect register's S407 line. Read those, not this summary, if they ever differ.

## The order of the whole job

1. **You, now (this brief):** the gate, the theme heading, and the three fixed headings swept into the records. **Do not push any quote record to the build site yet.**
2. **Cowork, next:** writes heading 3, the idea, into every quote record. She starts when your DONE file for this brief lands.
3. **You, last:** one push of every changed quote record, on a brief Chat writes when Cowork reports done.

One push, so no page on the build site ever shows the new headings with the old third one.

## What to do

1. **The gate.** Update `content_gate_standards.json` (and anything else in `content_gate.py` that holds the quote headings) to the four headings in order: 1, 2 and 4 matched word for word; 3 matched as the fixed frame "What Can We Learn From the Idea That ‘" + an idea of two to seven words + "’?". Keep the fourteen S388 exception working. Give the change the S407 date under the Standard's section 15.2 item 2, so records not yet swept are measured by the rules of their time. Add acceptance cases that go red as well as green.
2. **The records.** In every quote record in Content Records' quote-page folder (`CQ*` and `Q*` records; leave the `_stale_*.bak` files and `_to_delete` alone): insert heading 1 above the provenance paragraphs; replace the old headings 2 and 4 with the new words. **Leave the old heading 3, "What Can We Take Away From It?", exactly as it is,** so Cowork can find every place her idea goes. Change no other word. Report the count of records changed and any record whose headings did not match the expected old ones, by name, without fixing it.
3. **The fourteen S388 pages.** List each with the heading that currently carries its keyword, so Cowork keeps the keyword when she writes the idea.
4. **The theme, on Kain's word (S407), named in your commit and report per the harness:** the related reading block on the quote page reads "Explore More Quote Articles". First read what that block holds on a built quote page. If it holds anything other than quote pages (articles, book notes), do not rename it: say so in your report, because the heading would then mislead and the call goes back to Kain. Deploy only the theme change.
5. **The exemplar.** `Q07026__life-comes-with-no-rulebook.md` is swept like every other record. Name it in your report.
6. **The Standard's archive copy.** Write Version 9 from git into the factory folder's Archive as `000__THE_ACHOLOGY_CONTENT_STANDARD__Version_9_S405_signed.md`, as you did for Version 8.
7. **Anything else that names the old headings** (importer, schema, build sheets, prototypes, the quote-page skill, the theme's own strings): list each by name in your report. Change only what this brief names.

## Report back

One DONE file in TO Chat: the gate change and its acceptance printout, the record count and any misfits, the fourteen pages' keyword headings, the related block finding and the deployed version, the archive copy, the list of other places the old headings live. Open it with the line Cowork needs: "Cowork may start the idea headings."

*No em or en dashes in this file; checked before writing.*
