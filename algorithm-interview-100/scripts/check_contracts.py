"""Check the real question registry against Markdown, standalone Python and inline code.

This is a source contract, not a proof of algorithm correctness; differential
oracles in tests/ provide the independent behavioral checks.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {
    "id": "num", "leetcode": "lc", "difficulty": "difficulty",
    "priority": "priority", "evidence": "evidence", "pattern": "pattern",
    "category": "category",
}
LINK = re.compile(r"\[([^]]+)\]\(([^)]+)\)")


def frontmatter(markdown: str) -> dict[str, str]:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", markdown, re.S)
    if not match:
        raise ValueError("no YAML frontmatter")
    result = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep or key in result:
            raise ValueError(f"bad/duplicate field {line!r}")
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        result[key] = str(value)
    return result


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    registry = json.loads((root / "data/problems.json").read_text(encoding="utf-8"))
    if len(registry) != 100 or [r.get("num") for r in registry] != list(range(1, 101)):
        return ["registry must have 100 unique sorted IDs"]
    md_files = list((root / "problems").glob("[0-9][0-9]-*/[0-9][0-9][0-9]-*.md"))
    py_files = list((root / "solutions/python").glob("[0-9][0-9][0-9]-*.py"))
    if len(md_files) != 100 or len(py_files) != 100:
        errors.append(f"expected exactly 100 Markdown and 100 Python files, got {len(md_files)}/{len(py_files)}")
    if len({p.name[:3] for p in md_files}) != 100 or len({p.name[:3] for p in py_files}) != 100:
        errors.append("duplicate question IDs in physical files")
    for entry in registry:
        qid = entry["num"]
        path = entry.get("path", "")
        source = entry.get("solution", "")
        if (not isinstance(path, str) or not path.startswith("problems/") or
                not isinstance(source, str) or not source.startswith("solutions/python/")):
            errors.append(f"{qid:03d}: invalid relative path")
            continue
        markdown = (root / path).resolve()
        python = (root / source).resolve()
        if (not markdown.is_relative_to(root.resolve()) or
                not python.is_relative_to(root.resolve()) or
                not markdown.is_file() or not python.is_file()):
            errors.append(f"{qid:03d}: missing/escaping file")
            continue
        if not markdown.name.startswith(f"{qid:03d}-") or not python.name.startswith(f"{qid:03d}-"):
            errors.append(f"{qid:03d}: metadata/file ID mismatch")
        if not markdown.parent.name.startswith(entry["category_slug"]):
            errors.append(f"{qid:03d}: metadata/category path mismatch")
        text = markdown.read_text(encoding="utf-8")
        try:
            fields = frontmatter(text)
        except (ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{qid:03d}: invalid YAML: {exc}")
            continue
        for name, key in FIELDS.items():
            observed = fields.get(name)
            expected = entry.get(key)
            # YAML id is conventionally zero-padded: id: 041 vs integer num=41.
            if name == "id":
                matches = bool(observed and observed.isdecimal() and int(observed) == expected and
                               observed == f"{qid:03d}")
            else:
                matches = observed == str(expected)
            if not matches:
                errors.append(f"{qid:03d}: frontmatter {name} differs from registry")
        match = re.search(
            r"^## 9\. Python 参考实现\s*\n\s*```python\s*\n(.*?)\n```",
            text, re.M | re.S
        )
        if not match:
            errors.append(f"{qid:03d}: section 9 missing Python snippet")
            continue
        inline = match.group(1).strip()
        actual = python.read_text(encoding="utf-8").strip()
        if inline != actual:
            errors.append(f"{qid:03d}: inline code differs from standalone Python source")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        for failure in failures[:50]:
            print("ERROR:", failure)
        sys.exit(1)
    print("OK: 100 metadata records, frontmatter and Markdown/source-code pairs agree")
