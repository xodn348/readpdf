# readpdf

Convert PDFs to text for token-efficient AI agent reading.

## Why

Reading PDFs with vision costs 100–500 tokens per page. Converting to text first lets any AI agent read only the sections it needs — saving **up to 90% of tokens**.

## Install

```bash
pip install readpdf
```

Requires `pdftotext`:
```bash
# macOS
brew install poppler

# Linux
apt install poppler-utils
```

## Usage

```bash
# Convert to file, then read selectively
readpdf paper.pdf -o paper.txt

# Extract a single page
readpdf paper.pdf -o paper.txt -p 3

# Extract a page range
readpdf paper.pdf -o paper.txt --pages 3-7

# Print to stdout
readpdf paper.pdf
```

Works with any AI agent that has shell access: Claude, GPT-4, Gemini, Cursor, etc.

## License

MIT
