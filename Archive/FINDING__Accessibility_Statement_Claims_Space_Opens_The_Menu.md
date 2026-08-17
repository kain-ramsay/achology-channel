# FINDING: the Accessibility Statement says the menus open with Enter or Space. Space does not open them

**From:** Claude Code, S047. **Date:** 2026-08-05. **Theme:** v0.38.18.
**Found on:** page 7 of the S047 walk, https://achologytest.com/policies/accessibility-statement/
**Needs:** a decision on which of two honest fixes to take. Both are small; they are not equivalent.

## The claim

Quoted from the live page, section 3:

> "**Full keyboard access.** Site navigation, including dropdown menus, can be operated entirely by keyboard: menus open and close with Enter or Space, Tab moves through the links, and Escape closes a menu and returns focus to where you were."

## What I tested, and how

I drove the real page with real key presses rather than reading the code, and I confirmed the result on screen as well as in the DOM, because a probe misled me once during this same page's pass and I do not want to file another wrong finding.

| Claim | Result |
|---|---|
| Enter opens the menu | **True.** Focus on the Academy trigger, Enter pressed: `aria-expanded` goes false to true, the Academy panel becomes `visibility: visible` at `opacity: 1`, its 7 links become reachable, and the page does not navigate away despite the trigger carrying `href="/academy/"`. Confirmed on screen. |
| Escape closes it and returns focus | **True, exactly as written.** Escape pressed: every menu returns to hidden, `aria-expanded` returns to false, the menu's links drop out of the tab order (0 reachable), and `document.activeElement` is the trigger itself, not the body. This is the strong form of the behaviour, and it is correct. |
| Tab moves through the links | **True.** All 7 panel links reachable while open, none reachable while closed. |
| **Space opens the menu** | **False.** Focus on the trigger, scroll reset to 0, Space pressed: the menu stays closed. Verified in the DOM and then confirmed by screenshot, which shows the trigger focused with its chevron down and no panel. |
| Visible focus outline | **True.** 2px outline in brand orange #ED6922 on the focused trigger, keyboard only. |

## Why Space behaves this way, which decides the fix

The triggers are anchors: `<a href="/academy/" aria-haspopup="true" aria-expanded="false">`. On a link, Enter activates and Space is the browser's page-scroll key. Space not opening the menu is therefore **native, conventional link behaviour**, not a bug someone introduced. The code is doing the ordinary thing; the sentence describes something else.

That matters, because it means the cheap fix and the correct fix point in different directions.

## The two honest fixes

1. **Correct the sentence.** Remove "or Space" so the page describes what the control does. One word, no code, no risk. It leaves the control as a link that also opens a menu, which is a slightly unusual pattern but a working and keyboard-operable one.

2. **Change the control to a button and make Space work.** A control whose job is opening a disclosure is conventionally a `button`, and on a button both Enter and Space activate, which is what a keyboard user is taught to expect. This makes the sentence true rather than making it narrower. It is a real change to the header on every page, it would need its own signed brief under Rule 3, and it interacts with the fact that these triggers also carry a real destination URL that a mouse user can click through to.

**I am not choosing.** Option 1 is Chat's copy work; option 2 is a chrome change that touches every page and needs Kain. My own view, offered and not acted on: the sentence is the thing that is wrong today, so option 1 closes the honesty gap immediately, and option 2 is a separate and larger question about whether the nav triggers should be links at all, which belongs with the mega menu and footer design session that is already scheduled.

## One thing worth saying plainly in the statement's favour

Three of the four keyboard claims on that page are true, and the Escape behaviour is better than most sites manage: it closes the menu, restores `aria-expanded`, seals the panel links out of the tab order, and puts focus back on the trigger. Section 4 of the same page is also exemplary, and it is why this finding is small rather than serious: the page explicitly declines to claim conformance until an assessment is done. It says "we do not claim full conformance". A page that had overclaimed would be in a much worse position than this one is.

*No em or en dashes in this file; checked before writing.*
