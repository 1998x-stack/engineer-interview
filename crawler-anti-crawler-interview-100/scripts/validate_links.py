from pathlib import Path
import re, sys

root=Path(__file__).resolve().parents[1]
errors=[]
checked=0
for f in root.rglob('*.md'):
    text=f.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if target.startswith(('http://','https://','mailto:','#')):
            continue
        target=target.split('#',1)[0]
        if not target:
            continue
        checked += 1
        p=(f.parent/target).resolve()
        if not p.exists():
            errors.append(f'{f.relative_to(root)} -> {target}')

# MkDocs nav validation without a YAML dependency.
for line in (root/'mkdocs.yml').read_text(encoding='utf-8').splitlines():
    s=line.strip()
    if not s.startswith('- ') or '.md' not in s or ': ' not in s:
        continue
    rel=s.rsplit(': ',1)[1].strip().strip('"\'')
    if not rel.endswith('.md'):
        continue
    checked += 1
    if not (root/'docs'/rel).exists():
        errors.append(f'mkdocs.yml -> docs/{rel}')

if errors:
    print('\n'.join('ERROR '+x for x in errors[:100]))
    sys.exit(1)
print(f'OK: {checked} internal Markdown/MkDocs paths resolve.')
