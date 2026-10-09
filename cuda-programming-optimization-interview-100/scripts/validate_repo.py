from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
errors = []

qs = sorted(root.glob('questions/*/q*.md'))
if len(qs) != 100:
    errors.append(f'expected 100 question files, got {len(qs)}')

nums = []
for p in qs:
    m = re.match(r'q(\d{3})\.md$', p.name)
    if m:
        nums.append(int(m.group(1)))
if nums != list(range(1, 101)):
    errors.append(f'question numbering is not continuous 001..100: {nums[:5]} ... {nums[-5:]}')

required_question_headings = [
    '## PDF 基线题解',
    '## 深入分析',
    '## 面试回答：30 秒 / 2 分钟 / 深挖',
    '## 实战验证建议',
    '## 面试评分 Rubric',
    '## 自测题',
    '## 参考资料',
    '## 专业增强版 V2：机制、量化与验证',
    '### 1. 硬件机制与核心心智模型',
    '### 2. 定量推导 / 性能模型',
    '### 3. 代码 / 白板核心片段',
    '### 4. Nsight 证据链：怎样证明你的判断',
    '### 5. 架构迁移视角',
    '### 6. 可复现实验（建议真的做）',
    '### 7. 深挖追问树',
    '### 8. 高分回答检查清单',
]
for p in qs:
    txt = p.read_text(encoding='utf-8')
    for h in required_question_headings:
        if h not in txt:
            errors.append(f'{p.relative_to(root)} missing heading: {h}')
    if '<!-- PROFESSIONAL-V2 -->' not in txt:
        errors.append(f'{p.relative_to(root)} missing PROFESSIONAL-V2 marker')
    if len(txt.splitlines()) < 185:
        errors.append(f'{p.relative_to(root)} too short for V2: {len(txt.splitlines())} lines')
    # V2 should contain a real code/whiteboard fence and a question-specific experiment/follow-up tree.
    v2 = txt.split('<!-- PROFESSIONAL-V2 -->', 1)[-1]
    if '```cpp' not in v2:
        errors.append(f'{p.relative_to(root)} V2 missing cpp/whiteboard code fence')
    if v2.count('### ') < 8:
        errors.append(f'{p.relative_to(root)} V2 section count too small')


# Validate chapter-level professional guides.
chapter_readmes = sorted(root.glob('questions/*/README.md'))
if len(chapter_readmes) != 10:
    errors.append(f'expected 10 chapter READMEs, got {len(chapter_readmes)}')
for p in chapter_readmes:
    txt = p.read_text(encoding='utf-8')
    if '<!-- CHAPTER-PROFESSIONAL-V2 -->' not in txt:
        errors.append(f'{p.relative_to(root)} missing chapter V2 guide')
    for h in ['## 专业学习指南 V2','### 前置能力','### 本章核心因果模型','### 必做实验','### 掌握度检查']:
        if h not in txt:
            errors.append(f'{p.relative_to(root)} missing chapter heading: {h}')

pdf = root / 'docs' / 'CUDA_编程优化面试100题_专业版.pdf'
if not pdf.exists() or pdf.stat().st_size == 0:
    errors.append('PDF missing or empty')

summary = (root / 'SUMMARY.md').read_text(encoding='utf-8')
for n in range(1, 101):
    if f'Q{n:03d}' not in summary:
        errors.append(f'Q{n:03d} missing from SUMMARY')

# Check relative markdown/file links in every Markdown file.
link_re = re.compile(r'\[[^]]*\]\(([^)]+)\)')
for p in sorted(root.rglob('*.md')):
    txt = p.read_text(encoding='utf-8')
    for link in link_re.findall(txt):
        if link.startswith(('http://', 'https://', '#', 'mailto:')):
            continue
        clean = link.split('#', 1)[0]
        if not clean:
            continue
        target = (p.parent / clean).resolve()
        if not target.exists():
            errors.append(f'broken link in {p.relative_to(root)}: {link}')

# Reject extraction artifacts in question markdowns.
artifacts = [
    'GPU Kernel / HPC / AI Infra / 推理优化 ·',
    'CUDA 编程优化面试 100 题 · 专业版',
    '\x0c',
]
for p in qs:
    txt = p.read_text(encoding='utf-8')
    for artifact in artifacts:
        if artifact in txt:
            errors.append(f'extraction artifact in {p.relative_to(root)}: {artifact!r}')

if errors:
    print('VALIDATION FAILED')
    for e in errors:
        print('-', e)
    sys.exit(1)

print(f'OK: {len(qs)} V2 question files, 10 enriched chapter READMEs, continuous numbering, PDF present, all Markdown links valid, required sections present.')
