**For Code. What this needs from you:** two locks on your side, the import refusal and a scan of the build site, then a DONE with the scan's count. It replaces the ask in NOTE__Working_Notes_Found_In_Twelve_Signed_Bodies_S447: the two patterns are already in, so no gate file edit is owed for them.

# BRIEF: no working note may ever reach an article body (Chat, Session 447, 26 October 2026)

**Why.** Kain asked for a guarantee that no working note ever reaches an article again. Notes have reached build site pages before (the S104 footer on 67 posts, the S346 process text on 117), and on 26 October 2026 a signing line written in full ("Signed by Kain Ramsay ... Session 425") sat in ten signed bodies where the phrase list could not see it. A careful writer is not a guarantee, so the answer is five locks, each stopping a note alone.

**Done on Chat's side today, each tested by trying to break it:**
1. **End of body.** All 1,084 signed records now carry `## End of body` where the article stops, placed by `vault_gate.py mark-end`, which writes a record only when `extract_body()` reads the same words afterwards. Signing adds it from now on.
2. **The writing guard.** The project's PreToolUse hook now refuses any Write or Edit to a record that would leave a working note in its body, or that removes the End of body line. It fails closed if the check cannot load.
3. **Signing.** `vault_gate.py sign` refuses any page whose body carries a note.
The shared list: ten patterns added to `shared.process_text_registry` in `content_gate_standards.json` (a session in full, a signature, a desk note, a ruling stamp, a pack or lane name, one of us named, a working-notes heading, a vault link, a placeholder, the footer inside a body). `process_phrases()` already adds the registry to the built-in floor, so `machinery_in_body()` refuses them in both gates with no code change. Run against all 1,084 signed bodies: no false finding, and it caught two real notes the old list missed ("## Lane B rewrite note (process text, never imported)" inside two book notes), now moved below the body. `body_guard.py` in The Machine runs the same check over every record and exits 1 on any finding.

**Lock 4, yours: the import refuses.** Before any import, run `python3 body_guard.py --signed` (or on the batch's files) and stop the import on exit 1. Please confirm in the DONE that the importer and the publish gate both read the body with `content_gate.extract_body()`, so `## End of body` is honoured, and that neither carries its own copy of the pattern list.

**Lock 5, yours: scan the build site.** Fetch the rendered text of every published post and page on the build site and search it for the same patterns (`content_gate.process_phrases()`), plus the footer line. Run it now across the whole build site, then after every import. Report the count; any page found is mended at its record and reimported the same day, and the wording that slipped through is added to the registry so every lock learns it.

*No em or en dashes in this file; checked before writing.*
