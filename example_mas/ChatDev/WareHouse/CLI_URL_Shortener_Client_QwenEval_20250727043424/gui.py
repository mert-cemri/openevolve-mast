'''
Module containing the GUI logic using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from url_shortener import shorten_url
class URLShortenerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")
        self.root.geometry("400x200")
        self.label = tk.Label(root, text="Enter the long URL:")
        self.label.pack(pady=10)
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack(pady=5)
        self.shorten_button = tk.Button(root, text="Shorten URL", command=self.shorten_url)
        self.shorten_button.pack(pady=20)
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)
    def shorten_url(self):
        long_url = self.url_entry.get()
        if not long_url:
            messagebox.showerror("Error", "Please enter a URL.")
            return
        shortened_url = shorten_url(long_url)
        if "Error" in shortened_url:
            messagebox.showerror("Error", shortened_url)
        else:
            self.result_label.config(text=f"Shortened URL: {shortened_url}")
def run_gui():
    root = tk.Tk()
    app = URLShortenerGUI(root)
    root.mainloop()