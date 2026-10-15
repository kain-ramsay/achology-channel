> Code: the pulsing Know Your Psychology logo under the contents glitches because fit() in knowledge-hub.js tears its class off and puts it back on every load and resize, which kills the two ripples and restarts them mid-pulse. One small JS fix below; no visual change, so no options sitting. Kain asked for this.

# BRIEF: the logo ripple restarts (Chat, S428, Thursday 15 October 2026)

**Where:** `knowledge-hub.js`, section 4, the `fit` function (about line 816), and the ripple in `kh-band.css` (about lines 489 to 523). Theme folder as it stands tonight.

**What Chat found, on the build site in Playwright at 1440 by 860 (10 Ethically Dubious Experiments and Freud's Defence Mechanisms):**
1. `fit()` begins with `aside.classList.remove('kh-aside--nofit', 'kh-aside--kyp')`, then reads `contents.offsetHeight`. That read forces a style pass with the logo's class gone, so the browser cancels both ripple animations; the class goes back on and two new animations start from nothing.
2. `fit()` runs on `load` and on every `resize`. Measured with `document.getAnimations()`: the ripple pair is replaced at the `load` event (new start time 16 ms after load) and again on a single resize event (current time 88,295 ms before, 184 ms after). On Kain's machine the load event lands after the pictures arrive, so the rings vanish part way through a pulse and start again small: the glitch. Dragging the window, zooming or opening a sidebar restarts it on every resize tick.
3. Scrolling does not restart it: section 0b's `settle()` runs 150 ms after every scroll stop and rewrites the aside's class and style ten times, but it never touches `kh-aside--kyp`. Leave `settle()` alone.

**The fix:**
1. In `fit()`, stop removing the two classes at the top. Work out the answer with the classes where they are (the measurement uses fixed numbers for the picture, `216 + 24` or `357`, and the logo sits after the contents, so neither class changes `contents.offsetHeight`, `hidden` or `panel.clientHeight`), then set each with `classList.toggle(name, answer)`. When the answer is unchanged nothing is written, so nothing restarts.
2. Run `fit()` on resize only when `innerWidth` or `innerHeight` has changed since the last run, once per animation frame.
3. Keep `fit()` on load (fonts and pictures can change the contents' height); with fix 1 it only restarts the ripple when the logo really appears or goes.

**Done when:** on an article where the logo shows, `document.getAnimations()` returns the same two `kh-kyp-ripple` animations before and after the load event and after a resize that does not cross the fit line; the logo still appears and goes where it fits and where it does not (Kain S166 rule unchanged); the production JS test passes; checked in Safari and Chrome on Kain's iMac size.

**Not in this fix:** the ripple's look (size, colour, timing) is Kain's S166 design and stays as it is.

OWED BACK: one DONE with the before and after animation readings.

*No em or en dashes in this file; checked before writing.*
