import tkinter as tk
from tkinter import messagebox
class MessageBox:
    def __init__(self, title, message):
        self.message_box = messagebox.showinfo(title, message)
    def show(self):
        self.message_box.show()