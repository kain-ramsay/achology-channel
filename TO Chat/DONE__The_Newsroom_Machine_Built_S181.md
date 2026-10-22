Needs from Chat: read where the machine lives and how to run one piece, open the packets before the proof run, and answer the ASK that names what the proof waits on (`ASK__The_Newsroom_Machine_Gaps_In_The_Cards_S181.md`).

# DONE: the newsroom machine is built, tested at no cost, and backed up; its proof run on golden page 9 waits on two inputs (Code S181, factory, iMac Pro, 22 October 2026)

Answers `BRIEF__Build_The_Newsroom_Machine_That_Runs_The_Desks_S441`. Built, not yet proved: the brief's proof is one spending run on golden page 9, and that waits on the ASK's items 1 and 2. So the brief stays in FROM Chat with a WAITS line.

## Where it lives

- **The live files:** `newsroom_machine` in the Machine room of The Achology Newsroom folder: `newsroom.py`, `desk_scripts.py`, `detector.py` and a README. iCloud carries them between the Macs.
- **The off-machine copy:** the private GitHub repository achology-newsroom. Kain renamed it from achology-factory in this session. The copy was pushed by `publish_factory_copy.py` as commit 9bd5227, and the remote head was read back and matched.
- **The run records:** each piece's records live in `newsroom_machine/pieces/<id>`. They are run output, so the GitHub copy leaves them out.

## How to run one piece

    python3 newsroom.py new --id CQ018-016-1 --record <record> --commission <commission> --research <research file>
    python3 newsroom.py packets --piece CQ018-016-1          every packet, its count and its stamp; nothing sent
    ~/.achology/venv/bin/python newsroom.py run --piece CQ018-016-1 --from first-objectivity --go --max-usd 10

The README in the folder has every command, including `decide` (Chat settles an UNSURE), `sign` (Kain's verdict), `sample` and `weekly`.

## What it does, item by item against the brief

1. **Packets.** Assembled from `reading_lists.json` and the piece's files. A missing or unapproved note is refused, with every reason named. The head is stamped with the date, Content Standard 32, the model, the effort and the card's version (its approval lines and a hash of the run card). The words are counted. A count more than a fifth over the measured one is printed to name to Kain. Built.
2. **Each desk runs fresh**, with the card's brief read word for word from the vault at run time. The model and effort come from the model map's row, thinking is on, and the packet goes in with nothing else. Built; not yet run against the API.
3. **Verdicts are read from the last line's word**, punctuation and bold removed. UNSURE stops the piece for Chat. A record with no allowed word runs once more, fresh, and a second makes the piece HELD. Built and tested.
4. **The index's order and routes.** Teaching runs only where a lecture is given. The clean-up skips research. The machine stops before the people's desks. Built and tested.
5. **The redraft gate as code.** One redraft carries every failing desk's reasons. A second fail is HELD. A legal HOLD goes to Chat whatever the others found. KAIN READS THIS PAGE is carried forward. Built and tested.
6. **The sample desk's five:** Chat-decided UNSURE pieces first, then rewritten pieces, then the narrowest passes, then random from a recorded seed. Built and tested. How a "narrowest pass" is recognised is the ASK's item 10.
7. **Every record kept with the piece:** each packet, each desk's full record with its stamp, the model, the card version, the usage and the cost. Built.
8. **The weekly numbers:** catch rate and false fail rate apart, the UNSURE count and the bar. A change to a desk's model, card or packet notes restarts its count. Built; there is no data until Kain signs pieces.
9. **The detector**, below.
10. **The stance gap scan:** not built. It has no model map row (ASK item 5). The weekly count of partial connections is built and reads any scan results.

## The proof so far, at no cost

- **The machine's self-test:** every verdict word checked against its own card, every brief read word for word, every desk's model map row found, and the verdict and route rules. All pass.
- **A simulated run of six pieces, with made-up answers and no API call:**
  - a clean page passed the gate;
  - a page failed by the fact checker was rewritten once and passed in round 2;
  - a page failed twice by the stance editor was HELD;
  - an UNSURE stopped the piece for Chat;
  - a legal HOLD went to Chat;
  - two records with no allowed word made the piece HELD;
  - the sample picked the two rewritten pieces first.
- **The scripts on golden page 9's published text:**
  - copy editor: no fails; one watched word ("permission"); closing question 86 characters (band 79 to 89); the author named twice;
  - originality: no shared runs with the sources; 20 common runs listed once; 71 pages sharing a rarer run, the nearest being a draft article that quotes this page's own quote.

**Packet counts measured today**, against the map's measured table:

| Desk | Vault words today | Measured | Change |
|---|---|---|---|
| search | 5,306 | 4,931 | up 7.6 per cent |
| legal and safety | 2,226 | 2,034 | up 9.4 per cent |
| cold reader | 0 | 0 | none |
| teach-back reader | 0 | 0 | none |

The rest cannot be built until the commission names its stances and the ASK's item 1 is settled. None measured so far grew by a fifth.

**The cost per piece is not measured yet.** It needs the spending run. Nothing was spent in this session.

## The detector chosen, and why

**Binoculars** (Hans and others, 2024; BSD 3-Clause), run on Qwen2.5-1.5B and Qwen2.5-1.5B-Instruct (Apache 2.0), on this Mac's processor through PyTorch 2.2.2, the last build for an Intel Mac. It is in its own Python, `~/.achology/detector_venv`.

**Why this one:**
- It needs no training data and no account.
- Its licence allows business use.
- In a 2026 comparison it made the fewest false alarms on human writing, which matters most while it only flags.
- It takes about 25 seconds a page here, models loaded.

**Its weakness, plainly:** no published figure covers Claude's writing, and one benchmark put it near chance on an older Claude model. So it flags and never fails until it is calibrated on Kain's own writing (ASK item 12). Golden page 9 scored 1.0464, uncalibrated.

The fallback, if calibration shows it useless, is Fast-DetectGPT (MIT licence), in the same Python.

## Also done in this session

- **The H2 declaration file**, built to Chat's NOTE answer 2: `DONE__H2_Reads_A_Declaration_File_S181.md`, in the channel Archive.
- **`publish_factory_copy.py`** now points at achology-newsroom, picks the SSH address this Mac can push by, and copies the newsroom machine, the fact check trial, the pack kits, the workbook build tool, the packs from their new home and the rule documents from theirs.
- **The folder maps** were regenerated for the new folder.

OWED BACK: after the ASK is answered, the proof run's records, each packet's count and the cost per piece, in a REPORT.

*No em or en dashes in this file; checked before writing.*
