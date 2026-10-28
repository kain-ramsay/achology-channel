**For Chat. What this needs from you:** road step 18 on the eight pages; record mends for the two pages at 85; and the inbound link sentences (TO Chat/ASK__The_Resisting_Change_Inbound_Links_Need_Their_Sentences_S195).

# DONE (Code, factory session S195, a side session of S194): the eight signed resisting change quote pages are on the build site

Answers BRIEF__Import_The_Eight_Signed_Resisting_Change_Quote_Pages_S448, on Kain's go ("yes, please do", given in the S194 sitting). Also answers section 3 of RULING__Gate_Lines_On_Signed_Words S449 (the signature fix) and item 1 of NOTE__Gate_Faults_Found_On_The_Resisting_Change_Batch_S448.

## 1. The eight, on the build site and published

| quote_id | Post | Address now | How |
|---|---|---|---|
| Q07056 | 38517 | /learn/helping-people/quotes/why-people-resist-change-until-they-have-to/ | updated, address unchanged |
| CQ018-041-1 | 36380 | /learn/mental-wellness/quotes/do-people-only-change-when-its-too-late/ | updated and renamed |
| CQ001-043-1 | 41214 | /learn/motivation/quotes/do-people-only-change-when-they-want-to/ | **created**, then published |
| CQ018-018-1 | 36344 | /learn/mental-wellness/quotes/is-it-human-nature-to-resist-change/ | updated and renamed |
| CQ018-027-1 | 36361 | /learn/mental-wellness/quotes/why-is-it-so-hard-to-change-your-mindset/ | updated and renamed |
| CQ018-009-1 | 36325 | /learn/mental-wellness/quotes/why-do-i-resist-change-so-much/ | updated and renamed |
| Q07016 | 36267 | /learn/helping-people/quotes/why-we-resist-change-even-when-its-positive/ | updated and renamed |
| Q07042 | 38503 | /learn/helping-people/quotes/why-is-change-so-hard/ | updated and renamed |

**CQ001-043-1 was not on the build site** under any quote_id or address, so the brief's "update in place" could not apply to it. It was created as a draft by the importer, its share picture was made, and it was published through `publish_gate.py`. The page had no public address yet, so the clearance (1343902b3c8b4eee) went through the override, quoting Kain's S417 ruling ("Signed pages are published on the build site") and his S194 yes. It was then re-gated live.

**The importer.** `import_quote_pages.py` (The Machine) now matches a record whose new address holds no post by its quote_id, so the seven renamed posts were updated rather than duplicated. Two posts on one quote_id is refused, never guessed. It also had two dead paths since the S434 move (records and course covers), now read from the shared importer. The plan run before the push showed seven UPDATEs and one new draft. `--verify` reads 8 of 8 clean, and the update path changed no status. The shared `import_field_authority_articles.py` was not touched. `body_guard.py --signed` exits 0.

**Read back off the build site, logged out:** each of the eight answers 200 at its new address. Its search title, headline and description match the record (the apostrophes come back as entities, as everywhere on the site), and the course cover and author picture are present.

**Share pictures.** The seven existing pages carried share pictures made from an older card design (a550389032b5), and the gate refused them for it. All eight were baked fresh at design cbbdd1cf055c with `make_quote_cards.py --attach`. Then all eight cleared `publish_gate.py --clear --update` at their live addresses (clearance 69d35e34fcac10f6). Carried, not blocking: dsrd6-record, image-budget, image-responsive, keyword-density, orphan.

## 2. Redirects: six, not seven

Written and proved by `publish_gate.py --write-redirect` (each a 301 that the server answered):
- /learn/mental-wellness/quotes/the-desire-to-change-becomes-greater/ to do-people-only-change-when-its-too-late/
- /learn/mental-wellness/quotes/why-change-becomes-greater-than-the-desire-to-remain-the-same/ to is-it-human-nature-to-resist-change/
- /learn/mental-wellness/quotes/why-the-desire-to-change-must-outweigh-staying/ to why-is-it-so-hard-to-change-your-mindset/
- /learn/mental-wellness/quotes/why-theres-a-limit-to-how-much-change-people-can-handle/ to why-do-i-resist-change-so-much/
- /learn/helping-people/quotes/ready-to-change/ to why-we-resist-change-even-when-its-positive/
- /learn/helping-people/quotes/why-change-never-happens-overnight/ to why-is-change-so-hard/

The seventh new address, CQ001-043-1's, has no old address on the build site to redirect from, because the page never existed there.

## 3. Inbound links: none added, waiting on Chat

Not added. The records name the linking pages but not the sentences the links sit in, and none of the five linking pages carries any of the eight titles. A new sentence would be drafting on signed pages. The full count and what Code will do on the answer are in ASK__The_Resisting_Change_Inbound_Links_Need_Their_Sentences_S195.

## 4. Rank Math scores (bar 86, RULING__The_Article_Publish_Bar_Is_86 S449)

Read by the theme's `tools/score_run.py`, all settled:

| Post | quote_id | Focus phrase | Score |
|---|---|---|---|
| 41214 | CQ001-043-1 | people only change when they want to | 91 |
| 36380 | CQ018-041-1 | only change when it's too late | 88 |
| 36344 | CQ018-018-1 | human nature to resist change | 87 |
| 36361 | CQ018-027-1 | hard to change your mindset | 87 |
| 36325 | CQ018-009-1 | resist change so much | 87 |
| 38517 | Q07056 | people resist change | 86 |
| 36267 | Q07016 | resist change even when it's positive | **85** |
| 38503 | Q07042 | why is change so hard | **85** |

Six reach 86. **Two read 85, one under the bar.** The score run does not read Rank Math's own list of failing tests. What Code measured from the records and pages: on both pages the focus phrase appears once in the body (in the opening) and in no subheading. `search_gate.py` reads its density at 0.12 and 0.11 per cent against the 1.0 floor. The only page carrying the phrase twice (41214) is the one at 91. Both stay published, since they were already public and this import changed no status. Chat mends their records, with Kain's yes for the signed words, and Code lands the mend on its own update.

## 5. The gate fixes

- **The vault gate signature form passes** (`content_gate.py`, `signed_check`). Where a signature names a session and carries no version, the gate reads the Standard version in force on the signature's date from the Standard's own version paragraphs (Version 34 on 27 October 2026) and says so on the line. Acceptance cases added (`content_gate_acceptance.py`, S195, seven cases, all passing): the real signatures on anxiety-is-ruining-my-life and Q07056 pass as Version 34; Version 33 is read for 23 October; a signature with no version and no session still fails; anyone but Kain still fails; the check sheet form is unchanged. The suite reads 459 of 463. The four still failing (worked example article on disk, worked example landing page body on disk, help answer runs no other voice line, finding 13) failed identically before this change, read against the gate at HEAD. This also passes the 53 Help answers' "YES (Session 449 ...)" signature, which names its session the same way.
- **Item 1 of the S448 gate faults note: confirmed.** No importer calls `body_guard.is_signed`. `import_quote_pages.py` reads the signed field itself through `content_gate.read_fields`, as do the others.
- **Not done here:** items 2 and 3 of that note, NOTE__Quote_Pages_Need_No_External_Source_Link_Gate_Fault_S449, and RULING__Quote_Closing_Question_Has_No_Character_Band_S450. They wait on a factory session with the content gate open.

## Commits

Project: the importer and gate change set (named in the commit message "Eight resisting change quote pages, S195"). Channel: this DONE, the ASK and the disposition lines.

*No em or en dashes in this file; checked before writing.*
