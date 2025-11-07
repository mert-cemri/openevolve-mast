'''
Handles the graphical user interface interactions using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from maze_generator import MazeGenerator
class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Maze Generator")
        self.width_label = tk.Label(self.root, text="Width (odd number):")
        self.width_label.pack()
        self.width_entry = tk.Entry(self.root)
        self.width_entry.pack()
        self.height_label = tk.Label(self.root, text="Height (odd number):")
        self.height_label.pack()
        self.height_entry = tk.Entry(self.root)
        self.height_entry.pack()
        self.generate_button = tk.Button(self.root, text="Generate Maze", command=self.generate_maze)
        self.generate_button.pack()
        self.text_area = tk.Text(self.root, height=20, width=40)
        self.text_area.pack()
    def run(self):
        self.root.mainloop()
    def generate_maze(self):
        try:
            width = int(self.width_entry.get())
            height = int(self.height_entry.get())
            if width % 2 == 0 or height % 2 == 0:
                raise ValueError("Width and height must be odd numbers.")
            generator = MazeGenerator()
            maze = generator.generate(width, height)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, str(maze))
        except ValueError as e:
            messagebox.showerror("Invalid Input", f"Invalid input: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")