# PDF to JSON Converter

Extract text content from PDF files and convert to structured JSON format with page and paragraph preservation.

## Installation

```bash
pip install -r requirements.txt
```

**Dependencies:** pdfplumber, Pillow, cffi

## Usage

```bash
python convert.py input.pdf output.json
python convert.py input.pdf output.json --compact  # minified output
```

**Output structure:**
```json
{
  "source_file": "input.pdf",
  "total_pages": 2,
  "pages": [{"page_number": 1, "text": "...", "paragraphs": [...]}]
}
```

## Known Limitations

- **Text-based PDFs only** - Scanned PDFs (images) are not supported yet
- Complex layouts may not preserve exact formatting

## Future Features (v2.0)

- OCR support for scanned PDFs using pytesseract
- Table extraction and structured data parsing
