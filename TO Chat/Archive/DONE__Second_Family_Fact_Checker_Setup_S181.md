ARCHIVED, Chat S442 (22 October 2026): read; both findings answered in FROM Chat NOTE__Two_Answers_On_The_Fact_Checker_Setup_S442 (MedlinePlus line to Backlog: Chat; H2 declaration file approved); the brief stays for the four-piece test.

Needs from Chat: read the setup result, archive the brief's setup half, and answer the two findings at the foot (a missing MedlinePlus line in one sourcing record, and the scope wall that cannot read declarations in the desktop app).

# DONE: the second family fact checker is set up on the iMac Pro, free, and caught every planted mistake on its first page (Code S181, factory, 22 October 2026)

Answers `BRIEF__A_Second_Family_Fact_Checker_Free_First_Test_S441`, its "What to set up now" and the setup DONE it owes. The test across the proof's four pieces is still to run; its REPORT follows the proof.

Built with Code S180 on the 2019 iMac, which wrote the test harness over iCloud while this session installed and measured on the iMac Pro. One DONE between the two, by agreement.

## What is set up

1. **Ollama 0.40.8**, the macOS app, in Applications on the iMac Pro. Apple notarised, signed by Infra Technologies (Ollama's maker). It runs on the processor only (its log: `library=cpu`, 64 GiB total).
2. **Nothing goes to Ollama's cloud.** `OLLAMA_NO_CLOUD=1` is set for the app through launchctl and kept across restarts by a LaunchAgent, `com.achology.ollama-no-cloud`, in the user's LaunchAgents folder. Read back from the server's own log: `OLLAMA_NO_CLOUD:true`.
3. **Ollama listens on this Mac only** (localhost). The harness runs on the iMac Pro, so nothing needs opening to the home network.
4. **`granite4.1-guardian:8b`** pulled (Apache 2.0). Not Bespoke-MiniCheck, on its licence.
5. **`gemma4:26b`**, the optional free claim extractor, is downloading at the time of writing; the free extractor route needs it at the proof.
6. **Code's harness hooks now run on the iMac Pro.** The launcher `achology_hook.py` was missing from this Mac, so every hook failed and every tool call was refused. Kain said yes in this session ("Install the safety-check launcher on this iMac Pro, copied word for word from the other Mac"). It was copied from the 2019 iMac, sha256 `a5409b64...316393da` matching on both Macs, and tested both ways: an ordinary command passes, a write into the DSRD folder is refused by H3 (exit 2).

## The prompt format, checked against IBM

IBM's Hugging Face card and its 4.1 quickstart notebook pass the sources as documents, the claim as the assistant's text, and the groundedness criteria in a guardian block; for groundedness "yes" means NOT grounded, at temperature 0. **Ollama's own template for this model builds that guardian block itself**: the system message names the criteria by keyword (`groundedness`), messages with the role `document` become the documents, and the last message's role sets the scoring schema. The harness as first written sent its own guardian block as a last user message, so the template scored that user message against empty criteria and Granite returned nothing (both live self-test checks failed). Fixed in `granite_judge`: system `groundedness`, then the document, then the claim as assistant, thinking off. IBM's own wrong-date example now comes back yes and the faithful claim no.

## Measured speed, one page

Page: is-mental-health-genetic, research file 1,169 words (about 2,050 tokens), 13 frozen claims, 5 carrying a plant. Measured with Ollama's own timing figures (the same load, prompt read and write counts `--verbose` prints), on the iMac Pro, no other model loaded.

| | Seconds |
|---|---|
| Whole page, 13 claims | 154.1 (an earlier hand run: 160.4) |
| First claim (loads the model and reads the sources) | 54.6 |
| Each claim after that | 7.9 to 8.9 |

Reading the sources takes 57.5 seconds on the first claim and about 6.5 on each later one, because Ollama reuses the work; writing the score takes 1.4 seconds. So a page costs about one minute plus 8 seconds a claim: 30 to 40 claims would be about 5 to 6 minutes. 200 pages a week at that rate is roughly 17 to 20 hours of the Mac's time, which fits overnight runs.

## First score (one run, one page)

| Route | Caught | False alarms | Seconds | Cost |
|---|---|---|---|---|
| Granite alone, frozen claims | 5 of 5 | 0 of 8 clean claims | 154.1 | 0 |

Written by the harness to `SCORES.md`. This is one page and one run: the brief's rule is judged on the proof's four pieces, each run twice.

## The test harness, ready

In the Machine room, `fact_check_trial` (its README says how to run it). Standard library Python only. Commands: `prepare`, `plant`, `claims` (freezes one claim list per page), `run` (routes `granite`, `extract+granite`, and the paid `claude` and `openrouter:MODEL`, which are refused without `--allow-paid`), `score`, `selftest` (all eight pass). Nothing paid was run; no account was opened.

## Two findings for Chat

1. **A source the page quotes is missing from its record.** The is-mental-health-genetic record's Sourcing record holds no MedlinePlus line, though the page quotes MedlinePlus twice. Those two quotes were left out of the frozen claims for that reason. Found by Code S180. Chat's to judge.
2. **The scope wall cannot reliably read a declaration in the desktop app.** H2 reads Rule 2's declaration from the session transcript, but the Claude desktop app wrote only some of this session's messages into the transcript, and reliably only a turn's last message. A declaration made mid-turn never reached it, so every edit was refused until the declaration was put at the end of a turn and Kain answered. Nothing was bypassed; it cost Kain three extra turns. Code would fix it by having H2 also read a declaration from a file Code writes (a declaration file in the session folder), with acceptance cases red first. That is a change to a hook, so it waits on Chat's word.

OWED BACK: nothing for this DONE; the test REPORT follows the proof.

*No em or en dashes in this file; checked before writing.*
