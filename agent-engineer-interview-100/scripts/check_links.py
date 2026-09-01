#!/usr/bin/env python3
"""Check local relative Markdown/PDF links without network access."""
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
pat=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
for md in ROOT.rglob('*.md'):
    text=md.read_text(encoding='utf-8')
    for raw in pat.findall(text):
        target=raw.strip().split('#',1)[0]
        if not target or target.startswith(('http://','https://','mailto:')):
            continue
        target=target.replace('%20',' ')
        dest=(md.parent/target).resolve()
        try: dest.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f'{md.relative_to(ROOT)} -> escapes repo: {raw}')
            continue
        if not dest.exists():
            errors.append(f'{md.relative_to(ROOT)} -> missing: {raw}')
if errors:
    print('LINK CHECK FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print('OK: all local Markdown/PDF links resolve.')
