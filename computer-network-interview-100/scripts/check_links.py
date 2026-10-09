#!/usr/bin/env python3
from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
errors=[]
for p in root.rglob('*.md'):
    text=p.read_text(encoding='utf-8')
    # markdown links, ignoring URLs, anchors and mailto
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        target=target.strip().split('#',1)[0]
        if not target or target.startswith(('http://','https://','mailto:')): continue
        # angle brackets or optional title not used in this repo
        t=(p.parent/target).resolve()
        if not t.exists():
            errors.append(f'{p.relative_to(root)} -> {target}')
if errors:
    print('Broken local links:')
    print('\n'.join(errors[:100]))
    raise SystemExit(1)
print('OK: local Markdown links resolve')
