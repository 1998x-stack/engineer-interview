from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
files=sorted(root.glob('chapters/*/q[0-9][0-9][0-9].md'))
errors=[]
if len(files)!=100:
    errors.append(f'expected 100 question files, got {len(files)}')
seen=[]
for f in files:
    text=f.read_text(encoding='utf-8')
    m=re.search(r'^id:\s*(Q\d{3})$', text, re.M)
    if not m:
        errors.append(f'{f}: missing id')
        continue
    qid=m.group(1); seen.append(qid)
    if f.stem != qid.lower(): errors.append(f'{f}: filename/id mismatch {qid}')
    for required in ['30–60 秒面试标准回答','PDF 原理拆解','深度扩展','进一步追问树','官方参考']:
        if required not in text: errors.append(f'{f}: missing section {required}')
expected=[f'Q{i:03d}' for i in range(1,101)]
if sorted(seen)!=expected: errors.append('question IDs are incomplete or duplicated')
for req in ['README.md','SUMMARY.md','docs/pdf/Redis_Interview_100_Offer_Style_2026.pdf','docs/appendix/a-followups.md','docs/appendix/b-production-runbook.md','docs/appendix/c-study-plan.md','docs/appendix/d-version-matrix.md','docs/references.md']:
    if not (root/req).exists(): errors.append(f'missing {req}')
summary=(root/'SUMMARY.md').read_text(encoding='utf-8')
for qid in expected:
    if qid not in summary: errors.append(f'SUMMARY missing {qid}')
link_re=re.compile(r'\[[^\]]*\]\(([^)]+)\)')
for md in root.rglob('*.md'):
    text=md.read_text(encoding='utf-8')
    for href in link_re.findall(text):
        href=href.strip()
        if href.startswith(('http://','https://','#','mailto:')): continue
        target=href.split('#')[0]
        if target and not (md.parent/target).resolve().exists():
            errors.append(f'{md.relative_to(root)}: broken relative link {href}')
for f in files:
    if '\nCHAPTER ' in f.read_text(encoding='utf-8'):
        errors.append(f'{f}: chapter divider leaked into question body')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print(f'OK: {len(files)} question files; IDs, artifacts, and relative links are valid.')
