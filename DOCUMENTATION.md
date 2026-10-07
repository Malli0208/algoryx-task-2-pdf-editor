# PDF Editor Application – Project Documentation

## 1. Project Overview

The **PDF Editor Application** is a Python-based desktop application designed to provide common PDF editing and management operations through a graphical user interface.

The project was developed as part of the **Algoryx Python Internship – Week 2 Task 2**.

The application provides multiple PDF operations including merging, splitting, rotating, deleting, reordering, text extraction, image/PDF conversion, watermarking, password protection, and page preview.

---

## 2. Objectives

The main objectives of the project are:

- Develop a desktop-based PDF editor using Python
- Provide a clean graphical user interface
- Implement multiple PDF manipulation features
- Follow object-oriented programming principles
- Maintain a modular project structure
- Implement logging and exception handling
- Provide an executable Windows build
- Document the project clearly

---

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Tkinter | Graphical user interface |
| PyMuPDF | PDF processing, rendering, and conversion |
| pypdf | PDF page manipulation and password protection |
| Pillow | Image processing |
| PyInstaller | Windows executable generation |
| Git | Version control |
| GitHub | Source code hosting |

---

## 4. Functional Features

### 4.1 Merge PDFs

Combines multiple PDF files into a single PDF document.

### 4.2 Split PDF

Splits a PDF into individual page-based PDF files.

### 4.3 Rotate Pages

Rotates selected PDF pages using a specified rotation angle.

### 4.4 Delete Pages

Removes selected pages from a PDF document.

### 4.5 Reorder Pages

Allows pages to be rearranged according to the specified page order.

### 4.6 Extract Text

Extracts text content from the PDF and displays it inside the application.

### 4.7 PDF to Images

Converts PDF pages into image files.

### 4.8 Image to PDF

Converts an image into a PDF document.

### 4.9 Watermark

Adds text-based watermarks to PDF pages.

### 4.10 Password Protection

Creates password-protected PDF documents.

### 4.11 Page Preview

Renders and displays a selected PDF page for preview.

### 4.12 PDF Validation

Checks whether a selected PDF can be opened and processed successfully. If the PDF is invalid or corrupted, the application displays an appropriate error message.

---

## 5. Application Architecture

The project follows a modular and object-oriented structure.

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
```

---

## 6. Module Description

### 6.1 `app.py`

The main entry point of the application.

**Responsibilities:**

- Configure application logging
- Create the Tkinter root window
- Initialize the PDF Editor GUI
- Start the Tkinter event loop

---

### 6.2 `src/gui.py`

Contains the `PDFEditorGUI` class.

**Responsibilities:**

- Build the graphical interface
- Handle user interactions
- Open PDF files
- Display PDF information
- Trigger PDF operations
- Display extracted text
- Display page previews
- Show success and error messages

---

### 6.3 `src/pdf_operations.py`

Contains the `PDFOperations` class responsible for the core PDF processing functionality.

**Responsibilities:**

- Merge PDFs
- Split PDFs
- Rotate pages
- Delete pages
- Reorder pages
- Extract text
- Convert images to PDF
- Convert PDF pages to images
- Add watermarks
- Password-protect PDFs
- Validate PDF files
- Get PDF page counts

---

### 6.4 `src/utils.py`

Contains application utility functions.

**Responsibilities:**

- Configure application logging
- Record informational messages
- Record application errors

---

## 7. Object-Oriented Design

The application uses object-oriented programming to separate the graphical interface from the PDF processing logic.

The main classes are:

```text
PDFOperations
      |
      └── PDF processing operations


PDFEditorGUI
      |
      └── Graphical interface and user interaction
```

This separation makes the application easier to maintain and extend.

---

## 8. Error Handling

The application uses exception handling to prevent unexpected failures during PDF operations.

Examples of handled situations include:

- Invalid PDF files
- Corrupted PDF files
- Missing files
- Invalid page numbers
- Invalid user input
- PDF processing failures

When an operation fails, the GUI displays an appropriate error message instead of terminating unexpectedly.

---

## 9. Logging

The application includes a logging system implemented in `src/utils.py`.

Log files are stored in:

```text
logs/app.log
```

Logging is used to record:

- Application startup
- Informational events
- Application errors

This helps with troubleshooting and debugging.

---

## 10. PDF Validation

Before processing an opened PDF, the application validates the document.

The validation process checks whether the PDF can be successfully opened.

If the PDF is invalid or corrupted:

1. The application detects the problem.
2. The user receives an error message.
3. Further processing of the invalid PDF is prevented.

This provides graceful handling of corrupted or invalid PDF files.

---

## 11. Executable Build

The application can be packaged into a standalone Windows executable using **PyInstaller**.

### Build Command

```powershell
pyinstaller --onefile --windowed --name PDFEditor app.py
```

The generated executable is:

```text
dist/PDFEditor.exe
```

The executable was successfully generated and tested to launch the graphical application.

---

## 12. Installation

### Requirements

- Python 3.11 or later
- Windows operating system
- Required Python packages

### Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## 13. Running the Application

### Activate the Virtual Environment

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### Run the Application

```powershell
python app.py
```

The PDF Editor graphical interface will open.

---

## 14. Running the Executable

After building the application with PyInstaller, the executable will be available at:

```text
dist/PDFEditor.exe
```

The executable can be launched directly without running:

```powershell
python app.py
```

---

## 15. User Workflow

The general workflow of the application is:

```text
Launch Application
       ↓
Open PDF
       ↓
Validate PDF
       ↓
Select Operation
       ↓
Process PDF
       ↓
Choose Output Location
       ↓
Save Result
```

For operations such as **Merge PDFs** and **Image → PDF**, the application allows the required input files to be selected directly.

---

## 16. Security

The application provides password protection functionality for PDF files.

Users can enter a password through the graphical interface and generate a protected PDF document.

---

## 17. Project Quality

The project follows the main development practices required for the internship task:

- Object-oriented programming
- Modular architecture
- Readable folder structure
- Exception handling
- Logging
- Requirements management
- Graphical user interface
- Executable build
- Project documentation
- Git version control

---

## 18. Future Improvements

Potential future improvements include:

- Drag-and-drop PDF support
- Thumbnail-based page navigation
- Dark and light themes
- PDF metadata editing
- Page cropping
- Advanced PDF annotations
- Batch PDF processing
- Additional PDF security options

---

## 19. Internship Information

| Field | Details |
|---|---|
| Program | Algoryx Python Internship |
| Week | Week 2 |
| Task | PDF Editor Application |
| Developer | C. Mallikarjun Reddy |

---

## 20. Conclusion

The **PDF Editor Application** provides a graphical desktop solution for performing common PDF editing, conversion, preview, text extraction, watermarking, and security operations.

The project demonstrates:

- Python programming
- Object-oriented design
- Modular architecture
- GUI development
- PDF processing
- Image processing
- Exception handling
- Logging
- Executable packaging
- Git version control
- Project documentation

The application fulfills the core requirements of the **Algoryx Python Internship – Week 2 PDF Editor Application task**.

---

## Author

**C. Mallikarjun Reddy**

GitHub:  
https://github.com/Malli0208

