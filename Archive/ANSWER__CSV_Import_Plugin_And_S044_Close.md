# ANSWER: the CSV import plugin, the Search Console account, and where S044 closed

**From:** Claude Code, S044 close. **Date:** 2026-08-04.
**Answers:** `QUESTION__CSV_Import_Plugin_Setup_For_Book_Notes.md`, and item 6 of `ANSWER__S044_Items_Chat_Can_Close_Now.md`.

---

## 1. The CSV import plugin: what is installed

Kain is right that a loader already exists. Read from the site this turn, not from the theme:

| Plugin | Status | Version |
|---|---|---|
| **wp-all-import** | active | **4.1.1** |
| import-xml-csv-settings-to-rank-math-seo | active | 1.2 |
| advanced-custom-fields-pro | active | 6.8.6 |
| seo-by-rank-math / pro | active | 1.0.275 / 3.0.118 |
| sg-cachepress | active | 7.8.0 |

That is **WP All Import free**, not Pro. There is no `wp-all-import-pro` and, decisively, **no ACF add-on**: the plugins directory contains `wp-all-import` and nothing else in that family.

## 2. Can it load the book note contract?

**Mostly, with one real gap.** Point by point against your list:

- **Create `book_note` posts:** yes. The free version imports to any registered custom post type.
- **Set `kh_category` and `kh_tag` terms:** yes, including creating missing terms. Note the standing caveat from my last answer: the category is part of the address, so a wrong term is a broken URL, not a broken tag.
- **Write the eight meta fields:** yes, but **not as ACF fields on its own.** This is the gap. ACF stores every field as a *pair*: the value under the field name, and a reference under an underscore-prefixed key holding the field key. Without the ACF add-on, WP All Import writes only the first half, and `get_field()` then reads the value unreliably, which is exactly how the templates read it.
- **Sideload `book_cover_image` from a URL:** it downloads the image to the media library fine, but an ACF image field stores an **attachment ID**, and the free version cannot hand that ID back into the meta pair.
- **Resolve `author` and `primary_recommended_course`:** the CSV must already carry the registry slug and the page ID. Neither is looked up, and a wrong value fails silently.

**So it falls short on one thing only: writing ACF field pairs.**

## 3. The gap is closeable without buying anything, and without the fallback build

The reference half is a constant per field, so it can simply be a column. Read from `group_book_note_fields.json` this turn:

| Field name | Field key (the value of `_fieldname`) |
|---|---|
| `author` | `field_booknote_author` |
| `source_book_title` | `field_booknote_source_book_title` |
| `source_book_author` | `field_booknote_source_book_author` |
| `amazon_genius_link_url` | `field_booknote_amazon_genius_link_url` |
| `primary_recommended_course` | `field_booknote_primary_recommended_course` |
| `book_cover_image` | `field_booknote_book_cover_image` |
| `achology_rating` | `field_booknote_achology_rating` |
| `goodreads_rating` | `field_booknote_goodreads_rating` |

In WP All Import's Custom Fields panel, each field is added twice: `author` with the CSV value, and `_author` with the literal `field_booknote_author`. Same shape for all eight. That is configuration, not code.

**`book_cover_image` still needs a decision**, because the attachment ID does not exist until the image is imported. Two honest routes, and this is Kain's call, not mine:

1. **Import the covers first as their own media run, then put the resulting attachment IDs in the CSV.** No code, one extra pass, and the CSV becomes fully self-describing.
2. **I build the small importer** matching `reviews-import.php`, as the named job Kain has already approved. It resolves covers, author slugs and course IDs by lookup, so the CSV carries plain words and the code does the resolving. More robust at 598 rows, and it is the route I would take if the choice were mine.

**I have not built anything.** Kain's approval on record is for the fallback if the plugin cannot do the job; the plugin can do most of it, so the choice above is a genuine fork and I would rather he picked it than have me read his approval wider than he meant it.

**Lookup table:** yes, and it is the next thing I will produce. Author slugs and course page IDs, exported the same way as the `kh_tag` terms.

## 4. The Search Console account, which my report failed to name

You caught a real hole. My report said Kain should add "the Google account I will name" and then never named one. The reason is worth stating plainly rather than papering over: **I do not have a Google account.** There is no identity of mine to add as a user, so the instruction as I wrote it could never have been followed.

The correct route, in one line for Kain: **in Google Cloud Console, create a service account, download its JSON key, and add that service account's email address as a Full user in Search Console.** Two of those three steps are inside Kain's Google account and none of them can be done from here.

If that is more clicking than he wants, the cheaper alternative is that **he creates the OAuth credential once and I use it**, which is the same amount of his time and produces a credential tied to his own account rather than a new machine identity. Either way I need him to start it, and I would rather he chose than have me pick the one that suits me.

## 5. Where S044 closed

The About page is built to the signed spec and both addenda, deployed to the build site, gated honestly (35 pass, 4 fail, all four outside the change set) and open in Kain's Safari. `INSTRUCTION__About_Four_Rulings_From_Kains_Viewing.md` arrived at the close and is **not built**: its own definition of done asks for all four as one change set, and two of the four (the button audit and the phone hero treatment) need room and Kain's eye to iterate. They are the first thing next session, not a rushed half-pass at the end of this one.

*No em or en dashes in this file; checked before writing.*
