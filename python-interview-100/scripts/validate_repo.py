from pathlib import Path
import re, sys
root=Path(__file__).resolve().parents[1]
files=sorted((root/'docs'/'questions').glob('**/q*.md'))
errors=[]
if len(files)!=100:
    errors.append(f'expected 100 question files, got {len(files)}')
nums=[]
required=['## 题目定位','## 30-60 秒标准回答','## 原理拆解','## 易错点 / Gotchas','## 工程实践检查表','## 面试官连续追问','## 举一反三','## 自测标准','## 参考资料']
for p in files:
    m=re.fullmatch(r'q(\d{2,3})\.md',p.name)
    if not m:
        errors.append(f'bad filename: {p}')
        continue
    nums.append(int(m.group(1)))
    text=p.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        errors.append(f'missing front matter: {p}')
    for h in required:
        if h not in text:
            errors.append(f'missing {h}: {p}')
if sorted(nums)!=list(range(1,101)):
    errors.append(f'question numbers are not contiguous: {nums}')
pdf=root/'book'/'Python面试宝典_100道核心真题_专业版.pdf'
if not pdf.exists() or pdf.stat().st_size<100_000:
    errors.append('book PDF missing or unexpectedly small')
if errors:
    print('\n'.join('ERROR: '+e for e in errors))
    sys.exit(1)
print('OK: 100 question markdown files validated.')
