'''
Handles graphical user interactions.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from archiver import Archiver
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('File Archiver')
        self.archiver = Archiver()
        self.zip_path = tk.StringVar()
        self.extract_to = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text='ZIP Path:').grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.zip_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text='Browse', command=self.browse_zip).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self.root, text='Extract To:').grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.extract_to, width=50).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text='Browse', command=self.browse_extract).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(self.root, text='Add Files/Directories', command=self.add_files).grid(row=2, column=0, columnspan=3, pady=10)
        tk.Button(self.root, text='Extract', command=self.extract_files).grid(row=3, column=0, columnspan=3, pady=10)
    def browse_zip(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")])
        if file_path:
            self.zip_path.set(file_path)
    def browse_extract(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            self.extract_to.set(dir_path)
    def add_files(self):
        files = filedialog.askopenfilenames()
        if files and self.zip_path.get():
            try:
                self.archiver.add_to_zip(self.zip_path.get(), files)
                messagebox.showinfo('Success', 'Files added to ZIP archive successfully!')
            except Exception as e:
                messagebox.showerror('Error', str(e))
    def extract_files(self):
        if self.zip_path.get() and self.extract_to.get():
            try:
                self.archiver.extract_zip(self.zip_path.get(), self.extract_to.get())
                messagebox.showinfo('Success', 'Files extracted successfully!')
            except Exception as e:
                messagebox.showerror('Error', str(e))
    def run(self):
        self.root.mainloop()