# RECORD: the pen-name bios and the five URL corrections, complete

**From:** Claude Code, S048. **Date:** 2026-08-06. **Theme:** v0.38.57 to v0.38.59, live.
**Answers:** `BRIEF__Pen_Name_Bios_And_External_Links_S245.md`, all six acceptance criteria.

## The ten live pages, at their final URLs

| # | Page | Opening line |
|---|---|---|
| 1 | https://achologytest.com/about/instructors/amelia-a-sinclair/ | placed |
| 2 | https://achologytest.com/about/instructors/benjamin-lockwood/ | placed |
| 3 | https://achologytest.com/about/instructors/charlotte-j-avery/ | placed |
| 4 | https://achologytest.com/about/instructors/declan-fitzpatrick/ | placed |
| 5 | https://achologytest.com/about/instructors/evelyn-montgomery/ | placed |
| 6 | https://achologytest.com/about/instructors/frederick-s-martin/ | placed |
| 7 | https://achologytest.com/about/instructors/isabella-s-whitmore/ | placed |
| 8 | https://achologytest.com/about/instructors/jackson-p-hartley/ | placed |
| 9 | https://achologytest.com/about/instructors/kain-ramsay/ | n/a, instructor |
| 10 | https://achologytest.com/about/instructors/gerard-egan/ | n/a, instructor |

**Acceptance 6 asks which pages skipped the opening line because the bio already
opened with the name. None did.** All eight pen-name bios opened with a first
name only ("Amelia is...", "Jackson answers..."), never the full name, so
placement rule 1 fired on all eight. Checked one entry at a time rather than
assumed.

**Prof. Egan is the one page with no closing sentence added**, and that is
placement rule 4 working: his bio already named The Skilled Helper, so the link
went onto that existing mention rather than duplicating the sentence.

## Proved against the brief, not read back by me

A checker pulls the approved strings out of the brief itself and compares them
with the live rendered pages, so the claim is a character comparison rather
than my opinion:

```
  amelia-a-sinclair      pass  (intro verbatim, closing verbatim, link on 'The Elements of Style', 0 dashes)
  benjamin-lockwood      pass  (... 'A New History of Western Philosophy')
  charlotte-j-avery      pass  (... 'The Chemical History of a Candle')
  declan-fitzpatrick     pass  (... 'Essays: First Series')
  evelyn-montgomery      pass  (... 'Talks to Teachers on Psychology')
  frederick-s-martin     pass  (... 'The Problems of Philosophy')
  isabella-s-whitmore    pass  (... 'Lombard Street')
  jackson-p-hartley      pass  (... 'Essays')
  kain-ramsay            pass  (intro n/a, ... 'The Ultimate Life Coaching Handbook')
  gerard-egan            pass  (intro n/a, ... 'The Skilled Helper')
  10 of 10 pages pass
```

It also confirms **no bare URL is visible in any bio** and **zero em or en
dashes on any of the ten pages**.

**One checker bug, recorded rather than buried.** The first run failed Egan for
a missing closing sentence. The page was right and the checker was wrong: it
was enforcing a rule the brief explicitly exempts him from. I fixed the checker
to express the brief's actual conditional, rather than "fixing" a correct page
to satisfy a wrong test.

## All ten links resolve

Eight return 200 to an automated request. **Amazon returned 500 and Cengage a
redirect loop**, so rather than report two broken links I opened both in a real
browser: Amazon serves the right book (Ramsay, ISBN 9781544544809) and Cengage
the right edition (11th, 9781305865716). Those two hosts refuse automated
requests. The links are sound, and the distinction between "dead" and "refuses
robots" is worth keeping.

## The five URL corrections

```
  amelia-sinclair    ->  amelia-a-sinclair
  charlotte-avery    ->  charlotte-j-avery
  frederick-martin   ->  frederick-s-martin
  isabella-whitmore  ->  isabella-s-whitmore
  jackson-hartley    ->  jackson-p-hartley
```

Benjamin Lockwood, Declan Fitzpatrick and Evelyn Montgomery have no middle
initial: checked, already correct, left alone, exactly as the brief said to.

**Two places, because the key is the URL.** The registry array key is what
`achology_person_url()` builds the address from, and it also matches the
WordPress page's `post_name`. Both were changed in one pass.

**Nothing pointed at the old five, verified before changing rather than after.**
A grep across every php, js, json and py file found them only in
`people-setup.php`. The database held no postmeta value equal to any of them,
and no `post_content` anywhere containing an old profile URL. That is why no
redirects were needed beyond the brief's own reasoning.

**Proved after, on the live site, rewrites flushed and cache purged:**

- all ten new URLs return **200**
- all five old URLs return **404**
- every link on the Our People hub points at a new URL, read out of the HTML
- the five `post_name` values read back from the database and are correct
- the ten bios still pass the checker at their new addresses, 10 of 10

The bio checker was deliberately run against the **old** five first. It reported
NO BIO SECTION FOUND on all five, which is what a 404 looks like from inside
that script. A 404 nobody has actually observed is a 404 somebody is guessing at.

## Found in passing, filed separately, not fixed

`achology_person_works()` queries the meta key `achology_author`. **The database
has zero rows with that key.** The live data uses `author`, with two rows. So no
article can attribute itself to a profile, and all ten pages show their empty
state. Out of scope for this brief, and filed as
`FINDING__No_Article_Can_Attribute_Itself_To_A_Profile_S048.md`.

## Also still open, from the brief's own note

`QUESTION__Pen_Name_Pages_As_Built.md` is named in this brief as still standing.
It is not in FROM Chat, so I have not answered it. If it still needs answering,
it needs to arrive.

*No em or en dashes in this file; checked before writing.*
