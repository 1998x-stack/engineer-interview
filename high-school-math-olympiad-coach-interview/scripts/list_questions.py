from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
for q in json.loads((ROOT/'metadata/questions.json').read_text(encoding='utf-8')):
    print(f"Q{q['id']}\t{q['chapter']}\t{q['title']}")
