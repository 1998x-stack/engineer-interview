from pathlib import Path
import json, re, sys
ROOT=Path(__file__).resolve().parents[1]
qfiles=sorted((ROOT/'questions').glob('**/q*.md'))
errors=[]
if len(qfiles)!=100: errors.append(f'expected 100 question md files, found {len(qfiles)}')
ids=[]
required=[
    '## 1. 面试官到底在考什么',
    '## 2. 先给结论（30 秒版本）',
    '## 3. Formalization：变量、假设与数学对象',
    '## 4. 标准推导：从第一原则得到答案',
    '## 5. Why：为什么这个方法有效',
    '## 6. 量化金融 / 工程语境中的对应问题',
    '## 7. 边界条件、失效场景与模型风险',
    '## 8. 追问树：不只列问题，还要会接',
    '## 9. 高频错误：错误为什么会发生',
    '## 10. 3 分钟专业回答模板',
    '## 11. 自测与延伸练习',
    '## 12. 关联题目',
    '## 13. 延伸阅读',
    '## 14. 来源与内容边界',
]
for f in qfiles:
    text=f.read_text(encoding='utf-8')
    m=re.search(r'^id: q(\d{3})$', text, re.M)
    if not m:
        errors.append(f'{f}: missing frontmatter id'); continue
    ids.append(int(m.group(1)))
    if 'version: "2.0"' not in text:
        errors.append(f'{f}: missing V2 version marker')
    for s in required:
        if s not in text: errors.append(f'{f}: missing section {s}')
    if len(text)<4000:
        errors.append(f'{f}: content too short for V2 ({len(text)} chars)')
    if any(ord(c)<32 and c!='\n' for c in text):
        errors.append(f'{f}: contains ASCII control character')
if sorted(ids)!=list(range(1,101)): errors.append('question ids are not exactly 001..100')
if not (ROOT/'book/剑指QuantOffer_金融量化算法岗100题_专业版.pdf').exists(): errors.append('PDF missing')
try:
    data=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
    if len(data)!=100: errors.append('questions.json must contain 100 rows')
except Exception as e: errors.append(f'questions.json invalid: {e}')

link_re=re.compile(r'\[[^\]]*\]\(([^)]+)\)')
all_md=list(ROOT.glob('*.md'))+list((ROOT/'docs').glob('*.md'))+list((ROOT/'references').glob('*.md'))+qfiles+list((ROOT/'questions').glob('**/README.md'))
for f in all_md:
    for link in link_re.findall(f.read_text(encoding='utf-8')):
        if link.startswith(('http://','https://','#','mailto:')): continue
        clean=link.split('#',1)[0]
        if not clean: continue
        target=(f.parent/clean).resolve()
        if not target.exists(): errors.append(f'{f}: broken link -> {link}')

for f in qfiles:
    text=f.read_text(encoding='utf-8')
    if "\\n\\n" in text:
        errors.append(f"{f}: contains literal escaped newlines")

try:
    import yaml
    cfg=yaml.safe_load((ROOT/'mkdocs.yml').read_text(encoding='utf-8'))
    def walk_nav(node):
        if isinstance(node, list):
            for x in node: yield from walk_nav(x)
        elif isinstance(node, dict):
            for v in node.values(): yield from walk_nav(v)
        elif isinstance(node, str): yield node
    for rel in walk_nav(cfg.get('nav', [])):
        if rel.endswith('.md') and not (ROOT/'docs'/rel).exists() and not (ROOT/rel).exists():
            errors.append(f"mkdocs nav missing: {rel}")
except ImportError:
    pass

if errors:
    print('VALIDATION FAILED')
    for e in errors: print('-',e)
    sys.exit(1)
print('OK: 100 V2 question files, 14-section structure, metadata, PDF, links and content density validated.')
