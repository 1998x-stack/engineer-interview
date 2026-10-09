from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
qs=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
errors=[]
if len(qs)!=100: errors.append(f'questions.json count={len(qs)}')
files=sorted((ROOT/'docs').glob('[0-9][0-9]-*/q*.md'))
if len(files)!=100: errors.append(f'question markdown count={len(files)}')
ids=[]
for f in files:
    m=re.search(r'q(\d{2,3})\.md$',f.name)
    if m: ids.append(int(m.group(1)))
    txt=f.read_text(encoding='utf-8')
    if '## 2. 30 秒标准回答' not in txt: errors.append(f'missing short answer: {f}')
    if '## 6. GitHub 扩展：工程化理解' not in txt: errors.append(f'missing expansion: {f}')
    if '## 11. 参考资料' not in txt: errors.append(f'missing refs: {f}')
    if '<!-- PROFESSIONAL_ENRICHMENT_START -->' not in txt or '<!-- PROFESSIONAL_ENRICHMENT_END -->' not in txt: errors.append(f'missing professional enrichment: {f}')
    if '<!-- PROFESSIONAL_LAB_START -->' not in txt or '<!-- PROFESSIONAL_LAB_END -->' not in txt: errors.append(f'missing professional lab: {f}')
    if len(txt) < 7000: errors.append(f'question too short for v2 deep-dive: {f} ({len(txt)} chars)')
if sorted(ids)!=list(range(1,101)): errors.append('question IDs are not exactly 1..100')
# validate relative markdown links inside docs
for f in ROOT.glob('docs/**/*.md'):
    txt=f.read_text(encoding='utf-8')
    for link in re.findall(r'\[[^\]]+\]\(([^)]+\.md)\)',txt):
        if link.startswith('http'): continue
        target=(f.parent/link).resolve()
        if not target.exists(): errors.append(f'broken link {link} in {f.relative_to(ROOT)}')
# assets
if not any((ROOT/'assets/pdf').glob('*.pdf')): errors.append('missing source PDF')
if errors:
    print('VALIDATION FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print('OK: 100 question Markdown files, IDs 1..100, required sections, links and PDF asset validated.')
