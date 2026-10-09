from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
files=sorted(root.glob('docs/[0-9][0-9]-*/*-*.md'))
qfiles=[]
for f in files:
    m=re.match(r'(\d{3})-',f.name)
    if m and 1<=int(m.group(1))<=100:
        qfiles.append(f)
errors=[]
if len(qfiles)!=100: errors.append(f'expected 100 question files, got {len(qfiles)}')
nums=[]
for f in qfiles:
    txt=f.read_text(encoding='utf-8')
    m=re.search(r'^question_id:\s*(\d+)',txt,re.M)
    if not m: errors.append(f'{f}: missing question_id'); continue
    n=int(m.group(1)); nums.append(n)
    for sec in ['## 2. 30 秒标准回答','## 3. 原理推导','## 4. 深入分析','## 5. 代码 / 白板 / 可复现实验','## 10. 面试评分 Rubric','## 11. 专业深化','## 12. 反例、边界与故障注入','## 13. 源码阅读路线与实战 Lab','## 14. 官方资料与源码阅读']:
        if sec not in txt: errors.append(f'{f}: missing section {sec}')
if sorted(nums)!=list(range(1,101)): errors.append('question ids are not exactly 1..100')
if not (root/'book/SQLite面试100题_专业详解_2026.pdf').exists(): errors.append('missing PDF')
if not (root/'README.md').exists(): errors.append('missing README')
labs=list((root/'docs/labs').glob('[0-9][0-9]-*.md'))
if len(labs)!=10: errors.append(f'expected 10 lab files, got {len(labs)}')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print('OK: 100 enriched question markdown files + 10 labs + metadata + PDF + indexes')
