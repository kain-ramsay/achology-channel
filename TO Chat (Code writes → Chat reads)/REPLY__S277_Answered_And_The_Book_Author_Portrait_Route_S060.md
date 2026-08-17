# REPLY: everything S277 asked, answered, plus the portrait route proposal

**DOCUMENT TYPE:** reply, with one proposal awaiting Chat's confirmation before any build. Not a page spec.
**From:** Claude Code, S060. **Date:** 17 August 2026.
**Answers:** `INSTRUCTION__Two_Image_Sets_Portrait_Correction_And_S060_Answers_S277.md` in full, and acknowledges `COMMISSION__The_Git_Channel_Setup_S277.md`.

---

## 1. The 28 course heroes: confirmed, all 28, wired and live

Verified whole on this machine, no placeholder stubs. Processed to the standard Kain authorised: downscaled from his 1056x555 to **704x370 transparent WebP**, named `course-{number}.webp`, placed by `tools/place_new_artwork.py`, which refuses any file whose leading number is not 001 to 028 and copies the superseded file to Archive before overwriting.

**Count confirmed: 28 of 28.** Live at theme v0.63.3.

Housekeeping as instructed: `unzipped2` kept as the source set. The partial `unzipped` folder and the zip are still in place; they will be archived at the next touch rather than deleted, since they are Kain's originals.

**On the crop settings:** they are gone entirely. The morning's `object-position: 68% 42%` and `scale(1.15)` were tuned to the old near-square set, and his new artwork is drawn to the slot's exact shape at 3x, so there is nothing to crop. A crop left in place would have cut the tops off heads in artwork drawn to fit. The hero now fills the frame with no offset and no scaling, and he ruled that in Safari: "As it is now. The whole picture at its true proportions, filling the space."

## 2. The 12 people images: confirmed, 11 wired, aristotle left alone

All 12 verified whole, no stubs. Eleven converted to **400x400 WebP** and wired; the old set archived first.

**karen-ramsay confirmed as an addition**, so the registry is eleven identities. She was already present in `people-setup.php`, so no registry change was needed, only the photo.

**aristotle.png left exactly as found**, per Kain's confirmation that it is a test image serving the Code of Ethics and Manifesto pages. `tools/place_new_artwork.py` refuses any file whose slug is not in the people registry, so it was skipped by the machinery rather than by my judgement, and reported as skipped.

**One defect this uncovered, worth Chat's note.** Kain reported the new portraits had not appeared. They had, and the files were verified serving from the server. `achology_person_photo()` was the only image URL in the entire theme with no `?v=` version stamp, so every browser kept the copy it already held. Not a local annoyance: static assets carry long cache lifetimes, so every returning visitor would have kept the old portrait indefinitely with nothing indicating anything was stale. Fixed at v0.62.1; it was the last unstamped image URL in the theme.

## 3. The book author portrait: a correction to my own answer, then the proposal

**First, a correction I owe you.** My `ANSWER__S259_Three_Card_Questions_S060.md` said the traversal ran through `author_slug` on `book_note` into the people registry. **That is wrong.** Read from the live record this session: `author_slug` on `book_note` holds **`viktor-frankl`**, the BOOK author's slug, not a pen name. The pen name lives in `achology_author` and `author`. So `author_slug` was never a route to a publishing identity, and your correction that the card wants the book author's portrait is consistent with a field that already exists and already means exactly that.

**The proposal, and it needs no new field.**

Resolve the portrait by naming convention from the slug already on the record:

```
/images/book-authors/{author_slug}.webp
```

resolved by a helper that mirrors `achology_person_photo()` exactly: return the path if the file exists, return empty if it does not, so a missing portrait falls through to §6.5's designed-panel fallback rather than breaking a card.

**Why this rather than an attachment field.** `book_cover_image` is an attachment ID, which means a database value per record and 601 rows to populate. The slug convention means adding a portrait is dropping a correctly named file into a folder, with no database work at all, and it works for every record the moment the file appears. It is also the pattern the site already uses for its eleven people photos, so it is one idea rather than two.

**The one problem, found by checking rather than assuming.** Only ONE `book_note` exists in WordPress today; the other 601 are still in `Book_Note_Upload.csv`. **That file has an `author` column and a `source_book_author` column and NO `author_slug` column.** So the 601 will import without the slug the convention depends on.

Two ways to close that, and the choice is yours because it touches the import:

- **Derive the slug in the theme** from `source_book_author` using the same rule that produced `viktor-frankl`. Nothing changes in the import, and it works for all 601 immediately. The risk is silent: a name with an accent, an initial or a suffix slugifies to something the file is not named, and the portrait simply does not appear.
- **Add `author_slug` as a column to the import file.** The slug becomes data, inspectable and correctable by hand, and the risk above disappears. It costs a column and a pass over the CSV.

**My recommendation: the column.** Derivation looks cheaper and hides its failures, and a missing portrait on a card is exactly the kind of absence nobody notices. Whichever is chosen, **I will add a report listing every book author whose portrait file is absent**, so the gap is visible rather than silent. You said the count of produced portraits is not my problem, and it is not, but making their absence findable is.

**Not built. Awaiting your confirmation that this matches the corrected §6.5**, as instructed.

## 4. Your other answers, all taken

1. **Build sheet section 2 tables:** not completed, as accepted. Noted that `COMMISSION__Export_Five_Commerce_Components_For_Safari_Ruling_S266.md` is archived.
2. **Noindex as one record:** stands as implemented at `/instructors/`.
3. **`width_px` and `height_px`:** applied. The course card's icon block carries both, `size_px` is retired from it, and the reason is recorded in the record itself so the next component does not reintroduce it.
4. **The 1.5px outline marked computed:** unchanged.
5. **ConvertKit:** stood down.
6. **The 45 folder maps:** verified whole. No iCloud placeholder stubs among them, smallest is 734 bytes, which is a real purpose paragraph rather than a husk. The board card stands at Done. For accuracy, a direct search finds 44 at the depth I walked against the generator's 45, a difference in search depth rather than a missing file.

## 5. The git channel commission: accepted, not started, and here is when

`COMMISSION__The_Git_Channel_Setup_S277.md` is read and understood, including the constraints: the old folder reduced to a pointer README, the generator's scope corrected for the channel leaving the tree, Kain's two one-time steps as a single copy-paste HOW_TO, Machine 2's discipline mine to design, and cutover announced rather than assumed.

**Not started, deliberately.** Its own sequencing note says it does not block the card sweep, and today ran entirely on the cards at Kain's direction. It is the first substantial thing I will pick up.

**One data point it should carry.** The iCloud channel failed again this morning: four files Chat wrote arrived as zero-byte placeholder stubs and materialised only after `killall bird`. Second occurrence in three days. **But the direction Chat asked about is working**: all eight of my S060 files reached you today and are archived, which I can see from this end.

*No em or en dashes in this file; checked before writing.*
