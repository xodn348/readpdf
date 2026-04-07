#!/usr/bin/env python3
"""readpdf - Convert PDF to text for token-efficient AI reading"""

import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF to text for token-efficient AI agent reading"
    )
    parser.add_argument("pdf", help="PDF file path")
    parser.add_argument("-o", "--output", help="Output text file (default: stdout)")
    parser.add_argument("-p", "--page", type=int, help="Extract specific page only")
    parser.add_argument("--pages", help="Page range, e.g. 3-7", metavar="START-END")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"Error: {pdf_path} not found", file=sys.stderr)
        sys.exit(1)

    cmd = ["pdftotext", "-layout"]

    if args.page:
        cmd += ["-f", str(args.page), "-l", str(args.page)]
    elif args.pages:
        try:
            start, end = args.pages.split("-")
            cmd += ["-f", start.strip(), "-l", end.strip()]
        except ValueError:
            print("Error: --pages format must be START-END, e.g. 3-7", file=sys.stderr)
            sys.exit(1)

    if args.output:
        cmd += [str(pdf_path), args.output]
    else:
        cmd += [str(pdf_path), "-"]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr}", file=sys.stderr)
            sys.exit(1)
        if not args.output:
            print(result.stdout, end="")
    except FileNotFoundError:
        print(
            "Error: pdftotext not found.\n"
            "  macOS:  brew install poppler\n"
            "  Linux:  apt install poppler-utils",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
