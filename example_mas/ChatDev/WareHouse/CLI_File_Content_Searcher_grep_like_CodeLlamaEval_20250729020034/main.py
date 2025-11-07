import tkinter as tk
from search import search
class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Search")
        self.window.geometry("300x100")
        self.directory_label = tk.Label(self.window, text="Directory:")
        self.directory_label.pack()
        self.directory_entry = tk.Entry(self.window)
        self.directory_entry.pack()
        self.pattern_label = tk.Label(self.window, text="Pattern:")
        self.pattern_label.pack()
        self.pattern_entry = tk.Entry(self.window)
        self.pattern_entry.pack()
        self.search_button = tk.Button(self.window, text="Search", command=self.search)
        self.search_button.pack()
        self.results_label = tk.Label(self.window, text="Results:")
        self.results_label.pack()
        self.results_text = tk.Text(self.window)
        self.results_text.pack()
        self.window.mainloop()
    def search(self):
        directory = self.directory_entry.get()
        pattern = self.pattern_entry.get()
        search(directory, pattern)
        self.results_text.insert(tk.END, f"{directory}: {pattern}\n")
if __name__ == "__main__":
    GUI()