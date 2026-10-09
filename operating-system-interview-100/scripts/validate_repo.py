#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
files=sorted((ROOT/'questions').glob('*/q*.md'))
errors=[]
if len(files)!=100: errors.append(f'expected 100 question files, got {len(files)}')
nums=[]
for p in files:
    m=re.match(r'q(\d{2,3})\.md$',p.name)
    if not m: continue
    n=int(m.group(1)); nums.append(n)
    text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'): errors.append(f'{p}: missing frontmatter')
    if f'id: "Q{n:02d}"' not in text: errors.append(f'{p}: wrong/missing id')
    if f'# Q{n:02d} ' not in text: errors.append(f'{p}: missing title heading')
if sorted(nums)!=list(range(1,101)): errors.append('question numbering is not exactly 01..100')

# Validate relative markdown links in repo markdown files (ignore http/https and anchors)
pat=re.compile(r'\[[^\]]*\]\(([^)]+)\)')
for p in ROOT.rglob('*.md'):
    text=p.read_text(encoding='utf-8')
    for target in pat.findall(text):
        target=target.split('#',1)[0]
        if not target or '://' in target or target.startswith('mailto:'): continue
        dest=(p.parent/target).resolve()
        if not dest.exists(): errors.append(f'{p.relative_to(ROOT)} -> broken link: {target}')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print(f'OK: {len(files)} question markdown files, numbering 01..100, internal links valid.')
