#!/usr/bin/env python3
"""
PDF to JSON Converter
Extracts text content from PDF files and converts to structured JSON format.
"""

import argparse
import json
import sys
from pathlib import Path
import pdfplumber


def extract_text_from_pdf(pdf_path):
    """
    Extract text content from PDF file with structure preservation.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        Dictionary containing structured PDF content
    """
    result = {
        "source_file": str(pdf_path),
        "total_pages": 0,
        "pages": []
    }

    try:
        with pdfplumber.open(pdf_path) as pdf:
            result["total_pages"] = len(pdf.pages)

            for page_num, page in enumerate(pdf.pages, start=1):
                # Extract text from the page
                text = page.extract_text()

                # Split into paragraphs (separated by double newlines or more)
                paragraphs = []
                if text:
                    # Split by empty lines to identify paragraphs
                    raw_paragraphs = text.split('\n\n')
                    paragraphs = [p.strip() for p in raw_paragraphs if p.strip()]

                # Get page dimensions for metadata
                page_data = {
                    "page_number": page_num,
                    "width": page.width,
                    "height": page.height,
                    "text": text if text else "",
                    "paragraphs": paragraphs,
                    "paragraph_count": len(paragraphs)
                }

                result["pages"].append(page_data)

    except Exception as e:
        print(f"Error processing PDF: {e}", file=sys.stderr)
        sys.exit(1)

    return result


def save_to_json(data, output_path, pretty=True):
    """
    Save data to JSON file.

    Args:
        data: Dictionary to save
        output_path: Path to output JSON file
        pretty: Whether to format JSON with indentation
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            if pretty:
                json.dump(data, f, indent=2, ensure_ascii=False)
            else:
                json.dump(data, f, ensure_ascii=False)
        print(f"Successfully converted PDF to JSON: {output_path}")
    except Exception as e:
        print(f"Error saving JSON: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF files to structured JSON format"
    )
    parser.add_argument(
        "input_pdf",
        help="Path to input PDF file"
    )
    parser.add_argument(
        "output_json",
        help="Path to output JSON file"
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Output compact JSON without indentation"
    )

    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input_pdf)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    if not input_path.suffix.lower() == '.pdf':
        print(f"Error: Input file must be a PDF: {input_path}", file=sys.stderr)
        sys.exit(1)

    # Extract text from PDF
    print(f"Processing PDF: {input_path}")
    data = extract_text_from_pdf(input_path)

    # Save to JSON
    output_path = Path(args.output_json)
    save_to_json(data, output_path, pretty=not args.compact)

    # Print summary
    print(f"\nSummary:")
    print(f"  Pages processed: {data['total_pages']}")
    total_paragraphs = sum(p['paragraph_count'] for p in data['pages'])
    print(f"  Total paragraphs: {total_paragraphs}")


if __name__ == "__main__":
    main()
