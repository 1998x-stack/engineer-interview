#!/usr/bin/env python3
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
files=sorted(ROOT.glob('docs/questions/*/q*-*.md'))
errors=[]
if len(files)!=100:
    errors.append(f'expected 100 question files, got {len(files)}')
required=['## 1. 面试官真正想考什么','## 2. Know-Why','## 3. Know-How','## 3A. Production Deep Dive','## 4. Failure Modes','## 5. Trade-offs','## 6. 最小 Eval','## 8. 90 秒回答版本','## 9. 5 分钟深挖版本','## 12. 扩展阅读','## 14. 专业深挖：把“会回答”升级为“会设计”','### 14.4 Fault Injection：如何主动证明系统能扛住坏情况','### 14.5 可证伪实验 / Ablation','### 14.7 Debugging Playbook','### 14.8 Senior / Staff 级回答信号']
ids=[]
for f in files:
    txt=f.read_text(encoding='utf-8')
    if len(txt) < 8000: errors.append(f'{f}: content too short for v1.1 ({len(txt)} chars)')
    if '> **内容分层**' not in txt: errors.append(f'{f}: missing provenance banner')
    m=re.search(r'^id:\s*(q\d{2,3})$',txt,re.M)
    if not m: errors.append(f'{f}: missing id')
    else: ids.append(m.group(1))
    for x in required:
        if x not in txt: errors.append(f'{f}: missing section {x}')
    for link in re.findall(r'\]\(([^)]+\.md)\)',txt):
        if link.startswith('http'): continue
        target=(f.parent/link).resolve()
        if not target.exists(): errors.append(f'{f}: broken link {link}')
expected={f'q{i:02d}' for i in range(1,101)}
if set(ids)!=expected:
    errors.append('question ids are not exactly q01..q100')
if errors:
    print('\n'.join('ERROR: '+e for e in errors[:200]))
    sys.exit(1)
print(f'OK: {len(files)} question files; all required sections and checked links pass.')
