from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PAGES = [p for p in (ROOT / 'problems').rglob('*.md') if p.name != 'README.md']

errors: list[str] = []
required_headings = [
    '## 17. 解法谱系',
    '## 18. 状态设计与不变量审计',
    '## 19. 正确性证明',
    '## 20. 复杂度深拆',
    '## 21. 测试工程',
    '## 22. 代码 Review Checklist',
    '## 23. Follow-up Tree',
    '## 24. 算法工程化',
    '## 25. 同类题迁移导航',
    '## 26. 面试评分 Rubric',
    '## 27. 复习卡片',
    '## 28. 资料与证据',
]

if len(PAGES) != 100:
    errors.append(f'expected 100 problem pages, got {len(PAGES)}')

for page in PAGES:
    text = page.read_text(encoding='utf-8')
    lines = text.splitlines()
    if len(lines) < 350:
        errors.append(f'{page.relative_to(ROOT)} too short: {len(lines)} lines')
    for heading in required_headings:
        if heading not in text:
            errors.append(f'{page.relative_to(ROOT)} missing heading: {heading}')
    if text.count('<!-- PRO-ENRICHMENT-V2:START -->') != 1:
        errors.append(f'{page.relative_to(ROOT)} enrichment marker count != 1')
    # Require a four-column solution ladder and at least three approaches.
    m = re.search(
        r'\| 层级 \| 方案 \| 复杂度/代价 \| 面试价值 \|\n'
        r'\|---\|---\|---\|---\|\n(.*?)(?=\n\n###)',
        text,
        flags=re.S,
    )
    if not m:
        errors.append(f'{page.relative_to(ROOT)} missing solution ladder table')
    else:
        rows = [x for x in m.group(1).splitlines() if x.startswith('|')]
        if len(rows) < 3:
            errors.append(f'{page.relative_to(ROOT)} solution ladder has <3 rows')

if errors:
    print('CONTENT DEPTH CHECK FAILED')
    for error in errors:
        print('-', error)
    sys.exit(1)

lengths = [len(p.read_text(encoding='utf-8').splitlines()) for p in PAGES]
print(
    'OK: 100 interview-grade pages; '
    f'avg={sum(lengths)/len(lengths):.1f} lines, '
    f'min={min(lengths)}, max={max(lengths)}'
)
