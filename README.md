# readpdf

Convert PDFs to text for token-efficient AI agent reading.

## Why

Reading PDFs with vision costs 100–500 tokens per page. Converting to text first lets any AI agent read only the sections it needs — saving **up to 90% of tokens**.

## Install

```bash
pip install readpdf-cli
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

## How it works

```
Without readpdf:
  PDF → AI vision → ~200 tokens/page × 30 pages = 6,000 tokens (full doc, every time)

With readpdf:
  PDF → pdftotext → paper.txt (on disk, 0 tokens)
  AI reads only offset/limit chunks it needs → ~300 tokens total
```

**Step 1.** `readpdf paper.pdf -o paper.txt` runs `pdftotext` locally — no AI tokens consumed.

**Step 2.** The AI uses a file-reading tool (e.g. Read with `offset`/`limit`) to load only the relevant lines. Because the text file already exists on disk, the AI never pays the cost of processing the entire PDF.

**Why not MCP?** MCP tool results return the full content back into the AI's context window — same cost as reading directly. A disk file lets the AI pull exactly the slice it needs, nothing more.

## License

MIT
