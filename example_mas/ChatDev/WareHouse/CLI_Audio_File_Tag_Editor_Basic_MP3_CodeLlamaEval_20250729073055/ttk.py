import tkinter as tk
from tkinter import ttk
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