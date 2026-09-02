from pathlib import Path
import re, json
root=Path(__file__).resolve().parents[1]
qfiles=sorted(root.glob('docs/[0-9][0-9]-*/q[0-9][0-9][0-9].md'))
assert len(qfiles)==100, f'expected 100 question files, got {len(qfiles)}'
nums=[]
for p in qfiles:
    m=re.search(r'q(\d{3})\.md$',p.name); nums.append(int(m.group(1)))
    text=p.read_text(encoding='utf-8')
    assert text.startswith('---\n'), f'missing YAML: {p}'
    assert f'id: Q{int(m.group(1)):03d}' in text, f'id mismatch: {p}'
    assert '## 30 秒回答' in text and '## 高频追问与参考答案' in text and '## V2 专业深化' in text, f'incomplete: {p}'
assert nums==list(range(1,101)), f'non-contiguous numbers: {nums}'
meta=json.loads((root/'data/questions.json').read_text(encoding='utf-8'))
assert len(meta)==100
assert (root/'assets/pdf/图像算法岗_剑指Offer_100题_2026版.pdf').exists()
assert (root/'docs/assets/pdf/图像算法岗_剑指Offer_100题_2026版.pdf').exists()
# validate relative links inside docs
pat=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
errors=[]
for p in root.glob('docs/**/*.md'):
    text=p.read_text(encoding='utf-8')
    for target in pat.findall(text):
        target=target.strip().split('#',1)[0]
        if not target or target.startswith(('http://','https://','mailto:')): continue
        target=target.replace('%20',' ')
        dest=(p.parent/target).resolve()
        try: dest.relative_to(root.resolve())
        except ValueError:
            errors.append(f'{p.relative_to(root)} -> outside repo: {target}'); continue
        if not dest.exists(): errors.append(f'{p.relative_to(root)} -> missing: {target}')
assert not errors, 'broken relative links:\n'+'\n'.join(errors[:50])
print('OK: 100 questions, metadata, PDFs, required sections and relative links are complete.')
