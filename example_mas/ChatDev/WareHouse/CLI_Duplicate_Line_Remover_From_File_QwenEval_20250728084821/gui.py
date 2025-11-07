'''
Handles the graphical user interface logic for removing duplicate lines.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from core import remove_duplicates
def remove_duplicates_gui():
    '''
    Starts the GUI for removing duplicate lines.
    Provides a user-friendly interface to select input and output files and submit the request.
    '''
    root = tk.Tk()
    root.title('Remove Duplicate Lines')
    input_label = tk.Label(root, text='Input File:')
    input_label.grid(row=0, column=0, padx=10, pady=10)
    input_entry = tk.Entry(root, width=50)
    input_entry.grid(row=0, column=1, padx=10, pady=10)
    input_button = tk.Button(root, text='Browse', command=lambda: browse_file(input_entry))
    input_button.grid(row=0, column=2, padx=10, pady=10)
    output_label = tk.Label(root, text='Output File:')
    output_label.grid(row=1, column=0, padx=10, pady=10)
    output_entry = tk.Entry(root, width=50)
    output_entry.grid(row=1, column=1, padx=10, pady=10)
    output_button = tk.Button(root, text='Browse', command=lambda: browse_file(output_entry))
    output_button.grid(row=1, column=2, padx=10, pady=10)
    submit_button = tk.Button(root, text='Submit', command=lambda: on_submit(input_entry.get(), output_entry.get()))
    submit_button.grid(row=2, column=1, pady=20)
    root.mainloop()
def browse_file(entry):
    '''
    Opens a file dialog to select a file and updates the entry widget.
    '''
    file_path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, file_path)
def on_submit(input_file, output_file):
    '''
    Callback function for the submit button in the GUI.
    Handles exceptions and provides feedback to the user.
    '''
    try:
        remove_duplicates(input_file, output_file)
        messagebox.showinfo('Success', 'Duplicates removed successfully!')
    except Exception as e:
        messagebox.showerror('Error', str(e))