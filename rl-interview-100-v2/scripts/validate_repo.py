from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
meta=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
errors=[]
if len(meta)!=100: errors.append(f'questions.json has {len(meta)}, expected 100')
ids=[x['id'] for x in meta]
if ids!=list(range(1,101)): errors.append('question IDs are not Q001-Q100 continuous')
for q in meta:
    p=ROOT/q['path']
    if not p.exists(): errors.append(f'missing {q["path"]}'); continue
    txt=p.read_text(encoding='utf-8')
    for marker in ['PDF 原始要点','Repo 扩展解析','工程实现与训练观测','高频追问','面试官评分标准']:
        if marker not in txt: errors.append(f'{p}: missing section {marker}')
    if p.stat().st_size < 3500: errors.append(f'{p}: unexpectedly short ({p.stat().st_size} bytes)')
for required in ['README.md','book/强化学习算法岗面试宝典_100题_2026版.pdf','references/formula-sheet.md','code/grpo_core.py']:
    if not (ROOT/required).exists(): errors.append(f'missing required artifact {required}')
# conservative internal markdown link check
mds=list(ROOT.rglob('*.md'))
pat=re.compile(r'\[[^]]+\]\(([^)]+)\)')
for p in mds:
    text=p.read_text(encoding='utf-8')
    for link in pat.findall(text):
        if link.startswith(('http://','https://','#','mailto:')): continue
        target=(p.parent/link.split('#')[0]).resolve()
        if link.split('#')[0] and not target.exists(): errors.append(f'{p.relative_to(ROOT)} -> broken link {link}')
if errors:
    print('VALIDATION FAILED')
    for e in errors[:100]: print('-',e)
    sys.exit(1)
print(f'OK: {len(meta)} questions, {len(mds)} markdown files, required artifacts present.')
