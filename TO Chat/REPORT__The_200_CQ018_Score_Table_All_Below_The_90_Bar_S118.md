# REPORT: the 200 CQ018 pages, all scored, all below the 90 bar

**Filed by Claude Code, Session 118. Date:** 15 September 2026.
**Answers:** `BRIEF__Import_And_Score_All_200_CQ018_Quote_Pages_Publish_On_Kains_Word_Only_S360.md`, per Chat's NOTE this session to run it now.

---

## 1. Import, confirmed

200 of 200 `CQ018-*.md` records passed `content_gate.py quote-page` at the front door. Imported as drafts (`import_quote_pages.py --push --only CQ018-`), 200 of 200 verified clean against the install (`--verify`). Nothing refused, nothing published.

## 2. The score, read off every page, in the WordPress editor itself (never estimated)

**Every single page scores below the site's 90 bar.** The distribution is three values only, not a normal scatter: 3 pages at 76, 97 at 80, 100 at 84. Nothing above 84, nothing below 76.

That shape is worth naming plainly: 200 independently-written quotes converging on three near-identical numbers looks like a structural ceiling this content type hits, not 200 individual pieces of weak writing. `content_gate.py`'s own quote-page checks (the Achology-specific band) already passed all 200 clean, so whatever is capping the Rank Math number sits in tests the gate does not check, and I have not yet built the capability to read which named tests Rank Math itself is failing per page (`score_run.py` reads the settled numeric score only, not the per-test breakdown). Naming what I do not know rather than guessing at it.

**The score table, worst first:**

| score | post ID | slug |
|---|---|---|
| 76 | 36369 | why-congruence-gives-us-a-basis-for-trust |
| 76 | 36463 | why-no-single-label-can-define-who-you-are |
| 76 | 36471 | why-no-teacher-can-make-you-learn |
| 80 | 36308 | why-we-take-courses-to-be-challenged-not-soothed |
| 80 | 36310 | why-wanting-what-you-lack-can-lead-to-sadness |
| 80 | 36317 | why-we-must-stay-committed-to-the-process-of-personal-growth |
| 80 | 36318 | why-we-behave-out-of-what-we-believe |
| 80 | 36320 | why-fulfillment-is-better-than-happiness |
| 80 | 36322 | why-the-wisest-response-is-to-consider-and-reflect |
| 80 | 36323 | why-making-no-decision-is-still-a-decision |
| 80 | 36324 | why-you-have-to-let-go-of-what-youre-holding-onto |
| 80 | 36325 | why-theres-a-limit-to-how-much-change-people-can-handle |
| 80 | 36326 | why-people-respond-to-assumptions-not-your-intentions |
| 80 | 36329 | why-saying-yes-or-no-is-determined-by-us |
| 80 | 36331 | why-theres-a-consequence-for-every-action-or-inaction |
| 80 | 36332 | why-we-dont-need-anything-magical-or-mystical-to-transform-our-lives |
| 80 | 36333 | why-people-are-moved-by-fear-or-by-freedom |
| 80 | 36336 | why-we-can-grow-in-intellect-without-growing-in-character |
| 80 | 36337 | why-no-one-intends-to-be-an-emotional-train-wreck |
| 80 | 36340 | why-we-keep-looking-one-level-deeper-than-you-need |
| 80 | 36341 | why-change-is-only-one-new-habit-away |
| 80 | 36342 | why-most-of-your-thoughts-are-not-true |
| 80 | 36347 | why-anxiety-comes-about-when-we-are-scared |
| 80 | 36348 | why-we-are-not-creating-space-for-people-to-grow |
| 80 | 36350 | why-something-being-called-therapy-doesnt-make-it-helpful |
| 80 | 36351 | why-applying-what-you-learn-is-what-learning-means |
| 80 | 36353 | why-once-a-mind-has-been-truly-expanded-it-never-goes-back |
| 80 | 36356 | why-hard-times-make-us-push-ourselves-and-grow |
| 80 | 36359 | why-mistakes-are-not-the-most-effective-way |
| 80 | 36360 | why-we-dont-know-we-have-a-choice |
| 80 | 36363 | why-every-emotion-is-triggered-by-a-thought |
| 80 | 36365 | why-the-pattern-of-thinking-determines-our-emotional-state |
| 80 | 36366 | why-we-wont-experience-yesterday-again-tomorrow |
| 80 | 36367 | why-the-caliber-of-the-relationships-we-build-is-a-choice |
| 80 | 36376 | why-i-cant-do-this-is-usually-just-a-choice |
| 80 | 36377 | why-people-determine-the-rules-that-they-live-by |
| 80 | 36384 | why-your-own-future-results-depend-on-your-choices |
| 80 | 36386 | why-self-acceptance-has-got-to-be-our-goal-in-life |
| 80 | 36395 | why-you-cannot-guide-others-beyond-your-own-stage |
| 80 | 36396 | why-personal-growth-is-rarely-a-joyous-process |
| 80 | 36397 | why-doing-your-best-matters-more-than-the-outcome |
| 80 | 36398 | why-your-character-shows-most-when-no-one-watches |
| 80 | 36400 | why-the-future-is-not-simply-a-repeat-of-the-past |
| 80 | 36406 | why-managing-your-emotions-is-work-that-never-ends |
| 80 | 36407 | why-your-life-runs-on-fumes-without-giving-back |
| 80 | 36408 | why-staying-angry-at-others-costs-you-so-much |
| 80 | 36410 | why-our-beliefs-are-just-guesses-or-ideas-at-best |
| 80 | 36411 | why-so-few-of-us-actually-know-what-we-believe |
| 80 | 36417 | why-changing-perception-will-change-how-we-relate-to-it |
| 80 | 36418 | what-it-means-when-they-say-they-dont-like-you |
| 80 | 36421 | why-life-eventually-becomes-about-other-people |
| 80 | 36422 | why-taking-time-to-reflect-brings-you-real-insight |
| 80 | 36423 | living-life-defined-by-labels-that-they-assign |
| 80 | 36424 | what-it-means-to-be-human-beings-not-human-doings |
| 80 | 36433 | why-peace-must-be-the-umpire-of-every-decision |
| 80 | 36434 | why-self-control-has-to-precede-our-own-growth |
| 80 | 36437 | why-what-you-do-always-outweighs-what-you-say |
| 80 | 36440 | why-real-control-means-taking-responsibility-for-the-parts-of-our-life |
| 80 | 36443 | why-you-are-your-own-harshest-critic |
| 80 | 36445 | why-not-every-thought-is-a-universal-truth |
| 80 | 36446 | why-maturity-is-not-associated-with-age |
| 80 | 36447 | what-it-means-to-keep-going-round-in-circles |
| 80 | 36448 | why-every-choice-you-make-will-cost-you-something |
| 80 | 36457 | why-relationships-are-the-cornerstone-of-our-life |
| 80 | 36458 | what-is-the-real-mark-of-maturity |
| 80 | 36460 | why-it-is-easier-to-spot-flaws-in-others |
| 80 | 36461 | why-we-compromise-our-integrity-to-keep-the-peace |
| 80 | 36464 | why-being-right-is-not-the-point-at-all |
| 80 | 36465 | why-needing-to-be-a-hero-hides-your-insecurity |
| 80 | 36467 | why-you-are-more-than-your-past |
| 80 | 36469 | why-experience-gives-us-authority-in-life |
| 80 | 36474 | why-a-blamer-hides-loneliness-behind-a-tough-mask |
| 80 | 36475 | why-no-mountain-gives-you-the-fulfillment-you-seek |
| 80 | 36478 | why-telling-the-truth-is-what-leads-to-trust |
| 80 | 36479 | why-to-honor-someone-is-to-assume-their-best |
| 80 | 36480 | why-real-peace-begins-once-you-accept-each-other |
| 80 | 36483 | why-wrestling-with-hard-ideas-is-how-we-grow |
| 80 | 36485 | what-wisdom-says-is-worth-your-time |
| 80 | 36486 | why-more-effort-now-means-better-results-later-on |
| 80 | 36487 | why-how-you-respond-matters-more-than-what-occurs |
| 80 | 36488 | why-anything-can-be-learned-and-mastered |
| 80 | 36490 | why-knowing-facts-is-not-the-same-as-understanding |
| 80 | 36492 | the-moment-we-assume-we-break-rapport |
| 80 | 36493 | why-focusing-on-the-positive-is-how-you-influence |
| 80 | 36494 | why-power-struggle-always-reveals-a-lack-of-trust |
| 80 | 36495 | why-simply-having-clarity-is-what-makes-people-act |
| 80 | 36496 | why-how-you-use-today-must-always-be-purposeful |
| 80 | 36497 | why-you-get-distressed-by-what-you-focus-on |
| 80 | 36498 | why-freedom-is-always-simply-a-choice-you-make |
| 80 | 36499 | why-real-understanding-ends-all-tension-in-a-bond |
| 80 | 36500 | why-simplicity-is-key-to-a-highly-effective-life |
| 80 | 36501 | why-you-cannot-work-harder-than-someone-else-will |
| 80 | 36503 | why-how-people-feel-is-always-their-real-problem |
| 80 | 36504 | why-discipline-is-what-turns-a-plan-into-action |
| 80 | 36505 | why-giving-our-time-to-others-teaches-us-ourselves |
| 80 | 36507 | why-we-never-get-around-to-doing-anything |
| 84 | 36309 | why-unmet-expectations-hurt-more-than-results |
| 84 | 36311 | why-maturity-means-severing-our-dependency-on-other-people |
| 84 | 36312 | why-life-is-a-constant-process-of-deciding |
| 84 | 36313 | why-we-end-up-going-round-and-round-in-circles |
| 84 | 36314 | why-unawareness-in-life-is-slavery |
| 84 | 36315 | why-we-become-masters-of-our-own-destiny |
| 84 | 36316 | why-thinking-like-a-winner-is-where-it-starts |
| 84 | 36319 | why-emotions-are-not-illnesses-to-be-fixed |
| 84 | 36321 | why-happiness-is-not-a-strong-motivator |
| 84 | 36327 | why-you-are-not-obligated-to-give-your-time |
| 84 | 36328 | why-the-people-we-let-into-our-lives-matter-most |
| 84 | 36330 | why-you-cannot-counsel-what-you-havent-taught |
| 84 | 36334 | why-we-relate-to-other-imperfect-human-beings |
| 84 | 36335 | why-we-can-listen-to-someone-without-hearing-them |
| 84 | 36338 | why-self-awareness-precedes-all-personal-growth |
| 84 | 36339 | why-profound-personal-growth-happens-in-private |
| 84 | 36343 | why-we-miss-the-inner-dialogues-that-go-on-inside |
| 84 | 36344 | why-change-becomes-greater-than-the-desire-to-remain-the-same |
| 84 | 36345 | why-self-pity-is-powerless |
| 84 | 36346 | why-the-only-control-we-have-is-how-we-choose-to-respond |
| 84 | 36349 | why-all-growth-is-relational |
| 84 | 36352 | why-were-not-entitled-to-anything |
| 84 | 36354 | why-techniques-are-the-lazy-persons-sport |
| 84 | 36355 | why-our-thoughts-create-feelings |
| 84 | 36357 | why-unwillingness-disguised-as-inability |
| 84 | 36358 | why-congruency-means-being-reflective-of-our-values |
| 84 | 36361 | why-the-desire-to-change-must-outweigh-staying |
| 84 | 36362 | why-complete-control-of-our-lives-begins-with-awareness |
| 84 | 36364 | why-we-interpret-our-life-events-the-way-we-do |
| 84 | 36368 | why-we-build-the-foundations-of-our-life-on-facts |
| 84 | 36370 | why-we-cant-occupy-two-spaces-at-the-same-time |
| 84 | 36371 | why-our-degree-of-relatability-depends-on-objectivity |
| 84 | 36372 | why-every-war-begins-in-the-mind |
| 84 | 36373 | why-the-brain-can-change-what-it-learned |
| 84 | 36374 | why-were-clean-slates-when-we-enter-the-world |
| 84 | 36375 | understanding-the-dialogue-inside-of-our-minds |
| 84 | 36378 | until-problems-have-owners-they-never-go-away |
| 84 | 36379 | why-everything-comes-back-to-taking-responsibility-for-your-life |
| 84 | 36380 | the-desire-to-change-becomes-greater |
| 84 | 36381 | being-completely-honest-about-ourselves |
| 84 | 36382 | why-truth-is-rarely-convenient-for-anyone |
| 84 | 36383 | why-personal-responsibility-comes-first |
| 84 | 36385 | why-being-at-peace-with-other-people-starts-within |
| 84 | 36387 | why-labels-are-for-tin-cans |
| 84 | 36388 | why-identity-is-the-mask-people-wear |
| 84 | 36389 | what-it-means-to-see-yourself-as-being-better-than-another |
| 84 | 36390 | why-its-wise-to-cut-out-the-unhealthy-relationships |
| 84 | 36391 | how-we-become-unrelatable-to-others |
| 84 | 36392 | the-difference-you-can-actually-make |
| 84 | 36393 | why-we-cant-be-motivated-by-something-that-we-already-have |
| 84 | 36394 | why-so-few-people-transcend-beyond-self-actualization |
| 84 | 36399 | why-what-simmers-beneath-the-surface-undermines-us |
| 84 | 36401 | why-our-beliefs-are-based-upon-our-past-experiences |
| 84 | 36402 | the-only-area-with-any-freedom-whatsoever |
| 84 | 36403 | one-decision-away-from-transforming-everything |
| 84 | 36404 | why-responsibility-starts-with-you |
| 84 | 36405 | nothing-happens-without-our-full-consent |
| 84 | 36409 | why-everyone-has-a-choice-to-change |
| 84 | 36412 | why-we-assume-that-what-we-think-is-true |
| 84 | 36413 | why-we-have-a-problem-with-our-sad-memories |
| 84 | 36414 | why-perception-is-not-reality |
| 84 | 36415 | why-emotions-reflect-our-perception |
| 84 | 36416 | why-youre-only-one-mind-change-away-from-feeling-different |
| 84 | 36419 | why-contribution-brings-about-fulfillment |
| 84 | 36420 | why-maturity-comes-down-to-acceptance-of-responsibility |
| 84 | 36425 | how-they-live-their-life-reveals-what-they-believe |
| 84 | 36426 | why-accepting-who-we-are-ends-despair |
| 84 | 36427 | why-a-low-opinion-of-yourself-causes-offence |
| 84 | 36428 | why-we-must-make-peace-with-our-flaws |
| 84 | 36429 | why-we-are-one-decision-away-from-making-complete-peace-with-ourselves |
| 84 | 36430 | why-its-easier-to-diagnose-people-than-to-understand-them |
| 84 | 36431 | why-being-real-starts-with-understanding-yourself |
| 84 | 36432 | why-people-pleasing-is-false-friendliness |
| 84 | 36435 | why-were-all-perfectly-imperfect |
| 84 | 36436 | why-youre-not-determined-by-anyone-else |
| 84 | 36438 | why-not-everyone-wants-you-to-grow |
| 84 | 36439 | growing-together-or-growing-apart |
| 84 | 36441 | why-belief-drives-your-wellbeing |
| 84 | 36442 | why-being-positively-influential-over-other-people-requires-nothing-in-return |
| 84 | 36444 | choosing-to-be-part-of-the-solution |
| 84 | 36449 | why-mutual-respect-decides-if-a-relationship-survives |
| 84 | 36450 | why-you-cant-trust-a-scared-person |
| 84 | 36451 | why-trust-is-the-foundation-of-every-relationship |
| 84 | 36452 | how-learning-from-mistakes-makes-you-more-valuable |
| 84 | 36453 | why-assumptions-are-the-killer-of-human-connectedness |
| 84 | 36454 | what-happens-when-dialogue-becomes-disrespectful |
| 84 | 36455 | why-confiding-requires-real-trust |
| 84 | 36456 | why-life-hangs-in-the-balance-of-our-judgments |
| 84 | 36459 | what-it-means-to-let-dead-things-stay-dead |
| 84 | 36462 | what-real-intolerance-for-difference-looks-like |
| 84 | 36466 | what-one-shift-in-perspective-can-actually-change |
| 84 | 36468 | why-we-become-the-relationships-that-we-keep |
| 84 | 36470 | why-change-in-your-life-belongs-to-you-alone |
| 84 | 36472 | why-self-regulation-precedes-social-awareness |
| 84 | 36473 | what-responsibility-actually-breeds |
| 84 | 36476 | how-your-values-shape-your-priorities |
| 84 | 36477 | why-you-are-not-what-you-do |
| 84 | 36481 | why-hardship-produces-growth-when-nothing-else-does |
| 84 | 36482 | why-trust-plus-time-is-the-real-intimacy-formula |
| 84 | 36484 | why-we-can-never-fully-understand-anyone-else |
| 84 | 36489 | why-vulnerability-is-not-weakness-but-strength |
| 84 | 36491 | why-youre-not-entitled-to-peoples-trust |
| 84 | 36502 | why-practice-does-not-make-perfect |
| 84 | 36506 | the-relief-in-not-having-it-all-together |
## 3. What this does not yet do

**No DSRD 6 record carries a score line.** These 200 pages are new tonight and none has a `DSRD6_RECORD.md` yet; that generator (task list item 2, `BRIEF__Every_Published_Article_And_Book_Note_Gets_A_DSRD_6_Record_S358.md`) is unstarted and is its own sitting. The score above lives here, in this table, until that generator exists to carry it into a per-page record, exactly as the skill's own rule says: a score exists only in this table until then.

**Nothing published.** That waits on Kain's word after his own Safari sample, per the brief.

---

OWED BACK: your read on whether 76 to 84 is an acceptable ceiling for this type as built, or whether the theme has a real gap worth finding before Kain's sample sitting.
