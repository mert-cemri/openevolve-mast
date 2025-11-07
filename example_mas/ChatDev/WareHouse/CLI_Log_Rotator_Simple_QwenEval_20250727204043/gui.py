'''
GUI module to handle the graphical user interface for the log rotator application.
'''
import tkinter as tk
from tkinter import messagebox
from log_rotator import LogRotator
class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Log Rotator")
        self.setup_ui()
    def setup_ui(self):
        self.log_file_label = tk.Label(self.master, text="Log File:")
        self.log_file_label.grid(row=0, column=0, padx=10, pady=10)
        self.log_file_entry = tk.Entry(self.master, width=50)
        self.log_file_entry.grid(row=0, column=1, padx=10, pady=10)
        self.compress_var = tk.BooleanVar()
        self.compress_checkbutton = tk.Checkbutton(self.master, text="Compress Old Logs", variable=self.compress_var)
        self.compress_checkbutton.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.delete_var = tk.BooleanVar()
        self.delete_checkbutton = tk.Checkbutton(self.master, text="Delete Logs Older Than", variable=self.delete_var)
        self.delete_checkbutton.grid(row=2, column=0, padx=10, pady=10)
        self.delete_days_entry = tk.Entry(self.master, width=10)
        self.delete_days_entry.grid(row=2, column=1, padx=10, pady=10)
        self.rotate_button = tk.Button(self.master, text="Rotate Logs", command=self.on_rotate_logs)
        self.rotate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
    def on_rotate_logs(self):
        log_file = self.log_file_entry.get()
        compress = self.compress_var.get()
        delete_days_entry = self.delete_days_entry.get()
        if self.delete_var.get():
            if not delete_days_entry.isdigit() or int(delete_days_entry) < 0:
                messagebox.showerror("Error", "Delete logs older than must be a non-negative integer.")
                return
            delete_older_than = int(delete_days_entry)
        else:
            delete_older_than = None
        log_rotator = LogRotator(log_file, compress, delete_older_than)
        try:
            log_rotator.rotate_logs()
            messagebox.showinfo("Success", "Logs rotated successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))