from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
enrich=json.loads((ROOT/'data/question_enrichment_v2.json').read_text(encoding='utf-8'))
files=sorted((ROOT/'questions').glob('**/q[0-9][0-9][0-9].md'))
assert len(data)==100, f'questions.json has {len(data)} questions'
assert len(enrich)==100, f'question_enrichment_v2.json has {len(enrich)} questions'
assert len(files)==100, f'found {len(files)} question markdown files'
enrich_by_n={x['n']:x for x in enrich}
followup_total=0
for q in data:
    matches=[p for p in files if p.name==f"q{q['n']:03d}.md"]
    assert len(matches)==1, (q['n'],matches)
    p=matches[0]
    text=p.read_text(encoding='utf-8')
    assert len(text)>=5000, f'Q{q["n"]:03d} too short for v1.1 expert edition: {len(text)} chars'
    for needle in [q['title'], q['core'], q['intuition'], q['pitfall'], q['oral']]:
        assert needle in text, f"Q{q['n']:03d} missing PDF-derived field: {needle[:30]}"
    for f in q['followups']:
        assert f in text, f"Q{q['n']:03d} missing followup: {f}"
    expected_math=q['math'].strip().replace('\\[', '$$').replace('\\]', '$$')
    assert expected_math in text, f"Q{q['n']:03d} missing/changed math field"
    for required in [
        'PDF 原始内容（完整保留）', '仓库增强：深度展开', '专家版扩展 v2',
        '推导路线与适用条件', '工程验证矩阵', '高频追问详答',
        '反例与失效条件', '面试回答的三档深度', '自测题'
    ]:
        assert required in text, f'Q{q["n"]:03d} missing v1.1 section: {required}'
    assert '这道追问应从原题' not in text, f'Q{q["n"]:03d} still contains generic followup placeholder'
    bad=[ord(c) for c in text if ord(c)<32 and c not in '\n\r\t']
    assert not bad, f'Q{q["n"]:03d} contains control chars: {sorted(set(bad))}'
    e=enrich_by_n[q['n']]
    assert len(e['followup_answers'])==len(q['followups'])
    for f in q['followups']:
        ans=e['followup_answers'][f]
        followup_total += 1
        assert len(ans)>=35, f'Q{q["n"]:03d} followup answer too short: {f}'
        norm=lambda s: s.replace('\\\\','\\')
        assert norm(ans) in norm(text), f'Q{q["n"]:03d} markdown does not contain structured followup answer: {f}'
assert followup_total==300, f'expected 300 followup answers, got {followup_total}'
# Chapter README quality gates
chapter_readmes=sorted((ROOT/'questions').glob('*/README.md'))
assert len(chapter_readmes)==10
for p in chapter_readmes:
    t=p.read_text(encoding='utf-8')
    for required in ['专业学习框架','知识主线','学完本章应达到','面试表达原则','推荐复习顺序']:
        assert required in t, f'{p.relative_to(ROOT)} missing {required}'
# basic internal markdown link validation
for p in list(ROOT.glob('*.md'))+list((ROOT/'docs').glob('*.md'))+list((ROOT/'questions').glob('**/*.md'))+list((ROOT/'book').glob('*.md')):
    text=p.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        if target.startswith(('http://','https://','#','mailto:')): continue
        path=(p.parent/target.split('#')[0]).resolve()
        assert path.exists(), f'broken link in {p.relative_to(ROOT)} -> {target}'
assert (ROOT/'pdf/control-theory-interview-100-2026.pdf').exists()
print('OK: 100 expert question files, 300 detailed followup answers, PDF parity, v1.1 sections, chapter guides, and internal links validated.')
