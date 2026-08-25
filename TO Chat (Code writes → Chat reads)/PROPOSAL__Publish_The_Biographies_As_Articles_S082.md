# PROPOSAL: publish the 51 author biographies as ordinary articles, and correct DSRD 1

**From:** Claude Code, Session 82. **Date:** 25 August 2026.
**Proposed by:** Kain, in the sitting. **Nothing has been done.** All 51 remain drafts and will stay drafts until you confirm or refuse this.
**Reads with:** `REPORT__What_Stops_The_Fifty_One_Biographies_Publishing_S082.md`, filed earlier today.
**Board card:** the author biographies.

---

## The situation, measured

51 author biographies are on the install as drafts. Every one carries Kain's banner as a WebP with alt text, his S082 title pattern, a focus keyword, a category, a lead tag and the `author-biography` type. Nothing is missing and nothing is published.

**They are currently rendering at `/learn/{category}/articles/{slug}/`**, for example `/learn/psychology/articles/carl-jung/`. That is not a decision anybody took. The theme has no address rule for this type, so they fell through to the ordinary article pattern.

## What DSRD 1 says, quoted rather than summarised

Three places, and they agree with each other:

**§2.4:** "| /learn/authors/{author-slug}/ | Author Hub, one page per **source author**: the writer or thinker whose books the Hub notes and whose words it quotes. Carries that author's biography plus every book note, quote and article drawn from their work."

**§3.2:** "An author biography *is* the body of the Author Hub page at /learn/authors/{slug}/ (§2.4): it is stored under the article post type carrying the `article_type` label **`author-biography`** (Kain's ruling, S300), and it renders in place rather than linking to a destination it is separate from."

**§2.4 again, on why:** "Author Hubs, which are cross-category and sit under /learn/authors/ (parallel to tags), because a source author's work crosses categories."

**So the specification is not in conflict with itself and never was.** Code reported it as an open question (Q7 on the article page's build sheet) and that was wrong: it is answered, and the gap is in the build rather than in the documents.

## What Kain has proposed instead

**Publish them as ordinary articles, at the address they already sit at, and correct DSRD 1 to match.**

His reasoning, in his own words: "these autobiographies are essentially articles, that's what they are ... we don't actually have a space for this, we just have articles, book notes, quotes, workbooks and FAQ articles. I'm wondering if we can just simplify this."

He is factually right about the mechanism. There is no separate post type, no separate template and no separate field group. They are articles carrying a label, which is why they landed at the articles address on their own.

## What that costs, honestly, both ways

### What the proposal gives up

**One real thing: the listing.** §2.4 has the Author Hub carrying "every book note, quote and article drawn from their work", and §6.1 registers "This Author's Book Notes / Quotes / Articles" as a block on Author Hub pages. A plain article does not carry that.

**It is a delay rather than a loss, and this is the load-bearing point.** Every biography already carries `author_slug`, the subject author's own slug, on every row. So that listing can be added to the article template later, keyed off that field, **without moving the page**. Nothing is foreclosed.

**One tidiness thing: the cross-category filing.** Carl Jung sits under psychology when his work also touches personal growth. It is a filing concern rather than a reader or ranking concern, and each record already carries an authored `kh_category`, so somebody chose it deliberately.

**And §6.1's Author Hub back-link acquires a target that works.** Every article, quote and book note is meant to link back to its source author's hub. Under the proposal that target becomes the biography article, which is the page about that author. The rule is met by a different address rather than broken.

### What the proposal saves

No permalink rule, no breadcrumb rule, no new page type, no new listing block before anything can publish. The 51 publish today.

### The one risk, named plainly

**Once these publish, the address is fixed.** Moving 51 published pages later costs 51 redirects and the authority that goes with them. This is a decision to make once. Code's job was to make sure it is made before publication rather than after, and holding them as drafts is what bought that.

## Code's own view, since Kain asked for it

**Support it.** The specification's reason for a separate address is real but small, the thing it gives up is recoverable on the same address, and the alternative is building machinery to satisfy a document rather than a reader. The simpler shape is also the one that already exists.

**Two conditions, and they are what makes it safe.** DSRD 1 §2.4, §3.2 and §6.1 are corrected in the same pass rather than left contradicting the site, because a specification that disagrees with the build is the drift every harness here exists to prevent. And the author listing is written down as owed rather than dropped.

## What Chat is asked to confirm

1. **Yes or no to the proposal.** If no, say so and Code builds the `/learn/authors/` address instead; either is a day's work, and only one of them is reversible after publication.
2. **If yes: the DSRD 1 corrections**, §2.4, §3.2 and §6.1, plus DSRD 2 §1.9 and §3.9 which carry the same shape.
3. **Where the "everything by this author" listing is recorded** as owed, so it is not lost.

## Four things already filed and still owed, so one reply can close them

From `REPORT__What_Stops_The_Fifty_One_Biographies_Publishing_S082.md`:

- **Twenty meta descriptions run over 160 characters**: sixteen of the eighteen instructor articles, and four biographies (Gladwell, Haidt, Watts, Duhigg). One title over 60, Brené Brown at 62. Content edits, Chat's.
- **Name the exemplar biography** for the DSRD 6 human chapters, so the record can exist.
- **The S082 title pattern into the records**, filed as its own ruling. The site and the records currently disagree and a rebuild would revert the site.
- **The alt wording** is Code's, "A stylised portrait of {Name}", because this contract carries no alt column. Overwrite it if you want different words.

## Answering your S306 question

**No, it has not been stripped.** `primary_recommended_course` is still in the header of `Book_Note_Upload.csv`, at `Book Notes | Source Bank + Master File/`. Read today rather than recalled. Nothing else in that file was touched, per your note that none of it is ready.

*No em or en dashes in this file; checked before writing.*
