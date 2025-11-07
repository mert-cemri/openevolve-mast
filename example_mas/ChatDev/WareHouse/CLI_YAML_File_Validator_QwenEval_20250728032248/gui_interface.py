'''
Handles the graphical user interface for the YAML file validator.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from yaml_validator import YAMLValidator
class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("YAML File Validator")
        self.root.geometry("400x200")
        self.label = tk.Label(self.root, text="Select a YAML file to validate:")
        self.label.pack(pady=10)
        self.button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)
    def run(self):
        self.root.mainloop()
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml *.yml")])
        if file_path:
            self.validate_file(file_path)
    def validate_file(self, file_path):
        validator = YAMLValidator()
        result = validator.validate_file(file_path)
        if result['success']:
            self.result_label.config(text="Success: The YAML file is valid.")
        else:
            error_messages = "\n".join(result['errors'])
            self.result_label.config(text=f"Error: The YAML file is invalid.\n{error_messages}")
            messagebox.showerror("Validation Error", f"The YAML file is invalid.\n{error_messages}")