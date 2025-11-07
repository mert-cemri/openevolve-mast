'''
This file contains the main application code for a GUI-based multiple-choice question app using Tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    def __init__(self, text, options, correct_index):
        '''
        Initialize a Question instance.
        :param text: The question text.
        :param options: A list of answer options.
        :param correct_index: The index of the correct answer in the options list.
        '''
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    def __init__(self, root):
        '''
        Initialize the main application window.
        :param root: The root window of the Tkinter application.
        '''
        self.root = root
        self.root.title("Moral Disputes Quiz")
        # Define the question
        self.question = Question(
            "Kant's humanity formulation of the categorical imperative makes it impermissible for us to, he argues,",
            ["sell one of our teeth.", "engage in prostitution.", "both A and B", "Neither A nor B"],
            2
        )
        self.selected_answer = tk.IntVar()
        self.display_question()
    def display_question(self):
        '''
        Display the question and answer options in the GUI.
        '''
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400)
        question_label.pack(pady=10)
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(
                self.root, text=option, variable=self.selected_answer, value=idx
            )
            radio_button.pack(anchor='w')
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer and display whether it is correct.
        '''
        selected_index = self.selected_answer.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct!")
        else:
            correct_option = self.question.options[self.question.correct_index]
            messagebox.showinfo("Result", f"Incorrect. The correct answer is: {correct_option}")
if __name__ == "__main__":
    # Check if running in a headless environment
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please run this application in an environment with a graphical display.")
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()