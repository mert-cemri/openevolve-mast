'''
Main application file for the econometrics multiple-choice question GUI.
'''
import tkinter as tk
from tkinter import messagebox
import os
class MainApp:
    def __init__(self, root):
        '''
        Initializes the main application with a question and answer options.
        '''
        self.root = root
        self.root.title("Econometrics Quiz")
        # Question and answer options
        self.question = "What are the dimensions of \\(\\hat{u}^t \\hat{u}\\)?"
        self.options = [
            "T x k",
            "T x 1",
            "k x 1",
            "1 x 1"
        ]
        self.correct_answer_index = 3  # The correct answer is "1 x 1"
        # Create the question frame
        self.create_question_frame()
    def create_question_frame(self):
        '''
        Creates the question and answer options in the GUI.
        '''
        question_label = tk.Label(self.root, text=self.question, wraplength=400, justify="left")
        question_label.pack(pady=10)
        self.var = tk.IntVar()
        self.var.set(-1)  # No selection initially
        for idx, option in enumerate(self.options):
            radio_button = tk.Radiobutton(self.root, text=option, variable=self.var, value=idx)
            radio_button.pack(anchor="w")
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Checks the user's selected answer and displays the correct answer.
        '''
        selected_index = self.var.get()
        if selected_index == -1:
            messagebox.showwarning("Selection Error", "Please select an answer.")
        elif selected_index == self.correct_answer_index:
            self.display_result("Correct! The answer is (3).")
        else:
            self.display_result(f"Incorrect. The correct answer is (3).")
    def display_result(self, message):
        '''
        Displays the result of the user's selection.
        '''
        messagebox.showinfo("Result", message)
if __name__ == "__main__":
    # Check if DISPLAY is set, if not, set it for virtual display
    if os.environ.get('DISPLAY', '') == '':
        os.environ.__setitem__('DISPLAY', ':99.0')  # Changed to :99.0 for Xvfb compatibility
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()