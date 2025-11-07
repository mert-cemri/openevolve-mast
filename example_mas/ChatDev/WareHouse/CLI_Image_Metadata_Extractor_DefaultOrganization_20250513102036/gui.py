'''
GUI module for the image metadata extractor application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from metadata_extractor import extract_metadata
class ImageMetadataApp(tk.Tk):
    '''
    A class that defines the GUI application using Tkinter.
    '''
    def __init__(self):
        super().__init__()
        self.title("Image Metadata Extractor")
        self.geometry("400x300")
        self.label = tk.Label(self, text="Select an image file to extract metadata")
        self.label.pack(pady=20)
        self.browse_button = tk.Button(self, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=10)
        self.metadata_text = tk.Text(self, height=10, width=50)
        self.metadata_text.pack(pady=20)
    def browse_file(self):
        '''
        Opens a file dialog to select an image file.
        '''
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            metadata = extract_metadata(file_path)
            self.display_metadata(metadata)
    def display_metadata(self, metadata):
        '''
        Displays the extracted metadata in the GUI.
        :param metadata: Dictionary containing metadata.
        '''
        self.metadata_text.delete(1.0, tk.END)
        if 'Error' in metadata:
            messagebox.showerror("Error", metadata['Error'])
        else:
            for key, value in metadata.items():
                self.metadata_text.insert(tk.END, f"{key}: {value}\n")