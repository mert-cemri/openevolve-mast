'''
Defines the FileWatcherGUI class to create a GUI using tkinter for the file watcher.
'''
import tkinter as tk
from tkinter import filedialog
from file_watcher import FileWatcher
import threading
class FileWatcherGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Watcher")
        self.path = tk.StringVar()
        self.watcher_thread = None
        self.watcher = None
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Directory to Watch:").pack(pady=5)
        tk.Entry(self.root, textvariable=self.path, width=50).pack(pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_directory).pack(pady=5)
        tk.Button(self.root, text="Start Watching", command=self.start_watching).pack(pady=5)
        tk.Button(self.root, text="Stop Watching", command=self.stop_watching).pack(pady=5)
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.path.set(directory)
    def start_watching(self):
        if self.path.get():
            self.watcher = FileWatcher(self.path.get())
            self.watcher_thread = threading.Thread(target=self.watcher.start)
            self.watcher_thread.start()
    def stop_watching(self):
        if self.watcher and self.watcher_thread and self.watcher_thread.is_alive():
            self.watcher.stop()
            self.watcher_thread.join()
            print("Watcher stopped.")
    def run(self):
        self.root.mainloop()