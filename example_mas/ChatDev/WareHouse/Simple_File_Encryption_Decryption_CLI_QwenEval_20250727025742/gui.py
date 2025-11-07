'''
Module containing the GUI implementation using tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from file_encryptor import encrypt_file, decrypt_file
class FileEncryptorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Encryptor/Decryptor")
        self.geometry("400x300")
        self.input_file_path = tk.StringVar()
        self.output_file_path = tk.StringVar()
        self.password = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self, text="Input File:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.input_file_path, width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self, text="Browse", command=self.select_input_file).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.output_file_path, width=40).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self, text="Browse", command=self.select_output_file).grid(row=1, column=2, padx=10, pady=10)
        tk.Label(self, text="Password:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.password, show="*", width=40).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self, text="Encrypt", command=self.encrypt_button_click).grid(row=3, column=0, padx=10, pady=10)
        tk.Button(self, text="Decrypt", command=self.decrypt_button_click).grid(row=3, column=1, padx=10, pady=10)
    def select_input_file(self):
        file_path = filedialog.askopenfilename()
        self.input_file_path.set(file_path)
    def select_output_file(self):
        file_path = filedialog.asksaveasfilename()
        self.output_file_path.set(file_path)
    def encrypt_button_click(self):
        input_file = self.input_file_path.get()
        output_file = self.output_file_path.get()
        password = self.password.get()
        if not input_file or not output_file or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        try:
            encrypt_file(input_file, output_file, password)
            messagebox.showinfo("Success", "File encrypted successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def decrypt_button_click(self):
        input_file = self.input_file_path.get()
        output_file = self.output_file_path.get()
        password = self.password.get()
        if not input_file or not output_file or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        try:
            decrypt_file(input_file, output_file, password)
            messagebox.showinfo("Success", "File decrypted successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))