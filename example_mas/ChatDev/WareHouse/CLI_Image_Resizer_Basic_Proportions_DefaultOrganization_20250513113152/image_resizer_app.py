'''
Defines the ImageResizerApp class which handles the GUI and user interactions for resizing images.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from image_utils import resize_image
class ImageResizerApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Image Resizer")
        self.image_label = tk.Label(self.root, text="No image selected")
        self.image_label.pack()
        self.open_button = tk.Button(self.root, text="Open Image", command=self.open_image)
        self.open_button.pack()
        self.width_entry = tk.Entry(self.root)
        self.width_entry.pack()
        self.width_entry.insert(0, "Enter target width")
        self.height_entry = tk.Entry(self.root)
        self.height_entry.pack()
        self.height_entry.insert(0, "Enter target height")
        self.resize_button = tk.Button(self.root, text="Resize Image", command=self.resize_image)
        self.resize_button.pack()
        self.save_button = tk.Button(self.root, text="Save Image", command=self.save_image)
        self.save_button.pack()
        self.original_image = None
        self.resized_image = None
    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.original_image = Image.open(file_path)
            self.image_label.config(text=f"Image loaded: {file_path}")
    def resize_image(self):
        if not self.original_image:
            messagebox.showerror("Error", "No image loaded")
            return
        target_width = self.width_entry.get()
        target_height = self.height_entry.get()
        try:
            target_width = int(target_width) if target_width else None
            target_height = int(target_height) if target_height else None
        except ValueError:
            messagebox.showerror("Error", "Invalid width or height")
            return
        self.resized_image = resize_image(self.original_image, target_width, target_height)
        messagebox.showinfo("Success", "Image resized successfully")
    def save_image(self):
        if not self.resized_image:
            messagebox.showerror("Error", "No resized image to save")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        if file_path:
            self.resized_image.save(file_path)
            messagebox.showinfo("Success", f"Image saved to {file_path}")
    def run(self):
        self.root.mainloop()