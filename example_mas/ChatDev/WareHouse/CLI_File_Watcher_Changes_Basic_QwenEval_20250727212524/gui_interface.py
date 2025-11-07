'''
GUIInterface class to handle graphical user interactions.
Accepts user input and starts the file watcher.
Uses tkinter for the GUI.
'''
import tkinter as tk
from filewatcher import FileWatcher
class GUIInterface:
    def __init__(self, path):
        self.root = tk.Tk()
        self.root.title("File Watcher")
        self.path_entry = tk.Entry(self.root, width=50)
        self.path_entry.insert(0, path)  # Pre-fill the path
        self.path_entry.pack(pady=10)
        self.start_button = tk.Button(self.root, text="Start Watching", command=self.start_watching)
        self.start_button.pack(pady=10)
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack(pady=10)
        self.watcher = None
    def run(self):
        self.root.mainloop()
    def start_watching(self):
        path = self.path_entry.get()
        if not path:
            self.update_display("Please enter a path")
            return
        try:
            self.watcher = FileWatcher(path, self.update_display)
            self.watcher.start()
        except Exception as e:
            self.update_display(f"Error starting file watcher: {str(e)}")
    def update_display(self, message):
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)