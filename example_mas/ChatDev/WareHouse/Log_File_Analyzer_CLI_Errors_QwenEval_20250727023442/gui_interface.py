'''
GUIInterface class for handling graphical input and output using tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from log_analyzer import LogAnalyzer
class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Log File Analyzer")
        self.log_file_label = tk.Label(self.root, text="Log File:")
        self.log_file_label.grid(row=0, column=0, padx=10, pady=10)
        self.log_file_entry = tk.Entry(self.root, width=50)
        self.log_file_entry.grid(row=0, column=1, padx=10, pady=10)
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)
        self.pattern_label = tk.Label(self.root, text="Pattern:")
        self.pattern_label.grid(row=1, column=0, padx=10, pady=10)
        self.pattern_entry = tk.Entry(self.root, width=50)
        self.pattern_entry.grid(row=1, column=1, padx=10, pady=10)
        self.analyze_button = tk.Button(self.root, text="Analyze", command=self.analyze_log)
        self.analyze_button.grid(row=2, column=1, padx=10, pady=10)
    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.log_file_entry.delete(0, tk.END)
        self.log_file_entry.insert(0, file_path)
    def analyze_log(self):
        log_file = self.log_file_entry.get()
        pattern = self.pattern_entry.get()
        if not log_file or not pattern:
            messagebox.showerror("Error", "Please specify both log file and pattern.")
            return
        analyzer = LogAnalyzer(log_file, pattern)
        count = analyzer.count_pattern()
        messagebox.showinfo("Result", f"Number of lines containing '{pattern}': {count}")
    def run(self):
        self.root.mainloop()