# REPORT: seven theme versions shipped at S097, all from a factory session on Kain's word

**From:** Claude Code, Session 097. **Date:** 3 September 2026. **Session type:** factory.
**Under:** Harness Version 3.12, which makes a theme edit in a factory session legitimate where Kain rules it in the sitting and obliges the ruling to be named in the report and the commit. Every one below carries his word.
**Board cards:** the Our People page card; the harness card.

---

## What shipped

| Version | What changed | Kain's word |
|---|---|---|
| 0.141.0 | The hairline above the closing enquiries panel returns. `.policy-closing` moved from `about.css` to `warm-room.css`, finishing the S083 move that left it behind | *"please go ahead"* |
| 0.142.0 | The profile page's bio gets paragraph spacing and the 880 reading column. It had no paragraph margins at all | *"Yes, fix those two now"* |
| 0.143.0 | The profile page's writing section joins the same column | *"Fix the dividing line and spacing next please"* |
| 0.144.0 | That column is centred rather than pinned left | *"they are the correct width, but you have left aligned them on the page"* |
| 0.145.0 | The breadcrumb and hero join it, so the whole profile page shares one edge | *"bring them in so the whole page shares one edge please"* |
| 0.146.0 | The Our People hero paragraph takes new copy | his words, pasted |
| 0.147.0 | The same paragraph takes a revised pass of that copy | his words, pasted |

Every one deployed, cache purged, and all three deploy proofs green. `css_gate` green on each of the five that touched CSS.

## The two paragraphs, for the record, since this is page copy

**Before tonight:** "Behind every Achology project is a team of experts. Driven by a commitment to personal and professional growth, our instructors, eldership, and editorial team handle all teachings, events, and publications. They ensure the accuracy of content, provide insightful training, and uphold our quality standards at all times."

**Now:** "All Achology projects are led by a team of specialists dedicated to personal and professional development. Our instructors, eldership, and editorial team oversee all teachings, events, and publications, ensuring accuracy, delivering valuable training, and upholding consistent quality standards."

Three sentences to two, 49 words to 38. It lives in `template-our-people.php` rather than in a record, so it is named here in full rather than pointed at.

## Three corrections made to my own findings while doing this, all named where they happened

**The dividing line was never too wide.** It matched its own list exactly; it only looked wrong after I narrowed the bio. The real fault was the section sitting outside the site's reading column.

**The spacing was never uneven.** A heading belongs closer to the list it introduces than to what precedes it, so 56 above and 24 below was right. Only the 56 was wrong, because it is not the house value. My pre-sitting list had called it a fault and it was not.

**A max-width does not centre anything.** Capping the column and leaving it pinned left was my omission, and Kain caught it by eye within a minute of it shipping.

## Two things checked before changing them, because both could have reached pages nobody asked about

`.ap-crumb` is also the Our People hub's breadcrumb, so the new rule is scoped by `.ap-page`, which the profile carries and the hub does not. And the hero's watermark is positioned against the viewport rather than its block, so narrowing the hero left it exactly where it was; measured afterwards at the same offset rather than assumed.

## The hub needed nothing

Checked block by block at Kain's request after the profile pages were done: the breadcrumb, header, all four team groups and the closing panel already sit at one edge, centred. The one wider band is the tinted instructors panel, which steps out by exactly its own padding so its contents still land on that edge. That is the documented pattern and pulling it in would indent the words inside it.

---

OWED BACK: nothing. The remaining Our People items are on the pre-sitting list and the theme queue.

*No em or en dashes in this file; checked before writing.*
