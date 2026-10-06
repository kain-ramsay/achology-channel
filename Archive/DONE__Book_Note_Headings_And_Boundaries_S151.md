**Record, asks nothing (theme session S151): the 150 book note headings, the S150 fallback removed, Boundaries corrected, and the page checker made fast. Theme 0.707.136.**

# DONE: book note headings and Boundaries (S151)

- **Five new headings in all 150 book notes**, Kain's S150 wording, through `tools/book_note_headings_S314.py` on clearance 1370a18d83ac9812: 150 of 150 changed and read back correct. Five books with more than one author read "The Authors’ Background and Perspective".
- **0.707.136 deployed**: the S150-only fallback in `single-book_note.php` removed. Contents links checked against the headings' ids on five book notes (Noise, Utilitarianism, Boundaries, Crucial Conversations, Cognitive Behavior Therapy): all five match.
- **Boundaries (post 35940)**, clearance f06ea2a3087d52ee: cover imported under a new name, `boundaries-cloud-townsend.jpg` (attachment 40319), so browsers cannot show the old picture; amazon_url `https://www.amazon.com/dp/0310351804?tag=kainramsay01-21`; isbn 0310351804. Read back; the live page carries both; the Amazon address opens the Updated and Expanded Edition by Cloud and Townsend. For Chat's record: source_book_author still reads "Henry Cloud" only.
- **Aaron Beck link** in the Cognitive Behavior Therapy book note (35942) pointed at an address that does not exist; corrected to `aaron-beck-the-pioneer-who-revolutionized-cognitive-psychology` on Kain's yes (override clearance f2ad4fa9163862bf).
- **The page checker** (`publish_gate.py`, `page_gate.py`): links to pages not built yet never block an update on the build site (RULING__Unbuilt_Links_Never_Block_S151 in TO Chat); pages measured ten to a browser, each address asked once per run, passing readings saved so a stopped run resumes. 150 pages went from about two and a half hours to about 15 minutes. Three batches at once was tried and made the build server answer 502; it runs one batch at a time.

OWED BACK: nothing; a record.

*No em or en dashes in this file; checked before writing.*
