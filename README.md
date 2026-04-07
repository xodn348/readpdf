# readpdf

Convert PDFs to text for token-efficient AI agent reading.

If this saves you tokens, consider giving it a ⭐ on GitHub — it helps others find it.

## Why

Reading PDFs with vision costs 100–500 tokens per page. Converting to text first lets any AI agent read only the sections it needs — saving **up to 90% of tokens**.

## Quick Start

**1. Install the dependency:**
```bash
# macOS
brew install poppler

# Linux
apt install poppler-utils
```

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
