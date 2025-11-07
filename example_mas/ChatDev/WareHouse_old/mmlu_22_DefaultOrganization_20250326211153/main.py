'''
This file contains the main application logic for the philosophy quiz.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, text, options, correct_index):
        '''
        Initialize a Question object.
        :param text: The question text.
        :param options: A list of possible answers.
        :param correct_index: The index of the correct answer in the options list.
        '''
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window.
        :param root: The root window object.
        '''
        self.root = root
        self.root.title("Philosophy Quiz")
        # Define the question
        self.question = Question(
            "Before his conversion, what was Tolstoy surrounded by?",
            [
                "what is considered complete happiness",
                "things that no one would want",
                "what is considered heavenly bliss",
                "what is considered deep insight"
            ],
            0
        )
        # Set up the GUI components
        self.question_label = tk.Label(root, text=self.question.text)
        self.question_label.pack(pady=10)
        self.var = tk.IntVar()
        self.var.set(-1)  # No selection initially
        self.radio_buttons = []
        for idx, option in enumerate(self.question.options):
            rb = tk.Radiobutton(root, text=option, variable=self.var, value=idx)
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check if the selected answer is correct and display a message.
        '''
        selected_index = self.var.get()
        if selected_index == -1:
            messagebox.showwarning("No selection", "Please select an answer.")
        elif selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (0).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (0).")
if __name__ == "__main__":
    # Check if the DISPLAY environment variable is set
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please set the DISPLAY environment variable or run the application in a graphical environment.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()