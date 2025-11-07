'''
Provides a graphical user interface for the SnippetManager.
'''
import tkinter as tk
from tkinter import messagebox, simpledialog
from snippet_manager import SnippetManager
class SnippetManagerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Code Snippet Manager")
        self.geometry("600x400")
        self.snippet_manager = SnippetManager()
        self.create_widgets()
    def create_widgets(self):
        self.add_button = tk.Button(self, text="Add Snippet", command=self.add_snippet)
        self.add_button.pack(pady=10)
        self.search_entry = tk.Entry(self)
        self.search_entry.pack(pady=10)
        self.search_button = tk.Button(self, text="Search", command=self.search_snippets)
        self.search_button.pack(pady=10)
        self.snippet_listbox = tk.Listbox(self, width=80, height=15)
        self.snippet_listbox.pack(pady=10)
    def add_snippet(self):
        language = simpledialog.askstring("Input", "Enter the language:")
        description = simpledialog.askstring("Input", "Enter a description:")
        code = simpledialog.askstring("Input", "Enter the code snippet:")
        if language and description and code:
            self.snippet_manager.add_snippet(language, description, code)
            messagebox.showinfo("Success", "Snippet added successfully!")
    def search_snippets(self):
        query = self.search_entry.get()
        if query:
            snippets = self.snippet_manager.search_snippets(query)
            self.display_snippets(snippets)
    def display_snippets(self, snippets):
        self.snippet_listbox.delete(0, tk.END)
        for i, snippet in enumerate(snippets):
            display_text = f"{i}: {snippet['language']} - {snippet['description']}"
            self.snippet_listbox.insert(tk.END, display_text)