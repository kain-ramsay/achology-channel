> **WITHDRAWN BY CHAT, S391, on Kain's instruction: do not run this. Kain downloaded the 29 files himself and is uploading them. Archived unrun.**

**Needs from Code:** run one small script on Kain's skill library folder, approved by Kain at S391. It takes the long dashes out of 29 skill files, keeping every file name exactly as it is. Report the counts.

# BRIEF: take the long dashes out of 29 skill files in the library

**From:** Claude Chat, S391, Tuesday 29 September 2026. **To:** Claude Code.
**Kain's yes, S391:** he asked Chat to put the dash-free skills straight into his skill library folder. Chat cannot write 29 files of up to 70 KB each through the Filesystem connector without running out of room, so the job comes to you as a script.

## Where

The skill library folder in the Project Delivery System (the one holding `session-close-SKILL.md` and its siblings). Change nothing else in it.

## The 29 files, names exactly as they are in the folder

Circle-API-Reference-SKILL.md, ai-collaboration-SKILL.md, author-biography-SKILL.md, book-derived-article-SKILL.md, build-reconciliation-SKILL.md, buyer-intent-answer-SKILL.md, content-factory-SKILL.md, conversation-audit-SKILL.md, honest-capabilities-SKILL.md, instructor-article-SKILL.md, mid-session-capture-SKILL.md, notion-board-management-SKILL.md, notion-registry-audit-SKILL.md, notion-workspace-SKILL.md, page-composition-SKILL.md, priority-interrupt-SKILL.md, problem-interrupt-SKILL.md, problem-solving-SKILL.md, product-based-planning-SKILL.md, production-css-files-SKILL.md, production-html-files-SKILL.md, second-brain-vault-audit-SKILL.md, skill-architecture-SKILL.md, skill-authoring-SKILL.md, thorough-audit-SKILL.md, vault-audit-SKILL.md, vault-reference-SKILL.md, visual-design-craft-SKILL.md, voice-audio-pipeline-SKILL.md.

**Never rename a file.** Kain's standing rule: a skill keeps exactly the name it has in the library.

## The script (Python 3), run in that folder

```python
import re, sys
FILES = sys.argv[1:]
D = '[\u2014\u2013]'
KEEP = re.compile(r'(`[^`\n]*`|\[\[[^\]\n]*\]\])')  # code spans and vault links keep their dashes

def fix(seg):
    t = re.sub(r'(\d)\s*[\u2013\u2014]\s*(\d)', r'\1 to \2', seg)          # ranges: 1-5 becomes 1 to 5
    t = re.sub(r' ' + D + r' ([^\u2014\u2013\n]{1,140}?) ' + D + r' ', r' (\1) ', t)  # paired dashes become brackets
    t = re.sub(r'(?m)^(\s*[-*]?\s*)' + D + r'\s+', r'\1', t)                 # a dash opening a line
    t = re.sub(r'\s+' + D + r'\s*$', ':', t, flags=re.M)                      # a dash ending a line
    t = re.sub(r'(?m)^(#+ [^\n]*?) ' + D + ' ', r'\1: ', t)                   # headings
    t = re.sub(r'(?m)^(\s*[-*] [^\n]{1,80}?) ' + D + ' ', r'\1: ', t)        # list labels
    t = re.sub(r'\*\*\s*' + D + r'\s+', r'**: ', t)                           # bold labels
    t = re.sub(r' ' + D + ' ', ': ', t)                                       # any other spaced dash
    t = re.sub(r'(\w)' + D + r'(\w)', r'\1, \2', t)                           # unspaced dash
    t = re.sub(D, ',', t)
    return t.replace('::', ':').replace(': :', ':').replace(', .', '.').replace(',,', ',')

for f in FILES:
    s = open(f, encoding='utf-8').read()
    before = len(re.findall(D, s))
    t = ''.join(x if KEEP.fullmatch(x) else fix(x) for x in KEEP.split(s))
    after = len(re.findall(D, t))
    open(f, 'w', encoding='utf-8').write(t)
    print(f, before, after)
```

Pass the 29 names above as arguments. Commit the library folder before running, so the change can be undone.

## What comes back, through TO Chat

The script's printout (file, dashes before, dashes after). "After" should be 0 except where a dash sits inside a code span or a vault link, which is kept on purpose (the content skills quote the banned character itself). Then tell Kain in the session that the 29 are ready to upload from the library folder.

*No em or en dashes in this file; checked before writing.*
