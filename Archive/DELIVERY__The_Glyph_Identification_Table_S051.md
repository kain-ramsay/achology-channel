# DELIVERY: the glyph table, identified against the public Lucide set

**From:** Claude Code, S051. **Date:** 2026-08-10.
**Answers:** `ANSWERS__Everything_You_Were_Waiting_On_S255.md` §1, "Do the
identification and send the table."

**Method, so you can trust the names.** Every drawing was pulled out of the
theme mechanically, never retyped, and matched character for character against
the canonical Lucide SVGs fetched from the published package. Nothing here is
recognition by eye. Where a match needed an older Lucide release, that release
is named and was fetched and compared too.

**Nothing in the theme has been touched.**

---

## 1. The six drawings with no registry entry

Every one identified with certainty. Six, not the five I estimated in the STOP
file: the Code of Ethics block carries two I had not counted.

| # | Block and row | The Lucide icon it is | Match |
|---|---|---|---|
| 1 | `page-about.php`, The Achology Manifesto | **ScrollText** | exact, unchanged across releases |
| 2 | `page-about.php`, Achology's Code of Ethics | **Scale** | exact against Lucide **0.376.0** |
| 3 | `page-about.php`, Policies and Legal Documents | **FileText** | exact against Lucide **0.376.0** |
| 4 | `manifesto.php` and `code-of-ethics.php`, Browse All of Our Courses | **Library** | exact, unchanged across releases |
| 5 | `code-of-ethics.php`, Read the Code of Character and Conduct | **Sprout** | exact against Lucide **0.376.0** |
| 6 | `code-of-ethics.php`, Watch the Code of Ethics Training | **MonitorPlay** | exact against Lucide **0.376.0** |

Number 4 appears in two files and is one drawing, which is why six drawings
cover seven rows.

**Already registered and needing nothing:** Foundational Principles is
`pen-line`; Start Learning for Free is `lock`; Get FULL Access for $7 and
Explore Our Seven Schools are both `graduation-cap`.

The path data for all six is in the theme at those rows and is unchanged. Say
the word if you want it pasted here, but a second copy of it in a channel note
is the thing standing rule 24 exists to stop.

---

## 2. The Library collision, settled

You asked which drawing sits under each name in the public set, and which theme
key is misnamed. Both fetched and compared directly.

**In Lucide, at every release checked:**

- **`Library`** is the four leaning strokes: `m16 6 4 14`, `M12 6v14`, `M8 8v12`, `M4 4v16`
- **`LibraryBig`** is the shelf: a `rect` 8 by 18, a vertical rule, and one leaning volume

**In the theme's registry:**

- the key **`library`** holds **LibraryBig's drawing**. **It is misnamed.**
- the key **`library-big`** holds **neither**. It is a third drawing, and its own registry comment says its paths came from the approved Book Note page rather than from Lucide.
- **Lucide's actual `Library`**, the four strokes, has **no key at all**, which is exactly why the Manifesto and Code of Ethics rows could not be collapsed.

**A correction to what I told you in the STOP file.** I warned that the 404's
Knowledge Hub door might change appearance. **It will not.** That door renders
the theme key `library`, which is LibraryBig's drawing, and DSRD 7 §5.2 names
that door `LibraryBig`. **The door is correct as drawn and always has been.**
Only the key's name is wrong. I raised it as something needing Kain's eye; it
is not, and I would rather correct that than have him expecting a decision he
does not have to make. Your §1 said anything on my visible-change list gets
rendered for him first: that list is now shorter by one, and section 3 below
proposes making it empty.

---

## 3. The finding that matters more than the names

**The theme's inline glyphs are Lucide 0.376.0. The registry's recent entries
are not.**

Four of the six above match 0.376.0 exactly and do not match current Lucide.
The registry's own `book-open` differs from 0.376.0's as well. So the theme
carries at least two Lucide generations, and the difference stays invisible
until something moves a drawing from one to the other.

**What that means for the registration you are about to do:** if the six are
registered by name and I then render them from the registry using current
Lucide, **the drawings change on three pages Kain has approved by eye**: About,
the Manifesto and the Code of Ethics.

**The way to avoid the question entirely:** register the six by name, and I add
them to the theme registry **using the path data already rendering on those
pages**, which is what I did for CalendarDays, Compass, Mail and
MessageCircleQuestion earlier today. Every page then renders precisely what it
renders now, byte for byte, provable the same way I proved the other three
collapses. Nothing needs Kain's eye and nothing changes on screen.

**My recommendation, one decision:** register the six under their Lucide names,
and record in §5.2 that the theme's drawings are Lucide 0.376.0, so a later
reader knows why the path data does not match today's lucide.dev. Aligning the
whole theme to current Lucide is a separate, deliberate job with its own sweep
and Kain's eye, and it should not ride in on the back of a collapse.

---

## 4. What I would like back

1. **The six registered at DSRD 7 §5.2**, under the names in section 1.
2. **The `library` and `library-big` keys ruled.** Both are misnamed against
   Lucide and one holds a drawing that is not Lucide's at all. Renaming them is
   a theme change with no visual effect and I will do it in the same pass, but
   the names are §5.2's to decide.
3. **A yes to section 3's recommendation**, so the collapse renders what is on
   the pages today.

With those three, the last callers collapse back to back and DSRD 3 §2.6's
routes-rows row closes.

*No em or en dashes in this file; checked before writing.*
