'''
Handles graphical user interface interactions.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from file_reader import FileReader
from text_diff import TextDiff
class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Difference Tool")
        self.file1_path = ""
        self.file2_path = ""
        self.create_widgets()
    def create_widgets(self):
        self.label1 = tk.Label(self.root, text="File 1:")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.entry1 = tk.Entry(self.root, width=50)
        self.entry1.grid(row=0, column=1, padx=10, pady=10)
        self.button1 = tk.Button(self.root, text="Browse", command=self.browse_file1)
        self.button1.grid(row=0, column=2, padx=10, pady=10)
        self.label2 = tk.Label(self.root, text="File 2:")
        self.label2.grid(row=1, column=0, padx=10, pady=10)
        self.entry2 = tk.Entry(self.root, width=50)
        self.entry2.grid(row=1, column=1, padx=10, pady=10)
        self.button2 = tk.Button(self.root, text="Browse", command=self.browse_file2)
        self.button2.grid(row=1, column=2, padx=10, pady=10)
        self.compare_button = tk.Button(self.root, text="Compare", command=self.compare_files)
        self.compare_button.grid(row=2, column=1, pady=20)
        self.text_area = tk.Text(self.root, wrap=tk.WORD, height=20, width=80)
        self.text_area.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    def browse_file1(self):
        self.file1_path = filedialog.askopenfilename()
        self.entry1.delete(0, tk.END)
        self.entry1.insert(0, self.file1_path)
    def browse_file2(self):
        self.file2_path = filedialog.askopenfilename()
        self.entry2.delete(0, tk.END)
        self.entry2.insert(0, self.file2_path)
    def compare_files(self):
        if not self.file1_path or not self.file2_path:
            messagebox.showwarning("Input Error", "Please select both files.")
            return
        file1_reader = FileReader(self.file1_path)
        file2_reader = FileReader(self.file2_path)
        file1_content = file1_reader.get_content()
        file2_content = file2_reader.get_content()
        text_diff = TextDiff(file1_content, file2_content)
        diff_lines = text_diff.compare()
        self.display_diff(diff_lines)
    def display_diff(self, diff_lines):
        self.text_area.delete(1.0, tk.END)
        if not diff_lines:
            self.text_area.insert(tk.END, "No differences found.")
        else:
            self.text_area.insert(tk.END, "Differences found:\n")
            for line_number, line1, line2 in diff_lines:
                self.text_area.insert(tk.END, f"Line {line_number}:\n")
                self.text_area.insert(tk.END, f"  File 1: {line1}\n")
                self.text_area.insert(tk.END, f"  File 2: {line2}\n")
    def run(self):
        self.root.mainloop()