from pathlib import Path
import re, json, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
qfiles=sorted((ROOT/'questions').glob('*/Q[0-9][0-9][0-9].md'))
if len(qfiles)!=100: errors.append(f'Expected 100 question files, found {len(qfiles)}')
ids=[]
for p in qfiles:
    txt=p.read_text(encoding='utf-8')
    m=re.search(r'^id:\s*Q(\d{3})$',txt,re.M)
    if not m: errors.append(f'Missing YAML id: {p}')
    else: ids.append(m.group(1))
    for heading in ['## PDF 核心内容（完整迁移）','## 仓库增强：深度解析与训练设计','### 专业版 v2：','## 关联题目']:
        if heading not in txt: errors.append(f'Missing {heading}: {p}')
    bad=[c for c in txt if ord(c)<32 and c not in '\n\r\t']
    if bad: errors.append(f'Control character found: {p}')
    # local markdown/pdf/image links only
    for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',txt):
        if link.startswith(('http://','https://','#','mailto:')): continue
        target=(p.parent/link.split('#',1)[0]).resolve()
        if not target.exists(): errors.append(f'Broken link {link} in {p.relative_to(ROOT)}')
expected=[f'{i:03d}' for i in range(1,101)]
if sorted(ids)!=expected: errors.append('Question IDs are not exactly 001..100')
for required in ['assets/pdf/high_school_math_olympiad_coach_interview_100.pdf','source/high_school_math_olympiad_coach_interview_100.tex','metadata/questions.json']:
    if not (ROOT/required).exists(): errors.append(f'Missing {required}')
try:
    data=json.loads((ROOT/'metadata/questions.json').read_text(encoding='utf-8'))
    if len(data)!=100: errors.append('questions.json does not contain 100 entries')
except Exception as e: errors.append(f'questions.json invalid: {e}')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print('OK: 100 questions, source artifacts, metadata, internal links, Professional v2 sections, and control characters validated.')
