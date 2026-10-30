from pathlib import Path
import re, sys, json

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
    fm = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.DOTALL)
    if not fm:
        errors.append(f'{p}: missing leading YAML frontmatter')
    else:
        # Only fields in the leading YAML frontmatter count.
        fields = dict(re.findall(r'(?m)^([a-zA-Z_][\w-]*):[ \t]*(.*?)[ \t]*$', fm.group(1)))
        if fields.get('id') != f'Q{q:03d}':
            errors.append(f'{p}: frontmatter id mismatch')
        title = fields.get('title', '').strip().strip('"\'')
        if not title.startswith(f'Q{q:03d} '):
            errors.append(f'{p}: frontmatter title mismatch')
        if fields.get('chapter') != str(int(p.parent.name.split('-')[-1])):
            errors.append(f'{p}: frontmatter chapter mismatch')
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

# Ensure the JSON registry agrees with canonical Markdown files.
manifest_file = ROOT / 'data/questions.json'
if not manifest_file.exists():
    errors.append('data/questions.json missing')
else:
    try:
        registry = json.loads(manifest_file.read_text(encoding='utf-8'))
        if not isinstance(registry, list):
            raise ValueError('registry must be a list')
        canonical = {f'Q{int(p.stem[1:]):03d}': p.relative_to(ROOT).as_posix()
                     for p in question_files}
        seen_ids, seen_paths = set(), set()
        if len(registry) != 100:
            errors.append(f'data/questions.json: expected 100 items, found {len(registry)}')
        for entry in registry:
            if not isinstance(entry, dict):
                errors.append('data/questions.json: non-object entry')
                continue
            qid, target = entry.get('id'), entry.get('path')
            if not isinstance(qid, str) or not isinstance(target, str):
                errors.append('data/questions.json: id and path must be strings')
                continue
            if qid in seen_ids or target in seen_paths:
                errors.append(f'data/questions.json: duplicate id/path {qid}: {target}')
            seen_ids.add(qid)
            seen_paths.add(target)
            if canonical.get(qid) != target:
                errors.append(f'data/questions.json: {qid} path mismatch: {target}')
            chapter_part = target.split('/')[2] if len(target.split('/')) >= 4 else None
            if not isinstance(entry.get('chapter'), int) or chapter_part != f"chapter-{entry['chapter']:02d}":
                errors.append(f'data/questions.json: {qid} chapter mismatch')
        if seen_ids != set(canonical):
            errors.append('data/questions.json: question IDs differ from Markdown')
    except (ValueError, OSError, TypeError) as exc:
        errors.append(f'data/questions.json: invalid registry: {exc}')

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
    'OK: Q001-Q100 metadata, manifest, and V2 sections; '
    '9 chapter overviews and 10 system-design pages present.'
)
