from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
items=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
errors=[]
if len(items)!=100: errors.append(f"expected 100 metadata rows, got {len(items)}")
required=['## 1. 题目','## 2. 面试官到底在考什么','## 3. 30-60 秒标准回答','## 5. 第一性原理与 Know-Why','## 8. 高频失分点','## 9. 追问树','## 11. 参考资料']
for i,item in enumerate(items,1):
    if item['id']!=f'Q{i:03d}': errors.append(f"id mismatch at {i}: {item['id']}")
    p=ROOT/item['path']
    if not p.exists(): errors.append(f"missing {p}"); continue
    txt=p.read_text(encoding='utf-8')
    for h in required:
        if h not in txt: errors.append(f"{item['id']} missing heading: {h}")
    if not txt.startswith('---\n'): errors.append(f"{item['id']} missing frontmatter")
raw=list((ROOT/'sources/questions_raw').glob('Q*.txt'))
if len(raw)!=100: errors.append(f"expected 100 raw question files, got {len(raw)}")
if errors:
    print('VALIDATION FAILED')
    print('\n'.join('- '+e for e in errors))
    sys.exit(1)
print('OK: 100 questions, metadata, source files and required sections validated.')
