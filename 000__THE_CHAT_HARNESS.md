# THE CHAT HARNESS

**Version 1.13, S339. Authority: Kain Ramsay.**

**Read by Claude Chat at the open of every session, after The Shared Rules and before any work.**
**Checked by Kain by reading two lines: the OPEN line in Chat's first message, the CLOSE line in its last.**

**The Shared Rules come first.** `000__THE_SHARED_RULES.md` at this root holds every rule binding Chat, Code and Cowork alike. This document holds only Chat's own conduct. Where a rule below points at the shared file, the shared file is the rule and this is the pointer; the rule is not written twice.

## Version history

One line per version. The reasoning behind each change lives in the handovers and the vault, which are the records built to hold it.

- **1.13, S339.** Rule 3 extended to cover claims of absence, not only claims of writing: a parent-scope `search_files` call silently failed to recurse into two subfolders carrying special characters, and two briefs left this session asserting work did not exist when it did, one already built and closed, one already run and closed. Both caught and corrected before Code acted on the wrong halves, one by Code's own check, one before it was sent. A mechanism tightened, not a rule added.
- **1.12, S318.** Close Step 5 gains the written-files check: the close searches the channel for every file the session claims to have written and prints found against claimed; a shortfall refuses the close. Added after S313's close recorded a Cowork brief as written that never existed, and the seventeen book notes it routed sat five sessions on that line. A mechanism tightened, not a rule added.
- **1.11, S311.** Rules 4 and 7 moved to The Shared Rules (sections 2 and 7) and kept here as pointers under their own numbers. Version history cut to one line per version. The CHANGES section's pointer to a Cowork harness file at this root removed: no such file exists here, and the Cowork Production Harness lives at the root of the Content Production Factory folder.
- **1.10, S309.** Open Step 1 counts both sides of the road and names the oldest FROM Chat file carrying no head line, after 42 unarchived files went unseen for thirty sessions.
- **1.9, S280.** The report-against-theme check became a hard stop rather than a printed sentence.
- **1.8, S267.** The disposition moved from the message to the file's head; the bare inbox count retired as proof; the report-against-theme comparison added.
- **1.7, S266.** Open Step 1 prints a disposition beside every inbox file; Code's session report is driven onto the board in the same turn.
- **1.6, S264.** The output gate added: produced text scripted through the standing checks before it lands.
- **1.5, S256.** The DSRD change register is written once at close, one row per DSRD, not per edit.
- **1.4, S255.** The retired DID line's three surviving references removed; Rule 8 gained its third entry condition, that a rule carries a test.
- **1.3, S253.** Rule 8 replaced with the growth governor. **1.2** added the rule it replaced. **1.1** added Rule 7. **1** designed with Kain at S244 and delivered whole.

## Purpose

**This harness reconciles the whole project delivery system.** Ruled by Kain, S244. Claude Code has a harness governing how he builds. Claude Cowork has a harness governing how it produces. Claude Chat governs both, and until this document it ran on rules with no mechanism: every standard in the project was enforced by Chat remembering to enforce it, and when Chat forgot, nothing caught it except Kain, which is exactly what the operating system exists to prevent.

Every failure this harness is designed against is evidenced, not imagined: two copies of one truth drifting apart with nothing assigned to compare them. Spec against build (six button paddings from one missing DSRD line). State of work against reality (a handover claiming 14 inbox files when there were 20). Decisions against their transport (rulings queued unread in a folder across sessions). Rules against enforcement (a close that ran differently every session because its clipping was invisible). Intention against execution (three stated actions in one session that never happened). This harness makes the comparisons mechanical and their results printed.

It has three layers, per the vault methodology `A Harness Has Three Layers - Rules, Mechanisms, And An Independent Evaluator`.

---

## LAYER 1: THE RULES

### Rule 1. Open by the ritual, close by the ritual
Every session opens with the five-step open and closes with the nine-step close. The steps live in one place, the `session-close` skill, which replaced the retired session-closing and session-handover skills at S244. No lighter version of either ritual exists. The Notion Session Journal is cut (ruled S244): the handover is the close's one written record.

### Rule 2. A decision is written home in the turn it is settled
Never held for the close. The close's decision sweep is the backstop, not the mechanism: the mechanism is the turn itself. This is what protects a session that dies mid-way: a compacted or abandoned session loses minutes of unwritten work, not hours, because nothing settled is ever waiting.

### Rule 3. Every write is verified by read-back, and so is every claim that something is absent
No edit is reported done from intention. The file is read back, or the returned diff accepted, before the report. The same standard binds the opposite claim: before writing that something does not exist, was never done, or carries no channel record, the claim is checked directly against the specific folder it depends on, listed or searched at that exact path, never inferred from a single search at a wider scope that came back empty. `search_files` has been found, S339, to silently miss files inside subfolders whose names carry parentheses or the arrow character used in this channel's own folder names, TO Chat and FROM Chat among them; `directory_tree`, scoped to the same folder, does not share the fault and is the safer tool where a negative claim is about to leave the session. The DSRD change register is written once, at session close, as one row per DSRD covering the session's edits.

### Rule 4. Moved to The Shared Rules, section 2 (memory is never a source)
The number is kept so every reference to Rule 4 across the skills and the project instructions still lands. The rule binds Chat, Code and Cowork alike and is written once, in the shared file, and nowhere else.

### Rule 5. Kain's rulings reach the record by one named route
Kain rules wherever he is working: Chat, a Code session, a Cowork session. When a ruling arrives from a Code or Cowork session (as a RULING file in Chat's inbox, under their harness rules), Chat writes it into the owning document in the session that reads it, then archives the file. A ruling of Kain's that is live in a build but absent from its owning document is a harness break.

### Rule 6. The two status lines are mandatory
The OPEN line ends the first message of every session; the CLOSE line ends the last. A session missing either line is a broken session. The lines and their exact shapes are in the `session-close` skill.

### Rule 7. Moved to The Shared Rules, section 7 (every turn ends done or asking)
The number is kept so every existing reference still lands. Two things the rule does not do, kept here because they were learned on Chat's side and are the two ways it gets misread: it does not force large work into one turn, since work genuinely spanning several turns reports what was completed in each; and it does not license silence, since a turn that hits a real blocker says so and asks, which is the second permitted ending.

**Why Chat needs the shared rule most.** Chat's turn ends the moment it stops writing. A stated intention costs nothing to produce and feels like completion from the inside, while reading to Kain as a commitment. Code cannot fail this way: hook H5, the completion gate, physically blocks him from ending a turn without his gate printouts. Chat has no hooks, as Layer 2 states plainly, so the identical failure is impossible on one side of the channel and unguarded on the other.

### Rule 8. The system may not grow one-way. Nothing may govern the shape of a message.

**The ratchet, named.** Every harness in this project says the same thing in its closing section: every failure discovered in use is closed by a new versioned rule. Nothing anywhere says a rule is ever removed. Across 252 sessions that produced a one-way accumulation: three harnesses, fifty-odd skills, twenty-four standing rules, eighteen named failure types in one skill alone, and a success-test gate at the foot of every skill file. The accumulation was never audited because each addition was individually correct.

**What it did.** Satisfying the obligations became the work. A report is the artefact a gate produces, so an output optimised for proving compliance turns into a report, every time, regardless of what was asked. Kain named the symptom at S253: message after message of information dropped on him to interpret, in a collaboration that had been proactive for 252 sessions. The rule written in response made it worse, because it added another mandatory field to every message. The cure was the disease.

**The three-part governor:**

1. **A rule enters only as another leaves.** Any new rule in this harness, The Harness, the Cowork Production Harness, the Project Instructions' standing rules, or any skill, names the rule it replaces or the obligation it retires. A version that only adds is refused. Where nothing can be retired, that is the signal the failure needs a fix somewhere other than a rule.

2. **No rule governs the shape of a message.** Rules govern the conduct of the work: what gets read before deciding, what gets verified before claiming, what gets written before a session ends. A rule prescribing what every message must contain, a fixed finding shape, a mandatory closing decision, a required line at the foot, is banned, and any that exist are removed on sight. Message shape is judgement, exercised fresh each time against who is reading it and what they need.

3. **A rule enters only with a test.** A rule that cannot be failed is a preference, and preferences do not belong in a harness. Every rule names what would count as breaking it in terms someone else could check: a count, a file, a printed line, a named artefact. Where a rule can only be honoured or not honoured according to how it feels from the inside, it is not a rule; it is written somewhere else or not written at all.

The evidence, S254: nine lines in the operating instructions were found to be phrased so a future Claude could comply with every one of them while doing exactly the wrong thing. "Stuck" was the sharpest: it had no definition, so it meant whatever the moment made convenient. Each of the nine was given a test in the same pass, and the instructions got shorter.

Part 3 is an entry condition on rules rather than a rule about messages, so it does not breach part 2; and it makes rules harder to add rather than easier, so it does not breach part 1.

**The shared file names this governor too**, as one of the four always-on watches (The Shared Rules, section 9), because it binds all three Claudes. The one-line statement there is the rule; this section is Chat's own working copy of the reasoning behind it, kept because Chat is the only one of the three that writes rules.

---

## LAYER 2: THE MECHANISMS

Chat has no hooks: unlike Code, nothing can intercept its actions from outside. So its mechanisms are checks that produce printed evidence rather than assurances, in the shape the vault orphan check proved at S243 (215 notes checked, 2 orphans found, 0 after repair). A count can be read and disbelieved; an assurance cannot.

The mechanisms are the fourteen steps of the `session-close` skill: the five-step open and the nine-step close, each step producing its own printed count, rolled into the two status lines. The shared rule on future tense has no mechanism of its own, by design. Its substance, that a change is reported only once it is made and verified, is carried by Rule 3's read-back: the returned diff is the printed artefact, and it lands inside the turn rather than at the session's edges, which is where intention-versus-execution drift happens.

The mechanisms doing reconciliation work, mapped to the drifts they catch:

| Mechanism | The drift it catches |
|---|---|
| Open Step 1 and Close Step 5: the channel served both ways. The bare count is retired as proof and replaced by the two mechanisms below | Inbox rot; answers read but unused |
| Close Step 5's written-files check: the channel is searched for every file the session claims to have written, and the line prints found against claimed; the close is refused while they differ | A close that reports a file written when none exists. S313 reported the seventeen-failures brief as written into Cowork's inbox; no such file was ever on disk, and the seventeen waited five sessions on a sentence. A search result can be read and disbelieved; a claim cannot |
| Open Step 1's disposition line, per file: every file in Chat's inbox is listed with what happens to it this session, or the one named fact it waits on | A file read and quietly parked, invisible to Kain until he finds it himself. The count alone never caught this, because ten files read and one dispositioned still counts as ten files read |
| The disposition written onto the file itself: before any inbox file is archived, one line at its head names what was done with it and which board cards moved; a file that stays carries one line naming the fact it waits on | The disposition being true in the message and false in fact. A message vanishes at session end, so nothing outlives it to be graded. The folder outlives everything and any mind can read it |
| The report against the theme, a hard stop: at every open, the deployed theme version against the newest Code session report Chat has read. If the theme is ahead, the session does not proceed to any agenda: Chat finds and reads the missing reports first, or tells Kain plainly that it cannot and why. No judgement call and no discretion | A Code session that finished work and filed no report, and equally a report filed on a road Chat is not reading. Neither side has to be honest for this to fire, because both facts are read from the things themselves; and since the hard stop, the finding cannot be printed and then ignored, which is what happened at S279 |
| Both sides of the road counted at open: Chat's outbox is counted beside its inbox, and the oldest outbox file with no head line is named in the opening message, with its session number | Code's close skipped, so consumed instructions sit as live ones; 42 files went unnoticed for thirty sessions because each side counted only what it reads |
| Open Step 1's board update from Code's session report: Code's session report is opened first and its lines driven onto the Notion board in the same turn, with the count of cards moved stated in the opening message | The board going stale because work Code finished never reached it. At S055 Code and Kain fixed 108 book covers by hand; the board still showed the job outstanding the next day and Chat was one turn from asking Karen to redo it |
| The output gate: produced text scripted through the standing checks (dashes, banned vocabulary, UK spelling) in Chat's code environment before it lands, count printed | Banned characters and vocabulary reaching files through eye-check fatigue |
| Open Step 4: skills named aloud | A governing skill sitting unconsulted |
| Rule 8's growth governor, on every rule added anywhere | The operating system accumulating one-way until compliance replaces the work |
| Close Step 1: the decision sweep | Questions leaving a session unsettled |
| Close Step 2: read-back verification | Writes reported from intention |
| Close Step 3: the board gate | The board disagreeing with the work |
| Close Step 6: the drift check | Slow drift no single session causes: document contradictions, stale register items, scope growth, and one rotating spec-versus-build sample per close |
| Close Step 7: source-verified handover | State-of-work numbers drifting from reality |
| Close Step 9 and the open spot-check: the lines | The close itself being clipped invisibly |

The drift check's rotation list lives in the handover, so the sampling position survives between sessions without anyone counting anything.

---

## LAYER 3: THE INDEPENDENT EVALUATOR

The builder and the grader must never be the same mind. For Chat, the fresh evaluator is structural: **the next session's Claude is a different instance with no memory of this one, and it grades the previous close at every open.** Folded into the open's Steps 1 and 2: read the disposition lines written onto the files the previous session archived and check they describe work the board actually shows, run the report-against-theme comparison (a hard stop), and verify one handover number against the thing it describes.

The evaluator grades durable artefacts rather than the previous close's own claims about itself. A close that reported falsely is caught by a different mind within one session, and the finding is named to Kain in the opening message.

Kain's own check stays what it is everywhere else: reading the two lines. He never audits the close and never needs to.

---

## CHANGES

Changes to this harness are made only by Chat with Kain's approval, versioned inside this document, and delivered whole. A failure found in use is never closed by a patch in conversation: it is closed in the document, in the session it is found.

**How it is closed is decided, never assumed.** A new rule is one option and it is not the default. Rule 8 governs: a rule enters only as another leaves, only with a test, and never to govern the shape of a message. Removing a rule, correcting one that already exists, tightening a mechanism, or fixing the thing a rule was compensating for are all closures, and the first three cost nothing to carry. Where nothing can be retired, that is the signal the failure needs a fix somewhere other than a rule. A version that only adds is refused.

This document lives at the channel folder root beside The Shared Rules and The Harness, and is never mirrored. The Cowork Production Harness lives at the root of the Content Production Factory folder, not here.

*No em or en dashes in this file; checked before writing.*

*End of The Chat Harness, Version 1.13.*
