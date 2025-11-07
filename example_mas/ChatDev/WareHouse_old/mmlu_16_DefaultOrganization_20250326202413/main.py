'''
This script creates a GUI application using tkinter to present a multiple-choice question about clinical knowledge and checks the user's answer.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clinical Knowledge Quiz")
        # Define the question
        self.question = Question(
            "Which of the following is true of calcium metabolism?",
            [
                "Calcitonin causes a rise in plasma calcium",
                "Primary hyperparathyroidism is usually asymptomatic",
                "Vitamin D is secreted by the parathyroid glands",
                "Oliguria is a symptom of hypercalcaemia"
            ],
            1  # The correct answer index
        )
        self.selected_option = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        # Create and place the question label
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400, justify="left")
        question_label.pack(pady=10)
        # Create and place the radio buttons for options
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(
                self.root, 
                text=option, 
                variable=self.selected_option, 
                value=idx
            )
            radio_button.pack(anchor="w")
        # Create and place the submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        selected_index = self.selected_option.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (1).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (1).")
if __name__ == "__main__":
    # Check if the DISPLAY environment variable is set
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Using Xvfb for virtual display.")
        try:
            from pyvirtualdisplay import Display
            display = Display(visible=0, size=(800, 600))
            display.start()
        except ImportError:
            print("Xvfb is not installed. Please install it using 'sudo apt-get install xvfb'.")
            exit(1)
        except FileNotFoundError:
            print("Xvfb executable not found. Please ensure it is installed and accessible.")
            exit(1)
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()