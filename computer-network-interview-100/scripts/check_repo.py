#!/usr/bin/env python3
from pathlib import Path
import re, json, sys
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'manifest.json').read_text(encoding='utf-8'))
files=[]
for c in manifest['chapters']:
    for q in c['questions']:
        p=root/q['path']
        if not p.exists(): raise SystemExit(f'MISSING: {q["path"]}')
        text=p.read_text(encoding='utf-8')
        required=['30 秒标准回答','深度解析：Know-How + Know-Why','二次深化','面试官常见追问','高频易错点','动手验证 / 抓包实验','面试评分 Rubric','权威资料 / 延伸阅读','关联题目']
        for x in required:
            if x not in text: raise SystemExit(f'{p}: missing section {x}')
        files.append(p)
if len(files)!=100: raise SystemExit(f'Expected 100 question files, got {len(files)}')
ids=[]
for p in files:
    m=re.search(r'^id:\s*(\d+)\s*$',p.read_text(encoding='utf-8'),re.M)
    if not m: raise SystemExit(f'{p}: no id')
    ids.append(int(m.group(1)))
if sorted(ids)!=list(range(1,101)): raise SystemExit('Question ids are not exactly 1..100')
if not (root/'book'/'计算机网络面试100题_专业详解版_2026.pdf').exists(): raise SystemExit('Source PDF missing')
print('OK: 100 question markdowns + source PDF + required sections')
