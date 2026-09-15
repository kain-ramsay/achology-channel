# REPLY: the sixteen fields the book-note importer still carries nowhere

**Filed by Claude Code, Session 118. Date:** 15 September 2026.
**Answers:** item 2 of `REPLY__Five_S329_Fields_Into_The_Importer_Then_The_Nine_Import_S361.md`.

---

The five S329 fields are in (`book_note_import.py`, `Book_Note_Master.xlsx` header, `Book_Note_Upload.csv`). These sixteen remain, named with what a real record's row actually holds, so your ruling has real values in front of it rather than a bare list of names.

| field | one live example |
|---|---|
| `amazon_genius_link_url` | `https://www.amazon.co.uk/s?k=A+Path+through+the+Jungle+Steve+Peters&i=stripbooks` |
| `brief_state` | `pre-standard` |
| `cover_status` | `pending` |
| `demand_evidence` | `Stage 0 check run S344 (Cowork): live search on "A Liberated Mind"... Focus keyword unchanged, evidenced.` |
| `destination_course_url` | `/academy/cognitive-behavioural-psychology/cbt-toolkit/` |
| `inbound_from` | Three site addresses, each with the sentence the linking page uses to reach this one |
| `kh_tag_order` | `master-your-mindset,grow-self-awareness,beginner-friendly` |
| `prod_cover_image_alt` | `Book cover of A New Guide to Rational Living by Albert Ellis and Robert A. Harper` |
| `prod_delivery_note` | `Well-documented revised REBT text: draft from knowledge, verify claims with live research. No full-text quoting.` |
| `prod_first_published` | `1961` |
| `prod_free_source` | `Live research` |
| `prod_note_author_name` | `Benjamin Lockwood` |
| `prod_recommended_course_name` | `The CBT Toolkit: Core Principles and Real-World Applications` |
| `prod_source_route` | `Route 2: knowledge + research` |
| `prod_subtitle` | `A Practical Method for Overcoming Irrational Beliefs` |
| `publication_year` | `2009` |

Checked, not guessed: `content_gate.py`'s `S329_FIELDS` contract does not name any of these sixteen, and none is read anywhere in the theme's PHP (grepped whole). Nothing here is currently reaching a published page either way; the question is only which of them should.

Waiting on your ruling before touching any of the sixteen.
