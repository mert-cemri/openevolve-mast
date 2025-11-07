'''
GUI implementation using tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from html_processor import strip_html_tags
class HTMLStripperGUI(tk.Tk):
    '''
    Graphical User Interface for the HTML stripping tool.
    '''
    def __init__(self):
        super().__init__()
        self.title('HTML Stripper')
        self.geometry('500x500')
        self.label = tk.Label(self, text='Enter HTML or select a file:')
        self.label.pack(pady=10)
        self.text_area = tk.Text(self, height=10, width=60)
        self.text_area.pack(pady=10)
        self.file_button = tk.Button(self, text='Select File', command=self.on_file_select)
        self.file_button.pack(pady=5)
        self.submit_button = tk.Button(self, text='Strip HTML', command=self.on_submit)
        self.submit_button.pack(pady=10)
        self.result_label = tk.Label(self, text='Plain Text Result:')
        self.result_label.pack(pady=10)
        self.result_text_area = tk.Text(self, height=10, width=60)
        self.result_text_area.pack(pady=10)
    def strip_html(self, html_content):
        '''
        Strips HTML tags from the given HTML content.
        '''
        return strip_html_tags(html_content)
    def on_submit(self):
        '''
        Handles the submit button click event.
        '''
        html_content = self.text_area.get('1.0', tk.END).strip()
        if not html_content:
            messagebox.showwarning('Input Error', 'Please enter HTML content or select a file.')
            return
        plain_text = self.strip_html(html_content)
        self.result_text_area.delete('1.0', tk.END)
        self.result_text_area.insert(tk.END, plain_text)
    def on_file_select(self):
        '''
        Handles the file selection button click event.
        '''
        file_path = filedialog.askopenfilename(filetypes=[('HTML files', '*.html')])
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    html_content = file.read()
                self.text_area.delete('1.0', tk.END)
                self.text_area.insert(tk.END, html_content)
            except FileNotFoundError:
                messagebox.showerror('File Error', f"The file {file_path} does not exist.")
            except Exception as e:
                messagebox.showerror('File Error', f"Error reading the file: {e}")