from pathlib import Path
import re, sys, json
root=Path(__file__).resolve().parents[1]
errors=[]
qfiles=sorted((root/'docs/chapters').glob('*/q*.md'))
ids=[]
for f in qfiles:
    t=f.read_text(encoding='utf-8')
    m=re.search(r'^id:\s*(Q\d{3})$',t,re.M)
    if not m: errors.append(f'missing id: {f}')
    else: ids.append(m.group(1))
    for required in ['## 30 秒面试回答','## 2. 关键公式 / 成本模型','## 3. 深入原理：Know-Why','## 4. 工程场景 / 现场推演','## 8. 追问链','## 9. 面试官评分标准','## 10. 2026 工程扩展（外部资料）','## 10.1 专家级深挖：把结论推到白板上','## 10.2 源码 / Runtime 视角','## 10.3 Benchmark Lab：如何把本题变成可复现实验','## 10.4 资深面试进阶：从“会答”到“会做系统”']:
        if required not in t: errors.append(f'missing section {required}: {f}')
expected=[f'Q{i:03d}' for i in range(1,101)]
if ids!=expected: errors.append(f'question ids mismatch: {ids[:3]}...{ids[-3:]} count={len(ids)}')
# Check every local markdown link in every markdown file
for f in root.rglob('*.md'):
    t=f.read_text(encoding='utf-8')
    for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)',t):
        if link.startswith(('http://','https://','mailto:','#')): continue
        target=link.split('#',1)[0]
        if not target: continue
        p=(f.parent/target).resolve()
        if not p.exists(): errors.append(f'broken link: {f.relative_to(root)} -> {link}')
# machine-readable data
try:
    data=json.loads((root/'data/questions.json').read_text(encoding='utf-8'))
    if len(data)!=100: errors.append(f'questions.json count={len(data)}')
except Exception as e: errors.append(f'questions.json invalid: {e}')
# source PDF and extracted text
for p in [root/'assets/pdf/LLM_Inference_Interview_100_2026.pdf',root/'sources/pdf-extracted.txt']:
    if not p.exists() or p.stat().st_size==0: errors.append(f'missing source asset: {p}')
# MkDocs nav targets (simple path extraction)
mk=(root/'mkdocs.yml').read_text(encoding='utf-8')
for rel in re.findall(r':\s+([^\s]+\.md)$',mk,re.M):
    if not (root/'docs'/rel.strip('"\'')).exists(): errors.append(f'mkdocs missing: {rel}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'OK: {len(qfiles)} question files; IDs continuous; required sections present; all local Markdown links valid; data/source/MkDocs checks passed.')
