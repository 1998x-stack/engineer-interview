from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
qfiles = sorted(DOCS.glob('[0-9][0-9]-*/q*.md'))
errors=[]

if len(qfiles)!=100:
    errors.append(f'Expected 100 question files, got {len(qfiles)}')

ids=[]
required=[
    '## PDF 核心结论',
    '## 深入扩展',
    '## 机制展开：从输入到结果',
    '## 定量模型与最小例子',
    '## 工程连接',
    '## 架构实现差异：x86 / Arm / RISC-V 应怎么回答',
    '## 30–60 秒标准回答',
    '## 原 PDF 追问 + 二阶追问树',
    '## 面试官评分标准',
    '## 自测',
    '## 延伸阅读',
]
for f in qfiles:
    txt=f.read_text(encoding='utf-8')
    m=re.search(r'^id: Q(\d{3})$',txt,re.M)
    if not m:
        errors.append(f'{f}: missing id')
    else:
        ids.append(int(m.group(1)))
    if 'content_version: "2.0-deep"' not in txt:
        errors.append(f'{f}: missing v2 content_version')
    for s in required:
        if s not in txt:
            errors.append(f'{f}: missing section {s}')
    if len(txt) < 6000:
        errors.append(f'{f}: unexpectedly short ({len(txt)} chars)')

if ids != list(range(1,101)):
    errors.append('Question IDs are not exactly 001..100')

# Validate local Markdown/PDF links.
for f in ROOT.rglob('*.md'):
    txt=f.read_text(encoding='utf-8',errors='ignore')
    for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)',txt):
        target=m.group(1).strip()
        if target.startswith(('http://','https://','mailto:','#')):
            continue
        target=target.split('#',1)[0]
        if not target:
            continue
        p=(f.parent/target).resolve()
        if not p.exists():
            errors.append(f'{f.relative_to(ROOT)}: broken link -> {target}')

# Validate mkdocs referenced local paths exist.
yml=(ROOT/'mkdocs.yml').read_text(encoding='utf-8')
for path in re.findall(r':\s+([A-Za-z0-9_./-]+\.md)\s*$',yml,re.M):
    if not (DOCS/path).exists():
        errors.append(f'mkdocs.yml: missing nav target {path}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)

chars=[len(f.read_text(encoding='utf-8')) for f in qfiles]
print(f'OK: {len(qfiles)} question files, IDs 001..100, v2 sections present, links valid.')
print(f'Content size: avg={sum(chars)//len(chars)} chars, min={min(chars)}, max={max(chars)}.')
