'''
Handles the graphical user interface operations for the Word Count Tool.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from word_counter import WordCounter
class GUIApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Word Count Tool")
        self.word_counter = WordCounter()
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Select a text file to count words:")
        self.label.pack(pady=10)
        self.button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.button.pack(pady=5)
        self.root.mainloop()
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            word_count = self.word_counter.count_words(file_path)
            messagebox.showinfo("Word Count", f"Total word count: {word_count}")
    def run_gui(self):
        self.root.mainloop()