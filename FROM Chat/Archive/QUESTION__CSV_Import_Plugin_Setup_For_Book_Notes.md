# QUESTION: what CSV import plugin is on the site, and can it load book notes?

**From:** Claude Chat, S238. **Date:** 2026-08-04.
**Follows:** your ANSWER__Book_Note_Column_Contract.md. Kain has ruled on the loader, with one check first.

Kain says the site's mass uploads have been going through a CSV plugin on the WordPress site (that is how earlier bulk content went in), so a loader may already exist that your theme-only survey did not cover. Before anything is built:

1. **Name what is installed.** Which CSV import plugin is on the site, and its version.
2. **Can it load the book note contract?** Specifically: create `book_note` posts; write the eight meta fields; sideload `book_cover_image` from a URL column into an attachment; resolve `author` as the people-registry slug and `primary_recommended_course` as a page ID; and set `kh_category` and `kh_tag` terms.
3. **If it covers all of that:** no build. Chat produces the CSV to the plugin's expected headers; confirm those headers if they differ from the contract you gave.
4. **If it falls short:** name the gaps. Kain has already approved the fallback: you build the small importer matching reviews-import.php, as one named job. His approval is on record here, so if the plugin cannot do it, proceed to the build without waiting on another round trip.

*No em or en dashes in this file; checked before writing.*
