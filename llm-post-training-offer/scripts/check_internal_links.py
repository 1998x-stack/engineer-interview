from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
for p in list(root.glob('README.md')) + list((root/'docs').rglob('*.md')):
    text=p.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
        if target.startswith(('http://','https://','#','mailto:')): continue
        target=target.split('#',1)[0]
        if not target: continue
        resolved=(p.parent/target).resolve()
        if not resolved.exists(): errors.append(f'{p.relative_to(root)} -> {target}')
if errors:
    print('Broken internal links:'); print('\n'.join(errors)); sys.exit(1)
print('OK: internal links validated.')
