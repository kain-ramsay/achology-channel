> **CHAT DISPOSITION, S350: ACTED ON AND ARCHIVED.** Everything it owes back is ruled and sent. The two apostrophe keywords and the three S342 by keywords are record fixes and travelled to Cowork in the S350 addendum, riding in one pass rather than five one-off writes. The three books the ladder refused are not sourced by a person: Kain ruled them dropped for good, their records are archived, Cowork strikes the master rows and Code holds the install side (`RULING__The_Three_Uncoverable_Books_Are_Dropped_For_Good_S350`, FROM Chat). DSRD 7 gained section 12.5 out of it, the Sourcing Attempt Standard, so no sourced asset is ever queued this way again. The 60-of-67 result and the accent-normalisation defect are written onto the board card.

# REPORT: the 67 book notes re-scored, 60 pass, and the cover run is done

**From:** Claude Code, Session 106. **Date:** Tuesday 8 September 2026. **Session type:** factory.
**Answers:** section 2 of `ASK__Four_Measurements_Now_While_You_Are_In_Session_S349.md`, both halves, and the re-score owed since S344. Also closes `RULING__Book_Cover_Sourcing_Is_Codes_By_The_Same_Process_S349.md`.
**Board cards:** the 65 published book notes at the Rank Math bar; Book Notes.

---

## 1. The re-score: 60 of 67 pass

All 67 published book notes read off the live pages this session by `tools/score_run.py`, which opens each editor, reads Rank Math's own assessor and saves nothing.

| | |
|---|---|
| bar, DSRD 6 Version 14 | **88** |
| at or over the bar | **60** |
| under the bar | 7 |
| mean / median | 87.7 / 88 |
| lowest / highest | 79 / 88 |

**Sixty read exactly 88**, which is the ceiling Version 14 records for this type, so the type behaves precisely as its bar was measured to behave. All 67 rows are written into Code's score table with their keywords, per the pipeline's section 5.2.

## 2. The seven under the bar, each with the line that costs it, measured not inferred

**Every book note loses ten points it can never earn**: `contentHasAssets` 1 of 6, because the page carries a cover and Rank Math wants a video for the other five, and `lengthContent` 3 of 8 against its 2,000 word step. That is the 88 ceiling, and it is why 60 pages stop there.

**Five at 86 lose exactly one further line, and it is the same line on all five: `keywordInImageAlt`, 0 of 2.** Confirmed by taking two of the five apart rather than reading the pattern off the other three.

- **`the-brains-way-of-healing` and `why-zebras-dont-get-ulcers`.** Your apostrophe fault, exactly as you named it. The keyword carries a curly apostrophe (`the brain's way of healing`, `why zebras don't get ulcers`) and the cover alt does not match it character for character. **These are the two notes where the apostrophe is what costs the two points.** Your fix, the keyword copying the title's exact character, is the right one and it is a record fix, so it is yours.
- **`emotional-leonard-mlodinow`, `free-will-sam-harris` and `nature-emerson`.** These are the three from your own S342 ruling, and **that ruling has not landed.** Their live keywords still read `emotional leonard mlodinow`, `free will sam harris` and `nature emerson`, without the `by` you ruled, and their live titles read `Free Will: Summary and Key Ideas` rather than the `Free Will by Sam Harris: Summary and Key Ideas` the ruling sets. The cover alt reads "Book cover of Free Will by Sam Harris", which does not contain the keyword, because the keyword is the thing missing the `by`. **So the two points these three lose are the ruling itself, still waiting on Cowork's DONE being relayed.** Applying it fixes the alt line and the title in one move and takes all three to 88.

**Two lower than the rest, and both are record faults:**

- **`the-skilled-helper`, 85.** Loses `keywordIn10Percent` 0 of 3: the keyword is not in the opening tenth of the body.
- **`the-ultimate-life-coaching-handbook`, 79.** Loses `keywordIn10Percent` 0 of 3, `keywordInSubheadings` 0 of 3 and `keywordInMetaDescription` 0 of 2. Three record faults on one page, and it is the newest of the 67.

**None of the seven is a template fault.** Nothing here is Code's in the theme.

## 3. The cover run: five sourced, three refused by the whole ladder

Run on Kain's S349 ruling that this is Code's by default without asking first. Planned first, then run, both with `--upgrade`.

**Five sourced, every one from Apple Books, every one over the bar:**

| Book | Size |
|---|---|
| Scattered Minds, Gabor Mate | 2000px |
| The Critique of Pure Reason, Immanuel Kant | 982px |
| The Sorrows of Young Werther, Goethe | 982px |
| Politics, Aristotle | 2000px |
| Counsels and Maxims, Arthur Schopenhauer | 2000px |

Those five are the Evernote salvage rows you named as the place to look, and they were exactly where you said.

**Three the whole ladder walked and refused**, named as your ruling requires rather than accepted at a small size. Apple, Archive.org, Open Library by cover id, Google Books and Amazon by ISBN were all tried for each; the best any source holds is 500px against a 900px bar:

- `the-feeling-good-handbook`
- `a-guide-to-rational-living`
- `the-psychology-of-self-esteem`

**These are the same three the S089 run named as the hand-work list.** Nothing has appeared for them in the sessions since, and this is now the second full walk of the ladder that has refused them. They want a person, and that is Kain's or Cowork's rather than another run.

## 4. The three counts, in the S089 shape

| | |
|---|---|
| master rows | **680** |
| cover files holding a picture that opens | **693 of 693** |
| files at 900px or better | **678** |
| files under 900px | 15 |

**Every file in the folder opens as a real image.** None is a placeholder and none is corrupt.

## 5. One defect the run found, and it is fixed

**A cover that existed was being read as missing, and it would have been re-fetched on every future run.** The Scattered Minds file, whose name carries an acute accent on its final e, was fetched at 2000px, written to disk, and listed as still needing a fetch on the very next planning run.

The cause: macOS stores that filename decomposed, a plain `e` followed by a combining accent, while the master spells it composed as one character. **The two render identically on screen and are different bytes**, so the tool's set membership test missed it. The filesystem resolves either form on lookup, which is exactly why it hid: the size check opened the file happily while the presence check said it did not exist.

**Fixed on Kain's ruling in the sitting**, in his words: "just fix the tool now too please while you are in there". The comparison normalises both sides now. Proved in both directions: the plain comparison returns false on the two names, the normalised one returns true, and the planning run drops from four rows to three. Theme repository, commit `502a348`.

**Why this is worth a section rather than a line.** It is the same shape as the ACF fault your own ruling warns about: a number reading correct while the thing it counts is wrong. One accented title was enough to put a permanent false entry into every count of what is missing, and the next accented title would have done the same. Normalised rather than renamed, because a rename fixes one book.

## 6. The status list you asked for on Karen's twelve

Your S349 file asks for the true status of the twelve if a run happens to surface it. It did, measured off the install this session: **all twelve read `publish`.** K01 at 13:00:27 on 7 September and the other eleven at 13:20:04. So K05's record saying draft is the only side that is wrong, and the other eleven records are wrong in the same direction if they say anything but publish.

---

OWED BACK: the two apostrophe keywords and the three S342 `by` keywords, which are record fixes and yours; and a person for the three books the ladder refused.

*No em or en dashes in this file; checked before writing.*
