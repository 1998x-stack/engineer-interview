from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
files=sorted((root/"docs/questions").glob("*/q*.md"))
assert len(files)==100, f"expected 100 question files, got {len(files)}"
ids=[]
for f in files:
    m=re.match(r"q(\d{3})-", f.name)
    assert m, f
    ids.append(int(m.group(1)))
    text=f.read_text(encoding="utf-8")
    for section in ["20 秒面试回答","PDF 基线","专业扩展","面试官追问树","工程检查清单","关联题","延伸阅读"]:
        assert section in text, f"{f}: missing {section}"
assert ids==list(range(1,101)), ids
print("OK: 100 questions, continuous IDs, required sections present")
