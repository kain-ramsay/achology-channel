# RULING: the label above the page title goes wherever it repeats the breadcrumb

**Ruled by:** Kain, in session, Session 080, 24 August 2026.
**Where:** Safari, on the tabbed comparison at `previews/overline-repeat-options.html`, three page families on one sheet, each with its real breadcrumb above it. Only that one line differed between the panels.
**His words:** "yes, please remove the repeat"
**Shipped in theme v0.83.0**, deployed and verified on all four live pages.

---

## What he saw

He was looking at a help answer and said it plainly: "we actually have a double breadcrumb. We've got the breadcrumbs, and then we have the category sitting above the actual question."

He was right, and it was wider than the help page. Measured on the live pages:

| Page | The trail says | The line above the title said |
|---|---|---|
| Help answer | Help > **About Achology: Our Identity** > What is Achology? | **About Achology: Our Identity** |
| Policy page | **Policies** > Privacy Policy | **Policies** |
| Knowledge Hub article | Learn > **Helping People** > Articles > Why People Seek Help | **Helping People** |

The same word twice, a few centimetres apart, on three of the site's four main page families.

## The rule he settled

**A label above the title that repeats a word already in the trail above it earns nothing and costs a line. It stays only where it says something the trail does not.**

It is the same principle as DSRD 8 §11.0, which he ruled for the commerce cards at S279: the small line above a product's name names the parent and never repeats the heading below it. Here the parent is already named, in the breadcrumb.

**404.php keeps its overline and is untouched**, because "Find your way" is not a repeat of anything. That is the test.

## What changed in the theme

Three templates, one line each: `single-faq_article.php`, `template-policy.php`, `single-article.php`. Each carries a comment recording the ruling and the reasoning in place.

**The category is not lost to the reader on the article page:** the breadcrumb links to it, which is the same destination the pill carried.

## What this supersedes, named rather than smuggled

**DSRD 9 §22.4** specifies the category pill with its full anatomy: font, transform, letter-spacing, colours, padding, radius and link. That row goes.

**`SIGNED_SPEC__The_Individual_Article_Page_S302`**, which Kain signed hours earlier the same day, lists the pill in block 3 as "Hero: category pill, H1, meta line". **His later ruling governs**, and I am flagging it rather than letting you find the two documents disagreeing.

**The help and policy equivalents** need the same treatment wherever their overlines are specified.

## One thing I did NOT do

**I did not touch the three help pages' extra spacing**, which was the question in front of us when he spotted this. Two of the three are genuine drift and he has approved bringing them into line; the third, the help article's 56px, turns out to be a value he ruled himself, splitting the difference between 48 and 64, and it is recorded as locked in `help.css`. I stopped rather than overwrite his own ruling on a general instruction, and that question is still open with him.

*No em or en dashes in this file; checked before writing.*
