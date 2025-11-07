'''
Contains the GUI implementation for the directory synchronizer application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from synchronizer import DirectorySynchronizer
class DirectorySynchronizerGUI:
    def __init__(self):
        '''
        Initializes the GUI for the directory synchronizer.
        '''
        try:
            self.root = tk.Tk()
            self.root.title("Directory Synchronizer")
            self.source_dir = ""
            self.target_dir = ""
            self.create_widgets()
        except tk.TclError as e:
            print("Tkinter error: ", e)
            print("Ensure you have a display environment or use X11 forwarding.")
    def create_widgets(self):
        '''
        Creates the GUI components.
        '''
        self.source_button = tk.Button(self.root, text="Select Source Directory", command=self.select_source)
        self.source_button.pack(pady=10)
        self.target_button = tk.Button(self.root, text="Select Target Directory", command=self.select_target)
        self.target_button.pack(pady=10)
        self.sync_button = tk.Button(self.root, text="Synchronize", command=self.run_synchronization)
        self.sync_button.pack(pady=20)
    def select_source(self):
        '''
        Opens a dialog to select the source directory.
        '''
        self.source_dir = filedialog.askdirectory(title="Select Source Directory")
        if self.source_dir:
            messagebox.showinfo("Source Directory", f"Selected Source: {self.source_dir}")
    def select_target(self):
        '''
        Opens a dialog to select the target directory.
        '''
        self.target_dir = filedialog.askdirectory(title="Select Target Directory")
        if self.target_dir:
            messagebox.showinfo("Target Directory", f"Selected Target: {self.target_dir}")
    def run_synchronization(self):
        '''
        Runs the synchronization process.
        '''
        if not self.source_dir or not self.target_dir:
            messagebox.showwarning("Warning", "Please select both source and target directories.")
            return
        synchronizer = DirectorySynchronizer()
        synchronizer.synchronize(self.source_dir, self.target_dir)
        messagebox.showinfo("Success", "Synchronization complete!")
    def run(self):
        '''
        Runs the main loop of the GUI.
        '''
        self.root.mainloop()