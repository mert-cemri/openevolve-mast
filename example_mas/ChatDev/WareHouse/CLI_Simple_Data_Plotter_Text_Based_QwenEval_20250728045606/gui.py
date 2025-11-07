'''
GUI class to handle the graphical user interface using tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from dataloader import DataLoader
from plotter import Plotter
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CLI Data Plotter GUI")
        self.data = []
        self.load_button = tk.Button(self.root, text="Load Data", command=self.load_data)
        self.load_button.pack(pady=10)
        self.plot_button = tk.Button(self.root, text="Plot Data", command=self.plot_data)
        self.plot_button.pack(pady=10)
        self.text_area = tk.Text(self.root, height=20, width=60)
        self.text_area.pack(pady=10)
    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                data_loader = DataLoader()
                self.data = data_loader.load_from_file(file_path)
                self.text_area.insert(tk.END, f"Data loaded from {file_path}\n")
            except ValueError:
                messagebox.showerror("Error", "File contains non-numeric data.")
                self.data = []
    def plot_data(self):
        if self.data:
            plotter = Plotter(self.data)
            bar_chart = "\nBar Chart:\n" + plotter.plot_bar_chart()
            line_graph = "\nLine Graph:\n" + plotter.plot_line_graph()
            self.text_area.insert(tk.END, bar_chart + "\n" + line_graph)
        else:
            self.text_area.insert(tk.END, "No data loaded.\n")
    def run(self):
        self.root.mainloop()