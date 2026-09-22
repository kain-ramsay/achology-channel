# SESSION REPORT: S128

**Claude Code, theme session, Tuesday 22 September 2026.**
**Theme v0.620.0 at the open, v0.639.0 at the close, deployed and pushed.**

Assembled from the version control log, per Harness Rule 13. Hand-added lines are marked.

## Finished

**Board card: Pricing page.**

- **The page's schema is built.** `WebPage`, an `OfferCatalog` of 38 `Offer` nodes and `BreadcrumbList`, to DSRD 10 §9's row. It carried none before. Both DSRD 6 §4 checkers clean. §4 is now `pass` in the record. v0.621.0. Detail in `ASK__The_Pricing_Pages_Schema_Is_Built_And_Two_Things_It_Left_Open_S128.md`.
- **The accessibility chapter's machine half is clean.** Re-run on Kain's instruction, found still failing after the S127 repair, put to him, and cleared. v0.622.0 to v0.625.0. Detail in `RULING__Kain_Takes_The_AA_Safe_Orange_Into_The_Pricing_Pages_Last_Three_Controls_S128.md`.
- **The site gained a control orange, `--color-orange-action` #C85015,** chosen by Kain from four rendered options. It reaches every primary button on every page. Same RULING file.
- **The lighter grey is off every light ground site-wide.** 40 elements measured across 20 built pages, 36 failing, all repaired. Reaches the help desk front page and the theme's cards. v0.626.0.
- **The school cards open on the reader's choice,** all eight, reversing Kain's own S123 instruction on a new argument of his. v0.628.0 to v0.633.0. Detail in `RULING__Kain_Opens_The_School_Cards_On_The_Readers_Choice_S128.md`.
- **Four membership benefit lines removed,** on his instruction and his ruling that this is a pricing page and not a sales page. v0.633.0. Same RULING file.
- **The page's rhythm corrected twice:** a separator that was being drawn where nobody could see it, and one junction where Kain ruled the line off and the air with it. v0.635.0 to v0.637.0.
- **The pricing stylesheet's dead rules swept.** 60 of 265 selectors matched nothing; all removed except the 23 belonging to the parked Access All Areas renderer. 691 elements measured before and after: none moved. v0.639.0.

## Not finished, and what remains

- **The pricing page's DSRD 6 record is not closed.** §4 passes and §7's machine half is clean. §2, §3 and §5 fail; §1, §6, §7's hand half, §8, §9, §10 and §11 have not run. It is reported as "built, gate open", never as done.
- **The page has no search title, description or focus keyword, so Rank Math has never scored it.** This is the only thing Code is blocked on. Asked for in `ASK__The_Pricing_Page_Cannot_Be_Scored_Until_It_Has_A_Search_Description_S128.md`.

## Filed to TO Chat this session

`ASK__The_Pricing_Pages_Schema_Is_Built_And_Two_Things_It_Left_Open_S128.md`, `RULING__Kain_Takes_The_AA_Safe_Orange_Into_The_Pricing_Pages_Last_Three_Controls_S128.md`, `RULING__Kain_Opens_The_School_Cards_On_The_Readers_Choice_S128.md`, `ASK__The_Pricing_Page_Cannot_Be_Scored_Until_It_Has_A_Search_Description_S128.md`, and this report.

## Added to the theme queue

One line: `help.css` is downloaded twice on every page that renders a help component, because a site-wide enqueue and a component enqueue use different handles for the same file.

## Three things Chat is owed that are bigger than this page

1. **DSRD 7 contradicts itself on the resting colour of a text link.** Its colour section puts body links on the AA-safe orange because brand orange "fails AA below large-text size"; its S263 ruling has every link rest in brand orange site-wide. Both cannot hold, and the second makes every resting body link on the site fail DSRD 6 §7.
2. **DSRD 6 §7's machine half cannot see a hover, focus or active state at all.** Three failing hover states were found this session by a person reading a stylesheet, every one on a page whose scan had just come back clean. The chapter nowhere says the scan is blind to them, so a clean §7 line reads as more than it is.
3. **The filed S123 ruling and the live page disagree about the course index.** The ruling says all 28 with no expand control and names "eight rows then View all 28" among the options that lost; the page shows nine rows and that control.

## One claim checked and found untrue

Chat reported that Code's channel pull had been failing since 18:23 on 21 September. It has not. Both machines' watchers wrote a heartbeat every ten minutes without a break across that whole period, including 31 and 34 beats respectively between midnight and 08:00 on the 22nd; a live fetch this evening succeeded; local is level with origin in both directions; and both status files written minutes ago read "Channel and origin agree". The read path also demonstrably worked today, since the inbox wall stopped this session mid-job the moment Chat's S375 brief landed. Nothing was changed. **Hand-added line.** What may be true underneath it: FROM Chat holds 105 live files, and from Chat's side "Code is not pulling" and "Code is not acting on what I send" look the same.

*No em or en dashes in this file; checked before writing.*
