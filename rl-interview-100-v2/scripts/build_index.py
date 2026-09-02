from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
qs=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
for q in qs:
    print(f"Q{q['id']:03d}\t{q['title']}\t{q['path']}")
