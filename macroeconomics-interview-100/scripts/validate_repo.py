#!/usr/bin/env python3
from pathlib import Path
import re, json, sys
ROOT=Path(__file__).resolve().parents[1]
files=sorted((ROOT/'docs').glob('*/q[0-9][0-9][0-9]-*.md'))
errors=[]
if len(files)!=100: errors.append(f'expected 100 question files, got {len(files)}')
ids=[]
required=['## 1. 这道题真正考什么','## 2. 90 秒标准作答','## 3. 核心公式 / 结构','## 4. 深挖解析','## 5. 专业扩展','## 6. 教授追问','## 7. 常见失分点','## 8. 举一反三','## 9. 面试评分 Rubric','## 10. 关联题目','## 11. 资料与来源']
for f in files:
    t=f.read_text(encoding='utf-8')
    m=re.search(r'^qid:\s*Q(\d{3})$',t,re.M)
    if not m: errors.append(f'{f}: missing qid frontmatter'); continue
    qid=int(m.group(1)); ids.append(qid)
    for h in required:
        if h not in t: errors.append(f'{f}: missing section {h}')
    pm=re.search(r'^pdf_page:\s*(\d+)$',t,re.M)
    if not pm or not (1<=int(pm.group(1))<=78): errors.append(f'{f}: invalid pdf_page')
if sorted(ids)!=list(range(1,101)): errors.append('question IDs are not exactly 1..100')
# lightweight local markdown link checker
for f in list((ROOT/'docs').rglob('*.md'))+[ROOT/'README.md']:
    t=f.read_text(encoding='utf-8')
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',t):
        if link.startswith(('http://','https://','#','mailto:')): continue
        target=link.split('#',1)[0]
        if not target: continue
        p=(f.parent/target).resolve()
        if not p.exists(): errors.append(f'{f}: broken link -> {link}')
# structured index
idx=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
if len(idx)!=100: errors.append('data/questions.json must contain 100 entries')
if errors:
    print('VALIDATION FAILED')
    for e in errors[:200]: print('-',e)
    sys.exit(1)
print(f'OK: {len(files)} question files, IDs Q001-Q100, required sections and local links validated.')
