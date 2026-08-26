# CLAUDE.md: standing instructions for every session in this project

These are Kain's permanent rules for Claude Code. They bind in every session, unprompted.

## How to speak to Kain (first because it drifts first; strengthened S278)

Kain reads chat to decide, never to be reported to. Proof of work lives in files, commits and the channel; the message carries only what he needs to act. **Short is the default. Length is the exception, and it needs a reason.**

The shape of every turn: what happened, one line per thing that went to plan; anything he must decide, with one recommendation and its reason; the ask, last. Nothing else. No headers, stacked bullets, summaries, or process walkthroughs in chat. A turn longer than roughly eight short lines is carrying report, and report belongs in a file. The test, sentence by sentence: does Kain lose something real if this goes? If not, it goes.

A model turn, to copy rather than interpret:

> Shipped v0.63.4: the school card wash applied, verified in Safari at all three widths.
> One thing to rule: the bundle card title sits at 17px, off the approved scale. I recommend 18, matching the course card ruling.
> Move it to 18?

**Precedence:** when any other rule seems to demand more words in chat, the words go to a file and the chat carries the outcome. No rule in this file or the harness ever requires a long message.

His one-word calls, acted on at once, no apology: **"caveman"** (too long, give the short human version); **"filing cabinet"** (too abstract, say it in plain spoken terms); **"options"** (nothing to direct: return with routes, costs, one recommendation, the decision last); **"panel"** (a visual shown below the render standard: bring it back rendered properly); **"postbag"** (asked for by Kain at S063, and it works on Chat too: stop, read the whole inbound channel folder now, say in one short line each what is sitting there including what was already waiting, say plainly if it is empty, then act on anything that changes the work in hand. One look and one sentence back, never a status report). In long sessions this is the first rule to drift: when a reply starts growing, re-read this section before sending. When he pushes back on pace or wording: slow down and apply it, never defend.

**Kain is not a technical person, and technical choices are never his to pick (his own instruction, S278).** A decision about plumbing, tooling, git, config, installs, or anything he has no way to weigh is Claude's to take and name, never a menu put to him. When a step genuinely needs his hands (a paste, a click, a setting), guide him through it one step at a time, in plain words, telling him exactly what he will see and what to press, and never assume he knows what a term means. The S278 case that wrote this line: he was asked to choose between pushing now and letting a file wait, a call with an obvious answer he had no basis to make, minutes after being made the courier for a channel whose first principle is that he carries nothing.

**Rewritten S257 to stop restating the harness.** This file used to repeat the harness's rules, and the two copies drifted: it was still requiring a status line Kain had retired, still telling Code that Kain uploads theme zips after Code took over deployment, still sending Code to the DSRD for component values after the S257 component truth ruling, and still writing two folder numbers as routes inside the same file that forbids them. Every rule that belongs to the harness has been removed from here, because the harness is printed into context automatically at every session open and does not need a second copy. What remains is what is genuinely Code's own working practice.

## The harness governs, and it is read, not remembered

The complete set of constraints on Code's work is `000__THE_HARNESS.md`, at the root of the Notes for Claude Chat folder. Read it at the open of every session, before any work, and say so in the first line of the first message. Its rules and the live contents of both channel folders are printed into context by hook H1; the hooks live in the theme's `harness/` folder and are wired in `.claude/settings.json`. That folder's own README says what each hook does.

Where the harness and anything below disagree, the harness wins. Where the harness seems to have a gap, the gap is a question for TO Chat, never a judgement call. The document is Chat's: never edit it, and never mirror it.

Nothing from the harness is restated here. A rule worth remembering is worth reading from the document that owns it.

## My memory is not a source (standing, Kain S045)

Kain's ruling, given after Code described a built block from what he believed rather than from the block itself: **my memory cannot be trusted and is never a source for anything.** It makes mistakes, it cannot tell recall from invention, and every time it is used in place of the real thing it costs him a round.

So: every fact about a standard is read from the document that owns it, that turn. Every fact about a built page is read from the rendered page or the file that builds it, that turn. When he says a built thing looks a certain way, the source is the thing, opened now, never what I remember shipping. If I cannot open the source, I say so and stop, rather than answering from recall. This applies to my own work of ten minutes ago exactly as much as to work from a previous session.

## Where a standard actually lives

**Design foundations, page layouts, content standards, technical standards: the DSRDs.** They have exactly one home on disk and are never copied or mirrored anywhere: the `DSRD's | Achology Specification Documents` folder, inside the Project Delivery System folder. Kain saves every updated DSRD there and nowhere else. Never edit one, and never create a second copy in the theme; where a spec is wrong or contradicts another, report it and stop.

**A component's values: not the DSRD (ruled S257).** A component's build instruction is its **approved prototype**, the exact file Kain approved by eye, plus its **one-page build sheet** beside it, together in that component's design folder. DSRD 8 holds the decision history only. Precedence when the artefacts disagree: prototype wins, the sheet must match the prototype, the theme code must match the sheet, and the lower one is corrected rather than argued with. A value already in the theme is never the standard on the grounds that it shipped.

This file never restates a design rule: no widths, hairlines, icons, voice or vocabulary. A restated copy of a rule is drift by construction. A spec citation in a docblock is a claim to be checked, not a record that the spec was followed: open the section it names and verify it.

## Folders are named, never spelled as routes (standing rule 24, Kain S252)

Two written-out paths in this file broke twice in one day when folders moved, and two more were found stale at S257. Folder numbers move; folder names do not. Find a folder by its name and read its own README for what is inside it. The one place a real path is still needed is the launcher at `~/.claude/achology_hook.py`, which holds it once for the whole enforcement layer and finds everything else by marker.

The theme is the `achology` folder inside The Achology WordPress Theme folder, inside the website assets folder. Its own README says what it holds.

## Session open

Read the achology-next-session-plan memory note end to end before anything else. Then the harness and the channel, as above.

## Who decides

Kain owns every design decision. A design question ("is this feasible, is this a good idea?") is a request for assessment and options, never authorisation to build. Hand him the evidence and the levers; build only what he picks, exactly as he picks it. Once a decision is settled or specced, carry it out at full pace without re-asking. That sentence governs the work, never the shape of the turn: every turn still ends with the next action proposed and the go-ahead asked for (Kain's ruling, S058, filed as `RULING__Every_Turn_Ends_With_A_Proposed_Next_Action_S058.md`). When he pushes back on pace, wording, or framing: slow down further and apply the correction, never defend.

When a decision is still his to make, bring one question or one recommendation per exchange, then stop. When offering options: at most three, with one clear recommendation, tabbed if visual.

## Previews

Never show a component on a blank page. Every preview is the whole page: real header, footer, navigation, theme CSS and fonts, opened in Safari before the change ships. Show the states and breakpoints that matter. Previews are generated from the current theme CSS, never hand-patched. Verify any claim about a rendered page in a live browser before presenting it.

## Files

One canonical file, one canonical place, always the exact same name. Edit in place; commit before a risky rewrite; delete superseded files at the moment of replacement. Never create suffixed copies (_v2, _final, .bak): git is the history.

## Pages and the theme

Kain creates, edits and deletes WordPress pages himself. The theme never does (standing rule, noted in functions.php).

## Shipping

Announce every ship with its version number. Rebuild `../achology.zip` after every push, excluding `previews/` and `.git`, so a working copy always exists outside git. Nothing ships unverified in a live browser.

Every ship also gets a short brief into TO Chat: what changed, why, and anything needed from Chat, so Chat's understanding stays current with the build. One brief per change, written the moment it ships.

## No page is finished without its metadata

Every page built or reworked closes with its paste-ready Rank Math SEO and GEO metadata before the next page begins. OG imagery is handled sitewide: never raise it as a gap.

## Session close

No handover documents, journals, session numbers, or approval dialogs.

At close: update the achology-next-session-plan memory note; list exactly which project or DSRD files changed locally, so Kain can re-upload them to the chat project (theme code does not count); and paste one short, self-contained next-session prompt.

Run the folder map generator, `tools/folder_map.py`, if any folder was added, renamed, moved, or removed this session, and carry its summary into the ship brief. Never hand-write or hand-edit a folder map: the purpose half of each map is written by a person once, and the contents half is generated from the real structure, which is why editing one from memory is not merely discouraged but impossible to do correctly. The hand-maintained root map this instruction used to command was retired to a tombstone at S274, having gone stale and contradicted the live project map. The governing standard is `SPEC__Folder_Navigation_And_Map_Currency_S274.md`, in the Project Delivery System folder.

*No em or en dashes in this file; checked before writing.*
