> CODE DISPOSITION, S180: WAITS ON more memory in this Mac: it is a 2019 iMac (i5-9600K, 8 GB, already 4.5 GB in swap), not an iMac Pro; the 8b Guardian with a 16384 context will not run at a usable speed, gemma4:26b not at all. Nothing installed, nothing sent. A 32 GB upgrade (the 27-inch has a rear memory door) would let the free test run.

> CHAT UPDATE, S441 (22 October 2026), answering the S180 disposition: Kain's yes to run it on the iMac Pro instead, which has 64 GB of memory and is the machine the research measured. A Code factory session opened on the iMac Pro takes this brief; the 2019 iMac is not upgraded. Everything else in the brief stands, and the machine check in step 3 is run on the iMac Pro first.

For Code (factory session): install Ollama with IBM's Granite Guardian on the iMac Pro, and build the side-by-side fact checker test the proof will run; the cheapest setup that catches every planted mistake is kept, and free is tried first.

# BRIEF: a second fact checker from other model families, free first, chosen by test (Chat, S441, 22 October 2026)

Read from the vault first: the Blueprint desk note The Fact Checker Clears Every Claim Against the Sources the Writer Was Given (its run card), and the research behind this brief, REPORT__A_Second_Family_Fact_Checker_Routes_And_Setup_S441 and REPORT__Proven_Loops_Of_Writing_And_Checking_Agents_S441, both in the Working Papers' research_S440 folder.

Model line: Code's own factory session on Opus 5.5 at xhigh, building the machine; the models under test are named below.

## Why

Every writer and checker in the newsroom is Claude. Published research finds judges from one family share blind spots and favour their own family's writing, and the costliest miss is a false fact. So the fact check gains a second and a third judge from other companies. Kain's words: "I'm pretty convinced that we should be able to run this for free. So yeah, let's do this."

## What to set up now

1. Ollama on the iMac Pro (the macOS app; it runs on the processor only on this Intel Mac), with `OLLAMA_NO_CLOUD=1` so nothing goes to Ollama's cloud.
2. `ollama pull granite4.1-guardian:8b` (Apache 2.0, built for "is this claim grounded in these documents"). Check its exact groundedness prompt format against IBM's model card on Hugging Face, not the third-party example in the report; for groundedness its "yes" means NOT grounded. Set `num_ctx` to at least 16384.
3. Measure its real speed on one page with `--verbose` and write the figure down; the report's speeds are arithmetic, not measured.
4. Not Bespoke-MiniCheck: its licence is non-commercial.
5. Optional, free: `gemma4:26b` as a free local claim extractor candidate.

## The test (run during the proof, on its four pieces)

Each test page needs its draft and its research file, which the proof pieces will have.

1. Make a second copy of each page with three to five planted mistakes: a changed figure, a wrong year, a misattributed quote, an overstated finding. Record each plant.
2. Freeze one claim list per page (extracted once, then merged), so every checker judges the same claims.
3. Run, side by side, on the same inputs and the same instruction text: Claude's fact checker as its run card gives it; Granite Guardian alone, on each claim; a free local extractor (gemma4:26b) feeding Granite, for a fully free route; and, only if the free routes miss any plant, the paid candidates through OpenRouter with zero data retention and data collection denied: the two cheap ones (Gemini Flash class, GPT Luna class) and the two mid-priced ones (Gemini 4 Argon, GPT 6.1 Sol).
4. Score each: plants caught out of plants planted; false alarms on clean claims; seconds and cost per page. Run each twice.
5. Chat checks every disagreement against the sources by hand.

## The rule, written before the test (Kain's yes, S441)

Keep the cheapest setup that catches every planted mistake. If a free route catches them all, the newsroom stays free and no account is opened. If none does, the cheapest paid candidate that does is kept, and Kain is asked then.

## What needs Kain's hands, and only if the free routes fail

An OpenRouter account and 10 US dollars of credit: Kain creates the account and buys the credit himself; Claude never creates accounts or enters payment details. He then gives you the key, stored as `OPENROUTER_API_KEY`.

## What comes back

A DONE file now: Ollama and Granite installed, the measured speed per page, and the test harness ready. After the proof: one REPORT with the scores per route and the setup kept under the rule.

Signed by Kain, 22 October 2026, in Chat's Session 441: "So yeah, let's do this. Let's go with this. Thank you, Claude."

OWED BACK: the DONE file for the setup.

*No em or en dashes in this file; checked before writing.*
