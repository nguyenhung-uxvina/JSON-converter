#!/usr/bin/env python3
"""
Create a sample PDF for testing the converter
"""

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def create_test_pdf(filename="test_sample.pdf"):
    """Create a simple multi-page PDF with paragraphs"""
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Page 1
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Test Document - Page 1")

    c.setFont("Helvetica", 12)
    y_position = height - 100

    paragraphs_page1 = [
        "This is the first paragraph of the test document. It contains some sample text to test the PDF to JSON converter.",
        "This is the second paragraph. It demonstrates how the converter handles multiple paragraphs on a single page.",
        "The third paragraph shows that the tool can extract structured content from PDF files."
    ]

    for para in paragraphs_page1:
        c.drawString(50, y_position, para)
        y_position -= 60

    c.showPage()

    # Page 2
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Test Document - Page 2")

    c.setFont("Helvetica", 12)
    y_position = height - 100

    paragraphs_page2 = [
        "This is page 2 of the test document. It contains different content to verify multi-page extraction.",
        "The converter should properly handle page boundaries and maintain document structure.",
        "Each page is processed independently while maintaining the overall document organization."
    ]

    for para in paragraphs_page2:
        c.drawString(50, y_position, para)
        y_position -= 60

    c.showPage()

    # Save the PDF
    c.save()
    print(f"Created test PDF: {filename}")


if __name__ == "__main__":
    create_test_pdf()
