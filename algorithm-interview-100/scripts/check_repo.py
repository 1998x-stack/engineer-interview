from __future__ import annotations
import ast, json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data/problems.json').read_text(encoding='utf-8'))
errors=[]
if len(data)!=100: errors.append(f'expected 100 problems, got {len(data)}')
ids=[x['num'] for x in data]
if ids!=list(range(1,101)): errors.append('problem ids are not exactly 1..100')
for x in data:
    md=ROOT/x['path']; py=ROOT/x['solution']
    if not md.exists(): errors.append(f'missing {md}')
    if not py.exists(): errors.append(f'missing {py}')
    if md.exists():
        text=md.read_text(encoding='utf-8')
        for field in ['id:','leetcode:','difficulty:','priority:','evidence:','pattern:','category:']:
            if field not in text[:800]: errors.append(f'{md}: missing front matter {field}')
        for h in ['## 4. 暴力基线与瓶颈','## 5. 关键观察与不变量','## 7. 正确性说明','## 11. 边界与测试清单','## 13. 面试追问']:
            if h not in text: errors.append(f'{md}: missing section {h}')
        # relative links only: verify Markdown links that are not http/anchor
        for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
            if link.startswith(('http://','https://','#')): continue
            target=(md.parent/link.split('#')[0]).resolve()
            if not target.exists(): errors.append(f'{md}: broken link {link}')
    if py.exists():
        try: ast.parse(py.read_text(encoding='utf-8'))
        except SyntaxError as e: errors.append(f'{py}: syntax error {e}')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print(f'OK: {len(data)} problems, markdown/front-matter/links/python syntax passed')
