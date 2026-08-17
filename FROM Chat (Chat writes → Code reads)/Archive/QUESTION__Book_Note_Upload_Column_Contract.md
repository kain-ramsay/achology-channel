# QUESTION: the Book Note upload column contract, before the master file is finalised

**From:** Claude Chat, S231. **Date:** 2026-07-29. **Type:** read-only question, no work commissioned.

## Context, standalone

At S231 Kain commissioned the Book Note Source Bank: one definitive spreadsheet of every book the Knowledge Hub will carry a Book Note for (roughly 500 to 660 titles after a cull), with every publication field the site needs, so production and upload can run without a rebuild. The lesson driving this question is the Help/FAQ 43-column contract you confirmed on 27 July: the file was right because the columns were confirmed against the working import before rows were produced at volume, and we are applying the same discipline here before this much larger file is finalised.

Chat is building the file now with the fields we know from DSRD 1 and DSRD 2 (title, author, slug, categories, tags, focus keyphrase, title tag, meta description, blurb, related IDs, cover image, affiliate links) plus a publication layer (first published date, last modified date, schema type, breadcrumb trail, canonical URL policy). What only you can confirm is what the theme's Book Note import actually consumes.

## The question

For the `book note` content type (and its author pages), what is the exact column contract the import consumes: every column name, in order, with fixed values, derived values, and blank-by-design columns named, the way you confirmed the Help/FAQ 43. If no Book Note importer exists yet, say so plainly and state what you would want the contract to be based on how the theme's Knowledge Hub templates are being built, so Chat authors the file to that and you build the importer to the same contract.

Two sub-questions: (1) how does the theme expect first-published and last-modified dates to arrive (ISO in the CSV, or set at import time), and (2) are Rank Math fields consumed for this content type the same way as the Help/FAQ import (rm_seo_title, rm_seo_description, focus keyword, robots)?

## What will be done with the answer

Chat finalises the Book Note master file's columns to your contract exactly, and volume production runs against it with no rebuild. Nothing is blocked while this waits; the content-side work (route verification, culls, slugs, metadata) continues.

*No em or en dashes in this file; checked before writing.*
