'''
This module contains the MorseCodeApp class which provides a GUI for translating
between English text and Morse code using tkinter.
'''
import tkinter as tk
from morse_code_translator import MorseCodeTranslator
class MorseCodeApp:
    def __init__(self, root):
        '''Initializes the GUI components.'''
        self.root = root
        self.root.title("Morse Code Translator")
        # Input text area
        self.input_text = tk.Text(root, height=5, width=50)
        self.input_text.pack()
        # Translate to Morse button
        self.to_morse_button = tk.Button(root, text="Translate to Morse", command=self.translate_to_morse)
        self.to_morse_button.pack()
        # Translate to Text button
        self.to_text_button = tk.Button(root, text="Translate to Text", command=self.translate_to_text)
        self.to_text_button.pack()
        # Output text area
        self.output_text = tk.Text(root, height=5, width=50)
        self.output_text.pack()
    def translate_to_morse(self):
        '''Handles the translation of text to Morse code.'''
        text = self.input_text.get("1.0", tk.END).strip()
        morse_code = MorseCodeTranslator.text_to_morse(text)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, morse_code)
    def translate_to_text(self):
        '''Handles the translation of Morse code to text.'''
        morse = self.input_text.get("1.0", tk.END).strip()
        text = MorseCodeTranslator.morse_to_text(morse)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)