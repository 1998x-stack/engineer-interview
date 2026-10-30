"""Validate source integrity for the NLP/LLM 100-question handbook.

Requires only Python standard library. PDF is an external reference (opt-in check).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = (
    "## 1. 题目",
    "## 2. 面试官到底在考什么",
    "## 3. 30-60 秒标准回答",
    "## 5. 第一性原理与 Know-Why",
    "## 6. 专业深挖：原理、边界与工程",
    "## 7. 实现、复杂度与工程验证",
    "## 8. 高频失分点",
    "## 9. 追问树",
    "## 11. 参考资料",
    "## 12. 关联题目与知识网络",
)
PDF = ROOT / "assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf"


def frontmatter(text: str) -> dict[str, object]:
    block = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if block is None:
        raise ValueError("leading YAML frontmatter missing")
    result: dict[str, object] = {}
    current_list: str | None = None
    for line in block.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if current_list and re.match(r"^\s+-\s+", line):
            assert isinstance(result[current_list], list)
            result[current_list].append(line.split("-", 1)[1].strip())
            continue
        matched = re.fullmatch(r"([\w-]+):\s*(.*)", line)
        if not matched:
            raise ValueError(f"unsupported YAML frontmatter line: {line!r}")
        key, value = matched.groups()
        if key in result:
            raise ValueError(f"duplicate frontmatter field: {key}")
        if not value:
            result[key] = []
            current_list = key
        else:
            result[key] = value.removeprefix('"').removesuffix('"')
            current_list = None
    return result


def validate(require_pdf: bool = False) -> list[str]:
    errors: list[str] = []
    try:
        manifest = json.loads((ROOT / "data/questions.json").read_text(encoding="utf-8"))
        if not isinstance(manifest, list):
            raise ValueError("questions.json is not a list")
    except (ValueError, OSError) as exc:
        return [f"questions.json unreadable: {exc}"]
    expected_ids = {f"Q{i:03d}" for i in range(1, 101)}
    entries = {}
    for i, row in enumerate(manifest):
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            errors.append(f"invalid metadata record at index {i}")
            continue
        qid = row["id"]
        if qid in entries:
            errors.append(f"duplicate metadata id {qid}")
        entries[qid] = row
    if len(manifest) != 100 or set(entries) != expected_ids:
        errors.append("metadata must contain exactly Q001-Q100")
    files = list(ROOT.glob("docs/[0-9][0-9]-*/Q[0-9][0-9][0-9]-*.md"))
    if len(files) != 100 or {p.name[:4] for p in files} != expected_ids:
        errors.append(f"expected exactly 100 unique question Markdown files; found {len(files)}")
    for qid, item in entries.items():
        path_value = item.get("path")
        if not isinstance(path_value, str):
            errors.append(f"{qid}: missing string path")
            continue
        path = (ROOT / path_value).resolve()
        if not path.is_relative_to(ROOT.resolve()) or not path.is_file():
            errors.append(f"{qid}: path missing or outside repository: {path_value}")
            continue
        if path.name[:4] != qid:
            errors.append(f"{qid}: filename/ID mismatch")
        text = path.read_text(encoding="utf-8")
        try:
            fm = frontmatter(text)
        except ValueError as exc:
            errors.append(f"{qid}: {exc}")
            continue
        for field, expected in (
            ("id", qid),
            ("title", item.get("title")),
            ("chapter", item.get("chapter_title")),
            ("difficulty", item.get("difficulty")),
            ("frequency", item.get("frequency")),
            ("tags", item.get("tags")),
        ):
            if fm.get(field) != expected:
                errors.append(f"{qid}: frontmatter/JSON mismatch: {field}")
        chapter_no = item.get("chapter")
        if not isinstance(chapter_no, int) or path.parent.name[:2] != f"{chapter_no:02d}":
            errors.append(f"{qid}: directory/JSON chapter mismatch")
        for heading in HEADINGS:
            if text.count(heading + "\n") != 1:
                errors.append(f"{qid}: missing or repeated heading: {heading}")
        if text.count("### 回答追问时的升级原则\n") != 1:
            errors.append(f"{qid}: duplicate/missing follow-up guidance")
        raw = ROOT / "sources/questions_raw" / f"{qid}.txt"
        if not raw.is_file():
            errors.append(f"{qid}: source extraction absent")
    raw_files = sorted((ROOT / "sources/questions_raw").glob("Q[0-9][0-9][0-9].txt"))
    if len(raw_files) != 100 or {p.stem for p in raw_files} != expected_ids:
        errors.append("raw source collection must contain exactly Q001-Q100")
    pack_path = ROOT / "data/deepdives_v2.mdpack"
    if pack_path.is_file():
        pack_ids = re.findall(r"(?m)^@@(Q\d{3})\s*$", pack_path.read_text(encoding="utf-8"))
        if len(pack_ids) != 100 or set(pack_ids) != expected_ids:
            errors.append("deepdives_v2.mdpack has missing/duplicate blocks")
    else:
        errors.append("missing data/deepdives_v2.mdpack")
    if not (ROOT / "sources/pdf_text.txt").is_file():
        errors.append("missing sources/pdf_text.txt")
    # Validate links across docs, including references to raw sources outside docs/.
    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    root_resolved = ROOT.resolve()
    for path in ROOT.glob("docs/**/*.md"):
        text = path.read_text(encoding="utf-8")
        for original in link_pattern.findall(text):
            target = original.strip().split("#", 1)[0]
            if not target or re.match(r"^(?:[a-z][a-z0-9+.-]*:|//)", target, re.I):
                continue
            target = re.split(r'\s+["\']', unquote(target), maxsplit=1)[0]
            dest = (path.parent / target).resolve()
            if not dest.is_relative_to(root_resolved):
                errors.append(f"{path.relative_to(ROOT)}: link escapes module: {target}")
            elif not dest.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")
    if require_pdf and not PDF.is_file():
        errors.append("optional source PDF is not available")
    elif not PDF.is_file():
        print("NOTICE: original PDF is not in this Git source snapshot; validated extracted text instead")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-pdf", action="store_true",
                        help="require external source PDF when it is legally available")
    args = parser.parse_args()
    result = validate(require_pdf=args.require_pdf)
    if result:
        for msg in result[:80]:
            print(f"FAIL: {msg}")
        if len(result) > 80:
            print(f"FAIL: ... and {len(result) - 80} further errors")
        sys.exit(1)
    print("OK: 100 unique questions, source text, frontmatter, deepdives, and links")
