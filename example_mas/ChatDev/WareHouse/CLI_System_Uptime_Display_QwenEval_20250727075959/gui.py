'''
Module for handling the graphical user interface using tkinter.
'''
import tkinter as tk
def create_gui(uptime_text):
    root = tk.Tk()
    root.title("System Uptime")
    uptime_label = tk.Label(root, text=f"System Uptime: {uptime_text}", font=("Helvetica", 16))
    uptime_label.pack(pady=20)
    root.mainloop()