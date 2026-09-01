from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for p in ROOT.rglob('*.md'):
    text=p.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
        target=target.split('#',1)[0]
        if not target or '://' in target or target.startswith('mailto:'): continue
        dest=(p.parent/target).resolve()
        if not dest.exists():errors.append(f'{p.relative_to(ROOT)} -> {target}')
if errors:
    print('Broken relative links:')
    print('\n'.join(errors));sys.exit(1)
print('OK: relative Markdown links resolve.')
