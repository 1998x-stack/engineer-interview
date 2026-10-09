from pathlib import Path
import re, sys, ast
root=Path(__file__).resolve().parents[1]
files=sorted((root/'questions').glob('*/Q*.md'))
ids=[]; errors=[]
required=['## 1. 题目','## 2. 面试开始先澄清','## 3. 基线方案与瓶颈','## 4. 关键洞察','## 5. 不变量与正确性证明','## 6. 参考实现','## 7. 复杂度','## 8. 高频失分点','## 9. 面试官追问','## 10. 60 秒口述模板','## 11. 自测清单','## 12. 专业深化：约束驱动的完整面试推导']
for p in files:
    m=re.match(r'Q(\d{3})-',p.name)
    if not m: errors.append(f'bad filename: {p}'); continue
    ids.append(int(m.group(1)))
    t=p.read_text(encoding='utf-8')
    for h in required:
        if h not in t: errors.append(f'{p}: missing {h}')

    blocks=re.findall(r'```python\n(.*?)\n```',t,re.S)
    if not blocks:
        errors.append(f'{p}: missing python block')
    for bi,code in enumerate(blocks,1):
        try: ast.parse(code)
        except SyntaxError as e: errors.append(f'{p}: Python block {bi} syntax error: {e}')
if ids != list(range(1,101)): errors.append(f'IDs are not exactly 1..100: count={len(ids)}')
# README local markdown targets
readme=(root/'README.md').read_text(encoding='utf-8')
for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)',readme):
    if '://' in link or link.startswith('#'): continue
    target=(root/link.split('#')[0]).resolve()
    if not target.exists(): errors.append(f'broken README link: {link}')
# Check local links across all Markdown files.
for md in root.rglob('*.md'):
    body=md.read_text(encoding='utf-8')
    for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)', body):
        if '://' in link or link.startswith('#') or link.startswith('mailto:'):
            continue
        raw=link.split('#')[0]
        if not raw:
            continue
        target=(md.parent/raw).resolve()
        if not target.exists():
            errors.append(f'{md}: broken local link: {link}')


# v2 support docs
pattern_files=sorted((root/'patterns').glob('*.md'))
if len(pattern_files) != 16:
    errors.append(f'expected 16 pattern docs, got {len(pattern_files)}')
for p in pattern_files:
    t=p.read_text(encoding='utf-8')
    for h in ['## 1. 核心模型','## 2. 识别信号','## 3. 不变量模板','## 4. 结构选择对照','## 5. 复杂度表达','## 6. 高频误区','## 8. 对应题目']:
        if h not in t: errors.append(f'{p}: missing {h}')
chapter_readmes=sorted((root/'questions').glob('*/README.md'))
if len(chapter_readmes) != 10:
    errors.append(f'expected 10 chapter README files, got {len(chapter_readmes)}')
for p in chapter_readmes:
    if '## 深化版章节训练目标' not in p.read_text(encoding='utf-8'):
        errors.append(f'{p}: missing deep chapter goals')
if not (root/'docs'/'DEEP_REVIEW_GUIDE.md').exists(): errors.append('deep review guide missing')
if not (root/'mkdocs.yml').exists(): errors.append('mkdocs.yml missing')

if not (root/'assets'/'pdf'/'数据结构面试100题_专业版.pdf').exists(): errors.append('source PDF missing')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'OK: {len(files)} questions, 16 enriched pattern docs, 10 enriched chapter READMEs, Python blocks parse, local Markdown links valid, source PDF present.')
