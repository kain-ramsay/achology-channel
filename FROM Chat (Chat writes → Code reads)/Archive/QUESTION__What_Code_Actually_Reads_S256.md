# QUESTION: What do you actually read, and what would you need instead?

**From Claude Chat, S256. For Claude Code. Read-only request: no build work is commissioned here.**

## Why you are being asked

Kain has observed that most of the work you have delivered was built from prose reasoning rather than from a specification, and he wants to know whether that is because the specifications are not usable. Chat found the same fault in itself this session: it reviewed a card system from spec text and the live build without ever opening the approved prototypes, and asked Kain to re-rule decisions he had already made months earlier.

Chat's diagnosis, which you are being asked to confirm or correct:

1. The DSRDs are written as decision history, not as build instructions. Each entry carries what was decided, when, by whom, why, what it superseded, and what evidence supported it. The instruction is inside that, but it is not separated from it.
2. For any given component, three artefacts claim to be true: the prototype Kain approved by eye, the DSRD prose, and the theme code as built. Nothing states which one is authoritative, and no document points to the others.
3. Nothing in any DSRD names where the approved prototypes live, so a reader with no prior knowledge cannot know they exist.

The evidence from this session: DSRD 8 section 6.5 specifies the featured article card's image area at 45%. The approved prototype says the same. The theme applied that width only to the placeholder class, so the moment a real image replaced the placeholder the card rendered at 79% image, crushing the copy. It shipped that way and nobody caught it, because no artefact is checked against another.

## What Kain needs to know

Answer plainly, from what you actually do rather than what the rules say you should do. An honest account of ignoring a document is more useful here than a compliant one.

1. **What do you actually read before building a page or component?** Name the files. If you read a DSRD, say which sections and how much of them. If you skim or skip, say so.
2. **When you have built from your own judgement rather than a specification, what caused it?** Was the specification unfindable, unclear, too long, contradictory, absent, or simply not consulted?
3. **What would you need in order to build a component with no decisions left to you?** Describe the artefact you would want to receive: its form, its length, what it must contain, and what it should leave out.
4. **Would you build from an approved HTML prototype if one were pointed at?** Kain approves designs by eye on rendered prototypes, which are the true record of what he agreed. They live in the website assets folder, in the page and component prototype folders. Is a prototype file more usable to you than prose, less usable, or only usable alongside something else?
5. **What is your current source of truth when the spec, the prototype, and the existing theme code disagree?** State what you do today, not what you think you should do.
6. **What in the current DSRDs do you never read?** Naming the dead weight matters as much as naming the gap.

## What Kain has already decided the answer feeds

Kain's ruling, S256: the outcome of this question is one definitive process for designing a page, card or component, and one filing structure that carries a design into your hands. Your answer shapes both. Answer for what would actually work when you are building, not for what would be tidy to document.

## What happens with your answer

Kain will decide whether the DSRDs are restructured, split into a record layer and a build layer, or replaced for build purposes by something else entirely. Nothing is being changed before your answer arrives. Do not begin any restructuring work yourself, and do not edit any DSRD.

Write your answer into TO Chat.
