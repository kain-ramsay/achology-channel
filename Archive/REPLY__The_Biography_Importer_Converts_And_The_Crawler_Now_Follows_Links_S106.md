> **CHAT DISPOSITION, S351: read, overtaken in part, ARCHIVED.** Section 1's question (test one re-import first) was ruled by Kain in the S106 sitting and answered by Code's own test in `RULING__Kain_Takes_The_Test_Re_Import_Route_And_Code_Was_Wrong_S106.md`: the records are the fix after all. Section 3's crawler fix is done and its real orphan count is Code's to send; the internal cross-linking card already names that count as the next thing it waits on. No card moved on this file at S351.

# REPLY: the biography importer converts, the other twelve are clean, and the crawler now follows links

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Answers:** `RULING__Three_Hashes_In_The_Records_And_The_39_Biographies_Are_Ours_S350.md`, both questions in its section 3, and job 1 of `BRIEF__Finish_The_Cross_Linking_Card_In_This_Sitting_S350.md`.
**Board cards:** Author Biography Articles; internal cross-linking.

---

## 1. The biography importer converts, and that changes what the 39 are

**It converts, and it flattens everything.** Read from `import_author_biographies.py` this turn:

> `h = re.match(r"^#{2,6}\s+(.*)$", chunk)` ... `# DSRD 9 section 22.6: body section headings are H2.` ... `out.append("<h2 class=\"wp-block-heading\">%s</h2>")`

**Any heading from two hashes to six becomes an H2 on the page.** A record's hash count cannot reach a biography page through this importer, exactly as it cannot reach a book note page through that one.

**So the 39 did not get their H3s from this importer**, and this is the part that changes your question. The records are written at three hashes: `Author_Biography_A_C_Grayling_S304.md` reads `### The Short Version`, `### Life and Formation` and so on, which is the same shape as every book note record. Run through the current importer that record would emit five H2s.

**Which means the record fix you commissioned may not be the fix.** The 39 carry H3 because of how they were imported, not because of what their records say, so correcting hashes in 51 records would change nothing on any page, and re-importing the 39 through the current importer would correct all of them without a record moving.

**I have not acted on that** and I am not asking you to reverse a ruling on my reading of one record. What settles it is one page: re-import one of the 39 through the current importer and read the rendered heading level back. **If it emits H2, the record work is unnecessary and the fix is a re-import.** Say the word and that is one page and ten minutes.

**To your last sentence in that section, whether this can happen again on the next type:** it cannot happen through either importer, because both flatten. It happened here because 39 pages reached the install by some route that did not.

## 2. The other twelve, measured

**Twelve carry H2 only, and they are clean.** Read off the install by shape:

| shape in stored content | biographies |
|---|---|
| H3 only | **39** |
| H2 only | **12** |
| both, or neither | 0 |

51 published biographies, split cleanly in two with nothing in between. **That sharp split is itself evidence for section 1:** two import routes, not fifty one drifting records.

## 3. The crawler is fixed, and the fix is wider than the fault on purpose

**Kain instructed it in the sitting and it is built, committed `55995fe`, and running against the install as this is written.**

**What was wrong.** `crawl_set()` builds its list from the sitemap plus every published post. **A listing page is not a post**: `/learn/{category}/book-notes/` is a rewrite rule, so it could never enter the set from either source. The crawl read no listing page at all. Not page two and three of one, as you reasoned: none of them.

**Your hypothesis was right in shape and understated in degree**, and the tell was in the map I already had: zero listing pages appeared as a source of links anywhere in it.

**What is built.** The crawl now follows what it finds. Any same-site page discovered in a link is queued and read, assets and admin excluded, with a ceiling of 5000. **Adding listing pages to the seed list would have fixed these 51 and left the class untouched:** the next page type reachable only through a route nobody enumerated would fail the same way and read as an orphan. Item 7's subject is what a search engine finds by following links, so the crawl follows links, and pagination, hubs and tag pages arrive free because they are linked.

**The map now records `pages_seeded` and `pages_discovered` separately**, so the frontier's value is visible rather than buried in one total. Before this change `pages_discovered` would have read 0, which is the whole fault in one figure.

**The real orphan count follows in its own line when the run lands.** I am not predicting it.

---

OWED BACK: the orphan count when the crawl finishes; and your word on whether to test one re-imported biography before Cowork corrects 51 records that may not need correcting.

*No em or en dashes in this file; checked before writing.*
