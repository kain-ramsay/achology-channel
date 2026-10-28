> CODE DISPOSITION, S194: WAITS ON a factory session (gate work; this theme menu session touches no gate file).

**For Code: add one new kind of page, somap-article, to the content gate and the vault gate, so that SoMAP's articles can travel the Newsroom's road. No page is built or imported yet.**

**Why.** Kain has agreed the plan for a new SoMAP website (Session 450, 28 October 2026), with a library of about 100 articles: 48 live at launch and 52 released weekly for the year after. He has approved fourteen SoMAP stances and signed the SoMAP Article Pack, which sets out how these pieces are written. Both are in the SoMAP project folder (0004. Society of Modern Applied Psychology), in its 04. SoMAP Editorial Pack folder. The pack's Gate type and records line asks for this change before the first batch.

**What to add.**

1. A content records folder for the kind, named somap-article, in The Stock's Content Records.
2. In the content gate's standards file, an entry for somap-article: required fields as for the article kinds, the shared banned, flagged and watched lists, and the limits the pack sets (no sentence over 40 words; paragraphs of three to six sentences; no price, student count or rating; no course link). Four shapes within the kind, carried as a field: explainer (1,200 to 1,800 words), practice piece (1,500 to 2,000), position statement (800 to 1,200) and report (2,000 to 3,000).
3. In the vault gate, the kind added to its list, reading the SoMAP Article Pack and the SoMAP stances from the SoMAP project folder as its pack and stance notes, so a brief for a SoMAP batch is built from them and never from Achology's article pack alone.
4. One rule the gate checks on this kind only: the words helper and helpers never appear outside the title The Skilled Helper, and no sentence says a practitioner refers someone on (Kain, Session 450).

**Done when** `vault_gate.py build --kind somap-article` builds a brief from the SoMAP pack and stances for a test pages file, and `content_gate.py` passes a short test record of each of the four shapes and fails one that uses helper.

**Nothing needed from Chat or Kain** before this is built. The SoMAP website itself is a later build with its own brief.
