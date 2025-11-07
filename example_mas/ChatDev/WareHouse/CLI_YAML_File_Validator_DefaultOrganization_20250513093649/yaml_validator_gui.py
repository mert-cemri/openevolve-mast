'''
YAML Validator GUI class to provide a graphical interface for the validator.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from yaml_validator import YAMLValidator
class YAMLValidatorGUI:
    '''
    Provides a graphical user interface for the YAML validator.
    '''
    def __init__(self):
        '''
        Initializes the GUI components.
        '''
        self.root = tk.Tk()
        self.root.title("YAML Validator")
        self.file_path = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Creates and places the GUI widgets.
        '''
        tk.Label(self.root, text="YAML File Path:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_file).grid(row=0, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Validate", command=self.validate_file).grid(row=1, column=1, pady=10)
    def browse_file(self):
        '''
        Opens a file dialog to select a YAML file.
        '''
        file_path = filedialog.askopenfilename(filetypes=[("YAML files", "*.yaml *.yml")])
        self.file_path.set(file_path)
    def validate_file(self):
        '''
        Calls the YAMLValidator to validate the selected file and displays the result.
        '''
        file_path = self.file_path.get()
        if file_path:
            result = YAMLValidator.validate_yaml(file_path)
            messagebox.showinfo("Validation Result", result)
        else:
            messagebox.showwarning("No File Selected", "Please select a YAML file to validate.")
    def run(self):
        '''
        Runs the main loop of the GUI application.
        '''
        self.root.mainloop()