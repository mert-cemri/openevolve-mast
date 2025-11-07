import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
class Tk:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("MP3 Tag Editor")
        self.root.geometry("500x300")
    def pack(self, fill="both", expand=True):
        self.root.pack(fill=fill, expand=expand)
    def mainloop(self):
        self.root.mainloop()
class Frame:
    def __init__(self, master):
        self.frame = ttk.Frame(master)
    def pack(self, fill="both", expand=True):
        self.frame.pack(fill=fill, expand=expand)
class Button:
    def __init__(self, master, text, command):
        self.button = ttk.Button(master, text=text, command=command)
    def pack(self, side="left"):
        self.button.pack(side=side)
class Label:
    def __init__(self, master, text):
        self.label = ttk.Label(master, text=text)
    def pack(self, side="left"):
        self.label.pack(side=side)
class Entry:
    def __init__(self, master):
        self.entry = ttk.Entry(master)
    def pack(self, side="left"):
        self.entry.pack(side=side)
class MessageBox:
    def __init__(self, master, title, message):
        self.message_box = messagebox.showinfo(title, message)
    def show(self):
        self.message_box.show()