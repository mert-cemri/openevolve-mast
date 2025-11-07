import tkinter as tk
from tkinter import filedialog
class FileDialog:
    def __init__(self, initialdir="/", title="Select MP3 File", filetypes=(("MP3 files", "*.mp3"),)):
        self.file_dialog = filedialog.askopenfilename(initialdir=initialdir, title=title, filetypes=filetypes)
    def get_file_path(self):
        return self.file_dialog