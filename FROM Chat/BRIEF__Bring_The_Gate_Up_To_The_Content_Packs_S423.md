> CODE DISPOSITION, S162: WAITS ON a factory session being open (the content gate is factory work; this theme session touches no gate file).

First line of need: Code, one factory job: seven changes to `content_gate_standards.json` and `content_gate.py` so the gate matches the signed Standard and the four new content packs. Kain's yes, Session 423. No theme work.

# BRIEF: bring the gate up to the content packs (Chat, Session 423, Tuesday 13 October 2026)

**Why.** Chat built four content type packs this session (`Content Type Packs/PACK_01` to `PACK_04`, Content Production Factory). Gathering them found the gate behind the Standard in seven places. Until it catches up, it fails good pages and passes wrong ones. Proof run: ten articles gated today; printouts in `PACK_01__Articles/PROOF__Ten_Articles_S423/gate_after`.

**The seven changes.**
1. **Quote page band.** `quote-page` reads 650 to 825 words; Standard 17.5 (Version 19, S420) reads 800 to 1,000, a guide. Also remove the fourteen-page S388 heading exception (withdrawn by Kain, S422, K9; DSRD 2 section 3.3).
2. **Book note headings.** `book-note` still locks the old five ("What this Book is Actually Saying" and four more). DSRD 9 section 32.7 holds Kain's S150 five: What This Book Is Saying; The Author's Background and Perspective; What Could This Book Mean for Society?; What You Could Learn From the Book; What Might Your Next Learning Steps Be? Lock those, keeping the old set as a dated fallback for records not yet moved, as the theme does.
3. **Exception (q), course nicknames.** The link-text check (2 to 5 words) fails an approved DSRD 5 section 9 nickname longer than five words, for example "Mental Health and Wellbeing Practitioner Diploma" on `is-mental-health-genetic`. A link whose text is an approved nickname passes.
4. **Exception (o), series links.** The link-text check fails the Seven Beliefs back and next links, which sit on the part's full title by ruling (`PART_03__know-thyself`). On `seven-beliefs-series`, the series link block is excused.
5. **Reading ease counts the foot.** The Flesch score includes the Sources list, whose web addresses drag it down (`what-is-counselling`: 57.2 with the list, about 62 without). Score the teaching only, as the section count already does with `foot_headings`.
6. **Rebuilt old pages have no live type.** `field-authority-article` is retired (S351) and refuses records dated after 5 October; `book-derived-article` requires `source_reference`, which a rebuilt non-book page cannot fill. Standard 15.1 item 21 says a rebuilt page takes the type it is rebuilt as. Please propose the smallest fix (for example: `book-derived-article` with `source_reference` optional when `old_address` is set) and tell Chat; Chat rules it.
7. **The S161 hero lengths.** Your S161 ruling owes the gate two checks on every Knowledge Hub type: title 50 to 60 characters and subtitle 150 to 170, counting spaces. Add them as NOTE lines first (warnings, not fails), because Kain has one open decision on book note titles and existing titles are reported, never forced.

**Done when.** The seven are in, `content_gate_fixtures.py` and `content_gate_acceptance.py` pass, and the ten proof records re-gate with no FAIL except "signed by Kain". Report in TO Chat as `DONE__Gate_Up_To_The_Content_Packs_S423.md`, one line per change.

**Also waiting on you (separate file, facts only):** `ASK__Three_Facts_For_The_Articles_Pack_S423` (the subtitle field, the practice block field, the hub question type).

*No em or en dashes in this file; checked before writing.*
