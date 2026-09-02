from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
files=sorted(ROOT.glob('docs/questions/*/Q[0-9][0-9][0-9].md'))
errors=[]
if len(files)!=100: errors.append(f'Expected 100 question files, got {len(files)}')
ids=[]
for p in files:
    text=p.read_text(encoding='utf-8')
    m=re.search(r'^id:\s*(Q\d{3})$',text,re.M)
    if not m: errors.append(f'Missing id: {p}')
    else: ids.append(m.group(1))
    for req in ['## 1. 这道题在考什么？','## 2. 30 秒回答','## 6. 工程实现与系统接口','## 7. 工程 Gotchas','## 12. References / Further Reading']:
        if req not in text: errors.append(f'Missing section {req}: {p}')
expected=[f'Q{i:03d}' for i in range(1,101)]
if sorted(ids)!=expected: errors.append('Question IDs are not exactly Q001..Q100')
# all internal markdown links
link_re=re.compile(r'\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)')
mds=list(ROOT.glob('*.md'))+list(ROOT.glob('docs/**/*.md'))
for p in mds:
    text=p.read_text(encoding='utf-8')
    for link in link_re.findall(text):
        if link.startswith(('http://','https://')): continue
        target=(p.parent/link).resolve()
        if not target.exists(): errors.append(f'Broken link in {p.relative_to(ROOT)} -> {link}')
# Release artifacts
if not list((ROOT/'releases').glob('*.pdf')): errors.append('Missing PDF release')
if errors:
    print('\n'.join('ERROR: '+x for x in errors)); sys.exit(1)
print(f'OK: {len(files)} question files, sequential IDs, required sections, all internal Markdown links, release artifacts validated.')
