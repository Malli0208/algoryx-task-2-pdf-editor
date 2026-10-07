# PDF Editor Application

A Python-based desktop PDF Editor with a clean graphical user interface for performing common PDF operations efficiently.

This project was developed as part of the **Algoryx Python Internship – Week 2 Task 2**.

---

## 📌 Project Overview

The PDF Editor is a desktop application built using Python that provides multiple PDF management and editing features through an easy-to-use graphical interface.

The application supports PDF manipulation, page management, text extraction, image/PDF conversion, watermarking, password protection, and page preview.

---

## ✨ Features

### PDF Management
- Merge multiple PDF files
- Split a PDF into individual pages
- Rotate selected pages
- Delete selected pages
- Reorder PDF pages

### Content & Conversion
- Extract text from PDF files
- Convert PDF pages to images
- Convert images to PDF

### Security & Customization
- Add text watermarks
- Password-protect PDF files

### Preview & Validation
- Preview individual PDF pages
- Display current PDF information
- Validate PDF files before processing
- Graceful handling of invalid or corrupted PDFs

---

## 🖥️ Application Interface

The application provides a graphical interface containing:

- File selection
- PDF operations
- Page preview
- Current PDF information
- Extracted text display
- Error and success notifications

---

## 🛠️ Technologies Used

- **Python 3.11+**
- **Tkinter** – Graphical User Interface
- **PyMuPDF (fitz)** – PDF rendering and manipulation
- **pypdf** – PDF page operations and encryption
- **Pillow** – Image processing
- **PyInstaller** – Executable generation
- **Git & GitHub** – Version control and project hosting

---

## 📂 Project Structure

```text
algoryx-task-2-pdf-editor/
│
├── src/
│   ├── __init__.py
│   ├── pdf_operations.py
│   ├── gui.py
│   └── utils.py
│
├── logs/
├── output/
│
├── app.py
├── requirements.txt
├── README.md
├── DOCUMENTATION.md
├── .gitignore
└── LICENSE

## 📖 How to Use

### Open PDF

1. Click **Open PDF**
2. Select a PDF file
3. The application loads the PDF and displays its page count

### Page Preview

1. Open a PDF
2. Click **Page Preview**
3. Enter the page number
4. The selected page is displayed

### Merge PDFs

1. Click **Merge PDFs**
2. Select multiple PDF files
3. Choose the output location
4. The PDFs are combined into one file

### Split PDF

1. Open a PDF
2. Click **Split PDF**
3. Select the output folder
4. Individual pages are created as separate PDF files

### Rotate Pages

1. Open a PDF
2. Click **Rotate Pages**
3. Enter the required page numbers
4. Enter the rotation angle
5. Save the modified PDF

### Delete Pages

1. Open a PDF
2. Click **Delete Pages**
3. Enter the page numbers to remove
4. Save the resulting PDF

### Reorder Pages

1. Open a PDF
2. Click **Reorder Pages**
3. Enter the desired page order
4. Save the reordered PDF

### Extract Text

1. Open a PDF
2. Click **Extract Text**
3. Extracted text is displayed inside the application

### PDF → Images

1. Open a PDF
2. Click **PDF → Images**
3. Select an output folder
4. PDF pages are converted into image files

### Image → PDF

1. Click **Image → PDF**
2. Select an image
3. Choose the output location
4. A PDF file is generated from the image

### Add Watermark

1. Open a PDF
2. Click **Add Watermark**
3. Enter the watermark text
4. Select the output location

### Password Protect

1. Open a PDF
2. Click **Password Protect**
3. Enter a password
4. Save the protected PDF

---

## 🛡️ Error Handling

The application includes error handling for operations such as:

- Invalid PDF files
- Corrupted PDF files
- Missing files
- Invalid page numbers
- Incorrect user input
- Failed PDF operations

Application errors are also recorded through the logging system.

---

## 📝 Logging

Application logs are stored in:

```text
logs/app.log

