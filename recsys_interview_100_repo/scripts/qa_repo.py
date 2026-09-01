from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
qs = sorted((DOCS / "questions").glob("*/q*.md"))


def strip_code_for_link_check(text: str) -> str:
    """Remove fenced and inline code before interpreting Markdown links."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"~~~.*?~~~", "", text, flags=re.S)
    text = re.sub(r"`[^`\n]*`", "", text)
    return text

def validate_local_markdown_links() -> int:
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    checked = 0
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = strip_code_for_link_check(md.read_text(encoding="utf-8"))
        for raw in pattern.findall(text):
            target = raw.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            target = target.replace("%20", " ")
            checked += 1
            resolved = (md.parent / target).resolve()
            assert resolved.exists(), f"{md}: broken local link {raw}"
    return checked

assert len(qs) == 100, f"expected 100 question files, got {len(qs)}"

required = [
    "## 题目定位",
    "## 30 秒回答",
    "## 深入拆解",
    "## V2 深度版：从“会答”到“能落地”",
    "### 针对本题的关键推导",
    "### 90 秒标准回答（建议练到可以脱稿）",
    "### 上线验证与监控",
    "### 一个可用于面试的具体例子",
    "### 工程决策矩阵",
    "### 边界条件与反例",
    "## 工业级工程视角",
    "## 常见失分",
    "## 连续追问",
    "## 连续追问参考答案",
    "## 相关题目",
    "## 参考资料",
]

for f in qs:
    text = f.read_text(encoding="utf-8")
    for h in required:
        assert h in text, f"{f}: missing {h}"

    assert len(text.encode("utf-8")) >= 10_000, f"{f}: content too short ({len(text.encode('utf-8'))} bytes)"
    assert text.count("<!-- V2_ENRICHMENT_START -->") == 1, f"{f}: bad V2 start marker count"
    assert text.count("<!-- V2_ENRICHMENT_END -->") == 1, f"{f}: bad V2 end marker count"
    assert "回答这类追问时先明确" not in text, f"{f}: generic follow-up answer remains"

    block = re.search(r"## 连续追问\n\n(.*?)(?=\n## 连续追问参考答案)", text, re.S)
    assert block, f"{f}: follow-up block missing"
    followups = re.findall(r"^\d+\.\s+.+$", block.group(1), re.M)
    assert len(followups) == 5, f"{f}: expected 5 follow-ups, got {len(followups)}"

    answer_block = re.search(r"## 连续追问参考答案\n\n(.*?)(?=\n## 自测清单)", text, re.S)
    assert answer_block, f"{f}: answer block missing"
    answers = re.findall(r"^### 追问 \d+：", answer_block.group(1), re.M)
    assert len(answers) == 5, f"{f}: expected 5 follow-up answers, got {len(answers)}"

    # Detect common PDF extraction / generated LaTeX corruption.
    assert "O(L           )" not in text, f"{f}: malformed complexity remains"
    assert "ESCM     " not in text, f"{f}: malformed model name remains"
    assert "\t" not in "".join(re.findall(r"\$\$(.*?)\$\$", text, re.S)), f"{f}: tab found inside display math"

    for link in re.findall(r"\]\(([^)]+\.md)\)", text):
        if link.startswith("http"):
            continue
        target = (f.parent / link).resolve()
        assert target.exists(), f"{f}: broken link {link}"

# Repository-level reference and study artifacts.
assert (DOCS / "references" / "primary-sources.md").exists()
assert (DOCS / "study" / "high-frequency-20.md").exists()
assert (ROOT / "scripts" / "enrich_v2.py").exists()
assert (ROOT / "scripts" / "enrich_followups.py").exists()
assert (ROOT / "scripts" / "polish_followups.py").exists()

checked_links = validate_local_markdown_links()
print(f"QA PASS: 100 detailed question files; V2 sections, 500 answered follow-ups, {checked_links} local Markdown links OK")
