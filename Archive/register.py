"""The locked term register, read from the canonical DSRD on every single run.

DSRD 2 section 2.24 carries a table of terms, each with a full identification
used once at first mention and a short identification used thereafter. That table
is the only source. Nothing here is typed from memory and nothing is cached to
disk, because a cached copy is a mirror and a mirror goes stale.

The governing sentences, quoted from DSRD 2 section 2.24, read from the canonical
file:

    "The help section takes the strict form of the front-door rule (DSRD 6 s1).
    No bare acronym is written anywhere in a help article, at any mention. The
    first mention of a term gives its full canonical name with the short form in
    brackets, taken word for word from the register below. Every later mention
    takes the short identification, not the acronym."

    "The wording is copied, never rewritten per article. Identical wording across
    every help page reads as one organisation to a person and as one entity to an
    answer engine."

Usage:
    python3 register.py            print the register exactly as read today
"""
import io
import os
import re

DSRD_2 = os.path.join(
    os.path.expanduser("~"), "Documents", "CLAUDE | Anthropic Ai",
    "Claude Code (Projects)", "Achology Website Upgrade 2026",
    "003. DSRD's | Achology Specification Documents",
    "DSRD 2. Content Production & Knowledge Standards",
    "DSRD_2_Content_Production_and_Knowledge_Standards.md")

HEADER = ("| Term | Full identification, used once at first mention "
          "| Short identification, used thereafter |")


def load(path=DSRD_2):
    """Every row of the register table in DSRD 2 section 2.24, in document order."""
    text = io.open(path, encoding="utf-8").read()
    start = text.find(HEADER)
    if start < 0:
        raise SystemExit(
            "register.py: the table header in DSRD 2 section 2.24 has changed.\n"
            "Do not guess the new shape. Write the finding to TO Chat and stop.")
    rows = []
    for line in text[start:].splitlines()[2:]:
        line = line.strip()
        if not line.startswith("|"):
            break
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 3 or not cells[0]:
            break
        rows.append({"term": cells[0], "full": cells[1], "short": cells[2]})
    if not rows:
        raise SystemExit("register.py: the register read empty. Stop and report it.")
    return rows


BRACKETED = re.compile(r"\(([A-Za-z]{2,8})\)")


def short_forms(row):
    """Every acronym this register row governs, read from the row itself."""
    out = []
    term = row["term"]
    if re.fullmatch(r"[A-Za-z]{2,8}", term) and not term.islower():
        out.append(term)
    for m in BRACKETED.finditer(row["full"]):
        if m.group(1) not in out:
            out.append(m.group(1))
    for part in re.split(r"\s+and\s+", term):
        part = part.strip()
        if re.fullmatch(r"[A-Z]{2,8}", part) and part not in out:
            out.append(part)
    return out


def index():
    """acronym -> its register row, for every acronym the register governs."""
    out = {}
    for row in load():
        for s in short_forms(row):
            out.setdefault(s, row)
    return out


def never_abbreviated(row):
    """A row whose short identification forbids the short form outright."""
    return "never abbreviated" in row["short"].lower()


if __name__ == "__main__":
    rows = load()
    print("The register, read from DSRD 2 section 2.24 just now: %d terms\n" % len(rows))
    for r in rows:
        print("TERM  " + r["term"])
        print("  governs: " + (", ".join(short_forms(r)) or "no short form"))
        print("  full  : " + r["full"][:140] + ("..." if len(r["full"]) > 140 else ""))
        print("  short : " + r["short"])
        if never_abbreviated(r):
            print("  NOTE  : never abbreviated, at any mention")
        print()
