'''
Handles the graphical user interface for the XML file pretty printer.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from xml_processor import XMLProcessor
class GUIInterface:
    def __init__(self, xml_processor):
        self.xml_processor = xml_processor
        self.root = tk.Tk()
        self.root.title("XML File Pretty Printer")
        self.root.geometry("600x400")
        self.input_file_path = tk.StringVar()
        self.output_file_path = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Input XML File:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.input_file_path, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_input_file).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self.root, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.output_file_path, width=50).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_output_file).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Pretty Print", command=self.pretty_print).grid(row=2, column=1, pady=20)
    def browse_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
        if file_path:
            self.input_file_path.set(file_path)
    def browse_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
        if file_path:
            self.output_file_path.set(file_path)
    def pretty_print(self):
        input_file = self.input_file_path.get()
        output_file = self.output_file_path.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        try:
            xml_content = self.xml_processor.read_file(input_file)
            pretty_xml = self.xml_processor.pretty_print(xml_content)
            if output_file:
                self.xml_processor.write_file(output_file, pretty_xml)
                messagebox.showinfo("Success", f"Pretty-printed XML saved to {output_file}")
            else:
                messagebox.showinfo("Output", pretty_xml)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.root.mainloop()