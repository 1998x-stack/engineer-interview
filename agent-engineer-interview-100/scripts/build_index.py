#!/usr/bin/env python3
"""Generate/check the questions table from data/questions.json."""
from pathlib import Path
import argparse,json,re,sys
ROOT=Path(__file__).resolve().parents[1]
INDEX=ROOT/'questions/README.md'
qs=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
chapters=[]
for q in qs:
    if q['chapter'] not in [x[1] for x in chapters]:
        chapters.append((q['chapter_no'],q['chapter'],Path(q['path']).parent.name))
rows=[]
for q in qs:
    rel=Path(q['path']).relative_to('questions')
    rows.append(f'| [Q{q["number"]:03d}]({rel.as_posix()}) | {q["q"]} | {q["chapter"]} | {q["freq"]} | {q["diff"]} | {"⭐" if q["priority20"] else ""} |')
text='# 100 道 Agent Engineer 面试题\n\n每个问题独立为一个 Markdown 文件；题号是稳定 ID，方便引用、Issue、PR 和自动化工具处理。\n\n| 题号 | 问题 | 能力轴 | 频率 | 难度 | 必刷 |\n|---|---|---|---|---|---|\n'+'\n'.join(rows)+'\n\n## 章节导航\n\n'+'\n'.join([f'- [CHAPTER {n:02d} · {title}]({d}/README.md) — Q{(n-1)*10+1:03d}–Q{n*10:03d}' for n,title,d in chapters])+'\n'
ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); args=ap.parse_args()
if args.check:
    cur=INDEX.read_text(encoding='utf-8') if INDEX.exists() else ''
    if cur!=text:
        print('questions/README.md is out of date; run python scripts/build_index.py'); sys.exit(1)
    print('OK: questions/README.md is up to date.')
else:
    INDEX.write_text(text,encoding='utf-8'); print('updated',INDEX)
