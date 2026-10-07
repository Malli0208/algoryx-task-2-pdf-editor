from pathlib import Path

import fitz
from pypdf import PdfReader, PdfWriter

from src.utils import log_error, log_info
class PDFOperations:
    """Provides PDF editing and conversion operations."""

    def merge_pdfs(self, input_files, output_file):
        """Merge multiple PDF files into a single PDF."""
        writer = PdfWriter()

        for file in input_files:
            reader = PdfReader(file)

            for page in reader.pages:
                writer.add_page(page)

        with open(output_file, "wb") as output:
            writer.write(output)

    def split_pdf(self, input_file, output_folder):
        """Split a PDF into individual page files."""
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

        reader = PdfReader(input_file)
        output_files = []

        for index, page in enumerate(reader.pages, start=1):
            writer = PdfWriter()
            writer.add_page(page)

            output_file = output_folder / f"page_{index}.pdf"

            with open(output_file, "wb") as output:
                writer.write(output)

            output_files.append(str(output_file))

        return output_files

    def rotate_pages(self, input_file, output_file, page_numbers, angle):
        """Rotate selected pages by the specified angle."""
        reader = PdfReader(input_file)
        writer = PdfWriter()

        selected_pages = set(page_numbers)

        for index, page in enumerate(reader.pages, start=1):
            if index in selected_pages:
                page.rotate(angle)

            writer.add_page(page)

        with open(output_file, "wb") as output:
            writer.write(output)

    def delete_pages(self, input_file, output_file, page_numbers):
        """Delete selected pages from a PDF."""
        reader = PdfReader(input_file)
        writer = PdfWriter()

        pages_to_delete = set(page_numbers)

        for index, page in enumerate(reader.pages, start=1):
            if index not in pages_to_delete:
                writer.add_page(page)

        with open(output_file, "wb") as output:
            writer.write(output)

    def reorder_pages(self, input_file, output_file, page_order):
        """Reorder PDF pages according to the supplied page order."""
        reader = PdfReader(input_file)
        writer = PdfWriter()

        for page_number in page_order:
            writer.add_page(reader.pages[page_number - 1])

        with open(output_file, "wb") as output:
            writer.write(output)

    def extract_text(self, input_file):
        """Extract text from all pages of a PDF."""
        document = fitz.open(input_file)
        extracted_text = []

        try:
            for page in document:
                extracted_text.append(page.get_text())
        finally:
            document.close()

        return "\n".join(extracted_text)

    def image_to_pdf(self, image_file, output_file):
        """Convert an image into a PDF."""
        image = fitz.open(image_file)

        try:
            pdf = fitz.open()
            pdf_bytes = image.convert_to_pdf()
            pdf_document = fitz.open("pdf", pdf_bytes)
            pdf.insert_pdf(pdf_document)

            pdf.save(output_file)

            pdf_document.close()
            pdf.close()
        finally:
            image.close()

    def pdf_to_images(self, input_file, output_folder):
        """Convert every PDF page into a PNG image."""
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

        document = fitz.open(input_file)
        output_files = []

        try:
            for index, page in enumerate(document, start=1):
                pixmap = page.get_pixmap()
                output_file = output_folder / f"page_{index}.png"

                pixmap.save(str(output_file))
                output_files.append(str(output_file))
        finally:
            document.close()

        return output_files

    def add_watermark(self, input_file, output_file, watermark_text):
        """Add text watermark to every page."""
        document = fitz.open(input_file)

        try:
            for page in document:
                page.insert_text(
                    (50, 50),
                    watermark_text,
                    fontsize=20,
                    rotate=0,
                    overlay=True,
                )

            document.save(output_file)
        finally:
            document.close()

    def protect_with_password(self, input_file, output_file, password):
        """Protect a PDF with a password."""
        reader = PdfReader(input_file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        with open(output_file, "wb") as output:
            writer.write(output)

    def validate_pdf(self, input_file):
        """Validate whether a PDF can be opened successfully."""

        try:
            document = fitz.open(input_file)

            if document.page_count == 0:
                document.close()
                return False, "The PDF contains no pages."

            document.close()

            log_info(f"PDF validation successful: {input_file}")
            return True, "PDF is valid."

        except (fitz.FileDataError, fitz.EmptyFileError) as error:
            log_error(error)
            return False, "The PDF is corrupted or cannot be read."

        except Exception as error:
            log_error(error)
            return False, f"Unable to validate PDF: {error}"

    def get_page_count(self, input_file):
        """Return the number of pages in a PDF."""
        document = fitz.open(input_file)

        try:
            return len(document)
        finally:
            document.close()