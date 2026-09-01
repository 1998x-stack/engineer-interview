#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
qfiles=sorted((ROOT/'questions').glob('[0-9][0-9]-*/*.md'))
qfiles=[p for p in qfiles if p.name!='README.md']
errs=[]
if len(qfiles)!=100: errs.append(f'expected 100 question files, got {len(qfiles)}')
nums=[]
required=['面试官为什么问','30 秒结论','3 分钟标准回答','Know-how','高频追问','常见失分点','面试评分 Rubric','自测','一句话记忆','题源与可信度','延伸阅读']
for p in qfiles:
    m=re.match(r'(\d{3})\.md$',p.name)
    if not m: errs.append(f'bad filename: {p}') ; continue
    nums.append(int(m.group(1)))
    txt=p.read_text(encoding='utf-8')
    for x in required:
        if x not in txt: errs.append(f'{p}: missing section {x}')
    for rel in re.findall(r'\]\((\.\.?/[^)#]+\.md)\)',txt):
        target=(p.parent/rel).resolve()
        if not target.exists(): errs.append(f'{p}: broken link {rel}')
if nums!=list(range(1,101)): errs.append(f'question ids not continuous: {nums[:5]}...{nums[-5:]}')
if errs:
    print('\n'.join('ERROR '+e for e in errs)); sys.exit(1)
print('OK: 100 questions, required sections present, internal question links valid.')
