'''
Handles displaying the system uptime in a graphical user interface.
Uses tkinter for the GUI.
'''
import tkinter as tk
from tkinter import ttk
from uptime_fetcher import UptimeFetcher
class GUIInterface:
    def __init__(self, uptime_fetcher):
        self.uptime_fetcher = uptime_fetcher
        self.root = tk.Tk()
        self.root.title("System Uptime")
        self.root.geometry("300x100")
        self.label = ttk.Label(self.root, text="Fetching Uptime...", font=("Helvetica", 14))
        self.label.pack(pady=20)
        self.update_uptime()
    def update_uptime(self):
        uptime = self.uptime_fetcher.get_uptime()
        self.label.config(text=f"System Uptime: {uptime}")
        self.root.after(1000, self.update_uptime)
    def display_uptime(self):
        self.root.mainloop()