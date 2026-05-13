#!/usr/bin/env python3
"""
Convert PDF slide decks in raw/slides/ to Markdown in raw/slides-md/.
Run from the vault root directory.

Usage:
    python convert_slides.py           # skip already-converted files
    python convert_slides.py --force   # re-convert everything
"""

import argparse
import sys
from pathlib import Path

SLIDES_DIR = Path("raw/slides")
OUTPUT_DIR = Path("raw/slides-md")


def check_dependencies():
    try:
        import pymupdf4llm  # noqa: F401
    except ImportError:
        print("pymupdf4llm not found. Install it with:")
        print("    pip install pymupdf4llm")
        sys.exit(1)


def convert(pdf_path: Path, out_path: Path) -> bool:
    import pymupdf4llm

    try:
        md = pymupdf4llm.to_markdown(str(pdf_path))
        out_path.write_text(md, encoding="utf-8")
        return True
    except Exception as e:
        print(f"  ERROR: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Convert PDF slides to Markdown.")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-convert files that already exist in raw/slides-md/",
    )
    args = parser.parse_args()

    check_dependencies()

    if not SLIDES_DIR.exists():
        print(f"Slides directory not found: {SLIDES_DIR}")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(SLIDES_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"No PDF files found in {SLIDES_DIR}/")
        sys.exit(0)

    print(f"Found {len(pdfs)} PDF(s) in {SLIDES_DIR}/\n")

    converted, skipped, failed = 0, 0, 0

    for pdf in pdfs:
        out = OUTPUT_DIR / (pdf.stem + ".md")

        if out.exists() and not args.force:
            print(f"  SKIP  {pdf.name}  (already converted, use --force to overwrite)")
            skipped += 1
            continue

        print(f"  Converting  {pdf.name} ...", end=" ", flush=True)
        if convert(pdf, out):
            size_kb = out.stat().st_size // 1024
            print(f"OK  ({size_kb} KB → {out.name})")
            converted += 1
        else:
            failed += 1

    print(f"\nDone — converted: {converted}, skipped: {skipped}, failed: {failed}")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
