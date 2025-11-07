'''
This module contains the GUIInterface class which handles the graphical user interface logic.
'''
import tkinter as tk
from base64_tool import Base64Tool
class GUIInterface:
    def __init__(self):
        self.tool = Base64Tool()
        self.root = tk.Tk()
        self.root.title("Base64 Encoder/Decoder")
        self.label = tk.Label(self.root, text="Enter string:")
        self.label.pack()
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack()
        self.encode_button = tk.Button(self.root, text="Encode", command=self.encode)
        self.encode_button.pack()
        self.decode_button = tk.Button(self.root, text="Decode", command=self.decode)
        self.decode_button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
    def run(self):
        '''Runs the GUI interface.'''
        self.root.mainloop()
    def encode(self):
        '''Handles the encoding action in the GUI.'''
        input_string = self.entry.get()
        result = self.tool.encode(input_string)
        self.result_label.config(text=f"Encoded: {result}")
    def decode(self):
        '''Handles the decoding action in the GUI.'''
        input_string = self.entry.get()
        result = self.tool.decode(input_string)
        self.result_label.config(text=f"Decoded: {result}")