'''
Module for the graphical user interface of the QR Code Generator.
Handles user input, generates QR codes, and displays them.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from qr_generator import generate_qr_code, save_qr_code, qr_to_ascii
class QRCodeApp:
    def __init__(self, args):
        self.args = args
        self.root = tk.Tk()
        self.root.title('QR Code Generator')
        self.root.geometry('400x300')
        self.label = tk.Label(self.root, text='Enter text or URL:')
        self.label.pack(pady=10)
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=5)
        self.generate_button = tk.Button(self.root, text='Generate QR Code', command=self.generate_qr_code)
        self.generate_button.pack(pady=10)
        self.save_button = tk.Button(self.root, text='Save QR Code', command=self.save_qr_code)
        self.save_button.pack(pady=5)
        self.ascii_label = tk.Label(self.root, text='')
        self.ascii_label.pack(pady=10)
        self.qr_code = None
    def generate_qr_code(self):
        data = self.entry.get()
        if not data:
            messagebox.showwarning('Input Error', 'Please enter text or URL.')
            return
        self.qr_code = generate_qr_code(data)
        ascii_art = qr_to_ascii(self.qr_code)
        self.ascii_label.config(text=ascii_art)
    def save_qr_code(self):
        if not self.qr_code:
            messagebox.showwarning('Save Error', 'No QR code generated yet.')
            return
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if filename:
            save_qr_code(self.qr_code, filename)
            messagebox.showinfo('Save Success', f'QR code saved to {filename}')
    def run(self):
        self.root.mainloop()