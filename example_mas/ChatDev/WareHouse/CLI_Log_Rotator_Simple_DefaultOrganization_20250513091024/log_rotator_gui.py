'''
Module for the graphical user interface of the Log Rotator application.
'''
import tkinter as tk
from tkinter import messagebox
class LogRotatorGUI:
    def __init__(self, log_rotator):
        self.log_rotator = log_rotator
        self.root = tk.Tk()
        self.root.title("Log Rotator")
    def setup_gui(self):
        # Create and place widgets
        tk.Label(self.root, text="Log Rotator").pack(pady=10)
        rotate_button = tk.Button(self.root, text="Rotate Logs", command=self.rotate_logs)
        rotate_button.pack(pady=5)
        compress_var = tk.BooleanVar(value=self.log_rotator.compress)
        compress_check = tk.Checkbutton(self.root, text="Compress Logs", variable=compress_var, command=self.toggle_compress)
        compress_check.pack(pady=5)
        delete_days_label = tk.Label(self.root, text="Delete logs older than (days):")
        delete_days_label.pack(pady=5)
        self.delete_days_entry = tk.Entry(self.root)
        self.delete_days_entry.insert(0, str(self.log_rotator.delete_days))
        self.delete_days_entry.pack(pady=5)
    def toggle_compress(self):
        self.log_rotator.compress = not self.log_rotator.compress
    def rotate_logs(self):
        try:
            self.log_rotator.delete_days = int(self.delete_days_entry.get())
            self.log_rotator.execute()
            messagebox.showinfo("Success", "Log rotation completed successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.root.mainloop()