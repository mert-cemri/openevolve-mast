'''
GUI module for the CLI program that counts lines of code in a directory.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from cli import count_lines_of_code
def on_button_click():
    '''
    Handles the button click event in the GUI to select a directory and count lines of code.
    '''
    directory = filedialog.askdirectory()
    if directory:
        try:
            result = count_lines_of_code(directory)
            result_str = "\n".join([f"{ext}: {count} lines" for ext, count in result.items()])
            messagebox.showinfo("Result", result_str)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showinfo("Info", "No directory selected.")
def create_gui():
    '''
    Creates and runs the GUI for the program.
    '''
    root = tk.Tk()
    root.title("Lines of Code Counter")
    root.geometry("300x100")
    button = tk.Button(root, text="Select Directory", command=on_button_click)
    button.pack(pady=20)
    root.mainloop()