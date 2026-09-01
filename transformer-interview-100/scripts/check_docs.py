from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
question_files = sorted((ROOT / 'docs/questions').glob('chapter-*/Q*.md'))
errors = []
ids = []

required_sections = [
    '30 秒回答',
    '核心公式 / Shape',
    'Professional Expansion',
    '常见失分点',
    '面试评分 Rubric',
    '深入推导：把结论变成可验证的模型',
    '题目特异的工程 Checklist',
    '推荐验证协议',
    '面试官真正想听到的“边界条件”',
    'Whiteboard / Coding 表达模板',
]

for p in question_files:
    m = re.fullmatch(r'Q(\d{3})\.md', p.name)
    if not m:
        continue
    q = int(m.group(1))
    ids.append(q)
    text = p.read_text(encoding='utf-8')
    if f'id: Q{q:03d}' not in text:
        errors.append(f'{p}: frontmatter id mismatch')
    if f'# Q{q:03d} ·' not in text:
        errors.append(f'{p}: title mismatch')
    for section in required_sections:
        if section not in text:
            errors.append(f'{p}: missing section {section}')
    if len(text) < 4500:
        errors.append(f'{p}: unexpectedly short ({len(text)} chars)')

expected = list(range(1, 101))
if ids != expected:
    errors.append(
        f'question ids are not exactly Q001-Q100: '
        f'{ids[:5]}...{ids[-5:]} count={len(ids)}'
    )

for chapter in range(1, 10):
    p = ROOT / f'docs/questions/chapter-{chapter:02d}/index.md'
    if not p.exists():
        errors.append(f'missing chapter overview: {p}')
        continue
    text = p.read_text(encoding='utf-8')
    if '本章完成标准' not in text or '本章自测' not in text:
        errors.append(f'{p}: incomplete chapter overview')

for sd in range(1, 11):
    p = ROOT / f'docs/system-design/SD{sd:02d}.md'
    if not p.exists():
        errors.append(f'missing system design page: {p}')
    elif len(p.read_text(encoding='utf-8')) < 1500:
        errors.append(f'{p}: system design page too short')

if errors:
    print('\n'.join(errors))
    sys.exit(1)

print(
    'OK: Q001-Q100 complete with V2 sections; '
    '9 chapter overviews and 10 system-design pages present.'
)
