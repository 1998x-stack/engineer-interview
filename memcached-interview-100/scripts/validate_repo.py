#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
files=sorted((root/'docs').glob('[0-9][0-9]-*/*.md'))
qs=[p for p in files if p.name!='README.md']
errors=[]
if len(qs)!=100: errors.append(f'expected 100 question markdowns, got {len(qs)}')
ids=[]
required=['## 题目','## 30-90 秒标准回答','## 深度机制','## 源码导航','## 常见易错点','## 高频追问','## 动手验证','## 官方参考']
for p in qs:
    text=p.read_text(encoding='utf-8')
    m=re.search(r'^id:\s*(\d{3})$',text,re.M)
    if not m: errors.append(f'{p}: missing frontmatter id'); continue
    ids.append(int(m.group(1)))
    for sec in required:
        if sec not in text: errors.append(f'{p}: missing {sec}')
    for link in re.findall(r'\]\((\.\.?/[^)#]+\.md)\)', text):
        target=(p.parent/link).resolve()
        if not target.exists(): errors.append(f'{p}: broken link {link}')
if sorted(ids)!=list(range(1,101)): errors.append('question IDs are not exactly 001..100')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print('OK: 100 question files, required sections and internal markdown links validated.')
