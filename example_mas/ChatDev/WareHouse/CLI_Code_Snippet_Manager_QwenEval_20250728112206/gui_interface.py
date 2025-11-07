'''
Handles the graphical user interface interactions.
'''
import tkinter as tk
from tkinter import messagebox, simpledialog
from snippet_manager import SnippetManager, Snippet
class GUIInterface:
    def __init__(self):
        self.manager = SnippetManager()
        self.root = tk.Tk()
        self.root.title("GUI Code Snippet Manager")
        self.root.geometry("600x400")
        self.create_widgets()
    def run(self):
        self.root.mainloop()
    def create_widgets(self):
        self.add_button = tk.Button(self.root, text="Add Snippet", command=self.add_snippet)
        self.add_button.pack(pady=10)
        self.get_button = tk.Button(self.root, text="Get Snippets by Language", command=self.get_snippets_by_language)
        self.get_button.pack(pady=10)
        self.search_button = tk.Button(self.root, text="Search Snippets", command=self.search_snippets)
        self.search_button.pack(pady=10)
        self.list_button = tk.Button(self.root, text="List All Snippets", command=self.list_all_snippets)
        self.list_button.pack(pady=10)
        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=10)
    def add_snippet(self):
        language = simpledialog.askstring("Input", "Enter the language:", parent=self.root)
        code = simpledialog.askstring("Input", "Enter the code:", parent=self.root)
        description = simpledialog.askstring("Input", "Enter the description (optional):", parent=self.root)
        if language is None or code is None:
            messagebox.showerror("Error", "Language and code are required.")
            return
        if not language.strip() or not code.strip():
            messagebox.showerror("Error", "Language and code are required.")
            return
        snippet = Snippet(language, code, description)
        self.manager.add_snippet(snippet)
        messagebox.showinfo("Success", "Snippet added successfully.")
    def get_snippets_by_language(self):
        language = simpledialog.askstring("Input", "Enter the language:", parent=self.root)
        if language is None:
            messagebox.showerror("Error", "Language is required.")
            return
        if not language.strip():
            messagebox.showerror("Error", "Language is required.")
            return
        snippets = self.manager.get_snippets_by_language(language)
        if snippets:
            message = "\n".join([f"Snippet {i+1}:\nLanguage: {s['language']}\nCode: {s['code']}\nDescription: {s['description']}" for i, s in enumerate(snippets)])
            messagebox.showinfo("Snippets", message)
        else:
            messagebox.showinfo("Snippets", "No snippets found for this language.")
    def search_snippets(self):
        query = simpledialog.askstring("Input", "Enter the search query:", parent=self.root)
        if query is None:
            messagebox.showerror("Error", "Query is required.")
            return
        if not query.strip():
            messagebox.showerror("Error", "Query is required.")
            return
        snippets = self.manager.search_snippets(query)
        if snippets:
            message = "\n".join([f"Snippet {i+1}:\nLanguage: {s['language']}\nCode: {s['code']}\nDescription: {s['description']}" for i, s in enumerate(snippets)])
            messagebox.showinfo("Snippets", message)
        else:
            messagebox.showinfo("Snippets", "No snippets found matching the query.")
    def list_all_snippets(self):
        snippets = self.manager.get_all_snippets()
        if snippets:
            message = "\n".join([f"Snippet {i+1}:\nLanguage: {s['language']}\nCode: {s['code']}\nDescription: {s['description']}" for i, s in enumerate(snippets)])
            messagebox.showinfo("Snippets", message)
        else:
            messagebox.showinfo("Snippets", "No snippets found.")