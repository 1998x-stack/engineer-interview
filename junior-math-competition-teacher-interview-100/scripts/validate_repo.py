#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
qfiles=[p for p in (ROOT/'questions').rglob('q*.md') if re.match(r'q\d{3}-',p.name)]
errors=[]
if len(qfiles)!=100: errors.append(f'expected 100 question markdown files, got {len(qfiles)}')
ids=[]
required=['## 0. 30 秒快速作答卡','## 1. 面试定位与前置能力','## 2. 深度分析：为什么这条路最自然','## 3. 完整标准解 / 高分回答','## 4. 教学化转译','## 5. 常见错误、根因与纠错','## 6. 面试追问：逐题实答','## 7. 变式设计与迁移训练','## 8. 面试官评分 Rubric','## 9. 刻意练习与复盘']
for p in qfiles:
    text=p.read_text(encoding='utf-8')
    if len(text) < 5000: errors.append(f'{p}: content too short for v2 deep standard ({len(text)} chars)')
    m=re.search(r'^id: Q(\d{3})$',text,re.M)
    if not m: errors.append(f'{p}: missing id')
    else: ids.append(int(m.group(1)))
    for sec in required:
        if sec not in text: errors.append(f'{p}: missing {sec}')
if sorted(ids)!=list(range(1,101)): errors.append('question IDs are not exactly Q001-Q100')
js=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
if len(js)!=100: errors.append('questions.json does not contain 100 records')
pdfs=list((ROOT/'book').glob('*.pdf'))
if len(pdfs)!=1: errors.append(f'expected exactly one PDF, got {len(pdfs)}')
if errors:
    print('VALIDATION FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print(f'OK: {len(qfiles)} question files, IDs Q001-Q100, JSON={len(js)}, PDF={pdfs[0].name}')
