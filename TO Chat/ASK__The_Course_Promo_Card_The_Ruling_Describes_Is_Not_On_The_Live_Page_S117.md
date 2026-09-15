# ASK: the course promo card the ruling describes is not on the live page

**Filed by Claude Code, Session 117. Date:** 15 September 2026.
**Answers:** `RULING__Article_Page_Course_Promo_Image_Runs_Full_Width_At_Tablet_And_Phone_S361.md`.

---

Checked the named page directly, live: `https://achologytest.com/learn/helping-people/articles/why-giving-advice-does-not-work/`. Searched its rendered DOM for the exact wording the ruling names.

**"Explore This Course" appears nowhere on the page.** The only element carrying the "Know Your Psychology" artwork is a plain linked image, no course name, no blurb, no button, in two places: the side rail (`.kh-aside__course`) and the narrow-width foot (`.kh-foot__kyp`). Neither is a course promo card.

**There is a card matching that exact description in the theme, but it never renders.** `achology_article_promo_card()` in `knowledge-hub-parts.php` builds precisely what the ruling names, dark card, DiMAP artwork, course name, blurb, "Explore This Course" button, class `.kh-promo`. It has zero call sites anywhere in the theme. Its own comment records why: Kain cut this exact card from the article page at S112, on purpose, and the code was deliberately left standing rather than deleted in case he wanted it back. Confirmed again this session while sweeping for dead code, S117.

So either Kain was looking at a different page than the one named, or at a mockup rather than the live build, or he is asking for the S112 cut to be reversed and this card brought back before the width fix can apply to it. Not guessing which; the width change itself is a two line CSS fix once I know where it goes.

---

OWED BACK: which page or surface Kain actually had open in Safari, or confirmation that S112's cut is reversed and this card comes back first.

*No em or en dashes in this file; checked before writing.*
