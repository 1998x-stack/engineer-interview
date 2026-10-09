from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
idx=json.loads((root/'data/question-index.json').read_text(encoding='utf-8'))
errors=[]
if len(idx)!=100: errors.append(f'index count={len(idx)} expected=100')
ids=[x['id'] for x in idx]
expected=[f'Q{i:02d}' for i in range(1,100)]+['Q100']
if ids!=expected: errors.append('IDs are not continuous Q01-Q100')
for x in idx:
    p=root/x['path']
    if not p.exists(): errors.append(f'missing {p}') ; continue
    text=p.read_text(encoding='utf-8')
    for key in ['id:','title:','chapter:','difficulty:','framework:','pdf_page:','## PDF 基线内容','## 扩展解析：从“会回答”到“会做工程”']:
        if key not in text: errors.append(f'{x["id"]} missing marker {key}')
for c in range(1,11):
    n=sum(1 for x in idx if x['chapter']==c)
    if n!=10: errors.append(f'chapter {c} count={n} expected=10')
if not (root/'pdf/网络安全面试宝典_100题_2026.pdf').exists(): errors.append('missing source PDF')
if errors:
    print('VERIFY FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print('VERIFY OK: 100 questions, 10 chapters, source PDF present, required sections present.')
