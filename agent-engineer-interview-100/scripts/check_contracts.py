#!/usr/bin/env python3
"""Independent registry/frontmatter/PDF integrity checks, stdlib only.

Unlike the historical length-and-fragment checker, this validates real bindings
between the manifest, CSV, Markdown frontmatter and pinned binary asset.
"""
from __future__ import annotations
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = [f"q{i:03d}" for i in range(1, 101)]
CSV_FIELDS = {
    "id": "id", "number": "number", "chapter_no": "chapter_no",
    "chapter": "chapter", "question": "q", "frequency": "freq",
    "difficulty": "diff", "priority20": "priority20", "path": "path",
}
FRONT_FIELDS = {
    "id": "id", "title": "q", "chapter": "chapter",
    "chapter_no": "chapter_no", "frequency": "freq",
    "difficulty": "diff", "priority20": "priority20",
}


def scalar(value: str):
    value = value.strip()
    if value in ("true", "false"):
        return value == "true"
    if re.fullmatch(r"[0-9]+", value):
        return int(value)
    if value.startswith('"') and value.endswith('"'):
        return json.loads(value)
    return value


def read_frontmatter(text: str) -> dict:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        raise ValueError("missing leading frontmatter")
    result = {}
    for line in match.group(1).splitlines():
        if line.startswith((" ", "\t")) or not line.strip():
            continue  # List content is not needed for scalar field comparisons.
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"frontmatter line lacks colon: {line!r}")
        if key in result:
            raise ValueError(f"duplicate frontmatter key {key}")
        result[key] = scalar(value)
    return result


def check(root: Path = ROOT) -> list[str]:
    errors = []
    try:
        questions = json.loads((root / "data/questions.json").read_text("utf-8"))
        with (root / "data/questions.csv").open(encoding="utf-8-sig", newline="") as handle:
            csv_rows = list(csv.DictReader(handle))
        manifest = json.loads((root / "MANIFEST.json").read_text("utf-8"))
    except (OSError, ValueError) as exc:
        return [f"cannot read registry: {exc}"]
    if len(questions) != 100 or [q.get("id") for q in questions] != EXPECTED:
        errors.append("JSON must contain exactly ordered q001..q100")
    if len(csv_rows) != 100 or [q.get("id") for q in csv_rows] != EXPECTED:
        errors.append("CSV must contain exactly ordered q001..q100")

    actual_files = list((root / "questions").glob("[0-9][0-9]-*/q[0-9][0-9][0-9].md"))
    if len(actual_files) != 100 or {p.stem for p in actual_files} != set(EXPECTED):
        errors.append(f"question file set mismatch; expected 100, found {len(actual_files)}")
    root_resolved = root.resolve()
    for index, question in enumerate(questions):
        qid = question.get("id", f"row{index}")
        if index >= len(csv_rows):
            break
        row = csv_rows[index]
        for col, json_key in CSV_FIELDS.items():
            value = question.get(json_key)
            expected = str(value).lower() if isinstance(value, bool) else str(value)
            if row.get(col, "").lower() != expected.lower() if col == "priority20" else row.get(col) != expected:
                errors.append(f"{qid}: CSV/JSON mismatch: {col}")
        relative = question.get("path")
        if not isinstance(relative, str) or not relative.startswith("questions/"):
            errors.append(f"{qid}: unsafe or missing path")
            continue
        path = (root / relative).resolve()
        if not path.is_relative_to(root_resolved) or not path.is_file():
            errors.append(f"{qid}: missing or escaping path: {relative}")
            continue
        if path.stem != qid or path.parent.name[:2] != f"{question.get('chapter_no'):02d}":
            errors.append(f"{qid}: chapter or filename mismatch")
        try:
            meta = read_frontmatter(path.read_text(encoding="utf-8"))
            for field, json_key in FRONT_FIELDS.items():
                if meta.get(field) != question.get(json_key):
                    errors.append(f"{qid}: frontmatter/JSON mismatch: {field}")
        except (ValueError, json.JSONDecodeError) as exc:
            errors.append(f"{qid}: bad frontmatter: {exc}")

    pdf = root / "assets/Agent_Engineer_Offer_100_Interview_Handbook.pdf"
    sums = root / "assets/SHA256SUMS.txt"
    if not pdf.is_file() or not sums.is_file():
        errors.append("PDF or SHA256SUMS missing")
    else:
        digest = hashlib.sha256()
        with pdf.open("rb") as handle:
            for block in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(block)
        actual = digest.hexdigest()
        expected = manifest.get("pdf_sha256")
        if actual != expected:
            errors.append("PDF SHA-256 does not match MANIFEST.json")
        if f"{actual}  {pdf.name}" not in sums.read_text("utf-8"):
            errors.append("PDF SHA-256 does not match SHA256SUMS.txt")
    return errors


if __name__ == "__main__":
    problems = check()
    if problems:
        for error in problems[:40]:
            print("FAIL:", error)
        sys.exit(1)
    print("OK: 100 question pages match JSON/CSV/frontmatter; PDF SHA-256 matches")
