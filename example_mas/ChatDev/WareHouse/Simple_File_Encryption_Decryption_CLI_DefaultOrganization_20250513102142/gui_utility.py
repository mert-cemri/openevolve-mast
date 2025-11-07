'''
Provides a graphical user interface for the file encryption and decryption utility.
'''
# gui_utility.py
import tkinter as tk
from tkinter import filedialog, messagebox
from file_encryptor import FileEncryptor
import os
class GUIUtility:
    def __init__(self):
        self.encryptor = FileEncryptor()
    def create_gui(self):
        # Check if the DISPLAY environment variable is set
        if os.environ.get('DISPLAY', '') == '':
            print("No display found. Running in CLI mode instead.")
            return
        self.root = tk.Tk()
        self.root.title("File Encryption/Decryption Utility")
        tk.Label(self.root, text="Input File:").grid(row=0, column=0, padx=10, pady=10)
        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_input_file).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self.root, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_output_file).grid(row=1, column=2, padx=10, pady=10)
        tk.Label(self.root, text="Password:").grid(row=2, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(self.root, show='*', width=50)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)
        self.mode_var = tk.StringVar(value='encrypt')
        tk.Radiobutton(self.root, text="Encrypt", variable=self.mode_var, value='encrypt').grid(row=3, column=0, padx=10, pady=10)
        tk.Radiobutton(self.root, text="Decrypt", variable=self.mode_var, value='decrypt').grid(row=3, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Execute", command=self.execute).grid(row=4, column=0, columnspan=3, pady=20)
        self.root.mainloop()
    def browse_input_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, filename)
    def browse_output_file(self):
        filename = filedialog.asksaveasfilename()
        if filename:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, filename)
    def execute(self):
        input_file = self.input_entry.get()
        output_file = self.output_entry.get()
        password = self.password_entry.get()
        mode = self.mode_var.get()
        try:
            if mode == 'encrypt':
                self.encryptor.encrypt_file(input_file, output_file, password)
            elif mode == 'decrypt':
                self.encryptor.decrypt_file(input_file, output_file, password)
            messagebox.showinfo("Success", f"File {mode}ed successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))