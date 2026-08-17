> **ARCHIVED, Session 268, 12 August 2026.** Read, and the finding is accepted rather than argued with: neither question was a matter of taste once the markup and the stylesheets were read, so neither costs Kain a sitting. Written onto **The Component Truth System** card in full, with the two registry consequences named as work still to apply: the three breadcrumb rows describe one library component and should carry one prototype and one build sheet between them, which moves the count of 78, and the misleading wrapper name is recorded rather than renamed. No render is requested.

# REPORT: both render questions answer themselves in the markup. Neither needs Kain's eye

**DOCUMENT TYPE:** not a page spec.
**From:** Claude Code, Session 055. **Date:** 2026-08-12.
**Answers:** `RULING__Seventeen_Site_Wide_Families_Are_Library_Components_S267.md`, the two renders.

I went to build both renders and found that both questions have factual answers, checked on the delivered markup and the stylesheets rather than judged by eye. **Neither is a matter of taste, so neither should cost Kain a sitting.** Renders are still available if he wants to look; they would confirm rather than decide.

## Render one: there are not two breadcrumbs. There is one, in two parts

**`policy-breadcrumb` is the `<nav>` wrapper. `breadcrumb` is the `<ol>` inside it.**

```html
<nav class="policy-breadcrumb" aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb__item">...
```

**Checked on the delivered markup of four live pages**, not in the source, because the rendered page is what a visitor meets:

| Page | `<nav class="policy-breadcrumb">` | `<ol class="breadcrumb">` nested inside it |
|---|---|---|
| `/about/` | present | **yes** |
| `/reviews/` | present | **yes** |
| `/policies/privacy-policy/` | present | **yes** |
| `/help/` | present | **yes** |

And in the source, **the same thirteen templates emit both**, never one without the other. That is the tell: two competing components would appear on different pages, not on identical sets of pages in a fixed parent-and-child relationship.

**So the census counted one component twice**, because it counts class prefixes and this component has two. That is a limitation of counting prefixes and not a fault in the theme.

**What this leaves for Kain, and it is smaller and different from what was asked.** Not "are these one thing or two", which is settled, but **the wrapper is called `policy-breadcrumb` while it renders on thirteen templates, most of which are not policy pages.** The name is a leftover from where the block was first built. Renaming it is a thirteen-template change for tidiness alone and I am not proposing it; recording it as one component with a misleading wrapper name costs nothing and loses nothing.

**Registry consequence:** `breadcrumb`, `policy-breadcrumb` and `icon-breadcrumb` are three rows describing **one** library component. They should carry one prototype and one build sheet between them, not three.

## Render two: the Where Next panel has not drifted. Zero conflicts

`policy-next` is declared in five stylesheets, which was the strongest case in the census for duplication. **It is not duplication.**

I extracted every `policy-next` rule from all sixteen stylesheets and compared them property by property:

| Stylesheet | Rules | Distinct selectors |
|---|---|---|
| **components.css** | **49** | **46** |
| help.css | 6 | 4 |
| book-note.css | 2 | 2 |
| about.css | 1 | 1 |
| footer.css | 1 | 1 |

**Same selector declaring the same property with a different value, anywhere: zero.**
**Same selector declaring the same property with the same value, anywhere: zero.**

There is no drift and not even a redundant duplicate. The component lives in components.css, and the other four files add page-specific selectors that components.css does not contain at all:

- **about.css**, one rule: `.pfq + .policy-next--pair { margin-top: 0; }`, a spacing fix where the panel follows the FAQ block.
- **footer.css**, one rule: `.footer-col__head .policy-next__accent { color: inherit; }`, the orange accent standing down inside a footer heading.
- **book-note.css**, two rules: the panel inside the book note separator and page.
- **help.css**, six rules: the `--bubble` variant and its no-mark modifier.

**So it is one component with four small, non-overlapping extensions**, which is untidy rather than wrong. Whether the four move into components.css is a housekeeping call, not a design one, and it changes nothing a visitor sees.

**Registry consequence:** `policy-next` is one library component with one home. The five-stylesheet count in the census is a true fact that means something different from what it looked like.

## Why I am reporting this instead of building the renders

Chat's own words: both questions "turn on whether the things actually look the same, which is a question for his eye on rendered examples, not for either of us in words". **That was right when the only evidence was a census count.** With the markup and the stylesheets read, neither question turns on appearance any more:

- The breadcrumb question is settled by nesting, which is structure and not appearance.
- The Where Next question is settled by there being no conflicting declaration to see. Two panels that differ would render differently; **there is nothing that could render differently.**

Putting a render in front of Kain now would be asking him to look at two things that are provably the same thing and confirm they look the same. That costs his attention and buys a conclusion I already hold with better evidence than eyes give.

**If either of you disagrees, say so and I will build both renders in one pass.** They are half an hour, the pages are live, and I would rather build them than have this read as me deciding something that was his.

## One thing genuinely unresolved, and it is small

`/learn/` returns a 302 rather than a page, so it carries no breadcrumb to check. That is why the fifth page in my table is missing. It is a routing fact about the listing URL and not a breadcrumb finding; I have not chased it because nothing in this question depends on it.

*No em or en dashes in this file; checked before writing.*
