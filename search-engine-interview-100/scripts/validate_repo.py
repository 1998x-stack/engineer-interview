#!/usr/bin/env python3
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
qfiles=sorted((ROOT/'docs/questions').glob('*/Q*.md'))
errors=[]
if len(qfiles)!=100: errors.append(f"expected 100 question files, got {len(qfiles)}")
ids=[]
for p in qfiles:
    t=p.read_text(encoding='utf-8')
    m=re.search(r'^id:\s*(Q\d{3})$',t,re.M)
    if not m: errors.append(f"missing id: {p}"); continue
    ids.append(m.group(1))
    if len(t) < 2500: errors.append(f'too short (<2500 chars): {p.relative_to(ROOT)}')
    required=['## 30 秒回答','## 5 分钟深度回答','## 进一步深挖：从“会答”到“能做”','## 高频失分点 / Gotcha','## 实战练习','## 一句话记忆','## 参考资料']
    for h in required:
        if h not in t: errors.append(f'missing section {h}: {p.relative_to(ROOT)}')
    for link in re.findall(r'\[[^]]+\]\(([^)]+)\)',t):
        if link.startswith(('http://','https://','#')): continue
        target=(p.parent/link).resolve()
        if not target.exists(): errors.append(f"broken link {link} in {p.relative_to(ROOT)}")
expected=[f"Q{i:03d}" for i in range(1,101)]
if ids!=expected: errors.append(f"IDs mismatch: first={ids[:3]} last={ids[-3:]}")
manifest=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
if len(manifest)!=100: errors.append('questions.json must contain 100 rows')
for row in manifest:
    if not (ROOT/row['path']).exists(): errors.append(f"manifest path missing: {row['path']}")

# Validate local links across all Markdown files
all_md_files=list(ROOT.rglob('*.md'))
for p in all_md_files:
    t=p.read_text(encoding='utf-8')
    for link in re.findall(r'\[[^]]+\]\(([^)]+)\)',t):
        link=link.split('#',1)[0]
        if not link or link.startswith(('http://','https://','mailto:')): continue
        target=(p.parent/link).resolve()
        if not target.exists(): errors.append(f'broken repo link {link} in {p.relative_to(ROOT)}')

if errors:
    print('VALIDATION FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print(f'OK: {len(qfiles)} questions, links and manifest validated')
