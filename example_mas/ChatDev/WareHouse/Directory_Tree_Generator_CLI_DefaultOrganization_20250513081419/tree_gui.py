'''
Contains the TreeGUI class which handles the graphical user interface using Tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from tree_generator import TreeGenerator
class TreeGUI:
    def start(self):
        '''
        Initializes and runs the GUI application.
        '''
        try:
            self.root = tk.Tk()
            self.root.title("Directory Tree Generator")
            self.label = tk.Label(self.root, text="Select Directory:")
            self.label.pack()
            self.select_button = tk.Button(self.root, text="Browse", command=self.browse_directory)
            self.select_button.pack()
            self.depth_label = tk.Label(self.root, text="Max Depth:")
            self.depth_label.pack()
            self.depth_entry = tk.Entry(self.root)
            self.depth_entry.pack()
            self.depth_entry.insert(0, "3")
            self.generate_button = tk.Button(self.root, text="Generate Tree", command=self.generate_tree)
            self.generate_button.pack()
            self.output_text = tk.Text(self.root, wrap=tk.WORD)
            self.output_text.pack(expand=True, fill=tk.BOTH)
            self.root.mainloop()
        except tk.TclError as e:
            print("Error initializing Tkinter GUI:", e)
            print("Ensure you are running in an environment with a graphical display or use CLI mode.")
    def browse_directory(self):
        '''
        Opens a file dialog to select a directory.
        '''
        self.directory = filedialog.askdirectory()
        self.label.config(text=f"Selected Directory: {self.directory}")
    def generate_tree(self):
        '''
        Generates the directory tree and displays it in the text widget.
        '''
        try:
            max_depth = int(self.depth_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Max Depth must be an integer.")
            return
        generator = TreeGenerator()
        tree = generator.generate_tree(self.directory, max_depth)
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, tree)