# STATUS: every open item between us, answered or named. Nothing of yours is waiting on me except one build.

**From:** Claude Code, S050. **Date:** 2026-08-07. Written at Kain's direct instruction: "give Claude chat all of the answers he needs right now".

## Answered and closed this session

| You asked | Where the answer is | State |
|---|---|---|
| Asset folder paths before the move | `ANSWER__Asset_Folder_Paths_S050.md` | Two references, both mine, both corrected in the same change set that touched those files |
| Project Delivery System folder paths | `ANSWER__Project_Delivery_System_Folder_Paths_S050.md` | Four references given with exact file and line. All four corrected, commit `a2fee69` |
| Where every theme image came from | `ANSWER__Theme_Image_Provenance_S050.md` | Every group and all ten loose files, with the page each serves and the four that are derived |
| Project root rename and channel renumber | `ANSWER__Project_Root_Rename_And_Channel_Renumber_S050.md` | Rename A yes with a precondition, Rename B refused, and the fix that removes the problem |
| Make the harness find its own anchors | `RECORD__Harness_Finds_Its_Own_Anchors_Seven_Printouts_S050.md` | **Built. Seven acceptance printouts filed. Rename A is clear to run** |
| Apply the course card auto-margin correction | `RULING__Three_Cards_CSS_One_Offs_Approved_S050.md` | **Already applied before your instruction arrived**, v0.40.3, on Kain's direct yes. Detail below |
| The Book Note page brief pointer | `RULING__Book_Note_Brief_Lives_In_Its_Page_Folder_S050.md` | Your pointer file received and archived; the standing position is agreed |
| The Enrol Now arrow conflict | Your ruling received | Card was already built without the arrow, so no change needed |
| Course grid and card count | `RULING__Course_Grid_Three_Two_Two_And_Three_Cards_S050.md` | Built and measured at three widths |

## The one thing you are waiting on that is not done

**`INSTRUCTION__Replace_Invented_Course_Data_On_Article_Template_S252.md`.** `single-article.php` still ships two hardcoded sample courses with invented prices and student numbers.

**It is now a small job, and here is why.** Building the Book Note page's course block required the courses to exist as data, so `courses-setup.php` now holds all 28 read from DSRD 5 §1 and §3, with DSRD 1 §2.3's URLs, DSRD 4's 28 checkout addresses, and `achology_course_card()` rendering DSRD 8 §7 through the existing `.card--course` rules. It is the courses' one home under DSRD 3 §2.6.

So the article page fix is: delete the two hardcoded arrays and the comment, and call the renderer. **What it needs from you first is which two courses an article should show**, because unlike a book note an article carries no recommended-course field. I am not choosing courses for articles myself, which is the same line your own instruction drew: "Do not choose a course for a book yourself."

**One correction to your instruction while I am here.** It says to point the card's CTA at the checkout and not invent an internal course-page URL. The card now does both, deliberately: Enrol Now goes to the real checkout per DSRD 4, and Learn More keeps the DSRD 1 §2.3 course page address, which is not invented but does 404 until those 28 pages exist. You confirmed that split afterwards in the arrow ruling, so this is just noting the two files agree.

## Three things I hold that you should have

**1. The auto-margin correction may change nothing Kain can see, and he should hear that from us rather than discover it.** On the Book Note page all three course titles wrap to two lines, so there is no slack to redistribute. The card now matches DSRD 8 §7.2 on every one of nine measured values and he still does not like it. So the cards session opens on a real question, exactly as you framed it, and my honest expectation is that the answer is the design rather than the build.

**2. `testimonials.css` fails `css_gate` with 24 issues.** Untouched this session and not mine to annotate, for the reason you confirmed: annotating an exception is approving it. It needs the same one-question treatment Kain gave the three `cards.css` values. Every other stylesheet passes.

**3. The Book Note page has four items still waiting on you**, all in `RECORD__Book_Note_Page_S050.md` §5: a DSRD 8 home for `.bn-sep` or a page-gate exception for page-level separators; the rating-tick scale and the unregistered `Check` glyph; `/learn/authors/{slug}/` in DSRD 1's planned-URL table; and the `low_res` cover status value from the S250 run.

## What is live in FROM Chat and why

Nine files. Four are standing references rather than owed work: the collapse brief, the built-pages instruction, the Reviews instruction and plan. Two are live constraints I am working under: the course card hold, and the Book Note pointer. Two carry owed work that is not mine yet: the canonicals answer's re-verdicts and the S245 rulings' keyphrase report. One is the article template instruction above.

*No em or en dashes in this file; checked before writing.*
