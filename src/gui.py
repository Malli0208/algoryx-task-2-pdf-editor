import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

import fitz
from PIL import Image, ImageTk

from src.pdf_operations import PDFOperations
from src.utils import log_error, log_info


class PDFEditorGUI:
    """Graphical user interface for the PDF Editor."""

    def __init__(self, root):
        self.root = root
        self.root.title("PDF Editor")
        self.root.geometry("950x700")
        self.root.minsize(850, 650)

        self.pdf_operations = PDFOperations()
        self.current_pdf = None

        self.create_interface()

    def create_interface(self):
        """Create the main application interface."""

        # ---------------- HEADER ----------------

        header = tk.Frame(self.root)
        header.pack(fill="x", padx=30, pady=(20, 10))

        title = tk.Label(
            header,
            text="PDF Editor",
            font=("Arial", 26, "bold"),
        )
        title.pack()

        subtitle = tk.Label(
            header,
            text="Edit, manage and convert your PDF files",
            font=("Arial", 11),
        )
        subtitle.pack(pady=(5, 0))

        # ---------------- FILE ACTIONS ----------------

        file_frame = tk.LabelFrame(
            self.root,
            text="File",
            padx=15,
            pady=15,
        )
        file_frame.pack(fill="x", padx=30, pady=10)

        tk.Button(
            file_frame,
            text="Open PDF",
            width=20,
            height=2,
            command=self.open_pdf,
        ).pack(side="left", padx=8)

        tk.Button(
            file_frame,
            text="Merge PDFs",
            width=20,
            height=2,
            command=self.merge_pdfs,
        ).pack(side="left", padx=8)

        tk.Button(
            file_frame,
            text="Split PDF",
            width=20,
            height=2,
            command=self.split_pdf,
        ).pack(side="left", padx=8)

        # ---------------- PDF OPERATIONS ----------------

        operations_frame = tk.LabelFrame(
            self.root,
            text="PDF Operations",
            padx=15,
            pady=15,
        )
        operations_frame.pack(
            fill="x",
            padx=30,
            pady=10,
        )

        buttons = [
            ("Page Preview", self.page_preview),
            ("Rotate Pages", self.rotate_pages),
            ("Delete Pages", self.delete_pages),
            ("Reorder Pages", self.reorder_pages),
            ("Extract Text", self.extract_text),
            ("PDF → Images", self.pdf_to_images),
            ("Image → PDF", self.image_to_pdf),
            ("Add Watermark", self.add_watermark),
            ("Password Protect", self.password_protect),
        ]

        for index, (text, command) in enumerate(buttons):
            row = index // 3
            column = index % 3

            tk.Button(
                operations_frame,
                text=text,
                width=24,
                height=2,
                command=command,
            ).grid(
                row=row,
                column=column,
                padx=8,
                pady=8,
            )

        # ---------------- STATUS ----------------

        status_frame = tk.LabelFrame(
            self.root,
            text="Current PDF",
            padx=15,
            pady=10,
        )
        status_frame.pack(
            fill="x",
            padx=30,
            pady=10,
        )

        self.status_label = tk.Label(
            status_frame,
            text="No PDF selected",
            anchor="w",
        )
        self.status_label.pack(fill="x")

        self.page_info = tk.Label(
            status_frame,
            text="Pages: -",
            anchor="w",
        )
        self.page_info.pack(fill="x", pady=(5, 0))

        # ---------------- TEXT OUTPUT ----------------

        text_frame = tk.LabelFrame(
            self.root,
            text="Extracted Text",
            padx=10,
            pady=10,
        )
        text_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(5, 20),
        )

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side="right", fill="y")

        self.text_area = tk.Text(
            text_frame,
            wrap="word",
            yscrollcommand=scrollbar.set,
        )
        self.text_area.pack(
            fill="both",
            expand=True,
        )

        scrollbar.config(
            command=self.text_area.yview
        )

    def open_pdf(self):
        """Open and validate a PDF file."""

        file_path = filedialog.askopenfilename(
            title="Select PDF",
            filetypes=[("PDF Files", "*.pdf")],
        )

        if not file_path:
            return

        try:
            valid, message = self.pdf_operations.validate_pdf(
                file_path
            )

            if not valid:
                messagebox.showerror(
                    "Invalid PDF",
                    message,
                )
                return

            page_count = self.pdf_operations.get_page_count(
                file_path
            )

            self.current_pdf = file_path

            self.status_label.config(
                text=f"Selected: {file_path}"
            )

            self.page_info.config(
                text=f"Pages: {page_count}"
            )

            log_info(f"Opened PDF: {file_path}")

            messagebox.showinfo(
                "Success",
                f"PDF opened successfully.\nPages: {page_count}",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to open PDF.\n\n{error}",
            )

    def merge_pdfs(self):
        """Merge multiple PDF files."""

        files = filedialog.askopenfilenames(
            title="Select PDFs to Merge",
            filetypes=[("PDF Files", "*.pdf")],
        )

        if not files:
            return

        output_file = filedialog.asksaveasfilename(
            title="Save Merged PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
        )

        if not output_file:
            return

        try:
            self.pdf_operations.merge_pdfs(
                files,
                output_file,
            )

            log_info(f"Merged PDFs into: {output_file}")

            messagebox.showinfo(
                "Success",
                "PDFs merged successfully.",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to merge PDFs.\n\n{error}",
            )

    def split_pdf(self):
        """Split the selected PDF into individual pages."""

        if not self.require_pdf():
            return

        output_folder = filedialog.askdirectory(
            title="Select Output Folder"
        )

        if not output_folder:
            return

        try:
            files = self.pdf_operations.split_pdf(
                self.current_pdf,
                output_folder,
            )

            log_info(
                f"PDF split into {len(files)} pages."
            )

            messagebox.showinfo(
                "Success",
                f"PDF split successfully.\n"
                f"Created {len(files)} files.",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to split PDF.\n\n{error}",
            )

    def page_preview(self):
        """Display a visual preview of a selected PDF page."""

        if not self.require_pdf():
            return

        try:
            page_number = simpledialog.askinteger(
                "Page Preview",
                "Enter page number:",
                minvalue=1,
                maxvalue=self.pdf_operations.get_page_count(
                    self.current_pdf
                ),
            )

            if not page_number:
                return

            document = fitz.open(self.current_pdf)

            try:
                page = document.load_page(page_number - 1)

                pixmap = page.get_pixmap(
                    matrix=fitz.Matrix(1.5, 1.5)
                )

                image = Image.frombytes(
                    "RGB",
                    [pixmap.width, pixmap.height],
                    pixmap.samples,
                )

            finally:
                document.close()

            preview_window = tk.Toplevel(self.root)
            preview_window.title(
                f"Page Preview - Page {page_number}"
            )
            preview_window.geometry("700x850")

            image.thumbnail((650, 750))

            photo = ImageTk.PhotoImage(image)

            preview_label = tk.Label(
                preview_window,
                image=photo,
            )

            preview_label.image = photo
            preview_label.pack(
                expand=True,
                padx=20,
                pady=20,
            )

            tk.Label(
                preview_window,
                text=f"Page {page_number}",
                font=("Arial", 12, "bold"),
            ).pack(pady=10)

            log_info(
                f"Preview displayed for page {page_number}."
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Preview Error",
                f"Unable to preview the selected page.\n\n{error}",
            )

    def rotate_pages(self):
        """Rotate selected pages."""

        if not self.require_pdf():
            return

        pages = simpledialog.askstring(
            "Rotate Pages",
            "Enter page numbers separated by commas:\n"
            "Example: 1,2,3",
        )

        if not pages:
            return

        angle = simpledialog.askinteger(
            "Rotation Angle",
            "Enter rotation angle:\n90, 180 or 270",
        )

        if angle not in (90, 180, 270):
            messagebox.showerror(
                "Invalid Angle",
                "Please enter 90, 180 or 270.",
            )
            return

        try:
            page_numbers = [
                int(page.strip())
                for page in pages.split(",")
            ]

            output_file = filedialog.asksaveasfilename(
                title="Save Rotated PDF",
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
            )

            if not output_file:
                return

            self.pdf_operations.rotate_pages(
                self.current_pdf,
                output_file,
                page_numbers,
                angle,
            )

            messagebox.showinfo(
                "Success",
                "Pages rotated successfully.",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to rotate pages.\n\n{error}",
            )

    def delete_pages(self):
        """Delete selected pages."""

        if not self.require_pdf():
            return

        pages = simpledialog.askstring(
            "Delete Pages",
            "Enter page numbers separated by commas:",
        )

        if not pages:
            return

        try:
            page_numbers = [
                int(page.strip())
                for page in pages.split(",")
            ]

            output_file = filedialog.asksaveasfilename(
                title="Save PDF",
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
            )

            if not output_file:
                return

            self.pdf_operations.delete_pages(
                self.current_pdf,
                output_file,
                page_numbers,
            )

            messagebox.showinfo(
                "Success",
                "Pages deleted successfully.",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to delete pages.\n\n{error}",
            )

    def reorder_pages(self):
        """Reorder pages."""

        if not self.require_pdf():
            return

        order = simpledialog.askstring(
            "Reorder Pages",
            "Enter page order.\nExample: 3,1,2",
        )

        if not order:
            return

        try:
            page_order = [
                int(page.strip())
                for page in order.split(",")
            ]

            output_file = filedialog.asksaveasfilename(
                title="Save Reordered PDF",
                defaultextension=".pdf",
                filetypes=[("PDF Files", "*.pdf")],
            )

            if not output_file:
                return

            self.pdf_operations.reorder_pages(
                self.current_pdf,
                output_file,
                page_order,
            )

            messagebox.showinfo(
                "Success",
                "Pages reordered successfully.",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to reorder pages.\n\n{error}",
            )

    def extract_text(self):
        """Extract text from the selected PDF."""

        if not self.require_pdf():
            return

        try:
            text = self.pdf_operations.extract_text(
                self.current_pdf
            )

            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, text)

            log_info("Text extracted successfully.")

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to extract text.\n\n{error}",
            )

    def pdf_to_images(self):
        """Convert PDF pages to images."""

        if not self.require_pdf():
            return

        output_folder = filedialog.askdirectory(
            title="Select Output Folder"
        )

        if not output_folder:
            return

        try:
            files = self.pdf_operations.pdf_to_images(
                self.current_pdf,
                output_folder,
            )

            messagebox.showinfo(
                "Success",
                f"Created {len(files)} images.",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to convert PDF.\n\n{error}",
            )

    def image_to_pdf(self):
        """Convert an image to PDF."""

        image_file = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("Image Files", "*.png *.jpg *.jpeg"),
            ],
        )

        if not image_file:
            return

        output_file = filedialog.asksaveasfilename(
            title="Save PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
        )

        if not output_file:
            return

        try:
            self.pdf_operations.image_to_pdf(
                image_file,
                output_file,
            )

            messagebox.showinfo(
                "Success",
                "Image converted to PDF successfully.",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to convert image.\n\n{error}",
            )

    def add_watermark(self):
        """Add a text watermark."""

        if not self.require_pdf():
            return

        watermark = simpledialog.askstring(
            "Watermark",
            "Enter watermark text:",
        )

        if not watermark:
            return

        output_file = filedialog.asksaveasfilename(
            title="Save Watermarked PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
        )

        if not output_file:
            return

        try:
            self.pdf_operations.add_watermark(
                self.current_pdf,
                output_file,
                watermark,
            )

            messagebox.showinfo(
                "Success",
                "Watermark added successfully.",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to add watermark.\n\n{error}",
            )

    def password_protect(self):
        """Protect a PDF with a password."""

        if not self.require_pdf():
            return

        password = simpledialog.askstring(
            "Password Protection",
            "Enter password:",
            show="*",
        )

        if not password:
            return

        output_file = filedialog.asksaveasfilename(
            title="Save Protected PDF",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
        )

        if not output_file:
            return

        try:
            self.pdf_operations.protect_with_password(
                self.current_pdf,
                output_file,
                password,
            )

            messagebox.showinfo(
                "Success",
                "PDF password protection added.",
            )

        except Exception as error:
            log_error(error)
            messagebox.showerror(
                "Error",
                f"Unable to protect PDF.\n\n{error}",
            )

    def require_pdf(self):
        """Check whether a PDF is currently selected."""

        if not self.current_pdf:
            messagebox.showwarning(
                "No PDF Selected",
                "Please open a PDF first.",
            )
            return False

        return True