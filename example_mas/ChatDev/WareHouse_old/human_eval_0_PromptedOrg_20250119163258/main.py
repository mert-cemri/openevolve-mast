'''
This module contains the implementation of a GUI application to check if any two numbers in a list are closer than a given threshold.
'''
import tkinter as tk
from tkinter import messagebox
from typing import List
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
class CloseElementsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Close Elements Checker")
        self.label_numbers = tk.Label(root, text="Enter numbers (comma-separated):")
        self.label_numbers.pack()
        self.entry_numbers = tk.Entry(root, width=50)
        self.entry_numbers.pack()
        self.label_threshold = tk.Label(root, text="Enter threshold:")
        self.label_threshold.pack()
        self.entry_threshold = tk.Entry(root, width=50)
        self.entry_threshold.pack()
        self.check_button = tk.Button(root, text="Check", command=self.check_close_elements)
        self.check_button.pack()
    def check_close_elements(self):
        try:
            numbers = list(map(float, self.entry_numbers.get().split(',')))
            threshold = float(self.entry_threshold.get())
            result = has_close_elements(numbers, threshold)
            message = "Yes, there are close elements." if result else "No, there are no close elements."
            messagebox.showinfo("Result", message)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers and threshold.")
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = CloseElementsApp(root)
        root.mainloop()
    except tk.TclError:
        print("GUI cannot be displayed. Please ensure you have a graphical environment or use a virtual display.")