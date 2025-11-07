'''
Handles graphical user interactions using tkinter for the file archiver application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
class GUI:
    def __init__(self, archiver):
        self.archiver = archiver
    def create_gui(self):
        '''
        Initializes and runs the GUI application.
        '''
        self.root = tk.Tk()
        self.root.title("File Archiver")
        # Create buttons for creating and extracting ZIP files
        create_btn = tk.Button(self.root, text="Create ZIP", command=self.create_zip)
        create_btn.pack(pady=10)
        extract_btn = tk.Button(self.root, text="Extract ZIP", command=self.extract_zip)
        extract_btn.pack(pady=10)
        self.root.mainloop()
    def create_zip(self):
        '''
        Opens a file dialog to select files and create a ZIP archive.
        '''
        files = filedialog.askopenfilenames(title="Select files to ZIP")
        if files:
            zip_name = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")])
            if zip_name:
                self.archiver.create_zip(zip_name, files)
                messagebox.showinfo("Success", f"Created ZIP file: {zip_name}")
    def extract_zip(self):
        '''
        Opens a file dialog to select a ZIP file and extract its contents.
        '''
        zip_name = filedialog.askopenfilename(title="Select ZIP file", filetypes=[("ZIP files", "*.zip")])
        if zip_name:
            extract_to = filedialog.askdirectory(title="Select directory to extract to")
            if extract_to:
                self.archiver.extract_zip(zip_name, extract_to)
                messagebox.showinfo("Success", f"Extracted ZIP file to: {extract_to}")