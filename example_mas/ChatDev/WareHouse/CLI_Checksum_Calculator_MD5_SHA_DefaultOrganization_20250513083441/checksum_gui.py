'''
This module contains the ChecksumGUI class for the graphical user interface.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from checksum_calculator import ChecksumCalculator
class ChecksumGUI:
    def __init__(self):
        '''
        Initialize the GUI components.
        '''
        self.root = tk.Tk()
        self.root.title("Checksum Calculator")
        self.file_path = tk.StringVar()
        tk.Label(self.root, text="Select a file:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_file).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Calculate Checksums", command=self.calculate_checksums).grid(row=1, column=0, columnspan=3, pady=10)
        self.md5_result = tk.StringVar()
        self.sha256_result = tk.StringVar()
        tk.Label(self.root, text="MD5:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.md5_result, width=50, state='readonly').grid(row=2, column=1, columnspan=2, padx=10, pady=10)
        tk.Label(self.root, text="SHA256:").grid(row=3, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.sha256_result, width=50, state='readonly').grid(row=3, column=1, columnspan=2, padx=10, pady=10)
    def browse_file(self):
        '''
        Open a file dialog to select a file.
        '''
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path.set(file_path)
    def calculate_checksums(self):
        '''
        Trigger checksum calculation and display results.
        '''
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showerror("Error", "Please select a file first.")
            return
        try:
            md5_checksum = ChecksumCalculator.calculate_md5(file_path)
            sha256_checksum = ChecksumCalculator.calculate_sha256(file_path)
            self.md5_result.set(md5_checksum)
            self.sha256_result.set(sha256_checksum)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    def run(self):
        '''
        Run the main loop of the GUI.
        '''
        self.root.mainloop()