'''
DictionaryApp class to handle GUI and dictionary operations.
'''
import tkinter as tk
from tkinter import messagebox
class DictionaryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dictionary Lookup Tool")
        self.geometry("400x200")
        self.dictionary = self.load_dictionary("dictionary.txt")
        self.create_widgets()
    def load_dictionary(self, filepath):
        '''
        Load the dictionary from a file.
        :param filepath: Path to the dictionary file.
        :return: Dictionary with words as keys and definitions as values.
        '''
        dictionary = {}
        try:
            with open(filepath, 'r') as file:
                for line in file:
                    word, definition = line.strip().split(':', 1)
                    dictionary[word.strip()] = definition.strip()
        except FileNotFoundError:
            messagebox.showerror("Error", "Dictionary file not found.")
        return dictionary
    def lookup_word(self):
        '''
        Retrieve and display the definition of the input word.
        '''
        word = self.word_entry.get().strip()
        definition = self.dictionary.get(word, "Word not found in dictionary.")
        self.definition_label.config(text=definition)
    def create_widgets(self):
        '''
        Set up the GUI widgets.
        '''
        self.word_label = tk.Label(self, text="Enter word:")
        self.word_label.pack(pady=10)
        self.word_entry = tk.Entry(self)
        self.word_entry.pack(pady=5)
        self.lookup_button = tk.Button(self, text="Lookup", command=self.lookup_word)
        self.lookup_button.pack(pady=10)
        self.definition_label = tk.Label(self, text="", wraplength=350)
        self.definition_label.pack(pady=10)