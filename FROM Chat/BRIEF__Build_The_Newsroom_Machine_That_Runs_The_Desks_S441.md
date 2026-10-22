> CODE DISPOSITION, S181: WAITS ON the file pieces/CQ018-016-1/inputs/commission.md existing in the newsroom machine's folder, with the ASK's item 1 ruled and ~/.achology/anthropic_api_key present on the iMac Pro (the proof run). The machine is built, tested at no cost and backed up: TO Chat/DONE__The_Newsroom_Machine_Built_S181.md; the gaps are in TO Chat/ASK__The_Newsroom_Machine_Gaps_In_The_Cards_S181.md.

> CODE DISPOSITION, S180: WAITS ON the iMac Pro factory session (S181), which runs it after the fact checker setup; the brief places the machine on the iMac Pro.

For Code (factory session, after the second fact checker setup): build the newsroom machine that runs the 23 approved desk cards in order, assembles each desk's packet from the map, reads each verdict word, runs the redraft gate, and keeps the weekly numbers; and add the free machine-writing detector the copy editor's card expects.

# BRIEF: build the newsroom machine that runs the desks (Chat, S441, 22 October 2026)

Read from the vault first: in the Blueprint, the method How a Piece Moves From Request to Signature, Is Sent Back With Reasons, and Comes Out the Same Every Time (the loop, approved today), the 00 Desks Index and every desk note's run card in 01 Desks (all approved today); in the Newsroom, 00 THE MAP, its reading tables and its new section What each desk reads, measured for a quote page.

Model line: Code's own factory session on Opus 5.5 at xhigh, building the machine; each desk runs on the model and effort the model map (Working Papers) gives it, and never a bigger one.

## What Kain asked

Kain, Session 441: "I'm also a great believer in not putting off until tomorrow what we could otherwise do today ... is this something that we can just commission right now?" The cards are the instructions; this is the machine that carries them out. Nothing in the Machine folder does it yet (Chat searched it today).

## Where it runs

On the iMac Pro (64 GB), beside Ollama and the free fact checker, so the machine calls the local checker directly (Kain's yes, Session 441, after Code found the 2019 iMac has 8 GB). The desks themselves call the Anthropic API, so this costs nothing extra in power.

## What the machine does

1. **Assembles each packet** from the desk's reading list (the desk note's Reads and the map's row for the kind), with the piece's own files the card names. It refuses a packet that names a missing or unapproved note, stamps the packet's head with the date, the Content Standard's version, the model and the card's version, and counts its words. The tool `reading_list_counts.py` in the Working Papers' tools folder and `reading_lists.json` beside the step 8 drafts already resolve the lists; build on them.
2. **Runs each desk fresh,** a new call with the card's brief word for word and the packet and nothing else, at the map's model and effort, with thinking on for every judging desk.
3. **Reads each verdict from the word on the last line** of the record, with punctuation and bold marks removed. A record whose last word is UNSURE stops the piece and sends it to Chat. A record with no allowed word is run once more, fresh; a second makes the piece HELD.
4. **Runs the desks in the index's order,** with the routes the index names (the clean-up skips request, demand, topical and research; the teaching desk runs only where a lecture is named).
5. **The redraft gate** is code: it reads every checking desk's last word and the legal desk's; on any FAIL it hands the writer the piece, every desk's reasons and the same packet, once; the checking desks rerun fresh; a second fail is HELD. A legal HOLD goes to Chat whatever the others found. A piece marked KAIN READS THIS PAGE goes to the signature desk whole.
6. **The sample desk's five** are chosen by the machine: UNSURE pieces Chat decided, then rewritten pieces, then the narrowest passes, then random.
7. **Keeps every record** with the piece: each desk's full record, the packet's stamp, the model and the card version.
8. **The weekly numbers:** for each desk, its catch rate and false fail rate against Kain's verdicts at the signature desk, reported apart, its UNSURE count, the count of pieces that reached each stance through a partial connection, and whether it has cleared the bar (at least 20 pages Kain read, 9 in 10 caught, no more than 1 in 10 good pages failed). A change to a desk's model, card or packet notes restarts its count.
9. **The machine-writing detector** the copy editor's card names: a free one that runs on the Mac, chosen by you, flagging rather than failing until its false alarm rate on Kain's own writing is measured. Say which you chose and why.
10. **Runs the stance gap scan before commissioning** for every book note, quote page and workbook, puts each nearest stance with its reaching sentence into the commissioning packet, never holds a piece on the scan's result, and counts each week how many pieces reached each stance through a partial connection, for Chat to bring to Kain (Kain's ruling A Missing Stance Never Blocks a Piece, Session 441).

## How it is proved

Run it first on one quote page, golden page 9 (CQ018-016-1) with a commission and a research file Chat supplies, by the proof's step. Every desk's packet is opened by Chat before the run; the counts are written into the map's desk table beside the measured ones; a count that grows by more than a fifth is named to Kain. The machine's cost per piece is measured on that run and reported, because the gate's line 5 is set from it.

## What comes back

A DONE file: where the machine lives, how to run one piece, the first run's records, each packet's count, and the cost per piece; plus the detector chosen.

Signed by Kain, 22 October 2026, in Chat's Session 441, on commissioning the open items today: "is this something that we can just commission right now?"

OWED BACK: the DONE file.

*No em or en dashes in this file; checked before writing.*
