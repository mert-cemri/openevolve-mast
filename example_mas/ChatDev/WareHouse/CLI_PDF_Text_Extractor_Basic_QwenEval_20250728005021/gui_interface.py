'''
Handles the graphical user interface for the PDF text extractor tool.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf_extractor import PDFExtractor
from utils import validate_pdf_path, validate_output_path
class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PDF Text Extractor")
        self.root.geometry("400x200")
        self.pdf_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="PDF File:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.pdf_path, width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_pdf).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self.root, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.output_path, width=40).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_output).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Extract Text", command=self.extract_text).grid(row=2, column=1, pady=20)
    def browse_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if file_path:
            self.pdf_path.set(file_path)
    def browse_output(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            self.output_path.set(file_path)
    def extract_text(self):
        pdf_path = self.pdf_path.get()
        output_path = self.output_path.get()
        if not validate_pdf_path(pdf_path):
            messagebox.showerror("Error", f"Invalid PDF file path '{pdf_path}'")
            return
        if output_path and not validate_output_path(output_path):
            messagebox.showerror("Error", f"Invalid output file path '{output_path}'")
            return
        pdf_extractor = PDFExtractor()
        text = pdf_extractor.extract_text(pdf_path)
        if output_path:
            pdf_extractor.save_text_to_file(text, output_path)
            messagebox.showinfo("Success", f"Text extracted and saved to '{output_path}'")
        else:
            messagebox.showinfo("Extracted Text", text)
    def run(self):
        self.root.mainloop()