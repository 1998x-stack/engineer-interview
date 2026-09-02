from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))
print(f'{len(data)} questions loaded.')
for q in data[:5]: print(q['id'] if 'id' in q else q['n'], q['title'])
