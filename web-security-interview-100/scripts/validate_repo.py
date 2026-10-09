#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = ROOT / "questions"

errors = []
files = sorted(QUESTIONS.glob("*/Q[0-9][0-9][0-9].md"))

if len(files) != 100:
    errors.append(f"Expected 100 question files, found {len(files)}")

ids = []
for p in files:
    text = p.read_text(encoding="utf-8")
    m = re.search(r"(?m)^id:\s*(Q\d{3})\s*$", text)
    if not m:
        errors.append(f"{p}: missing front-matter id")
        continue
    qid = m.group(1)
    ids.append(qid)
    if p.stem != qid:
        errors.append(f"{p}: filename/id mismatch")
    if len(text.encode("utf-8")) < 10_000:
        errors.append(f"{p}: content unexpectedly short after V2 enrichment")
    for required in [
        "title:",
        "source_pdf_page:",
        "## PDF 母版题解",
        "## GitHub 增强版：深度展开",
        "### 安全不变量（Security Invariants）",
        "### 代码审计 / 设计评审 / 测试视角",
        "## 专业增强版 V2：从面试答案到 AppSec 工程",
        "### 8.1 威胁建模：先定义资产、主体与边界",
        "### 8.6 安全验证矩阵：如何证明“真的修好了”",
        "### 8.10 面试回答分层",
        "## 标准映射",
        "## 关联题目",
    ]:
        if required not in text:
            errors.append(f"{p}: missing {required}")

expected = [f"Q{i:03d}" for i in range(1, 101)]
if sorted(ids) != expected:
    errors.append("Question IDs are not exactly Q001-Q100")

# Verify local Markdown/PDF links across repository.
for md in ROOT.rglob("*.md"):
    text = md.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        if not target:
            continue
        candidate = (md.parent / target).resolve()
        if not candidate.exists():
            errors.append(f"Broken local link in {md.relative_to(ROOT)}: {target}")

pdf = ROOT / "docs/pdf/web-security-interview-100-2026.pdf"
if not pdf.exists():
    errors.append("Source PDF is missing")
elif pdf.stat().st_size < 100_000:
    errors.append("Source PDF looks unexpectedly small")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("OK")
print(f"Questions: {len(files)}")
print(f"Source PDF: {pdf.stat().st_size:,} bytes")
