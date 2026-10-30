"""Prepare an isolated MkDocs source tree without modifying original questions.

MkDocs rejects docs_dir equal to configuration root and site_dir inside docs_dir.
This script stages only tracked Markdown content, preserving relative paths.
"""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / ".mkdocs-src"
DIRECTORIES = ("docs", "questions", "references")


def stage() -> None:
    if STAGING.is_symlink():
        raise RuntimeError("refusing to stage through a symlink")
    if STAGING.exists():
        shutil.rmtree(STAGING)
    STAGING.mkdir()
    for name in DIRECTORIES:
        source = ROOT / name
        if not source.is_dir():
            raise FileNotFoundError(f"required documentation directory missing: {source}")
        for markdown in source.rglob("*.md"):
            if markdown.is_symlink():
                raise RuntimeError(f"refusing symlink in docs: {markdown}")
            destination = STAGING / markdown.relative_to(ROOT)
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(markdown, destination)
    for name in ("README.md", "README_EN.md"):
        source = ROOT / name
        if source.is_file():
            shutil.copy2(source, STAGING / name)
    print(f"Staged MkDocs markdown in {STAGING.relative_to(ROOT)}")


if __name__ == "__main__":
    stage()
