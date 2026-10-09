#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
QROOT = ROOT / "questions"
files = sorted(QROOT.glob("*/Q[0-9][0-9][0-9].md"))

rows = ["# 100 道 Web 漏洞面试题索引", ""]
current = None
for p in files:
    text = p.read_text(encoding="utf-8")
    qid = re.search(r"(?m)^id:\s*(Q\d{3})$", text).group(1)
    title = re.search(r'(?m)^title:\s*"(.+)"$', text).group(1)
    chapter = re.search(r'(?m)^chapter:\s*"(.+)"$', text).group(1)
    if chapter != current:
        rows += [f"## {chapter}", ""]
        current = chapter
    rel = p.relative_to(QROOT).as_posix()
    rows.append(f"- [{qid} {title}]({rel})")
rows.append("")
(QROOT / "README.md").write_text("\n".join(rows), encoding="utf-8")
print(f"Wrote {len(files)} entries")
