'''
Main application file for the one-way directory synchronizer with GUI.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from synchronizer import DirectorySynchronizer
class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Synchronizer")
        self.source_dir = tk.StringVar()
        self.target_dir = tk.StringVar()
        tk.Label(root, text="Source Directory:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.source_dir, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(root, text="Browse", command=self.select_source).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(root, text="Target Directory:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.target_dir, width=50).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(root, text="Browse", command=self.select_target).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(root, text="Synchronize", command=self.start_synchronization).grid(row=2, column=1, pady=20)
    def select_source(self):
        directory = filedialog.askdirectory()
        if directory:
            self.source_dir.set(directory)
    def select_target(self):
        directory = filedialog.askdirectory()
        if directory:
            self.target_dir.set(directory)
    def start_synchronization(self):
        source = self.source_dir.get()
        target = self.target_dir.get()
        if not source or not target:
            messagebox.showerror("Error", "Both source and target directories must be selected.")
            return
        synchronizer = DirectorySynchronizer()
        try:
            synchronizer.synchronize(source, target)
            messagebox.showinfo("Success", "Synchronization complete.")
        except RuntimeError as e:
            messagebox.showerror("Synchronization Error", str(e))
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = AppGUI(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Unable to start the GUI. Ensure you are running in a graphical environment.")