from pathlib import Path
import json, re, sys

ROOT=Path(__file__).resolve().parents[1]
files=sorted((ROOT/'questions').glob('**/Q*.md'))
errors=[]
if len(files)!=100:
    errors.append(f'expected 100 question markdown files, got {len(files)}')
required=['## 面试官在考什么','## 一句话结论','## 60–90 秒面试回答','## 深度解析','## 数学、Shape 与复杂度','## 工程实现 / PyTorch 验证','## 工程实践与诊断视角','## 面试官连续追问','## 高频失分点','## 90 分深挖：从会背到能做设计','## 项目化证据链：如何证明你真的做过','## 5 分钟深挖路线','## 自测清单','## 参考资料']
ids=[]
for p in files:
    t=p.read_text(encoding='utf-8')
    m=re.search(r'^id: "(Q\d{3})"$',t,re.M)
    if not m:
        errors.append(f'{p}: missing id')
        continue
    ids.append(m.group(1))
    for h in required:
        if h not in t: errors.append(f'{p}: missing {h}')
    if len(t)<3500: errors.append(f'{p}: v2 content too short ({len(t)} chars)')
    if 'content_level: "v2-deep"' not in t: errors.append(f'{p}: missing content_level v2-deep')
    if '建议的最小验证套路' in t: errors.append(f'{p}: generic verification placeholder remains')
    if '### 推荐验证协议' not in t: errors.append(f'{p}: missing question-specific verification protocol')

    # validate relative markdown links
    for link in re.findall(r'\[[^\]]+\]\(([^)]+\.md)\)', t):
        if link.startswith(('http://','https://')):
            continue
        target=(p.parent/link).resolve()
        if not target.exists():
            errors.append(f'{p}: broken markdown link -> {link}')
expected=[f'Q{i:03d}' for i in range(1,101)]
if ids!=expected:
    errors.append('question IDs are not exactly Q001..Q100 in lexical order')
meta=json.loads((ROOT/'metadata/questions.json').read_text(encoding='utf-8'))
if len(meta)!=100: errors.append('metadata/questions.json must contain 100 records')
if errors:
    print('\n'.join('ERROR: '+e for e in errors))
    sys.exit(1)
print(f'OK: {len(files)} questions; v2-deep structure, depth gates, links and metadata present.')
