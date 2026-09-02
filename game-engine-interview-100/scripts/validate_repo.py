from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
files=sorted((ROOT/'docs'/'questions').glob('*/Q*.md'))
errors=[]
if len(files)!=100: errors.append(f'Expected 100 question files, got {len(files)}')
nums=[]
required=['## 2. 30 秒回答（PDF 核心内容）','## 4. 专业扩展（Repository v2）','## 5. 如何验证，而不是“凭感觉优化”','## 10. 参考资料']
for f in files:
    m=re.fullmatch(r'Q(\d{3})\.md',f.name)
    if not m: errors.append(f'Bad filename: {f}'); continue
    n=int(m.group(1)); nums.append(n)
    s=f.read_text(encoding='utf-8')
    if f'id: Q{n:03d}' not in s: errors.append(f'Frontmatter id mismatch: {f}')
    for r in required:
        if r not in s: errors.append(f'Missing section {r}: {f}')
    # internal markdown links only
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',s):
        if '://' in target or target.startswith('#'): continue
        target=target.split('#',1)[0]
        p=(f.parent/target).resolve()
        if target and not p.exists(): errors.append(f'Broken internal link {target} in {f}')
if nums!=list(range(1,101)): errors.append(f'Question numbering mismatch: {nums[:5]}...{nums[-5:]}')
if errors:
    print('\n'.join('ERROR: '+e for e in errors)); sys.exit(1)
print(f'OK: {len(files)} questions, numbering Q001-Q100, required sections and internal links validated.')
