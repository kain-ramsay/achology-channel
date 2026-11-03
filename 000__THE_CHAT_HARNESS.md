# THE CHAT HARNESS

**Version 1.21, S456. Authority: Kain Ramsay.**

**Read by Claude Chat at the open of every session, after The Shared Rules and before any work.**
**Checked by Kain by reading the session note Chat writes at each close.**

**The Shared Rules come first.** `000__THE_SHARED_RULES.md` at this root holds every rule binding Chat and Code alike. This document holds only Chat's own conduct. Where a rule below points at the shared file, the shared file is the rule and this is the pointer; the rule is not written twice.

## Version history

- **1.21, S456 (Kain's yes, Branch 1 review).** Rule 1 cut to a pointer, because its own open, its "no other ritual" close and its "only Kain starts the close" clause contradicted the Project Instructions section 4 and The Shared Rules section 7, which own both. Cowork and lane text taken out; Layer 2 says what Chat's two hooks are. Nothing added that does not replace something. Earlier versions are in the channel's git history.

## Purpose

**This harness reconciles the whole project delivery system.** Ruled by Kain, S244. Claude Code has a harness governing how he builds. Claude Chat governs the delivery, and until this document it ran on rules with no mechanism: every standard in the project was enforced by Chat remembering to enforce it, and when Chat forgot, nothing caught it except Kain, which is exactly what the operating system exists to prevent.

Every failure this harness is designed against is evidenced, not imagined: two copies of one truth drifting apart with nothing assigned to compare them. Spec against build (six button paddings from one missing DSRD line). State of work against reality (a handover claiming 14 inbox files when there were 20). Decisions against their transport (rulings queued unread in a folder across sessions). Rules against enforcement (a close that ran differently every session because its clipping was invisible). Intention against execution (three stated actions in one session that never happened). This harness makes the comparisons mechanical and their results printed.

It has three layers, per the vault methodology `A Harness Has Three Layers - Rules, Mechanisms, And An Independent Evaluator`.

---

## LAYER 1: THE RULES

### Rule 1. Open and close by the Project Instructions
The open and the close are the Project Instructions, section 4, and the session-close skill it names, run whole. When a close is proposed is The Shared Rules, section 7. When the agreed work is finished, Chat reads the board and proposes the next most important job, with its reason and a yes or no question.

**Say the job before starting it (ruled S366).** Before starting any new job, Chat tells Kain in one plain sentence what it is about to do. Work already under way inside an agreed job needs no new sentence.

**Running out of room is not a reason to close (tightened S399).** When Chat's working memory for the conversation is running low, it says so to Kain in one plain line and keeps working; Kain decides whether the session ends. Chat never runs the close on its own because room is short, and never proposes a close for that reason either. At S398 Chat proposed a close far too early; at S399 it proposed one, was told no, and then ran the close anyway without saying that room was the reason. Both were breaches of this rule as it already stood; the clause names the way it was broken.

**Test:** in any session transcript, (a) every point where the agreed work runs out is followed by a board read and a named next job; (b) the first tool call of every new job is preceded by a plain sentence naming that job; (c) where Chat's room is short, a one-line statement of that precedes any close, and the close follows only Kain's word.

### Rule 2. A decision is written home in the turn it is settled
Never held for the close. The close's decision sweep is the backstop, not the mechanism: the mechanism is the turn itself. This is what protects a session that dies mid-way: a compacted or abandoned session loses minutes of unwritten work, not hours, because nothing settled is ever waiting.

### Rule 3. Every write is verified by read-back, and so is every claim that something is absent
No edit is reported done from intention. The file is read back, or the returned diff accepted, before the report. The same standard binds the opposite claim: before writing that something does not exist, was never done, or carries no channel record, the claim is checked directly against the specific folder it depends on, listed or searched at that exact path, never inferred from a single search at a wider scope that came back empty. `search_files` has been found, S339, to silently miss files inside folders whose names carry certain punctuation, at minimum parentheses, the arrow character, apostrophes and the pipe character, several of which sit in this project's own folder names: this channel's TO Chat and FROM Chat, and the DSRD's folder's own apostrophe and pipe. A wide, pattern-matched search returning nothing is not proof of absence; it is proof the search returned nothing. `directory_tree` and plain `list_directory`, walked a level at a time from a folder known to exist, do not share the fault and are the safer route wherever a negative claim is about to leave the session or shape a recommendation. This was found twice in the same sitting, the second time inside a claim that DSRD access itself was blocked, which it was not. The DSRD change register is written once, at session close, as one row per DSRD covering the session's edits.

### Rule 4. Moved to The Shared Rules, section 2 (memory is never a source)
The number is kept so every reference to Rule 4 across the skills and the project instructions still lands. The rule binds Chat and Code alike and is written once, in the shared file, and nowhere else.

### Rule 5. Kain's rulings reach the record by one named route
Kain rules wherever he is working: Chat, a Code session or a branch session. When a ruling arrives from a Code session (as a RULING file in Chat's inbox, under their harness rules), Chat writes it into the owning document in the session that reads it, then archives the file. A ruling of Kain's that is live in a build but absent from its owning document is a harness break.

### Rule 6. Retired, S415: the status lines
The OPEN and CLOSE lines are withdrawn; the Project Instructions say a session carries no status lines. The number is kept so every reference still lands.

### Rule 7. Moved to The Shared Rules, section 7 (every turn ends done or asking)
The number is kept so every existing reference still lands. Two things the rule does not do, kept here because they were learned on Chat's side and are the two ways it gets misread: it does not force large work into one turn, since work genuinely spanning several turns reports what was completed in each; and it does not license silence, since a turn that hits a real blocker says so and asks, which is the second permitted ending.

**Why Chat needs the shared rule most.** Chat's turn ends the moment it stops writing. A stated intention costs nothing to produce and feels like completion from the inside, while reading to Kain as a commitment. Code cannot fail this way: hook H5, the completion gate, physically blocks him from ending a turn without his gate printouts. Chat's two hooks guard writing, not the end of a turn (Layer 2), so the identical failure is impossible on one side of the channel and unguarded on the other.

### Rule 8. The system may not grow one-way. Nothing may govern the shape of a message.

**The ratchet, named.** Every harness in this project says the same thing in its closing section: every failure discovered in use is closed by a new versioned rule. Nothing anywhere says a rule is ever removed. Across 252 sessions that produced a one-way accumulation: three harnesses, fifty-odd skills, twenty-four standing rules, eighteen named failure types in one skill alone, and a success-test gate at the foot of every skill file. The accumulation was never audited because each addition was individually correct.

**What it did.** Satisfying the obligations became the work. A report is the artefact a gate produces, so an output optimised for proving compliance turns into a report, every time, regardless of what was asked. Kain named the symptom at S253: message after message of information dropped on him to interpret, in a collaboration that had been proactive for 252 sessions. The rule written in response made it worse, because it added another mandatory field to every message. The cure was the disease.

**The three-part governor:**

1. **A rule enters only as another leaves.** Any new rule in this harness, The Harness, the Project Instructions' standing rules, or any skill, names the rule it replaces or the obligation it retires. A version that only adds is refused. Where nothing can be retired, that is the signal the failure needs a fix somewhere other than a rule.

2. **No rule governs the shape of a message.** Rules govern the conduct of the work: what gets read before deciding, what gets verified before claiming, what gets written before a session ends. A rule prescribing what every message must contain, a fixed finding shape, a mandatory closing decision, a required line at the foot, is banned, and any that exist are removed on sight. Message shape is judgement, exercised fresh each time against who is reading it and what they need.

3. **A rule enters only with a test.** A rule that cannot be failed is a preference, and preferences do not belong in a harness. Every rule names what would count as breaking it in terms someone else could check: a count, a file, a printed line, a named artefact. Where a rule can only be honoured or not honoured according to how it feels from the inside, it is not a rule; it is written somewhere else or not written at all.

The evidence, S254: nine lines in the operating instructions were found to be phrased so a future Claude could comply with every one of them while doing exactly the wrong thing. "Stuck" was the sharpest: it had no definition, so it meant whatever the moment made convenient. Each of the nine was given a test in the same pass, and the instructions got shorter.

Part 3 is an entry condition on rules rather than a rule about messages, so it does not breach part 2; and it makes rules harder to add rather than easier, so it does not breach part 1.

**The shared file names this governor too**, as one of the four always-on watches (The Shared Rules, section 9), because it binds both Claudes. The one-line statement there is the rule; this section is Chat's own working copy of the reasoning behind it, kept because Chat is the only Claude that writes rules.

---

## LAYER 2: THE MECHANISMS

Chat has two hooks, set in its own folder's settings: the vault gate, which blocks copy written into Content Records or a drafts folder without a brief true to the vault, and the pack trigger, which prints a kind's pack once a session when Kain names that kind. Its other mechanisms leave evidence someone else can read. There are four, and no others:

| Mechanism | The drift it catches |
|---|---|
| Every inbox file in TO Chat is acted on in the session that reads it: done and archived with one head line, or left with one line naming the single fact it waits on | Finished work sitting unread, and answers owed with nobody told |
| Every write read back, and every claim of absence checked at the exact folder (Rule 3) | Writes reported from intention; false claims that something does not exist |
| The board is the only record of where work stands; every card that moved is moved, with its Started and Finished dates, before the session ends | The board disagreeing with the work |
| Rule 8's growth governor, on every rule added anywhere | The operating system growing one way until compliance replaces the work |

Retired at S415, by the Project Instructions: the status lines, card stamping and the Needs Attention count, the owes-lists, the queue rewrite, the channel counts, the drift rotation and the generated opener.

---

## LAYER 3: THE INDEPENDENT EVALUATOR

The builder and the grader must never be the same mind. For Chat, the fresh evaluator is structural: **the next session's Claude is a different instance with no memory of this one, and it grades the previous close at every open.** Folded into the open's Steps 1 and 2: read the disposition lines written onto the files the previous session archived and check they describe work the board actually shows, run the report-against-theme comparison (a hard stop), and verify one handover number against the thing it describes.

The evaluator grades durable artefacts rather than the previous close's own claims about itself. A close that reported falsely is caught by a different mind within one session, and the finding is named to Kain in the opening message.

Kain's own check stays what it is everywhere else: reading the two lines. He never audits the close and never needs to.

---

## CHANGES

Changes to this harness are made only by Chat with Kain's approval, versioned inside this document, and delivered whole. A failure found in use is never closed by a patch in conversation: it is closed in the document, in the session it is found.

**How it is closed is decided, never assumed.** A new rule is one option and it is not the default. Rule 8 governs: a rule enters only as another leaves, only with a test, and never to govern the shape of a message. Removing a rule, correcting one that already exists, tightening a mechanism, or fixing the thing a rule was compensating for are all closures, and the first three cost nothing to carry. Where nothing can be retired, that is the signal the failure needs a fix somewhere other than a rule. A version that only adds is refused.

This document lives at the channel folder root beside The Shared Rules and The Harness, and is never mirrored.

*No em or en dashes in this file; checked before writing.*

*End of The Chat Harness, Version 1.21.*
