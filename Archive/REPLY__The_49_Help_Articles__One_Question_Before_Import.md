# REPLY: the 49 Help articles — found the file, one question before I import

**From:** Claude Code · **Date:** 2026-07-27 · **Re:** *S223 - The 49 Help
articles ready to import plus audio*

## I have the file

It is there and the content is complete. One thing to flag so we are working
from the same picture: **the filename and shape differ from your note.**

| | Your note said | What is in the folder |
|---|---|---|
| Filename | `Achology_FAQ_49_Help_Articles_IMPORT_43col.csv` | `Achology_FAQ_49_Help_Articles_COMPLETE.csv` |
| Rows | 49 | **51** |
| Columns | 43 | **48** |
| Byte-order mark on `id` | yes | **no** |

Checked against the proven master: **all 43 master columns are present and
populated**, in the master's own schema. The differences are additive, not
missing content:

- **Five extra working columns:** `why_this_is_a_gap`, `vault_source_note`,
  `priority`, `closest_existing_question`, `overlap_score`. These are the
  gap-analysis columns your note said are "stripped before hand-off".
- **Two extra rows:** `GAP-018` ("What is the Achology Professional Directory
  and how do I get listed?") and `GAP-019` ("Why would I be removed from the
  Achology Professional Directory?") — exactly the two parked Professional
  Directory rows your note said were excluded.

Remove those two rows and those five columns and it is precisely the 49-row,
43-column file you described. So this looks like the working file was saved to
the folder rather than the stripped hand-off file.

The renamed category is present and correct: 12 rows carry **"Accreditation and
Certification"**. I will match on `category_slug`
(`certificates-cpd-accreditation`), never on the display name, as you asked.

## The one question, and the only thing blocking me

**Did you intend to strip the five working columns and the two parked rows
before hand-off, or is that stripping mine to do at import time?**

I am not deciding this myself. Either answer is easy for me:

- **You strip it and re-hand the file** — I import exactly what you give me,
  no transformation on my side, which is the safer of the two because the file
  you verified is the file that lands.
- **I strip it here** — tell me explicitly and I will drop `GAP-018` and
  `GAP-019` and those five columns, add the byte-order mark to match the
  master, and show you the resulting header row and row count for confirmation
  **before** anything touches the site.

I would rather you re-handed it, so that the file your content gate passed is
the file that gets imported. But it is your call.

## Everything else in your note, held until you answer

I have not started the import, the audit or the audio. **Kain has stopped my
build work** pending a harness being designed around how I operate (see
`REQUEST__Design_A_Harness_Around_Code__Honest_Failure_Analysis.md` and
`HANDOVER__Full_Site_Inventory_and_Standardisation_Brief.md` in this folder).
So please treat this as a reply to your question, not as work starting.

When Kain releases it, I will come back with the import method, the count
checks, the end-to-end spot checks including a certificate-category row, and
what I need from you on the audio (voice, format, naming, destination) rather
than assuming any of it.

Thank you for the file, and for the CSS gate — that gate is the most useful
thing anyone has built on this project and I should have read it hours earlier
than I did.
