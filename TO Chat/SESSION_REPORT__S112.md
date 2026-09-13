# SESSION REPORT: S112, theme session, Sunday 13 September 2026

Assembled from the version control log for the session, per Harness Rule 13. Theme 0.326.0 at the open, 0.377.0 at the close, 48 change sets, all deployed to the build ground and pushed to origin.

---

## Finished

**The S111 sweep, family one: the three reading pages.** Board card: the type scale sweep. The reading text is 18 on 1.75, the reading column 800, the paragraph gap 16, and three heading sizes became one, across the article, the book note and the help answer. 23 off-scale sizes came onto the nine steps across the help family and the reading pages' own furniture. Filed as `RULING__The_Article_Template_Rebuilt_With_Kain_S112`.

**The two gate checks Kain asked for at the S111 close.** `css_gate.py` gains E, size is a role, and F, width is a token. Both are live and both fired during this session, refusing files until they were clean. Remaining across the families not yet swept, measured this session: 87 off-scale sizes and 77 hand-typed on-scale sizes.

**The sweep's acceptance instrument.** `previews/sweep_diff.py` renders the three real pages against two git revisions and reports every element whose computed type, spacing or width moved. `previews/sweep_sitting.py` builds the two-column before and after. `tools/type_step_sweep.py` applies a plan of named line-and-value pairs and refuses any row that has moved.

**The article template, rebuilt with Kain.** The whole of it is in the RULING file named above. Board card: the Knowledge Hub article template.

**components.css and people.css onto the nine steps.** Forced by the new gate, which refuses any edit to a file that still breaks them. 13 declarations in components.css, 7 in people.css, four one-off widths annotated.

**The trial panel and the course block take Kain's rewritten copy.** Both given whole in the sitting, typed character for character, and both reach every hub page type.

**deploy.py refuses PHP that will not parse.** Added after this session shipped a stray comment block that took the whole build site down for a few minutes. Every theme .php is now piped through the server's own PHP before the rsync, in one session, and the deploy is refused if one fails. Proved by breaking a file on purpose.

**Two faults of mine, reported because they cost Kain time.** A preview rebuilt at the same address showed him a cached page twice, now fixed with a build number on every asset; and a rule that set a size on a link rather than on the words inside it was reported as done after measuring the wrong element.

## Not finished

**The article page does not pass its own gate.** `page_gate.py`: 40 passed, 12 failed. Two were mine and are fixed. The rest are content: a dead link, four unspelled acronyms, keyword density at 0.30 against a 1.0 floor, no DSRD 6 record, and a Rank Math score older than the page. **Next session, first job**, and it is a factory sitting.

**The five author biography headings are not applied.** Chat's reply arrived mid-sitting. 51 records and 51 live pages, verified on the install this session; no other post type carries them. Factory work.

**The rest of the S111 sweep.** Families not yet swept: cards, about, reviews, testimonials, global impact, policies, quote, course, header, footer. The gate names every one.

**Three briefs read and queued, all factory work, all dispositioned in FROM Chat:** the 50 book quote imports, the Search Console pull for the 28 course pages, and the author biography heading sweep.

## Hand added, no machine record

Nothing. Every line above appears in the log.

OWED BACK: nothing. The rulings travel in their own file.

*No em or en dashes in this file; checked before writing.*
