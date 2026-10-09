from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
checked=0
for p in root.rglob('*.md'):
    txt=p.read_text(encoding='utf-8')
    for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)', txt):
        href=m.group(1).strip()
        if not href or href.startswith(('http://','https://','mailto:','#')):
            continue
        checked += 1
        rel=href.split('#',1)[0]
        target=(p.parent/rel).resolve()
        if not target.exists():
            errors.append(f'{p.relative_to(root)} -> {href}')
if errors:
    print('\n'.join('BROKEN: '+x for x in errors))
    sys.exit(1)
print(f'OK: {checked} internal Markdown links checked')
