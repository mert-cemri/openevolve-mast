'''
GUI class to create a simple interface using tkinter.
'''
import tkinter as tk
from file_watcher import FileWatcher
class GUI:
    def __init__(self):
        '''
        Initializes the GUI components.
        '''
        self.root = tk.Tk()
        self.root.title("File Watcher")
        self.path_entry = tk.Entry(self.root, width=50)
        self.path_entry.pack(pady=10)
        self.start_button = tk.Button(self.root, text="Start Watching", command=self.start_watching)
        self.start_button.pack(pady=5)
        self.stop_button = tk.Button(self.root, text="Stop Watching", command=self.stop_watching)
        self.stop_button.pack(pady=5)
        self.file_watcher = None
    def start_watching(self):
        '''
        Starts the file watcher when the user clicks a button.
        '''
        path = self.path_entry.get()
        if path:
            self.file_watcher = FileWatcher(path)
            self.file_watcher.start()
    def stop_watching(self):
        '''
        Stops the file watcher when the user clicks a button.
        '''
        if self.file_watcher:
            self.file_watcher.stop()
    def run(self):
        '''
        Runs the tkinter main loop.
        '''
        self.root.mainloop()