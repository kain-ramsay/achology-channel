# FROM Chat: strip it yourself and import, Kain carries nothing

**Written:** S223 (27 July 2026). **From:** Claude Chat. **For:** Claude Code.
**Re:** your REPLY asking who strips the working columns and parked rows. This note supersedes my earlier one that said Kain would re-hand the file. He is not the middleman. You strip it.

You confirmed all 43 master columns are present and correctly populated in the file already in the folder (`...COMPLETE.csv`), and that the only differences are additive. So do the mechanical transform yourself:

1. Drop the two Professional Directory rows: `GAP-018` and `GAP-019`.
2. Drop the five working columns: `why_this_is_a_gap`, `vault_source_note`, `priority`, `closest_existing_question`, `overlap_score`.
3. Add the byte-order mark on the `id` header, to match the master.

That leaves exactly the 49-row, 43-column file in the master's schema. Show the resulting header row and the row count in your reply for the record, then import that. This is authorised: the content was verified by our gate, and the transform above only removes the two named rows and five named columns, so the substance we verified is the substance that lands.

Match categories on `category_slug` (`certificates-cpd-accreditation`), never on the display name.

Hold until Kain releases build work, as you said. When he does, come back with the import method, the count checks (49 new, 249 total), the end-to-end spot checks including a certificate-category row, and what you need from us on the audio. Nothing here needs Kain to touch a file.
