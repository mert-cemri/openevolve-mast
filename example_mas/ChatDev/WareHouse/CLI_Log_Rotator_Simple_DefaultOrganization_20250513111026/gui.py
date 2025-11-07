'''
GUI for the log rotator application using Tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from log_rotator import LogRotator
def create_gui():
    def rotate():
        log_file = file_entry.get()
        if not log_file:
            messagebox.showerror("Error", "Please select a log file.")
            return
        rotator = LogRotator(log_file)
        rotator.rotate_log()
        if compress_var.get():
            rotator.compress_logs()
        if delete_var.get():
            days = int(days_entry.get())
            rotator.delete_old_logs(days)
        messagebox.showinfo("Success", "Log rotation completed.")
    def browse_file():
        filename = filedialog.askopenfilename(title="Select Log File")
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)
    root = tk.Tk()
    root.title("Log Rotator")
    tk.Label(root, text="Log File:").grid(row=0, column=0, padx=5, pady=5)
    file_entry = tk.Entry(root, width=50)
    file_entry.grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=5, pady=5)
    compress_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Compress Logs", variable=compress_var).grid(row=1, column=0, columnspan=2, padx=5, pady=5)
    delete_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Delete Logs Older Than N Days", variable=delete_var).grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    tk.Label(root, text="Days:").grid(row=3, column=0, padx=5, pady=5)
    days_entry = tk.Entry(root, width=5)
    days_entry.grid(row=3, column=1, padx=5, pady=5)
    tk.Button(root, text="Rotate Logs", command=rotate).grid(row=4, column=0, columnspan=3, padx=5, pady=10)
    root.mainloop()