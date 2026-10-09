from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
files=sorted(root.glob('docs/[0-9][0-9]-*/Q[0-9][0-9][0-9]-*.md'))
errors=[]
min_chars=3600
ids=[]
required=['## 考察点','## 60-90 秒推荐回答','## 原理深挖','## 高级面试扩展','## 工程化落地','## 常见误区与 Gotchas','## 面试追问拆解','## 面试官评分参考','## 一句话记忆','## 延伸阅读']
for f in files:
    text=f.read_text(encoding='utf-8')
    m=re.search(r'^id:\s*(Q\d{3})$',text,re.M)
    if not m: errors.append(f'{f}: missing front matter id'); continue
    qid=m.group(1); ids.append(qid)
    if not f.name.startswith(qid+'-'): errors.append(f'{f}: filename/id mismatch')
    for h in required:
        if h not in text: errors.append(f'{f}: missing {h}')
    if len(text) < min_chars: errors.append(f'{f}: too short ({len(text)} < {min_chars})')
    bad_followup=re.findall(r'^### 追问 \d+：(第[一二三四五六七八九十]+章|附录|参考资料|RFC |https?://)', text, re.M)
    if bad_followup: errors.append(f'{f}: contaminated followup {bad_followup[:2]}')
expected=[f'Q{i:03d}' for i in range(1,101)]
if ids!=expected: errors.append(f'IDs mismatch: got {len(ids)} files; missing={sorted(set(expected)-set(ids))}')
for src in ['assets/pdf/爬虫与反爬虫面试100题_专业详解.pdf','assets/source/爬虫与反爬虫面试100题_剑指Offer式详解.docx']:
    if not (root/src).exists(): errors.append(f'missing source artifact: {src}')
if errors:
    print('\n'.join('ERROR '+e for e in errors)); sys.exit(1)
print(f'OK: {len(files)} question files, Q001-Q100 complete, required sections present, depth/contamination checks passed.')
