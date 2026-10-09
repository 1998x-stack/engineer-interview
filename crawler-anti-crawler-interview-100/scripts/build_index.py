import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
rows=json.loads((root/'data/question-index.json').read_text(encoding='utf-8'))
for r in rows:
    print(f'- [{r["id"]} {r["title"]}]({r["path"]}) {r["difficulty"]}')
