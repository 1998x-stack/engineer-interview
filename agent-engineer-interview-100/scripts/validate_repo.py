#!/usr/bin/env python3
"""Validate structural integrity of the interview repository using stdlib only."""
from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/questions.json'
errors=[]
if not DATA.exists(): errors.append('missing data/questions.json')
else:
    qs=json.loads(DATA.read_text(encoding='utf-8'))
    if len(qs)!=100: errors.append(f'expected 100 questions, got {len(qs)}')
    ids=[q.get('id') for q in qs]
    expected=[f'q{i:03d}' for i in range(1,101)]
    if ids!=expected: errors.append('question ids are not exactly q001..q100 in order')
    required=['q','quick','points','followups','pitfall','why','how','freq','diff','path']
    for q in qs:
        for k in required:
            if k not in q or q[k] in (None,'',[]): errors.append(f'{q.get("id")}: missing {k}')
        p=ROOT/q['path']
        if not p.exists(): errors.append(f'{q["id"]}: missing markdown {q["path"]}')
        else:
            text=p.read_text(encoding='utf-8')
            for heading in ['## 面试官在考什么','## 30 秒回答','## 深挖解析','## 连续追问','## 易错回答','## Know-Why','## Know-How']:
                if heading not in text: errors.append(f'{q["id"]}: missing heading {heading}')
            expanded_required=['## 3 分钟专业展开','## 参考架构 / 控制流','## 状态与接口设计','## Failure Modes：方案最容易坏在哪里','## Trade-off：为什么不能只有一个标准答案','## 可观测性与关键指标','## Production Checklist','## 面试自测']
            for heading in expanded_required:
                if heading not in text: errors.append(f'{q["id"]}: missing expanded heading {heading}')
            if len(text.encode('utf-8')) < 9000: errors.append(f'{q["id"]}: expanded markdown too small')
            # Verify source-data parity: every exact source-derived field must survive in Markdown.
            expected_fragments=[q['q'],q['quick'],q['pitfall'],q['why'],q['how'],*q['points'],*q['followups']]
            for frag in expected_fragments:
                if frag not in text: errors.append(f'{q["id"]}: source fragment missing: {frag[:36]}')
            if q['number']==100:
                follow=q.get('system_design_followups',[])
                if len(follow)!=20: errors.append('q100 must contain 20 system-design followups in data')
                for frag in follow:
                    if frag not in text: errors.append(f'q100: missing system-design followup: {frag[:36]}')
    if sum(1 for q in qs if q.get('priority20')) != 20: errors.append('priority20 count must be 20')
if not (ROOT/'assets/Agent_Engineer_Offer_100_Interview_Handbook.pdf').exists(): errors.append('missing handbook PDF')
if not (ROOT/'README.md').exists(): errors.append('missing README.md')
if errors:
    print('VALIDATION FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print('OK: 100 questions, required sections, priority list and PDF are structurally complete.')
