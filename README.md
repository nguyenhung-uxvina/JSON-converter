# PDF to JSON Converter

A simple command-line tool to extract text content from PDF files and convert it to structured JSON format.

## Features

- Extract text content from text-based PDF files
- Preserve document structure (pages, paragraphs)
- Clean JSON output with metadata
- Command-line interface
- Support for both pretty-printed and compact JSON output

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd JSON-converter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Basic usage:
```bash
python convert.py input.pdf output.json
```

With compact JSON output:
```bash
python convert.py input.pdf output.json --compact
```

### Command-line Arguments

- `input_pdf` - Path to the input PDF file (required)
- `output_json` - Path to the output JSON file (required)
- `--compact` - Output compact JSON without indentation (optional)

## Output Format

The converter generates JSON with the following structure:

```json
{
  "source_file": "input.pdf",
  "total_pages": 3,
  "pages": [
    {
      "page_number": 1,
      "width": 612.0,
      "height": 792.0,
      "text": "Full page text...",
      "paragraphs": [
        "First paragraph text...",
        "Second paragraph text..."
      ],
      "paragraph_count": 2
    }
  ]
}
```

### JSON Fields

- `source_file`: Original PDF filename
- `total_pages`: Total number of pages in the PDF
- `pages`: Array of page objects, each containing:
  - `page_number`: Page number (1-indexed)
  - `width`: Page width in points
  - `height`: Page height in points
  - `text`: Full text content of the page
  - `paragraphs`: Array of paragraph strings
  - `paragraph_count`: Number of paragraphs on the page

## Requirements

- Python 3.7+
- pdfplumber
- Pillow

## Limitations

- Currently supports text-based PDFs only
- Scanned PDFs (images) require OCR (future enhancement)
- Complex layouts may not preserve exact formatting

## Future Enhancements

- [ ] OCR support for scanned PDFs (using pytesseract)
- [ ] Table extraction
- [ ] Image extraction
- [ ] Better paragraph detection
- [ ] Section/heading detection
- [ ] Multiple output formats (CSV, XML)

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
