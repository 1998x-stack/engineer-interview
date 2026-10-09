from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
qs=sorted((ROOT/'docs/questions').glob('*/Q[0-9][0-9][0-9].md'))
errs=[]
if len(qs)!=100: errs.append(f'Expected 100 question files, found {len(qs)}')
ids=[]
for p in qs:
    m=re.fullmatch(r'Q(\d{3})\.md',p.name)
    if not m: errs.append(f'Bad filename: {p}')
    else: ids.append(int(m.group(1)))
    txt=p.read_text(encoding='utf-8')
    required=['## 2. 30 秒回答','## 3. 3 分钟标准展开','## 4. 白板公式与推导路线','## 7. 面试官连续追问','## 9. 迁移题','## 10. 评分 Rubric','## 14. Advanced Deep Dive｜研究生级深化','### 14.5 实证识别 / 咨询分析怎么落地','### 14.10 Mastery Gate｜真正掌握的标准']
    for h in required:
        if h not in txt: errs.append(f'{p}: missing {h}')
    if len(txt) < 6800: errs.append(f'{p}: too short for v2 professional standard ({len(txt)} chars)')
    if '**本题的额外关键点：**' not in txt: errs.append(f'{p}: missing question-specific advanced insight')
if ids!=list(range(1,101)): errs.append('Question IDs are not exactly 1..100')
for extra in ['docs/reference/advanced-methods.md','docs/reference/econometrics-for-micro-interviews.md','docs/reference/diagram-playbook.md']:
    if not (ROOT/extra).exists(): errs.append(f'Missing v2 reference: {extra}')
data=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
if len(data)!=100: errs.append('data/questions.json does not contain 100 questions')
# relative markdown links
for p in [ROOT/'README.md', *ROOT.glob('docs/**/*.md')]:
    txt=p.read_text(encoding='utf-8')
    for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)',txt):
        if '://' in link or link.startswith('#'): continue
        target=(p.parent/link.split('#')[0]).resolve()
        if not target.exists(): errs.append(f'Broken link in {p.relative_to(ROOT)} -> {link}')
if errs:
    print('VERIFY FAILED')
    for e in errs: print('-',e)
    sys.exit(1)
print('VERIFY OK: 100 questions, indexes/data present, internal links resolve.')
