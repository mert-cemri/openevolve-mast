'''
Main application file for the clinical knowledge quiz.
This application uses Tkinter to create a simple GUI for a quiz question about calcium metabolism.
'''
import tkinter as tk
from tkinter import messagebox
import os
class Question:
    '''
    A class to represent a quiz question.
    Attributes:
    text : str
        The text of the question.
    options : list
        A list of answer options.
    correct_index : int
        The index of the correct answer in the options list.
    '''
    def __init__(self, text, options, correct_index):
        self.text = text
        self.options = options
        self.correct_index = correct_index
class MainApp:
    '''
    The main application class for the quiz.
    Attributes:
    root : Tk
        The root window of the Tkinter application.
    question : Question
        The quiz question to be displayed.
    selected_option : IntVar
        The currently selected answer option.
    '''
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
            1  # Correct answer index
        )
        self.selected_option = tk.IntVar()
        self.create_widgets()
    def create_widgets(self):
        '''
        Create and display the widgets for the quiz question and options.
        '''
        # Display the question
        question_label = tk.Label(self.root, text=self.question.text, wraplength=400)
        question_label.pack(pady=10)
        # Display the options as radio buttons
        for idx, option in enumerate(self.question.options):
            radio_button = tk.Radiobutton(
                self.root, 
                text=option, 
                variable=self.selected_option, 
                value=idx
            )
            radio_button.pack(anchor='w')
        # Submit button
        submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        submit_button.pack(pady=20)
    def check_answer(self):
        '''
        Check the selected answer and display a message indicating whether it is correct.
        '''
        selected_index = self.selected_option.get()
        if selected_index == self.question.correct_index:
            messagebox.showinfo("Result", "Correct! The answer is (1).")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is (1).")
if __name__ == "__main__":
    # Check if running in a headless environment and set a virtual display if necessary
    if os.environ.get('DISPLAY', '') == '':
        print('No display found. Ensure Xvfb is installed and running for a virtual display.')
    else:
        root = tk.Tk()
        app = MainApp(root)
        root.mainloop()