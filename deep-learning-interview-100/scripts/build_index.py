from pathlib import Path
import json, argparse, re, sys
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser(); parser.add_argument('--check',action='store_true'); args=parser.parse_args()
meta=json.loads((ROOT/'metadata/questions.json').read_text(encoding='utf-8'))
rows='\n'.join(f"| {m['id']} | [{m['title']}]({m['path']}) | {m['chapter_name']} | {m['difficulty']} | {m['priority']} |" for m in meta)
readme=(ROOT/'README.md').read_text(encoding='utf-8')
start='| ID | 题目 | 章节 | 难度 | 优先级 |\n|---|---|---|---|---|\n'
pos=readme.find(start)
if pos<0: raise SystemExit('README index header not found')
a=pos+len(start)
end=readme.find('\n\n## 原始 PDF',a)
new=readme[:a]+rows+readme[end:]
if args.check:
    if new!=readme:
        print('README index is stale'); sys.exit(1)
    print('OK: README index is current')
else:
    (ROOT/'README.md').write_text(new,encoding='utf-8'); print('README index rebuilt')
