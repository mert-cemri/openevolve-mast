'''
Handles the Graphical User Interface (GUI) for the Image Metadata Extractor tool.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from image_metadata_extractor import ImageMetadataExtractor
class ImageMetadataGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Metadata Extractor")
        self.extractor = ImageMetadataExtractor()
        self.label = tk.Label(root, text="Select an image file:")
        self.label.pack(pady=10)
        self.button = tk.Button(root, text="Browse", command=self.browse_file)
        self.button.pack(pady=5)
        self.metadata_label = tk.Label(root, text="", justify=tk.LEFT)
        self.metadata_label.pack(pady=20)
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            metadata = self.extractor.extract_metadata(file_path)
            self.display_metadata(metadata)
    def display_metadata(self, metadata):
        metadata_text = (
            f"Format: {metadata['format']}\n"
            f"Resolution: {metadata['resolution']}\n"
            f"Creation Date: {metadata['creation_date']}"
        )
        self.metadata_label.config(text=metadata_text)