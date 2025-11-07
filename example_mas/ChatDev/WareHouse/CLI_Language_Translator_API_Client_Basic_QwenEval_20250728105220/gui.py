'''
Handles the GUI logic using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from translator import Translator
class TranslatorApp:
    def __init__(self):
        self.translator = Translator()
        self.root = tk.Tk()
        self.root.title("Language Translator")
        self.text_label = tk.Label(self.root, text="Enter text to translate:")
        self.text_label.pack(pady=5)
        self.text_entry = tk.Entry(self.root, width=50)
        self.text_entry.pack(pady=5)
        self.language_label = tk.Label(self.root, text="Enter target language (e.g., en, fr):")
        self.language_label.pack(pady=5)
        self.language_entry = tk.Entry(self.root, width=50)
        self.language_entry.pack(pady=5)
        self.translate_button = tk.Button(self.root, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="Translation:")
        self.result_label.pack(pady=5)
        self.result_text = tk.Entry(self.root, width=50)
        self.result_text.pack(pady=5)
    def translate_text(self):
        text = self.text_entry.get().strip()
        target_language = self.language_entry.get().strip()
        if not text or not target_language:
            messagebox.showerror("Input Error", "Text and target language must be provided.")
            return
        translation = self.translator.translate(text, target_language)
        self.result_text.delete(0, tk.END)
        self.result_text.insert(0, translation)
    def run(self):
        self.root.mainloop()