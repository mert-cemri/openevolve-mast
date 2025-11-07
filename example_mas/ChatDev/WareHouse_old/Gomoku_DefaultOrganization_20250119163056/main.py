import tkinter as tk
from tkinter import messagebox
from typing import List
from utils import has_close_elements
def check_close_elements():
    try:
        numbers = [float(num) for num in numbers_entry.get().split()]
        threshold = float(threshold_entry.get())
        result = has_close_elements(numbers, threshold)
        messagebox.showinfo("Result", f"There are close elements: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers and threshold.")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        root.title("Close Elements Checker")
        numbers_label = tk.Label(root, text="Numbers:")
        numbers_label.pack()
        numbers_entry = tk.Entry(root)
        numbers_entry.pack()
        threshold_label = tk.Label(root, text="Threshold:")
        threshold_label.pack()
        threshold_entry = tk.Entry(root)
        threshold_entry.pack()
        check_button = tk.Button(root, text="Check", command=check_close_elements)
        check_button.pack()
        root.mainloop()
    except tk.TclError as e:
        messagebox.showerror("Error", str(e))