"""Cross-check JSON, JSONL, chapter filenames and question YAML frontmatter.

Pure standard library. The original PDF is optional: do not pretend a PDF
exists in a clean clone when only derived Markdown is checked in.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ("id", "title", "chapter", "chapter_name", "difficulty", "frequency",
          "priority", "pdf_page", "tags", "last_reviewed", "content_level")
PDF = ROOT / "assets/pdf/deep_learning_algorithm_interview_100_2026.pdf"


def parse_frontmatter(text: str) -> dict:
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if match is None:
        raise ValueError("missing leading YAML frontmatter")
    result = {}
    list_field = None
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if list_field is not None and re.fullmatch(r"\s+-\s+.*", line):
            value = line.strip()[2:].strip()
            result[list_field].append(json.loads(value) if value.startswith('"') else value)
            continue
        m = re.fullmatch(r"([a-z][a-z0-9_]*):\s*(.*)", line)
        if m is None:
            raise ValueError(f"unsupported YAML line: {line}")
        key, raw = m.groups()
        if key in result:
            raise ValueError(f"duplicate field: {key}")
        if raw == "":
            result[key] = []
            list_field = key
        elif raw.startswith('"'):
            result[key] = json.loads(raw)
            list_field = None
        elif re.fullmatch(r"\d+", raw):
            result[key] = int(raw)
            list_field = None
        else:
            result[key] = raw
            list_field = None
    return result


def check(root: Path = ROOT, require_pdf: bool = False) -> list[str]:
    errors = []
    try:
        manifest = json.loads((root / "metadata/questions.json").read_text("utf-8"))
        jsonl = [json.loads(line) for line in (root / "metadata/questions.jsonl")
                 .read_text("utf-8").splitlines() if line.strip()]
    except (OSError, ValueError) as exc:
        return [f"metadata unreadable: {exc}"]
    if not isinstance(manifest, list) or len(manifest) != 100:
        return ["metadata/questions.json must be list of 100 records"]
    if manifest != jsonl:
        errors.append("JSON and JSONL registries differ")
    ids = [f"Q{i:03d}" for i in range(1, 101)]
    if [row.get("id") for row in manifest] != ids:
        errors.append("metadata IDs must be exactly Q001-Q100 in order")
    files = list((root / "questions").glob("[0-9][0-9]-*/Q[0-9][0-9][0-9]-*.md"))
    if len(files) != 100 or {f.name[:4] for f in files} != set(ids):
        errors.append(f"physical question file count or unique IDs mismatch: {len(files)}")
    resolved_root = root.resolve()
    for row in manifest:
        qid = row.get("id")
        relative = row.get("path")
        if not isinstance(relative, str) or not relative.startswith("questions/"):
            errors.append(f"{qid}: missing/invalid registry path")
            continue
        path = (root / relative).resolve()
        if not path.is_relative_to(resolved_root) or not path.is_file():
            errors.append(f"{qid}: path missing or escapes module: {relative}")
            continue
        chapter = row.get("chapter")
        if not isinstance(chapter, int) or not 1 <= chapter <= 10 or path.parent.name[:2] != f"{chapter:02d}" or path.name[:4] != qid:
            errors.append(f"{qid}: chapter or path mismatch")
        try:
            meta = parse_frontmatter(path.read_text("utf-8"))
        except ValueError as exc:
            errors.append(f"{qid}: {exc}")
            continue
        for field in FIELDS:
            if row.get(field) != meta.get(field):
                errors.append(f"{qid}: {field} mismatches registry/frontmatter")
        if not row.get("has_question_specific_verification"):
            errors.append(f"{qid}: verification metadata not asserted")
        if not row.get("has_project_evidence_chain"):
            errors.append(f"{qid}: evidence chain metadata not asserted")
    if require_pdf and not (root / "assets/pdf/deep_learning_algorithm_interview_100_2026.pdf").is_file():
        errors.append("requested original PDF is not tracked")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-pdf", action="store_true",
                        help="require legally obtained PDF for local source audit")
    args = parser.parse_args()
    problems = check(require_pdf=args.require_pdf)
    if problems:
        for problem in problems[:50]:
            print("ERROR:", problem)
        sys.exit(1)
    if not PDF.exists():
        print("NOTICE: original PDF is not tracked; source-page provenance cannot be independently verified")
    print("OK: 100 pages, JSON/JSONL, chapter names, frontmatter and metadata aligned")
