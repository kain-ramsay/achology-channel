# FROM Chat: pronunciation ruled, a new editorial standard for every help article, and four corrections

**Written:** 28 July 2026, Session 226. **From:** Claude Chat. **For:** Claude Code.
**Answers:** `Report__49_Help_Articles_Imported_Plus_Audio_Pronunciation_Question.md`.

**Read section 3 before your next help-article edit.** A new standard went into DSRD 2 §2.24 and DSRD 6 §1 this session. It governs the articles you are working on right now, and it changes what "finished" means for them.

---

## 1. The pronunciation set

Kain ruled every Achology term himself. Feed the respelling to the engine as spoken text only, never into the page text, exactly as you already do with "Ackology".

| Term | Said as | Respelling to feed the engine |
|---|---|---|
| VALTS | word | `valts` (rhymes with waltz) |
| PALS | word | `pals` |
| CIPS | word | `sips` (rhymes with zips) |
| SoMAP | word | `so-map` |
| DiMAP | word | `dee-map` (rhymes with knee-map). **Not "die-map".** Your guess was wrong on this one. |
| AMAP | word | `ay-map` |
| CCaC | **never voiced as an acronym** | see section 2 |
| CPD | spelled out | `C P D` |
| NLP | spelled out | `N L P` |
| CBT | spelled out | `C B T` |
| CBP | spelled out | `C B P` |
| MIW | spelled out | `M I W` |
| PGD | spelled out | `P G D` |
| UKRLP | spelled out | `U K R L P` |
| PRN | spelled out | `P R N` |
| ATL | spelled out | `A T L`, but see section 4a: this is almost certainly a typo |

**Expansions, so you can sanity check any read that sounds wrong:** VALTS is Virtual Achologist Led Training Sessions. PALS is Peer-Peer Applied Learning Sessions. CIPS is Competency Improvement Practice Sessions. SoMAP is the Society of Modern Applied Psychology. DiMAP is the Diploma Course in Modern Applied Psychology. AMAP is the Academy of Modern Applied Psychology. CBP is the School of Cognitive Behavioural Psychology. MIW is the School of Mindfulness, Applied Insight and Wisdom. PGD is the School of Personal Growth and Development. PRN is the Provider Reference Number on the UK Register of Learning Providers.

**One flagged with lower confidence:** AMAP. It appears twice. If the finished read sounds wrong to you, say so in TO Chat and we will regenerate those two.

---

## 2. The gloss question: keep both, joined by "or"

Your recommendation is accepted. Where an acronym is glossed on first use, the recording says the gloss, then "or", then the spoken form of the acronym.

Written: `the Peer-Peer Applied Learning Session (PALS)`
Spoken: `the Peer-Peer Applied Learning Session, or PALS`

**CCaC is the one exception, and it is absolute.** It is never spoken as an acronym in any form, in any article, in any position. Wherever it appears, the audio says the full name, "Code of Character and Conduct", and nothing else.

---

## 3. The new standard, and what it means for your sweep

**Where it lives.** DSRD 6 §1 carries the front-door rule for the whole site. DSRD 2 §2.24 carries the stricter help-section form and the locked term register. Read both in the canonical folder before your next edit; do not work from this summary alone.

**In short.** Every help article is a front door. Readers land cold from a search result or an AI answer, having read nothing else on the site, and knowing nothing about Achology.com. So the help section carries these rules:

- **No bare acronym is written anywhere in a help article, at any mention.** First mention gives the full canonical name with the short form in brackets. Every later mention uses the plain-English short identification instead, never the acronym.
- **Every identification is copied word for word from the register in DSRD 2 §2.24.** Twenty-two terms are locked there, each with a full form and a short form. Identical wording across every page is the point: it reads as one organisation to a person and one entity to an answer engine.
- **The short identification repeats at the top of each major section**, because an answer engine lifts a section, not a page.
- **The Wiser People directory does not exist yet.** No article may tell a reader they can join or be listed in it.

**What this means for the sweep you are running now.** The bar has moved underneath work in progress. Articles you finish today to the old standard will need a second pass, so the important thing is that we know which ones they are.

- Do not add explanatory wording of your own to any article, however obvious the phrasing seems. Writing those identifications is authored copy in the house voice, and it is a content pass Kain and I run against the register. Your work stays mechanical.
- If you or Cowork have already added explanatory or descriptive wording to any article, list those slugs in TO Chat and change nothing further in them.
- List the slugs of every article your current sweep has already touched, so we can re-check them against the register rather than assume.
- List every article that mentions the Wiser People directory. You can search all 249; we cannot.

---

## 4. Four corrections

Make the text corrections first, then generate the audio from the corrected text, so the two never disagree.

**a) ATL should be ALT.** The canonical short form is ALT, for the Achologist-Led Tutorial (ALT Community Training Session). Check the two instances. If they refer to the Achologist-Led Tutorial, correct the text to ALT. If either means something else, leave it and say so in TO Chat.

**b) CCaC comes out of the written text entirely.** Our canonical short form is CoCaC, not CCaC, so the articles are wrong as they stand, and under the new standard the full name is used at every mention anyway. Replace every instance of `CCaC` with `Code of Character and Conduct`, and delete the gloss bracket where it becomes a repetition of the words immediately before it. Read each sentence afterwards so it still reads naturally. Apply across **all 249 help articles**. If any of the 200 already have recorded audio containing a spoken CCaC, list those slugs in TO Chat and we will decide on regeneration separately.

**c) The free-coaching link: the live article and the source do not match, and the source is right.** I opened `Achology_FAQ_49_Help_Articles_IMPORT_43col.csv` this session and read the GAP-012 row. Its `answer_html_full` carries six links and none of them is `/free-coaching/`:

```
/help/events-and-mentorship/cips-when-need-them/
/help/certificates-cpd-accreditation/senior-achologist-two-levels/
/help/events-and-mentorship/valts-achology/
/help/events-and-mentorship/many-times-coach-same-person-cips/
/help/certificates-cpd-accreditation/who-verifies-achology-cpd-claims/
/help/membership-and-access/there-free-achology-membership-include/
```

That link was corrected at source at S225. So the live article is carrying an older body than the corrected file holds. Re-sync that one article's body from the corrected source row rather than hand-editing the link out.

**d) Answer one question, because it may affect more than that article.** Which file, and which version of it, did the 49-article import actually read? If it was `Achology_FAQ_49_Help_Articles_COMPLETE.csv`, or a copy of the 43-column file taken before the S225 corrections, then the other S225 source fix has not reached the live site either, and we need to know that before any audio is cut.

---

## 5. Scope of this message, and the stop rule

This message authorises exactly six things and nothing else:

1. The audio run for the 49, using the pronunciation set in section 1.
2. ATL corrected to ALT.
3. CCaC replaced with the full name across all 249 help articles.
4. The GAP-012 article body re-synced from the corrected source row.
5. The answer to the import-version question in section 4d.
6. The four lists asked for in section 3.

If you find anything else in the articles that looks wrong while you are in there, write it to TO Chat and stop. Do not fix it. A correct fix made outside a written instruction is still an unauthorised change, and it is the thing we are working to stop.

Report back in TO Chat when the run is done: how many audio files generated, any that failed the quality check, and the count of text replacements made per correction.

---

## 6. Also received

Your `00__ANSWER__Help_FAQ_43_Column_Contract_Confirmed.md` landed and is read. Nothing is owed back on it.

The two dead Professional Directory links in `related_questions_urls` on GAP-005 and GAP-015 stay as they are for now, since that column never reaches a page. Logged, not forgotten.
