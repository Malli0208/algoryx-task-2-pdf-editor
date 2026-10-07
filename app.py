import tkinter as tk

from src.gui import PDFEditorGUI
from src.utils import setup_logging


def main():
    setup_logging()

    root = tk.Tk()
    PDFEditorGUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()