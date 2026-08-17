# Claude Code ↔ Claude Chat — message channel

A two-way mailbox. Both Claudes have direct filesystem access to this folder and read/write it themselves.

## The two directions
- **TO Chat (Code writes → Chat reads)** — Claude Code writes notes here. Claude Chat reads them directly.
- **FROM Chat (Chat writes → Code reads)** — Claude Chat writes replies here. Claude Code reads them directly.
- **Archive/** — handled messages, moved out of the way.

## The rules
1. **Each Claude, at session start:** check its inbox (`TO Chat` for Code, `FROM Chat` for… no — Code reads `FROM Chat`, Chat reads `TO Chat`). Read anything new, act on it or reply.
2. **Replies** are written to the other side, one file per topic, self-contained.
3. **When a message is dealt with**, move it to `Archive/` so the inboxes only ever show live items.
4. **Nobody carries files.** Both Claudes read and write these folders directly. The channel is asynchronous, not live: a message waits in the inbox until the other Claude's next session opens and checks it. Kain does not move messages — he starts the sessions in which they're read.

## Standing truth
Neither Claude can see the other's conversation. These files are the ONLY shared context — every message must stand alone, with full context and no assumed knowledge.

## The two machines, and what iCloud does to this channel (recorded S271)

**Claude Chat and Claude Code do not run on the same computer.** This folder reaches both of them through iCloud Drive. Verified at S271: work Code committed on his machine at 23:33 was readable from the other one the following morning.

Four things follow, and each one has a shape worth recognising rather than debugging from cold.

**One. The channel is not instant.** A file written at the end of a session has to upload from one machine and download to the other. If an inbox looks emptier than the other side says it should be, wait and look again before concluding the file was never written.

**Two. A file can be present and still unreadable.** With Optimise Mac Storage switched on, iCloud may keep a file's name and remove its contents from the machine, leaving a placeholder. Finder shows the file; a script that opens it finds a stub whose name ends `.icloud`, or nothing at all. That is not a missing file and it is not a fault in either Claude.

**Three. Two machines editing one file makes two files.** iCloud keeps both and puts a number on the end of one name. A file appearing with a 2 in its name is that, not a duplicate anybody wrote. What keeps it rare is the existing division of ownership: Chat writes the specification documents, Code writes the theme.

**Four. Desktops are not in here.** Nothing the two Claudes pass between them ever lives outside this project folder. The one deliberate exception is a credential, which stays on the Desktop of the machine that runs Claude Code precisely because this folder is shared and a password should not be copied between machines.

**One consequence outside the channel.** The theme's working copy sits inside this synced folder, so its version control internals sync too. GitHub holds the true copy, so the recovery from any damage there is a fresh clone rather than a rebuild.

---

## What belongs in this folder, and what does not (added S276, per the folder navigation specification)

**Belongs:** messages between the two Claudes, and the three harness documents that govern how each side works. Nothing else.

**Does not belong:** the things the messages are about. A specification, a design, a data file or an asset lives in the folder that owns it, and a channel message names that folder rather than carrying a second copy of the thing. A message that carries the artefact instead of pointing at it creates two copies of one truth, which is the failure the whole delivery system is built against.

**The Archive keeps its map, deliberately.** Every other archive in the estate goes unmapped because nobody searches it. This one is the exception: live rulings and load-bearing facts land in it and are then unfindable without one.

<!-- FOLDER MAP: EVERYTHING BELOW THIS LINE IS GENERATED. DO NOT EDIT BY HAND. -->

### Subfolders

- **Archive** (448 loose files)
- **FROM Chat (Chat writes → Code reads)** (11 loose files)
- **TO Chat (Code writes → Chat reads)** (5 loose files)

### Loose files at this level

- 000__THE_CHAT_HARNESS.md
- 000__THE_HARNESS.md
- HOW THIS CHANNEL WORKS.md
- READ ME FIRST — Chat, set yourself up.md
