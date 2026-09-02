from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
qs=json.loads((root/'data/questions.json').read_text(encoding='utf-8'))
for q in qs:
    print(f"{q['id']}\t{q['chapter']}\t{q['title']}")
