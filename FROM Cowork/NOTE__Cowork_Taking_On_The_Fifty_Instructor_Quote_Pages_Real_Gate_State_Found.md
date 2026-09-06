# NOTE: Cowork is taking on the 50 instructor quote pages card, on Kain's direct instruction

**From:** Claude Cowork. **Date:** 6 September 2026.
**Board card:** "50 instructor book quote pages, from The Skilled Helper and The Ultimate Life Coaching
Handbook" (Website Project Board, id 3d24da19-af35-815c-affa-d88aa80fb38d).
**Trigger:** Kain asked directly whether these fifty were delivered. They were not. He then told me to
take the card on myself, since its own route had assigned the drafting to Chat.

## The real state, checked directly, not read off the card

The card's own "Definition of Done" field, last edited S342, says the 25 Handbook records fail on
demand_evidence and outcome-tag count. That description is stale. Running `content_gate.py` on all 25 today
finds every one failing, but on a different and wider set of lines than the card names, 5 to 9 each, none
passing:

- Every sampled record has em or en dashes present.
- Every sampled record's Flesch reading ease runs 74 to 78, above the 60-to-70 band: too simple, not too
  complex, which is the opposite direction from most content this session.
- Every sampled record has a focus keyword that does not actually appear in its own SEO title, description,
  address slug, or first 10% of body. Q07026's focus keyword is "no right way to live"; its slug is
  "life-has-no-rulebook". These were not close misses, the keyword and the page's own address say different
  things throughout.
- Every sampled record has zero external links.
- Every sampled record fails "keyword in a subheading."

The demand_evidence and outcome-tag fields the card names as broken are, on direct check, already fine on
every record I sampled (proper live-search evidence present, 3 to 4 tags each, within the 2-to-4 band). I
think that part of the card was fixed at S342 (there's a `Batch_Report__Quote_Metadata_Finish_S342.md` in the
quote-page folder dated after the card's last edit) and the card was never updated to reflect it. Worth
correcting the card's Definition of Done and Status/Pipeline Stage/Owner fields to Cowork, since I don't
touch the board myself.

## One real open question, not something I can just work around

"Keyword in a subheading" cannot be passed by any quote page as the type is actually built. The quote-page
skill is explicit: the H1 is the only heading the writer ever creates; Hook-Book-Look-Took is the underlying
shape and never a visible heading. I checked `content_gate_standards.json`'s shared section for an existing
page-type exemption on this check, the way the seven Rank Math tests carry declared exemptions elsewhere;
there isn't one for quote-page. Until this is ruled one way or the other, I'm treating it as a named,
accepted exception on every quote-page record rather than inventing a fake subheading to satisfy a machine
check the type was never meant to carry. Flagging for whoever owns that config file to add the exemption
properly, rather than each session re-discovering the same dead end.

## What I'm doing

Fixing the 25 existing Handbook records to gate-clean first: real fixes, not fake ones, meaning the focus
keyword, title, description, slug and opening actually get realigned to agree with each other and with what
each page is actually about, Flesch brought down into band with more considered phrasing, one genuine
external link added per page, dashes removed. Then drafting the 25 Skilled Helper records fresh, from
Q07026 as the corrected exemplar once it's fixed, gate-clean from the first draft. Both halves still wait on
the quote page template being signed before anything publishes; that doesn't block getting the content itself
ready.

OWED BACK: progress reports as the 25 existing records clear the gate, then as the 25 new ones are drafted.
