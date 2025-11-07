'''
ChecksumGUI class to handle the graphical user interface for the Checksum Utility.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from checksum_calculator import ChecksumCalculator
class ChecksumGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Checksum Utility")
        self.root.geometry("400x200")
        self.file_path = tk.StringVar()
        self.label = tk.Label(self.root, text="Select a file to calculate checksums:")
        self.label.pack(pady=10)
        self.entry = tk.Entry(self.root, textvariable=self.file_path, width=50)
        self.entry.pack(pady=5)
        self.button_browse = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.button_browse.pack(pady=5)
        self.button_calculate = tk.Button(self.root, text="Calculate", command=self.calculate_checksums)
        self.button_calculate.pack(pady=10)
    def browse_file(self):
        """Open a file dialog to select a file."""
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)
    def calculate_checksums(self):
        """Calculate and display the MD5 and SHA256 checksums."""
        file_path = self.file_path.get()
        if not file_path:
            messagebox.showwarning("Warning", "Please select a file.")
            return
        calculator = ChecksumCalculator()
        md5_checksum = calculator.calculate_md5(file_path)
        sha256_checksum = calculator.calculate_sha256(file_path)
        messagebox.showinfo("Checksums", f"MD5: {md5_checksum}\nSHA256: {sha256_checksum}")
    def run(self):
        """Run the GUI application."""
        self.root.mainloop()