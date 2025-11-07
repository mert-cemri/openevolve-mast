'''
Main application file for the elementary mathematics question solver.
This script creates a GUI for users to input data and calculates the number of subjects studied.
'''
import tkinter as tk
from tkinter import messagebox
import os
class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Elementary Mathematics Solver")
        # Labels and Entries for input
        self.label_total_time = tk.Label(root, text="Total time spent on homework (hours):")
        self.label_total_time.pack()
        self.entry_total_time = tk.Entry(root)
        self.entry_total_time.pack()
        self.label_subject_time = tk.Label(root, text="Time spent on one subject (hours):")
        self.label_subject_time.pack()
        self.entry_subject_time = tk.Entry(root)
        self.entry_subject_time.pack()
        # Button to calculate
        self.calculate_button = tk.Button(root, text="Calculate Subjects", command=self.calculate_subjects)
        self.calculate_button.pack()
        # Label to display result
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()
    def calculate_subjects(self):
        try:
            total_time = float(self.entry_total_time.get())
            subject_time = float(self.entry_subject_time.get())
            if subject_time <= 0:
                raise ValueError("Time spent on one subject must be greater than zero.")
            subjects = total_time / subject_time
            self.display_result(subjects)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
    def display_result(self, subjects):
        self.result_label.config(text=f"The number of subjects studied is: {int(subjects)}")
def run_app():
    # Check if the DISPLAY environment variable is set
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Ensure Xvfb is installed and running for virtual display.")
        return
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
if __name__ == "__main__":
    run_app()