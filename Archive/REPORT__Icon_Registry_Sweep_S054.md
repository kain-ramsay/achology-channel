# REPORT: the icon registry sweep

**From:** Claude Code, Session 054. **Date:** 2026-08-11. **Theme:** v0.60.5, deployed and verified live.
**Answers:** `COMMISSION__Icon_Registry_Sweep_S262.md`, items 1 to 4. The build sheet export at the end of that file is reported separately below.

## 1. Kain's ruling 2, applied

Three call sites moved, and nothing else changed on any page:

| Where | Was | Now |
|---|---|---|
| The figure register's courses row, `achology_figures()` | LibraryBig | GraduationCap |
| The manifesto page's Browse All of Our Courses card | Library | GraduationCap |
| The code of ethics page's Browse All of Our Courses card | Library | GraduationCap |

LibraryBig now has one caller, the Knowledge Hub, which is what the ruling asked for: the 404 page's Knowledge Hub door and the routes-grid Knowledge Hub row. The 404's Courses door still carries BookOpen, the recorded exception.

**ONE JUDGEMENT CALL, FLAGGED RATHER THAN DECIDED, AND IT NEEDS KAIN'S EYE.** The manifesto's pair panel has two cards: Browse All of Our Courses, and Explore Our Seven Schools. The second was already GraduationCap. So the flip has put **the same glyph on both cards of one two-card panel**, side by side, on a page Kain approved. The ruling did not address the collision. It is live at v0.60.5 because the ruling said flip it, and it is a visible change on an approved page, so it is his to settle on the rendered page. The code of ethics panel has no collision: its other card is MonitorPlay.

## 2. The sweep itself

**100 loose inline SVGs are now registry calls.** Twelve drawings that had no key got one. The registry is **49 glyphs**, up from 37.

| Group | Count | What happened |
|---|---|---|
| Repointed at `achology_icon()` | 100 | 78 written as markup, 22 written as whole PHP string literals |
| Newly registered drawings | 12 | listed below |
| Deliberately left out, Kain's three exempt groups | 10 | 6 footer social marks, 3 breadcrumb separators, 1 artwork (the About era chart) |
| Filled marks, not the outline registry | 2 | the two play triangles |
| Left inline, reported here | 12 | the drift pairs and the two string-concatenation sites, both below |

**The twelve new keys**, every one moved from the template that carried it rather than redrawn: `circle-question-mark`, `circle-x`, `arrow-down`, `arrow-up`, `badge-check`, `shield-check`, `layout-grid`, `menu`, `thumbs-up`, `thumbs-down`, `book-marked`, `clock`.

`circle-question-mark` was the most-repeated loose glyph on the site, at ten call sites across About, testimonials, the manifesto, the code of ethics and the founders' letter. It is a different drawing from the registered `message-circle-question`, which is the speech-bubble variant, so both keep a key.

**The proof, because a sweep of this size is exactly where a page loses a glyph silently.** Twenty-three built pages were captured before the sweep and again after it, and every inline SVG on every page was compared by drawing, by attribute set and by position in the page. **Three drawings changed across the whole site, and all three are the ruled courses-glyph flips above.** Everything else is identical. The 404, a book note, a Knowledge Hub category and an author profile were checked separately for fatals and icon counts, since the snapshot did not cover them.

## 3. Item 3: the three glyphs with no caller

All three were found, and **the S053 dump was wrong on two of them.**

| Glyph | Verdict | Where |
|---|---|---|
| `compass` | **Has a caller.** Not the country panel, as suspected: the 404 page's About door, `404.php` line 81, passed positionally in the doors array rather than as `'icon' =>`, which is why a name-based search missed it. | 404.php |
| `home` | **Has 16 callers**, the most-called glyph after ChevronRight. Every page's breadcrumb home mark now comes through the registry. Before this sweep those were hand-written, which is why the dump found none. | every page |
| `sprout` | **Has one caller**, the code of ethics page's Code of Character and Conduct bar. | code-of-ethics.php |

Nothing was removed, as the bounds require. The lesson worth keeping is the one the globe already taught: a caller search that reads names finds nothing when the call site pastes a drawing instead.

## 4. Item 4: CircleCheck against Check

Measured this turn. **No consolidation made.**

| Glyph | Callers | Where, and what it means there |
|---|---|---|
| `circle-check` | 1 | The routes-grid row "What Achology Membership Includes", `shared-parts.php`. A tick inside a circle, at row-icon size in a tinted container. |
| `check` | 3 | The two Reviews control-bar dropdowns, as the selected-option tick (`page-reviews.php`), and the Book Note hero's Achology rating, repeated once per rating rank (`single-book_note.php`). |

**The facts that bear on Kain's ruling.** They are not competing for one job: `circle-check` is a row mark inside an icon container, and `check` is a tick drawn inside a control or beside a rating. One is signage, the other is state. They also sit at different sizes and never appear on the same page. My read, offered rather than applied: they are two marks with two meanings and the one-mark-one-meaning rule is already satisfied. The ruling is Kain's.

## 5. What is left inline, and why

**Ten drift pairs.** Each is a drawing already in the registry under a different, older release of the same Lucide icon. Consolidating means changing a drawing on a page Kain approved, which the bounds forbid, so all ten stay inline and are reported:

| Where | The mark | The registered counterpart it differs from |
|---|---|---|
| `header.php` line 190, `single-article.php` line 168 | Newspaper, older release | `newspaper` |
| `header.php` line 208 | FilePen, older release | `file-pen` |
| `single-article.php` line 172 | Compass, the polygon version | `compass` |
| `single-article.php` line 329 | GraduationCap, older release | `graduation-cap` |
| `courses-setup.php` line 498, `faq-icons.php` line 53 | Star, the polygon version | `star` |
| `shared-parts.php` line 857 | a play triangle at different coordinates | `achology_icon_play()` |
| `faq-icons.php` lines 73 and 117 | the generated FAQ category set | its own registry |

**`faq-icons.php` is a second icon registry**, generated from DSRD 7 section 5.2's FAQ category table, with its own emitter. It is not drift and it should probably stay separate, but two registries in one theme is worth Chat's eye rather than mine.

**Two string-concatenation call sites** stay inline: `single-article.php` line 169 and `template-our-people.php` line 31. Both sit inside a PHP expression where a wrong rewrite is a fatal rather than a wrong glyph, so they were left for hand work rather than swept by script.

## 6. The build sheet export

Reported separately at the end of this session's work, with an honest statement of whether it was reached. It is a document that becomes the standard the theme is corrected against, so a thin one is worse than none.

## 7. What I need back

1. **Kain's eye on the manifesto pair panel**, which now shows GraduationCap twice.
2. **Kain's ruling on CircleCheck against Check**, with section 4's facts in front of him.
3. **Chat's view on `faq-icons.php` being a second registry**, and on whether the ten drift pairs are consolidated or recorded as deliberate.
4. **DSRD 7 section 5.2 needs rewriting against this sweep**, as the S261 request already anticipated. The registry is 49 glyphs and section 5.2 does not yet know about most of them.

*No em or en dashes in this file; checked before writing.*
