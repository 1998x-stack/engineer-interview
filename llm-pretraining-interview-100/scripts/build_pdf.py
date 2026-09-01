#!/usr/bin/env python3
"""Build the printable interview handbook PDF from the maintained HTML source."""
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build LLM Pretraining Interview 100 PDF")
    parser.add_argument(
        "--input",
        default="book/llm_pretrain_offer.html",
        help="HTML source relative to repository root",
    )
    parser.add_argument(
        "--output",
        default="book/LLM-Pretraining-Interview-100.pdf",
        help="PDF output relative to repository root",
    )
    args = parser.parse_args()

    repo = Path(__file__).resolve().parents[1]
    src = (repo / args.input).resolve()
    out = (repo / args.output).resolve()
    if not src.exists():
        raise SystemExit(f"source HTML does not exist: {src}")

    try:
        from weasyprint import HTML
    except ImportError as exc:
        raise SystemExit(
            "WeasyPrint is required. Install with: pip install -r requirements-pdf.txt"
        ) from exc

    out.parent.mkdir(parents=True, exist_ok=True)
    HTML(filename=str(src), base_url=str(src.parent)).write_pdf(str(out))

    if not out.exists() or out.stat().st_size < 50_000:
        raise SystemExit(f"PDF generation failed or output is unexpectedly small: {out}")

    print(f"Built {out.relative_to(repo)} ({out.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
