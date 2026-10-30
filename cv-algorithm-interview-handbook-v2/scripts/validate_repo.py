"""Stdlib-only integrity gate for the 100-question computer-vision handbook."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
Q_PATTERN = re.compile(r"q(\d{3})\.md$")
REQUIRED = ("## 30 秒回答", "## 高频追问与参考答案", "## V2 专业深化")
PDF_PATHS = (
    Path("assets/pdf/图像算法岗_剑指Offer_100题_2026版.pdf"),
    Path("docs/assets/pdf/图像算法岗_剑指Offer_100题_2026版.pdf"),
)


def read_frontmatter(path: Path) -> dict:
    """Parse the repository's simple JSON-compatible inline YAML scalar format.

    Keeping the validation dependency-free allows checking source integrity before
    installing MkDocs. Unsupported YAML features are rejected, not misinterpreted.
    """
    text = path.read_text(encoding="utf-8")
    block = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.DOTALL)
    if not block:
        raise ValueError("missing leading YAML frontmatter")
    fields = {}
    for line in block.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line {line!r}")
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if key in fields:
            raise ValueError(f"duplicate frontmatter key {key}")
        if value.startswith(('"', "[")):
            parsed = json.loads(value)
        elif value in ("true", "false"):
            parsed = value == "true"
        elif re.fullmatch(r"\d+", value):
            parsed = int(value)
        else:
            parsed = value
        fields[key] = parsed
    return fields


def run(require_pdf: bool = False) -> list[str]:
    errors = []
    pages = sorted(ROOT.glob("docs/[0-9][0-9]-*/q[0-9][0-9][0-9].md"))
    canonical = {f"Q{int(p.stem[1:]):03d}": p for p in pages}
    if len(pages) != 100 or set(canonical) != {f"Q{i:03d}" for i in range(1, 101)}:
        errors.append(f"expected unique Q001–Q100 pages, found {len(pages)}")

    try:
        registry = json.loads((ROOT / "data/questions.json").read_text(encoding="utf-8"))
        if not isinstance(registry, list):
            raise ValueError("questions.json must contain a list")
    except (OSError, ValueError) as exc:
        errors.append(f"metadata JSON not readable: {exc}")
        registry = []
    records = {}
    for entry in registry:
        if not isinstance(entry, dict) or not isinstance(entry.get("id"), str):
            errors.append("metadata JSON contains an entry without a string id")
            continue
        qid = entry["id"]
        if qid in records:
            errors.append(f"duplicate metadata id: {qid}")
        records[qid] = entry
    if len(registry) != 100 or set(records) != set(canonical):
        errors.append(f"JSON must contain exactly Q001–Q100: records={len(registry)}")

    core_fields = ("id", "title", "chapter", "chapter_title", "difficulty",
                   "frequency", "top30", "tags", "source_label")
    for qid, path in canonical.items():
        content = path.read_text(encoding="utf-8")
        try:
            fields = read_frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        entry = records.get(qid)
        if entry is None:
            continue
        relative = path.relative_to(ROOT).as_posix()
        if entry.get("path") != relative or entry.get("number") != int(qid[1:]):
            errors.append(f"{qid}: JSON path/number mismatch")
        for key in core_fields:
            if fields.get(key) != entry.get(key):
                errors.append(f"{qid}: frontmatter vs JSON mismatch in {key}")
        if int(path.parent.name[:2]) != entry.get("chapter"):
            errors.append(f"{qid}: chapter directory mismatch")
        if not content.startswith(f"---\n") or f"# {qid} ·" not in content:
            errors.append(f"{qid}: Markdown heading mismatch")
        for section in REQUIRED:
            if section not in content:
                errors.append(f"{qid}: missing section {section}")

    try:
        with (ROOT / "data/questions.csv").open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            csv_entries = list(reader)
        csv_by_id = {}
        for entry in csv_entries:
            qid = entry["id"]
            if qid in csv_by_id:
                errors.append(f"CSV duplicate id: {qid}")
            csv_by_id[qid] = entry
        if len(csv_entries) != 100 or set(csv_by_id) != set(canonical):
            errors.append(f"CSV must contain exactly Q001–Q100: rows={len(csv_entries)}")
        for qid, entry in records.items():
            other = csv_by_id.get(qid)
            if not other:
                continue
            for field in ("id", "title", "path"):
                if other[field] != str(entry.get(field)):
                    errors.append(f"{qid}: CSV vs JSON mismatch in {field}")
            for field in ("number", "chapter", "difficulty", "frequency"):
                if int(other[field]) != entry.get(field):
                    errors.append(f"{qid}: CSV vs JSON mismatch in {field}")
            if other["top30"].lower() != str(entry.get("top30")).lower():
                errors.append(f"{qid}: CSV vs JSON mismatch in top30")
            if other["tags"].split("|") != entry.get("tags"):
                errors.append(f"{qid}: CSV vs JSON mismatch in tags")
    except (OSError, ValueError, KeyError) as exc:
        errors.append(f"metadata CSV not valid: {exc}")

    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.glob("docs/**/*.md"):
        for raw in link_pattern.findall(path.read_text(encoding="utf-8")):
            target = raw.strip().split("#", 1)[0]
            if not target or re.match(r"^(?:[a-z][a-z\d+.-]*:|//)", target, re.I):
                continue
            target = unquote(target)
            # Links with optional quoted title: target.md "title".
            target = re.split(r'\s+["\']', target, maxsplit=1)[0]
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(ROOT.resolve()):
                errors.append(f"{path.relative_to(ROOT)}: relative link escapes repository: {target}")
            elif not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local link: {target}")

    missing_pdfs = [str(path) for path in PDF_PATHS if not (ROOT / path).is_file()]
    if require_pdf and missing_pdfs:
        errors.append("required external PDF assets missing: " + ", ".join(missing_pdfs))
    elif missing_pdfs:
        print("NOTICE: external reference PDF not distributed in tracked source: " +
              ", ".join(missing_pdfs))

    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-pdf", action="store_true",
                        help="also require externally supplied PDF assets")
    args = parser.parse_args()
    failures = run(args.require_pdf)
    if failures:
        print("\n".join(f"FAIL: {error}" for error in failures[:100]))
        if len(failures) > 100:
            print(f"... {len(failures) - 100} additional errors")
        sys.exit(1)
    print("OK: 100 questions, frontmatter, JSON/CSV registry, sections and links.")
