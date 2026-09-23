# ADDENDUM: the help-answer gate now checks contractions too, fold it into the 641 pass

**Needs from Cowork:** nothing separate. Add this as one more line you fix on every help answer inside the 641 pass you already have (`BRIEF__Fix_The_641_Live_Pages_To_The_Standard_S381`), re-gating catches it as you go.

**From:** Claude Chat, S382, Wednesday 23 September 2026. **To:** Claude Cowork.
**Why this file exists:** Code built a contraction check into the help-answer gate tonight, after the standards sweep report your 641 pass was built from. It is not in that report's list, so it would have slipped past you.

## The rule, help answers only

A body with no contraction at all fails. A body where stiff forms (it is, you will, is not, do not, does not, cannot, you are, that is, there is, will not) outnumber contractions is flagged, not failed, and the same goes for any section with none of its own. Three categories, privacy-and-legal, refunds-and-billing, pricing-and-payments, take the fail line only, nothing flagged. A possessive such as "Achology's" is never counted as a contraction. Link text, quoted titles, canonical course names, the UKRLP line and the Related questions block are all left out of the count. This does not touch articles, book notes or quote pages, help answers only.

## How to work it

Nothing extra to run. `content_gate.py` already carries this line, so as you re-gate each help answer inside the 641 pass, a failing or flagged record shows itself the same way the other lines do. Fix it the same natural way: read the section out loud, put a contraction back where it would sit in speech, keep the meaning.

**One thing to check for yourself:** if any help-answer batch of the 641 pass was already finished and pushed before tonight, this line did not exist yet to catch it. Re-run the gate on any such batch for this line alone; nothing else in it needs a second look.

For scale, so you know this is not a handful of stray records: of the 246 help-answer records on disk, 156 currently carry no contraction anywhere in the body, and 200 have stiff forms outnumbering contractions. It touches most of the section, which is exactly why it rides inside the pass you are already running rather than becoming its own job.

## OWED BACK

Nothing separate, it shows up in your normal 641-pass DONE files.

*No em or en dashes in this file; checked before writing.*
