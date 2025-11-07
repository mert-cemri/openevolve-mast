'''
This file contains the main application code for a simple math quiz using tkinter.
It displays a question about elementary mathematics and calculates the answer when prompted.
'''
import tkinter as tk
from tkinter import messagebox
import os
class MathQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Math Quiz")
        # Question and options
        self.question = "Keri spent 3 hours on her homework. She spent equal amounts of time on all subjects. If Keri spent 1 over 2 hour on science, how many subjects did she study?"
        self.options = [
            "4 subjects",
            "2 subjects",
            "6 subjects",
            "5 subjects"
        ]
        # Setup GUI
        self.setup_gui()
    def setup_gui(self):
        # Display question
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Display options
        self.option_vars = []
        for idx, option in enumerate(self.options):
            var = tk.StringVar(value=option)
            option_label = tk.Label(self.root, text=f"{idx}. {option}")
            option_label.pack(anchor="w")
            self.option_vars.append(var)
        # Calculate button
        calculate_button = tk.Button(self.root, text="Calculate Answer", command=self.calculate_answer)
        calculate_button.pack(pady=20)
    def calculate_answer(self):
        # Logic to calculate the answer
        total_hours = 3
        time_per_subject = 0.5
        number_of_subjects = total_hours / time_per_subject
        # Determine the correct option index
        if number_of_subjects == 6:
            answer_index = 2
        else:
            answer_index = -1  # Invalid case
        # Display the answer
        if answer_index != -1:
            messagebox.showinfo("Answer", f"The answer is ({answer_index})")
        else:
            messagebox.showerror("Error", "Could not determine the correct answer.")
if __name__ == "__main__":
    # Check if running in a headless environment
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Running in headless mode.")
    else:
        root = tk.Tk()
        app = MathQuizApp(root)
        root.mainloop()