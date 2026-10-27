**For Code (factory session). What this needs from you:** a factory import of the eight quote pages Kain signed today, updating the eight existing quote posts in place, then one DONE with the counts and the Rank Math score table.

# BRIEF: import the eight signed resisting change quote pages (Chat, Session 448, 27 October 2026)

Read from the vault first: The Shared Road Every Kind of Page Travels, From Kain's First Words to a Page on the Build Site, and The Quote Article Pack (17 Packs); Every Page Is Written in Truth, on One Principle, With No Empty Line (03 Voice).

Model line: no writing or checking model is needed for this job; it is an import.

**Why.** These eight pages are the first batch run end to end on the new shared road, from question titles found by live search to Kain's signature. Each was written whole by hand to the new writing standard, checked by a second model with every finding settled, and read by Kain on one page. They are the proof that the road reaches the build site, so this import is the road's last two steps.

**Kain's signature, word for word:** "Kain Ramsay; 2026-10-27; quote pages, resisting change: eight question titles from live search approved first, each written whole by hand in truth on one principle, a notch towards soft, checked by a second model with every finding settled, read on one page; Kain said: I've read them. Yes, sign the eight resisting change pages. Session 448".

**What changed.** Every page has a new title (post_title, the headline and rm_seo_title set together), a new focus phrase claimed in KEYWORD_REGISTER.csv, a new description and excerpt, and a new body. Seven pages also have a new address (post_name), chosen by Chat because nothing is launched and the address now carries the search phrase. Match each post by its quote_id, never by its old address.

| quote_id | Record | New title | New post_name (old in brackets) | Focus phrase |
|---|---|---|---|---|
| Q07056 | Q07056__why-people-resist-change-until-they-have-to | Why Do So Many People Resist Change? | unchanged | people resist change |
| CQ018-041-1 | CQ018-041-1__the-desire-to-change-becomes-greater | Do People Really Only Change When It's Too Late? | do-people-only-change-when-its-too-late (the-desire-to-change-becomes-greater) | only change when it's too late |
| CQ001-043-1 | CQ001-043-1__why-people-only-change-when-they-want-to | Is It True That People Only Change When They Want To? | do-people-only-change-when-they-want-to (why-people-only-change-when-they-want-to) | people only change when they want to |
| CQ018-018-1 | CQ018-018-1__why-change-becomes-greater-than-the-desire-to-remain-the-same | Is It Simply Human Nature to Resist Change? | is-it-human-nature-to-resist-change (why-change-becomes-greater-than-the-desire-to-remain-the-same) | human nature to resist change |
| CQ018-027-1 | CQ018-027-1__why-the-desire-to-change-must-outweigh-staying | Why Can It Feel So Hard to Change Your Mindset? | why-is-it-so-hard-to-change-your-mindset (why-the-desire-to-change-must-outweigh-staying) | hard to change your mindset |
| CQ018-009-1 | CQ018-009-1__why-theres-a-limit-to-how-much-change-people-can-handle | Why Do I Seem to Resist Change So Much? | why-do-i-resist-change-so-much (why-theres-a-limit-to-how-much-change-people-can-handle) | resist change so much |
| Q07016 | Q07016__ready-to-change | Why Might We Resist Change Even When It's Positive? | why-we-resist-change-even-when-its-positive (ready-to-change) | resist change even when it's positive |
| Q07042 | Q07042__why-change-never-happens-overnight | Why Is Change So Hard for So Many of Us? | why-is-change-so-hard (why-change-never-happens-overnight) | why is change so hard |

CQ001-043-1's rm_seo_title is "Is It True People Only Change When They Want To?" so the phrase sits inside the first 50 characters; every other rm_seo_title is the title.

**Before you import.** `python3 body_guard.py --signed` exits 0 (it does tonight, with the S448 fix to its signed check named in NOTE__Gate_Faults_Found_On_The_Resisting_Change_Batch_S448). The three import checks on each record: fields complete, body shape (the body ends at its `## End of body` line), named files exist (the course quote covers 001 and 018 are in the theme; Kain Ramsay's author picture is the one your importer already checks).

**On the build site.**
1. Update the eight posts in place, matched by quote_id, from the records as they stand now.
2. For the seven new addresses, add a redirect from each old address to its new one, so no link already on the build site breaks.
3. Add the three inbound links each record names in `inbound_from`, with the record's own title as the link text.
4. Read each page back off the build site and its Rank Math score; write the score table into your DONE. A page under 90 is listed with its failing tests and stays as it is until Chat mends the record.

**What Chat checks afterwards (road step 18).** Each page opens at its new address on the build site, its title, headline, search title and description match the record, the course cover and author picture show, its links work, and its score is 90 or more. Chat then recounts the Full Editorial List and closes the batch.

**Supersedes** any earlier import instruction for these eight records.

OWED BACK: one DONE in TO Chat with the eight imported, the seven redirects added, the inbound links added, and the score table.

*No em or en dashes in this file; checked before writing.*
