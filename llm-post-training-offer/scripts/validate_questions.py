from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
files=sorted(root.glob('docs/[0-9][0-9]-*/q*.md'))
ids=[]
errors=[]
for p in files:
    m=re.match(r'q(\d{3})-',p.name)
    if not m: continue
    qid=int(m.group(1)); ids.append(qid)
    text=p.read_text(encoding='utf-8')
    required=['## 1. 题目定位','## 2. 面试回答阶梯','## 3. Know-Why','## 4. Know-How','## 8. Failure Modes','## 9. 推荐实验','## 10. 面试官连续追问树','## 13. 参考资料']
    for h in required:
        if h not in text: errors.append(f'{p}: missing {h}')
expected=list(range(1,101))
if ids != expected:
    errors.append(f'Question ids mismatch: got {ids[:5]}...{ids[-5:]} count={len(ids)}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('OK: 100 question files validated.')
